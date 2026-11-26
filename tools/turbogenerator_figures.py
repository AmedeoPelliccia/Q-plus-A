# Generated 2026-11-26 - turbogenerator_figures.py (0.1.0)
"""Figures of gas turbines and generators read at public sources, set beside the rule of the cruise-point screening.

    python3 tools/turbogenerator_figures.py <analysis folder> <KNOT register> [--check | --write]

Reads turbogenerator-figures.yaml in the analysis folder. It holds figures that a research record accepted: two published
tables of power against altitude and speed, consumptions of engines and of engine models, part-load points, and masses.
The tool sets the tables beside the rule that the screening of the cruise points states for the air a gas turbine takes
in, which it takes from tools/cruise_points.py and does not restate. It turns consumptions into efficiencies at a declared
heating value, and it refers the cruise power of the working reference to sea level by each table. The README of the
folder holds the output between two markers: --check fails when it differs, --write replaces it. Every figure printed
follows from the figures of the input, and the output says how many are assumptions and who read the others. The tool
sizes nothing and states no conformity with any rule. It exits with status 1 on a failure and then prints only its first line.
"""
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cruise_points as cp  # noqa: E402
import mission_closure as mc  # noqa: E402
import relations_project as rp  # noqa: E402

READ = {"both": "two readers", "reviewer": "the reviewer", "reported": "as reported"}
CLASSES = ("A", "B", "C", "D")
TECHNOLOGY = ("current", "mid", "advanced")
SECTIONS = ("id", "version", "date", "knot", "serves", "record", "screening", "heating_value_mj_kg", "generator_efficiency", "reference",
            "power_tables", "second_document", "cycle_models", "flight", "ground_test", "consumptions", "size_models", "part_load", "masses", "study_masses")
BEGIN, END = "<!-- figures:begin -->", "<!-- figures:end -->"
LB = 0.45359237                                             # kilograms in a pound
P0, T0 = 101325.0, 288.15                                   # standard sea level, Pa and K


def figures(node):
    """Every mapping of the analysis that names a basis, at any depth."""
    out = []
    if isinstance(node, dict):
        out += [node] * ("basis" in node)
        for value in node.values():
            out += figures(value)
    elif isinstance(node, list):
        for value in node:
            out += figures(value)
    return out


def stated(x):
    """An assumption carries a note. A figure read at a source names it, says who read it, and has a proposed class or none."""
    if x.get("basis") == "assumption":
        return rp.has_text(x.get("note"))
    return x.get("basis") == "source" and rp.has_text(x.get("ref")) and x.get("read") in READ and x.get("class") in CLASSES + (None,)


def positive(*values):
    return all(mc.number(v) and v > 0 for v in values)


def air(altitude_ft, isa_k=0.0, kt=None, mach=None):
    """Mach number, and the air of the rule of the screening against sea level at rest, at an altitude, a temperature offset and a speed."""
    t, pressure, _ = cp.atmosphere(altitude_ft)
    t += isa_k
    if mach is None:
        mach = kt * cp.KT / math.sqrt(cp.GAMMA * cp.R_AIR * t)
    return mach, cp.air_flow(t, pressure, mach)


def dec(x):
    """A consumption with three decimals, or four where the source gives four."""
    text = f"{x:.4f}"
    return text[:-1] if text.endswith("0") else text


def lower(text):
    return text[:1].lower() + text[1:]


def kg_kwh(lb_hp_h):
    return lb_hp_h * LB / cp.SHP


def efficiency(kg_per_kwh, heating_value):
    """Shaft work over the heating value of the fuel, from kg/kWh and MJ/kg."""
    return 3.6 / (kg_per_kwh * heating_value)


def intercept(load_1, sfc_1, load_2, sfc_2):
    """Intercept a of a straight fuel-flow line, Wf/Wf_full = a + (1 - a) L, through two points of one engine at one flight condition."""
    r = sfc_1 / sfc_2
    return (r - 1.0) / ((1.0 / load_1 - 1.0) - r * (1.0 / load_2 - 1.0))


def on_line(a, load):
    """Consumption for each kWh at a load, over that at full load, on the line of intercept a."""
    return (a + (1.0 - a) * load) / load


def flight_mach(indicated_kt, altitude_ft):
    """Mach number from an indicated airspeed taken as calibrated, at a pressure altitude."""
    _, pressure, _ = cp.atmosphere(altitude_ft)
    impact = P0 * ((1 + 0.2 * (indicated_kt * cp.KT) ** 2 / (cp.GAMMA * cp.R_AIR * T0)) ** 3.5 - 1)
    return math.sqrt(5 * ((impact / pressure + 1) ** (2 / 7) - 1))


