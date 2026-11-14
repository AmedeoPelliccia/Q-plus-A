# Generated 2026-11-14 - mission_closure_test.py (0.3.0)
"""Tests of tools/mission_closure.py on the candidate missions of the eWTW. Run from the repository root:

    python3 tools/mission_closure_test.py

Each test copies the analysis and the KNOT register to a temporary folder, changes one input
and expects the matching result. The fit and the equations of the committed input are computed again by hand.
"""
import math
import pathlib
import shutil
import statistics
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import mission_closure as mc  # noqa: E402

MODEL = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW")
REG = MODEL / "01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
MSN = REG / "000_General" / "evidence" / "MSN-EWTW-NRG-001"
G, NM, LB = 9.80665, 1.852, 0.45359237


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

    def restore(self):
        shutil.copy(MSN / "missions.yaml", self.msn / "missions.yaml")

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
        self.assertTrue(lines[0].endswith("3 missions, 4 pack levels, 6 reference sectors; 31 figures, 14 of them assumptions; rule failures: none"), lines[0])

    # the fit to the reference
    def test_fit_by_another_implementation(self):
        sectors = self.read()["reference"]["sectors"]
        xs = [s["esad_nm"] * NM for s in sectors]
        ys = [-math.log(1 - s["block_fuel_usg"] * 6.70 * LB / (s["takeoff_lb"] * LB)) for s in sectors]
        line = statistics.linear_regression(xs, ys)
        fitted = mc.fit(self.read())
        self.assertAlmostEqual(fitted["per_km"], line.slope, places=12)
        self.assertAlmostEqual(fitted["terminal_km"], line.intercept / line.slope, places=6)
        self.assertAlmostEqual(fitted["product"], 1000 * G / (line.slope * 43.0e6), places=9)
        self.assertAlmostEqual(fitted["terminal_km"], 483, delta=1)
        self.assertAlmostEqual(fitted["product"], 4.08, places=2)

    def test_fit_reproduces_the_published_sectors(self):
        rows = mc.fit(self.read())["rows"]
        self.assertAlmostEqual(rows[0]["fuel_kg"], 633 * 6.70 * LB)
        self.assertAlmostEqual(rows[0]["takeoff_kg"], 89366 * LB)
        self.assertLess(max(abs(r["fitted_kg"] / r["fuel_kg"] - 1) for r in rows), 0.015)

    def test_fit_recovers_the_values_that_made_the_sectors(self):
        per_km, terminal = 6.0e-5, 400.0
        made = [{"name": f"S{n}", "esad_nm": n, "takeoff_lb": 90000.0,
                 "block_fuel_usg": 90000.0 * (1 - math.exp(-per_km * (n * NM + terminal))) / 6.70} for n in (200, 450, 700, 1200)]
        self.analysis(lambda a: a["reference"].update(sectors=made))
        fitted = mc.fit(self.read())
        self.assertAlmostEqual(fitted["per_km"], per_km, places=12)
        self.assertAlmostEqual(fitted["terminal_km"], terminal, places=6)

    def test_check_outside_the_fit_by_hand(self):
        a = self.read()
        fitted = mc.fit(a)
        km = (2400 + 100) * NM + fitted["terminal_km"] + 400 * 45 / 60          # the reserve of the reference: no contingency, 100 nm, 45 minutes
        self.assertAlmostEqual(fitted["check"]["asked_kg"], 50300 * (1 - math.exp(-fitted["per_km"] * km)))
        self.assertEqual(fitted["check"]["loadable_kg"], 50300 - 27753 - 100 * 100)
        self.assertAlmostEqual(fitted["check"]["asked_kg"] / fitted["check"]["loadable_kg"] - 1, 0.047, places=3)

    def test_check_does_not_use_the_reserve_of_the_aircraft_under_test(self):
        before = mc.fit(self.read())["check"]["asked_kg"]
        self.analysis(lambda a: (a["reserves"]["final_reserve_min"].update(value=90), a["reserves"]["alternate_km"].update(value=500)))
        self.assertAlmostEqual(mc.fit(self.read())["check"]["asked_kg"], before)
        self.analysis(lambda a: a["reference"]["range_check"].update(flight_min=30))
        self.assertLess(mc.fit(self.read())["check"]["asked_kg"], before)

    def test_tolerance_of_the_check(self):
        self.assertTrue(any("No tolerance is written for this point: it is a check of the test, not a requirement of the aircraft." in line for line in self.run_tool()[1]))
        self.analysis(lambda a: a["reference"]["range_check"].update(tolerance_share=0.05))
        self.assertTrue(any("The tolerance written for this point is 5%." in line for line in self.run_tool()[1]))
        self.analysis(lambda a: a["reference"]["range_check"].update(tolerance_share=1.5))
        self.fails("reference.range_check: a range, passengers and their mass")
        self.restore()
        self.analysis(lambda a: a["reference"]["range_check"].pop("reserve_ref"))
        self.fails("reference.range_check: a range, passengers and their mass")

    # the equations
    def test_distance_flown_by_hand(self):
        m, missions = self.model()
        terminal = mc.fit(self.read())["terminal_km"]
        self.assertAlmostEqual(m.reserve_km, 185 + 400 * 30 / 60)
        self.assertAlmostEqual(m.equivalent_km(missions["S"]), 500 * 1.05 + terminal + 385)
        self.assertAlmostEqual(self.model("favourable")[0].terminal_km, 0.6 * terminal)

    def test_option_b_by_hand(self):
        m, missions = self.model()
        fuel = 1 - math.exp(-m.equivalent_km(missions["M"]) * 1000 * G / (0.35 * 0.90 * 0.85 * 15 * 43.0e6))
        self.assertAlmostEqual(m.option_b(missions["M"]), (27753 + 9500) / (1 - fuel))
        self.assertAlmostEqual(m.option_b(missions["M"]) / 1000, 41.8, places=1)
        self.assertAlmostEqual(m.product_b, 0.35 * 0.90 * 0.85 * 15)

    def test_option_a_by_hand(self):
        m, missions = self.model()
        km, km_per_share = m.equivalent_km(missions["S"]), 3600 * 0.72 * 0.90 * 0.85 * 15 / (1000 * G)   # km flown by a pack of 1 Wh/kg that is the whole aircraft
        room = 1 - (27753 + 9500) / 51800
        self.assertAlmostEqual(m.room(), room)
        self.assertAlmostEqual(m.pack_needed_a(missions["S"]), km / km_per_share / room)
        self.assertAlmostEqual(m.pack_needed_a(missions["S"]), 1635, delta=1)
        self.assertAlmostEqual(m.option_a(missions["S"], 2000), (27753 + 9500) / (1 - km / (2000 * km_per_share)))
        self.assertIsNone(m.option_a(missions["S"], 177), "the energy alone is more than the aircraft")

    def test_option_c_by_hand(self):
        m, missions = self.model()
        trip, km_per_share = m.trip_km(missions["S"]), 650 * 3600 * 0.72 * 0.90 * 0.85 * 15 / (1000 * G)
        fuel = 1 - math.exp(-(0.75 * trip + 385) * 1000 * G / (0.35 * 0.90 * 0.85 * 15 * 43.0e6))
        self.assertAlmostEqual(m.option_c(missions["S"], 0.25, 650), (27753 + 9500) / (1 - 0.25 * trip / km_per_share - fuel))

    def test_empty_mass_grows_by_its_share(self):
        self.analysis(lambda a: a["empty_growth_share"].update(value=0.5))
        m, missions = self.model()
        self.assertAlmostEqual(m.empty_at(50300), 27753)
        self.assertAlmostEqual(m.empty_at(40000), 27753 * (0.5 + 0.5 * 40000 / 50300))
        mass = m.option_b(missions["S"])
        self.assertAlmostEqual(mass, m.empty_at(mass) + 9500 + mass * m.fuel_fraction(m.equivalent_km(missions["S"])), places=6)
        self.analysis(lambda a: a["empty_growth_share"].update(value=1.0))
        self.assertAlmostEqual(self.model()[0].empty_at(25000) / 25000, 27753 / 50300)

    # consistency of the equations
    def test_pack_needed_puts_the_aircraft_at_the_mass_limit(self):
        for growth in (0.0, 0.5):
            self.analysis(lambda a: a["empty_growth_share"].update(value=growth))
            for which in mc.SETS:
                m, missions = self.model(which)
                self.assertAlmostEqual(m.option_a(missions["S"], m.pack_needed_a(missions["S"])), 51800, places=3)
                self.assertAlmostEqual(m.option_c(missions["S"], 0.25, m.pack_needed_c(missions["S"], 0.25)), 51800, places=3)

    def test_longest_trip_is_the_inverse_of_the_pack_needed(self):
        m, _ = self.model("favourable")
        trip = m.trip_within_limit_a(650)
        self.assertGreater(trip, 0)
        self.assertAlmostEqual(m.pack_needed_a({"range_km": trip}), 650, places=6)
        self.assertEqual(self.model()[0].trip_within_limit_a(650), 0.0, "the terminal phases and the reserves alone exceed the limit")

    def test_sets_are_ordered(self):
        fav, nom, unf = (self.model(s) for s in mc.SETS)
        for key in "SM":
            self.assertLess(fav[0].pack_needed_a(fav[1][key]), nom[0].pack_needed_a(nom[1][key]))
            self.assertLess(nom[0].pack_needed_a(nom[1][key]), unf[0].pack_needed_a(unf[1][key]))
            self.assertLess(fav[0].option_b(fav[1][key]), nom[0].option_b(nom[1][key]))
            self.assertLess(nom[0].option_b(nom[1][key]), unf[0].option_b(unf[1][key]))

    def test_over_the_limit_does_not_close(self):
        unf, missions = self.model("unfavourable")
        self.assertFalse(unf.closes(unf.option_b(missions["L"])))
        self.assertFalse(unf.closes(None))
        lines = self.run_tool()[1]
        self.assertIn("| L | 35.3 · 44.1 · over | 6839 | 8.8 | 12 | 9 |", lines)
        self.assertIn("| S | 673 · 1635 · 3186 | none | over | over | over |", lines)

    def test_fuel_burned_is_compared_in_kilograms(self):
        m, missions = self.model()
        b = m.option_b(missions["S"]) * m.fuel_fraction(m.equivalent_km(missions["S"]))
        c = m.option_c(missions["S"], 0.10, 177) * m.fuel_c(missions["S"], 0.10)
        self.assertAlmostEqual(c / b - 1, 0.16, places=2)
        self.assertIn("| S | 10% | 51 · 158 · 478 | 50.2 · 43.3 · 42.4 · 41.6 | +16% · -0% · -2% · -4% |", self.run_tool()[1])

    def test_sensitivity_rows_are_the_model_at_each_growth(self):
        lines = self.run_tool()[1]
        self.assertIn("| 0% | 40.3 | 1635 | — · -0% · -6% · -11% |", lines)
        self.assertIn("| 100% | 25.5 | 1734 | — · +44% · +19% · +2% |", lines)
        self.analysis(lambda a: a["empty_growth_share"].update(value=1.0))
        m, missions = self.model()
        self.assertAlmostEqual(m.option_b(missions["S"]) / 1000, 25.5, places=1)
        self.assertAlmostEqual(m.pack_needed_a(missions["S"]), 1734, delta=1)

    def test_units_are_counted_at_take_off_power(self):
        m, missions = self.model()
        power = m.option_b(missions["M"]) * 0.20
        self.assertEqual((math.ceil(power / 750), math.ceil(power / 1000)), (12, 9))
        self.assertIn("| M | 34.0 · 41.8 · 48.5 | 4535 | 8.4 | 12 | 9 |", self.run_tool()[1])

    def test_longer_final_reserve_costs_the_battery_more(self):
        before = self.model()[0].pack_needed_a(self.model()[1]["S"])
        km = self.model()[0].equivalent_km(self.model()[1]["S"])
        self.analysis(lambda a: a["reserves"]["final_reserve_min"].update(value=45))
        after = self.model()[0].pack_needed_a(self.model()[1]["S"])
        self.assertAlmostEqual(after / before, (km + 100) / km, places=9)

    # form of the input
    def test_nominal_outside_its_range(self):
        self.analysis(lambda a: a["parameters"]["lift_to_drag"].update(nominal=25))
        self.fails("lift_to_drag: the nominal value lies between the favourable and the unfavourable one")

    def test_share_of_one_or_more(self):
        self.analysis(lambda a: a["parameters"]["propulsor_efficiency"].update(favourable=1.0))
        self.fails("propulsor_efficiency: favourable, nominal and unfavourable are positive, and below 1")
        self.restore()
        self.analysis(lambda a: a["empty_growth_share"].update(value=1.5))
        self.fails("empty_growth_share: a record with a value from 0 to 1")

    def test_source_without_reference_and_unknown_basis(self):
        self.analysis(lambda a: a["missions"][1].pop("ref"))
        self.fails("mission M: a figure with a source names it in ref")
        self.analysis(lambda a: a["missions"][1].update(basis="estimate"))
        self.fails("mission M: basis is one of assumption, source, decision")
        self.restore()
        self.analysis(lambda a: a["missions"][2].pop("ref"))
        self.fails("mission L: a figure with a decision names it in ref")

    def test_reference_masses_and_sectors(self):
        self.analysis(lambda a: a["reference"]["sizing_takeoff_kg"].update(value=60000))
        self.fails("reference: an aircraft, a source for its sectors, and masses in the order empty, sizing take-off, take-off limit")
        self.restore()
        self.analysis(lambda a: a["reference"].update(sectors=a["reference"]["sectors"][:2]))
        self.fails("reference.sectors: at least three")
        self.restore()
        self.analysis(lambda a: a["reference"]["sectors"][0].update(block_fuel_usg=20000))
        self.fails("reference.sectors: at least three, each with a name, a distance, a block fuel below the take-off mass")
        self.restore()
        self.analysis(lambda a: a["reference"].pop("sectors_ref"))
        self.fails("reference: an aircraft, a source for its sectors")

    def test_sectors_that_give_no_fit(self):
        self.analysis(lambda a: [s.update(block_fuel_usg=2000 - s["esad_nm"]) for s in a["reference"]["sectors"]])
        self.fails("reference.sectors: the published sectors must give a positive cost of cruise and a positive terminal distance")
        self.restore()
        self.analysis(lambda a: [s.update(esad_nm=300) for s in a["reference"]["sectors"]])
        self.fails("reference.sectors: the published sectors must give a positive cost of cruise and a positive terminal distance")

    def test_missions_have_roles_and_one_requirement(self):
        self.analysis(lambda a: a["missions"][1].update(key="S"))
        self.fails("missions: keys are used once, and one mission is the requirement")
        self.restore()
        self.analysis(lambda a: a["missions"][2].update(role="scoring"))
        self.fails("missions: keys are used once, and one mission is the requirement")
        self.restore()
        self.analysis(lambda a: a["missions"][1].update(role="requirement"))
        self.fails("missions: keys are used once, and one mission is the requirement")
        self.restore()
        self.analysis(lambda a: a["missions"][0].update(role="design"))
        self.fails("missions: each has a key, a name, a positive range_km, and a role among requirement, scoring, sensitivity, reference")
        self.restore()
        self.analysis(lambda a: a["missions"][0].update(range_km=0))
        self.fails("missions: each has a key, a name, a positive range_km")

    def test_requirement_mission_is_reported(self):
        lines = self.run_tool()[1]
        self.assertIn("| L | Long stage | requirement | 2000 | 2968 | decision | KNOT-EWTW-NRG-001, ruling R2 of 2026-11-14. It must close |", lines)
        self.assertTrue(any(line.startswith("On the requirement mission L, option B closes at favourable and nominal values, and not at unfavourable values. "
                                            "Option A needs 1556 · 3485 · 6555 Wh/kg at pack level") for line in lines))
        self.analysis(lambda a: (a["missions"][2].update(role="sensitivity"), a["missions"][0].update(role="requirement")))
        self.assertTrue(any(line.startswith("On the requirement mission S, option B closes at favourable and nominal and unfavourable values. ") for line in self.run_tool()[1]))

    def test_pack_levels_shares_and_single_figures(self):
        self.analysis(lambda a: a["pack_levels"][0].update(wh_per_kg=0))
        self.fails("pack_levels: each has a positive wh_per_kg and a label")
        self.restore()
        self.analysis(lambda a: a.update(hybrid_shares=[0.25, 1.0]))
        self.fails("hybrid_shares: a list of shares above 0 and below 1")
        self.restore()
        self.analysis(lambda a: a["reserves"]["alternate_km"].update(value=-1))
        self.fails("reserves.alternate_km: a record with a value that is not negative")

    def test_options_are_read_from_the_knot_with_their_state(self):
        self.assertIn("Options in `KNOT-EWTW-NRG-001`: A excluded by R2 · B open · C open · D excluded by R1.", self.run_tool()[1])
        self.knot(lambda k: next(o for o in k["options"] if o["id"] == "A").update(state="open", by=None))
        self.assertIn("Options in `KNOT-EWTW-NRG-001`: A open · B open · C open · D excluded by R1.", self.run_tool()[1])
        self.knot(lambda k: k.update(options=[o for o in k["options"] if o["id"] != "C"]))
        self.fails("KNOT-EWTW-NRG-001: options A, B and C must be in the record; C is not")

    def test_missing_section_and_inputs_that_cannot_be_read(self):
        self.analysis(lambda a: a.pop("reference"))
        self.fails("`analysis` must hold")
        (self.msn / "missions.yaml").write_text("analysis: [unclosed", encoding="utf-8")
        self.fails("missions.yaml: cannot be read as YAML")
        self.restore()
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
