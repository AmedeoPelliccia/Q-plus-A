# Generated 2026-11-12 - relations_project_test.py (0.1.0)
"""Tests of tools/relations_project.py on the eWTW pilot. Run from the repository root:

    python3 tools/relations_project_test.py

Each test copies the relations and the KNOT register to a temporary folder, changes one input
and expects the matching result.
"""
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

    def knot(self, topic, change):
        self.edit(next(self.reg.rglob(f"KNOT-EWTW-{topic}-001.yaml")), lambda d: change(d["knot"]))

    def projection(self, role):
        tax, prog, knots = rp.load(self.rel, self.reg)
        self.assertEqual(rp.validate(tax, prog, knots, rp.titles(TAX)), [])
        return rp.project(tax, prog, knots, role, "eWTW")

    def fails(self, fragment):
        bad, _ = rp.run(self.rel, self.reg, TAX)
        self.assertTrue(any(fragment in b for b in bad), f"expected {fragment!r} in {bad}")

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
        self.assertEqual(p["registered"], {})
        self.assertEqual([m for m, s in self.status(p).items() if s == "open"], [("024-360",), ("049",), ("068",), ("074",)])
        self.assertEqual(p["unaddressed"][0]["name"], "ram-air turbine")

    def test_candidate_chapters_outside_the_knot_scope(self):
        self.assertEqual((self.projection(SRC)["outside"], self.projection(ESS)["outside"]), ([], ["068", "074"]))

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

    def test_ratified_without_a_checked_source(self):
        self.taxonomy(lambda d: d["relations"][1].update(state="RATIFIED"))
        self.fails("turbogenerator-requires-carrier-delivery: ratified without a checked source")

    def test_symmetric_relation_stored_in_order(self):
        self.taxonomy(lambda d: next(r for r in d["relations"] if r["relation"] == "interfaces-with").update(subject="076", object="074"))
        self.fails("a symmetric relation is stored once")

    def test_duplicate_key(self):
        self.taxonomy(lambda d: d["relations"][1].update(key=d["relations"][0]["key"]))
        self.fails("missing or duplicate key")

    # register inputs
    def test_missing_prerequisite_is_reported(self):
        self.knot("ESS", lambda k: k.update(depends_on=[]))
        self.assertFalse(self.projection(ESS)["consistent"])

    def test_state_of_an_exclusion_follows_its_ruling(self):
        def complete(k):
            k["rulings"][0].update(rationale="stated", evidence=[{"view": "EBS", "ref": "x"}], state="COMPLETE")
        self.knot("NRG", complete)
        self.assertIn("COMPLETE", self.status(self.projection(SRC))[("075",)])


if __name__ == "__main__":
    unittest.main()
