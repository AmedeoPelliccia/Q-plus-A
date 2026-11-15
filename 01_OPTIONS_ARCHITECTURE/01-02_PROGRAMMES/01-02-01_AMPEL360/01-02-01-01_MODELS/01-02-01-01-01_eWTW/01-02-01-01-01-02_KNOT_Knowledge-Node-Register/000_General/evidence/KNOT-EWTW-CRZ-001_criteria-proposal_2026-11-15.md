# Criteria and maturity proposed — cruise point

| | |
|---|---|
| KNOT | `KNOT-EWTW-CRZ-001` Cruise point |
| Serves | `KNU-EWTW-CRZ-001-03` Decision criteria and maturity thresholds |
| Proposed by | Claude, 2026-11-15, at the request of the authority of the model |
| Issue | 2, of 2026-11-16. The weights of issue 1 are replaced by an order of precedence, on the decision of the authority that the more ecological option is the north star of the programme (rule 19 of CM-004) |
| Second reading | An assessment relayed by the author on 2026-11-15 found issue 1 consistent with the records and asked for the note on CS 25.841 above 25,000 ft. It does not name its producer |
| State | Proposed. Every criterion is `PROPOSED` in the record of the KNOT. To approve them is an act of the authority |
| Maturity | Three maturity records, on the decision of the authority to keep the threshold of ruling R2 of `KNOT-EWTW-NRG-001`. They are `PROPOSED` too |
| Gate | Rule 5 keeps the KNOT closed to scoring while a criterion or a maturity record is `PROPOSED` |

This record states a proposal and its reasons. It rules nothing, and by it no option is retained or rejected.

---

## What is being chosen

The published texts name the criteria of a cruise point: block time, fuel, noise, integration with faster traffic, propulsive efficiency, the power of the cabin compressors, the insulation margin. No text says which comes first.

On 2026-11-16 the authority said which: this work builds a more ecological alternative. Among the options that meet what is never traded — safety, the certification basis, the requirement mission, the required maturity — the more ecological one prevails over time and cost. That is rule 19 of CM-004, and it holds for every decision anchor.

Issue 1 of this proposal gave weights, and said that with the few criteria the screening can measure, to choose the weights was to choose the point. The order below says the same thing in one line and needs no weights. It is a reasoned decision about what the aircraft is, and it should be approved or refused as such.

## The trade

From the [screening of the cruise points](CRP-EWTW-CRZ-001/README.md) 0.2.0. The slowest point is left out of this table; it is treated under the floor below.

| Measure | `P2` 360 kt at 25,000 ft | `P3` Mach 0.62 at 27,000 ft | `P4` Mach 0.78 at 35,000 ft |
|---|---|---|---|
| Option of the KNOT | A | C | B |
| Time at cruise speed on the scoring mission, 1,100 km | 99 min | 96 min | 79 min |
| Time at cruise speed on the requirement mission, 2,000 km | 180 min | 175 min | 144 min |
| Fuel loaded on the scoring mission | 4,535 kg | 4,535 kg | 5,107 kg |
| Cruise power at the terminals of the generators | 7.0 MW | 7.2 MW | 9.9 MW |
| Gas turbines for the cruise, referred to sea level | 13.9 MW | 15.3 MW | 26.1 MW |
| Ideal work to compress the cabin air | 53 kJ/kg | 59 kJ/kg | 85 kJ/kg |
| Inception voltage left, against sea level | 78 % | 77 % | 70 % |

The jet point buys 17 to 20 minutes on the scoring mission. It asks for 13 % more fuel, 1.7 to 1.9 times the gas turbines, and 1.4 to 1.6 times the work of compression.

## The set

### Not traded

| Id | Criterion | Source |
|---|---|---|
| `M1` | The cabin pressure altitude is not above 8,000 ft at the maximum operating altitude, in normal operation | CS 25.841(a), read on 2026-11-15 |
| `M2` | Above 25,000 ft, the cabin pressure altitude stays at or below 15,000 ft after any reasonably probable failure of the pressurisation system | CS 25.841(a), read on 2026-11-15 |
| `M3` | The requirement mission closes at the cruise point, with the reserves of ruling R2 of `KNOT-EWTW-NRG-001` | Ruling R2 of 2026-11-14 |
| `M4` | The cruise speed is not below 360 kt true airspeed, that of the fastest turboprop of the class in service. It is the floor of service that rule 19 asks for | Proposed here, and kept by the authority on 2026-11-16. It is a requirement of the programme and is in no text |

