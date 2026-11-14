# Generated 2026-11-14 - essential_loads.py (0.1.0)
"""Budget of an essential load analysis: power, energy and battery size from a list of loads.

    python3 tools/essential_loads.py <analysis folder> <KNOT register> <S-ATLAS folder> [--check | --write]

Reads essential-loads.yaml in the analysis folder, checks its form and prints the budget. The README of the folder
holds the output between two markers: --check fails when it differs, --write replaces it. Every figure printed
follows from the figures of the input, and the output says how many of those are assumptions. The tool states no
conformity with any rule. It exits with status 1 on a failure and then prints only its first line.
"""
import math
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import relations_project as rp  # noqa: E402

LEVELS = ("low", "nominal", "high")
TIERS = ("immediate", "continued-flight", "landing")   # CS 25.1351(d): immediate safety, continued flight, landing
BASES = ("assumption", "source", "design")
SECTIONS = ("id", "version", "date", "knot", "serves", "scenario", "assumptions", "cases", "parameters", "loads",
            "events", "not_modelled")
BEGIN, END = "<!-- budget:begin -->", "<!-- budget:end -->"
ID = re.compile(r"[A-Z]\d{2}")


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def share(value):
    return number(value) and 0 < value <= 1


def triple(value):
    return (isinstance(value, dict) and set(LEVELS) <= set(value) and all(number(value[k]) for k in LEVELS)
            and 0 <= value["low"] <= value["nominal"] <= value["high"])


def figures(a):
    """Every record of the input that carries a figure, with a label."""
    p = a["parameters"]
    return ([(x["id"], x) for x in a["loads"] + a["events"]] + [(d["key"], d) for d in p["durations"]]
            + [(f["key"], f) for f in p["battery_factors"]]
            + [("distribution_efficiency", p["distribution_efficiency"]), ("specific_energy_wh_per_kg", p["specific_energy_wh_per_kg"])])


