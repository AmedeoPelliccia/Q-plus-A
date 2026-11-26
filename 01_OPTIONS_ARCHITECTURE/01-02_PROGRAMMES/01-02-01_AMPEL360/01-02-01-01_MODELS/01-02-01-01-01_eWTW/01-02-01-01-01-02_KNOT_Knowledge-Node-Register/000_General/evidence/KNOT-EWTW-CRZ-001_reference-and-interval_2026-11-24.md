# Review record — a reference for cruise, section and wing, and the interval of criterion M5

| | |
|---|---|
| KNOT | `KNOT-EWTW-CRZ-001` Cruise point |
| Serves | [Ruling R2](KNOT-EWTW-CRZ-001_ruling-R2_2026-11-24.md) of 2026-11-24; `KNOT-EWTW-FUS-001`, `KNOT-EWTW-WNG-001`, `KNOT-EWTW-AER-001`, `KNOT-EWTW-GEN-001` |
| Produced by | Claude, 2026-11-24 |
| Read by | A second reader re-ran the figures of this record with the same tool and obtained the same values. The method has no independent check: both readers use [`tools/configuration_screen.py`](../../../../../../../../tools/configuration_screen.py) |
| Status | Figures of first order, added to the [screening of the configurations](CFG-EWTW-AER-001/README.md) 0.2.0 and not part of its tables. The method of the interval is proposed and not ratified |

On 2026-11-20 and 2026-11-24 the authority forwarded two notes of a second reader, outside the repository. The first proposes a reference configuration, with a calculation. The second gives an opinion on the ten criteria and on a first budget of uncertainty. This record holds what was reproduced, what the reviewer added, what the second reader corrected, and the method proposed for the interval. The notes are not filed here.

---

## The proposal, reproduced

The first note proposes: 360 kt at 31,000 ft, the section of five abreast (`F5`), and a braced wing of 40.0 m of span with fixed tips, aspect ratio 17, 94.1 m². It fixes that geometry and runs the equations of the screening on the three technology sets. The reviewer ran its script as written and obtained its figures.

| Technology set | Take-off mass | Fuel loaded, 2,000 km | Fuel loaded, about 1,100 km | Margin on the new-type level |
|---|---:|---:|---:|---:|
| Nominal | 50.0 t | 7,316 kg | 4,860 kg | +2.1 % |
| Baskets of the ICAO experts for 2037 | 39.1 t | 5,289 kg | 3,521 kg | −27.2 % |
| Favourable | 38.2 t | 4,785 kg | 3,192 kg | −34.7 % |

- The wing holds 9,642 kg of fuel by the rule of the screening: the fuel of the requirement mission fits at nominal values.
- At 25,000 ft the same aircraft loads 5,370 kg at nominal values and 4,016 kg with the baskets: 31,000 ft takes 9.5 % and 12.3 % off.
- With an aspect ratio of 20 at the same span the fuel does not fit at nominal values: 7,121 kg against 6,966 kg.
- With the turbogenerator 2 % less efficient, the margin with the baskets is −25.6 %.

## What the reviewer added

Each line changes one thing on the aircraft of the proposal, with the baskets of 2037, and closes the masses again.

**The span buys the metric and costs fuel.** Braced wing, aspect ratio 17:

| Span | Code letter | Margin | Fuel on about 1,100 km |
|---:|---|---:|---:|
| 34.5 m | C | −21.1 % | 3,390 kg, the least |
| 35.9 m | C | −23.0 % | 3,402 kg |
| 38.6 m | D | −26.0 % | 3,467 kg |
| 40.0 m | D | −27.2 % | 3,521 kg |
| 44.0 m | D | −29.6 % | 3,730 kg |