`M2` applies to the points above 25,000 ft only. The turboprops of the class have their ceiling there ([record of the cruise point](KNOT-EWTW-CRZ-001_cruise-point_2026-11-15.md), statements 2 and 4). What it costs is not on record. Option A at its fast end is at 25,000 ft and is not above it; option C at 27,000 ft is. The choice between A and C has to be made knowing it.

The record of the cruise point gave three limits under 14 CFR 25.841. CS 25.841, read on 2026-11-15, gives the first two. The limits of exposure after a decompression are in the United States text and were not found in CS 25.841 as read.

### Traded, in order

| Order | Id | Criterion | Measure of the screening | Better | Margin |
|---|---|---|---|---|---|
| 1, north star | `T2` | Fuel loaded on the scoring mission | Kilograms | Lower | 5 % |
| 2 | `T1` | Power of the gas turbines for the cruise, referred to sea level | Megawatts, on the take-off mass of the requirement mission | Lower | 5 % |
| 3 | `T3` | Time at cruise speed on the scoring mission | Minutes | Lower | 5 % |
| 4 | `T4` | Inception voltage of partial discharge left at the cruise altitude | Share of the value at sea level | Higher | 5 % |
| 5 | `T5` | Ideal work to compress outside air to the cabin pressure | Kilojoules for each kilogram of air | Lower | 5 % |

A criterion separates two options only when they differ by more than its margin, a share of the best value. Otherwise the next criterion decides. The margin of 5 % is proposed: the screening is of first order and cannot carry a finer one. The identifiers are those of issue 1; only the order is new.

**The north star is fuel, because it is the one measure of environmental effect on record.** The emissions in flight follow the fuel burned. The effects on climate other than carbon dioxide, noise and the life cycle of the aircraft have no figure in the records. `KNU-EWTW-CRZ-001-04` asks the research for them.

**Installed power comes second.** It is mass, which is fuel again, and it is the feasibility of the generation: no turbogenerator of the megawatt class has flown.

**Time comes third.** It no longer weighs against fuel. It counts through the floor `M4`, and after it only between options that fuel and installed power do not separate. `T3` is a time at cruise speed, because the screening has no block time.

### Named in the texts and not in the set

Noise and integration with faster traffic have no figure on record, so nothing can be scored on them today. Propulsive efficiency is not a criterion by itself: it acts through `T2`.

## Maturity the decision requires

On 2026-11-15 the authority decided to keep for this KNOT the threshold of ruling R2 of `KNOT-EWTW-NRG-001`: level 6 of the Q+ATLANTIDE-TRL scale at the release of the preliminary-design baseline, with no waiver. Its reason: the elements this choice depends on are those of the chain that `KNOT-EWTW-NRG-001` and `KNOT-EWTW-GEN-001` size, and no record gives a ground for closing the cruise point on elements less mature than those of the energy carrier.

| Id | Element | Options that depend on it | Required | Level the records support |
|---|---|---|---|---|
| `Q1` | Turbogenerator of megawatt class | A, B, C | 6 | none |
| `Q2` | Propeller driven by an electric motor of megawatt class, at the cruise Mach of the option | A, C | 6 | none |
| `Q3` | Ducted fan driven by an electric motor of megawatt class, at the cruise Mach of the option | B | 6 | none |

- At the concept baseline an element may be below the threshold, if its level and the assumptions are on record.
- At the preliminary-design baseline an element below it needs an approved maturation cycle with its fallback, or a waiver. A waiver is an act of the authority, with its reason (rule 5 of CM-004).
- No level is set today. What the records hold are statements of makers and design studies, not test results.
- `Q1` is common to the three options and does not separate them. The cruise point changes how many megawatts of it are installed, which is criterion `T1`. `Q2` and `Q3` separate the propeller options from the jet option.

## What supports the order

1. **The architecture pays only through the propulsor.** The electric chain costs about a tenth of the power it carries. The [mission screening](MSN-EWTW-NRG-001/README.md) puts the cruise of the eWTW at about 5 % more fuel than the cruise fitted to its reference, at nominal values, with a propeller at 0.85. With the fan at 0.76 of the jet point that becomes about 17 % more. At the jet point the eWTW is, by its own figures, a less efficient jet than the one it is measured against. An ecological alternative cannot be that.
2. **Feasibility.** No turbogenerator of the megawatt class has flown ([record of the generation architecture](KNOT-EWTW-GEN-001_generation-architecture_2026-11-15.md)). Between 14 and 26 MW to install lies the difference between a programme that uses machines seen on a bench and one that waits for machines that do not exist. The means of compliance for a turbo generator is reserved ([record of the certification basis](KNOT-EWTW-CRT-001_certification-basis_2026-11-15.md), statement 11).
3. **The ratio holds even if the rule does not.** The megawatts of `T1` rest on a first-order rule that may be severe. The ratio between the jet point and the fast propeller points comes from the speed and from the air a machine takes in, and it stays between 1.7 and 1.9 whatever the level.

