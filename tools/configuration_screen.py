# Generated 2026-11-18 - configuration_screen.py (0.2.0)
"""Screening of configurations: fuselage sections, wings and cruise points, with a polar of first order and an empty mass by option.

    python3 tools/configuration_screen.py <analysis folder> <KNOT register> [--check | --write]

Reads configuration.yaml in the analysis folder, the mission screening and the cruise-point screening it names, and
the two KNOTs whose options it screens. It gives the dimensions of the fuselage of each section, and sets its drag
method on two types in service: on a jet for the skin friction, and on a turboprop for the drag level of the
propeller points. It sizes one aircraft for each combination of section, wing, cruise point and technology set:
lift-to-drag ratio, empty mass, take-off mass, fuel on the scoring mission, and the carbon dioxide metric at the best
ratio against the objective. Each is sized again with a mechanical drive, for comparison. It then repeats the
screening with one assumption changed at a time. The README of the folder holds the output between two markers:
--check fails when it differs, --write replaces it. Every figure printed follows from the figures of the inputs, and
the output says how many are assumptions. The tool chooses no option and states no conformity with any rule. It
exits with status 1 on a failure and then prints only its first line.
"""
import copy
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cruise_points as cp  # noqa: E402
import mission_closure as mc  # noqa: E402
import relations_project as rp  # noqa: E402

BEGIN, END = "<!-- configuration:begin -->", "<!-- configuration:end -->"
SECTIONS = ("id", "version", "date", "knot", "serves", "missions", "cruise_points", "section_knot", "wing_knot", "objective", "floor_speed_kt",
            "reference", "propeller_reference", "certified_jet", "cabin", "sections", "not_screened", "wings", "drag", "mass", "mechanical", "technology", "sensitivities")
BASES = ("source", "assumption", "decision")
NEEDED = {"reference": ("length_m", "width_m", "height_m", "cabin_length_m", "span_m", "wing_area_m2", "zero_fuel_kg", "usable_fuel_kg", "sweep_deg",
                        "cruise_mach", "cruise_altitude_ft", "wing_relief", "power_plant_share", "structure_share", "successor_below",
                        "successor_saving", "successor_span_m", "successor_wing_area_m2", "successor_usable_fuel_kg"),
          "propeller_reference": ("length_m", "diameter_m", "span_m", "wing_area_m2", "best_lift_to_drag", "seats", "seat_pitch_m", "cabin_width_m",
                                  "certified_mtom_kg", "certified_metric_kg_km", "certified_limit_kg_km"),
          "certified_jet": ("seats", "seat_pitch_m", "cabin_width_m", "certified_mtom_kg", "certified_metric_kg_km", "certified_limit_kg_km"),
          "cabin": ("seat_pitch_m", "service_area_m2", "flight_deck_m", "ends_factor", "wall_m"),
          "drag": ("skin_friction_low", "skin_friction_high", "taper_function", "fuselage_span_factor", "viscous_factor", "propeller_drag_share",
                   "brace_wetted_share", "wetted_factor", "root_chord_factor", "mean_chord_factor", "tail_volume_horizontal", "tail_volume_vertical",
                   "tail_arm_share", "nacelle_share", "sweep_above_mach", "sweep_deg", "wave_counts", "cruise_mass_share"),
          "mass": ("wing_constant", "wing_reference_span_m", "ultimate_load", "root_thickness_ratio", "spoilers", "relief_distributed", "braced_factor",
                   "fuselage_constant", "dive_speed_ms", "pressurised", "tail_kg_m2", "gear_share"),
          "mechanical": ("gearbox_efficiency", "generator_efficiency", "chain_mass_ratio")}
ITEMS = {"sections": ("cabin_width_m", "height_ratio", "mass_factor"), "wings": ("aspect_ratio", "loading_kg_m2"),
         "technology": ("turbogenerator_efficiency", "electric_chain_efficiency", "propulsor_factor", "drag_factor", "empty_factor",
                        "wing_tail_factor", "fuselage_factor", "chain_mass_ratio")}
LETTERS = (("A", 15), ("B", 24), ("C", 36), ("D", 52), ("E", 65), ("F", 80))       # aerodrome reference code: a letter up to, not including, a span in m
PARTS = ("wing", "fuselage", "tails", "gear", "propulsion", "rest")


def figures(node):
    """Every figure of the input: a mapping with a value and a basis."""
    if isinstance(node, dict):
        if "value" in node and "basis" in node:
            return [node]
        return [f for v in node.values() for f in figures(v)]
    if isinstance(node, list):
        return [f for v in node for f in figures(v)]
    return []


def values(section):
    """The figures of one section of the input, as plain numbers."""
    return {k: v["value"] for k, v in section.items() if isinstance(v, dict) and "value" in v}


def lookup(node, path):
    """The record at a dotted path. A list is entered by the key of one of its items."""
    for part in str(path).split("."):
        if isinstance(node, list):
            node = next((x for x in node if isinstance(x, dict) and x.get("key") == part), None)
        elif isinstance(node, dict):
            node = node.get(part)
        else:
            return None
    return node


def changed(a, missions, points, case):
    """Copies of the three inputs with the figures of one sensitivity case replaced, and a failure or None."""
    docs = {"analysis": copy.deepcopy(a), "missions": copy.deepcopy(missions), "points": copy.deepcopy(points)}
    for s in case.get("set") or []:
        target = lookup(docs.get(s.get("where", "analysis")), s.get("path")) if isinstance(s, dict) else None
        field = s.get("field", "value") if isinstance(s, dict) else None
        if not (isinstance(target, dict) and mc.number(target.get(field)) and mc.number(s.get("value")) and s["value"] >= 0):
            return a, missions, points, f"sensitivities: `{s.get('path') if isinstance(s, dict) else s}` is not a figure of the inputs, or its new value is not a number"
        target[field] = s["value"]
    return docs["analysis"], docs["missions"], docs["points"], None


def wetted_fuselage(diameter, length):
    """Wetted area of a fuselage with a cylindrical mid-section, after Torenbeek, in m2."""
    slenderness = length / diameter
    return math.pi * diameter * length * (1 - 2 / slenderness) ** (2 / 3) * (1 + 1 / slenderness ** 2)