def validate(a, knot, folder):
    """Return the failures of the analysis against its form, its KNOT, its record and the screening it names."""
    bad = [f"missing section {s}" for s in SECTIONS if s not in a]
    if bad:
        return bad
    bad += [f"{f} is not text" for f in ("id", "version", "record", "screening") if not rp.has_text(a[f])]
    bad += ["date is not a calendar date"] * (not rp.checked_date(a["date"]))
    knus = [u["knu_id"] for u in knot["knus"]]
    serves = a["serves"] if rp.is_list_of(a["serves"], str) and a["serves"] else []
    bad += ["serves lists at least one KNU"] * (not serves)
    bad += [f"{s} is not a KNU of {a['knot']}" for s in serves if s not in knus]
    if bad:
        return bad
    bad += [f"the research record {a['record']} is not beside this folder"] * (not (folder.parent / a["record"]).is_file())
    screening, failure = rp.read_yaml(folder.parent / a["screening"] / "cruise-points.yaml")
    rule = None if failure or not isinstance(screening, dict) else (screening.get("analysis") or {}).get("gas_turbine", {}).get("rule")
    bad += [f"the screening {a['screening']} does not state the rule `{cp.RULE}`, which this analysis compares"] * (rule != cp.RULE)
    bad += [f"a figure gives a basis, with a note for an assumption, and a source, a reader and a class for a figure read: {x.get('name') or x.get('key') or x.get('ref') or x.get('note')}"
            for x in figures(a) if not stated(x)]
    if bad:
        return bad
    lhv, gen, ref = a["heating_value_mj_kg"], a["generator_efficiency"], a["reference"]
    bad += ["heating_value_mj_kg gives low, value and high in rising order"] * (not (positive(lhv.get("low"), lhv.get("value"), lhv.get("high")) and lhv["low"] <= lhv["value"] <= lhv["high"]))
    bad += ["generator_efficiency is above 0 and not above 1"] * (not (positive(gen.get("value")) and gen["value"] <= 1))
    shaped = isinstance(ref, dict) and all(isinstance(ref.get(k), dict) for k in ("altitude_ft", "speed_kt", "cruise_mw", "takeoff_mw")) and isinstance(ref.get("budget"), list)
    if not (shaped and positive(ref["altitude_ft"].get("value"), ref["speed_kt"].get("value"), ref["cruise_mw"].get("value"), ref["takeoff_mw"].get("low"), ref["takeoff_mw"].get("high"))
            and rp.is_list_of(ref.get("candidates_ft"), int) and rp.is_list_of(ref.get("candidates_mach"), float) and ref["candidates_ft"] and ref["candidates_mach"]
            and all(0 < h <= 36000 for h in ref["candidates_ft"] + [ref["altitude_ft"]["value"]]) and all(0 < m < 1 for m in ref["candidates_mach"])
            and ref["budget"] and all(isinstance(b, dict) and rp.has_text(b.get("key")) and positive(b.get("value")) and b["value"] < 1 for b in ref["budget"])):
        bad.append("reference: an altitude up to 36,000 ft, a speed, a cruise power and a take-off band, candidate altitudes and Mach numbers, and the values of the budget below 1")
    tables = a["power_tables"]
    if not (isinstance(tables, list) and tables and all(isinstance(t, dict) and rp.has_text(t.get("key")) and rp.has_text(t.get("name")) and rp.has_text(t.get("rating")) for t in tables)):
        return bad + ["power_tables: each table has a key, a name and a rating"]
    keys = [t["key"] for t in tables]
    bad += [f"power table {k} repeated" for k in sorted(set(keys)) if keys.count(k) > 1]
    for t in tables:
        where, speeds, rows = f"power table {t['key']}", t.get("speeds_kt"), t.get("conditions")
        if not (positive(t.get("rated_shp")) and isinstance(speeds, list) and len(speeds) >= 2 and all(mc.number(v) for v in speeds) and speeds[0] == 0 and speeds == sorted(set(speeds))):
            bad.append(f"{where}: a rated power, and speeds that rise from 0")
            continue
        if not (isinstance(rows, list) and len(rows) >= 2 and all(
                isinstance(r, dict) and rp.has_text(r.get("key")) and mc.number(r.get("altitude_ft")) and 0 <= r["altitude_ft"] <= 36000 and mc.number(r.get("isa_k"))
                and isinstance(r.get("shp"), list) and len(r["shp"]) == len(speeds) and positive(*r["shp"]) for r in rows)):
            bad.append(f"{where}: each condition has a key, an altitude up to 36,000 ft, a temperature offset and one power for each speed")
            continue
        bad += [f"{where}: the first condition is sea level on a standard day"] * (rows[0]["altitude_ft"] != 0 or rows[0]["isa_k"] != 0)
        standard = [r["altitude_ft"] for r in rows if r["isa_k"] == 0]
        bad += [f"{where}: the conditions on a standard day rise in altitude"] * (standard != sorted(set(standard)))
    second = a["second_document"]
    table = next((t for t in tables if t["key"] == second.get("table")), None)
    if table is None or not positive(second.get("altitude_ft"), second.get("speed_kt"), second.get("available_hp"), second.get("engines"), second.get("rated_hp")):
        bad.append("second_document: it names a power table and gives an altitude, a speed, a power available, a number of engines and a rated power")
    elif not bad and bracket(table, second["altitude_ft"], second["speed_kt"]) is None:
        bad.append("second_document: its point lies inside the standard-day conditions and the speeds of the table it names")
    models = a["cycle_models"]
    if not (isinstance(models, list) and models and all(isinstance(m, dict) and rp.has_text(m.get("key")) and rp.has_text(m.get("name")) and isinstance(m.get("points"), list) and len(m["points"]) >= 2 for m in models)):
        return bad + ["cycle_models: each model has a key, a name and at least two points"]
    for m in models:
        pts = m["points"]
        if not all(isinstance(p, dict) and rp.has_text(p.get("name")) and mc.number(p.get("altitude_ft")) and mc.number(p.get("mach")) and positive(p.get("shp"), p.get("sfc_lb_hp_h"), p.get("air_lbm_s")) for p in pts):
            bad.append(f"cycle model {m['key']}: each point has a name, an altitude, a Mach number, a power, a consumption and an air flow")
        else:
            first, rest = pts[0], pts[1:]
            loads = [p.get("load") for p in rest]
            down = all(mc.number(x) for x in loads) and loads[0] == 1.0 and loads == sorted(set(loads), reverse=True) and loads[-1] > 0
            one = len({(p["altitude_ft"], p["mach"]) for p in rest}) == 1
            if first["altitude_ft"] != 0 or first["mach"] != 0 or first.get("load") is not None or not down or not one:
                bad.append(f"cycle model {m['key']}: the first point is sea level at rest, and the others go down from full throttle at one flight condition")
    flight = a["flight"]
    if not (positive(flight.get("altitude_ft"), flight.get("indicated_kt"), flight.get("rated_kw")) and mc.number(flight.get("static_temperature_c")) and isinstance(flight.get("engines"), list) and flight["engines"]
            and all(isinstance(e, dict) and rp.has_text(e.get("name")) and positive(e.get("shaft_kw"), e.get("fuel_kg_h")) for e in flight["engines"])):
        bad.append("flight: an altitude, a static temperature, an indicated airspeed, a rated power, and a shaft power and a fuel flow for each engine")
    test = a["ground_test"]
    modes = test.get("modes")
    if not (positive(test.get("heating_value_mj_kg"), test.get("ambient_kpa"), test.get("ambient_k")) and isinstance(modes, list) and len(modes) >= 2
            and all(isinstance(m, dict) and rp.has_text(m.get("name")) and positive(m.get("shaft_kw"), m.get("fuel_kg_s")) for m in modes)):
        bad.append("ground_test: a heating value, the ambient pressure and temperature, and a shaft power and a fuel flow for each mode")
    elif [m["shaft_kw"] for m in modes] != sorted(m["shaft_kw"] for m in modes):
        bad.append("ground_test: the modes rise in power, and the last is the reference")
    rows = a["consumptions"]
    bad += ["consumptions: each has a name and a consumption between 0.1 and 1 lb/(hp h)"] * (not (
        isinstance(rows, list) and rows and all(isinstance(r, dict) and rp.has_text(r.get("name")) and mc.number(r.get("sfc_lb_hp_h")) and 0.1 < r["sfc_lb_hp_h"] < 1 for r in rows)))
    sizes = a["size_models"]
    bad += ["size_models: each row has a name, a technology, a power, a consumption, a weight or none, and a class"] * (not (
        isinstance(sizes, list) and sizes and all(isinstance(s, dict) and isinstance(s.get("rows"), list) and s["rows"] and all(
            isinstance(r, dict) and rp.has_text(r.get("name")) and r.get("technology") in TECHNOLOGY and positive(r.get("hp"), r.get("sfc_lb_hp_h"))
            and (r.get("weight_lb") is None or positive(r["weight_lb"])) and r.get("class") in CLASSES for r in s["rows"]) for s in sizes)))
    points = a["part_load"].get("points")
    bad += ["part_load: two points or more, each with the power used, a larger power available and a consumption"] * (not (
        isinstance(points, list) and len(points) >= 2 and all(isinstance(p, dict) and rp.has_text(p.get("name")) and positive(p.get("used_hp"), p.get("available_hp"), p.get("sfc_lb_hp_h"))
                                                             and p["used_hp"] < p["available_hp"] for p in points)))
    masses = a["masses"]
    bad += ["masses: each has a name, a power, and a mass in lb or in kg, not both"] * (not (
        isinstance(masses, list) and masses and all(isinstance(m, dict) and rp.has_text(m.get("name")) and positive(m.get("kw")) and (positive(m.get("lb")) != positive(m.get("kg"))) for m in masses)))
    study = a["study_masses"]
    fields = ("generator_hp", "electric_lbm", "engine_lbm", "total_lbm", "baseline_lbm", "same_year_lbm")
    if not positive(*(study.get(f) for f in fields)):
        bad.append("study_masses: " + ", ".join(fields))
    elif study["electric_lbm"] + study["engine_lbm"] != study["total_lbm"]:
        bad.append("study_masses: the electric system and the engine add up to the total")
    return bad


