# CFG-EWTW-AER-001 — Screening of the configurations: sections, wings and cruise points

**Version:** 0.1.0 · **Date:** 2026-11-18 · **Status:** first issue, proposed
**For:** `KNOT-EWTW-AER-001`, `KNU-EWTW-AER-001-02` Polar of the eWTW in the screening. Its table of sections serves `KNU-EWTW-FUS-001-02`, its wings `KNU-EWTW-WNG-001-02` and its masses `KNU-EWTW-MAS-001-02`
**Input:** [`configuration.yaml`](configuration.yaml), the mission screening [`MSN-EWTW-NRG-001`](../MSN-EWTW-NRG-001/README.md) and the screening of the cruise points [`CRP-EWTW-CRZ-001`](../CRP-EWTW-CRZ-001/README.md), which are read and not changed
**Checked by:** [`tools/configuration_screen.py`](../../../../../../../../../tools/configuration_screen.py)
**Produced by:** Claude, 2026-11-18. The same hand chose the method, wrote the tool and checked it: no second reader has checked this screening

Steps 2 and 3 of the [path to the concept baseline](../../../../README.md): the dimensions of the fuselage for each section, a drag polar of first order, an empty mass by option, and one screening over every combination. Four sections, three wings and four cruise points, at three sets of technology: 144 aircraft. Each carries 100 passengers and is sized on the requirement mission of 2,000 km.

For each aircraft the screening gives two measures. The fuel on the scoring mission is criterion `T2` of `KNOT-EWTW-CRZ-001`. The margin of the carbon dioxide metric to the new-type level is criterion `M5`, against the objective the authority set on 2026-11-18: 26 % below that level, and beyond ([record of the objective](../KNOT-EWTW-CRZ-001_objective-and-premises_2026-11-18.md)).

This is a screening of first order. It recommends no option and states no conformity with any rule.

---

## What it shows

1. **At nominal values no aircraft is below the new-type level.** With the nominal chain of the mission screening and the airframe technology of the reference type, the margins lie between +4.9 % and +18.8 %. The aircraft weigh 48 to 54 t at take-off and 31 to 36 t empty. The propulsion system, at 2.27 times a conventional one, is 10.1 to 11.3 t of that.
2. **With the baskets of the ICAO experts for 2037, the best aircraft is 18.8 % below the level. None meets the objective.** The baskets take 9 % off the drag and 9 % off the empty mass, and give 10 % of fuel to propulsion. The margins lie between −8.3 % and −18.8 %, and the aircraft weigh 37 to 40 t at take-off.
3. **With the favourable chain and a composite airframe, two aircraft of 36 meet the objective, by less than half a point.** Both carry the braced wing at the jet point: −26.4 % and −26.1 %.
4. **The electrical chain costs about ten points of margin.** The tool sizes each aircraft a second time with a mechanical drive: the shaft of the same thermal machine, a gearbox, the same propulsor, and a propulsion system of conventional mass. With the baskets of 2037, at the floor of speed, the braced wing on the reference cabin then stands at −26.4 %, where the electrical chain leaves it at −16.6 %. The comparison charges the electrical chain its losses and its mass, and credits it with a lighter wing and nothing else: what propulsors along the span may give back is not in it (limits).
5. **The certified metric does not see the cruise speed. The fuel does.** The applicant selects the altitude and the speed of the metric, so the screening takes it at the best lift-to-drag ratio of each aircraft. The three propeller points then have the same margin within one point. On the scoring mission, a cruise at 275 kt burns 9 to 10 % less than a cruise at 360 kt and 25,000 ft; and with the same 360 kt flown at 31,000 ft, the least fuel of the screening falls by 7 %.
6. **The jet point burns about what the propeller points burn.** Its fuel is within 1 % of that of the point at the floor. A fan at 0.76 against a propeller at 0.85 is offset by the drag: the propeller points carry the drag level of a turboprop in service, 26 % more zero-lift drag than the method gives when it is set on the jet. This replaces item 2 of the [screening of the cruise points](../CRP-EWTW-CRZ-001/README.md), which gave every point one lift-to-drag ratio. If a propeller aircraft of this kind were as clean as the jet, the least fuel with the baskets of 2037 would be 17 % lower and the best margin −29.1 %.
7. **The section moves the fuel by about two per cent.** Five abreast burns 2 % less than the reference cabin, six abreast 1 % less. That is inside the error of the fuselage formula: with the wide fuselages 15 % heavier, the two figures become less than 1 % either way. A cabin of five abreast in the width of six, for a wide aisle or wider seats, burns 4 % more than the reference cabin. The metric counts floor area and not seats: six abreast loses three points of margin to the reference cabin at about the same fuel.
8. **For the wing, aspect ratio pays and a smaller area does not.** The wing of option B burns 2.4 to 3.4 % less than that of option A, and the braced wing 4.0 to 5.9 % less. A larger wing improves the margin and costs fuel at the floor of speed: with the baskets of 2037, every wing at 500 kg/m² gives −24.5 % for 3 % more fuel, and at 380 kg/m² −29.2 % for 12 % more. The wings of options B and C have little or no room for the fuel of the requirement mission: it is 0.85 to 1.15 times what they hold, by a rule of similarity, against 0.67 to 0.82 for the wing of option A.
9. **The levers add up.** A braced wing of aspect ratio 20 at 500 kg/m², with the point of the floor flown at 31,000 ft, gives a best margin of −28.0 % with the baskets of 2037, and a least fuel 9 % below that of the screening as it stands. The span of such a wing is about 40 m, beyond code letter C.
10. **Four assumptions move the result more than any choice of section.** The drag level of a propeller aircraft: ten points of margin between a turboprop in service and a jet. The lift-to-drag ratio of the jet reference: −16.6 % to −28.3 % across the range reported for regional jets. The friction drag due to lift: five points. The mass of the propulsion system: 7 to 9 % of fuel between 1.45 and 2.27 times a conventional one.

