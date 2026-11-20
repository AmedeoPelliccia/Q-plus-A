# Generated 2026-11-18 - configuration_screen_test.py (0.2.0)
"""Tests of tools/configuration_screen.py on the configuration screening of the eWTW. Run from the repository root:

    python3 tools/configuration_screen_test.py

Each test that changes an input copies the KNOT register, with its analyses, to a temporary folder. The geometry,
the two calibrations, the masses and one whole aircraft of the committed input are computed again by hand, from the
figures of the input and plain arithmetic.
"""
import math
import pathlib
import shutil
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import configuration_screen as cs  # noqa: E402
import cruise_points as cp  # noqa: E402
import mission_closure as mc  # noqa: E402

MODEL = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW")
REG = MODEL / "01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
CFG = REG / "000_General" / "evidence" / "CFG-EWTW-AER-001"
G = 9.80665
HEAD = ("CFG-EWTW-AER-001 0.2.0 for KNOT-EWTW-AER-001: 4 sections, 3 wings and 4 cruise points at 3 technology sets, on the missions of "
        "MSN-EWTW-NRG-001 0.3.0; 118 figures, 53 of them assumptions; rule failures: none")


def read(folder, name):
    return yaml.safe_load((folder / name).read_text(encoding="utf-8"))["analysis"]


def inputs(cfg=CFG):
    a = read(cfg, "configuration.yaml")
    return a, read(cfg.parent / a["missions"], "missions.yaml"), read(cfg.parent / a["cruise_points"], "cruise-points.yaml")


def torenbeek_wing(zero_fuel, area, span, sweep, relief, braced=1.0):
    structural = span / math.cos(math.radians(sweep))
    root = 0.14 * 1.5 * area / span
    return (zero_fuel * 0.00667 * structural ** 0.75 * (1 + math.sqrt(1.905 / structural)) * 3.75 ** 0.55
            * ((structural / root) / (zero_fuel / area)) ** 0.30 * 1.02 * relief * braced)


def wetted_fuselage(d, length):
    return math.pi * d * length * (1 - 2 * d / length) ** (2 / 3) * (1 + (d / length) ** 2)


def form(d, length):
    return 1 + 60 / (length / d) ** 3 + (length / d) / 400