def form_factor(slenderness):
    """Form factor of a fuselage from its slenderness, after DATCOM."""
    return 1 + 60 / slenderness ** 3 + slenderness / 400


def body(width, height, length, cabin=None):
    """A fuselage: its mean diameter, slenderness, wetted area, gross section and, with a cabin length, the floor the metric counts."""
    diameter = (width + height) / 2
    return {"outer": width, "height": height, "d": diameter, "length": length, "slenderness": length / diameter, "section": math.pi * width * height / 4,
            "wetted": wetted_fuselage(diameter, length), "cabin": cabin, "floor": None if cabin is None else width * cabin}


def section_geometry(cabin, section, passengers):
    """Dimensions of the fuselage of one section, for the passengers of the mission screening."""
    s = values(section)
    rows = math.ceil(passengers / section["abreast"])
    length = rows * cabin["seat_pitch_m"] + cabin["service_area_m2"] / s["cabin_width_m"]
    outer = s["cabin_width_m"] + 2 * cabin["wall_m"]
    height = outer * s["height_ratio"]
    out = body(outer, height, length + cabin["flight_deck_m"] + cabin["ends_factor"] * (outer + height) / 2, length)
    out.update(rows=rows, seats=rows * section["abreast"], mass_factor=s["mass_factor"])
    return out


def tail_areas(d, area, span, arm):
    """Horizontal and vertical tail areas from their volume coefficients, in m2."""
    chord = d["mean_chord_factor"] * area / span
    return d["tail_volume_horizontal"] * area * chord / arm, d["tail_volume_vertical"] * area * span / arm


def wetted_parts(d, geom, area, span, tails, reference_form, braced):
    """Wetted area by component, in m2. The fuselage is weighted by its form factor against that of the reference."""
    wing = d["wetted_factor"] * area * (1 - d["root_chord_factor"] * geom["outer"] / span)
    parts = {"fuselage": geom["wetted"] * form_factor(geom["slenderness"]) / reference_form, "wing": wing, "tails": d["wetted_factor"] * sum(tails),
             "brace": d["brace_wetted_share"] * wing if braced else 0.0}
    parts["nacelles"] = d["nacelle_share"] * sum(parts.values())
    return parts


def lift_factor(d, aspect, diameter, span):
    """Induced drag for a unit of lift coefficient squared: the planform and the fuselage, after Nita and Scholz, without friction."""
    return (1 + d["taper_function"] * aspect) / ((1 - d["fuselage_span_factor"] * (diameter / span) ** 2) * math.pi * aspect)


def wing_mass(m, d, zero_fuel, area, span, sweep_deg, relief, braced):
    """Mass of a wing after Torenbeek, from the zero-fuel mass it carries, in kg."""
    structural = span / math.cos(math.radians(sweep_deg))
    root = m["root_thickness_ratio"] * d["root_chord_factor"] * area / span
    share = (m["wing_constant"] * structural ** 0.75 * (1 + math.sqrt(m["wing_reference_span_m"] / structural))
             * m["ultimate_load"] ** 0.55 * ((structural / root) / (zero_fuel / area)) ** 0.30)
    return zero_fuel * share * (1 + m["spoilers"]) * relief * (m["braced_factor"] if braced else 1.0)


def fuselage_mass(m, geom, arm):
    """Mass of a pressurised fuselage after Torenbeek, in kg."""
    return m["fuselage_constant"] * math.sqrt(m["dive_speed_ms"] * arm / (geom["outer"] + geom["height"])) * geom["wetted"] ** 1.2 * m["pressurised"]


def cruise_state(altitude_ft, speed, unit):
    """True airspeed in m/s, Mach number and dynamic pressure in Pa at a cruise point."""
    t, pressure, sound = cp.atmosphere(altitude_ft)
    v = speed * (cp.KT if unit == "kt" else sound)
    return v, v / sound, 0.5 * pressure / (cp.R_AIR * t) * v * v


def best_ratio(zero, due):
    """Best lift-to-drag ratio of a polar: a drag at zero lift, and a drag due to lift for a unit of lift coefficient squared."""
    return 1 / (2 * math.sqrt(zero * due))


def metric_margin(co2, per_km, takeoff, floor):
    """The carbon dioxide metric over the new-type level at a take-off mass, less one."""
    metric = per_km * sum(cp.reference_masses(co2["reference_masses"], takeoff)) / 3 / floor ** co2["cabin_exponent"]["value"]
    return metric / cp.metric_limit(co2["limit"], takeoff) - 1


def certified_product(co2, energy, cabin, x, abreast, outer):
    """The floor of a type by the cabin rule of the screening, and the product of efficiency and lift-to-drag that its certified metric shows."""
    floor = outer * (math.ceil(x["seats"] / abreast) * x["seat_pitch_m"] + cabin["service_area_m2"] / x["cabin_width_m"])
    means = sum(cp.reference_masses(co2["reference_masses"], x["certified_mtom_kg"])) / 3
    return floor, 1000 * mc.G * means / (energy * x["certified_metric_kg_km"] * floor ** co2["cabin_exponent"]["value"])