## What it means for the KNOTs

These are inputs. None is a ruling, and no criterion of `KNOT-EWTW-CRZ-001` is approved.

- **`KNOT-EWTW-CRZ-001`, criteria `M5` and `T2`.** The two can pull apart. A wing sized to meet the metric is larger than the wing of least fuel at the floor of speed (item 8), and the metric is the same at 275 kt and at 360 kt (item 5). The fuel on the scoring mission is the measure that follows what the aircraft burns in service. The floor of speed, criterion `M4`, costs 9 to 10 % of that fuel at 25,000 ft; the cruise altitude is a second lever, which the candidate points do not explore.
- **`KNOT-EWTW-PRP-001` and `KNOT-EWTW-GEN-001`.** The objective is won or lost in the propulsion chain. Ten points of margin separate the electrical chain from a mechanical drive on the same airframe (item 4). The research of these KNOTs has to show what propulsors along the span give back, in figures the screening can use, or how much of the power has to go through the electrical chain.
- **`KNOT-EWTW-AER-001`.** The polar rests on two published figures, one for a jet and one for a turboprop, and the second is a statistic. A measured polar of a propeller aircraft of the class, or its fuel flow in cruise, is the figure the screening most needs.
- **`KNOT-EWTW-FUS-001`.** The wide tube is neither helped nor hurt by the fuel, within what the method can tell. The choice of section can be made on comfort and on the room it gives to an energy-carrier bay: the gross section is 7.9 m² for the reference cabin, 9.9 m² for five abreast and 11.9 m² for six. Comfort bought with width costs about 4 % of fuel and three points of margin. Option C, the flattened section, is not screened.
- **`KNOT-EWTW-WNG-001`.** The three options do not separate the two choices the screening shows to matter, the span and the brace. At the take-off masses of the second and third technology sets, the braced wing of aspect ratio 17 stays within code letter C; it passes 36 m at the masses of the first set only.
- **`KNOT-EWTW-FUL-001`.** The smaller wings have little or no room for the fuel (item 8). With the wings of options B and C, part of it may have to be carried elsewhere, or the wing grows.
- **`KNOT-EWTW-MAS-001`.** The empty mass by option is in the tables below. The share that rests on technology not in service is the difference between the three sets: 31 to 36 t, 22 to 25 t and 22 to 24 t.

## Limits