class Committed(unittest.TestCase):
    """The analysis as committed, computed once."""

    @classmethod
    def setUpClass(cls):
        cls.a, cls.missions, cls.points = inputs()
        cls.ref, cls.geoms, cls.rows = cs.compute(cls.a, cls.missions, cls.points)
        cls.grid = {(x["tech"], x["section"], x["wing"], x["point"]): x for x in cls.rows}

    def test_committed_analysis_passes_and_its_readme_is_current(self):
        bad, lines = cs.run(CFG, REG, "check")
        self.assertEqual(bad, [])
        self.assertEqual(lines[0], HEAD)

    def test_every_aircraft_closes(self):
        self.assertEqual(len(self.rows), 3 * 4 * 3 * 4)
        self.assertTrue(all(x["converged"] for x in self.rows))

    def test_section_of_five_abreast_by_hand(self):
        g = self.geoms["F5"]
        cabin = 20 * 0.82 + 15.9 / 3.28                                   # 20 rows of five, and the floor of doors, galleys and lavatories
        outer = 3.28 + 2 * 0.135
        length = cabin + 3.17 + 2.25 * outer
        self.assertEqual((g["rows"], g["seats"]), (20, 100))
        self.assertAlmostEqual(g["cabin"], cabin, places=9)
        self.assertAlmostEqual(g["length"], length, places=9)
        self.assertAlmostEqual(g["floor"], outer * cabin, places=9)       # 75.4 m2
        self.assertAlmostEqual(g["wetted"], wetted_fuselage(outer, length), places=6)
        self.assertAlmostEqual(g["wetted"], 310.15, delta=0.01)
        self.assertAlmostEqual(g["section"], math.pi * outer ** 2 / 4, places=9)

    def test_six_abreast_seats_a_whole_row_more(self):
        self.assertEqual((self.geoms["F6"]["rows"], self.geoms["F6"]["seats"]), (17, 102))

    def test_wider_section_for_the_same_seats_abreast_is_no_longer(self):
        self.assertEqual(self.geoms["F5W"]["rows"], self.geoms["F5"]["rows"])
        self.assertLess(self.geoms["F5W"]["cabin"], self.geoms["F5"]["cabin"])     # the same service floor on a wider cabin
        self.assertGreater(self.geoms["F5W"]["wetted"], self.geoms["F5"]["wetted"])

    def reference_by_hand(self):
        _, pressure, _ = cp.atmosphere(35000)
        q = 0.7 * pressure * 0.78 ** 2                                    # half of gamma times pressure times Mach squared
        lift = 0.95 * 50300 * G / (q * 92.5)
        aspect = 28.72 ** 2 / 92.5
        shape = (1 + 0.0019 * aspect) / ((1 - 2 * (3.18 / 28.72) ** 2) * math.pi * aspect)
        zero = (lift / 15 - 0.0010 - shape * lift ** 2) / (1 + 0.38 * lift ** 2)
        arm = 0.45 * 36.24
        tails = 1.0 * 92.5 * (1.05 * 92.5 / 28.72) / arm + 0.09 * 92.5 * 28.72 / arm
        wetted = (wetted_fuselage(3.18, 36.24) + 2.04 * 92.5 * (1 - 1.5 * 3.01 / 28.72) + 2.04 * tails) * 1.06
        return {"lift": lift, "shape": shape, "zero": zero, "wetted": wetted, "tails": tails, "arm": arm, "friction": zero * 92.5 / wetted}

    def test_skin_friction_set_on_the_jet_by_hand(self):
        hand = self.reference_by_hand()
        self.assertAlmostEqual(self.ref["friction"], hand["friction"], places=12)
        self.assertAlmostEqual(self.ref["friction"], 0.0033405, delta=1e-7)
        self.assertAlmostEqual(self.ref["wetted"] / 92.5, 6.29, delta=0.005)
        drag = hand["zero"] + 0.0010 + (hand["shape"] + 0.38 * hand["zero"]) * hand["lift"] ** 2
        self.assertAlmostEqual(hand["lift"] / drag, 15, places=9)         # the method gives the reference the ratio of the mission screening
        self.assertAlmostEqual(self.ref["best"], 1 / (2 * math.sqrt((hand["zero"] + 0.0010) * (hand["shape"] + 0.38 * hand["zero"]))), places=9)

    def test_masses_of_the_reference_by_hand(self):
        hand = self.reference_by_hand()
        wing = torenbeek_wing(40800, 92.5, 28.72, 23, 0.95)
        fuselage = 0.23 * math.sqrt(190 * hand["arm"] / (3.01 + 3.35)) * wetted_fuselage(3.18, 36.24) ** 1.2 * 1.08
        self.assertAlmostEqual(self.ref["masses"]["wing"], wing, places=6)
        self.assertAlmostEqual(wing, 4562.3, delta=0.1)
        self.assertAlmostEqual(self.ref["masses"]["fuselage"], fuselage, places=6)
        self.assertAlmostEqual(fuselage, 5577.9, delta=0.1)
        self.assertAlmostEqual(self.ref["masses"]["tails"], 27 * hand["tails"], places=6)
        self.assertAlmostEqual(self.ref["masses"]["gear"], 0.043 * 50300, places=6)
        self.assertAlmostEqual(self.ref["plant"], 0.0926 * 50300, places=6)
        self.assertAlmostEqual(self.ref["fixed"], 27753 - (wing + fuselage + 27 * hand["tails"] + 0.043 * 50300) - 0.0926 * 50300, places=6)
        self.assertAlmostEqual(self.ref["structure"] / 50300, 0.263, delta=0.001)          # the sample breakdown on record gives 0.2723

    def test_propeller_reference_is_met_by_hand(self):
        hand = self.reference_by_hand()
        arm = 0.45 * 27.17
        tails = 1.0 * 61 * (1.05 * 61 / 27.05) / arm + 0.09 * 61 * 27.05 / arm
        fuselage = wetted_fuselage(2.8, 27.17) * form(2.8, 27.17) / form(3.18, 36.24)
        wetted = (fuselage + 2.04 * 61 * (1 - 1.5 * 2.8 / 27.05) + 2.04 * tails) * 1.06
        aspect = 27.05 ** 2 / 61
        shape = (1 + 0.0019 * aspect) / ((1 - 2 * (2.8 / 27.05) ** 2) * math.pi * aspect)
        clean = hand["friction"] * wetted / 61
        self.assertAlmostEqual(self.ref["propeller_clean"], 1 / (2 * math.sqrt(clean * (shape + 0.38 * clean))), places=9)
        self.assertAlmostEqual(self.ref["propeller_clean"], 18.15, delta=0.01)
        raised = clean * self.ref["propeller"]
        self.assertAlmostEqual(1 / (2 * math.sqrt(raised * (shape + 0.38 * raised))), 15.74, places=9)     # the published best ratio
        self.assertAlmostEqual(self.ref["propeller"], 1.257, delta=0.001)

    def test_metric_of_the_reference_by_hand(self):
        co2, fitted = self.points["co2_metric"], mc.fit(self.missions)["product"]
        masses = cp.reference_masses(co2["reference_masses"], 50300)

        def margin(product):
            return 1000 * G / (product * 43.0e6) * sum(masses) / 3 / (3.01 * 25.91) ** 0.24 / cp.metric_limit(co2["limit"], 50300) - 1

        self.assertAlmostEqual(self.ref["cruise_margin"], margin(fitted), places=9)
        self.assertAlmostEqual(self.ref["margin"], margin(fitted * self.ref["best"] / 15), places=9)
        self.assertAlmostEqual(self.ref["margin"], 0.0855, delta=0.0005)
        self.assertAlmostEqual(self.ref["expected"], 0.89 / 0.827 - 1, places=9)           # 11 % below, and 17.3 % less fuel than the reference
        self.assertLess(abs(self.ref["margin"] - self.ref["expected"]), 0.01)

    def test_certified_turboprop_by_hand(self):
        sure, co2 = self.ref["certified"], self.points["co2_metric"]
        floor = 2.8 * (18 * 0.737 + 15.9 / 2.57)                           # 18 rows of four, and the service floor of the screening, on the width of the type
        self.assertAlmostEqual(sure["floor"], floor, places=9)
        self.assertAlmostEqual(floor, 54.5, delta=0.05)
        product = 1000 * G * sum(cp.reference_masses(co2["reference_masses"], 23000)) / 3 / (43.0e6 * 0.404 * floor ** 0.24)
        self.assertAlmostEqual(sure["product"], product, places=9)
        self.assertAlmostEqual(product, 4.14, delta=0.005)
        self.assertAlmostEqual(sure["efficiency"], product / 15.74, places=12)             # at the best ratio the propeller points are set on
        self.assertAlmostEqual(sure["efficiency"], 0.263, delta=0.0005)
        self.assertAlmostEqual(sure["share"], 0.404 / 0.507, places=12)                     # 79.7 % of the new-type level
        self.assertAlmostEqual(sure["limit"], 0.507, delta=0.0005)                          # the limit formula on record gives the limit the regulator prints
        self.assertAlmostEqual(sure["loading"], 23000 / floor, places=9)
        nominal = 0.35 * 0.90 * 0.85                                                        # the nominal chain is within 2 % of what the certified type shows
        self.assertLess(abs(nominal / sure["efficiency"] - 1), 0.02)

    def test_certified_jet_by_hand(self):
        jet, co2 = self.ref["certified_jet"], self.points["co2_metric"]
        floor = (3.28 + 2 * 0.135) * (24 * 0.82 + 15.9 / 3.28)             # 24 rows of five at the pitch of the screening
        self.assertAlmostEqual(jet["floor"], floor, places=9)
        self.assertAlmostEqual(floor, 87.1, delta=0.05)
        product = 1000 * G * sum(cp.reference_masses(co2["reference_masses"], 63730)) / 3 / (43.0e6 * 0.677 * floor ** 0.24)
        self.assertAlmostEqual(jet["product"], product, places=9)
        self.assertAlmostEqual(product, 6.03, delta=0.005)
        self.assertAlmostEqual(jet["share"], 0.677 / 0.764, places=12)                      # 88.6 % of the new-type level
        self.assertGreater(jet["product"], 1.4 * self.ref["certified"]["product"])          # the jet of today against the turboprop of today

    def test_floor_of_a_certified_type_counts_whole_rows(self):
        co2, cabin = self.points["co2_metric"], cs.values(self.a["cabin"])
        x = {"seats": 74, "seat_pitch_m": 0.8, "cabin_width_m": 2.5, "certified_mtom_kg": 23000, "certified_metric_kg_km": 0.4}
        floor, _ = cs.certified_product(co2, 43.0e6, cabin, x, 4, 2.8)
        self.assertAlmostEqual(floor, 2.8 * (19 * 0.8 + 15.9 / 2.5), places=9)                # 74 seats four abreast take 19 rows

    def test_shorter_requirement_mission_makes_a_lighter_aircraft(self):
        case = {"name": "x", "set": [{"where": "missions", "path": "missions.L", "field": "range_km", "value": 1596}]}
        b, flown, at, failure = cs.changed(self.a, self.missions, self.points, case)
        self.assertIsNone(failure)
        rows = {(x["tech"], x["section"], x["wing"], x["point"]): x for x in cs.compute(b, flown, at, mechanical=False)[2]}
        key = ("T1", "F4", "WA", "P2")
        self.assertLess(rows[key]["takeoff"], self.grid[key]["takeoff"] - 300)
        self.assertLess(rows[key]["loaded"], self.grid[key]["loaded"])
        self.assertLess(rows[key]["margin"], self.grid[key]["margin"])

    def test_fuel_a_wing_holds_is_checked_on_the_successor(self):
        self.assertAlmostEqual(self.ref["successor_holds"], 12971 * (103 ** 2 / 33.72) / (92.5 ** 2 / 28.72), places=6)
        self.assertLess(abs(self.ref["successor_holds"] / 13500 - 1), 0.02)

    def test_one_aircraft_by_hand(self):
        x, ref = self.grid[("T0", "F4", "WA", "P2")], self.ref
        takeoff, empty, payload = x["takeoff"], x["empty"], 100 * 95
        self.assertAlmostEqual(takeoff, 52928.3, delta=0.1)
        area = takeoff / 560
        span = math.sqrt(11.5 * area)
        height = 3.01 * 1.113
        d = (3.01 + height) / 2
        cabin = 25 * 0.82 + 15.9 / 2.74
        length = cabin + 3.17 + 2.25 * d
        arm = 0.45 * length
        tails = 1.0 * area * (1.05 * area / span) / arm + 0.09 * area * span / arm
        wetted = (wetted_fuselage(d, length) * form(d, length) / form(3.18, 36.24) + 2.04 * area * (1 - 1.5 * 3.01 / span) + 2.04 * tails) * 1.06
        t, pressure, _ = cp.atmosphere(25000)
        v = 360 * 1852 / 3600
        q = 0.5 * pressure / (287.05287 * t) * v ** 2
        lift = 0.95 * takeoff * G / (q * area)
        zero = ref["friction"] * wetted / area * ref["propeller"]         # a propeller point: the drag level of the turboprop in service
        slope = (1 + 0.0019 * 11.5) / ((1 - 2 * (d / span) ** 2) * math.pi * 11.5) + 0.38 * zero
        ratio = lift / (zero + slope * lift ** 2)
        self.assertAlmostEqual(x["ratio"], ratio, places=9)
        self.assertAlmostEqual(ratio, 14.45, delta=0.01)
        per_km = 1000 * G / (0.35 * 0.90 * 0.85 * ratio * 43.0e6)
        model = mc.Model(self.missions, "nominal")
        flown = {m["role"]: m for m in self.missions["missions"]}
        fraction = 1 - math.exp(-model.equivalent_km(flown["requirement"]) * per_km)
        self.assertAlmostEqual((empty + payload) / (1 - fraction), takeoff, delta=0.02)          # the take-off mass closes the requirement mission
        masses = {"gear": 0.043 * takeoff, "propulsion": 0.0926 * 50300 * takeoff / 50300 * 2.27, "rest": ref["fixed"], "tails": 27 * tails,
                  "fuselage": 0.23 * math.sqrt(190 * arm / (3.01 + height)) * wetted_fuselage(d, length) ** 1.2 * 1.08,
                  "wing": torenbeek_wing(empty + payload, area, span, 0, 0.90)}
        for k, mass in masses.items():
            self.assertAlmostEqual(x["masses"][k], mass, delta=0.01, msg=k)
        self.assertAlmostEqual(sum(masses.values()), empty, delta=0.02)
        scored = 1 - math.exp(-model.equivalent_km(flown["scoring"]) * per_km)
        self.assertAlmostEqual(x["scoring"], (empty + payload) * scored / (1 - scored), delta=0.01)
        best = 1 / (2 * math.sqrt(zero * slope))                                                  # the metric is taken at the best ratio
        co2 = self.points["co2_metric"]
        metric = 1000 * G / (0.35 * 0.90 * 0.85 * best * 43.0e6) * sum(cp.reference_masses(co2["reference_masses"], takeoff)) / 3 / (3.01 * cabin) ** 0.24
        self.assertAlmostEqual(x["margin"], metric / cp.metric_limit(co2["limit"], takeoff) - 1, places=6)
        self.assertAlmostEqual(x["margin"], 0.1477, delta=0.0005)
        self.assertAlmostEqual(x["holds"], 12971 * (area ** 2 / span) / (92.5 ** 2 / 28.72), delta=0.01)
        self.assertAlmostEqual(x["loaded"], takeoff * fraction, delta=0.01)

    def test_mechanical_drive_by_hand(self):
        tech = next(t for t in self.a["technology"] if t["key"] == "T0")
        point = next(p for p in self.points["points"] if p["key"] == "P2")
        wing = next(w for w in self.a["wings"] if w["key"] == "WA")
        model = mc.Model(self.missions, "nominal")
        x = cs.evaluate(self.a, self.missions, model, self.points["co2_metric"], self.ref, self.geoms["F4"], wing, point, tech, mechanical=True)
        self.assertAlmostEqual(x["chain"], 0.35 / 0.97 * 0.98 * 0.85, places=12)                   # the shaft of the thermal machine, a gearbox, the propeller
        self.assertAlmostEqual(x["masses"]["propulsion"], 0.0926 * x["takeoff"], delta=0.01)       # the power plant of the reference, in proportion
        self.assertAlmostEqual(x["masses"]["wing"], torenbeek_wing(x["empty"] + 9500, x["area"], x["span"], 0, 0.95), delta=0.01)     # two engines on the wing
        self.assertAlmostEqual(x["margin"], self.grid[("T0", "F4", "WA", "P2")]["mechanical"], places=12)
        self.assertTrue(all(r["mechanical"] < r["margin"] for r in self.rows))

    def test_jet_point_by_hand(self):
        x = self.grid[("T0", "F4", "WA", "P4")]
        _, pressure, _ = cp.atmosphere(35000)
        lift = 0.95 * x["takeoff"] * G / (0.7 * pressure * 0.78 ** 2 * x["area"])
        zero = self.ref["friction"] * sum(x["parts"].values()) / x["area"]                         # the drag level of the jet
        slope = (1 + 0.0019 * 11.5) / ((1 - 2 * (self.geoms["F4"]["d"] / x["span"]) ** 2) * math.pi * 11.5) + 0.38 * zero
        self.assertAlmostEqual(x["ratio"], lift / (zero + 0.0010 + slope * lift ** 2), places=9)   # ten counts of wave drag
        self.assertAlmostEqual(x["best"], 1 / (2 * math.sqrt((zero + 0.0010) * slope)), places=9)
        self.assertAlmostEqual(x["masses"]["wing"], torenbeek_wing(x["empty"] + 9500, x["area"], x["span"], 23, 0.90), delta=0.01)    # a swept wing
        self.assertAlmostEqual(x["chain"], 0.35 * 0.90 * 0.76, places=12)                          # a fan

    def test_metric_is_taken_at_the_best_ratio(self):
        self.assertTrue(all(x["best"] >= x["ratio"] for x in self.rows))
        jet = self.grid[("T0", "F4", "WA", "P4")]
        self.assertTrue(jet["swept"] and not self.grid[("T0", "F4", "WA", "P2")]["swept"])
        self.assertAlmostEqual(jet["zero"], self.ref["friction"] * sum(jet["parts"].values()) / jet["area"], places=12)     # no propeller excess at the jet point

    def test_floor_of_speed(self):
        self.assertEqual({x["point"] for x in self.rows if not x["floor"]}, {"P1"})
        self.assertTrue(self.grid[("T0", "F4", "WA", "P2")]["floor"])                              # 360 kt is at the floor

    def test_objective_count(self):
        met = {t: sum(1 for x in cs.at_floor(self.rows, t) if x["margin"] <= -0.26) for t in ("T0", "T1", "T2")}
        self.assertEqual(met, {"T0": 0, "T1": 0, "T2": 2})

    def test_brace_takes_its_share_off_the_wing(self):
        m, d = cs.values(self.a["mass"]), cs.values(self.a["drag"])
        self.assertAlmostEqual(cs.wing_mass(m, d, 40000, 80, 36, 0, 0.9, True), 0.77 * cs.wing_mass(m, d, 40000, 80, 36, 0, 0.9, False), places=9)

    def test_drag_due_to_lift_falls_with_the_aspect_ratio_and_rises_with_the_fuselage(self):
        d = cs.values(self.a["drag"])
        self.assertLess(cs.lift_factor(d, 17, 3.2, 36), cs.lift_factor(d, 11.5, 3.2, 36))
        self.assertGreater(cs.lift_factor(d, 14, 3.9, 30), cs.lift_factor(d, 14, 3.2, 30))

    def test_braced_wing_pays_for_its_brace_in_wetted_area(self):
        braced, plain = self.grid[("T0", "F4", "WC", "P2")]["parts"], self.grid[("T0", "F4", "WB", "P2")]["parts"]
        self.assertAlmostEqual(braced["brace"], 0.15 * braced["wing"], places=9)
        self.assertEqual(plain["brace"], 0.0)

    def test_code_letters(self):
        self.assertEqual([cs.code_letter(s) for s in (23.99, 24, 35.99, 36, 51.99, 52)], ["B", "C", "C", "D", "D", "E"])

    def test_lookup_enters_lists_by_key(self):
        self.assertEqual(cs.lookup(self.a, "wings.WC.aspect_ratio")["value"], 17)
        self.assertIsNone(cs.lookup(self.a, "wings.WZ.aspect_ratio"))
        self.assertIsNone(cs.lookup(self.a, "id.version"))

    def test_sensitivity_changes_copies_only(self):
        case = {"name": "x", "set": [{"path": "wings.WC.aspect_ratio", "value": 20}, {"where": "points", "path": "points.P2.altitude_ft", "value": 31000},
                                    {"where": "missions", "path": "parameters.lift_to_drag", "field": "nominal", "value": 14}]}
        b, flown, at, failure = cs.changed(self.a, self.missions, self.points, case)
        self.assertIsNone(failure)
        self.assertEqual((cs.lookup(b, "wings.WC.aspect_ratio")["value"], cs.lookup(at, "points.P2.altitude_ft")["value"], flown["parameters"]["lift_to_drag"]["nominal"]), (20, 31000, 14))
        self.assertEqual((cs.lookup(self.a, "wings.WC.aspect_ratio")["value"], cs.lookup(self.points, "points.P2.altitude_ft")["value"],
                          self.missions["parameters"]["lift_to_drag"]["nominal"]), (17, 25000, 15))

    def test_higher_cruise_at_the_same_speed_saves_fuel_and_leaves_the_metric(self):
        case = {"name": "x", "set": [{"where": "points", "path": "points.P2.altitude_ft", "value": 31000}]}
        b, flown, at, _ = cs.changed(self.a, self.missions, self.points, case)
        rows = {(x["tech"], x["section"], x["wing"], x["point"]): x for x in cs.compute(b, flown, at, mechanical=False)[2]}
        key = ("T1", "F4", "WA", "P2")
        self.assertLess(rows[key]["scoring"], 0.97 * self.grid[key]["scoring"])
        self.assertAlmostEqual(rows[key]["margin"], self.grid[key]["margin"], delta=0.01)

    def test_jet_reference_does_not_move_the_propeller_points(self):
        case = {"name": "x", "set": [{"where": "missions", "path": "parameters.lift_to_drag", "field": "nominal", "value": 14}]}
        b, flown, at, _ = cs.changed(self.a, self.missions, self.points, case)
        ref, _, found = cs.compute(b, flown, at, mechanical=False)
        rows = {(x["tech"], x["section"], x["wing"], x["point"]): x for x in found}
        self.assertGreater(ref["friction"], self.ref["friction"])
        self.assertAlmostEqual(rows[("T1", "F4", "WA", "P2")]["scoring"], self.grid[("T1", "F4", "WA", "P2")]["scoring"], delta=0.5)     # set on the turboprop
        self.assertGreater(rows[("T1", "F4", "WA", "P4")]["scoring"], 1.03 * self.grid[("T1", "F4", "WA", "P4")]["scoring"])


