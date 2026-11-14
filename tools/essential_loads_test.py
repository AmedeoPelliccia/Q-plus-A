# Generated 2026-11-14 - essential_loads_test.py (0.1.0)
"""Tests of tools/essential_loads.py on the essential load analysis of the eWTW. Run from the repository root:

    python3 tools/essential_loads_test.py

Each test copies the analysis and the KNOT register to a temporary folder, changes one input
and expects the matching result. The arithmetic of the committed input is computed again by hand.
"""
import pathlib
import shutil
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import essential_loads as el  # noqa: E402

MODEL = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW")
REG = MODEL / "01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
ELA = REG / "000_General" / "evidence" / "ELA-EWTW-ESS-001"
TAX = pathlib.Path("01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_S-ATLAS")


class EssentialLoads(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.ela, self.reg = self.tmp / "analysis", self.tmp / "register"
        shutil.copytree(ELA, self.ela)
        shutil.copytree(REG, self.reg)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def edit(self, path, key, change):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        change(doc[key])
        path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")

    def analysis(self, change):
        self.edit(self.ela / "essential-loads.yaml", "analysis", change)

    def knot(self, change):
        self.edit(next(self.reg.rglob("KNOT-EWTW-ESS-001.yaml")), "knot", change)

    def run_tool(self, mode=None):
        return el.run(self.ela, self.reg, TAX, mode=mode)

    def fails(self, fragment):
        bad, lines = self.run_tool()
        self.assertTrue(any(fragment in b for b in bad), f"expected {fragment!r} in {bad}")
        self.assertEqual(len(lines), 1, "no budget is printed after a failure")

    def load(self, ident, **fields):
        self.analysis(lambda a: next(x for x in a["loads"] + a["events"] if x["id"] == ident).update(fields))

    def budget(self, cases=()):
        a = yaml.safe_load((self.ela / "essential-loads.yaml").read_text(encoding="utf-8"))["analysis"]
        return el.budget(a, cases)

    def one_load(self, a):
        """Reduce the analysis to one load of 900 W, with no event and no loss, for arithmetic that can be read."""
        a["loads"] = [dict(a["loads"][0], power_w={"low": 450, "nominal": 900, "high": 1800})]
        a["events"] = []
        a["parameters"]["battery_factors"] = [dict(a["parameters"]["battery_factors"][0], value=0.5)]
        a["parameters"]["specific_energy_wh_per_kg"].update(low=100, nominal=150, high=200)

    # the analysis as committed
    def test_committed_analysis_passes_and_its_readme_is_current(self):
        bad, lines = el.run(ELA, REG, TAX, mode="check")
        self.assertEqual(bad, [])
        self.assertTrue(lines[0].endswith("37 figures, 35 of them assumptions; rule failures: none"), lines[0])

    def test_continuous_totals_are_the_sums_of_the_list(self):
        a = yaml.safe_load((ELA / "essential-loads.yaml").read_text(encoding="utf-8"))["analysis"]
        by_hand = {level: sum(x["power_w"][level] * x["duty"] for x in a["loads"] if x["when"] == "always") for level in el.LEVELS}
        self.assertEqual(by_hand, {"low": 1865, "nominal": 4190, "high": 10230})
        self.assertEqual({level: b["at_loads_w"] for level, b in el.budget(a).items()}, by_hand)

    def test_committed_budget_by_hand(self):
        b = self.budget()["nominal"]
        self.assertAlmostEqual(b["source_w"], 4190 / 0.9)
        self.assertAlmostEqual(b["event_wh"], (500 * 15 + 3000 * 40 + 3000 * 60 + 4000 * 5 * 20) / 3600 / 0.9)
        self.assertAlmostEqual(b["peak_w"], (4190 + 4000) / 0.9)
        whole, bridge = b["durations"]["endurance"], b["durations"]["bridge"]
        self.assertAlmostEqual(whole["energy_wh"], 4190 / 0.9 + b["event_wh"])
        self.assertAlmostEqual(whole["nameplate_wh"], whole["energy_wh"] / (0.9 * 0.95 * 0.8 * 0.9))
        self.assertAlmostEqual(bridge["energy_wh"], 4190 / 0.9 / 6, msg="the bridge excludes the events of the landing")
        self.assertAlmostEqual(bridge["rate"], 6 * 0.9 * 0.95 * 0.8 * 0.9)

    def test_loads_outside_the_scope_of_the_knot(self):
        self.assertIn("Chapters of loads outside the `taxonomy` field of `KNOT-EWTW-ESS-001`: "
                      "`021` · `027` · `029` · `030` · `032` · `033` · `064` · `068` · `074` · `077`.", self.run_tool()[1])
        self.knot(lambda k: k["taxonomy"].extend(["021", "027", "029", "030", "032", "033", "064", "068", "074", "077"]))
        self.assertIn("Chapters of loads outside the `taxonomy` field of `KNOT-EWTW-ESS-001`: none.", self.run_tool()[1])

    # arithmetic on one load
    def test_energy_nameplate_and_mass_of_one_load(self):
        self.analysis(self.one_load)
        b = self.budget()["nominal"]
        self.assertAlmostEqual(b["source_w"], 1000)
        self.assertAlmostEqual(b["durations"]["endurance"]["energy_wh"], 1000)
        self.assertAlmostEqual(b["durations"]["floor"]["energy_wh"], 500)
        self.assertAlmostEqual(b["durations"]["endurance"]["nameplate_wh"], 2000)
        row = next(line for line in self.run_tool()[1] if line.startswith("| Whole endurance on the store"))
        self.assertIn("| 1.00 · 2.00 · 4.00 | 13 | 5–40 | 0.5 |", row, "mass at 150 Wh/kg; range from low loads at 200 to high loads at 100")

    def test_duty_scales_a_load(self):
        self.analysis(self.one_load)
        self.load("L01", duty=0.5)
        self.assertAlmostEqual(self.budget()["nominal"]["source_w"], 500)

    def test_event_adds_energy_and_peak_but_not_continuous_load(self):
        self.analysis(self.one_load)
        self.analysis(lambda a: a["events"].append({"id": "E01", "service": "safe-landing", "tier": "landing", "item": "Braking", "taxonomy": "032",
                                                    "power_w": {"low": 0, "nominal": 1800, "high": 1800}, "seconds": 90, "count": 2,
                                                    "when": "always", "basis": "assumption"}))
        b = self.budget()["nominal"]
        self.assertAlmostEqual(b["source_w"], 1000)
        self.assertAlmostEqual(b["event_wh"], 100)
        self.assertAlmostEqual(b["peak_w"], 3000)
        self.assertAlmostEqual(b["durations"]["endurance"]["energy_wh"], 1100)
        self.assertAlmostEqual(b["durations"]["bridge"]["energy_wh"], 1000 / 6)

    def test_case_load_counts_only_in_its_case(self):
        self.assertAlmostEqual(self.budget(("icing",))["nominal"]["at_loads_w"] - self.budget()["nominal"]["at_loads_w"], 1250)
        self.assertAlmostEqual(self.budget(("turbogenerator",))["nominal"]["at_loads_w"] - self.budget()["nominal"]["at_loads_w"], 500)
        self.assertIn("| base + icing + turbogenerator | 1750 | 6.60 | 11.09 | 85 |", self.run_tool()[1])

    # form of the input
    def test_range_out_of_order(self):
        self.load("L03", power_w={"low": 600, "nominal": 550, "high": 900})
        self.fails("L03: power_w holds low, nominal and high, none negative and in that order")

    def test_negative_power(self):
        self.load("E02", power_w={"low": -1, "nominal": 3000, "high": 6000})
        self.fails("E02: power_w holds low, nominal and high")

    def test_address_outside_the_taxonomy(self):
        self.load("L10", taxonomy="129")
        self.fails("L10: 129 is not an S-ATLAS address")

    def test_duty_and_feeds(self):
        self.load("L04", duty=0)
        self.fails("L04: duty is above 0 and at most 1")
        self.load("L04", duty=1.0, feeds=0)
        self.fails("L04: duty is above 0 and at most 1, and feeds is 1, 2 or 3")

    def test_undeclared_case_and_unknown_tier(self):
        self.load("L21", when="snow")
        self.fails("L21: when is `always` or a declared case")
        self.load("L21", when="icing", tier="cruise")
        self.fails("L21: tier is one of")

    def test_identifier_used_twice(self):
        self.load("L02", id="L01")
        self.fails("L01: the identifier is used more than once")

    def test_figure_with_a_source_names_it(self):
        self.load("L10", basis="design")
        self.fails("L10: a figure with basis design names its reference in ref")
        self.load("L10", ref="Actuation load analysis, issue 1")
        bad, lines = self.run_tool()
        self.assertEqual(bad, [])
        self.assertIn("37 figures, 34 of them assumptions", lines[0])

    def test_basis_outside_the_vocabulary(self):
        self.load("L10", basis="estimate")
        self.fails("L10: basis is one of assumption, source, design")

    def test_event_without_duration(self):
        self.load("E01", seconds=0)
        self.fails("E01: seconds is positive and count is a whole number of at least 1")

    def test_factor_above_one(self):
        self.analysis(lambda a: a["parameters"]["battery_factors"][0].update(value=1.2))
        self.fails("battery_factors: each has a key, a text and a value above 0 and at most 1")
        self.analysis(lambda a: a["parameters"]["battery_factors"][0].update(value=0.9))
        self.analysis(lambda a: a["parameters"]["distribution_efficiency"].update(value=0))
        self.fails("distribution_efficiency: the value is above 0 and at most 1")

    def test_duration_names_a_standing_option(self):
        self.knot(lambda k: next(o for o in k["options"] if o["id"] == "E").update(state="rejected"))
        self.fails("duration endurance: E is not a standing option of KNOT-EWTW-ESS-001")

    def test_no_load_always_on(self):
        self.analysis(lambda a: [x.update(when="icing") for x in a["loads"]])
        self.fails("loads: at least one load is always on")

    def test_missing_section_and_wrong_types(self):
        self.analysis(lambda a: a.pop("events"))
        self.fails("`analysis` must hold")
        shutil.copy(ELA / "essential-loads.yaml", self.ela / "essential-loads.yaml")
        self.analysis(lambda a: a.update(loads="none"))
        self.fails("loads: each record has text in")
        shutil.copy(ELA / "essential-loads.yaml", self.ela / "essential-loads.yaml")
        self.analysis(lambda a: a.update(parameters=[]))
        self.fails("parameters: durations, distribution_efficiency")

    def test_inputs_that_cannot_be_read(self):
        (self.ela / "essential-loads.yaml").write_text("analysis: [unclosed", encoding="utf-8")
        self.fails("essential-loads.yaml: cannot be read as YAML")
        shutil.copy(ELA / "essential-loads.yaml", self.ela / "essential-loads.yaml")
        self.analysis(lambda a: a.update(knot="KNOT-EWTW-XXX-001"))
        self.fails("KNOT-EWTW-XXX-001: expected in one file of the register, found in 0")

    # the generated section
    def test_stale_readme_fails_the_check_and_is_rewritten(self):
        self.load("L10", power_w={"low": 600, "nominal": 2500, "high": 5000})
        bad, _ = self.run_tool("check")
        self.assertEqual(bad, ["README.md: the generated section differs from the output; run again with --write"])
        self.assertEqual(self.run_tool("write")[0], [])
        self.assertEqual(self.run_tool("check")[0], [])
        text = (self.ela / "README.md").read_text(encoding="utf-8")
        self.assertIn("| **Total at the loads** | 20 | 1865 | 5190 | 10230 | 100% |", text)
        self.assertTrue(text.startswith("---\nstatus: draft") and "## Revision history" in text, "the rest of the README is kept")

    def test_control_characters_are_printed_escaped(self):
        self.load("L01", item="Displays‮\x1b[2J | forged")
        bad, lines = self.run_tool()
        self.assertEqual(bad, [])
        row = next(line for line in lines if line.startswith("| L01 "))
        self.assertIn("Displays\\x202e\\x1b[2J / forged", row)
        self.assertEqual(row.count("|"), 13, "a bar in the text does not add a column")


if __name__ == "__main__":
    unittest.main()
