# Generated 2026-11-15 - cruise_points.py (0.2.0)
"""Screening of candidate cruise points: speed, time, the missions of option B, cruise power, gas turbines, cabin and insulation.

    python3 tools/cruise_points.py <analysis folder> <KNOT register> [--check | --write]

Reads cruise-points.yaml in the analysis folder and the mission screening it names, which stays as it is. For each
point it gives the true airspeed in the standard atmosphere, the time at cruise speed on each mission, the mission
of option B flown with the propulsor efficiency of the point, the power in cruise against the take-off power, that
power referred to sea level by the air a gas turbine takes in, the pressure ratio to the cabin and the insulation
margin left at that pressure. The README of the folder holds the
output between two markers: --check fails when it differs, --write replaces it. Every figure printed follows from
the figures of the two inputs, and the output says how many are assumptions. The tool states no conformity with
any rule. It exits with status 1 on a failure and then prints only its first line.
"""
import copy
import math
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import mission_closure as mc  # noqa: E402
import relations_project as rp  # noqa: E402

BASES = ("assumption", "source", "decision")
SECTIONS = ("id", "version", "date", "knot", "serves", "missions", "option", "cabin_altitude_ft", "gas_turbine", "points", "insulation")
RULE = "corrected-flow"                                     # the one rule this tool knows for the air a gas turbine takes in
ROLES = ("sensitivity", "scoring", "requirement")          # the missions of the aircraft; a reference is not flown here
BEGIN, END = "<!-- cruise:begin -->", "<!-- cruise:end -->"
KEY = re.compile(r"P\d")
FT, KT, SHP = 0.3048, 1852 / 3600, 0.745699872             # metres in a foot, metres per second in a knot, kilowatts in a horsepower
GAMMA, R_AIR, CP = 1.4, 287.05287, 1004.7                  # air: ratio of specific heats, gas constant and specific heat, J/(kg K)


def atmosphere(feet):
    """Temperature in K, pressure in Pa and speed of sound in m/s of the standard atmosphere at a pressure altitude."""
    h = feet * FT
    t = 288.15 - 0.0065 * min(h, 11000.0)
    p = 101325.0 * (t / 288.15) ** 5.25588
    if h > 11000.0:
        p *= math.exp(-mc.G * (h - 11000.0) / (R_AIR * t))
    return t, p, math.sqrt(GAMMA * R_AIR * t)


def air_flow(t, pressure, mach):
    """Air through a gas turbine held at one point of its map, against sea level at rest: total pressure over the root of total temperature."""
    t0, p0, _ = atmosphere(0)
    ram = 1 + (GAMMA - 1) / 2 * mach ** 2
    return (pressure / p0) * ram ** (GAMMA / (GAMMA - 1)) / math.sqrt(t / t0 * ram)


def figure(x, low=None, high=None):
    """A figure is a number with its basis; one read at a source names it."""
    ok = (isinstance(x, dict) and mc.number(x.get("value")) and x.get("basis") in BASES and (x["basis"] != "source" or rp.has_text(x.get("ref"))))
    return ok and (low is None or x["value"] > low) and (high is None or x["value"] < high)


def figures(a):
    out = [a["cabin_altitude_ft"], a["gas_turbine"]] + [{"basis": a["insulation"]["basis"]} for _ in a["insulation"]["table"]]
    for p in a["points"]:
        out += [p["speed"], p["altitude_ft"], p["propulsor_efficiency"]] + ([p["published"]] if p.get("published") else [])
    return out


