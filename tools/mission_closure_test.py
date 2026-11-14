# Generated 2026-11-14 - mission_closure_test.py (0.1.0)
"""Tests of tools/mission_closure.py on the candidate missions of the eWTW. Run from the repository root:

    python3 tools/mission_closure_test.py

Each test copies the analysis and the KNOT register to a temporary folder, changes one input
and expects the matching result. The equations of the committed input are computed again by hand.
"""
import math
import pathlib
import shutil
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import mission_closure as mc  # noqa: E402

MODEL = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW")
REG = MODEL / "01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
MSN = REG / "000_General" / "evidence" / "MSN-EWTW-NRG-001"
G = 9.80665


class MissionClosure(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.msn, self.reg = self.tmp / "analysis", self.tmp / "register"
        shutil.copytree(MSN, self.msn)
        shutil.copytree(REG, self.reg)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def edit(self, path, key, change):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        change(doc[key])
        path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")

    def analysis(self, change):
        self.edit(self.msn / "missions.yaml", "analysis", change)

    def knot(self, change):
        self.edit(next(self.reg.rglob("KNOT-EWTW-NRG-001.yaml")), "knot", change)

    def read(self):
        return yaml.safe_load((self.msn / "missions.yaml").read_text(encoding="utf-8"))["analysis"]

    def model(self, which="nominal"):
        a = self.read()
        return mc.Model(a, which), {m["key"]: m for m in a["missions"]}

    def run_tool(self, mode=None):
        return mc.run(self.msn, self.reg, mode=mode)

    def fails(self, fragment):
        bad, lines = self.run_tool()
        self.assertTrue(any(fragment in b for b in bad), f"expected {fragment!r} in {bad}")
        self.assertEqual(len(lines), 1, "no screening is printed after a failure")

    # the analysis as committed
    def test_committed_analysis_passes_and_its_readme_is_current(self):
        bad, lines = mc.run(MSN, REG, mode="check")
        self.assertEqual(bad, [])
        self.assertTrue(lines[0].endswith("3 candidate missions, 4 pack levels; 29 figures, 21 of them assumptions; rule failures: none"), lines[0])

    def test_distance_flown_by_hand(self):
        m, missions = self.model()
        climb = 18 * (7600 * 0.5 + (500 / 3.6) ** 2 / (2 * G)) / 1000
        self.assertAlmostEqual(m.climb_km, climb)
        self.assertAlmostEqual(m.reserve_km, 185 + 400 * 30 / 60)
        self.assertAlmostEqual(m.equivalent_km(missions["S"]), 500 * 1.05 + climb + 385)
        self.assertAlmostEqual(m.equivalent_km(missions["M"]), 1100 * 1.05 + climb + 385)

    def test_option_b_by_hand(self):
        m, missions = self.model()
        km = m.equivalent_km(missions["M"])
        fuel = 1 - math.exp(-km * 1000 * G / (0.35 * 0.90 * 0.85 * 18 * 43.0e6))
        self.assertAlmostEqual(m.option_b(missions["M"]), 9500 / (1 - 0.60 - fuel))
        self.assertAlmostEqual(m.option_b(missions["M"]) / 1000, 29.1, places=1)

    def test_option_a_by_hand(self):
        m, missions = self.model()
        km = m.equivalent_km(missions["S"])
        per_kg = 1000 * 3600 * 0.72 * 0.90 * 0.85 * 18 / (1000 * G)          # km flown for each kg of battery in a kg of aircraft, at 1,000 Wh/kg
        self.assertAlmostEqual(m.option_a(missions["S"], 1000), 9500 / (1 - 0.52 - km / per_kg))
        self.assertAlmostEqual(m.pack_needed_a(missions["S"]), km / (per_kg / 1000) / (1 - 0.52 - 9500 / 60000))
        self.assertAlmostEqual(m.pack_needed_a(missions["S"]), 851, delta=1)
        self.assertIsNone(m.option_a(missions["S"], 480.9), "the energy and the empty aircraft leave no payload")

    def test_option_c_by_hand(self):
        m, missions = self.model()
        trip, km_per = m.trip_km(missions["S"]), 650 * 3600 * 0.72 * 0.90 * 0.85 * 18 / (1000 * G)
        fuel = 1 - math.exp(-(0.75 * trip + 385) * 1000 * G / (0.35 * 0.90 * 0.85 * 18 * 43.0e6))
        self.assertAlmostEqual(m.option_c(missions["S"], 0.25, 650), 9500 / (1 - 0.61 - 0.25 * trip / km_per - fuel))

    # consistency of the equations
    def test_pack_needed_puts_the_aircraft_at_the_mass_limit(self):
        for which in mc.SETS:
            m, missions = self.model(which)
            self.assertAlmostEqual(m.option_a(missions["S"], m.pack_needed_a(missions["S"])), 60000, places=3)
            self.assertAlmostEqual(m.option_c(missions["M"], 0.25, m.pack_needed_c(missions["M"], 0.25)), 60000, places=3)

    def test_longest_trip_is_the_inverse_of_the_pack_needed(self):
        m, _ = self.model("favourable")
        trip = m.trip_within_limit_a(480.9)
        self.assertAlmostEqual(m.pack_needed_a({"range_km": trip}), 480.9, places=6)
        self.assertEqual(self.model("unfavourable")[0].trip_within_limit_a(480.9), 0.0, "the reserves alone exceed the limit")

    def test_sets_are_ordered(self):
        fav, nom, unf = (self.model(s) for s in mc.SETS)
        for key in "SML":
            self.assertLess(fav[0].pack_needed_a(fav[1][key]), nom[0].pack_needed_a(nom[1][key]))
            self.assertLess(nom[0].pack_needed_a(nom[1][key]), unf[0].pack_needed_a(unf[1][key]))
            self.assertLess(fav[0].option_b(fav[1][key]), nom[0].option_b(nom[1][key]))
            self.assertLess(nom[0].option_b(nom[1][key]), unf[0].option_b(unf[1][key]))

    def test_no_room_gives_none_and_over_the_limit_does_not_close(self):
        m, missions = self.model()
        self.assertIsNone(m.pack_needed_c(missions["X"], 0.10))
        self.assertFalse(m.closes(m.option_b(missions["X"])))
        self.assertFalse(m.closes(None))
        lines = self.run_tool()[1]
        self.assertIn("| X | 39.8 · over · none | — | — | — | — |", lines)
        self.assertIn("| S | 473 · 851 · 1419 | none | none | over | 46.0 |", lines)

    def test_fuel_burned_is_compared_in_kilograms(self):
        m, missions = self.model()
        b = m.option_b(missions["S"]) * m.fuel_fraction(m.equivalent_km(missions["S"]))
        c = m.option_c(missions["S"], 0.10, 170) * m.fuel_c(missions["S"], 0.10)
        self.assertAlmostEqual(c / b - 1, 0.34, places=2)
        self.assertIn("| S | 10% | 45 · 89 · 188 | 38.3 · 30.5 · 29.6 · 28.8 | +34% · +7% · +4% · +1% |", self.run_tool()[1])

    def test_units_are_counted_at_take_off_power(self):
        m, missions = self.model()
        power = m.option_b(missions["L"]) * 0.20
        self.assertEqual((math.ceil(power / 750), math.ceil(power / 1000)), (9, 7))
        self.assertIn("| L | 25.6 · 33.3 · 50.1 | 3813 | 6.7 | 9 | 7 |", self.run_tool()[1])

    def test_longer_final_reserve_costs_the_battery_more(self):
        before = self.model()[0].pack_needed_a(self.model()[1]["S"])
        self.analysis(lambda a: a["reserves"]["final_reserve_min"].update(value=45))
        after = self.model()[0].pack_needed_a(self.model()[1]["S"])
        self.assertAlmostEqual(after / before, (996.1 + 100) / 996.1, places=3)

    # form of the input
    def test_nominal_outside_its_range(self):
        self.analysis(lambda a: a["parameters"]["lift_to_drag"].update(nominal=25))
        self.fails("lift_to_drag: the nominal value lies between the favourable and the unfavourable one")

    def test_share_of_one_or_more(self):
        self.analysis(lambda a: a["parameters"]["empty_fraction_B"].update(unfavourable=1.0))
        self.fails("empty_fraction_B: favourable, nominal and unfavourable are positive, and below 1")

    def test_source_without_reference_and_unknown_basis(self):
        self.analysis(lambda a: a["missions"][1].pop("ref"))
        self.fails("mission M: a figure with a source names it in ref")
        self.analysis(lambda a: a["missions"][1].update(basis="estimate"))
        self.fails("mission M: basis is one of assumption, source")

    def test_missions_need_a_candidate_and_distinct_keys(self):
        self.analysis(lambda a: a["missions"][1].update(key="S"))
        self.fails("missions: keys are used once, and at least one mission is a candidate")
        shutil.copy(MSN / "missions.yaml", self.msn / "missions.yaml")
        self.analysis(lambda a: [m.update(candidate=False) for m in a["missions"]])
        self.fails("missions: keys are used once, and at least one mission is a candidate")
        shutil.copy(MSN / "missions.yaml", self.msn / "missions.yaml")
        self.analysis(lambda a: a["missions"][0].update(range_km=0))
        self.fails("missions: each has a key, a name, a positive range_km")

    def test_pack_levels_shares_and_single_figures(self):
        self.analysis(lambda a: a["pack_levels"][0].update(wh_per_kg=0))
        self.fails("pack_levels: each has a positive wh_per_kg and a label")
        shutil.copy(MSN / "missions.yaml", self.msn / "missions.yaml")
        self.analysis(lambda a: a.update(hybrid_shares=[0.25, 1.0]))
        self.fails("hybrid_shares: a list of shares above 0 and below 1")
        shutil.copy(MSN / "missions.yaml", self.msn / "missions.yaml")
        self.analysis(lambda a: a["reserves"]["alternate_km"].update(value=-1))
        self.fails("reserves.alternate_km: a record with a value that is not negative")
        shutil.copy(MSN / "missions.yaml", self.msn / "missions.yaml")
        self.analysis(lambda a: a["takeoff_mass_limit_kg"].update(value=0))
        self.fails("takeoff_mass_limit_kg: a record with a positive value")

    def test_options_must_stand_in_the_knot(self):
        self.knot(lambda k: next(o for o in k["options"] if o["id"] == "C").update(state="excluded"))
        self.fails("KNOT-EWTW-NRG-001: options A, B and C must stand; C does not")

    def test_missing_section_and_inputs_that_cannot_be_read(self):
        self.analysis(lambda a: a.pop("parameters"))
        self.fails("`analysis` must hold")
        (self.msn / "missions.yaml").write_text("analysis: [unclosed", encoding="utf-8")
        self.fails("missions.yaml: cannot be read as YAML")
        shutil.copy(MSN / "missions.yaml", self.msn / "missions.yaml")
        self.analysis(lambda a: a.update(knot="KNOT-EWTW-XXX-001"))
        self.fails("KNOT-EWTW-XXX-001: expected in one file of the register, found in 0")

    # the generated section
    def test_stale_readme_fails_the_check_and_is_rewritten(self):
        self.analysis(lambda a: a["payload"]["kg_per_passenger"].update(value=105))
        self.assertEqual(self.run_tool("check")[0], ["README.md: the generated section differs from the output; run again with --write"])
        self.assertEqual(self.run_tool("write")[0], [])
        self.assertEqual(self.run_tool("check")[0], [])
        text = (self.msn / "README.md").read_text(encoding="utf-8")
        self.assertIn("Payload: 100 passengers at 105 kg, 10500 kg.", text)
        self.assertTrue(text.startswith("---\nstatus: draft") and "## Revision history" in text, "the rest of the README is kept")

    def test_control_characters_are_printed_escaped(self):
        self.analysis(lambda a: a["missions"][0].update(name="Short‮ | forged"))
        row = next(line for line in self.run_tool()[1] if line.startswith("| S | Short"))
        self.assertIn("Short\\x202e / forged", row)
        self.assertEqual(row.count("|"), 8, "a bar in the text does not add a column")


if __name__ == "__main__":
    unittest.main()