def reference(a, missions, co2):
    """The method set on two types in service. On the jet: the skin-friction coefficient that gives it the lift-to-drag ratio of the mission
    screening, and the masses the method does not compute, by difference. On the turboprop: the zero-lift drag its published best ratio asks.
    With them, three checks on published figures: the metric of the jet, the fuel the wing of its successor holds, and the certified
    metric of the turboprop."""
    r, d, m = values(a["reference"]), values(a["drag"]), values(a["mass"])
    takeoff, operating = missions["reference"]["sizing_takeoff_kg"]["value"], missions["reference"]["basic_operating_kg"]["value"]
    area, span = r["wing_area_m2"], r["span_m"]
    geom = body(r["width_m"], r["height_m"], r["length_m"], r["cabin_length_m"])
    arm = d["tail_arm_share"] * geom["length"]
    tails = tail_areas(d, area, span, arm)
    form = form_factor(geom["slenderness"])
    wetted = sum(wetted_parts(d, geom, area, span, tails, form, False).values())
    _, mach, q = cruise_state(r["cruise_altitude_ft"], r["cruise_mach"], "mach")
    lift = d["cruise_mass_share"] * takeoff * mc.G / (q * area)
    aspect = span * span / area
    shape = lift_factor(d, aspect, geom["d"], span)
    wave = d["wave_counts"] * 1e-4 if mach > d["sweep_above_mach"] else 0.0
    target = missions["parameters"]["lift_to_drag"]["nominal"]
    zero = (lift / target - wave - shape * lift * lift) / (1 + d["viscous_factor"] * lift * lift)
    masses = {"wing": wing_mass(m, d, r["zero_fuel_kg"], area, span, r["sweep_deg"], r["wing_relief"], False), "fuselage": fuselage_mass(m, geom, arm),
              "tails": m["tail_kg_m2"] * sum(tails), "gear": m["gear_share"] * takeoff}
    structure, plant = sum(masses.values()), r["power_plant_share"] * takeoff
    fitted, friction, viscous = mc.fit(missions)["product"], zero * area / wetted, d["viscous_factor"]
    best = best_ratio(zero + wave, shape + viscous * zero)
    tank = area * area / span
    p = values(a["propeller_reference"])                           # a turboprop in service: what its published best ratio asks of the zero-lift drag
    other = body(p["diameter_m"], p["diameter_m"], p["length_m"])
    wet = sum(wetted_parts(d, other, p["wing_area_m2"], p["span_m"], tail_areas(d, p["wing_area_m2"], p["span_m"], d["tail_arm_share"] * p["length_m"]), form, False).values())
    edge = lift_factor(d, p["span_m"] ** 2 / p["wing_area_m2"], other["d"], p["span_m"])
    clean = friction * wet / p["wing_area_m2"]
    asked = ((-edge + math.sqrt(edge ** 2 + viscous / p["best_lift_to_drag"] ** 2)) / (2 * viscous) if viscous > 0 else 1 / (4 * p["best_lift_to_drag"] ** 2 * edge))
    energy, cabin, j = missions["fuel_energy_mj_per_kg"]["value"] * 1e6, values(a["cabin"]), values(a["certified_jet"])
    deck, product = certified_product(co2, energy, cabin, p, a["propeller_reference"]["abreast"], other["outer"])
    certified = {"floor": deck, "product": product, "efficiency": product / p["best_lift_to_drag"], "limit": cp.metric_limit(co2["limit"], p["certified_mtom_kg"]),
                 "share": p["certified_metric_kg_km"] / p["certified_limit_kg_km"], "loading": p["certified_mtom_kg"] / deck}
    deck, product = certified_product(co2, energy, cabin, j, a["certified_jet"]["abreast"], j["cabin_width_m"] + 2 * cabin["wall_m"])
    jet = {"floor": deck, "product": product, "share": j["certified_metric_kg_km"] / j["certified_limit_kg_km"], "loading": j["certified_mtom_kg"] / deck}
    return {"geom": geom, "form": form, "friction": friction, "zero": zero, "wetted": wetted, "area": area, "aspect": aspect, "lift": lift, "certified": certified, "certified_jet": jet,
            "target": target, "best": best, "efficiency": 1 / (math.pi * aspect * (shape + viscous * zero)), "takeoff": takeoff, "operating": operating,
            "masses": masses, "structure": structure, "plant": plant, "fixed": operating - structure - plant, "fitted": fitted,
            "nominal": mc.Model(missions, "nominal").product_b, "tank": tank, "holds": r["usable_fuel_kg"],
            "propeller": asked / clean, "propeller_clean": best_ratio(clean, edge + viscous * clean), "propeller_wetted": wet / p["wing_area_m2"],
            "cruise_margin": metric_margin(co2, 1000 * mc.G / (fitted * missions["fuel_energy_mj_per_kg"]["value"] * 1e6), takeoff, geom["floor"]),
            "margin": metric_margin(co2, 1000 * mc.G / (fitted * best / target * missions["fuel_energy_mj_per_kg"]["value"] * 1e6), takeoff, geom["floor"]),
            "expected": (1 - r["successor_below"]) / (1 - r["successor_saving"]) - 1,
            "successor_holds": r["usable_fuel_kg"] * r["successor_wing_area_m2"] ** 2 / r["successor_span_m"] / tank}