def validate(a, knot, missions):
    """Return the failures of a cruise-point analysis against its form, its KNOT and the mission screening it names."""
    bad = [f"missing section {s}" for s in SECTIONS if s not in a]
    if bad:
        return bad
    bad += [f"{f} is not text" for f in ("id", "version") if not rp.has_text(a[f])]
    bad += ["date is not a calendar date"] * (not rp.checked_date(a["date"]))
    bad += [f"{a['serves']} is not a KNU of {a['knot']}"] * (a["serves"] not in [u["knu_id"] for u in knot["knus"]])
    bad += [f"option {a['option']} is not an option of the mission screening"] * (a["option"] != "B")
    bad += ["cabin_altitude_ft is a figure between 0 and 15,000 ft"] * (not figure(a["cabin_altitude_ft"], -1, 15000))
    gas = a["gas_turbine"]
    bad += [f"gas_turbine: the rule is `{RULE}`, an assumption with a note"] * (not (isinstance(gas, dict) and gas.get("rule") == RULE and gas.get("basis") == "assumption" and rp.has_text(gas.get("note"))))
    options = {o["id"] for o in knot["options"]}
    points = a["points"]
    if not (isinstance(points, list) and points and all(isinstance(p, dict) and rp.has_text(p.get("key")) and KEY.fullmatch(p["key"]) and rp.has_text(p.get("name")) for p in points)):
        return bad + ["points: each point has a key P1, P2 ... and a name"]
    keys = [p["key"] for p in points]
    bad += [f"point {k} repeated" for k in sorted(set(keys)) if keys.count(k) > 1]
    for p in points:
        where, speed = f"point {p['key']}", p.get("speed")
        bad += [f"{where}: option {p.get('option')} is not an option of {a['knot']}"] * (p.get("option") not in options)
        if not (figure(speed, 0) and speed.get("unit") in ("kt", "mach") and (speed["unit"] == "kt" or speed["value"] < 1)):
            bad.append(f"{where}: speed is a figure in kt of true airspeed or in mach below 1")
        bad += [f"{where}: altitude_ft is a figure between 0 and 45,000 ft"] * (not figure(p.get("altitude_ft"), -1, 45001))
        bad += [f"{where}: propulsor_efficiency is a figure above 0 and below 1"] * (not figure(p.get("propulsor_efficiency"), 0, 1))
        pub = p.get("published")
        if pub is not None and not (isinstance(pub, dict) and all(mc.number(pub.get(f)) and pub[f] > 0 for f in ("takeoff_kg", "cruise_shp", "takeoff_shp"))
                                    and pub.get("basis") == "source" and rp.has_text(pub.get("ref"))):
            bad.append(f"{where}: published gives takeoff_kg, cruise_shp and takeoff_shp read at a source")
    ins = a["insulation"]
    rows = ins.get("table") if isinstance(ins, dict) else None
    if not (isinstance(rows, list) and len(rows) >= 2 and all(isinstance(r, dict) and mc.number(r.get("mbar")) and mc.number(r.get("kv")) and r["mbar"] > 0 and r["kv"] > 0 for r in rows)
            and ins.get("basis") == "source" and rp.has_text(ins.get("ref"))):
        return bad + ["insulation: a table of at least two rows of mbar and kv, read at a source"]
    pressures = [r["mbar"] for r in rows]
    bad += ["insulation: the rows go from sea level down, by falling pressure"] * (pressures != sorted(pressures, reverse=True) or len(set(pressures)) != len(pressures) or pressures[0] < 1000)
    bad += ["the mission screening has no mission of the aircraft"] * (not [m for m in missions["missions"] if m["role"] in ROLES])
    return bad


def inception(rows, mbar):
    """Inception voltage at a pressure as a share of its value at sea level: the measured rows joined by straight lines in the logarithm of the pressure."""
    if mbar >= rows[0]["mbar"]:
        return 1.0
    for hi, lo in zip(rows, rows[1:]):
        if mbar >= lo["mbar"]:
            x = (math.log(mbar) - math.log(lo["mbar"])) / (math.log(hi["mbar"]) - math.log(lo["mbar"]))
            return (lo["kv"] + x * (hi["kv"] - lo["kv"])) / rows[0]["kv"]
    return None                                                                    # below the lowest pressure measured


def compute(a, missions):
    """One row of results for each point. Masses in kg, power in kW for each kg of take-off mass, speed in m/s."""
    base = mc.Model(missions, "nominal")
    flown = [m for m in missions["missions"] if m["role"] in ROLES]
    requirement = next((m for m in flown if m["role"] == "requirement"), flown[-1])
    _, cabin, _ = atmosphere(a["cabin_altitude_ft"]["value"])
    out = []
    for p in a["points"]:
        t, pressure, sound = atmosphere(p["altitude_ft"]["value"])
        v = p["speed"]["value"] * (KT if p["speed"]["unit"] == "kt" else sound)
        b = copy.deepcopy(missions)
        b["parameters"]["propulsor_efficiency"]["nominal"] = p["propulsor_efficiency"]["value"]
        model = mc.Model(b, "nominal")
        flights = {}
        for m in flown:
            mass = model.option_b(m)
            flights[m["key"]] = {"minutes": m["range_km"] * 1000 / v / 60, "mass": mass, "closes": model.closes(mass),
                                 "fuel": None if mass is None else mass * model.fuel_fraction(model.equivalent_km(m))}
        shaft = mc.G * v / (base.p["lift_to_drag"] * p["propulsor_efficiency"]["value"]) / 1000          # at the propulsor shaft
        row = {"point": p, "mach": v / sound, "tas": v, "pressure": pressure, "flights": flights, "requirement": requirement["key"],
               "cruise": shaft / base.p["electric_chain_efficiency"], "takeoff": base.p["takeoff_kw_per_kg"], "air": air_flow(t, pressure, v / sound),
               "ratio": max(cabin / pressure, 1.0), "work": CP * t * (max(cabin / pressure, 1.0) ** ((GAMMA - 1) / GAMMA) - 1) / 1000,
               "inception": inception(a["insulation"]["table"], pressure / 100)}
        pub = p.get("published")
        if pub:
            per_kg = pub["cruise_shp"] * SHP / pub["takeoff_kg"]
            row["published"] = {"per_kg": per_kg, "model": shaft, "product": mc.G * v / (1000 * per_kg), "share": pub["cruise_shp"] / pub["takeoff_shp"],
                                "cruise": per_kg / base.p["electric_chain_efficiency"], "sea_level_shp": pub["cruise_shp"] / row["air"]}
        out.append(row)
    return out