## What the order costs

Time and cost are no longer weighed. A costly aircraft earns its cost by flying more, and a faster one makes more flights in a day. The records hold no figure for what 17 to 20 minutes are worth, so that argument is not answered here; it is set aside by a decision of policy.

The floor `M4` now carries all of it. An aircraft cuts emissions only if it flies in the place of another, and without a floor the north star always chooses the slowest point, with nothing to stop it at 275 kt. The 360 kt are a number of the programme, taken from the fastest turboprop in service and found in no text. `KNU-EWTW-CRZ-001-05` asked the research for the evidence behind a floor, and it found none for or against this one (below).

Three things would open the set again:

- a requirement of a customer or of the market on block time, which moves the floor and not the order;
- a measure of environmental effect that fuel does not carry — contrails, nitrogen oxides, noise — with a figure by cruise altitude;
- a drag polar of the eWTW, or the power of a real gas turbine against altitude, that changes the fuel or the megawatts of the screening.

## What the order implies on the points of the screening

This is an illustration. It retains and rejects nothing: rule 5 allows no scoring before the criteria and the maturity records are approved.

| Step | `P1` 275 kt | `P2` 360 kt | `P3` Mach 0.62 | `P4` Mach 0.78 |
|---|---|---|---|---|
| Floor `M4` | fails | passes | passes | passes |
| 1. Fuel on the scoring mission, against the best | — | best | equal | 13 % more: separated |
| 2. Gas turbines referred to sea level, against the best | — | best | 10 % more: separated | — |
| Order that results | — | first | second | third |

- **The north star alone puts the jet point last.** It loads 13 % more fuel, well beyond the margin. Any margin below 12 % gives the same.
- **The screening cannot separate the two propeller points on fuel.** It flies them with one propulsor efficiency and one lift-to-drag ratio, so their fuel is equal. Installed power separates them, and `M2` stands beside it: option C is above 25,000 ft.
- **Without the floor the slowest point comes first.** Its fuel is equal in the screening and its gas turbines are the smallest, 9.6 MW. The order then chooses an aircraft that takes 130 minutes at cruise speed on the scoring mission.
- **Options, not points, are retained.** Option A keeps its fast end, option C follows, option B is last.

The weights of issue 1 gave the same order: 0.96, 0.93 and 0.77 for `P2`, `P3` and `P4` with the floor, and the slowest point first without it.

## What the research of 2026-11-16 found

The [research record](KNOT-EWTW-CRZ-001_environmental-measure-and-floor_2026-11-16.md) of the two KNUs below changes nothing in the set and says where it stands.

- **On the measure.** A published measure of the same kind as `T2` exists: the carbon dioxide metric of ICAO, fuel for each kilometre in cruise against the size of the cabin, with a limit that tightens for new types from the end of 2031. The EU taxonomy gives a bar for an aircraft of this mass, 11 % below that limit. The programme cannot compute the metric of the eWTW before a cabin area and a drag polar are on record.
- **On the effects other than carbon dioxide.** A lower cruise reduces the forcing of nitrogen oxides and the coverage of contrails, in two assessments of the world fleet. They point the same way as fuel and put the jet point last. No figure sets them beside the fuel of a mission, so they are not scored.
- **On the floor.** Both 275 kt and 360 kt are in service, the slower type in the larger fleet, on stages shorter than those of ruling R2. Nothing anchors the floor at 360 kt and nothing refutes it. `M4` is a requirement of the programme: the missions of ruling R2 are flown by jets today, and the authority does not want the alternative to be slower than the fastest propeller aircraft in service.
- **On the margin.** The figures of the two makers for carbon dioxide by seat-kilometre are 4 % apart, inside the margin of 5 %. The north star does not separate 275 kt from 360 kt; without `M4`, installed power chooses the slower.

## Research asked

| KNU | What it asks | What it feeds |
|---|---|---|
| `KNU-EWTW-CRZ-001-04` | The published measures of the environmental performance of an aeroplane; the effects other than carbon dioxide against cruise altitude; fuel against cruise speed in published data; the rules on sustainable fuel | The north star `T2` |
| `KNU-EWTW-CRZ-001-05` | The speeds and block times operators have accepted in the class, the large turboprops that were studied and not built, the cost of block time, and any limit set by faster traffic | The floor `M4` |

Both were answered on 2026-11-16, the first in part.

One piece of work stays with the programme: the fuel of each cruise point with a drag polar and a machine of the eWTW, in the screening. Until then the north star separates the jet point from the propeller points and nothing else.