- **Inside code letter C the objective is not met.** At 35.9 m the best margin over aspect ratios of 10 to 20, braced or not, is −23.9 %.
- **The method does not show that the brace pays.** A cantilever wing of the same span and aspect ratio gives −27.9 % and 3,467 kg. Its wing is 1.26 t heavier, and the brace adds wetted area. The wing formula has no term for stiffness or flutter, so it cannot settle this.
- **31,000 ft is not an optimum of the model.** At 360 kt the fuel on about 1,100 km falls from 4,016 kg at 25,000 ft to 3,521 kg at 31,000 ft and 3,261 kg at 35,000 ft. The model does not size the gas turbines with altitude. By the rule the [screening of the cruise points](CRP-EWTW-CRZ-001/README.md) assumes, the cruise asks 13.0 MW referred to sea level at 25,000 ft, 14.2 MW at 31,000 ft and 15.3 MW at 35,000 ft, against about 7.9 MW at take-off.
- **The floor of 360 kt costs fuel.** At 330 kt and 31,000 ft the same aircraft loads 3,228 kg, 8.3 % less.
- **The section does not decide.** With the same wing: four abreast −27.1 % and 3,564 kg, five abreast −27.2 % and 3,521 kg, five abreast in the width of six −24.9 %, six abreast −25.2 %.
- **The electrical chain costs ten points here too.** With a mechanical drive the same aircraft stands at −37.4 %.

## What the second reader corrected

- **The floor of `M5` is not a limit of the type certificate.** Corrected on 2026-11-20 ([record of the objective](KNOT-EWTW-CRZ-001_objective-and-premises_2026-11-18.md)).
- **A quadrature over gains that are not demonstrated has no statistical meaning.** The first budget of the reviewer combined nine lines in quadrature and gave an unfavourable end of −12.5 %. Four of those lines are forecasts with no probability on record. Withdrawn together they move the margin by 29.3 points, to the +2.1 % of the nominal set, where the quadrature of the four gives 13.2. The method below treats them as scenarios.
- **`M2` follows the certified envelope**, and not the cruise point: it applies if certification for operation above 25,000 ft is requested. The authority approved it so.

## Two measures proposed for the section, not approved

The first note proposes a measure for each purpose of the wide tube. They belong to `KNOT-EWTW-FUS-001` and wait for its criteria.

| Purpose | Proposed | Remark of the reviewer |
|---|---|---|
| Comfort | At least 470 mm between lowered armrests in each of the 100 seats | It is the seat of an aircraft in service with this cabin width, so the section of five abreast meets it by construction. Width alone does not see that two and three puts 20 passengers of 100 in a middle seat |
| Ground for hydrogen tanks | Room for a cylinder of 2.90 m by 5.00 m, with the 100 seats kept | Such an envelope holds 1.3 to 1.8 t of liquid hydrogen, by wall thickness and heads. The fuel of the requirement mission is worth 1.9 t at equal energy with the baskets and 2.6 t at nominal values. With 21.2 m of cabin in 32.4 m of fuselage no volume of full section is 5 m long: it is the stretch of a derivative. On this aircraft the diameter is what can be verified |

## The interval of criterion M5: a method, proposed

Criterion `M5` as approved asks, at the release of the preliminary-design baseline, that the justified upper limit of the margin is at or below −26 %. The authority asked for a method to decide that limit together. This one is the reviewer's, as corrected by the second reader.

1. **Object.** The margin of the reference aircraft on the new-type level of 2017, by the tool of record.
2. **Lines.** Each input that moves the margin by half a point or more has a line, with the KNOT that closes it. Two more lines: the gap between the model and data, and the sum of the inputs below half a point.
3. **Class of evidence.** Each line has one. The central value and its extreme are justified apart.

   | Class | Evidence | How the line is treated |
   |---|---|---|
   | A | Measured on representative hardware at cruise conditions, with calibration, repeatability and installation | A distribution, from the measurement |
   | B | Measured on similar hardware, or published test data, with the transfer documented | A distribution, from the spread between sources |
   | C | A method or a statistic | A distribution or a justified limit, from its scatter against representative data |
   | D | An assumption or a forecast | A scenario: the gain is granted or withdrawn. It is not a distribution |

