# Generated 2026-11-15 - cruise_points_test.py (0.1.0)
"""Tests of tools/cruise_points.py on the cruise-point screening of the eWTW. Run from the repository root:

    python3 tools/cruise_points_test.py

Each test copies the analysis, the mission screening and the KNOT register to a temporary folder, changes one
input and expects the matching result. The arithmetic of the committed input is computed again by hand, and the
standard atmosphere is checked against its published table.
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
import mission_closure as mc  # noqa: E402

MODEL = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW")
REG = MODEL / "01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
CRP = REG / "000_General" / "evidence" / "CRP-EWTW-CRZ-001"
G = 9.80665


class CruisePoints(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.reg = self.tmp / "register"
        shutil.copytree(REG, self.reg)
        self.crp = self.reg / "000_General" / "evidence" / "CRP-EWTW-CRZ-001"
        self.path = self.crp / "cruise-points.yaml"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def edit(self, change):
        doc = yaml.safe_load(self.path.read_text(encoding="utf-8"))
        change(doc["analysis"])
        self.path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")

    def point(self, a, key):
        return next(p for p in a["points"] if p["key"] == key)

    def rows(self):
        a = yaml.safe_load(self.path.read_text(encoding="utf-8"))["analysis"]
        missions = yaml.safe_load((self.crp.parent / a["missions"] / "missions.yaml").read_text(encoding="utf-8"))["analysis"]
        return {r["point"]["key"]: r for r in cp.compute(a, missions)}, missions

    def fails(self, fragment):
        bad, lines = cp.run(self.crp, self.reg)
        self.assertTrue(any(fragment in b for b in bad), f"expected {fragment!r} in {bad}")
        self.assertEqual(len(lines), 1, "a failing run prints only its first line")

    # the analysis as committed
    def test_committed_analysis_passes_and_its_readme_is_current(self):
        bad, lines = cp.run(CRP, REG, "check")
        self.assertEqual(bad, [])
        self.assertEqual(lines[0], "CRP-EWTW-CRZ-001 0.1.0 for KNOT-EWTW-CRZ-001: 4 points on 3 missions of MSN-EWTW-NRG-001 0.3.0; "
                                   "19 figures, 4 of them assumptions; rule failures: none")

    def test_standard_atmosphere_matches_its_table(self):
        for feet, kelvin, hpa in ((0, 288.15, 1013.25), (8000, 272.30, 752.6), (25000, 238.62, 376.0), (35000, 218.81, 238.4), (41000, 216.65, 178.7)):
            t, p, a = cp.atmosphere(feet)
            self.assertAlmostEqual(t, kelvin, delta=0.01)
            self.assertAlmostEqual(p / 100, hpa, delta=0.15)
            self.assertAlmostEqual(a, math.sqrt(1.4 * 287.05287 * kelvin), delta=0.01)

    def test_speed_and_time_by_hand(self):
        rows, _ = self.rows()
        self.assertAlmostEqual(rows["P2"]["tas"], 360 * 1852 / 3600, places=6)             # 185.2 m/s
        self.assertAlmostEqual(rows["P2"]["mach"], 185.2 / 309.66, places=3)                # speed of sound at 25,000 ft
        self.assertAlmostEqual(rows["P4"]["tas"], 0.78 * 296.54, delta=0.02)                # Mach 0.78 at 35,000 ft: 231.3 m/s, 450 kt
        self.assertAlmostEqual(rows["P2"]["flights"]["L"]["minutes"], 2_000_000 / 185.2 / 60, places=6)   # 180 minutes
        self.assertAlmostEqual(rows["P4"]["flights"]["S"]["minutes"], 500_000 / 231.30 / 60, delta=0.01)

    def test_point_with_the_nominal_efficiency_reproduces_the_mission_screening(self):
        rows, missions = self.rows()
        model = mc.Model(missions, "nominal")
        for m in missions["missions"]:
            if m["key"] in ("S", "M", "L"):
                self.assertAlmostEqual(rows["P3"]["flights"][m["key"]]["mass"], model.option_b(m), places=6)
        self.assertAlmostEqual(rows["P3"]["flights"]["L"]["mass"] / 1000, 44.1, delta=0.05)
        self.assertAlmostEqual(rows["P3"]["flights"]["L"]["fuel"], 6839, delta=1)

    def test_mission_at_the_jet_point_by_hand(self):
        rows, a = self.rows()
        product = 0.35 * 0.90 * 0.76 * 15                                                   # turbogenerator, electric chain, fan of P4, lift-to-drag
        per_km = 1000 * G / (product * a["fuel_energy_mj_per_kg"]["value"] * 1e6)
        fitted = mc.fit(a)
        km = 2000 * 1.05 + fitted["terminal_km"] + 185 + 400 * 30 / 60                      # trip with contingency, terminal phases, alternate, final reserve
        share = 1 - math.exp(-per_km * km)
        mass = (a["reference"]["basic_operating_kg"]["value"] + 100 * 95) / (1 - share)
        self.assertAlmostEqual(rows["P4"]["flights"]["L"]["mass"], mass, delta=0.5)
        self.assertAlmostEqual(rows["P4"]["flights"]["L"]["fuel"], mass * share, delta=0.5)
        self.assertGreater(rows["P4"]["flights"]["L"]["fuel"], rows["P3"]["flights"]["L"]["fuel"])

    def test_cruise_power_by_hand(self):
        rows, _ = self.rows()
        self.assertAlmostEqual(rows["P2"]["cruise"], G * 185.2 / (15 * 0.85 * 0.90) / 1000, places=6)       # 0.158 kW/kg
        self.assertAlmostEqual(rows["P4"]["cruise"], G * rows["P4"]["tas"] / (15 * 0.76 * 0.90) / 1000, places=6)
        self.assertGreater(rows["P4"]["cruise"], rows["P4"]["takeoff"], "at the jet point the cruise asks more than the nominal take-off power")
        self.assertLess(rows["P1"]["cruise"], rows["P1"]["takeoff"])

    def test_published_point_by_hand(self):
        q = self.rows()[0]["P2"]["published"]
        self.assertAlmostEqual(q["per_kg"], 7894 * 0.745699872 / 29574, places=6)                            # 0.199 kW/kg at the shaft
        self.assertAlmostEqual(q["share"], 7894 / 9160, places=6)                                            # 86 % of take-off power
        self.assertAlmostEqual(q["product"], G * 185.2 / (1000 * q["per_kg"]), places=6)                     # 9.1
        self.assertAlmostEqual(q["model"], G * 185.2 / (15 * 0.85) / 1000, places=6)                         # 0.142 kW/kg, no electric chain
        self.assertAlmostEqual(q["cruise"], q["per_kg"] / 0.90, places=6)

    def test_cabin_compression_by_hand(self):
        rows, _ = self.rows()
        ratio = 752.6 / 376.0
        self.assertAlmostEqual(rows["P2"]["ratio"], ratio, delta=0.002)
        self.assertAlmostEqual(rows["P2"]["work"], 1004.7 * 238.62 * (ratio ** (0.4 / 1.4) - 1) / 1000, delta=0.1)   # 53 kJ/kg
        self.assertGreater(rows["P4"]["work"], 1.5 * rows["P2"]["work"])

    def test_cabin_below_the_cruise_altitude_needs_no_compression(self):
        self.edit(lambda a: self.point(a, "P1")["altitude_ft"].update(value=6000))
        row = self.rows()[0]["P1"]
        self.assertEqual((row["ratio"], row["work"]), (1.0, 0.0))

    def test_inception_voltage_is_interpolated_on_the_measured_rows(self):
        table = [{"mbar": 1013, "kv": 1.79}, {"mbar": 500, "kv": 1.49}, {"mbar": 250, "kv": 1.27}, {"mbar": 100, "kv": 1.02}, {"mbar": 50, "kv": 0.91}]
        self.assertEqual(cp.inception(table, 1013.25), 1.0)
        self.assertAlmostEqual(cp.inception(table, 250), 1.27 / 1.79, places=9)
        x = (math.log(376.0) - math.log(250)) / (math.log(500) - math.log(250))
        self.assertAlmostEqual(cp.inception(table, 376.0), (1.27 + x * 0.22) / 1.79, places=9)               # 78 %
        self.assertIsNone(cp.inception(table, 40))
        self.assertAlmostEqual(self.rows()[0]["P4"]["inception"], 0.70, delta=0.01)

    def test_generated_section_is_checked_and_written(self):
        self.edit(lambda a: self.point(a, "P4")["altitude_ft"].update(value=37000))
        self.assertEqual(cp.run(self.crp, self.reg, "check")[0], ["README.md: the generated section differs from the output; run again with --write"])
        self.assertEqual(cp.run(self.crp, self.reg, "write")[0], [])
        self.assertIn("37,000 ft", (self.crp / "README.md").read_text(encoding="utf-8"))

    # form and references
    def test_speed_is_in_knots_or_in_mach_below_one(self):
        self.edit(lambda a: self.point(a, "P4")["speed"].update(value=1.2))
        self.fails("point P4: speed is a figure in kt of true airspeed or in mach below 1")
        self.edit(lambda a: self.point(a, "P4")["speed"].update(value=0.78, unit="km/h"))
        self.fails("point P4: speed is a figure in kt of true airspeed or in mach below 1")

    def test_figure_read_at_a_source_names_it(self):
        self.edit(lambda a: self.point(a, "P2")["altitude_ft"].pop("ref"))
        self.fails("point P2: altitude_ft is a figure between 0 and 45,000 ft")

    def test_efficiency_and_altitude_have_bounds(self):
        self.edit(lambda a: self.point(a, "P1")["propulsor_efficiency"].update(value=1.0))
        self.fails("point P1: propulsor_efficiency is a figure above 0 and below 1")
        self.edit(lambda a: (self.point(a, "P1")["propulsor_efficiency"].update(value=0.85), self.point(a, "P1")["altitude_ft"].update(value=60000)))
        self.fails("point P1: altitude_ft is a figure between 0 and 45,000 ft")

    def test_point_names_an_option_of_its_knot(self):
        self.edit(lambda a: self.point(a, "P3").update(option="D"))
        self.fails("point P3: option D is not an option of KNOT-EWTW-CRZ-001")

    def test_points_are_unique(self):
        self.edit(lambda a: a["points"].append(dict(self.point(a, "P1"))))
        self.fails("point P1 repeated")

    def test_published_point_is_complete_and_sourced(self):
        self.edit(lambda a: self.point(a, "P2")["published"].pop("takeoff_shp"))
        self.fails("point P2: published gives takeoff_kg, cruise_shp and takeoff_shp read at a source")

    def test_insulation_rows_fall_from_sea_level(self):
        self.edit(lambda a: a["insulation"]["table"].reverse())
        self.fails("insulation: the rows go from sea level down, by falling pressure")

    def test_serves_a_knu_of_its_knot(self):
        self.edit(lambda a: a.update(serves="KNU-EWTW-CRZ-001-09"))
        self.fails("KNU-EWTW-CRZ-001-09 is not a KNU of KNOT-EWTW-CRZ-001")

    def test_mission_screening_is_found_and_sound(self):
        self.edit(lambda a: a.update(missions="MSN-EWTW-XXX-001"))
        self.fails("missions names the folder of a mission screening beside this one")
        self.edit(lambda a: a.update(missions="MSN-EWTW-NRG-001"))
        msn = self.crp.parent / "MSN-EWTW-NRG-001" / "missions.yaml"
        msn.write_text(msn.read_text(encoding="utf-8").replace("id: MSN-EWTW-NRG-001", "id: ''", 1), encoding="utf-8")
        self.fails("the mission screening MSN-EWTW-NRG-001 fails its own check")


if __name__ == "__main__":
    unittest.main()