def render(a, missions, rows):
    def tonnes(x):
        return "none" if x["mass"] is None else f"{x['mass'] / 1000:.1f}" + ("" if x["closes"] else " over")

    par, keys = missions["parameters"], list(rows[0]["flights"])
    band = [par["takeoff_kw_per_kg"][s] for s in mc.SETS]
    lines = ["### Points", "", "| Point | Option | Mach | True airspeed | Altitude | Ambient pressure | Propulsor efficiency | Basis of speed · altitude · efficiency |", "|---|---|---|---|---|---|---|---|"]
    lines += [f"| `{r['point']['key']}` {r['point']['name']} | {r['point']['option']} | {r['mach']:.2f} | {r['tas'] / KT:.0f} kt · {r['tas'] * 3.6:.0f} km/h | "
              f"{r['point']['altitude_ft']['value']:,.0f} ft | {r['pressure'] / 100:.0f} hPa | {r['point']['propulsor_efficiency']['value']:.2f} | "
              f"{r['point']['speed']['basis']} · {r['point']['altitude_ft']['basis']} · {r['point']['propulsor_efficiency']['basis']} |" for r in rows]
    lines += ["", "### Time at cruise speed", "", "The stage length divided by the true airspeed, in minutes. It is not a block time: climb, descent and taxi are not in it.", "",
              "| Point | " + " | ".join(f"{m['key']}, {m['range_km']:,.0f} km" for m in missions["missions"] if m["key"] in keys) + " |", "|---|" + "---|" * len(keys)]
    lines += [f"| `{r['point']['key']}` | " + " | ".join(f"{r['flights'][k]['minutes']:.0f}" for k in keys) + " |" for r in rows]
    lines += ["", f"### Option {a['option']} at each point", "",
              "The mission screening at its nominal values, with the propulsor efficiency of the point in place of its own. Nothing else changes with the point, so the differences below are those of that one figure.", "",
              "| Point | Propulsor efficiency | " + " | ".join(f"Take-off mass on {k}, t | Fuel on {k}, kg" for k in keys) + " |", "|---|---|" + "---|---|" * len(keys)]
    lines += [f"| `{r['point']['key']}` | {r['point']['propulsor_efficiency']['value']:.2f} | "
              + " | ".join(f"{tonnes(r['flights'][k])} | " + ("—" if r["flights"][k]["fuel"] is None else f"{r['flights'][k]['fuel']:,.0f}") for k in keys) + " |" for r in rows]
    lines += ["", "### Power in cruise against take-off", "",
              f"Electrical power at the terminals of the generators for each kilogram of mass, at a lift-to-drag ratio of {par['lift_to_drag']['nominal']:g} and an electric chain of "
              f"{par['electric_chain_efficiency']['nominal']:.2f}. The take-off power of the screening is {band[1]:.2f} kW/kg, between {min(band):.2f} and {max(band):.2f}. "
              f"The megawatts are for the take-off mass of mission {rows[0]['requirement']}, so they are an upper bound for the cruise.", "",
              "| Point | Cruise, kW/kg | Cruise, MW | Take-off, MW | Cruise against take-off |", "|---|---|---|---|---|"]
    for r in rows:
        mass = r["flights"][r["requirement"]]["mass"]
        mw = ("—", "—") if mass is None else (f"{r['cruise'] * mass / 1000:.1f}", f"{r['takeoff'] * mass / 1000:.1f}")
        lines.append(f"| `{r['point']['key']}` | {r['cruise']:.3f} | {mw[0]} | {mw[1]} | {r['cruise'] / r['takeoff']:.0%} |")
    for r in rows:
        if "published" in r:
            q, p = r["published"], r["point"]
            lines += ["", f"**Check on a published point, `{p['key']}`.** {p['published']['ref']}: {q['per_kg']:.3f} kW of shaft power in cruise for each kilogram of take-off mass, "
                      f"{q['share']:.0%} of the take-off power of the same engines. At the same speed the model gives {q['model']:.3f} kW/kg at the shaft, {q['model'] / q['per_kg']:.0%} of the published figure: "
                      f"the published point implies a product of lift-to-drag and propulsor efficiency of {q['product']:.1f}, against {par['lift_to_drag']['nominal'] * p['propulsor_efficiency']['value']:.1f} in the model. "
                      f"With the published figure and the electric chain, the cruise of this point asks {q['cruise']:.3f} kW/kg, {q['cruise'] / r['takeoff']:.0%} of the nominal take-off power."]
    lines += ["", "### Gas turbines: the cruise power referred to sea level", "",
              "A gas turbine held at one point of its map takes in air in proportion to the total pressure at its inlet and to the inverse of the square root of the total temperature. "
              "The second column is that air flow at the cruise point against the flow at sea level and at rest, in the standard atmosphere, behind an inlet that loses nothing. "
              "The cruise power divided by it is the power at sea level of machines that give the same work for each kilogram of air at both conditions. "
              "That rule is an assumption of this screening, of first order. It is not the fall of power of a machine, and none is on record for a turbogenerator.", "",
              "| Point | Air flow against sea level at rest | Cruise, MW | Referred to sea level, MW | Against take-off power |", "|---|---|---|---|---|"]
    for r in rows:
        mass = r["flights"][r["requirement"]]["mass"]
        mw = ("—", "—") if mass is None else (f"{r['cruise'] * mass / 1000:.1f}", f"{r['cruise'] / r['air'] * mass / 1000:.1f}")
        lines.append(f"| `{r['point']['key']}` | {r['air']:.0%} | {mw[0]} | {mw[1]} | {r['cruise'] / r['air'] / r['takeoff']:.0%} |")
    for r in rows:
        if "published" in r:
            q, pub = r["published"], r["point"]["published"]
            lines += ["", f"**The same rule on the published point, `{r['point']['key']}`.** The sheet rates its engines at {pub['cruise_shp']:,.0f} shp at maximum cruise. "
                      f"If they give it at this point, where the air flow is {r['air']:.0%} of that at sea level, the rule above makes them machines of {q['sea_level_shp']:,.0f} shp at sea level and at rest, "
                      f"{q['sea_level_shp'] / pub['takeoff_shp']:.0%} of the take-off power the sheet gives. The sheet does not say at what altitude the rating is given, "
                      "nor how much of the difference is a take-off rating held below what the engines give at sea level."]
    lines += ["", "### Cabin and insulation", "",
              f"Pressure ratio from the ambient pressure to a cabin at {a['cabin_altitude_ft']['value']:,.0f} ft, the ideal work to compress a kilogram of outside air through it, "
              "and the inception voltage of partial discharge left at the ambient pressure, as a share of its value at sea level on the specimens measured.", "",
              "| Point | Pressure ratio | Ideal work, kJ/kg of air | Inception voltage against sea level |", "|---|---|---|---|"]
    lines += [f"| `{r['point']['key']}` | {r['ratio']:.2f} | {r['work']:.0f} | " + ("below the pressures measured" if r["inception"] is None else f"{r['inception']:.0%}") + " |" for r in rows]
    return lines