4. **Scenarios.** Every combination of lines of class D that is still credible is a scenario, computed with its inputs together. So are the wing configurations left open.
5. **Propagation.** Inside each scenario the lines of classes A to C are propagated together, with their dependencies, to an upper limit of the margin at a stated coverage. A justified deterministic limit may stand in its place. A material line with neither keeps the verification open.
6. **Rule.** The highest upper limit over the credible scenarios is at or below −26 %. At the concept baseline the central value, the limit and the gap are recorded, and nothing is gated.

A scenario stops being credible when the evidence of its line changes class, on a record the authority approves. The evidence of level 6 that ruling R1 asks of the turbogenerator and of the propeller is that evidence, when it quantifies efficiency and mass with their uncertainty.

### First budget, on the working reference

| Scenario | Central margin | Five lines of class C, index in quadrature | Central plus index |
|---|---:|---:|---:|
| The four gains of 2037 granted | −27.2 % | 6.3 points | −20.9 % |
| The four gains withdrawn | +2.1 % | 9.3 points | +11.4 % |

| Line | Class | In the estimate | Stress | Effect, gains granted | KNOT |
|---|---|---|---|---:|---|
| Turbogenerator efficiency | D | 0.389 | 0.35, the value of today | +8.9 points | `GEN` |
| Drag, basket of 2037 | D | −9 % | none | +7.9 points | `AER` |
| Mass of the propulsion system | D | 1.45 times a conventional one | 2.27 times | +4.4 points | `GEN`, `PRP` |
| Empty mass, basket of 2037 | D | −9 % | none | +3.6 points | `MAS` |
| Propeller efficiency at Mach 0.61 | C | 0.85 | 0.80 | +5.0 points | `PRP` |
| Drag of a propeller aircraft | C | The statistic of turboprops in service | A quarter more of the excess over the jet | +2.8 points | `AER` |
| Efficiency of the electrical chain | C | 0.90 | 0.88 | +1.8 points | `PRP` |
| Brace: relief on the wing mass | C | −23 % | none | +1.7 points | `WNG` |
| Wide fuselage: its mass | C | That of the formula | +15 % | +1.0 points | `FUS`, `MAS` |

- **The index is an arithmetic indicator.** The stresses of the lines of class C are not standard uncertainties, and three have no source read: the propeller, the drag of a propeller aircraft and the electrical chain.
- **Today the scenario with no gain granted governs:** +2.1 %, 28 points from the objective. One gain granted alone leaves −9.3 % (turbogenerator), −8.1 % (drag), −4.7 % (propulsion mass) or −3.7 % (empty mass).
- **With every gain granted the lines of class C still fail the rule:** −20.9 %.
- **All nine stresses together give +21.6 %,** the worst of the 512 combinations. The fuel of the requirement mission still fits the wing there: 8,793 kg against 9,642 kg.
- **Where it leads.** With tolerances chosen as an example (turbogenerator ±2 %, drag ±3 %, empty mass ±3 %, propulsion mass ±10 %, electrical chain −1 point, propeller −1.5 points) the index is 3.6 points. The rule then asks a central margin of −29.6 % or better: about two and a half points more than the reference has with every gain granted.

*Note of 2026-11-26: the research on the lines of the turbogenerator and of the mass of the propulsion system has returned ([record](KNOT-EWTW-GEN-001_turbogenerator-efficiency-and-altitude_2026-11-26.md)). It proposes no change of class: both lines stay in class D, and no scenario changes. It finds that the two values of the first line run from the fuel to the terminals of the generator; that no engine of 2 to 6 MW in service has a measured cruise efficiency on record; that the value for 2037 moves with the size of the unit in the one family of models read; and that the 1.45 of the third line divides a propulsion system of 2030 by an engine of today, where the same table gives 2.02 against a conventional engine of the same year. At 30,000 ft and 350 kt two published tables put the 5.6 MW of the cruise at 12.7 to 12.8 MW of take-off rating at sea level.*

### Open for the authority