- **One hand.** The method, the tool and its tests were written by the same reviewer. Nothing here has been checked by a second reader.
- **The jet is set on a ratio the mission screening assumes.** The lift-to-drag ratio of 15 for the Embraer 190 is the nominal value of the mission screening, chosen so that its product fits the published sectors of the type. No manufacturer's figure supports it; the range reported for regional jets is 14 to 17. One check holds: with the metric taken at the best ratio, the method places the Embraer 190 at +8.5 % from the new-type level, and the figures of the ICAO experts and of Embraer together place it at +7.6 %.
- **The propeller points are set on a statistic.** The best ratio of 15.74 for the ATR 72 comes from a statistic of turboprops, applied in a published redesign that meets the masses of the type. It is not a measured polar. The other check on record is weaker: the sheet of the Dash 8-400 implies a product of propulsor efficiency and lift-to-drag of 9.1 if its engines give their cruise rating at 25,000 ft, and the aircraft of the screening have 11.7 to 12.7 there.
- **Propulsors along the span are neither credited nor charged.** No gain is taken for propellers at the wingtips, for lift blown at low speed beyond the wing loading assumed, or for ingestion of the boundary layer: the [records](../KNOT-EWTW-WNG-001_wings-in-service-and-propellers_2026-11-18.md) hold a wind-tunnel test at small scale and a flight campaign that reports no aerodynamic gain. No drag is added for many nacelles in a slipstream beyond the level of the turboprop.
- **The span efficiency falls with the aspect ratio.** The method adds to the induced drag a term in proportion to the zero-lift drag. It gives a span efficiency of 0.79 to the Embraer 190 and of 0.54 to 0.66 to the braced wings. With half that term the best margin with the baskets of 2037 is −24.2 %.
- **The wing formula is used beyond the wings it was fitted on.** It has no term for flutter or stiffness at aspect ratios of 14 to 20, and the relief of a brace is a handbook figure. With no relief the best margin moves by half a point to a point and a half.
- **The fuselage formula favours the wide sections.** It has no term for the pressure load of a wider shell or for a wider floor, and the [one study read](../KNOT-EWTW-FUS-001_wide-sections-and-hydrogen-tanks_2026-11-18.md) finds a wider regional fuselage heavier (statement 13).
- **Two simplifications work against the propeller points.** The design dive speed, and with it the fuselage mass, is the same at every cruise point. The terminal distance of every mission is that fitted on the jet reference.
- **The propulsion system is not sized.** Its mass is that of the reference in proportion to the take-off mass, times one ratio for each technology set, from one study. The [screening of the cruise points](../CRP-EWTW-CRZ-001/README.md) shows that the cruise sizes the machines at least as much as the take-off; a faster or a higher cruise would make them heavier, and that is not here.
- **The technology sets are not forecasts for this aircraft.** The baskets of the experts are stated for the single-aisle and twin-aisle classes, over their reference of 2017. Here they are laid on a jet airframe set on a type of 2005 and on a propeller aircraft set on a type designed in the 1980s. If the drag basket includes a higher aspect ratio, the wings of options B and C count it twice.
- **The metric is of first order.** Every reference mass is taken at the best ratio, without a check of ceiling or of minimum speed. The take-off mass of the requirement mission stands for the maximum take-off mass. The floor is the outer width times the cabin length.
- **Field performance is not checked.** A loading of 620 kg/m² is above the wings in service, and nothing here shows that the aircraft takes off and lands on the runways of the class.
- **The rest of the aircraft is that of the reference.** Systems, furnishings and operating items are held at 9.9 t for every aircraft. Tails are sized by volume coefficients, with no credit for thrust that can be steered.
- **The design range is the requirement mission.** The reference type is offered with 4,445 km. Part of the difference in take-off mass between it and the aircraft of the screening is range, not technology.

## The screening

Generated by the tool from the three inputs. Do not edit between the markers.

<!-- configuration:begin -->
CFG-EWTW-AER-001 0.1.0 for KNOT-EWTW-AER-001: 4 sections, 3 wings and 4 cruise points at 3 technology sets, on the missions of MSN-EWTW-NRG-001 0.3.0; 106 figures, 52 of them assumptions; rule failures: none

### Sections

| Section | Option | Abreast | Rows | Seats | Cabin width, m | Outer width and height, m | Gross section, m² | Cabin length, m | Fuselage length, m | Slenderness | Wetted area, m² | Floor for the metric, m² |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `F4` Four abreast, the cabin of the reference | A | 4 | 25 | 100 | 2.74 | 3.01 × 3.35 | 7.9 | 26.3 | 36.6 | 11.5 | 325 | 79.2 |
| `F5` Five abreast | B | 5 | 20 | 100 | 3.28 | 3.55 × 3.55 | 9.9 | 21.2 | 32.4 | 9.1 | 310 | 75.4 |
| `F5W` Five abreast in the width of six | B | 5 | 20 | 100 | 3.63 | 3.90 × 3.90 | 11.9 | 20.8 | 32.7 | 8.4 | 339 | 81.0 |
| `F6` Six abreast | B | 6 | 17 | 102 | 3.63 | 3.90 × 3.90 | 11.9 | 18.3 | 30.3 | 7.8 | 309 | 71.4 |

Not screened: option C of `KNOT-EWTW-FUS-001`. A flattened section that carries lift has no dimension and no mass method on record. Research record of the wide sections, 2026-11-18, findings 15 and 16.

### The method on two types in service

