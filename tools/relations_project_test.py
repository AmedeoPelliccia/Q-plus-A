# Generated 2026-11-13 - relations_project_test.py (0.2.0)
"""Tests of tools/relations_project.py on the eWTW pilot. Run from the repository root:

    python3 tools/relations_project_test.py

Each test copies the relations and the KNOT register to a temporary folder, changes one input
and expects the matching result.
"""
import datetime
import pathlib
import shutil
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import relations_project as rp  # noqa: E402

MODEL = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW")
REL = MODEL / "01-02-01-01-01-03_REL_Architecture-Relations"
REG = MODEL / "01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
TAX = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_S-ATLAS")
SRC, ESS = "electric power for propulsion", "essential electrical power"


class RelationsProject(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.rel, self.reg = self.tmp / "relations", self.tmp / "register"
        shutil.copytree(REL, self.rel)
        shutil.copytree(REG, self.reg)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def edit(self, path, change):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        change(doc)
        path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")

    def taxonomy(self, change):
        self.edit(self.rel / "taxonomy-relations.yaml", change)

    def programme(self, change):
        self.edit(self.rel / "programme-relations.yaml", change)

    def knot_file(self, topic):
        return next(self.reg.rglob(f"KNOT-EWTW-{topic}-001.yaml"))

    def knot(self, topic, change):
        self.edit(self.knot_file(topic), lambda d: change(d["knot"]))

    def run_tool(self, mode=None):
        return rp.run(self.rel, self.reg, TAX, mode=mode, models_root=MODEL.parent)

    def projection(self, role):
        tax, prog, knots, bad = rp.load(self.rel, self.reg)
        self.assertEqual(bad + rp.validate(tax, prog, knots, rp.titles(TAX), rp.models(MODEL.parent)), [])
        return rp.project(tax, prog, knots, role, "eWTW")

    def fails(self, fragment):
        bad, lines = self.run_tool()
        self.assertTrue(any(fragment in b for b in bad), f"expected {fragment!r} in {bad}")
        self.assertEqual(len(lines), 1, "no projection is printed after a failure")

    def status(self, projection):
        return {r["members"]: r["status"] for r in projection["rows"]}

    # the pilot as committed
    def test_source_options_match_the_register(self):
        p = self.projection(SRC)
        self.assertEqual((p["only_projected"], p["only_registered"]), ([], []))
        self.assertEqual(sorted(p["registered"].values()), ["A", "B", "C"])
        self.assertIn("PROVISIONAL", self.status(p)[("075",)])

    def test_prerequisites_agree_with_the_register(self):
        self.assertEqual((self.projection(SRC)["derived"], self.projection(SRC)["consistent"]), (["KNOT-EWTW-NRG-001"], True))
        p = self.projection(ESS)
        self.assertEqual(p["derived"], ["KNOT-EWTW-NRG-001", "KNOT-EWTW-SRC-001", "KNOT-EWTW-STO-001"])
        self.assertTrue(p["consistent"])

    def test_essential_power_candidates_are_proposals(self):
        p = self.projection(ESS)
        self.assertEqual((p["registered"], p["dead"]), ({}, {}))
        self.assertEqual([m for m, s in self.status(p).items() if s == "open"], [("024-360",), ("049",), ("068",), ("074",)])
        self.assertEqual(p["unaddressed"][0]["name"], "ram-air turbine")

    def test_candidate_chapters_outside_the_knot_scope(self):
        self.assertEqual((self.projection(SRC)["outside"], self.projection(ESS)["outside"]), ([], ["068", "074"]))

    def test_every_programme_relation_is_counted(self):
        bad, lines = self.run_tool()
        self.assertEqual(bad, [])
        self.assertEqual(lines[0], "2 alternative sets, 5 taxonomy relations, 5 programme relations; rule failures: none")

    def test_committed_readme_is_current(self):
        self.assertEqual(rp.run(REL, REG, TAX, mode="check")[0], [])

    # programme inputs
    def test_exclusion_covers_what_lies_under_it(self):
        self.taxonomy(lambda d: d["alternatives"][0].update(members=["068", "074", "075-100"]))
        self.assertTrue(self.status(self.projection(SRC))[("075-100",)].startswith("excluded"))

    def test_combination_removed(self):
        self.programme(lambda d: d.update(combinations=[]))
        self.assertEqual(self.projection(SRC)["only_registered"], [("068", "074")])

    def test_exclusion_removed(self):
        self.programme(lambda d: d.update(exclusions=[]))
        self.assertEqual(self.status(self.projection(SRC))[("075",)], "open")

    def test_combination_with_an_excluded_member_goes_to_review(self):
        self.programme(lambda d: d["combinations"][0].update(members=["068", "075"]))
        self.assertTrue(self.status(self.projection(SRC))[("068", "075")].startswith("review"))

    def test_exclusion_needs_a_recorded_ruling(self):
        self.programme(lambda d: d["exclusions"][0].update(ruling="KNOT-EWTW-NRG-001#R9"))
        self.fails("fuel-cells-from-ewtw: ruling KNOT-EWTW-NRG-001#R9 is not in the register")

    def test_combination_outside_the_alternatives(self):
        self.programme(lambda d: d["combinations"][0].update(members=["062", "068"]))
        self.fails("turbogenerators-with-batteries: members must be")

    def test_assignment_object_is_a_model_of_the_programme(self):
        self.programme(lambda d: d["assignments"][0]["object"].update(ns="aircraft"))
        self.fails("liquid-hydrogen-to-bwb-q100: the object is a model of the programme")
        self.programme(lambda d: d["assignments"][0].update(object={"ns": "model", "id": "BWB-Q200"}))
        self.fails("liquid-hydrogen-to-bwb-q100: the object is a model of the programme")

    def test_assignment_subject_is_an_address_or_a_known_reference(self):
        self.programme(lambda d: d["assignments"][0].update(subject={"ns": "colour", "id": "blue"}))
        self.fails("liquid-hydrogen-to-bwb-q100: the subject is an S-ATLAS address")
        self.programme(lambda d: d["assignments"][0].pop("subject"))
        self.fails("liquid-hydrogen-to-bwb-q100: the subject is an S-ATLAS address")

    def test_decision_link_needs_a_key(self):
        self.programme(lambda d: d["decided-by"][0].pop("key"))
        self.fails("decided-by: missing or duplicate key")

    def test_one_deciding_knot_for_a_role_and_a_model(self):
        self.programme(lambda d: d["decided-by"].append(dict(d["decided-by"][0], key="second-link", knot="KNOT-EWTW-NRG-001")))
        self.fails("second-link: electric power for propulsion for eWTW already has a deciding KNOT")

    def test_withdrawn_decision_link_leaves_the_role_free(self):
        def replace(d):
            d["decided-by"].append(dict(d["decided-by"][0], key="second-link"))
            d["decided-by"][0]["state"] = "WITHDRAWN"
        self.programme(replace)
        self.assertEqual(self.projection(SRC)["knot"], "KNOT-EWTW-SRC-001")

    def test_decision_link_to_an_unknown_model(self):
        self.programme(lambda d: d["decided-by"][0].update(model="eWTV"))
        self.fails("electric-propulsion-power-decided-by-src: eWTV is not a model of the programme")

    def test_decision_link_outside_the_effectivity_of_the_knot(self):
        self.programme(lambda d: d["decided-by"][0].update(model="BWB-Q100"))
        self.fails("the effectivity of KNOT-EWTW-SRC-001 does not include BWB-Q100")

    # taxonomy inputs
    def test_unknown_address(self):
        self.taxonomy(lambda d: d["alternatives"][0].update(members=["068", "074", "999"]))
        self.fails("999 is not an S-ATLAS address")

    def test_relation_holds_at_its_recorded_address_only(self):
        self.taxonomy(lambda d: d["alternatives"][0].update(members=["068", "074", "074-000", "075"]))
        row = next(r for r in self.projection(SRC)["rows"] if r["members"] == ("074-000",))
        self.assertEqual((row["requires"], [key for key, _ in row["elements"]]), ([], ["propulsive-battery-installation"]))

    def test_unsorted_members(self):
        self.taxonomy(lambda d: d["alternatives"][0].update(members=["074", "068", "075"]))
        self.fails("electric-propulsion-power-source: members must be")

    def test_members_that_are_not_a_list_of_addresses(self):
        self.taxonomy(lambda d: d["alternatives"][0].update(members="068"))
        self.fails("electric-propulsion-power-source: members must be")
        self.taxonomy(lambda d: d["alternatives"][0].update(members=[["068"], {"a": 1}]))
        self.fails("electric-propulsion-power-source: members must be")

    def test_withdrawn_set_is_replaced(self):
        def replace(d):
            d["alternatives"][0]["state"] = "WITHDRAWN"
            d["alternatives"].append(dict(d["alternatives"][0], key="replacement-set", members=["068", "074"], state="PROPOSED"))
        self.taxonomy(replace)
        self.assertEqual(sorted(self.status(self.projection(SRC))), [("068",), ("068", "074"), ("074",)])

    def test_withdrawn_set_without_a_replacement(self):
        self.taxonomy(lambda d: d["alternatives"][0].update(state="WITHDRAWN"))
        self.fails("role electric power for propulsion has no alternatives set")

    def test_ratified_without_a_checked_source(self):
        self.taxonomy(lambda d: d["relations"][1].update(state="RATIFIED"))
        self.fails("turbogenerator-requires-carrier-delivery: ratified without a checked source")

    def test_source_checked_is_a_date(self):
        for value in ("yesterday", "2026-13-40", 20261112):
            self.taxonomy(lambda d: d["relations"][0].update(source_checked=value))
            self.fails("propulsion-storage-requires-thermal-management: source_checked is not a date")

    def test_yaml_date_is_accepted(self):
        self.taxonomy(lambda d: d["relations"][0].update(state="RATIFIED", source_checked=datetime.date(2026, 11, 12)))
        self.assertIn("source_checked: 2026-11-12\n", (self.rel / "taxonomy-relations.yaml").read_text(encoding="utf-8"))
        self.assertEqual(self.run_tool()[0], [])

    def test_symmetric_relation_stored_in_order(self):
        self.taxonomy(lambda d: next(r for r in d["relations"] if r["relation"] == "interfaces-with").update(subject="076", object="074"))
        self.fails("a symmetric relation is stored once")

    def test_duplicate_key(self):
        self.taxonomy(lambda d: d["relations"][1].update(key=d["relations"][0]["key"]))
        self.fails("missing or duplicate key")

    # inputs that cannot be read
    def test_missing_file(self):
        (self.rel / "taxonomy-relations.yaml").unlink()
        self.fails("taxonomy-relations.yaml: cannot be read as YAML")

    def test_invalid_yaml(self):
        (self.rel / "programme-relations.yaml").write_text("decided-by: [", encoding="utf-8")
        self.knot_file("NRG").write_text("knot: [1", encoding="utf-8")
        self.fails("programme-relations.yaml: cannot be read as YAML")
        self.fails("KNOT-EWTW-NRG-001.yaml: cannot be read as YAML")

    def test_section_that_is_not_a_list_of_records(self):
        self.programme(lambda d: d.update(exclusions="none"))
        self.fails("programme-relations.yaml: exclusions must be a list of records")

    def test_register_record_the_projection_cannot_read(self):
        self.knot("SRC", lambda k: k.update(options="A"))
        self.fails("KNOT-EWTW-SRC-001: not a record the projection can read")

    # register inputs
    def test_knot_recorded_in_two_files(self):
        shutil.copy(self.knot_file("NRG"), self.reg / "053_Fuselage")
        self.fails("KNOT-EWTW-NRG-001: recorded in more than one file")

    def test_file_name_differs_from_the_knot_id(self):
        self.knot_file("NRG").rename(self.reg / "000_General" / "KNOT-EWTW-NRX-001.yaml")
        self.fails("KNOT-EWTW-NRX-001.yaml: no `knot` record whose knot_id is the file name")

    def test_missing_prerequisite_is_reported(self):
        self.knot("ESS", lambda k: k.update(depends_on=[]))
        self.assertFalse(self.projection(ESS)["consistent"])

    def test_state_of_an_exclusion_follows_its_ruling(self):
        def complete(k):
            k["rulings"][0].update(rationale="stated", evidence=[{"view": "EBS", "ref": "x"}], state="COMPLETE")
        self.knot("NRG", complete)
        self.assertIn("COMPLETE", self.status(self.projection(SRC))[("075",)])

    def test_rejected_option_no_longer_stands(self):
        def reject(k):
            for option in k["options"]:
                if option["id"] in ("B", "C"):
                    option["state"] = "rejected"
        self.knot("SRC", reject)
        p = self.projection(SRC)
        self.assertEqual((p["registered"], p["only_projected"]), ({("074",): "A"}, [("068",), ("068", "074")]))
        self.assertEqual(next(r for r in p["rows"] if r["members"] == ("068",))["elements"], [])
        self.assertIn("`068` (option B is rejected)", "\n".join(rp.render(p, rp.titles(TAX))))
        self.assertNotIn("KNOT-EWTW-SRC-001", self.projection(ESS)["derived"])

    # the generated section of the README
    def test_stale_readme_is_reported_then_rewritten(self):
        self.programme(lambda d: d.update(exclusions=[]))
        self.assertIn("README.md: the generated section differs", self.run_tool("check")[0][0])
        self.assertEqual(self.run_tool("write")[0], [])
        self.assertEqual(self.run_tool("check")[0], [])
        self.assertIn("| `075` Fuel Cell", (self.rel / "README.md").read_text(encoding="utf-8"))

    def test_readme_without_markers(self):
        readme = self.rel / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8").replace(rp.BEGIN, ""), encoding="utf-8")
        self.assertIn("README.md: the markers", self.run_tool("check")[0][0])

    # output
    def test_control_characters_are_made_visible(self):
        self.taxonomy(lambda d: d["alternatives"][1]["unaddressed"][0].update(name="turbine\x1b[2J\nOptions: none"))
        bad, lines = self.run_tool()
        self.assertEqual(bad, [])
        self.assertNotIn("\x1b", "\n".join(lines))
        self.assertIn("No S-ATLAS address: turbine\\x1b[2J\\x0aOptions: none", "\n".join(lines))


if __name__ == "__main__":
    unittest.main()
