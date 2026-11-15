# Generated 2026-11-14 - conops_check_test.py (0.1.0)
"""Tests of tools/conops_check.py on the concept of operations of the environmental control system of the eWTW.
Run from the repository root:

    python3 tools/conops_check_test.py

Each test copies the concept and the KNOT register to a temporary folder, changes one input and expects the
matching result. The counts of the committed input are made again by hand.
"""
import pathlib
import shutil
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import conops_check as cc  # noqa: E402

MODEL = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW")
REG = MODEL / "01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
SBS = MODEL / "01-02-01-01-01-01_SBS_System-Breakdown-Structure"
ECS = REG / "000_General" / "evidence" / "CONOPS-EWTW-ECS-001"
TAX = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_S-ATLAS")


class ConopsCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.ecs, self.reg = self.tmp / "conops", self.tmp / "register"
        shutil.copytree(ECS, self.ecs)
        shutil.copytree(REG, self.reg)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def edit(self, change):
        path = self.ecs / "conops.yaml"
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        change(doc["conops"])
        path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")

    def item(self, c, section, key):
        return next(i for i in c[section] if i["key"] == key)

    def run_tool(self, mode=None):
        return cc.run(self.ecs, self.reg, TAX, mode=mode, sbs=SBS)

    def fails(self, fragment):
        bad, lines = self.run_tool()
        self.assertTrue(any(fragment in b for b in bad), f"expected {fragment!r} in {bad}")
        self.assertEqual(len(lines), 1, "a failing run prints only its first line")

    # the concept as committed
    def test_committed_concept_passes_and_its_readme_is_current(self):
        bad, lines = self.run_tool("check")
        self.assertEqual(bad, [])
        self.assertIn("### Open inputs", lines)

    def test_counts_are_those_of_the_input(self):
        c = yaml.safe_load((ECS / "conops.yaml").read_text(encoding="utf-8"))["conops"]
        by = {}
        for section in ("functions", "supplies", "phases", "cases"):
            for i in c[section]:
                by[i["basis"]] = by.get(i["basis"], 0) + 1
        self.assertEqual(by, {"declared": 7, "assumption": 2, "proposed": 13, "open": 4})
        _, lines = self.run_tool()
        self.assertEqual(lines[0], "CONOPS-EWTW-ECS-001 0.1.1 for KNOT-EWTW-SRC-001: 7 phases, 8 functions, 4 supplies, 7 cases, 8 open inputs; "
                                   "26 statements — 7 declared, 2 from an analysis, 13 proposed here, 4 open; no figure; rule failures: none")

    def test_essential_case_sheds_the_packs_and_keeps_pressure_control(self):
        _, lines = self.run_tool()
        row = next(l for l in lines if l.startswith("| `normal-generation-lost` |"))
        cells = [x.strip() for x in row.strip("|").split("|")]
        self.assertEqual(cells[4:7], ["`pressure-control` · `equipment-cooling`", "`essential`", "`fresh-air` · `cooling` · `recirculation` · `distribution`"])
        self.assertEqual(cells[7], "assumption")

    def test_generated_section_is_checked_and_written(self):
        self.edit(lambda c: self.item(c, "phases", "cruise").update(text="Cruise at the altitude to be decided"))
        bad, _ = self.run_tool("check")
        self.assertEqual(bad, ["README.md: the generated section differs from the output; run again with --write"])
        self.assertEqual(self.run_tool("write")[0], [])
        self.assertEqual(self.run_tool("check")[0], [])
        self.assertIn("Cruise at the altitude to be decided", (self.ecs / "README.md").read_text(encoding="utf-8"))

    # form
    def test_no_figure(self):
        self.edit(lambda c: self.item(c, "functions", "cooling").update(power_kw=190))
        self.fails("a concept of operations carries no figure; 1 found")

    def test_basis_is_required(self):
        self.edit(lambda c: self.item(c, "phases", "climb").update(basis="measured"))
        self.fails("phases climb: basis is one of declared, assumption, proposed, open")

    def test_declared_names_its_source(self):
        self.edit(lambda c: self.item(c, "supplies", "turbogenerators").pop("source"))
        self.fails("supplies turbogenerators: a statement that is declared names its source")

    def test_open_names_who_decides(self):
        self.edit(lambda c: self.item(c, "cases", "turbogenerator-lost").update(decided_by="KNOT-EWTW-XXX-001"))
        self.fails("cases turbogenerator-lost: an open statement names the KNOT that decides it, or `authority`")

    def test_open_input_names_who_decides_and_what_it_blocks(self):
        self.edit(lambda c: self.item(c, "open_inputs", "cruise-point").update(decided_by=None))
        self.fails("open_inputs cruise-point: an open input names what it blocks and the KNOT that decides it, or `authority`")
        self.edit(lambda c: self.item(c, "open_inputs", "cruise-point").update(decided_by="KNOT-EWTW-CRZ-001", blocks=["landing"]))
        self.fails("open_inputs cruise-point: landing is not a key of this document")

    # references
    def test_phase_runs_known_functions_on_known_supplies(self):
        self.edit(lambda c: self.item(c, "phases", "cruise")["functions"].append("humidification"))
        self.fails("phases cruise: humidification is not a function")
        self.edit(lambda c: self.item(c, "phases", "cruise").update(functions=["cooling"], supply=["bleed-air"]))
        self.fails("phases cruise: bleed-air is not a supply")

    def test_case_cannot_keep_and_shed_the_same_function(self):
        self.edit(lambda c: self.item(c, "cases", "smoke")["keeps"].append("recirculation"))
        self.fails("cases smoke: recirculation is both kept and shed")

    def test_function_and_supply_are_used(self):
        self.edit(lambda c: c["functions"].append({"key": "humidification", "text": "Humidify the cabin air", "taxonomy": "021", "basis": "proposed"}))
        self.fails("function humidification runs in no phase and is kept in no case")
        self.edit(lambda c: (c["functions"].pop(), c["supplies"].append({"key": "ram-turbine", "text": "A ram-air turbine", "taxonomy": "024", "basis": "proposed"})))
        self.fails("supply ram-turbine supplies no phase and no case")

    def test_bindings_resolve(self):
        self.edit(lambda c: c["bindings"]["pbs"].append("eWTW-PBS-021-900"))
        self.fails("binding eWTW-PBS-021-900 is not on disk")
        self.edit(lambda c: c["bindings"].update(pbs=["eWTW-PBS-021-000"], functions=["eWTW-FBS-70-99"]))
        self.fails("binding eWTW-FBS-70-99 is not on disk")

    def test_taxonomy_of_a_function_resolves(self):
        self.edit(lambda c: self.item(c, "functions", "ram-air").update(taxonomy="021-999"))
        self.fails("functions ram-air: taxonomy 021-999 is not an S-ATLAS address")

    def test_serves_a_knu_of_its_knot(self):
        self.edit(lambda c: c.update(serves="KNU-EWTW-SRC-001-09"))
        self.fails("KNU-EWTW-SRC-001-09 is not a KNU of KNOT-EWTW-SRC-001")
        self.edit(lambda c: c.update(knot="KNOT-EWTW-ECS-001"))
        self.fails("KNOT-EWTW-ECS-001 is not a KNOT of the register")

    def test_keys_are_unique_across_sections(self):
        self.edit(lambda c: c["open_inputs"].append({"key": "cruise", "text": "Again", "blocks": ["climb"], "decided_by": "authority"}))
        self.fails("key cruise used in more than one section")


if __name__ == "__main__":
    unittest.main()