- **Geometry.** The Embraer 190 is 36.24 m long with a wing of 92.5 m². It has a slenderness of 11.4 and, by the method, a wetted area 6.29 times its wing area.
- **Drag of the jet.** The mission screening takes a lift-to-drag ratio of 15 at nominal values, so that its product of efficiency and lift-to-drag, 4.02, is near the 4.08 it fits on the published sectors of the type. This screening takes that ratio as the one of the type in its cruise. The method gives it with an equivalent skin-friction coefficient of 0.00334, inside the 0.003 to 0.004 of the source, and a span efficiency of 0.79. The best ratio of the type at that Mach number is then 15.9.
- **Drag of a propeller aircraft.** With that coefficient the method gives the ATR 72 a wetted area 6.34 times its wing area and a best lift-to-drag ratio of 18.2. The source gives it 15.74. The method meets that figure with a zero-lift drag 1.26 times its own, and the propeller points of the screening carry 100 % of that excess.
- **Structure.** The method gives the Embraer 190 a wing of 4,562 kg, a fuselage of 5,578 kg, tails of 914 kg and a landing gear of 2,163 kg: 13,217 kg, 26.3 % of its take-off mass of 50,300 kg. The sample breakdown on record gives 27.23 %.
- **The rest.** Its power plant is taken as 9.26 % of its take-off mass, 4,658 kg. What is left of its operating mass of 27,753 kg, 9,878 kg of systems, furnishings and operating items, is held for every aircraft of the screening.
- **Metric.** The applicant selects the altitude and the speed of the carbon dioxide metric, so the screening takes it at the best lift-to-drag ratio of each aircraft. With the fitted product raised in that proportion, a floor of 78.0 m² and that take-off mass, the metric of the Embraer 190 stands +8.5 % from the new-type level; at its cruise it would stand +14.7 %. Its successor, the Embraer E190-E2, stands 11 % below that level by the experts of ICAO and burns 17.3 % less by its manufacturer: the two together place the Embraer 190 at +7.6 %.
- **Fuel in the wing.** The fuel a wing holds is taken in proportion to the square of its area over its span, from the 12,971 kg of the Embraer 190. The rule gives the wing of the Embraer E190-E2 13,698 kg; it holds 13,500 kg.

### Polar by option: Nominal chain, airframe technology of the reference

Wetted areas, drag and span efficiency at `P2`, the slowest point at or above the floor of speed. The fuselage is weighted by its form factor against that of the Embraer 190. A count is one ten-thousandth of drag coefficient. The best ratio is that of the propeller points.

| Section | Wing | Wing area, m² | Wetted, m²: fuselage · wing · tails · brace · nacelles | Over the wing area | Zero-lift drag, counts | Drag due to lift, counts | Span efficiency | Best lift-to-drag | Lift-to-drag at `P1` | Lift-to-drag at `P2` | Lift-to-drag at `P3` | Lift-to-drag at `P4` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `F4` | `WA` | 94.5 | 324 · 166 · 70 · 0 · 34 | 6.29 | 264 | 119 | 0.71 | 15.6 | 15.5 | 14.5 | 14.5 | 16.3 |
| `F4` | `WB` | 85.1 | 324 · 151 · 60 · 0 · 32 | 6.67 | 280 | 129 | 0.66 | 16.1 | 16.0 | 15.0 | 15.1 | 17.0 |
| `F4` | `WC` | 82.9 | 324 · 149 · 58 · 22 · 33 | 7.08 | 297 | 116 | 0.61 | 16.5 | 16.2 | 14.8 | 14.9 | 16.9 |
| `F5` | `WA` | 91.7 | 320 · 156 · 75 · 0 · 33 | 6.38 | 268 | 120 | 0.71 | 15.4 | 15.3 | 14.3 | 14.4 | 16.1 |
| `F5` | `WB` | 82.5 | 320 · 142 · 65 · 0 · 32 | 6.76 | 284 | 130 | 0.66 | 15.9 | 15.8 | 14.8 | 14.9 | 16.8 |
| `F5` | `WC` | 80.3 | 320 · 140 · 63 · 21 · 33 | 7.18 | 301 | 117 | 0.60 | 16.3 | 16.1 | 14.7 | 14.7 | 16.7 |
| `F5W` | `WA` | 94.0 | 356 · 158 · 78 · 0 · 35 | 6.67 | 280 | 122 | 0.70 | 15.0 | 14.8 | 13.8 | 13.9 | 15.6 |
| `F5W` | `WB` | 84.6 | 356 · 143 · 67 · 0 · 34 | 7.09 | 298 | 133 | 0.64 | 15.4 | 15.3 | 14.3 | 14.3 | 16.2 |
| `F5W` | `WC` | 82.4 | 356 · 142 · 65 · 21 · 35 | 7.51 | 316 | 120 | 0.59 | 15.8 | 15.5 | 14.1 | 14.2 | 16.1 |
| `F6` | `WA` | 91.0 | 332 · 152 · 80 · 0 · 34 | 6.57 | 276 | 122 | 0.70 | 15.1 | 15.0 | 13.9 | 14.0 | 15.7 |
| `F6` | `WB` | 81.8 | 332 · 138 · 68 · 0 · 32 | 6.97 | 293 | 132 | 0.65 | 15.6 | 15.5 | 14.4 | 14.5 | 16.4 |
| `F6` | `WC` | 79.7 | 332 · 137 · 67 · 21 · 33 | 7.39 | 310 | 119 | 0.59 | 16.0 | 15.7 | 14.3 | 14.4 | 16.3 |

Check on a published point, `P2`: the sheet read for it implies a product of propulsor efficiency and lift-to-drag of 9.1, if its engines give their cruise rating there. The aircraft of this table have 11.7 to 12.7 at that point.

