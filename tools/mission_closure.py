# Generated 2026-11-14 - mission_closure.py (0.3.0)
"""First-order closure of candidate missions: which energy carrier flies each mission in an airframe of the class.

    python3 tools/mission_closure.py <analysis folder> <KNOT register> [--check | --write]

Reads missions.yaml in the analysis folder, checks its form and prints the screening. The README of the folder holds
the output between two markers: --check fails when it differs, --write replaces it. The test is a range equation.
It is first fitted to the published block fuel of a reference aircraft, and checked on one point outside the fit.
It then runs at three sets of parameters: favourable, nominal and unfavourable. It sizes no aircraft and states no
conformity. It exits with status 1 on a failure and then prints only its first line.

Options are those of the energy-carrier KNOT: A batteries alone, B fuel for a turbogenerator, C both.
"""
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import relations_project as rp  # noqa: E402

G, NM, LB = 9.80665, 1.852, 0.45359237                   # m/s2, km in a nautical mile, kg in a pound
SETS = ("favourable", "nominal", "unfavourable")
BASES = ("assumption", "source", "decision")
ROLES = ("requirement", "scoring", "sensitivity", "reference")   # reference: a point of comparison, not a mission of the aircraft
PARAMETERS = ("lift_to_drag", "propulsor_efficiency", "electric_chain_efficiency", "turbogenerator_efficiency",
              "pack_usable_share", "terminal_share", "empty_mass_share", "takeoff_kw_per_kg")
SHARES = PARAMETERS[1:5]                                # parameters that lie above 0 and below 1
SECTIONS = ("id", "version", "date", "knot", "serves", "scope", "assumptions", "reference", "missions", "payload", "reserves",
            "fuel_energy_mj_per_kg", "empty_growth_share", "parameters", "pack_levels", "hybrid_shares", "units")
SINGLES = (("payload", "kg_per_passenger"), ("reserves", "contingency_share"), ("reserves", "alternate_km"),
           ("reserves", "final_reserve_min"), ("reserves", "holding_speed_kmh"), ("units", "motor_kw"), ("units", "turbogenerator_kw"),
           ("reference", "basic_operating_kg"), ("reference", "sizing_takeoff_kg"), ("reference", "takeoff_limit_kg"), ("reference", "fuel_lb_per_usg"))
BEGIN, END = "<!-- screening:begin -->", "<!-- screening:end -->"


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def figures(a):
    """Every record of the input that carries a figure, with a label."""
    ref = a["reference"]
    return ([(f"{s}.{k}", a[s][k]) for s, k in SINGLES] + [(k, a[k]) for k in ("fuel_energy_mj_per_kg", "empty_growth_share")]
            + [("reference.sectors", {"basis": "source", "ref": ref.get("sectors_ref")}), ("reference.range_check", dict(ref["range_check"], basis="source"))]
            + [(k, a["parameters"][k]) for k in PARAMETERS] + [(f"mission {m['key']}", m) for m in a["missions"]]
            + [(f"pack level {p['wh_per_kg']:g}", p) for p in a["pack_levels"]])