def bracket(table, altitude_ft, speed_kt):
    """The two standard-day conditions and the two speeds of a table that enclose a point, or None."""
    standard = [r for r in table["conditions"] if r["isa_k"] == 0]
    rows = next(((lo, hi) for lo, hi in zip(standard, standard[1:]) if lo["altitude_ft"] <= altitude_ft <= hi["altitude_ft"]), None)
    speeds = table["speeds_kt"]
    cols = next(((i, i + 1) for i in range(len(speeds) - 1) if speeds[i] <= speed_kt <= speeds[i + 1]), None)
    return None if rows is None or cols is None else (rows, cols)


def interpolate(table, altitude_ft, speed_kt):
    """Power of a table at a point between its values: straight lines in speed, then in altitude."""
    (lo, hi), (i, j) = bracket(table, altitude_ft, speed_kt)
    x = (speed_kt - table["speeds_kt"][i]) / (table["speeds_kt"][j] - table["speeds_kt"][i])
    y = (altitude_ft - lo["altitude_ft"]) / (hi["altitude_ft"] - lo["altitude_ft"])
    low, high = (r["shp"][i] + x * (r["shp"][j] - r["shp"][i]) for r in (lo, hi))
    return low + y * (high - low)


def nearest(table, ref):
    """The standard-day condition and the speed of a table nearest to the working reference."""
    standard = [r for r in table["conditions"] if r["isa_k"] == 0]
    row = min(standard, key=lambda r: abs(r["altitude_ft"] - ref["altitude_ft"]["value"]))
    i = min(range(len(table["speeds_kt"])), key=lambda k: abs(table["speeds_kt"][k] - ref["speed_kt"]["value"]))
    return row, i