- The coverage of the upper limit. The second reader proposes 90 %, one-sided, as a choice of the programme.
- Who declares a scenario no longer credible, and on what record.
- The list of lines, and the class and the stress of each.
- Whether the brace and folding tips enter as scenarios before the wing is chosen.

## Limits

- First order, as the screening: the same limits apply. The propulsion system is not sized, and its mass does not follow the altitude.
- The technology sets are not forecasts for this aircraft. If the drag basket includes a higher aspect ratio, a wing of aspect ratio 17 counts it twice.
- The second reader used the same tool. The agreement of the two shows the arithmetic, not the method.

## To reproduce

From the repository root, with PyYAML:

```python
from copy import deepcopy
from pathlib import Path
import sys, yaml
sys.path.insert(0, "tools")
import configuration_screen as cfg, mission_closure as mc

EV = Path("01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/"
          "01-02-01-01-01-02_KNOT_Knowledge-Node-Register/000_General/evidence")
load = lambda p: yaml.safe_load((EV / p).read_text(encoding="utf-8"))["analysis"]
CONFIG, MISSIONS, CRUISE = (load("CFG-EWTW-AER-001/configuration.yaml"), load("MSN-EWTW-NRG-001/missions.yaml"),
                            load("CRP-EWTW-CRZ-001/cruise-points.yaml"))

def solve(tech_key, section="F5", span=40.0, aspect=17, altitude=31000, speed=360, braced=True,
          mechanical=False, tech=None, drag=None, mass=None, mass_factor=None):
    """One aircraft of fixed span and aspect ratio; the wing loading is iterated until the area is span squared over aspect ratio."""
    a = deepcopy(CONFIG)
    for k, v in (drag or {}).items(): a["drag"][k]["value"] = v
    for k, v in (mass or {}).items(): a["mass"][k]["value"] = v
    ref = cfg.reference(a, MISSIONS, CRUISE["co2_metric"])
    sec = deepcopy(next(s for s in a["sections"] if s["key"] == section))
    if mass_factor: sec["mass_factor"]["value"] = mass_factor
    geom = cfg.section_geometry(cfg.values(a["cabin"]), sec, MISSIONS["payload"]["passengers"])
    point = deepcopy(next(p for p in CRUISE["points"] if p["key"] == "P2"))
    point["altitude_ft"]["value"], point["speed"]["value"] = altitude, speed
    wing = deepcopy(next(w for w in a["wings"] if w["key"] == "WC"))
    wing["aspect_ratio"]["value"], wing["braced"] = aspect, braced
    t = deepcopy(next(x for x in a["technology"] if x["key"] == tech_key))
    for k, v in (tech or {}).items(): t[k]["value"] = v
    for _ in range(200):
        case = cfg.evaluate(a, MISSIONS, mc.Model(MISSIONS, "nominal"), CRUISE["co2_metric"], ref, geom, wing, point, t,
                            mechanical=mechanical)
        if abs(case["area"] - span * span / aspect) < 1e-6: return case
        wing["loading_kg_m2"]["value"] = case["takeoff"] / (span * span / aspect)

for key in ("T0", "T1", "T2"):                                             # the proposal
    c = solve(key); print(key, round(100 * c["margin"], 1), round(c["scoring"]), round(c["loaded"]), round(c["holds"]))
print(round(100 * solve("T1", span=35.9)["margin"], 1))                    # inside code letter C: -23.0
print(round(100 * solve("T1", tech={"turbogenerator_efficiency": 0.35})["margin"], 1))   # one gain withdrawn: -18.3
print(round(100 * solve("T1", tech={"propulsor_factor": 0.80 / 0.85})["margin"], 1))     # propeller at 0.80: -22.2
```

Other lines change `drag={"propeller_drag_share": 1.25}`, `mass={"braced_factor": 1.0}`, `mass_factor=1.15`, `tech={"electric_chain_efficiency": 0.88}`, `altitude`, `speed`, `section` or `mechanical=True`.