### Empty mass by option: Nominal chain, airframe technology of the reference

Masses in kg at `P2`.

| Section | Wing | Wing | Fuselage | Tails | Landing gear | Propulsion system | Systems, furnishings and operating items | Empty mass |
|---|---|---|---|---|---|---|---|---|
| `F4` | `WA` | 5,040 | 5,689 | 925 | 2,276 | 11,126 | 9,878 | 34,934 |
| `F4` | `WB` | 5,350 | 5,689 | 794 | 2,269 | 11,091 | 9,878 | 35,071 |
| `F4` | `WC` | 4,490 | 5,689 | 774 | 2,210 | 10,806 | 9,878 | 33,847 |
| `F5` | `WA` | 4,831 | 4,794 | 999 | 2,207 | 10,789 | 9,878 | 33,499 |
| `F5` | `WB` | 5,123 | 4,794 | 856 | 2,198 | 10,746 | 9,878 | 33,595 |
| `F5` | `WC` | 4,300 | 4,794 | 834 | 2,142 | 10,471 | 9,878 | 32,419 |
| `F5W` | `WA` | 4,976 | 5,117 | 1,028 | 2,264 | 11,069 | 9,878 | 34,332 |
| `F5W` | `WB` | 5,278 | 5,117 | 881 | 2,256 | 11,029 | 9,878 | 34,440 |
| `F5W` | `WC` | 4,429 | 5,117 | 859 | 2,198 | 10,744 | 9,878 | 33,224 |
| `F6` | `WA` | 4,772 | 4,401 | 1,058 | 2,192 | 10,714 | 9,878 | 33,016 |
| `F6` | `WB` | 5,057 | 4,401 | 906 | 2,182 | 10,666 | 9,878 | 33,091 |
| `F6` | `WC` | 4,244 | 4,401 | 883 | 2,126 | 10,392 | 9,878 | 31,925 |

### Screening: Nominal chain, airframe technology of the reference

Turbogenerator 0.350, electrical chain 0.90, propulsor of the point times 1; drag times 1; empty mass times 1, wing and tail times 1, fuselage times 1; propulsion system at 2.27 times a conventional one. Wing, masses, lift-to-drag ratio and fuel are those of `P2`. The last columns are margins of the carbon dioxide metric to the new-type level; a margin in bold meets the objective.

| Section | Wing | Wing area, m² | Span, m | Letter | Lift-to-drag | Empty, t | Take-off, t | Fuel loaded over what the wing holds | Fuel, scoring mission, kg | `P1`, below the floor | `P2` | `P3` | `P4` | `P2` with a mechanical drive |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `F4` | `WA` | 94.5 | 33.0 | C | 14.5 | 34.9 | 52.9 | 0.72 | 5,627 | +14.2 % | +14.8 % | +14.7 % | +14.5 % | -2.8 % |
| `F4` | `WB` | 85.1 | 34.5 | C | 15.0 | 35.1 | 52.8 | 0.90 | 5,432 | +10.5 % | +11.0 % | +10.9 % | +9.9 % | -5.2 % |
| `F4` | `WC` | 82.9 | 37.5 | D | 14.8 | 33.8 | 51.4 | 1.01 | 5,343 | +6.3 % | +6.9 % | +6.8 % | +4.9 % | -8.6 % |
| `F5` | `WA` | 91.7 | 32.5 | C | 14.3 | 33.5 | 51.3 | 0.74 | 5,515 | +14.7 % | +15.3 % | +15.3 % | +15.0 % | -2.4 % |
| `F5` | `WB` | 82.5 | 34.0 | C | 14.8 | 33.6 | 51.1 | 0.92 | 5,321 | +11.0 % | +11.5 % | +11.5 % | +10.4 % | -4.8 % |
| `F5` | `WC` | 80.3 | 37.0 | D | 14.7 | 32.4 | 49.8 | 1.04 | 5,231 | +6.7 % | +7.3 % | +7.3 % | +5.3 % | -8.3 % |
| `F5W` | `WA` | 94.0 | 32.9 | C | 13.8 | 34.3 | 52.7 | 0.75 | 5,838 | +17.9 % | +18.5 % | +18.5 % | +17.9 % | +0.7 % |
| `F5W` | `WB` | 84.6 | 34.4 | C | 14.3 | 34.4 | 52.5 | 0.94 | 5,648 | +14.4 % | +14.9 % | +14.8 % | +13.5 % | -1.5 % |
| `F5W` | `WC` | 82.4 | 37.4 | D | 14.1 | 33.2 | 51.1 | 1.06 | 5,552 | +9.9 % | +10.5 % | +10.5 % | +8.2 % | -5.1 % |
| `F6` | `WA` | 91.0 | 32.4 | C | 13.9 | 33.0 | 51.0 | 0.76 | 5,593 | +18.1 % | +18.8 % | +18.8 % | +18.3 % | +0.6 % |
| `F6` | `WB` | 81.8 | 33.9 | C | 14.4 | 33.1 | 50.7 | 0.95 | 5,400 | +14.5 % | +15.0 % | +14.9 % | +13.6 % | -1.7 % |
| `F6` | `WC` | 79.7 | 36.8 | D | 14.3 | 31.9 | 49.4 | 1.07 | 5,307 | +9.9 % | +10.6 % | +10.5 % | +8.4 % | -5.3 % |