def compute(a):
    """The derived figures, as one mapping. Powers in shp or MW, consumptions in kg/kWh, efficiencies as shares."""
    ref, lhv, gen = a["reference"], a["heating_value_mj_kg"], a["generator_efficiency"]["value"]
    out = {"candidates": [], "tables": [], "efficiencies": [], "sizes": [], "loads": [], "lines": [], "masses": []}
    for h in ref["candidates_ft"]:
        for m in ref["candidates_mach"]:
            out["candidates"].append((h, *air(h, mach=m), cp.atmosphere(h)[2] * m / cp.KT))
    mach, rule = air(ref["altitude_ft"]["value"], kt=ref["speed_kt"]["value"])
    out["reference"] = {"mach": mach, "rule": rule, "sea_level_mw": ref["cruise_mw"]["value"] / rule}
    for t in a["power_tables"]:
        at_rest = t["conditions"][0]["shp"][0]
        grid = []
        for r in t["conditions"]:
            cells = []
            for v, shp in zip(t["speeds_kt"], r["shp"]):
                _, share = air(r["altitude_ft"], r["isa_k"], kt=v)
                cells.append({"shp": shp, "rule": share, "rated": shp / t["rated_shp"] / share, "continuous": shp / at_rest / share})
            grid.append(cells)
        row, i = nearest(t, ref)
        shp = row["shp"][i]
        _, share = air(row["altitude_ft"], kt=t["speeds_kt"][i])
        mw = ref["cruise_mw"]["value"]
        near = {"altitude_ft": row["altitude_ft"], "kt": t["speeds_kt"][i], "mw": shp * cp.SHP / 1000, "rule": share,
                "rated_mw": mw / shp * t["rated_shp"], "continuous_mw": mw / shp * at_rest, "by_rule_mw": mw / share}
        near["carried_mw"] = near["rated_mw"] * share / rule
        worth = [(r["key"], r["shp"][-1] / r["shp"][0], air(r["altitude_ft"], r["isa_k"], kt=t["speeds_kt"][-1])[1] / air(r["altitude_ft"], r["isa_k"], kt=0)[1]) for r in t["conditions"]]
        high = [c for r, cells in zip(t["conditions"], grid) if r["isa_k"] == 0 and r["altitude_ft"] >= 25000 for c in cells]
        out["tables"].append({"table": t, "grid": grid, "near": near, "worth": worth, "at_rest": at_rest,
                              "rated_range": (min(c["rated"] for c in high), max(c["rated"] for c in high)),
                              "continuous_range": (min(c["continuous"] for c in high), max(c["continuous"] for c in high))})
    second = a["second_document"]
    table = next(t for t in a["power_tables"] if t["key"] == second["table"])
    scaled = second["available_hp"] / second["engines"] * table["rated_shp"] / second["rated_hp"]
    tabled = interpolate(table, second["altitude_ft"], second["speed_kt"])
    out["second"] = {"scaled": scaled, "tabled": tabled, "difference": scaled / tabled - 1, "mach": air(second["altitude_ft"], kt=second["speed_kt"])[0],
                     "share_rated": second["available_hp"] / second["engines"] / second["rated_hp"]}

    def row(name, published, per_kwh, x):
        eta = efficiency(per_kwh, lhv["value"])
        return {"name": name, "published": published, "kg_kwh": per_kwh, "eta": eta, "low": efficiency(per_kwh, lhv["high"]), "high": efficiency(per_kwh, lhv["low"]),
                "terminals": eta * gen, "read": x["read"], "class": x.get("class")}

    for m in a["cycle_models"]:
        full = m["points"][1]
        for p in m["points"]:
            out["efficiencies"].append(row(f"{m['name']}: {lower(p['name'])}, {p['shp'] * cp.SHP:,.0f} kW", f"{dec(p['sfc_lb_hp_h'])} lb/(hp h)", kg_kwh(p["sfc_lb_hp_h"]), m))
        for p in m["points"][2:]:
            out["loads"].append((m["name"], p["name"], p["shp"] / full["shp"], p["sfc_lb_hp_h"] / full["sfc_lb_hp_h"]))
        last = m["points"][-1]
        out["lines"].append((m["name"], "full throttle and its lowest point, at 20,000 ft", intercept(last["shp"] / full["shp"], last["sfc_lb_hp_h"], 1.0, full["sfc_lb_hp_h"]), last["shp"] / full["shp"]))
        rest = m["points"][0]
        _, share = air(full["altitude_ft"], mach=full["mach"])
        m_air, m_power = full["air_lbm_s"] / rest["air_lbm_s"], full["shp"] / rest["shp"]
        out.setdefault("cycle", []).append({"name": m["name"], "power": m_power, "air": m_air, "work": m_power / m_air, "rule": share})
    flight = a["flight"]
    out["flight_mach"] = flight_mach(flight["indicated_kt"], flight["altitude_ft"])
    for e in flight["engines"]:
        out["efficiencies"].append(row(f"{flight['name']}: {lower(e['name'])}, {e['shaft_kw']:,.1f} kW, {e['shaft_kw'] / flight['rated_kw']:.0%} of its take-off rating",
                                       f"{e['fuel_kg_h']} kg/h", e["fuel_kg_h"] / e["shaft_kw"], flight))
    test = a["ground_test"]
    top = test["modes"][-1]
    for m in test["modes"]:
        per_kwh = m["fuel_kg_s"] * 3600 / m["shaft_kw"]
        out["efficiencies"].append(row(f"{test['name']}: {lower(m['name'])}, {m['shaft_kw']:,.1f} kW", f"{m['fuel_kg_s']} kg/s", per_kwh, test))
        if m is not top:
            out["loads"].append((test["name"], m["name"], m["shaft_kw"] / top["shaft_kw"], (m["fuel_kg_s"] / m["shaft_kw"]) / (top["fuel_kg_s"] / top["shaft_kw"])))
    low = test["modes"][0]
    out["lines"].append((test["name"], "take-off and its lowest mode, on the ground", intercept(low["shaft_kw"] / top["shaft_kw"], low["fuel_kg_s"] / low["shaft_kw"], 1.0, top["fuel_kg_s"] / top["shaft_kw"]),
                         low["shaft_kw"] / top["shaft_kw"]))
    out["test_own"] = [m["shaft_kw"] / (m["fuel_kg_s"] * test["heating_value_mj_kg"] * 1000) for m in test["modes"]]
    for c in a["consumptions"]:
        out["efficiencies"].append(row(c["name"], f"{dec(c['sfc_lb_hp_h'])} lb/(hp h)", kg_kwh(c["sfc_lb_hp_h"]), c))
    part = a["part_load"]["points"]
    loads = [p["used_hp"] / p["available_hp"] for p in part]
    order = sorted(range(len(part)), key=lambda k: loads[k])
    lo, hi = order[0], order[-1]
    out["part"] = [(p["name"], load, p["sfc_lb_hp_h"]) for p, load in zip(part, loads)]
    out["lines"].append((a["part_load"]["name"], "its two cruise points at 28,000 ft", intercept(loads[lo], part[lo]["sfc_lb_hp_h"], loads[hi], part[hi]["sfc_lb_hp_h"]), loads[lo]))
    for s in a["size_models"]:
        for r in s["rows"]:
            eta, kw = efficiency(kg_kwh(r["sfc_lb_hp_h"]), lhv["value"]), r["hp"] * cp.SHP
            out["sizes"].append({"row": r, "mw": kw / 1000, "eta": eta, "terminals": eta * gen, "kg": None if r.get("weight_lb") is None else r["weight_lb"] * LB,
                                 "kw_kg": None if r.get("weight_lb") is None else kw / (r["weight_lb"] * LB)})
    for m in a["masses"]:
        kg = m["kg"] if m.get("kg") else m["lb"] * LB
        out["masses"].append((m, kg, m["kw"] / kg))
    out["budget"] = [(b, b["value"] / gen, 3.6 / (b["value"] / gen * lhv["value"]) / LB * cp.SHP) for b in ref["budget"]]
    study = a["study_masses"]
    out["study"] = {"generator_kw": study["generator_hp"] * cp.SHP, "electric_kg": study["electric_lbm"] * LB, "engine_kg": study["engine_lbm"] * LB, "total_kg": study["total_lbm"] * LB,
                    "baseline": study["total_lbm"] / study["baseline_lbm"], "same_year": study["total_lbm"] / study["same_year_lbm"],
                    "doubled": (study["engine_lbm"] + 2 * study["electric_lbm"]) / study["baseline_lbm"]}
    return out


