# Generated 2026-11-14 - mission_closure.py (0.1.0)
"""First-order closure of candidate missions: which energy carrier flies each mission within a take-off mass limit.

    python3 tools/mission_closure.py <analysis folder> <KNOT register> [--check | --write]

Reads missions.yaml in the analysis folder, checks its form and prints the screening. The README of the folder holds
the output between two markers: --check fails when it differs, --write replaces it. The test is a range equation
with mass fractions, at three sets of parameters: favourable, nominal and unfavourable. It sizes no aircraft and
states no conformity. It exits with status 1 on a failure and then prints only its first line.

Options are those of the energy-carrier KNOT: A batteries alone, B fuel for a turbogenerator, C both.
"""
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import relations_project as rp  # noqa: E402

G = 9.80665
SETS = ("favourable", "nominal", "unfavourable")
BASES = ("assumption", "source")
PARAMETERS = ("lift_to_drag", "propulsor_efficiency", "electric_chain_efficiency", "turbogenerator_efficiency",
              "pack_usable_share", "empty_fraction_A", "empty_fraction_B", "empty_fraction_C", "takeoff_kw_per_kg")
SHARES = PARAMETERS[1:8]                                # parameters that lie above 0 and below 1
SECTIONS = ("id", "version", "date", "knot", "serves", "scope", "assumptions", "missions", "payload", "reserves", "flight",
            "fuel_energy_mj_per_kg", "takeoff_mass_limit_kg", "parameters", "pack_levels", "hybrid_shares", "units")
SINGLES = (("payload", "kg_per_passenger"), ("reserves", "contingency_share"), ("reserves", "alternate_km"),
           ("reserves", "final_reserve_min"), ("reserves", "holding_speed_kmh"), ("flight", "cruise_altitude_m"),
           ("flight", "cruise_speed_kmh"), ("flight", "descent_recovery_share"), ("units", "motor_kw"), ("units", "turbogenerator_kw"))
BEGIN, END = "<!-- screening:begin -->", "<!-- screening:end -->"


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def figures(a):
    """Every record of the input that carries a figure, with a label."""
    return ([(f"{s}.{k}", a[s][k]) for s, k in SINGLES] + [(k, a[k]) for k in ("fuel_energy_mj_per_kg", "takeoff_mass_limit_kg")]
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
    for key in ("fuel_energy_mj_per_kg", "takeoff_mass_limit_kg"):
        if not (number(value(a[key])) and value(a[key]) > 0):
            bad.append(f"{key}: a record with a positive value")
    if not bad and not (isinstance(a["payload"].get("passengers"), int) and a["payload"]["passengers"] > 0 and value(a["payload"]["kg_per_passenger"]) > 0):
        bad.append("payload: passengers is a whole number above zero, and the mass of each is positive")
    if not bad and not (value(a["reserves"]["contingency_share"]) < 1 and value(a["flight"]["descent_recovery_share"]) <= 1
                        and min(value(a["units"][k]) for k in ("motor_kw", "turbogenerator_kw")) > 0):
        bad.append("contingency and descent recovery are shares, and unit ratings are positive")

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
                           and isinstance(m.get("candidate"), bool) for m in a["missions"]):
        bad.append("missions: each has a key, a name, a positive range_km, and candidate true or false")
    elif len(set(keys)) != len(keys) or not any(m["candidate"] for m in a["missions"]):
        bad.append("missions: keys are used once, and at least one mission is a candidate")
    if not (rp.is_list_of(a["pack_levels"], dict) and a["pack_levels"]
            and all(number(x.get("wh_per_kg")) and x["wh_per_kg"] > 0 and rp.has_text(x.get("label")) for x in a["pack_levels"])):
        bad.append("pack_levels: each has a positive wh_per_kg and a label")
    if not (isinstance(a["hybrid_shares"], list) and a["hybrid_shares"] and all(number(h) and 0 < h < 1 for h in a["hybrid_shares"])):
        bad.append("hybrid_shares: a list of shares above 0 and below 1")
    if not bad:
        for label, x in figures(a):
            if x.get("basis") not in BASES:
                bad.append(f"{label}: basis is one of " + ", ".join(BASES))
            elif x["basis"] == "source" and not rp.has_text(x.get("ref")):
                bad.append(f"{label}: a figure with a source names it in ref")
        standing = {o.get("id") for o in knot.get("options") or [] if isinstance(o, dict) and o.get("state") in rp.LIVE}
        if {"A", "B", "C"} - standing:
            bad.append(f"{a['knot']}: options A, B and C must stand; {', '.join(sorted({'A', 'B', 'C'} - standing))} does not")
    return bad