### Screening: Baskets of the ICAO experts for 2037

Turbogenerator 0.389, electrical chain 0.90, propulsor of the point times 1; drag times 0.91; empty mass times 0.91, wing and tail times 1, fuselage times 1; propulsion system at 1.45 times a conventional one. Wing, masses, lift-to-drag ratio and fuel are those of `P2`. The last columns are margins of the carbon dioxide metric to the new-type level; a margin in bold meets the objective.

| Section | Wing | Wing area, m² | Span, m | Letter | Lift-to-drag | Empty, t | Take-off, t | Fuel loaded over what the wing holds | Fuel, scoring mission, kg | `P1`, below the floor | `P2` | `P3` | `P4` | `P2` with a mechanical drive |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `F4` | `WA` | 70.9 | 28.6 | C | 14.0 | 24.3 | 39.7 | 0.77 | 3,944 | -11.9 % | -11.6 % | -11.6 % | -12.6 % | -22.2 % |
| `F4` | `WB` | 64.0 | 29.9 | C | 14.4 | 24.4 | 39.7 | 0.97 | 3,844 | -13.8 % | -13.6 % | -13.6 % | -15.2 % | -23.7 % |
| `F4` | `WC` | 62.9 | 32.7 | C | 14.3 | 23.8 | 39.0 | 1.09 | 3,804 | -16.8 % | -16.6 % | -16.6 % | -18.8 % | **-26.4 %** |
| `F5` | `WA` | 68.8 | 28.1 | C | 13.9 | 23.2 | 38.5 | 0.79 | 3,861 | -11.5 % | -11.2 % | -11.2 % | -12.2 % | -21.8 % |
| `F5` | `WB` | 62.0 | 29.5 | C | 14.3 | 23.3 | 38.4 | 1.00 | 3,762 | -13.4 % | -13.2 % | -13.2 % | -14.9 % | -23.4 % |
| `F5` | `WC` | 60.9 | 32.2 | C | 14.2 | 22.7 | 37.8 | 1.12 | 3,722 | -16.5 % | -16.3 % | -16.3 % | -18.5 % | **-26.1 %** |
| `F5W` | `WA` | 70.4 | 28.5 | C | 13.3 | 23.7 | 39.4 | 0.82 | 4,108 | -8.6 % | -8.3 % | -8.3 % | -9.5 % | -19.2 % |
| `F5W` | `WB` | 63.5 | 29.8 | C | 13.6 | 23.8 | 39.4 | 1.03 | 4,013 | -10.3 % | -10.1 % | -10.1 % | -12.0 % | -20.5 % |
| `F5W` | `WC` | 62.4 | 32.6 | C | 13.5 | 23.2 | 38.7 | 1.15 | 3,969 | -13.6 % | -13.3 % | -13.3 % | -15.8 % | -23.4 % |
| `F6` | `WA` | 68.2 | 28.0 | C | 13.5 | 22.8 | 38.2 | 0.82 | 3,920 | -8.7 % | -8.4 % | -8.4 % | -9.5 % | -19.3 % |
| `F6` | `WB` | 61.5 | 29.3 | C | 13.9 | 22.9 | 38.1 | 1.03 | 3,824 | -10.5 % | -10.3 % | -10.3 % | -12.2 % | -20.8 % |
| `F6` | `WC` | 60.4 | 32.0 | C | 13.8 | 22.3 | 37.5 | 1.15 | 3,781 | -13.8 % | -13.6 % | -13.6 % | -16.0 % | -23.7 % |

### Screening: Favourable chain and composite airframe

Turbogenerator 0.400, electrical chain 0.93, propulsor of the point times 1.035; drag times 0.91; empty mass times 0.97, wing and tail times 0.765, fuselage times 0.855; propulsion system at 1.45 times a conventional one. Wing, masses, lift-to-drag ratio and fuel are those of `P2`. The last columns are margins of the carbon dioxide metric to the new-type level; a margin in bold meets the objective.