def evaluate(a, missions, model, co2, ref, geom, wing, point, tech, mechanical=False):
    """One aircraft: a section, a wing, a cruise point and a technology set, sized on the requirement mission."""
    d, m, t, w, drive = values(a["drag"]), values(a["mass"]), values(tech), values(wing), values(a["mechanical"])
    v, mach, q = cruise_state(point["altitude_ft"]["value"], point["speed"]["value"], point["speed"]["unit"])
    swept = mach > d["sweep_above_mach"]
    wave, sweep = (d["wave_counts"] * 1e-4, d["sweep_deg"]) if swept else (0.0, 0.0)
    chain = drive["gearbox_efficiency"] / drive["generator_efficiency"] if mechanical else t["electric_chain_efficiency"]
    ratio = drive["chain_mass_ratio"] if mechanical else t["chain_mass_ratio"]
    relief = a["reference"]["wing_relief"]["value"] if mechanical else m["relief_distributed"]
    efficiency = t["turbogenerator_efficiency"] * chain * point["propulsor_efficiency"]["value"] * t["propulsor_factor"]
    aspect, loading = w["aspect_ratio"], w["loading_kg_m2"]
    payload = missions["payload"]["passengers"] * missions["payload"]["kg_per_passenger"]["value"]
    energy = missions["fuel_energy_mj_per_kg"]["value"] * 1e6
    flown = {x["role"]: x for x in missions["missions"]}
    required, scored = model.equivalent_km(flown["requirement"]), model.equivalent_km(flown["scoring"])
    arm = d["tail_arm_share"] * geom["length"]
    fuselage = fuselage_mass(m, geom, arm) * geom.get("mass_factor", 1.0) * t["fuselage_factor"]
    state = {"empty": ref["operating"]}

    def size(takeoff):
        """The take-off mass that the aircraft sized at a take-off mass needs for the requirement mission."""
        area = takeoff / loading
        span = math.sqrt(aspect * area)
        tails = tail_areas(d, area, span, arm)
        parts = wetted_parts(d, geom, area, span, tails, ref["form"], wing["braced"])
        lift = d["cruise_mass_share"] * takeoff * mc.G / (q * area)
        zero = ref["friction"] * sum(parts.values()) / area * (1.0 if swept else 1 + d["propeller_drag_share"] * (ref["propeller"] - 1))
        slope = lift_factor(d, aspect, geom["d"], span) + d["viscous_factor"] * zero
        due = slope * lift * lift
        drag = (zero + wave + due) * t["drag_factor"]
        per_km = 1000 * mc.G / (efficiency * lift / drag * energy)
        best = best_ratio(zero + wave, slope) / t["drag_factor"]     # the applicant selects the altitude and the speed of the metric
        masses = {"fuselage": fuselage, "tails": m["tail_kg_m2"] * sum(tails) * t["wing_tail_factor"], "gear": m["gear_share"] * takeoff,
                  "propulsion": ref["plant"] * takeoff / ref["takeoff"] * ratio, "rest": ref["fixed"]}
        rest, empty = sum(masses.values()), state["empty"]
        for _ in range(60):                                         # the wing carries the zero-fuel mass, which holds the wing
            masses["wing"] = wing_mass(m, d, empty + payload, area, span, sweep, relief, wing["braced"]) * t["wing_tail_factor"]
            new = (rest + masses["wing"]) * t["empty_factor"]
            if abs(new - empty) < 0.001:
                break
            empty = new
        fraction = 1 - math.exp(-required * per_km)
        state.update(empty=empty, area=area, span=span, lift=lift, zero=zero, due=due, drag=drag, per_km=per_km, parts=parts, fraction=fraction, best=best,
                     masses={k: x * t["empty_factor"] for k, x in masses.items()}, efficiency=1 / (math.pi * aspect * slope))
        return (empty + payload) / (1 - fraction)

    takeoff, converged = ref["takeoff"], False
    for _ in range(40):                                             # Aitken's step on the fixed point of size()
        first = size(takeoff)
        if abs(first - takeoff) < 0.01:
            converged = True
            break
        second = size(first)
        bend = second - 2 * first + takeoff
        takeoff = second if abs(bend) < 1e-9 else takeoff - (first - takeoff) ** 2 / bend
        if not 1000 < takeoff < 1e6:
            break
    fraction = 1 - math.exp(-scored * state["per_km"])
    out = {"converged": converged and takeoff <= co2["limit"]["up_to_kg"], "tas": v, "mach": mach, "swept": swept, "takeoff": takeoff, "chain": efficiency,
           "ratio": state["lift"] / state["drag"], "propulsive": point["propulsor_efficiency"]["value"] * t["propulsor_factor"] * state["lift"] / state["drag"],
           "loaded": takeoff * state["fraction"], "holds": ref["holds"] * state["area"] ** 2 / state["span"] / ref["tank"],
           "scoring": (state["empty"] + payload) * fraction / (1 - fraction),
           "margin": metric_margin(co2, 1000 * mc.G / (efficiency * state["best"] * energy), takeoff, geom["floor"]) if 1000 < takeoff < 1e6 else None}
    out.update({k: state[k] for k in ("empty", "area", "span", "lift", "zero", "due", "parts", "masses", "efficiency", "best")})
    return out


def code_letter(span):
    """Aerodrome reference code letter of a wingspan in m."""
    return next((letter for letter, top in LETTERS if span < top), "beyond F")


def compute(a, missions, points, mechanical=True):
    """Every combination. Returns the reference, the geometry of each section and one row for each aircraft."""
    co2 = points["co2_metric"]
    ref = reference(a, missions, co2)
    cabin, model = values(a["cabin"]), mc.Model(missions, "nominal")
    geoms = {s["key"]: section_geometry(cabin, s, missions["payload"]["passengers"]) for s in a["sections"]}
    floor = a["floor_speed_kt"]["value"] * cp.KT
    rows = []
    for tech in a["technology"]:
        for s in a["sections"]:
            for w in a["wings"]:
                for p in points["points"]:
                    row = evaluate(a, missions, model, co2, ref, geoms[s["key"]], w, p, tech)
                    row.update(tech=tech["key"], point=p["key"], section=s["key"], wing=w["key"], floor=row["tas"] >= floor - 1e-6)
                    if mechanical:
                        other = evaluate(a, missions, model, co2, ref, geoms[s["key"]], w, p, tech, mechanical=True)
                        row["mechanical"] = other["margin"] if other["converged"] else None
                    rows.append(row)
    return ref, geoms, rows


def attempt(a, missions, points, mechanical=True):
    """compute(), or the kind of arithmetic failure that stopped it."""
    try:
        return compute(a, missions, points, mechanical), None
    except (ArithmeticError, ValueError, TypeError) as error:
        return None, type(error).__name__


def at_floor(rows, tech):
    """The aircraft of one technology set that close and fly at or above the floor of speed."""
    return [x for x in rows if x["tech"] == tech and x["floor"] and x["converged"]]


def knus(register):
    """The identifiers of every KNU of the register."""
    out = set()
    for path in sorted(register.rglob("KNOT-*.yaml")):
        doc = rp.read_yaml(path)[0]
        if isinstance(doc, dict) and isinstance(doc.get("knot"), dict):
            out |= {u.get("knu_id") for u in doc["knot"].get("knus") or [] if isinstance(u, dict)}
    return out


