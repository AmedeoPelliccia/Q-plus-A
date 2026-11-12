# Generated 2026-11-13 - knot_check_test.py (0.1.1)
"""Tests of tools/knot_check.py on the eWTW KNOT register. Run from the repository root:

    python3 tools/knot_check_test.py

Each test copies the register to a temporary folder, breaks one rule and expects the matching failure.
"""
import pathlib
import shutil
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import knot_check  # noqa: E402

MODEL = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW")
REG = MODEL / "01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
PBS = MODEL / "01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure"
TAX = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_S-ATLAS")


class KnotCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.reg = self.tmp / "register"
        shutil.copytree(REG, self.reg)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def path(self, topic):
        return next(self.reg.rglob(f"KNOT-EWTW-{topic}-001.yaml"))

    def edit(self, topic, change):
        p = self.path(topic)
        doc = yaml.safe_load(p.read_text(encoding="utf-8"))
        change(doc["knot"])
        p.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")

    def option(self, knot, oid):
        return next(o for o in knot["options"] if o["id"] == oid)

    def fails(self, fragment):
        bad, _, _ = knot_check.check(self.reg, TAX, PBS)
        self.assertTrue(any(fragment in b for b in bad), f"expected {fragment!r} in {bad}")

    def test_register_passes(self):
        bad, prov, lines = knot_check.check(self.reg, TAX, PBS)
        self.assertEqual(bad, [])
        self.assertEqual(prov, ["`NRG` R1"])
        self.assertTrue(lines[0].startswith("11 KNOTs, 31 KNUs"))

    def test_missing_required_field(self):
        self.edit("LUG", lambda k: k.pop("criteria"))
        self.fails("KNOT-EWTW-LUG-001 missing ['criteria']")

    def test_wrong_folder(self):
        p = self.path("TSI")
        p.rename(self.reg / "000_General" / p.name)
        self.fails("KNOT-EWTW-TSI-001 filed under 000, expected 053")

    def test_knot_recorded_in_two_files(self):
        shutil.copy(self.path("NRG"), self.reg / "053_Fuselage")
        self.fails("KNOT-EWTW-NRG-001 recorded in more than one file")

    def test_scored_without_criteria(self):
        self.edit("DFN", lambda k: self.option(k, "A").update(state="rejected"))
        self.fails("KNOT-EWTW-DFN-001 scored without criteria or maturity")

    def test_ruled_on_provisional_ruling(self):
        self.edit("NRG", lambda k: k.update(resolution="RULED"))
        self.fails("KNOT-EWTW-NRG-001 ruled on a provisional ruling")

    def test_provisional_ruling_with_effects(self):
        effect = {"view": "ReqBS", "action": "create", "ref": None, "description": "Scope requirement"}
        self.edit("NRG", lambda k: k["rulings"][0]["effects"].append(effect))
        self.fails("KNOT-EWTW-NRG-001 R1 provisional ruling with authorised effects")

    def test_gate_to_missing_pbs_node(self):
        def change(k):
            next(a for a in k["affects"] if a.get("relation") == "gates")["ref"] = "eWTW-PBS-024-900"
        self.edit("ESS", change)
        self.fails("KNOT-EWTW-ESS-001 invalid PBS gate eWTW-PBS-024-900")

    def test_invalid_effectivity(self):
        self.edit("KEL", lambda k: k.update(effectivity=[]))
        self.fails("KNOT-EWTW-KEL-001 invalid effectivity")

    def test_element_created_twice(self):
        def change(k):
            item = self.option(k, "A")["pbs_footprint"][0]
            item["action"] = "create"
            item.pop("owner")
        self.edit("STO", change)
        self.fails("propulsive-battery-installation created by")

    def test_use_without_owner(self):
        self.edit("STO", lambda k: self.option(k, "B")["pbs_footprint"][0].pop("owner"))
        self.fails("KNOT-EWTW-STO-001 option B uses propulsive-battery-installation without its owner")

    def test_use_under_another_chapter(self):
        self.edit("PRP", lambda k: self.option(k, "B")["pbs_footprint"][0].update(taxonomy="062"))
        self.fails("KNOT-EWTW-PRP-001 option B files turbogenerator-installation under 062")

    def test_owner_of_element_nobody_creates(self):
        self.edit("DFN", lambda k: self.option(k, "A")["pbs_footprint"][0].update(owner="KNOT-EWTW-NRG-001"))
        self.fails("names owner KNOT-EWTW-NRG-001 for dorsal-fin-root-fairing")

    def test_conformity_claim(self):
        self.edit("TSI", lambda k: k.update(context=k["context"] + " The fairing is compliant."))
        self.fails("conformity claim")


if __name__ == "__main__":
    unittest.main()