| Section | Wing | Wing area, m² | Span, m | Letter | Lift-to-drag | Empty, t | Take-off, t | Fuel loaded over what the wing holds | Fuel, scoring mission, kg | `P1`, below the floor | `P2` | `P3` | `P4` | `P2` with a mechanical drive |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `F4` | `WA` | 69.3 | 28.2 | C | 13.9 | 23.9 | 38.8 | 0.73 | 3,572 | -20.1 % | -19.9 % | -19.9 % | -20.9 % | **-27.1 %** |
| `F4` | `WB` | 62.5 | 29.6 | C | 14.3 | 24.0 | 38.7 | 0.91 | 3,483 | -21.8 % | -21.7 % | -21.7 % | -23.2 % | **-28.5 %** |
| `F4` | `WC` | 61.6 | 32.4 | C | 14.2 | 23.5 | 38.2 | 1.02 | 3,454 | -24.6 % | -24.4 % | -24.4 % | **-26.4 %** | **-30.9 %** |
| `F5` | `WA` | 67.3 | 27.8 | C | 13.7 | 22.9 | 37.7 | 0.74 | 3,502 | -19.8 % | -19.5 % | -19.5 % | -20.5 % | **-26.7 %** |
| `F5` | `WB` | 60.7 | 29.2 | C | 14.1 | 23.0 | 37.6 | 0.93 | 3,414 | -21.4 % | -21.3 % | -21.3 % | -22.9 % | **-28.1 %** |
| `F5` | `WC` | 59.9 | 31.9 | C | 14.0 | 22.5 | 37.1 | 1.04 | 3,384 | -24.3 % | -24.1 % | -24.1 % | **-26.1 %** | **-30.7 %** |
| `F5W` | `WA` | 68.8 | 28.1 | C | 13.1 | 23.4 | 38.5 | 0.77 | 3,725 | -17.1 % | -16.9 % | -16.9 % | -18.1 % | -24.2 % |
| `F5W` | `WB` | 62.0 | 29.5 | C | 13.5 | 23.5 | 38.5 | 0.96 | 3,641 | -18.6 % | -18.5 % | -18.5 % | -20.3 % | -25.5 % |
| `F5W` | `WC` | 61.2 | 32.3 | C | 13.4 | 23.0 | 37.9 | 1.07 | 3,608 | -21.5 % | -21.4 % | -21.4 % | -23.7 % | **-28.1 %** |
| `F6` | `WA` | 66.8 | 27.7 | C | 13.4 | 22.6 | 37.4 | 0.76 | 3,559 | -17.2 % | -16.9 % | -17.0 % | -18.1 % | -24.3 % |
| `F6` | `WB` | 60.2 | 29.0 | C | 13.7 | 22.6 | 37.3 | 0.96 | 3,473 | -18.8 % | -18.7 % | -18.7 % | -20.4 % | -25.7 % |
| `F6` | `WC` | 59.4 | 31.8 | C | 13.7 | 22.2 | 36.8 | 1.07 | 3,441 | -21.8 % | -21.6 % | -21.6 % | -23.8 % | **-28.4 %** |

### Against the objective

The objective is a margin of -26.0 % to the new-type level, or better. The floor of speed is 360 kt.

| Technology set | Least fuel on the scoring mission, at or above the floor | Its margin | Best margin at or above the floor | Best margin with a mechanical drive | Meet the objective at or above the floor | Meet it below the floor |
|---|---|---|---|---|---|---|
| Nominal chain, airframe technology of the reference | `P3`, `F5`, `WC`: 5,193 kg | +7.3 % | `P4`, `F4`, `WC`: +4.9 % | `P4`, `F4`, `WC`: -10.8 % | 0 of 36 | 0 of 12 |
| Baskets of the ICAO experts for 2037 | `P4`, `F5`, `WC`: 3,676 kg | -18.5 % | `P4`, `F4`, `WC`: -18.8 % | `P4`, `F4`, `WC`: **-28.5 %** | 0 of 36 | 0 of 12 |
| Favourable chain and composite airframe | `P4`, `F5`, `WC`: 3,337 kg | **-26.1 %** | `P4`, `F4`, `WC`: **-26.4 %** | `P4`, `F4`, `WC`: **-32.9 %** | 2 of 36 | 0 of 12 |

### One choice at a time

Fuel on the scoring mission, averaged over the other two choices. A negative figure is less fuel.

| Choice | Nominal chain, airframe technology of the reference | Baskets of the ICAO experts for 2037 | Favourable chain and composite airframe |
|---|---|---|---|
| Section `F5` against `F4` | -2.1 % | -2.2 % | -2.0 % |
| Section `F5W` against `F4` | +3.6 % | +4.1 % | +4.2 % |
| Section `F6` against `F4` | -0.8 % | -0.7 % | -0.5 % |
| Wing `WB` against `WA` | -3.4 % | -2.5 % | -2.4 % |
| Wing `WC` against `WA` | -5.9 % | -4.2 % | -4.0 % |
| Cruise point `P1` against `P2` | -8.8 % | -10.0 % | -10.0 % |
| Cruise point `P3` against `P2` | -0.7 % | -0.7 % | -0.7 % |
| Cruise point `P4` against `P2` | +0.2 % | -0.8 % | -1.0 % |
| Section `F5` against `F4`: fuselage of the wide sections 15 % heavier than the formula gives | -0.2 % | -0.6 % | -0.6 % |
| Section `F5W` against `F4`: fuselage of the wide sections 15 % heavier than the formula gives | +5.7 % | +5.7 % | +5.7 % |
| Section `F6` against `F4`: fuselage of the wide sections 15 % heavier than the formula gives | +1.0 % | +0.7 % | +0.8 % |