class Model:
    """The range equation of one analysis at one set of parameters. Distances in km, masses in kg, energy per mass in J/kg."""

    def __init__(self, a, which):
        self.p = {k: a["parameters"][k][which] for k in PARAMETERS}
        r, f = a["reserves"], a["flight"]
        self.payload = a["payload"]["passengers"] * a["payload"]["kg_per_passenger"]["value"]
        self.limit = a["takeoff_mass_limit_kg"]["value"]
        self.contingency = r["contingency_share"]["value"]
        self.reserve_km = r["alternate_km"]["value"] + r["holding_speed_kmh"]["value"] * r["final_reserve_min"]["value"] / 60
        speed = f["cruise_speed_kmh"]["value"] / 3.6
        self.climb_km = self.p["lift_to_drag"] * (f["cruise_altitude_m"]["value"] * (1 - f["descent_recovery_share"]["value"]) + speed ** 2 / (2 * G)) / 1000
        electric = self.p["electric_chain_efficiency"] * self.p["propulsor_efficiency"] * self.p["lift_to_drag"]
        self.per_km_fuel = 1000 * G / (self.p["turbogenerator_efficiency"] * electric * a["fuel_energy_mj_per_kg"]["value"] * 1e6)
        self.per_km_battery = lambda wh_per_kg: 1000 * G / (wh_per_kg * 3600 * self.p["pack_usable_share"] * electric)

    def trip_km(self, mission):                                  # the trip with its contingency, take-off and climb
        return mission["range_km"] * (1 + self.contingency) + self.climb_km

    def equivalent_km(self, mission):
        return self.trip_km(mission) + self.reserve_km

    def fuel_fraction(self, km):
        return 1 - math.exp(-km * self.per_km_fuel)

    def mass(self, fractions):
        """Take-off mass for the given mass fractions of empty aircraft and energy, or None when they leave no payload."""
        left = 1 - sum(fractions)
        return self.payload / left if left > 0 else None

    def option_a(self, mission, wh_per_kg):
        return self.mass((self.p["empty_fraction_A"], self.equivalent_km(mission) * self.per_km_battery(wh_per_kg)))

    def option_b(self, mission):
        return self.mass((self.p["empty_fraction_B"], self.fuel_fraction(self.equivalent_km(mission))))

    def fuel_c(self, mission, share):
        return self.fuel_fraction((1 - share) * self.trip_km(mission) + self.reserve_km)

    def option_c(self, mission, share, wh_per_kg):
        battery = share * self.trip_km(mission) * self.per_km_battery(wh_per_kg)
        return self.mass((self.p["empty_fraction_C"], battery, self.fuel_c(mission, share)))

    def pack_needed_a(self, mission):
        """Pack specific energy, Wh/kg, at which option A meets the take-off mass limit; None when no pack does."""
        room = 1 - self.p["empty_fraction_A"] - self.payload / self.limit
        return self.equivalent_km(mission) * self.per_km_battery(1) / room if room > 0 else None

    def pack_needed_c(self, mission, share):
        room = 1 - self.p["empty_fraction_C"] - self.fuel_c(mission, share) - self.payload / self.limit
        return share * self.trip_km(mission) * self.per_km_battery(1) / room if room > 0 else None

    def trip_within_limit_a(self, wh_per_kg):
        """Longest trip, km, option A flies with its reserves at the take-off mass limit; zero when the reserves alone exceed it."""
        room = 1 - self.p["empty_fraction_A"] - self.payload / self.limit
        return max(0.0, (room / self.per_km_battery(wh_per_kg) - self.reserve_km - self.climb_km) / (1 + self.contingency)) if room > 0 else 0.0

    def closes(self, mass):
        return mass is not None and mass <= self.limit