def validate(a, register, missions, points):
    bad = [f"`{k}` is missing" for k in SECTIONS if k not in a]
    if bad:
        return bad
    bad += ["date is a calendar date"] * (not rp.checked_date(a["date"]))
    for name, keys in NEEDED.items():
        bad += [f"{name}: `{k}` is a figure" for k in keys if not (isinstance(a[name], dict) and isinstance(a[name].get(k), dict) and "value" in a[name][k])]
    for name, keys in ITEMS.items():
        items = a[name] if rp.is_list_of(a[name], dict) and a[name] else None
        if items is None:
            bad.append(f"{name}: a list of records")
            continue
        found = [x.get("key") for x in items]
        bad += [f"{name}: each has a key of its own and a name"] * (len(set(found)) != len(found) or not all(rp.has_text(x.get("key")) and rp.has_text(x.get("name")) for x in items))
        bad += [f"{name}: {x.get('key')} gives `{k}`" for x in items for k in keys if not (isinstance(x.get(k), dict) and "value" in x[k])]
    if bad:
        return bad
    for f in figures(a):
        told = rp.has_text(f.get("ref")) if f.get("basis") in ("source", "decision") else rp.has_text(f.get("note"))
        if not (mc.number(f.get("value")) and f["value"] > 0 and f.get("basis") in BASES and told):
            bad.append(f"a figure needs a positive value, a basis among {', '.join(BASES)}, and a ref for a source or a decision or a note for an assumption: {str(f)[:80]}")
    bad += ["objective: below is a share between 0 and 1"] * (not (isinstance(a["objective"], dict) and isinstance(a["objective"].get("below"), dict)
                                                                    and mc.number(a["objective"]["below"].get("value")) and 0 < a["objective"]["below"]["value"] < 1))
    bad += ["floor_speed_kt is a figure"] * (not (isinstance(a["floor_speed_kt"], dict) and mc.number(a["floor_speed_kt"].get("value"))))
    for label, items, knot in (("sections", a["sections"], a["section_knot"]), ("wings", a["wings"], a["wing_knot"])):
        found = sorted(register.rglob(f"{knot}.yaml")) if rp.has_text(knot) else []
        record = rp.read_yaml(found[0])[0] if len(found) == 1 else None
        if not (isinstance(record, dict) and isinstance(record.get("knot"), dict)):
            bad.append(f"{knot}: expected in one file of the register")
            continue
        states = mc.option_states(record["knot"])
        bad += [f"{label}: {x['key']} names option {x.get('option')} of {knot}, which is not an open option" for x in items
                if not str(states.get(x.get("option"), "")).startswith("open")]
        screened = {x.get("option") for x in items} | {x.get("option") for x in a["not_screened"] if isinstance(x, dict) and x.get("knot") == knot}
        bad += [f"{knot}: option {o} is open and is neither screened nor named in not_screened" for o, state in states.items()
                if state.startswith("open") and o not in screened]
    bad += [f"sections: {s['key']} seats a whole number of passengers abreast" for s in a["sections"] if not (isinstance(s.get("abreast"), int) and s["abreast"] > 0)]
    bad += [f"wings: {w['key']} says whether it is braced" for w in a["wings"] if not isinstance(w.get("braced"), bool)]
    for name, label in (("propeller_reference", "certified_type"), ("certified_jet", "aircraft")):
        bad += [f"{name}: it seats a whole number of passengers abreast and names the type certified"] * (
            not (isinstance(a[name].get("abreast"), int) and a[name]["abreast"] > 0 and rp.has_text(a[name].get(label))))
    bad += ["not_screened: each entry names a KNOT, an option and a reason"] * (not (rp.is_list_of(a["not_screened"], dict)
                                                                                     and all(rp.has_text(x.get(k)) for x in a["not_screened"] for k in ("knot", "option", "reason"))))
    known = knus(register)
    bad += [f"serves: {k} is not a KNU of the register" for k in (a["serves"] if isinstance(a["serves"], list) else [a["serves"]]) if k not in known]
    bad += [f"{a['knot']}: expected in one file of the register"] * (not (rp.has_text(a["knot"]) and len(sorted(register.rglob(f"{a['knot']}.yaml"))) == 1))
    bad += ["the mission screening has a requirement mission and a scoring mission"] * (not {"requirement", "scoring"} <= {x.get("role") for x in missions["missions"]})
    bad += ["the cruise-point screening holds the carbon dioxide metric"] * (not isinstance(points.get("co2_metric"), dict))
    if not (rp.is_list_of(a["sensitivities"], dict) and all(rp.has_text(c.get("name")) and rp.is_list_of(c.get("set"), dict) and c["set"]
                                                              and c.get("report") in (None, "section", "wing", "cruise") for c in a["sensitivities"])):
        bad.append("sensitivities: each case has a name and a list of figures to set, and may report on the section, the wing or the cruise point")
    elif not bad:
        bad += [failure for failure in (changed(a, missions, points, c)[3] for c in a["sensitivities"]) if failure]
    return bad