def validate(a, knot):
    """Failures of form. The screening is computed only when this returns none."""
    if not isinstance(a, dict) or [s for s in SECTIONS if s not in a]:
        return ["missions.yaml: `analysis` must hold " + ", ".join(SECTIONS)]
    if not all(rp.has_text(a[k]) for k in ("id", "version", "knot", "serves", "scope")) or not rp.checked_date(a["date"]):
        return ["missions.yaml: id, version, knot, serves and scope are text, and date is a date"]
    bad = []
    if not rp.is_list_of(a["assumptions"], dict) or not all(rp.has_text(x.get("id")) and rp.has_text(x.get("text")) for x in a["assumptions"]):
        bad.append("assumptions: each has an id and a text")
    value = lambda record: record.get("value") if isinstance(record, dict) else None
    for section, key in SINGLES:
        if not isinstance(a[section], dict) or not (number(value(a[section].get(key))) and value(a[section][key]) >= 0):
            bad.append(f"{section}.{key}: a record with a value that is not negative")
    if not (number(value(a["fuel_energy_mj_per_kg"])) and value(a["fuel_energy_mj_per_kg"]) > 0):
        bad.append("fuel_energy_mj_per_kg: a record with a positive value")
    if not (number(value(a["empty_growth_share"])) and 0 <= value(a["empty_growth_share"]) <= 1):
        bad.append("empty_growth_share: a record with a value from 0 to 1")
    if bad:
        return bad
    if not (isinstance(a["payload"].get("passengers"), int) and a["payload"]["passengers"] > 0 and value(a["payload"]["kg_per_passenger"]) > 0):
        bad.append("payload: passengers is a whole number above zero, and the mass of each is positive")
    if not (value(a["reserves"]["contingency_share"]) < 1 and min(value(a["units"][k]) for k in ("motor_kw", "turbogenerator_kw")) > 0):
        bad.append("the contingency is a share, and unit ratings are positive")

    ref = a["reference"]
    sectors, check = ref.get("sectors"), ref.get("range_check")
    masses = [value(ref[k]) for k in ("basic_operating_kg", "sizing_takeoff_kg", "takeoff_limit_kg")]
    if not (rp.has_text(ref.get("aircraft")) and rp.has_text(ref.get("sectors_ref")) and 0 < masses[0] < masses[1] <= masses[2] and value(ref["fuel_lb_per_usg"]) > 0):
        bad.append("reference: an aircraft, a source for its sectors, and masses in the order empty, sizing take-off, take-off limit")
    elif not (rp.is_list_of(sectors, dict) and len(sectors) >= 3 and all(
            rp.has_text(s.get("name")) and all(number(s.get(k)) and s[k] > 0 for k in ("esad_nm", "block_fuel_usg", "takeoff_lb"))
            and s["block_fuel_usg"] * value(ref["fuel_lb_per_usg"]) < s["takeoff_lb"] for s in sectors)):
        bad.append("reference.sectors: at least three, each with a name, a distance, a block fuel below the take-off mass, and a take-off mass")
    elif len({s["esad_nm"] for s in sectors}) < 2 or fit(a)["terminal_km"] <= 0 or fit(a)["per_km"] <= 0:
        bad.append("reference.sectors: the published sectors must give a positive cost of cruise and a positive terminal distance")
    if not (isinstance(check, dict) and rp.has_text(check.get("ref")) and rp.has_text(check.get("reserve_ref"))
            and all(number(check.get(k)) and check[k] > 0 for k in ("range_nm", "passengers", "kg_per_passenger"))
            and all(number(check.get(k)) and check[k] >= 0 for k in ("alternate_nm", "flight_min"))
            and (check.get("tolerance_share") is None or (number(check["tolerance_share"]) and 0 < check["tolerance_share"] < 1))):
        bad.append("reference.range_check: a range, passengers and their mass, the alternate and the minutes of its reserve, their sources, and a tolerance or null")

    p = a["parameters"]
    if not isinstance(p, dict) or [k for k in PARAMETERS if not isinstance(p.get(k), dict)]:
        bad.append("parameters: one record for each of " + ", ".join(PARAMETERS))
    else:
        for key in PARAMETERS:
            values = [p[key].get(s) for s in SETS]
            if not all(number(v) and v > 0 for v in values) or (key in SHARES and max(values) >= 1):
                bad.append(f"{key}: favourable, nominal and unfavourable are positive" + (", and below 1" if key in SHARES else ""))
            elif not (sorted(values) == values or sorted(values, reverse=True) == values):
                bad.append(f"{key}: the nominal value lies between the favourable and the unfavourable one")

    keys = [m.get("key") for m in a["missions"]] if rp.is_list_of(a["missions"], dict) else None
    if not keys or not all(rp.has_text(m.get("key")) and rp.has_text(m.get("name")) and number(m.get("range_km")) and m["range_km"] > 0
                           and m.get("role") in ROLES for m in a["missions"]):
        bad.append("missions: each has a key, a name, a positive range_km, and a role among " + ", ".join(ROLES))
    elif len(set(keys)) != len(keys) or [m["role"] for m in a["missions"]].count("requirement") != 1:
        bad.append("missions: keys are used once, and one mission is the requirement")
    if not (rp.is_list_of(a["pack_levels"], dict) and a["pack_levels"]
            and all(number(x.get("wh_per_kg")) and x["wh_per_kg"] > 0 and rp.has_text(x.get("label")) for x in a["pack_levels"])):
        bad.append("pack_levels: each has a positive wh_per_kg and a label")
    if not (isinstance(a["hybrid_shares"], list) and a["hybrid_shares"] and all(number(h) and 0 < h < 1 for h in a["hybrid_shares"])):
        bad.append("hybrid_shares: a list of shares above 0 and below 1")
    if not bad:
        for label, x in figures(a):
            if x.get("basis") not in BASES:
                bad.append(f"{label}: basis is one of " + ", ".join(BASES))
            elif x["basis"] != "assumption" and not rp.has_text(x.get("ref")):
                bad.append(f"{label}: a figure with a {x['basis']} names it in ref")
        if {"A", "B", "C"} - set(option_states(knot)):
            bad.append(f"{a['knot']}: options A, B and C must be in the record; {', '.join(sorted({'A', 'B', 'C'} - set(option_states(knot))))} is not")
    return bad