class Changed(unittest.TestCase):
    """One input changed at a time, in a copy of the register."""

    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.reg = self.tmp / "register"
        shutil.copytree(REG, self.reg)
        self.cfg = self.reg / "000_General" / "evidence" / "CFG-EWTW-AER-001"
        self.path = self.cfg / "configuration.yaml"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def edit(self, change):
        doc = yaml.safe_load(self.path.read_text(encoding="utf-8"))
        change(doc["analysis"])
        self.path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")

    def fails(self, fragment):
        bad, lines = cs.run(self.cfg, self.reg)
        self.assertTrue(any(fragment in b for b in bad), f"expected {fragment!r} in {bad}")
        self.assertEqual(len(lines), 1, "a failing run prints only its first line")

    def rows(self):
        a, missions, points = inputs(self.cfg)
        return {(x["tech"], x["section"], x["wing"], x["point"]): x for x in cs.compute(a, missions, points, mechanical=False)[2]}

    def test_copy_passes(self):
        bad, lines = cs.run(self.cfg, self.reg, "check")
        self.assertEqual((bad, lines[0]), ([], HEAD))

    def test_generated_section_is_checked_and_written(self):
        self.edit(lambda a: a["wings"][2]["aspect_ratio"].update(value=18))
        bad, _ = cs.run(self.cfg, self.reg, "check")
        self.assertTrue(any("differs from the output" in b for b in bad))
        self.assertEqual(cs.run(self.cfg, self.reg, "write")[0], [])
        self.assertEqual(cs.run(self.cfg, self.reg, "check")[0], [])

    def test_heavier_chain_makes_a_heavier_aircraft_that_burns_more(self):
        before = self.rows()[("T0", "F5", "WB", "P3")]
        self.edit(lambda a: a["technology"][0]["chain_mass_ratio"].update(value=3.0))
        after = self.rows()[("T0", "F5", "WB", "P3")]
        self.assertGreater(after["takeoff"], before["takeoff"] + 1000)
        self.assertGreater(after["scoring"], before["scoring"])

    def test_less_drag_and_less_mass_improve_the_margin(self):
        before = self.rows()[("T0", "F4", "WA", "P2")]
        self.edit(lambda a: (a["technology"][0]["drag_factor"].update(value=0.9), a["technology"][0]["empty_factor"].update(value=0.9)))
        after = self.rows()[("T0", "F4", "WA", "P2")]
        self.assertLess(after["margin"], before["margin"] - 0.10)
        self.assertLess(after["empty"], before["empty"])

    def test_propeller_points_can_be_given_the_drag_of_the_jet(self):
        before = self.rows()[("T1", "F4", "WA", "P2")]
        self.edit(lambda a: a["drag"]["propeller_drag_share"].update(value=0.001))
        after = self.rows()[("T1", "F4", "WA", "P2")]
        self.assertLess(after["scoring"], 0.90 * before["scoring"])

    def test_input_section_is_required(self):
        self.edit(lambda a: a.pop("mechanical"))
        self.fails("`mechanical` is missing")

    def test_figure_of_a_section_is_required(self):
        self.edit(lambda a: a["drag"].pop("viscous_factor"))
        self.fails("drag: `viscous_factor` is a figure")

    def test_certified_types_are_complete(self):
        self.edit(lambda a: a["certified_jet"].pop("certified_metric_kg_km"))
        self.fails("certified_jet: `certified_metric_kg_km` is a figure")

    def test_certified_types_are_named_and_seated(self):
        self.edit(lambda a: a["propeller_reference"].update(abreast=0))
        self.fails("propeller_reference: it seats a whole number of passengers abreast and names the type certified")

    def test_figure_read_at_a_source_names_it(self):
        self.edit(lambda a: a["mass"]["tail_kg_m2"].pop("ref"))
        self.fails("a figure needs a positive value")

    def test_assumption_carries_a_note(self):
        self.edit(lambda a: a["drag"]["wave_counts"].pop("note"))
        self.fails("a figure needs a positive value")

    def test_figure_is_positive(self):
        self.edit(lambda a: a["wings"][0]["loading_kg_m2"].update(value=0))
        self.fails("a figure needs a positive value")

    def test_objective_is_a_share(self):
        self.edit(lambda a: a["objective"]["below"].update(value=1.2))
        self.fails("objective: below is a share between 0 and 1")

    def test_section_names_an_open_option_of_its_knot(self):
        self.edit(lambda a: a["sections"][0].update(option="Z"))
        self.fails("sections: F4 names option Z of KNOT-EWTW-FUS-001, which is not an open option")

    def test_open_option_is_screened_or_named(self):
        self.edit(lambda a: a.update(not_screened=[]))
        self.fails("KNOT-EWTW-FUS-001: option C is open and is neither screened nor named in not_screened")

    def test_keys_are_unique(self):
        self.edit(lambda a: a["wings"][1].update(key="WA"))
        self.fails("wings: each has a key of its own and a name")

    def test_wing_says_whether_it_is_braced(self):
        self.edit(lambda a: a["wings"][2].update(braced="yes"))
        self.fails("wings: WC says whether it is braced")

    def test_serves_knus_of_the_register(self):
        self.edit(lambda a: a.update(serves=["KNU-EWTW-AER-001-02", "KNU-EWTW-AER-001-99"]))
        self.fails("serves: KNU-EWTW-AER-001-99 is not a KNU of the register")

    def test_sensitivity_names_a_figure_of_the_inputs(self):
        self.edit(lambda a: a["sensitivities"][2]["set"][0].update(path="drag.no_such_figure"))
        self.fails("sensitivities: `drag.no_such_figure` is not a figure of the inputs")

    def test_sensitivity_that_gives_no_aircraft_is_a_failure(self):
        self.edit(lambda a: a["sensitivities"][0]["set"][0].update(value=60))                     # a jet reference no wetted area can give
        self.fails("gives no aircraft")

    def test_sensitivity_has_a_name_and_figures(self):
        self.edit(lambda a: a["sensitivities"][0].update(set=[]))
        self.fails("sensitivities: each case has a name and a list of figures to set")

    def test_skin_friction_stays_in_the_range_of_its_source(self):
        self.edit(lambda a: a["drag"]["skin_friction_high"].update(value=0.0033))
        self.fails("leaves the range of its source")

    def test_screenings_it_reads_are_found_and_sound(self):
        self.edit(lambda a: a.update(cruise_points="CRP-EWTW-CRZ-999"))
        self.fails("cruise_points names the folder of a screening beside this one")
        self.edit(lambda a: a.update(cruise_points="CRP-EWTW-CRZ-001"))
        missions = self.cfg.parent / "MSN-EWTW-NRG-001" / "missions.yaml"
        missions.write_text(missions.read_text(encoding="utf-8").replace("kg_per_passenger", "kg_each"), encoding="utf-8")
        self.fails("the screening MSN-EWTW-NRG-001 fails its own check")

    def test_arguments(self):
        self.assertEqual(cs.main(["configuration_screen.py", str(self.cfg)]), 2)
        self.assertEqual(cs.main(["configuration_screen.py", str(self.cfg), str(self.reg), "--print"]), 2)


if __name__ == "__main__":
    unittest.main()