def validate(a, TAX, knot):
    """Failures of form. The budget is computed only when this returns none."""
    if not isinstance(a, dict) or [s for s in SECTIONS if s not in a]:
        return ["essential-loads.yaml: `analysis` must hold " + ", ".join(SECTIONS)]
    bad, p = [], a["parameters"]
    lists = {"assumptions": ("id", "text"), "cases": ("key", "text"), "loads": ("id", "service", "tier", "item", "taxonomy", "when"),
             "events": ("id", "service", "tier", "item", "taxonomy", "when"), "not_modelled": ("item", "taxonomy", "reason")}
    for name, fields in lists.items():
        if not rp.is_list_of(a[name], dict) or not all(rp.has_text(x.get(f)) for x in a[name] for f in fields):
            bad.append(f"{name}: each record has text in " + ", ".join(fields))
    if not isinstance(p, dict) or [k for k in ("durations", "distribution_efficiency", "battery_factors", "specific_energy_wh_per_kg") if k not in p]:
        bad.append("parameters: durations, distribution_efficiency, battery_factors and specific_energy_wh_per_kg are required")
    elif not (rp.is_list_of(p["durations"], dict) and p["durations"] and rp.is_list_of(p["battery_factors"], dict)
              and isinstance(p["distribution_efficiency"], dict) and isinstance(p["specific_energy_wh_per_kg"], dict)):
        bad.append("parameters: durations and battery_factors are lists of records; the other two are records")
    if bad or not all(rp.has_text(a[k]) for k in ("id", "version", "knot", "serves", "scenario")) or not rp.checked_date(a["date"]):
        return bad or ["essential-loads.yaml: id, version, knot, serves and scenario are text, and date is a date"]

    cases = {c["key"] for c in a["cases"]}
    ids = [x["id"] for x in a["loads"] + a["events"]]
    bad += [f"{i}: the identifier is used more than once" for i in sorted({i for i in ids if ids.count(i) > 1})]
    for x in a["loads"] + a["events"]:
        i = x["id"]
        if not ID.fullmatch(i):
            bad.append(f"{i}: an identifier is a letter and two digits")
        if x["taxonomy"] not in TAX:
            bad.append(f"{i}: {x['taxonomy']} is not an S-ATLAS address")
        if x["tier"] not in TIERS:
            bad.append(f"{i}: tier is one of " + ", ".join(TIERS))
        if x["when"] != "always" and x["when"] not in cases:
            bad.append(f"{i}: when is `always` or a declared case")
        if not triple(x.get("power_w")):
            bad.append(f"{i}: power_w holds low, nominal and high, none negative and in that order")
    for x in a["loads"]:
        if not share(x.get("duty")) or x.get("feeds") not in (1, 2, 3):
            bad.append(f"{x['id']}: duty is above 0 and at most 1, and feeds is 1, 2 or 3")
    for x in a["events"]:
        if not (number(x.get("seconds")) and x["seconds"] > 0 and isinstance(x.get("count"), int) and x["count"] >= 1):
            bad.append(f"{x['id']}: seconds is positive and count is a whole number of at least 1")
    if not any(x["when"] == "always" and number(x.get("power_w", {}).get("nominal")) and x["power_w"]["nominal"] > 0 for x in a["loads"] if isinstance(x.get("power_w"), dict)):
        bad.append("loads: at least one load is always on, with a nominal power above zero")
    bad += [f"not modelled, {x['item']}: {x['taxonomy']} is not an S-ATLAS address" for x in a["not_modelled"] if x["taxonomy"] not in TAX]

    standing = {o.get("id") for o in knot.get("options") or [] if isinstance(o, dict) and o.get("state") in rp.LIVE}
    for d in p["durations"]:
        key = d.get("key")
        if not (rp.has_text(key) and rp.has_text(d.get("text")) and number(d.get("minutes")) and d["minutes"] > 0
                and isinstance(d.get("events"), bool) and rp.is_list_of(d.get("options"), str)):
            bad.append(f"duration {key}: key and text, positive minutes, events true or false, and a list of options")
        elif set(d["options"]) - standing:
            bad.append(f"duration {key}: {', '.join(sorted(set(d['options']) - standing))} is not a standing option of {a['knot']}")
    if not all(rp.has_text(f.get("key")) and rp.has_text(f.get("text")) and share(f.get("value")) for f in p["battery_factors"]):
        bad.append("battery_factors: each has a key, a text and a value above 0 and at most 1")
    if not share(p["distribution_efficiency"].get("value")):
        bad.append("distribution_efficiency: the value is above 0 and at most 1")
    if not triple(p["specific_energy_wh_per_kg"]) or p["specific_energy_wh_per_kg"]["low"] <= 0:
        bad.append("specific_energy_wh_per_kg: low, nominal and high, positive and in that order")
    if not bad:
        for label, x in figures(a):
            if x.get("basis") not in BASES:
                bad.append(f"{label}: basis is one of " + ", ".join(BASES))
            elif x["basis"] != "assumption" and not rp.has_text(x.get("ref")):
                bad.append(f"{label}: a figure with basis {x['basis']} names its reference in ref")
    return bad


def budget(a, cases=()):
    """Power, energy and battery size at each level, for the loads that are always on and those of the cases given."""
    p = a["parameters"]
    efficiency, derating = p["distribution_efficiency"]["value"], math.prod(f["value"] for f in p["battery_factors"])
    on = lambda x: x["when"] == "always" or x["when"] in cases
    loads, events, out = [x for x in a["loads"] if on(x)], [x for x in a["events"] if on(x)], {}
    for level in LEVELS:
        at_loads = sum(x["power_w"][level] * x["duty"] for x in loads)
        source = at_loads / efficiency
        event_wh = sum(x["power_w"][level] * x["seconds"] * x["count"] for x in events) / 3600 / efficiency
        durations = {}
        for d in p["durations"]:
            energy = source * d["minutes"] / 60 + (event_wh if d["events"] else 0)       # Wh at the source
            durations[d["key"]] = {"energy_wh": energy, "nameplate_wh": energy / derating,
                                   "rate": source * derating / energy if energy else 0}  # discharges per hour
        out[level] = {"at_loads_w": at_loads, "source_w": source, "event_wh": event_wh, "durations": durations,
                      "peak_w": source + max((x["power_w"][level] for x in events), default=0) / efficiency}
    return out


