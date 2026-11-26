# Generated 2026-11-26 - turbogenerator_figures_test.py (0.1.0)
"""Tests of tools/turbogenerator_figures.py on the turbogenerator figures of the eWTW. Run from the repository root:

    python3 tools/turbogenerator_figures_test.py

Each test copies the KNOT register to a temporary folder, changes one input and expects the matching result. The
arithmetic of the committed input is computed again by hand, the rule is checked against the screening it comes from,
and the megawatts that a research report gave are checked against the horsepower read in the table.
"""
import math
import pathlib
import shutil
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cruise_points as cp  # noqa: E402
import turbogenerator_figures as tg  # noqa: E402

MODEL = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW")
REG = MODEL / "01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
TGF = REG / "000_General" / "evidence" / "TGF-EWTW-GEN-001"
HP, LB = 0.745699872, 0.45359237


def standard(feet):
    """Temperature and pressure ratios of the standard atmosphere below the tropopause, written again for the tests."""
    theta = 1 - 0.0065 * feet * 0.3048 / 288.15
    return theta, theta ** 5.25588


def rule(feet, knots):
    """Total pressure over the root of total temperature against sea level at rest, by hand."""
    theta, delta = standard(feet)
    mach = knots * 1852 / 3600 / math.sqrt(1.4 * 287.05287 * 288.15 * theta)
    ram = 1 + 0.2 * mach ** 2
    return delta * ram ** 3.5 / math.sqrt(theta * ram)