def option_states(knot):
    """State of each option of the KNOT, with the ruling that excluded it where one did."""
    return {o["id"]: o["state"] + (f" by {o['by']}" if o.get("by") else "") for o in knot.get("options") or []
            if isinstance(o, dict) and rp.has_text(o.get("id")) and rp.has_text(o.get("state"))}


def reserve_km(a):
    r = a["reserves"]
    return r["alternate_km"]["value"] + r["holding_speed_kmh"]["value"] * r["final_reserve_min"]["value"] / 60


def fit(a):
    """The range equation fitted to the published sectors of the reference: -ln(1 - fuel / take-off) = per_km x (distance + terminal).

    per_km is the share of the take-off mass that a kilometre of cruise costs, and terminal the distance in cruise that
    costs what taxi, take-off, climb, descent and approach cost. A least-squares line through the sectors gives both.
    """
    ref = a["reference"]
    density = ref["fuel_lb_per_usg"]["value"]
    rows = [{"name": s["name"], "km": s["esad_nm"] * NM, "takeoff_kg": s["takeoff_lb"] * LB, "fuel_kg": s["block_fuel_usg"] * density * LB} for s in ref["sectors"]]
    xs, ys = [r["km"] for r in rows], [-math.log(1 - r["fuel_kg"] / r["takeoff_kg"]) for r in rows]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    per_km = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    terminal = (my - per_km * mx) / per_km if per_km else 0.0
    for r in rows:
        r["fitted_kg"] = r["takeoff_kg"] * (1 - math.exp(-per_km * (r["km"] + terminal)))
    out = {"per_km": per_km, "terminal_km": terminal, "rows": rows,
           "product": 1000 * G / (per_km * a["fuel_energy_mj_per_kg"]["value"] * 1e6) if per_km > 0 else 0.0}
    check = ref.get("range_check")
    if isinstance(check, dict) and all(number(check.get(k)) for k in ("range_nm", "passengers", "kg_per_passenger", "alternate_nm", "flight_min")) and per_km > 0:
        takeoff = ref["sizing_takeoff_kg"]["value"]                # flown with the reserve of the reference, not with that of the aircraft under test
        km = (check["range_nm"] + check["alternate_nm"]) * NM + terminal + a["reserves"]["holding_speed_kmh"]["value"] * check["flight_min"] / 60
        out["check"] = {"km": check["range_nm"] * NM, "asked_kg": takeoff * (1 - math.exp(-per_km * km)),
                        "loadable_kg": takeoff - ref["basic_operating_kg"]["value"] - check["passengers"] * check["kg_per_passenger"]}
    return out


