# Generated 2026-11-14 - knot_check_test.py (0.1.5)
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

MATURITY = {"id": "Q1", "element": "Essential source", "taxonomy": "024", "options": ["A"], "decision": "REV-B_RELEASED", "required": 6,
            "evidence": "None on record", "level": None, "source": "Test", "state": "APPROVED"}


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
        self.assertEqual(prov, [], "ruling R1 of the energy carrier was completed on 2026-11-14")
        self.assertTrue(lines[0].startswith("17 KNOTs, 50 KNUs"))
        self.assertIn("Control: `CAD`", lines)
        self.assertIn("Obligation: `CRT`", lines)

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

    def test_scored_on_criteria_that_are_only_proposed(self):
        self.edit("ESS", lambda k: k.update(resolution="RULED", maturity_required=[dict(MATURITY)]))
        self.fails("KNOT-EWTW-ESS-001 scored without criteria or maturity")

    def test_scored_on_maturity_that_is_only_proposed(self):
        approve = lambda k: [c.update(state="APPROVED") for c in k["criteria"]]
        self.edit("ESS", lambda k: (approve(k), k.update(resolution="RULED", maturity_required=[dict(MATURITY, state="PROPOSED")])))
        self.fails("KNOT-EWTW-ESS-001 scored without criteria or maturity")
        self.edit("ESS", lambda k: k.update(maturity_required=[dict(MATURITY)]))
        self.assertFalse(any("scored without criteria or maturity" in b for b in knot_check.check(self.reg, TAX, PBS)[0]))

    def test_invalid_maturity_record(self):
        for change in ({"required": 10}, {"level": 0}, {"options": ["Z"]}, {"taxonomy": "999"}, {"state": "AGREED"}, {"evidence": ""}):
            self.edit("ESS", lambda k: k.update(maturity_required=[dict(MATURITY, **change)]))
            self.fails("KNOT-EWTW-ESS-001 invalid maturity record Q1")

    def test_invalid_criterion(self):
        self.edit("ESS", lambda k: k["criteria"][0].update({"class": "preferred"}))
        self.fails("KNOT-EWTW-ESS-001 invalid criterion M1")

    def provisional(self, k):
        k["rulings"][0].update(rationale=None, rationale_recorded=None, evidence=[], state="PROVISIONAL")

    def test_ruled_on_provisional_ruling(self):
        self.edit("NRG", lambda k: (self.provisional(k), k.update(resolution="RULED")))
        self.fails("KNOT-EWTW-NRG-001 ruled on a provisional ruling")

    def test_provisional_ruling_with_effects(self):
        effect = {"view": "ReqBS", "action": "create", "ref": None, "description": "Scope requirement"}
        self.edit("NRG", lambda k: (self.provisional(k), k["rulings"][0]["effects"].append(effect)))
        self.fails("KNOT-EWTW-NRG-001 R1 provisional ruling with authorised effects")

    def test_completed_ruling_without_evidence_is_a_state_error(self):
        self.edit("NRG", lambda k: k["rulings"][0].update(evidence=[]))
        self.fails("KNOT-EWTW-NRG-001 R1 state")

    # rule 6: a KNOT deferred to the choice of another
    def test_deferred_knots_keep_their_gates(self):
        _, _, lines = knot_check.check(self.reg, TAX, PBS)
        self.assertIn("| `KNOT-EWTW-NRG-001` | Energy carrier | `decision-anchor` | `000` | DEFERRED | 7 | `STK_SE` |", lines)
        self.assertTrue(any(l.startswith("| `eWTW-PBS-053-900-000` | `KNOT-EWTW-NRG-001` | DEFERRED |") for l in lines))
        self.assertTrue(any(l.startswith("| `eWTW-PBS-068-000` | `KNOT-EWTW-SRC-001` | DEFERRED |") for l in lines))

    def test_deferred_needs_another_knot(self):
        self.edit("NRG", lambda k: k.update(closed_with=[]))
        self.fails("KNOT-EWTW-NRG-001 deferred without another KNOT in closed_with")

    def test_deferred_needs_a_complete_ruling(self):
        self.edit("SRC", self.provisional)
        self.fails("KNOT-EWTW-SRC-001 deferred without a complete ruling")

    def test_deferring_scores_nothing(self):
        self.edit("SRC", lambda k: self.option(k, "B").update(state="retained"))
        self.fails("KNOT-EWTW-SRC-001 scored without criteria or maturity")

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