def render(a):
    models = {s: Model(a, s) for s in SETS}
    nominal, levels, cell = models["nominal"], a["pack_levels"], (lambda text: str(text).replace("|", "/"))
    tonnes = lambda m, mass: f"{mass / 1000:.1f}" if m.closes(mass) else ("over" if mass else "none")
    three = lambda fn: " · ".join(fn(models[s]) for s in SETS)
    wh = lambda value: f"{value:.0f}" if value else "none"
    ref = lambda x: cell(x.get("ref") or x.get("note") or "—")
    head = [f"{x['wh_per_kg']:g}" for x in levels]

    lines = [f"Scope: {cell(' '.join(a['scope'].split()))}", "", "### Missions", "",
             "| Key | Mission | Trip km | Flown with reserves km | Candidate | Basis | Source or note |", "|---|---|---:|---:|---|---|---|"]
    lines += [f"| {m['key']} | {cell(m['name'])} | {m['range_km']:g} | {nominal.equivalent_km(m):.0f} | {'yes' if m['candidate'] else 'no'} | {m['basis']} | {ref(m)} |"
              for m in a["missions"]]
    lines += ["", f"Payload: {a['payload']['passengers']} passengers at {a['payload']['kg_per_passenger']['value']:g} kg, {nominal.payload:.0f} kg. "
              f"Reserves at nominal values: {nominal.reserve_km:.0f} km for the alternate and the final reserve, and {nominal.climb_km:.0f} km for take-off and climb. "
              f"A mission closes when the take-off mass stays within {a['takeoff_mass_limit_kg']['value'] / 1000:g} t."]

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
    lines += ["", f"Fuel, power and units are at nominal values. Units are counted at {a['units']['motor_kw']['value']:g} kW for a motor and "
              f"{a['units']['turbogenerator_kw']['value']:g} kW for a turbogenerator, with all the take-off power from the turbogenerators."]

    lines += ["", "### Option A — batteries alone", "", "| Mission | Pack needed Wh/kg, favourable · nominal · unfavourable | " + " | ".join(f"Mass t at {h}" for h in head) + " |",
              "|---|---:|" + "---:|" * len(head)]
    lines += [f"| {m['key']} | {three(lambda x: wh(x.pack_needed_a(m)))} | " + " | ".join(tonnes(nominal, nominal.option_a(m, x["wh_per_kg"])) for x in levels) + " |"
              for m in a["missions"]]
    lines += ["", "| Pack Wh/kg | Level | Longest trip km at the mass limit, favourable · nominal · unfavourable | Basis | Source or note |", "|---:|---|---:|---|---|"]
    lines += [f"| {x['wh_per_kg']:g} | {cell(x['label'])} | {three(lambda y: format(y.trip_within_limit_a(x['wh_per_kg']), '.0f'))} | {x['basis']} | {ref(x)} |" for x in levels]

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

    lines += ["", "### Parameters", "", "| Parameter | Favourable | Nominal | Unfavourable | Basis | Note |", "|---|---:|---:|---:|---|---|"]
    lines += [f"| {k} | " + " | ".join(f"{a['parameters'][k][s]:g}" for s in SETS) + f" | {a['parameters'][k]['basis']} | {ref(a['parameters'][k])} |" for k in PARAMETERS]
    lines += ["", "| Figure | Value | Basis | Source or note |", "|---|---:|---|---|"]
    lines += [f"| {label} | {x['value']:g} | {x['basis']} | {ref(x)} |" for label, x in figures(a) if "value" in x]
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
            bad += validate(a, record["knot"])
    head, body = "mission closure; rule failures: ", []
    if not bad:
        counted = figures(a)
        head = (f"{a['id']} {a['version']} for {a['knot']}: {sum(m['candidate'] for m in a['missions'])} candidate missions, {len(a['pack_levels'])} pack levels; "
                f"{len(counted)} figures, {sum(1 for _, x in counted if x['basis'] == 'assumption')} of them assumptions; rule failures: ")
        body = [rp.safe(line) for line in [""] + render(a)]
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