class Model:
    """The range equation of one analysis at one set of parameters. Distances in km, masses in kg, pack energy in Wh/kg."""

    def __init__(self, a, which, fitted=None):
        fitted = fitted or fit(a)
        self.p = {k: a["parameters"][k][which] for k in PARAMETERS}
        ref = a["reference"]
        self.payload = a["payload"]["passengers"] * a["payload"]["kg_per_passenger"]["value"]
        self.limit, self.sizing = ref["takeoff_limit_kg"]["value"], ref["sizing_takeoff_kg"]["value"]
        self.empty, self.growth = ref["basic_operating_kg"]["value"] * self.p["empty_mass_share"], a["empty_growth_share"]["value"]
        self.contingency, self.reserve_km = a["reserves"]["contingency_share"]["value"], reserve_km(a)
        self.terminal_km = fitted["terminal_km"] * self.p["terminal_share"]
        chain = self.p["electric_chain_efficiency"] * self.p["propulsor_efficiency"] * self.p["lift_to_drag"]
        self.product_b = self.p["turbogenerator_efficiency"] * chain          # overall efficiency times lift-to-drag of option B
        self.per_km_fuel = 1000 * G / (self.product_b * a["fuel_energy_mj_per_kg"]["value"] * 1e6)
        self.per_km_battery = lambda wh_per_kg: 1000 * G / (wh_per_kg * 3600 * self.p["pack_usable_share"] * chain)

    def trip_km(self, mission):                                  # the trip with its contingency and its terminal phases
        return mission["range_km"] * (1 + self.contingency) + self.terminal_km

    def equivalent_km(self, mission):
        return self.trip_km(mission) + self.reserve_km

    def fuel_fraction(self, km):
        return 1 - math.exp(-km * self.per_km_fuel)

    def empty_at(self, takeoff):
        """Empty mass at a take-off mass: one share fixed, the other in proportion to the take-off mass."""
        return self.empty * (1 - self.growth + self.growth * takeoff / self.sizing)

    def mass(self, energy_fraction):
        """Take-off mass when energy takes the given share of it, or None when nothing is left for the payload."""
        left = 1 - energy_fraction - self.growth * self.empty / self.sizing
        return (self.empty * (1 - self.growth) + self.payload) / left if left > 0 else None

    def room(self):
        """Share of the take-off mass left for energy at the take-off mass limit."""
        return 1 - (self.empty_at(self.limit) + self.payload) / self.limit

    def option_a(self, mission, wh_per_kg):
        return self.mass(self.equivalent_km(mission) * self.per_km_battery(wh_per_kg))

    def option_b(self, mission):
        return self.mass(self.fuel_fraction(self.equivalent_km(mission)))

    def fuel_c(self, mission, share):
        return self.fuel_fraction((1 - share) * self.trip_km(mission) + self.reserve_km)

    def option_c(self, mission, share, wh_per_kg):
        return self.mass(share * self.trip_km(mission) * self.per_km_battery(wh_per_kg) + self.fuel_c(mission, share))

    def pack_needed_a(self, mission):
        """Pack specific energy at which option A meets the take-off mass limit; None when the limit leaves no room for energy."""
        return self.equivalent_km(mission) * self.per_km_battery(1) / self.room() if self.room() > 0 else None

    def pack_needed_c(self, mission, share):
        room = self.room() - self.fuel_c(mission, share)
        return share * self.trip_km(mission) * self.per_km_battery(1) / room if room > 0 else None

    def trip_within_limit_a(self, wh_per_kg):
        """Longest trip option A flies with its reserves at the take-off mass limit; zero when the reserves alone exceed it."""
        if self.room() <= 0:
            return 0.0
        return max(0.0, (self.room() / self.per_km_battery(wh_per_kg) - self.reserve_km - self.terminal_km) / (1 + self.contingency))

    def closes(self, mass):
        return mass is not None and mass <= self.limit