class TurbogeneratorFigures(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.reg = self.tmp / "register"
        shutil.copytree(REG, self.reg)
        self.folder = self.reg / "000_General" / "evidence" / "TGF-EWTW-GEN-001"
        self.path = self.folder / "turbogenerator-figures.yaml"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def again(self):
        self.tearDown()
        self.setUp()

    def analysis(self):
        return yaml.safe_load(self.path.read_text(encoding="utf-8"))["analysis"]

    def edit(self, change):
        doc = yaml.safe_load(self.path.read_text(encoding="utf-8"))
        change(doc["analysis"])
        self.path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")

    def fails(self, text, mode=None):
        bad, lines = tg.run(self.folder, self.reg, mode)
        self.assertTrue(any(text in b for b in bad), bad)
        self.assertEqual(len(lines), 1)

    def result(self):
        return tg.compute(self.analysis())

    def test_committed_analysis_passes_and_its_readme_is_current(self):
        bad, lines = tg.run(TGF, REG, "check")
        self.assertEqual(bad, [])
        self.assertTrue(lines[0].startswith("TGF-EWTW-GEN-001 0.1.0 for KNOT-EWTW-GEN-001: 38 figures, 8 of them assumptions"))
        self.assertTrue(lines[0].endswith("27 by two readers, 2 by the reviewer alone, 1 as reported; rule failures: none"))

    def test_rule_is_the_rule_of_the_screening(self):
        screening = yaml.safe_load((self.reg / "000_General" / "evidence" / "CRP-EWTW-CRZ-001" / "cruise-points.yaml").read_text(encoding="utf-8"))["analysis"]
        self.assertEqual(screening["gas_turbine"]["rule"], cp.RULE)
        shares = []
        for p in screening["points"]:
            t, pressure, sound = cp.atmosphere(p["altitude_ft"]["value"])
            mach = p["speed"]["value"] if p["speed"]["unit"] == "mach" else p["speed"]["value"] * cp.KT / sound
            mine = tg.air(p["altitude_ft"]["value"], mach=mach)[1]
            self.assertAlmostEqual(mine, cp.air_flow(t, pressure, mach), places=12)
            shares.append(round(100 * mine))
        self.assertEqual(shares, [56, 50, 47, 38])                      # the four shares the screening prints

    def test_rule_by_hand_and_on_a_warm_day(self):
        for feet, knots in ((0, 0), (25000, 350), (30000, 350), (31000, 360)):
            self.assertAlmostEqual(tg.air(feet, kt=knots)[1], rule(feet, knots), places=6)
        self.assertAlmostEqual(tg.air(0, kt=0)[1], 1.0, places=12)
        self.assertAlmostEqual(tg.air(5000, 20, kt=0)[1], standard(5000)[1] / math.sqrt(standard(5000)[0] + 20 / 288.15), places=6)
        self.assertLess(tg.air(5000, 20, kt=0)[1], tg.air(5000, 0, kt=0)[1])   # warmer air, less of it

    def test_working_reference(self):
        r = self.result()["reference"]
        self.assertAlmostEqual(r["mach"], 0.6135, places=3)
        self.assertAlmostEqual(r["rule"], 0.3976, places=3)
        self.assertAlmostEqual(r["sea_level_mw"], 5.6 / rule(31000, 360), places=3)
        self.assertAlmostEqual(r["sea_level_mw"], 14.1, places=1)

    def test_nearest_tabulated_point(self):
        nasa, cots = (t["near"] for t in self.result()["tables"])
        self.assertEqual((nasa["altitude_ft"], nasa["kt"]), (30000, 350))
        self.assertAlmostEqual(nasa["rated_mw"], 5.6 * 7500 / 3294, places=6)          # 12.75
        self.assertAlmostEqual(cots["rated_mw"], 5.6 * 7500 / 3303, places=6)          # 12.72
        self.assertAlmostEqual(nasa["continuous_mw"], 5.6 * 5896 / 3294, places=6)     # 10.02
        self.assertAlmostEqual(cots["continuous_mw"], 5.6 * 5900 / 3303, places=6)     # 10.00
        self.assertAlmostEqual(nasa["by_rule_mw"], 5.6 / rule(30000, 350), places=3)   # 13.7
        self.assertAlmostEqual(nasa["carried_mw"], nasa["rated_mw"] * rule(30000, 350) / rule(31000, 360), places=3)

    def test_tables_against_the_rule(self):
        nasa, cots = self.result()["tables"]
        cell = nasa["grid"][4][7]                                        # 30,000 ft, 350 kt
        self.assertAlmostEqual(cell["rated"], 3294 / 7500 / rule(30000, 350), places=4)
        self.assertAlmostEqual(cell["continuous"], 3294 / 5896 / rule(30000, 350), places=4)
        self.assertEqual([round(x, 2) for x in nasa["rated_range"]], [1.01, 1.07])
        self.assertEqual([round(x, 2) for x in cots["rated_range"]], [1.08, 1.20])
        self.assertEqual([round(x, 2) for x in nasa["continuous_range"]], [1.28, 1.37])
        self.assertEqual([round(x, 2) for x in cots["continuous_range"]], [1.37, 1.53])
        self.assertAlmostEqual(nasa["worth"][4][1], 3294 / 2605, places=9)
        self.assertAlmostEqual(cots["worth"][4][1], 3303 / 3005, places=9)

    def test_megawatts_of_the_second_report(self):
        given = {(0, 0): 4.400, (0, 300): 4.528, (0, 350): 4.585, (25000, 0): 2.727, (25000, 300): 2.904, (25000, 350): 2.984,
                 (30000, 0): 2.241, (30000, 300): 2.392, (30000, 350): 2.463}
        table = next(t for t in self.analysis()["power_tables"] if t["key"] == "cots")
        for (feet, knots), megawatts in given.items():
            row = next(r for r in table["conditions"] if r["altitude_ft"] == feet and r["isa_k"] == 0)
            self.assertAlmostEqual(row["shp"][table["speeds_kt"].index(knots)] * HP / 1000, megawatts, delta=0.0006)

    def test_two_documents_on_one_engine(self):
        s = self.result()["second"]
        at_25, at_30 = 3459 + 0.68 * (3632 - 3459), 2942 + 0.68 * (3100 - 2942)
        self.assertAlmostEqual(s["tabled"], at_25 + 0.6 * (at_30 - at_25), places=6)   # 3,260.32 shp
        self.assertAlmostEqual(s["scaled"], 11070 / 4 * 7500 / 6476, places=6)         # 3,205.10 shp
        self.assertAlmostEqual(100 * s["difference"], -1.6936, places=3)

    def test_efficiencies_by_hand(self):
        r = self.result()
        by_name = {e["name"]: e for e in r["efficiencies"]}
        cruise = next(e for n, e in by_name.items() if n.startswith("NASA model") and "full throttle" in n)
        self.assertAlmostEqual(cruise["eta"], 3.6 / (0.430 * LB / HP * 43.0), places=9)
        self.assertAlmostEqual(cruise["eta"], 0.3201, places=4)
        self.assertGreater(cruise["high"], cruise["eta"])                # a lower heating value gives a higher efficiency
        self.assertAlmostEqual(cruise["terminals"], cruise["eta"] * 0.97, places=12)
        flight = [e["eta"] for n, e in by_name.items() if n.startswith("PW120A")]
        self.assertEqual([round(x, 4) for x in flight], [0.2919, 0.2771])
        self.assertEqual([round(x, 4) for x in r["test_own"]], [0.2186, 0.2381, 0.2462, 0.2537])
        self.assertEqual([round(shaft, 4) for _, shaft, _ in r["budget"]], [0.3608, 0.4010])
        self.assertAlmostEqual(r["flight_mach"], 0.40, places=2)
        self.assertEqual(len(r["efficiencies"]), 25)

    def test_part_load(self):
        r = self.result()
        bench = [x for x in r["loads"] if x[0].startswith("T56")]
        self.assertAlmostEqual(bench[0][2], 2198.7 / 3442.0, places=9)
        self.assertAlmostEqual(bench[0][3], (0.235 / 2198.7) / (0.317 / 3442.0), places=9)     # 1.1605
        lines = {name: (slope, lowest) for name, _, slope, lowest in r["lines"]}
        slope = lines[next(n for n in lines if n.startswith("T56"))][0]
        self.assertAlmostEqual(tg.on_line(slope, 2198.7 / 3442.0), bench[0][3], places=9)      # the line passes through its point
        self.assertAlmostEqual(lines[next(n for n in lines if "LCTR2" in n)][0], 0.168, places=3)
        self.assertAlmostEqual(tg.intercept(0.6, (0.2 + 0.8 * 0.6) / 0.6, 0.7, (0.2 + 0.8 * 0.7) / 0.7), 0.2, places=9)

    def test_masses(self):
        r = self.result()
        ratios = [round(x, 2) for _, _, x in r["masses"]]
        self.assertEqual(ratios[:5], [7.87, 7.09, 6.48, 17.24, 16.06])
        self.assertEqual([round(r["study"][k], 2) for k in ("baseline", "same_year", "doubled")], [1.45, 2.02, 2.27])
        advanced = next(x for x in r["sizes"] if x["row"]["name"] == "ts7500a")
        self.assertAlmostEqual(advanced["kw_kg"], 7500 * HP / (773 * LB), places=6)

    def test_a_figure_read_names_its_source_its_reader_and_its_class(self):
        self.edit(lambda a: a["flight"].pop("ref"))
        self.fails("a figure gives a basis")
        self.again()
        self.edit(lambda a: a["flight"].update(read="someone"))
        self.fails("a figure gives a basis")
        self.again()
        self.edit(lambda a: a["flight"].update({"class": "E"}))
        self.fails("a figure gives a basis")

    def test_an_assumption_has_a_note(self):
        self.edit(lambda a: a["generator_efficiency"].pop("note"))
        self.fails("a figure gives a basis")

    def test_table_has_one_power_for_each_speed(self):
        self.edit(lambda a: a["power_tables"][0]["conditions"][3]["shp"].pop())
        self.fails("power table nasa: each condition has a key")

    def test_table_starts_at_rest_at_sea_level(self):
        self.edit(lambda a: a["power_tables"][1]["speeds_kt"].__setitem__(0, 10))
        self.fails("power table cots: a rated power, and speeds that rise from 0")
        self.again()
        self.edit(lambda a: a["power_tables"][1]["conditions"].reverse())
        self.fails("power table cots: the first condition is sea level on a standard day")

    def test_second_document_lies_inside_its_table(self):
        self.edit(lambda a: a["second_document"].update(altitude_ft=32000))
        self.fails("second_document: its point lies inside")
        self.again()
        self.edit(lambda a: a["second_document"].update(table="other"))
        self.fails("second_document: it names a power table")

    def test_serves_knus_of_its_knot(self):
        self.edit(lambda a: a.update(serves=["KNU-EWTW-GEN-001-09"]))
        self.fails("KNU-EWTW-GEN-001-09 is not a KNU of KNOT-EWTW-GEN-001")

    def test_record_is_beside_the_folder(self):
        self.edit(lambda a: a.update(record="KNOT-EWTW-GEN-001_other_2026-11-26.md"))
        self.fails("is not beside this folder")

    def test_screening_still_states_the_rule(self):
        path = self.reg / "000_General" / "evidence" / "CRP-EWTW-CRZ-001" / "cruise-points.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace("rule: corrected-flow", "rule: table", 1), encoding="utf-8")
        self.fails("does not state the rule `corrected-flow`")

    def test_bench_modes_rise_in_power(self):
        self.edit(lambda a: a["ground_test"]["modes"].reverse())
        self.fails("ground_test: the modes rise in power")

    def test_study_masses_add_up(self):
        self.edit(lambda a: a["study_masses"].update(total_lbm=12000))
        self.fails("study_masses: the electric system and the engine add up to the total")

    def test_mass_is_in_one_unit(self):
        self.edit(lambda a: a["masses"][0].update(kg=127.0))
        self.fails("masses: each has a name, a power, and a mass in lb or in kg, not both")

    def test_generated_section_follows_the_input(self):
        self.edit(lambda a: a["reference"]["cruise_mw"].update(value=6.0))
        self.fails("the generated section differs from the output", "check")
        bad, _ = tg.run(self.folder, self.reg, "write")
        self.assertEqual(bad, [])
        self.assertIn("6.0 MW at the gas turbines", (self.folder / "README.md").read_text(encoding="utf-8"))
        self.assertEqual(tg.run(self.folder, self.reg, "check")[0], [])


if __name__ == "__main__":
    unittest.main()