def render(a, missions, points, ref, geoms, rows, cases):
    objective = -a["objective"]["below"]["value"]
    sets, sections, wings, pts = a["technology"], a["sections"], a["wings"], points["points"]
    grid = {(x["tech"], x["section"], x["wing"], x["point"]): x for x in rows}
    corner = (sets[0]["key"], sections[0]["key"], wings[0]["key"])
    fast = [p["key"] for p in pts if grid[corner + (p["key"],)]["floor"]]
    record = min(fast, key=lambda k: grid[corner + (k,)]["tas"]) if fast else pts[0]["key"]
    sk, wk, pk = [s["key"] for s in sections], [w["key"] for w in wings], [p["key"] for p in pts]

    def pct(x):
        return "-" if x is None else f"{100 * x:+.1f} %"

    def margin(x, key="margin"):
        if not x["converged"] or x.get(key) is None:
            return "does not close" if key == "margin" else "-"
        return f"**{pct(x[key])}**" if x[key] <= objective + 1e-9 else pct(x[key])

    def mean(found, tech, pairs):
        ratios = [found[b]["scoring"] / found[c]["scoring"] - 1 for b, c in (((tech,) + b, (tech,) + c) for b, c in pairs) if found[b]["converged"] and found[c]["converged"]]
        return sum(ratios) / len(ratios) if ratios else None

    out = ["### Sections", "",
           "| Section | Option | Abreast | Rows | Seats | Cabin width, m | Outer width and height, m | Gross section, m² | Cabin length, m | Fuselage length, m | Slenderness | Wetted area, m² | Floor for the metric, m² |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in sections:
        g = geoms[s["key"]]
        out.append(f"| `{s['key']}` {s['name']} | {s['option']} | {s['abreast']} | {g['rows']} | {g['seats']} | {s['cabin_width_m']['value']:.2f} | {g['outer']:.2f} × {g['height']:.2f} | "
                   f"{g['section']:.1f} | {g['cabin']:.1f} | {g['length']:.1f} | {g['slenderness']:.1f} | {g['wetted']:.0f} | {g['floor']:.1f} |")
    for x in a["not_screened"]:
        out += ["", f"Not screened: option {x['option']} of `{x['knot']}`. {x['reason']}."]
    r, g, d, prop, sure, jet, flown = a["reference"], ref["geom"], a["drag"], a["propeller_reference"], ref["certified"], a["certified_jet"], ref["certified_jet"]
    nominal, drive = values(sets[0]), values(a["mechanical"])
    spin = next(p for p in pts if p["key"] == record)["propulsor_efficiency"]["value"] * nominal["propulsor_factor"]
    out += ["", "### The method on two types in service", "",
            f"- **Geometry.** The {r['aircraft']} is {g['length']:.2f} m long with a wing of {ref['area']:.1f} m². It has a slenderness of {g['slenderness']:.1f} and, by the method, "
            f"a wetted area {ref['wetted'] / ref['area']:.2f} times its wing area.",
            f"- **Drag of the jet.** The mission screening takes a lift-to-drag ratio of {ref['target']:g} at nominal values, so that its product of efficiency and lift-to-drag, "
            f"{ref['nominal']:.2f}, is near the {ref['fitted']:.2f} it fits on the published sectors of the type. This screening takes that ratio as the one of the type in its cruise. "
            f"The method gives it with an equivalent skin-friction coefficient of {ref['friction']:.5f}, inside the {d['skin_friction_low']['value']:g} to "
            f"{d['skin_friction_high']['value']:g} of the source, and a span efficiency of {ref['efficiency']:.2f}. The best ratio of the type at that Mach number is then {ref['best']:.1f}.",
            f"- **Drag of a propeller aircraft.** With that coefficient the method gives the {prop['aircraft']} a wetted area {ref['propeller_wetted']:.2f} times its wing area and a best "
            f"lift-to-drag ratio of {ref['propeller_clean']:.1f}. The source gives it {prop['best_lift_to_drag']['value']:g}. The method meets that figure with a zero-lift drag "
            f"{ref['propeller']:.2f} times its own, and the propeller points of the screening carry {100 * d['propeller_drag_share']['value']:.0f} % of that excess.",
            f"- **Certified metric of a propeller aircraft.** EASA certified the {prop['certified_type']} at {prop['certified_metric_kg_km']['value']:g} kg/km and a take-off mass of "
            f"{prop['certified_mtom_kg']['value']:,} kg: {pct(sure['share'] - 1)} from the new-type level, which its database gives as {prop['certified_limit_kg_km']['value']:g} kg/km "
            f"and the formula of the screening as {sure['limit']:.3f}. With a floor of {sure['floor']:.1f} m² by the cabin rule of the screening, that metric is a product of efficiency "
            f"and lift-to-drag of {sure['product']:.2f}. At the best ratio above, the type then turns {sure['efficiency']:.3f} of the energy of its fuel into thrust work. The nominal "
            f"chain of the screening turns {nominal['turbogenerator_efficiency'] * nominal['electric_chain_efficiency'] * spin:.3f} at `{record}`, and "
            f"{nominal['turbogenerator_efficiency'] / drive['generator_efficiency'] * drive['gearbox_efficiency'] * spin:.3f} with a mechanical drive. "
            f"The type weighs {sure['loading']:.0f} kg at take-off for each square metre of that floor.",
            f"- **Certified metric of a jet.** EASA certified the {jet['aircraft']} at {jet['certified_metric_kg_km']['value']:g} kg/km and a take-off mass of "
            f"{jet['certified_mtom_kg']['value']:,} kg: {pct(flown['share'] - 1)} from the new-type level of {jet['certified_limit_kg_km']['value']:g} kg/km in its database. With a floor "
            f"of {flown['floor']:.1f} m² by the same rule, that metric is a product of efficiency and lift-to-drag of {flown['product']:.2f}. The type weighs {flown['loading']:.0f} kg "
            f"at take-off for each square metre of that floor.",
            f"- **Structure.** The method gives the {r['aircraft']} a wing of {ref['masses']['wing']:,.0f} kg, a fuselage of {ref['masses']['fuselage']:,.0f} kg, tails of "
            f"{ref['masses']['tails']:,.0f} kg and a landing gear of {ref['masses']['gear']:,.0f} kg: {ref['structure']:,.0f} kg, {100 * ref['structure'] / ref['takeoff']:.1f} % of its "
            f"take-off mass of {ref['takeoff']:,} kg. The sample breakdown on record gives {100 * r['structure_share']['value']:.2f} %.",
            f"- **The rest.** Its power plant is taken as {100 * r['power_plant_share']['value']:.2f} % of its take-off mass, {ref['plant']:,.0f} kg. What is left of its operating "
            f"mass of {ref['operating']:,} kg, {ref['fixed']:,.0f} kg of systems, furnishings and operating items, is held for every aircraft of the screening.",
            f"- **Metric.** The applicant selects the altitude and the speed of the carbon dioxide metric, so the screening takes it at the best lift-to-drag ratio of each aircraft. "
            f"With the fitted product raised in that proportion, a floor of {g['floor']:.1f} m² and that take-off mass, the metric of the {r['aircraft']} stands {pct(ref['margin'])} "
            f"from the new-type level; at its cruise it would stand {pct(ref['cruise_margin'])}. Its successor, the {r['successor']}, stands "
            f"{100 * r['successor_below']['value']:.0f} % below that level by the experts of ICAO and burns {100 * r['successor_saving']['value']:.1f} % less by its manufacturer: "
            f"the two together place the {r['aircraft']} at {pct(ref['expected'])}.",
            f"- **Fuel in the wing.** The fuel a wing holds is taken in proportion to the square of its area over its span, from the {ref['holds']:,} kg of the {r['aircraft']}. "
            f"The rule gives the wing of the {r['successor']} {ref['successor_holds']:,.0f} kg; it holds {r['successor_usable_fuel_kg']['value']:,} kg."]
    first = sets[0]
    out += ["", f"### Polar by option: {first['name']}", "",
            f"Wetted areas, drag and span efficiency at `{record}`, the slowest point at or above the floor of speed. The fuselage is weighted by its form factor against that of "
            f"the {r['aircraft']}. A count is one ten-thousandth of drag coefficient. The best ratio is that of the propeller points.", "",
            "| Section | Wing | Wing area, m² | Wetted, m²: fuselage · wing · tails · brace · nacelles | Over the wing area | Zero-lift drag, counts | Drag due to lift, counts | Span efficiency | "
            "Best lift-to-drag | " + " | ".join(f"Lift-to-drag at `{k}`" for k in pk) + " |", "|---|---|---|---|---|---|---|---|---|" + "---|" * len(pk)]
    for s in sk:
        for w in wk:
            x = grid[(first["key"], s, w, record)]
            parts = x["parts"]
            out.append(f"| `{s}` | `{w}` | {x['area']:.1f} | " + " · ".join(f"{parts[k]:.0f}" for k in ("fuselage", "wing", "tails", "brace", "nacelles"))
                       + f" | {sum(parts.values()) / x['area']:.2f} | {1e4 * x['zero']:.0f} | {1e4 * x['due']:.0f} | {x['efficiency']:.2f} | {x['best']:.1f} | "
                       + " | ".join(f"{grid[(first['key'], s, w, k)]['ratio']:.1f}" for k in pk) + " |")
    for p in pts:
        if isinstance(p.get("published"), dict):
            mine = [grid[(first["key"], s, w, p["key"])]["propulsive"] for s in sk for w in wk]
            sheet = mc.G * grid[corner + (p["key"],)]["tas"] / (1000 * p["published"]["cruise_shp"] * cp.SHP / p["published"]["takeoff_kg"])
            out += ["", f"Check on a published point, `{p['key']}`: the sheet read for it implies a product of propulsor efficiency and lift-to-drag of {sheet:.1f}, if its engines give "
                        f"their cruise rating there. The aircraft of this table have {min(mine):.1f} to {max(mine):.1f} at that point."]
    out += ["", f"### Empty mass by option: {first['name']}", "", f"Masses in kg at `{record}`.", "",
            "| Section | Wing | Wing | Fuselage | Tails | Landing gear | Propulsion system | Systems, furnishings and operating items | Empty mass |", "|---|---|---|---|---|---|---|---|---|"]
    for s in sk:
        for w in wk:
            x = grid[(first["key"], s, w, record)]
            out.append(f"| `{s}` | `{w}` | " + " | ".join(f"{x['masses'][k]:,.0f}" for k in PARTS) + f" | {x['empty']:,.0f} |")
    for tech in sets:
        t = values(tech)
        out += ["", f"### Screening: {tech['name']}", "",
                f"Turbogenerator {t['turbogenerator_efficiency']:.3f}, electrical chain {t['electric_chain_efficiency']:.2f}, propulsor of the point times {t['propulsor_factor']:g}; "
                f"drag times {t['drag_factor']:g}; empty mass times {t['empty_factor']:g}, wing and tail times {t['wing_tail_factor']:g}, fuselage times {t['fuselage_factor']:g}; "
                f"propulsion system at {t['chain_mass_ratio']:g} times a conventional one. Wing, masses, lift-to-drag ratio and fuel are those of `{record}`. The last columns are "
                f"margins of the carbon dioxide metric to the new-type level; a margin in bold meets the objective.", "",
                "| Section | Wing | Wing area, m² | Span, m | Letter | Lift-to-drag | Empty, t | Take-off, t | Fuel loaded over what the wing holds | Fuel, scoring mission, kg | "
                + " | ".join(f"`{k}`" + ("" if k in fast else ", below the floor") for k in pk) + f" | `{record}` with a mechanical drive |",
                "|---|---|---|---|---|---|---|---|---|---|" + "---|" * (len(pk) + 1)]
        for s in sk:
            for w in wk:
                x = grid[(tech["key"], s, w, record)]
                cells = (f"{x['area']:.1f} | {x['span']:.1f} | {code_letter(x['span'])} | {x['ratio']:.1f} | {x['empty'] / 1000:.1f} | {x['takeoff'] / 1000:.1f} | "
                         f"{x['loaded'] / x['holds']:.2f} | {x['scoring']:,.0f} | ") if x["converged"] else "- | - | - | - | - | - | - | - | "
                out.append(f"| `{s}` | `{w}` | " + cells + " | ".join(margin(grid[(tech["key"], s, w, k)]) for k in pk) + f" | {margin(x, 'mechanical')} |")
    out += ["", "### Against the objective", "",
            f"The objective is a margin of {pct(objective)} to the new-type level, or better. The floor of speed is {a['floor_speed_kt']['value']} kt.", "",
            "| Technology set | Least fuel on the scoring mission, at or above the floor | Its margin | Best margin at or above the floor | Best margin with a mechanical drive | "
            "Take-off mass for each m² of floor, kg | Meet the objective at or above the floor | Meet it below the floor |", "|---|---|---|---|---|---|---|---|"]
    for tech in sets:
        mine = at_floor(rows, tech["key"])
        slow = [x for x in rows if x["tech"] == tech["key"] and not x["floor"] and x["converged"]]
        if not mine:
            out.append(f"| {tech['name']} | none closes | - | - | - | - | 0 | - |")
            continue
        least, best = min(mine, key=lambda x: x["scoring"]), min(mine, key=lambda x: x["margin"])
        driven = [x for x in mine if x.get("mechanical") is not None]
        other = min(driven, key=lambda x: x["mechanical"]) if driven else None
        out.append(f"| {tech['name']} | `{least['point']}`, `{least['section']}`, `{least['wing']}`: {least['scoring']:,.0f} kg | {margin(least)} | "
                   f"`{best['point']}`, `{best['section']}`, `{best['wing']}`: {margin(best)} | "
                   + (f"`{other['point']}`, `{other['section']}`, `{other['wing']}`: {margin(other, 'mechanical')}" if other else "-")
                   + f" | {min(x['takeoff'] / geoms[x['section']]['floor'] for x in mine):.0f} to {max(x['takeoff'] / geoms[x['section']]['floor'] for x in mine):.0f}"
                   + f" | {sum(1 for x in mine if x['margin'] <= objective + 1e-9)} of {len(mine)} | {sum(1 for x in slow if x['margin'] <= objective + 1e-9)} of {len(slow)} |")
    out += ["", "### What the objective asks", "",
            "For the aircraft of best margin at or above the floor in each set: the product of efficiency and best lift-to-drag ratio it has, and the product that would put it "
            f"at the objective at its take-off mass and on its floor. The certified turboprop has {sure['product']:.2f}, at {prop['certified_mtom_kg']['value'] / 1000:.1f} t and "
            f"{sure['floor']:.1f} m²; the certified jet has {flown['product']:.2f}, at {jet['certified_mtom_kg']['value'] / 1000:.1f} t and {flown['floor']:.1f} m².", "",
            "| Technology set | Aircraft | Take-off mass, t | Floor, m² | Product it has | Product the objective asks |", "|---|---|---|---|---|---|"]
    for tech in sets:
        mine = at_floor(rows, tech["key"])
        if mine:
            best = min(mine, key=lambda x: x["margin"])
            has = best["chain"] * best["best"]
            out.append(f"| {tech['name']} | `{best['point']}`, `{best['section']}`, `{best['wing']}` | {best['takeoff'] / 1000:.1f} | {geoms[best['section']]['floor']:.1f} | "
                       f"{has:.2f} | {has * (1 + best['margin']) / (1 + objective):.2f} |")
    choices = (("Section", sk, sk[0], lambda k, o: [((k, w, p), (o, w, p)) for w in wk for p in pk]),
               ("Wing", wk, wk[0], lambda k, o: [((s, k, p), (s, o, p)) for s in sk for p in pk]),
               ("Cruise point", pk, record, lambda k, o: [((s, w, k), (s, w, o)) for s in sk for w in wk]))
    out += ["", "### One choice at a time", "",
            "Fuel on the scoring mission, averaged over the other two choices. A negative figure is less fuel.", "",
            "| Choice | " + " | ".join(t["name"] for t in sets) + " |", "|---|" + "---|" * len(sets)]
    for label, keys, base, make in choices:
        out += [f"| {label} `{k}` against `{base}` | " + " | ".join(pct(mean(grid, t["key"], make(k, base))) for t in sets) + " |" for k in keys if k != base]
    for case in cases:
        if case["report"]:
            found = {(x["tech"], x["section"], x["wing"], x["point"]): x for x in case["rows"]}
            label, keys, base, make = next(c for c in choices if c[0].lower().startswith(case["report"]))
            out += [f"| {label} `{k}` against `{base}`: {case['name'][0].lower() + case['name'][1:]} | " + " | ".join(pct(mean(found, t["key"], make(k, base))) for t in sets) + " |"
                    for k in keys if k != base]
    out += ["", "### One assumption at a time", "",
            "The whole screening again with one assumption changed. For each technology set, the least fuel on the scoring mission and the best margin of the aircraft at or above "
            "the floor of speed. The two may belong to different aircraft.", "",
            "| Assumption changed | Skin friction set on the jet | Zero-lift drag of the propeller points over the method | " + " | ".join(t["name"] for t in sets) + " |",
            "|---|---|---|" + "---|" * len(sets)]
    share = d["propeller_drag_share"]["value"]
    for case in [{"name": "None: the screening as it stands", "ref": ref, "rows": rows, "share": share}] + cases:
        cells = []
        for t in sets:
            mine = at_floor(case["rows"], t["key"])
            cells.append(f"{min(x['scoring'] for x in mine):,.0f} kg · {margin(min(mine, key=lambda x: x['margin']))}" if mine else "none closes")
        out.append(f"| {case['name']} | {case['ref']['friction']:.5f} | {1 + case['share'] * (case['ref']['propeller'] - 1):.2f} | " + " | ".join(cells) + " |")
    return out


def run(folder, register, mode=None):
    """Return (failures, output lines). mode is None, "check" or "write" for the generated section of the README."""
    folder, register = pathlib.Path(folder), pathlib.Path(register)
    doc, failure = rp.read_yaml(folder / "configuration.yaml")
    bad, a, missions, points = ([failure] if failure else []), None, None, None
    if not bad and not (isinstance(doc, dict) and isinstance(doc.get("analysis"), dict)):
        bad.append("configuration.yaml: the top-level key is `analysis`")
    if not bad:
        a = doc["analysis"]
        for key, name, tool in (("missions", "missions.yaml", mc), ("cruise_points", "cruise-points.yaml", cp)):
            source = folder.parent / str(a.get(key))
            if not (rp.has_text(a.get(key)) and (source / name).is_file()):
                bad.append(f"{key} names the folder of a screening beside this one")
            elif tool.run(source, register)[0]:
                bad.append(f"the screening {a[key]} fails its own check")
    if not bad:
        missions = rp.read_yaml(folder.parent / a["missions"] / "missions.yaml")[0]["analysis"]
        points = rp.read_yaml(folder.parent / a["cruise_points"] / "cruise-points.yaml")[0]["analysis"]
        bad += validate(a, register, missions, points)
    head, lines = "configuration screening; rule failures: ", []
    if not bad:
        found, failure = attempt(a, missions, points)
        bad += [f"the inputs give no aircraft ({failure})"] if failure else []
    if not bad:
        ref, geoms, rows = found
        low, high = a["drag"]["skin_friction_low"]["value"], a["drag"]["skin_friction_high"]["value"]
        bad += [f"the skin-friction coefficient set on the reference, {ref['friction']:.5f}, leaves the range of its source"] * (not low <= ref["friction"] <= high)
        bad += ["the masses left by difference on the reference are not positive"] * (ref["fixed"] <= 0)
    cases = []
    for case in a["sensitivities"] if not bad else []:
        b, flown, at, _ = changed(a, missions, points, case)
        found, failure = attempt(b, flown, at, mechanical=False)
        if failure:
            bad.append(f"sensitivities: `{case['name']}` gives no aircraft ({failure})")
        else:
            cases.append({"name": case["name"], "ref": found[0], "rows": found[2], "share": b["drag"]["propeller_drag_share"]["value"], "report": case.get("report")})
    if not bad:
        counted = figures(a)
        head = (f"{a['id']} {a['version']} for {a['knot']}: {len(a['sections'])} sections, {len(a['wings'])} wings and {len(points['points'])} cruise points "
                f"at {len(a['technology'])} technology sets, on the missions of {missions['id']} {missions['version']}; "
                f"{len(counted)} figures, {sum(1 for x in counted if x['basis'] == 'assumption')} of them assumptions; rule failures: ")
        lines = [rp.safe(line) for line in [""] + render(a, missions, points, ref, geoms, rows, cases)]
        if mode:
            failure = rp.generated_section(folder / "README.md", "\n".join([rp.safe(head) + "none"] + lines), mode == "write", BEGIN, END)
            bad += [failure] if failure else []
    bad = [rp.safe(b) for b in bad]
    return bad, [rp.safe(head) + (str(bad) if bad else "none")] + ([] if bad else lines)


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