def render(a, r):
    ref, gen, lhv = a["reference"], a["generator_efficiency"]["value"], a["heating_value_mj_kg"]
    mw, band = ref["cruise_mw"]["value"], ref["takeoff_mw"]
    lines = ["### The rule of the screening at the candidate points", "",
             "The air a gas turbine takes in, against sea level at rest, by the rule the screening of the cruise points states: total pressure over the root of total temperature, "
             "in the standard atmosphere, behind an inlet that loses nothing. The screening takes the same work for each kilogram of air, so this is also its share of the sea-level power.", "",
             "| Altitude | Mach | True airspeed | Share of sea level at rest |", "|---|---|---|---|"]
    lines += [f"| {h:,.0f} ft | {m:.2f} | {kt:.0f} kt | {share:.3f} |" for h, m, share, kt in r["candidates"]]
    lines += ["", f"At the working reference, {ref['altitude_ft']['value']:,.0f} ft and {ref['speed_kt']['value']:.0f} kt, Mach {r['reference']['mach']:.3f}, the share is {r['reference']['rule']:.4f}: "
              f"{mw:.1f} MW at the gas turbines are {r['reference']['sea_level_mw']:.1f} MW referred to sea level, against {band['low']:.1f} to {band['high']:.1f} MW at take-off."]
    lines += ["", "### Two published tables beside the rule", "",
              "Each cell gives the power of the table in shp, then that power over the power the rule gives, twice: first with the maximum rated power as the sea-level figure, "
              "then with the maximum continuous power at sea level and at rest. Above 1, the engine of the table gives more than the rule."]
    for t in r["tables"]:
        table = t["table"]
        lines += ["", f"**{table['name']}.** {table['rating']}. Maximum rated power at sea level and at rest: {table['rated_shp']:,.0f} shp; maximum continuous power there: {t['at_rest']:,.0f} shp.", "",
                  "| True airspeed | " + " | ".join(c["key"] for c in table["conditions"]) + " |", "|---|" + "---|" * len(table["conditions"])]
        for k, v in enumerate(table["speeds_kt"]):
            lines.append(f"| {v:.0f} kt | " + " | ".join(f"{cells[k]['shp']:,.0f} · {cells[k]['rated']:.2f} · {cells[k]['continuous']:.2f}" for cells in t["grid"]) + " |")
        lines += ["", f"On a standard day at 25,000 ft and above, the table gives {t['rated_range'][0]:.2f} to {t['rated_range'][1]:.2f} times the rule on the first reading "
                  f"and {t['continuous_range'][0]:.2f} to {t['continuous_range'][1]:.2f} times on the second."]
    lines += ["", "### What the speed is worth", "", f"Power at {r['tables'][0]['table']['speeds_kt'][-1]:.0f} kt over power at rest, at the same altitude.", "",
              "| Condition | " + " | ".join(t["table"]["name"] for t in r["tables"]) + " | The rule |", "|---|" + "---|" * (len(r["tables"]) + 1)]
    for k, (key, _, share) in enumerate(r["tables"][0]["worth"]):
        lines.append(f"| {key} | " + " | ".join(f"{t['worth'][k][1]:.3f}" for t in r["tables"]) + f" | {share:.3f} |")
    lines += ["", "### The cruise power of the working reference, referred to sea level by each table", "",
              f"The tables stop below the working reference. The nearest tabulated point is taken, and {mw:.1f} MW are asked of the engine there.", "",
              "| Engine | Nearest tabulated point | Maximum continuous power there, for 7,500 shp rated | Maximum rated power at sea level | Maximum continuous power at sea level, at rest | By the rule at that point |",
              "|---|---|---|---|---|---|"]
    for t in r["tables"]:
        n = t["near"]
        lines.append(f"| {t['table']['name']} | {n['altitude_ft']:,.0f} ft, {n['kt']:.0f} kt | {n['mw']:.3f} MW | {n['rated_mw']:.1f} MW | {n['continuous_mw']:.1f} MW | {n['by_rule_mw']:.1f} MW |")
    lines += ["", "Carried from that point to the working reference by the shape of the rule, which is a hypothesis, the maximum rated power becomes "
              + " and ".join(f"{t['near']['carried_mw']:.1f}" for t in r["tables"]) + f" MW, against {r['reference']['sea_level_mw']:.1f} MW by the rule alone."]
    s, second = r["second"], a["second_document"]
    lines += ["", "### Two documents on one engine", "",
              f"{second['name']}: {second['available_hp']:,.0f} hp available for {second['engines']} engines at {second['altitude_ft']:,.0f} ft and {second['speed_kt']:.0f} kt, Mach {s['mach']:.3f}, "
              f"which is {s['share_rated']:.3f} of its maximum rated power. Scaled to the rated power of the table, that is {s['scaled']:,.0f} shp. The table, read between its four nearest values "
              f"by straight lines, gives {s['tabled']:,.0f} shp. The second document is {s['difference']:+.1%} from the table."]
    lines += ["", "### Consumption turned into efficiency", "",
              f"Shaft work over the heating value of the fuel, at {lhv['value']} MJ/kg; in brackets, at {lhv['high']} and at {lhv['low']} MJ/kg. The next column multiplies by a generator at {gen:.2f}: "
              "the boundary of the values of the budget, the terminals of the generator. No source read gives that product.", "",
              f"| Figure | As published | kg/kWh | Shaft efficiency | With a generator at {gen:.2f} | Read by | Class proposed |", "|---|---|---|---|---|---|---|"]
    lines += [f"| {e['name']} | {e['published']} | {e['kg_kwh']:.4f} | {e['eta']:.3f} ({e['low']:.3f} to {e['high']:.3f}) | {e['terminals']:.3f} | {READ[e['read']]} | {e['class'] or 'none'} |" for e in r["efficiencies"]]
    test = a["ground_test"]
    lines += ["", f"The bench test is on fuel of {test['heating_value_mj_kg']} MJ/kg, at {test['ambient_kpa']} kPa and {test['ambient_k']} K. At its own heating value its efficiencies are "
              + ", ".join(f"{x:.3f}" for x in r["test_own"]) + f". The cruise point of the flight datum is at Mach {r['flight_mach']:.2f}, with its indicated airspeed taken as calibrated.", "",
              "The values of the budget run from the fuel to the terminals of the generator. " + " ".join(
                  f"{b['value']:.3f} asks {shaft:.3f} at the shaft with a generator at {gen:.2f}, a consumption of {sfc:.3f} lb/(hp h)." for b, shaft, sfc in r["budget"])]
    for c in r["cycle"]:
        lines.append("")
        lines.append(f"{c['name']}, at full throttle at its cruise point against take-off: power {c['power']:.3f}, air {c['air']:.3f}, work for each kilogram of air {c['work']:.3f}. "
                     f"The rule gives {c['rule']:.3f} there. The model gives {c['power'] / c['rule']:.2f} times the rule: {c['air'] / c['rule']:.2f} times its air and {c['work']:.2f} times its work.")
    lines += ["", "### Efficiency and weight against the size of the unit, in one family of models", "",
              "Engines without a reduction gearbox, at their rated power at sea level and at rest. A model is not an engine, and the advanced rows are forecasts.", "",
              f"| Model | Technology | Rated power | lb/(hp h) | Shaft efficiency | With a generator at {gen:.2f} | Weight | Power for each kilogram | Class proposed |", "|---|---|---|---|---|---|---|---|---|"]
    for x in r["sizes"]:
        row = x["row"]
        weight = ("none | none" if x["kg"] is None else f"{x['kg']:.0f} kg | {x['kw_kg']:.1f} kW/kg")
        lines.append(f"| `{row['name']}` | {row['technology']} | {row['hp']:,.0f} hp, {x['mw']:.2f} MW | {dec(row['sfc_lb_hp_h'])} | {x['eta']:.3f} | {x['terminals']:.3f} | {weight} | {row['class']} |")
    lines += ["", "### Part load", "", "Consumption for each kilowatt-hour at a part of the power, over that at the reference of the same set: full throttle at the same flight condition, or take-off on the bench.", "",
              "| Set | Point | Share of the reference power | Consumption over the reference | Efficiency lost |", "|---|---|---|---|---|"]
    for name, point, load, ratio in r["loads"]:
        lost = 1 - 1 / ratio
        lines.append(f"| {name} | {point} | {load:.3f} | {ratio:.3f} | " + (f"{lost:.1%}" if lost >= 0 else f"a gain of {-lost:.1%}") + " |")
    lines += ["", f"{a['part_load']['name']}. No point at full power is published at its cruise condition.", "",
              "| Point | Share of the power available | lb/(hp h) |", "|---|---|---|"]
    lines += [f"| {name} | {load:.3f} | {dec(sfc)} |" for name, load, sfc in r["part"]]
    lines += ["", "A straight line of fuel flow against power through two points of a set is an assumption, not a reading. It gives the columns below. "
              "A value marked * is below the lowest point of its set: an extrapolation.", "",
              "| Set | Line through | Fuel flow at no power, as a share of full power | Consumption over full power at 70 % | at 60 % | at 50 % |", "|---|---|---|---|---|---|"]
    for name, through, slope, lowest in r["lines"]:
        lines.append(f"| {name} | {through} | {slope:.3f} | " + " | ".join(f"{on_line(slope, x):.3f}" + ("*" if x < lowest - 1e-9 else "") for x in (0.7, 0.6, 0.5)) + " |")
    lines += ["", "### Masses", "", "Rated power over mass, as each source bounds the mass. No row is a turbine with its generator, and none is an installed mass.", "",
              "| Item | Power | Mass | Power for each kilogram | Read by | Class proposed |", "|---|---|---|---|---|---|"]
    lines += [f"| {m['name']} | {m['kw']:,.0f} kW | {kg:.1f} kg | {ratio:.2f} kW/kg | {READ[m['read']]} | {m.get('class') or 'none'} |" for m, kg, ratio in r["masses"]]
    st, study = r["study"], a["study_masses"]
    lines += ["", f"{study['name']}: a generator of {st['generator_kw']:,.0f} kW, {st['electric_kg']:,.0f} kg of electric propulsion system and {st['engine_kg']:,.0f} kg of engine, {st['total_kg']:,.0f} kg together. "
              f"That is {st['baseline']:.2f} times the engine of its baseline of today and {st['same_year']:.2f} times its conventional engine of the same year. "
              f"With the electric system doubled it is {st['doubled']:.2f} times the engine of the baseline."]
    return lines