def run(folder, register, mode=None):
    """Return (failures, output lines). mode is None, "check" or "write" for the generated section of the README."""
    folder, register = pathlib.Path(folder), pathlib.Path(register)
    doc, failure = rp.read_yaml(folder / "cruise-points.yaml")
    bad, a, missions = ([failure] if failure else []), None, None
    if not bad and not (isinstance(doc, dict) and isinstance(doc.get("analysis"), dict)):
        bad.append("cruise-points.yaml: the top-level key is `analysis`")
    if not bad:
        a = doc["analysis"]
        found = sorted(register.rglob(f"{a.get('knot')}.yaml")) if rp.has_text(a.get("knot")) else []
        record, failure = rp.read_yaml(found[0]) if len(found) == 1 else (None, f"{a.get('knot')}: expected in one file of the register, found in {len(found)}")
        if failure or not (isinstance(record, dict) and isinstance(record.get("knot"), dict)):
            bad.append(failure or f"{found[0].name}: the top-level key is `knot`")
        elif not rp.has_text(a.get("missions")) or not (folder.parent / a["missions"] / "missions.yaml").is_file():
            bad.append("missions names the folder of a mission screening beside this one")
        else:
            source = folder.parent / a["missions"]
            failures, _ = mc.run(source, register)
            bad += [f"the mission screening {a['missions']} fails its own check"] * bool(failures)
            if not bad:
                missions = rp.read_yaml(source / "missions.yaml")[0]["analysis"]
                bad += validate(a, record["knot"], missions)
    head, body = "cruise points; rule failures: ", []
    if not bad:
        counted = figures(a)
        assumed = sum(1 for x in counted if x["basis"] == "assumption")
        flown = [m for m in missions["missions"] if m["role"] in ROLES]
        head = (f"{a['id']} {a['version']} for {a['knot']}: {len(a['points'])} points on {len(flown)} missions of {missions['id']} {missions['version']}; "
                f"{len(counted)} figures, {assumed} of them assumptions; rule failures: ")
        body = [rp.safe(line) for line in [""] + render(a, missions, compute(a, missions))]
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