def render(a, knot, TAX):
    p, base = a["parameters"], budget(a)
    se = p["specific_energy_wh_per_kg"]
    kw, kwh, cell = (lambda w: f"{w / 1000:.2f}"), (lambda wh: f"{wh / 1000:.2f}"), (lambda text: str(text).replace("|", "/"))
    three = lambda fn: " | ".join(fn(base[level]) for level in LEVELS)
    address = lambda t: f"`{t}` {TAX[t]}"
    note = lambda x: f" — {cell(x['note'])}" if x.get("note") else ""
    always = [x for x in a["loads"] if x["when"] == "always"]

    lines = [f"Scenario: {cell(' '.join(a['scenario'].split()))}", "", "### Loads", "", "| Id | Service | Tier | Load | S-ATLAS | Low W | Nominal W | High W | Duty | Feeds | When | Basis |",
             "|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|"]
    for x in a["loads"]:
        w = x["power_w"]
        lines.append(f"| {x['id']} | {x['service']} | {x['tier']} | {cell(x['item'])}{note(x)} | {address(x['taxonomy'])} | {w['low']:g} | "
                     f"{w['nominal']:g} | {w['high']:g} | {x['duty']:g} | {x['feeds']} | {x['when']} | {x['basis']} |")
    lines += ["", "### Events", "", "| Id | Service | Tier | Event | S-ATLAS | Low W | Nominal W | High W | Seconds | Count | When | Basis |",
              "|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|"]
    for x in a["events"]:
        w = x["power_w"]
        lines.append(f"| {x['id']} | {x['service']} | {x['tier']} | {cell(x['item'])}{note(x)} | {address(x['taxonomy'])} | {w['low']:g} | "
                     f"{w['nominal']:g} | {w['high']:g} | {x['seconds']:g} | {x['count']} | {x['when']} | {x['basis']} |")

    total = base["nominal"]["at_loads_w"]
    lines += ["", "### Continuous load by service, base case", "", "| Service | Loads | Low W | Nominal W | High W | Share of nominal |", "|---|---:|---:|---:|---:|---:|"]
    for service in dict.fromkeys(x["service"] for x in always):
        rows = [x for x in always if x["service"] == service]
        low, nominal, high = (sum(x["power_w"][level] * x["duty"] for x in rows) for level in LEVELS)
        lines.append(f"| {service} | {len(rows)} | {low:.0f} | {nominal:.0f} | {high:.0f} | {nominal / total:.0%} |")
    lines.append(f"| **Total at the loads** | {len(always)} | " + " | ".join(f"{base[level]['at_loads_w']:.0f}" for level in LEVELS) + " | 100% |")
    lines += ["", "### Continuous load by tier, base case", "", "| Tier | Loads | Nominal W | Share |", "|---|---:|---:|---:|"]
    for tier in TIERS:
        rows = [x for x in always if x["tier"] == tier]
        if not rows:
            continue                                  # what belongs to the landing alone is an event
        nominal = sum(x["power_w"]["nominal"] * x["duty"] for x in rows)
        lines.append(f"| {tier} | {len(rows)} | {nominal:.0f} | {nominal / total:.0%} |")

    lines += ["", "### Budget, base case", "", "| | Low | Nominal | High |", "|---|---:|---:|---:|",
              "| Continuous load at the loads, kW | " + three(lambda b: kw(b["at_loads_w"])) + " |",
              "| Continuous load at the source, kW | " + three(lambda b: kw(b["source_w"])) + " |",
              "| Peak demand at the source, kW | " + three(lambda b: kw(b["peak_w"])) + " |",
              "| Events, kWh at the source | " + three(lambda b: kwh(b["event_wh"])) + " |"]
    lines += [f"| Energy for {d['minutes']:g} min, kWh at the source | " + three(lambda b: kwh(b["durations"][d["key"]]["energy_wh"])) + " |"
              for d in p["durations"]]

    lines += ["", "### Battery by role, base case", "", "| Role | Options | Minutes | Nameplate kWh, low · nominal · high loads | Mass kg | Range kg | Rate per hour |",
              "|---|---|---:|---:|---:|---:|---:|"]
    for d in p["durations"]:
        low, nominal, high = (base[level]["durations"][d["key"]] for level in LEVELS)
        lines.append(f"| {cell(d['text'])}{'' if d['events'] else ', events excluded'} | {' · '.join(d['options']) or '—'} | {d['minutes']:g} | "
                     f"{kwh(low['nameplate_wh'])} · {kwh(nominal['nameplate_wh'])} · {kwh(high['nameplate_wh'])} | {nominal['nameplate_wh'] / se['nominal']:.0f} | "
                     f"{low['nameplate_wh'] / se['high']:.0f}–{high['nameplate_wh'] / se['low']:.0f} | {nominal['rate']:.1f} |")
    factors = " × ".join(f"{f['value']:g}" for f in p["battery_factors"])
    lines += ["", f"Nameplate is the energy at the source divided by {factors} = {math.prod(f['value'] for f in p['battery_factors']):.3f}. "
              f"Mass is at nominal loads and {se['nominal']:g} Wh/kg. The range runs from low loads at {se['high']:g} Wh/kg to high loads at {se['low']:g} Wh/kg. "
              "It is the mass of the battery alone. Rate is the continuous power at the source over the nameplate energy."]

    longest = max(p["durations"], key=lambda d: d["minutes"])
    lines += ["", "### Cases", "", f"| Case | Average load added W | Continuous at the source kW | Nameplate for {longest['minutes']:g} min kWh | Mass kg at {se['nominal']:g} Wh/kg |",
              "|---|---:|---:|---:|---:|"]
    keys = [c["key"] for c in a["cases"]]
    for combo in [()] + [(k,) for k in keys] + ([tuple(keys)] if len(keys) > 1 else []):
        b = budget(a, combo)["nominal"]
        nameplate = b["durations"][longest["key"]]["nameplate_wh"]
        lines.append(f"| {'base + ' + ' + '.join(combo) if combo else 'base'} | {b['at_loads_w'] - total:.0f} | {kw(b['source_w'])} | {kwh(nameplate)} | {nameplate / se['nominal']:.0f} |")
    lines += [""] + [f"Case `{c['key']}`: {cell(c['text'])}." for c in a["cases"]]

    lines += ["", "### Assumptions", "", "| Id | Assumption |", "|---|---|"] + [f"| {x['id']} | {cell(x['text'])} |" for x in a["assumptions"]]
    lines += ["", "### Not modelled", "", "| Item | S-ATLAS | Reason |", "|---|---|---|"]
    lines += [f"| {cell(x['item'])} | {address(x['taxonomy'])} | {cell(x['reason'])} |" for x in a["not_modelled"]]

    outside = sorted({x["taxonomy"][:3] for x in a["loads"] + a["events"]} - {str(t)[:3] for t in knot.get("taxonomy") or []})
    lines += ["", f"Chapters of loads outside the `taxonomy` field of `{a['knot']}`: " + (" · ".join(f"`{c}`" for c in outside) or "none") + "."]
    return lines