def run(folder, register, mode=None):
    """Return (failures, output lines). mode is None, "check" or "write" for the generated section of the README."""
    folder, register = pathlib.Path(folder), pathlib.Path(register)
    doc, failure = rp.read_yaml(folder / "turbogenerator-figures.yaml")
    bad, a = ([failure] if failure else []), None
    if not bad and not (isinstance(doc, dict) and isinstance(doc.get("analysis"), dict)):
        bad.append("turbogenerator-figures.yaml: the top-level key is `analysis`")
    if not bad:
        a = doc["analysis"]
        found = sorted(register.rglob(f"{a.get('knot')}.yaml")) if rp.has_text(a.get("knot")) else []
        record, failure = rp.read_yaml(found[0]) if len(found) == 1 else (None, f"{a.get('knot')}: expected in one file of the register, found in {len(found)}")
        if failure or not (isinstance(record, dict) and isinstance(record.get("knot"), dict)):
            bad.append(failure or f"{found[0].name}: the top-level key is `knot`")
        else:
            bad += validate(a, record["knot"], folder)
    head, body = "turbogenerator figures; rule failures: ", []
    if not bad:
        counted = figures(a)
        read = {k: sum(1 for x in counted if x.get("read") == k) for k in READ}
        head = (f"{a['id']} {a['version']} for {a['knot']}: {len(counted)} figures, {sum(1 for x in counted if x['basis'] == 'assumption')} of them assumptions; "
                f"of those read at a source, {read['both']} by two readers, {read['reviewer']} by the reviewer alone, {read['reported']} as reported; rule failures: ")
        body = [rp.safe(line) for line in [""] + render(a, compute(a))]
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