def render(a, knot):
    fitted = fit(a)
    models = {s: Model(a, s, fitted) for s in SETS}
    nominal, levels, ref, cell = models["nominal"], a["pack_levels"], a["reference"], (lambda text: str(text).replace("|", "/"))
    tonnes = lambda m, mass: f"{mass / 1000:.1f}" if m.closes(mass) else ("over" if mass else "none")
    three = lambda fn: " · ".join(fn(models[s]) for s in SETS)
    wh = lambda value: f"{value:.0f}" if value else "none"
    source = lambda x: cell(x.get("ref") or x.get("note") or "—")
    head = [f"{x['wh_per_kg']:g}" for x in levels]

    lines = [f"Scope: {cell(' '.join(a['scope'].split()))}", "", f"### Reference aircraft — {cell(ref['aircraft'])}", "",
             "| Sector | Distance km | Take-off t | Block fuel published kg | Block fuel fitted kg | Difference |", "|---|---:|---:|---:|---:|---:|"]
    lines += [f"| {cell(r['name'])} | {r['km']:.0f} | {r['takeoff_kg'] / 1000:.1f} | {r['fuel_kg']:.0f} | {r['fitted_kg']:.0f} | {r['fitted_kg'] / r['fuel_kg'] - 1:+.1%} |"
              for r in fitted["rows"]]
    check = fitted["check"]
    lines += ["", f"Source of the sectors: {cell(ref['sectors_ref'])}.", "",
              f"The fit has two results. Taxi, take-off, climb, descent and approach cost the fuel of {fitted['terminal_km']:.0f} km of cruise. "
              f"A thousand kilometres of cruise cost {fitted['per_km'] * 1000:.1%} of the take-off mass, which is an overall efficiency times lift-to-drag ratio of "
              f"{fitted['product']:.2f} at {a['fuel_energy_mj_per_kg']['value']:g} MJ/kg.", "",
              f"Check on a point outside the fit: for {check['km']:.0f} km with {ref['range_check']['passengers']:g} passengers and the reserve of the charts of the reference, "
              f"{ref['range_check']['alternate_nm']:g} nm of alternate and {ref['range_check']['flight_min']:g} minutes flown here at holding speed, the fit asks for "
              f"{check['asked_kg']:.0f} kg of fuel. At its take-off mass the aircraft can load {check['loadable_kg']:.0f} kg. The fit asks for {check['asked_kg'] / check['loadable_kg'] - 1:+.1%}. "
              + ("No tolerance is written for this point: it is a check of the test, not a requirement of the aircraft. " if ref["range_check"].get("tolerance_share") is None else
                 f"The tolerance written for this point is {ref['range_check']['tolerance_share']:.0%}. ")
              + f"Source of the point: {cell(ref['range_check']['ref'])}. Source of the reserve: {cell(ref['range_check']['reserve_ref'])}."]

    lines += ["", "### Missions", "", "| Key | Mission | Role | Trip km | Flown with terminal phases and reserves km | Basis | Source or note |", "|---|---|---|---:|---:|---|---|"]
    lines += [f"| {m['key']} | {cell(m['name'])} | {m['role']} | {m['range_km']:g} | {nominal.equivalent_km(m):.0f} | {m['basis']} | {source(m)}"
              + (f". {cell(m['note'])}" if m.get("ref") and m.get("note") else "") + " |" for m in a["missions"]]
    required = next(m for m in a["missions"] if m["role"] == "requirement")
    closing = [s for s in SETS if models[s].closes(models[s].option_b(required))]
    lines += ["", f"Options in `{a['knot']}`: " + " · ".join(f"{key} {state}" for key, state in sorted(option_states(knot).items())) + ".",
              f"On the requirement mission {required['key']}, option B closes at " + (" and ".join(closing) if closing else "no") + " values"
              + ("" if len(closing) == len(SETS) else ", and not at " + " and ".join(s for s in SETS if s not in closing) + " values")
              + f". Option A needs {three(lambda x: wh(x.pack_needed_a(required)))} Wh/kg at pack level, and option C {three(lambda x: wh(x.pack_needed_c(required, min(a['hybrid_shares']))))} Wh/kg "
              f"with the battery flying {min(a['hybrid_shares']):.0%} of the trip."]
    lines += ["", f"Payload: {a['payload']['passengers']} passengers at {a['payload']['kg_per_passenger']['value']:g} kg, {nominal.payload:.0f} kg. "
              f"At nominal values the terminal phases count for {nominal.terminal_km:.0f} km and the alternate with the final reserve for {nominal.reserve_km:.0f} km. "
              f"The empty mass is {nominal.empty:.0f} kg, and {a['empty_growth_share']['value']:.0%} of it grows with the take-off mass. "
              f"A mission closes when the take-off mass stays within {nominal.limit / 1000:g} t."]

    lines += ["", "### Option B — fuel for a turbogenerator, no propulsion battery", "",
              "| Mission | Take-off mass t, favourable · nominal · unfavourable | Fuel kg | Take-off power MW | Motors | Turbogenerators |", "|---|---:|---:|---:|---:|---:|"]
    for m in a["missions"]:
        mass = nominal.option_b(m)
        if nominal.closes(mass):
            power = mass * nominal.p["takeoff_kw_per_kg"]
            tail = (f"{mass * nominal.fuel_fraction(nominal.equivalent_km(m)):.0f} | {power / 1000:.1f} | {math.ceil(power / a['units']['motor_kw']['value'])} | "
                    f"{math.ceil(power / a['units']['turbogenerator_kw']['value'])}")
        else:
            tail = "— | — | — | —"
        lines.append(f"| {m['key']} | {three(lambda x: tonnes(x, x.option_b(m)))} | {tail} |")
    lines += ["", f"Fuel, with reserves, power and units are at nominal values. Units are counted at {a['units']['motor_kw']['value']:g} kW for a motor and "
              f"{a['units']['turbogenerator_kw']['value']:g} kW for a turbogenerator, with all the take-off power from the turbogenerators. "
              f"Against the cruise fitted to the reference, the cruise of option B costs {three(lambda x: format(fitted['product'] / x.product_b, '.2f'))} times as much fuel."]

    lines += ["", "### Option A — batteries alone", "", "| Mission | Pack needed Wh/kg, favourable · nominal · unfavourable | " + " | ".join(f"Mass t at {h}" for h in head) + " |",
              "|---|---:|" + "---:|" * len(head)]
    lines += [f"| {m['key']} | {three(lambda x: wh(x.pack_needed_a(m)))} | " + " | ".join(tonnes(nominal, nominal.option_a(m, x["wh_per_kg"])) for x in levels) + " |"
              for m in a["missions"]]
    lines += ["", "| Pack Wh/kg | Level | Longest trip km at the mass limit, favourable · nominal · unfavourable | Basis | Source or note |", "|---:|---|---:|---|---|"]
    lines += [f"| {x['wh_per_kg']:g} | {cell(x['label'])} | {three(lambda y: format(y.trip_within_limit_a(x['wh_per_kg']), '.0f'))} | {x['basis']} | {source(x)} |" for x in levels]

    lines += ["", "### Option C — both: the battery flies a share of the trip, fuel flies the rest and the reserves", "",
              "| Mission | Battery share | Pack needed Wh/kg, favourable · nominal · unfavourable | Mass t at " + " · ".join(head) + " | Fuel burned against option B at " + " · ".join(head) + " |",
              "|---|---:|---:|---:|---:|"]
    for m in a["missions"]:
        base = nominal.option_b(m)
        burned_b = base * nominal.fuel_fraction(nominal.equivalent_km(m)) if nominal.closes(base) else None
        for share in a["hybrid_shares"]:
            masses = [nominal.option_c(m, share, x["wh_per_kg"]) for x in levels]
            change = [f"{mass * nominal.fuel_c(m, share) / burned_b - 1:+.0%}" if burned_b and nominal.closes(mass) else "—" for mass in masses]
            lines.append(f"| {m['key']} | {share:.0%} | {three(lambda x: wh(x.pack_needed_c(m, share)))} | "
                         + " · ".join(tonnes(nominal, mass) for mass in masses) + " | " + " · ".join(change) + " |")
    lines += ["", "*over* means that the mission needs more than the take-off mass limit, and *none* that no take-off mass flies it. Masses are at nominal values. "
              "*Fuel burned against option B* compares kilograms of fuel on the same mission at nominal values: a plus sign means that the aircraft with a battery burns more."]

    first, middle = next(m for m in a["missions"] if m["role"] != "reference"), a["hybrid_shares"][len(a["hybrid_shares"]) // 2]
    lines += ["", "### Sensitivity to the growth of the empty mass", "",
              f"| Share that grows with take-off mass | Option B on {first['key']}, take-off t | Option A on {first['key']}, pack needed Wh/kg | "
              f"Option C on {first['key']} at {middle:.0%}, fuel burned against option B at " + " · ".join(head) + " |", "|---:|---:|---:|---:|"]
    for growth in sorted({0.0, 0.5, 1.0, a["empty_growth_share"]["value"]}):
        m = Model(dict(a, empty_growth_share=dict(a["empty_growth_share"], value=growth)), "nominal", fitted)
        base = m.option_b(first)
        burned_b = base * m.fuel_fraction(m.equivalent_km(first)) if m.closes(base) else None
        masses = [m.option_c(first, middle, x["wh_per_kg"]) for x in levels]
        change = [f"{mass * m.fuel_c(first, middle) / burned_b - 1:+.0%}" if burned_b and m.closes(mass) else "—" for mass in masses]
        lines.append(f"| {growth:.0%} | {tonnes(m, base)} | {wh(m.pack_needed_a(first))} | " + " · ".join(change) + " |")
    lines += ["", f"The test runs at {a['empty_growth_share']['value']:.0%}. At 100 % the empty mass is a fixed share of the take-off mass, and the aircraft shrinks with its mission."]

    lines += ["", "### Parameters", "", "| Parameter | Favourable | Nominal | Unfavourable | Basis | Note |", "|---|---:|---:|---:|---|---|"]
    lines += [f"| {k} | " + " | ".join(f"{a['parameters'][k][s]:g}" for s in SETS) + f" | {a['parameters'][k]['basis']} | {source(a['parameters'][k])} |" for k in PARAMETERS]
    lines += ["", "| Figure | Value | Basis | Source or note |", "|---|---:|---|---|"]
    lines += [f"| {label} | {x['value']:g} | {x['basis']} | {source(x)} |" for label, x in figures(a) if "value" in x]
    lines += ["", "### Assumptions", "", "| Id | Assumption |", "|---|---|"] + [f"| {x['id']} | {cell(x['text'])} |" for x in a["assumptions"]]
    return lines


def run(folder, register, mode=None):
    """Return (failures, output lines). mode is None, "check" or "write" for the generated section of the README."""
    folder = pathlib.Path(folder)
    doc, failure = rp.read_yaml(folder / "missions.yaml")
    bad, a = ([failure] if failure else []), None
    if not bad and not (isinstance(doc, dict) and isinstance(doc.get("analysis"), dict)):
        bad.append("missions.yaml: the top-level key is `analysis`")
    if not bad:
        a = doc["analysis"]
        found = sorted(pathlib.Path(register).rglob(f"{a.get('knot')}.yaml")) if rp.has_text(a.get("knot")) else []
        record, failure = rp.read_yaml(found[0]) if len(found) == 1 else (None, f"{a.get('knot')}: expected in one file of the register, found in {len(found)}")
        if failure or not (isinstance(record, dict) and isinstance(record.get("knot"), dict)):
            bad.append(failure or f"{found[0].name}: the top-level key is `knot`")
        else:
            knot = record["knot"]
            bad += validate(a, knot)
    head, body = "mission closure; rule failures: ", []
    if not bad:
        counted = figures(a)
        head = (f"{a['id']} {a['version']} for {a['knot']}: {sum(m['role'] != 'reference' for m in a['missions'])} missions, {len(a['pack_levels'])} pack levels, "
                f"{len(a['reference']['sectors'])} reference sectors; {len(counted)} figures, {sum(1 for _, x in counted if x['basis'] == 'assumption')} of them assumptions; rule failures: ")
        body = [rp.safe(line) for line in [""] + render(a, knot)]
        if mode:
            failure = rp.generated_section(folder / "README.md", "\n".join([rp.safe(head) + "none"] + body), mode == "write", BEGIN, END)
            bad += [failure] if failure else []
    bad = [rp.safe(b) for b in bad]
    return bad, [rp.safe(head) + (str(bad) if bad else "none")] + ([] if bad else body)


def main(argv):
    paths, flags = [x for x in argv[1:] if not x.startswith("--")], [x for x in argv[1:] if x.startswith("--")]
    if len(paths) != 2 or len(flags) > 1 or not set(flags) <= {"--check", "--write"}:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    bad, lines = run(*paths, mode=flags[0][2:] if flags else None)
    print("\n".join(lines))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
