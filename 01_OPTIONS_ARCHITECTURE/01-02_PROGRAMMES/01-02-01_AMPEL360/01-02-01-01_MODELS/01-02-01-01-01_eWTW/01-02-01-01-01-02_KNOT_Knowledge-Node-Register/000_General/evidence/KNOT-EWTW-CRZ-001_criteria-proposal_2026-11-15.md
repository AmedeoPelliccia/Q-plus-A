# Criteria and maturity proposed — cruise point

| | |
|---|---|
| KNOT | `KNOT-EWTW-CRZ-001` Cruise point |
| Serves | `KNU-EWTW-CRZ-001-03` Decision criteria and maturity thresholds |
| Proposed by | Claude, 2026-11-15, at the request of the authority of the model |
| Second reading | An assessment relayed by the author on 2026-11-15 found the set consistent with the records and asked for the note on CS 25.841 above 25,000 ft. It does not name its producer |
| State | Proposed. Every criterion is `PROPOSED` in the record of the KNOT. To approve them is an act of the authority |
| Maturity | Three maturity records, added the same day on the decision of the authority to keep the threshold of ruling R2 of `KNOT-EWTW-NRG-001`. They are `PROPOSED` too |
| Gate | Rule 5 keeps the KNOT closed to scoring while a criterion or a maturity record is `PROPOSED` |

This record states a proposal and its reasons. It rules nothing, and by it no option is retained or rejected.

---

## What is being chosen

The published texts name the criteria of a cruise point: block time, fuel, noise, integration with faster traffic, propulsive efficiency, the power of the cabin compressors, the insulation margin. No text gives the weight of time against fuel and installed power. That weight is the choice.

With the few criteria the screening can measure, to choose the weights is to choose the point. The set below is therefore a reasoned decision about what the aircraft is. It is not a neutral scoring, and it should be approved or refused as such.

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

The jet point buys 17 to 20 minutes on the scoring mission. It asks for 1.7 to 1.9 times the gas turbines, 13 % more fuel, and 1.4 to 1.6 times the work of compression.

## The set

### Not traded

| Id | Criterion | Source |
|---|---|---|
| `M1` | The cabin pressure altitude is not above 8,000 ft at the maximum operating altitude, in normal operation | CS 25.841(a), read on 2026-11-15 |
| `M2` | Above 25,000 ft, the cabin pressure altitude stays at or below 15,000 ft after any reasonably probable failure of the pressurisation system | CS 25.841(a), read on 2026-11-15 |
| `M3` | The requirement mission closes at the cruise point, with the reserves of ruling R2 of `KNOT-EWTW-NRG-001` | Ruling R2 of 2026-11-14 |
| `M4` | The cruise speed is not below 360 kt true airspeed, that of the fastest turboprop of the class in service | Proposed here. It is a requirement of the programme and is in no text |

`M2` applies to the points above 25,000 ft only. The turboprops of the class have their ceiling there ([record of the cruise point](KNOT-EWTW-CRZ-001_cruise-point_2026-11-15.md), statements 2 and 4). What it costs is not on record. Option A at its fast end is at 25,000 ft and is not above it; option C at 27,000 ft is. The choice between A and C has to be made knowing it.

The record of the cruise point gave three limits under 14 CFR 25.841. CS 25.841, read today, gives the first two. The limits of exposure after a decompression are in the United States text and were not found in CS 25.841 as read.

### Traded

| Id | Criterion | Measure of the screening | Better | Weight |
|---|---|---|---|---|
| `T1` | Power of the gas turbines for the cruise, referred to sea level | Megawatts, on the take-off mass of the requirement mission | Lower | 0.35 |
| `T2` | Fuel loaded on the scoring mission | Kilograms | Lower | 0.30 |
| `T3` | Time at cruise speed on the scoring mission | Minutes | Lower | 0.20 |
| `T4` | Inception voltage of partial discharge left at the cruise altitude | Share of the value at sea level | Higher | 0.10 |
| `T5` | Ideal work to compress outside air to the cabin pressure | Kilojoules for each kilogram of air | Lower | 0.05 |

Fuel and installed power carry 0.65 together, and time 0.20. No threshold is proposed for a traded criterion.

`T3` is a time at cruise speed, because the screening has no block time. A block time adds taxi, climb and descent, which narrow the differences.

### Named in the texts and not in the set

Noise and integration with faster traffic have no figure on record, so nothing can be scored on them today. If either gets a figure, the weights are to be opened again. Propulsive efficiency is not a criterion by itself: it acts through `T2`.

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

## Why fuel and installed power

1. **The architecture pays only through the propulsor.** The electric chain costs about a tenth of the power it carries. The [mission screening](MSN-EWTW-NRG-001/README.md) puts the cruise of the eWTW at about 5 % more fuel than the cruise fitted to its reference, at nominal values, with a propeller at 0.85. With the fan at 0.76 of the jet point that becomes about 17 % more. At the jet point the eWTW is, by its own figures, a less efficient jet than the one it is measured against.
2. **Feasibility.** No turbogenerator of the megawatt class has flown ([record of the generation architecture](KNOT-EWTW-GEN-001_generation-architecture_2026-11-15.md)). Between 14 and 26 MW to install lies the difference between a programme that uses machines seen on a bench and one that waits for machines that do not exist. The means of compliance for a turbo generator is reserved ([record of the certification basis](KNOT-EWTW-CRT-001_certification-basis_2026-11-15.md), statement 11).
3. **The ratio holds even if the rule does not.** The megawatts of `T1` rest on a first-order rule that may be severe. The ratio between the jet point and the fast propeller points comes from the speed and from the air a machine takes in, and it stays between 1.7 and 1.9 whatever the level.

## The argument against

A costly aircraft earns its cost by flying more. A faster aircraft makes more flights in a day, and its capital and its crew cost less for each seat-kilometre. The records hold no figure for what 17 to 20 minutes are worth, so the argument cannot be weighed here. It is not answered; it is unmeasured.

Three things would open the weights again:

- a requirement of a customer or of the market on block time;
- the power of a real gas turbine against altitude that contradicts the rule behind `T1`;
- a drag polar of the eWTW that makes the fuel of the jet point much closer to that of the propeller points.

## What the set implies on the points of the screening

This is an illustration. It retains and rejects nothing: rule 5 allows no scoring before the criteria and the maturity records are approved.

Each measure is divided into the best value among the points compared, so that the best point has 1 on each criterion, and the results are added with the weights.

| Points compared | `P1` 275 kt | `P2` 360 kt | `P3` Mach 0.62 | `P4` Mach 0.78 |
|---|---|---|---|---|
| With the floor `M4`: three points | fails `M4` | 0.96 | 0.93 | 0.77 |
| Without the floor: four points | 0.92 | 0.83 | 0.81 | 0.70 |

- **The floor does the work on the slow side.** Without `M4` the weights alone put the slowest point first. If the floor is refused, the set chooses an aircraft that takes 130 minutes at cruise speed on the scoring mission.
- **The weights do the work on the fast side.** The jet point is last in both rows. It would lead only with the weight of time at 0.59 or more, the other weights kept in proportion.
- **Options, not points, are retained.** Option A keeps its fast end, option C stays close behind it, option B is last. `M2` then separates A from C.