def run(folder, register, tax_root, mode=None):
    """Return (failures, output lines). mode is None, "check" or "write" for the generated section of the README."""
    folder = pathlib.Path(folder)
    doc, failure = rp.read_yaml(folder / "essential-loads.yaml")
    bad, a, TAX, knot = ([failure] if failure else []), None, rp.titles(tax_root), None
    if not TAX:
        bad.append("no S-ATLAS node found under the taxonomy path")
    if not bad and not (isinstance(doc, dict) and isinstance(doc.get("analysis"), dict)):
        bad.append("essential-loads.yaml: the top-level key is `analysis`")
    if not bad:
        a = doc["analysis"]
        found = sorted(pathlib.Path(register).rglob(f"{a.get('knot')}.yaml")) if rp.has_text(a.get("knot")) else []
        record, failure = rp.read_yaml(found[0]) if len(found) == 1 else (None, f"{a.get('knot')}: expected in one file of the register, found in {len(found)}")
        if failure or not (isinstance(record, dict) and isinstance(record.get("knot"), dict)):
            bad.append(failure or f"{found[0].name}: the top-level key is `knot`")
        else:
            knot = record["knot"]
            bad += validate(a, TAX, knot)
    head, body = "essential loads; rule failures: ", []
    if not bad:
        counted = figures(a)
        assumed = sum(1 for _, x in counted if x["basis"] == "assumption")
        head = (f"{a['id']} {a['version']} for {a['knot']}: {len(a['loads'])} loads, {len(a['events'])} events, {len(a['cases'])} cases; "
                f"{len(counted)} figures, {assumed} of them assumptions; rule failures: ")
        body = [rp.safe(line) for line in [""] + render(a, knot, TAX)]
        if mode:
            failure = rp.generated_section(folder / "README.md", "\n".join([rp.safe(head) + "none"] + body), mode == "write", BEGIN, END)
            bad += [failure] if failure else []
    bad = [rp.safe(b) for b in bad]
    return bad, [rp.safe(head) + (str(bad) if bad else "none")] + ([] if bad else body)


def main(argv):
    paths, flags = [x for x in argv[1:] if not x.startswith("--")], [x for x in argv[1:] if x.startswith("--")]
    if len(paths) != 3 or len(flags) > 1 or not set(flags) <= {"--check", "--write"}:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    bad, lines = run(*paths, mode=flags[0][2:] if flags else None)
    print("\n".join(lines))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