### One assumption at a time

The whole screening again with one assumption changed. For each technology set, the least fuel on the scoring mission and the best margin of the aircraft at or above the floor of speed. The two may belong to different aircraft.

| Assumption changed | Skin friction set on the jet | Zero-lift drag of the propeller points over the method | Nominal chain, airframe technology of the reference | Baskets of the ICAO experts for 2037 | Favourable chain and composite airframe |
|---|---|---|---|---|---|
| None: the screening as it stands | 0.00334 | 1.26 | 5,193 kg · +4.9 % | 3,676 kg · -18.8 % | 3,337 kg · **-26.4 %** |
| Jet reference at a lift-to-drag ratio of 14, the low end of the range reported for regional jets | 0.00369 | 1.14 | 5,193 kg · +6.8 % | 3,694 kg · -16.6 % | 3,359 kg · -24.4 % |
| Jet reference at a lift-to-drag ratio of 17, the high end of that range | 0.00277 | 1.52 | 4,478 kg · -7.4 % | 3,165 kg · **-28.3 %** | 2,874 kg · **-35.0 %** |
| Propeller points with half the excess of drag of the turboprop in service | 0.00334 | 1.13 | 4,735 kg · -1.2 % | 3,375 kg · -22.8 % | 3,069 kg · **-30.0 %** |
| Propeller points at the drag level of the jet | 0.00334 | 1.00 | 4,281 kg · -9.3 % | 3,055 kg · **-29.1 %** | 2,778 kg · **-35.7 %** |
| Half the friction drag due to lift | 0.00349 | 1.36 | 5,160 kg · -1.2 % | 3,640 kg · -24.2 % | 3,305 kg · **-31.4 %** |
| Every wing at 500 kg/m2 | 0.00334 | 1.26 | 5,464 kg · -0.1 % | 3,786 kg · -24.5 % | 3,423 kg · **-31.8 %** |
| Every wing at 380 kg/m2, near the loading of the ATR 72-600 | 0.00334 | 1.26 | 6,329 kg · -2.5 % | 4,131 kg · **-29.2 %** | 3,691 kg · **-36.5 %** |
| The point of the floor flown at 31,000 ft in the place of 25,000 ft | 0.00334 | 1.26 | 4,829 kg · +4.9 % | 3,419 kg · -18.8 % | 3,108 kg · **-26.4 %** |
| A brace that takes nothing off the mass of the wing | 0.00334 | 1.26 | 5,289 kg · +6.5 % | 3,733 kg · -18.3 % | 3,381 kg · **-26.1 %** |
| Braced wing at an aspect ratio of 20 | 0.00334 | 1.26 | 5,135 kg · +0.2 % | 3,629 kg · -22.5 % | 3,290 kg · **-29.8 %** |
| Fuselage of the wide sections 15 % heavier than the formula gives | 0.00334 | 1.26 | 5,287 kg · +4.9 % | 3,733 kg · -18.8 % | 3,383 kg · **-26.4 %** |
| Propulsion system at 2.27 times a conventional one in every set | 0.00334 | 1.26 | 5,193 kg · +4.9 % | 3,934 kg · -17.1 % | 3,576 kg · -24.9 % |
| Propulsion system at 1.45 times a conventional one in every set | 0.00334 | 1.26 | 4,767 kg · +1.7 % | 3,676 kg · -18.8 % | 3,337 kg · **-26.4 %** |
| Three of the above together: every wing at 500 kg/m2, the braced wing at an aspect ratio of 20, the point of the floor at 31,000 ft | 0.00334 | 1.26 | 4,871 kg · -4.5 % | 3,361 kg · **-28.0 %** | 3,038 kg · **-35.0 %** |
<!-- configuration:end -->

## How to verify

From the repository root:

```bash
REG="01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
python3 tools/configuration_screen.py "$REG/000_General/evidence/CFG-EWTW-AER-001" "$REG" --check
python3 tools/configuration_screen_test.py
```

The tool first runs the two screenings it reads through their own checks. It fails if a section or a wing names an option that is not open, if an open option is neither screened nor named as not screened, or if the skin friction it sets on the jet leaves the range of its source. Its tests compute again by hand, from the figures of the input, a section, the skin friction of the jet, the drag level of the propeller points, the masses of the reference, its metric, and one whole aircraft: geometry, polar, masses, the closure of the requirement mission, the fuel of the scoring mission and the metric.

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-18 | First issue: four sections, three wings and four cruise points at three technology sets, with fourteen assumptions changed one at a time. 106 figures, 52 of them assumptions |
