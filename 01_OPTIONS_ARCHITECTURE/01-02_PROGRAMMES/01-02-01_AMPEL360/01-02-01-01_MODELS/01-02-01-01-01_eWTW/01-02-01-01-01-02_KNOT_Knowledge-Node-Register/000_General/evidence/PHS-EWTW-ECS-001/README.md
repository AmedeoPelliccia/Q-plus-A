---
status: draft
standard_scope: governance
---

# PHS-EWTW-ECS-001 — Pack power by phase: candidate worksheet of class D

| | |
|---|---|
| KNOT | [`KNOT-EWTW-ECS-001`](../../KNOT-EWTW-ECS-001.yaml) Cooling cycle of the packs |
| Serves | `KNU-EWTW-ECS-001-02` Pack power by phase for each cycle, as a candidate. Not a table that the load analysis of `KNU-EWTW-SRC-001-01` reads |
| Version | 0.1.0 · 2026-11-28 |
| Produced by | The producer of report B of 2026-11-27, which the author relayed without words and whose producer is not stated. Deposited by Claude, on the ruling of the author of 2026-11-28 |
| Class | D, as its producer labels it: every figure rests on an assumption of the worksheet, none on a measurement of the eWTW |
| State | Candidate calculation, admitted by the author on 2026-11-28. Not a figure of record. Not ratified |
| Reviewed in | [Research record of 2026-11-28](../KNOT-EWTW-ECS-001_cooling-cycle-of-the-packs_2026-11-28.md), section *The worksheet of report B*; the assessment of the reviewer, issue 0.2.1, section 3.8 and table K1 |

This folder holds a calculation of the power that the packs draw and of the sink air they take, case by case of the concept of operations, for the three options of `KNOT-EWTW-ECS-001`. It ranks no option.

**Safety first.** The one-pack rows put the whole duty of the cabin on one unit and do not claim that it can carry it. They are no showing of the floor of fresh air after the loss of a pack, which the author has taken as a design case of `LC-A` with criterion E2 of the KNOT, its classification open until the safety assessment.

## What it may be used for

By the ruling of the author of 2026-11-28:

- `KNOT-EWTW-SRC-001` and its records may cite it **for sensitivities**: how a figure moves when an assumption moves.
- It is **not used for sizing** until cabin loads and pack maps accepted by the authority exist. Its rows do not become figures of record.
- The example given with the ruling: in the same modelled cruise at FL 310 and 360 kt, the fresh flow that the worksheet sets (0.7237 kg/s, 1.67 times the floor of 104 occupants) gives 59.55 kW for the compressor of outside air; at the ventilation floor the same compressor would draw 35.7 kW (assessment, K1).

## Files

| File | What it is | sha256 |
|---|---|---|
| `ecs001_phase_screen.py` | The script of report B, unchanged. Standard library only; it writes the CSV to standard output and nothing else | `babca732cac859d7a2300aeb1e0ffe669e7747d70ed3e5a4b47d7a206848929c` |
| `eWTW-ECS-001_phase-screen_2026-11-27.csv` | Its output as relayed, unchanged: 75 rows, 25 cases by options A, B and C, all of class D | `d6db6fe967abe825b75ae86b12896c1982e141f1d3e152dd67c7c6c1bb2e6d15` |

Neither file is edited in this register. A correction is made in a new issue of the producer, or in a calculation of the programme that names this one.

## How to reproduce

From a folder other than this one, so that no file of the folder is imported:

```
python3 -I <this folder>/ecs001_phase_screen.py > out.csv
sha256sum out.csv
```

The hash equals that of the CSV above. It did so on 2026-11-27 and on 2026-11-28, with Python 3.13. The review recomputes the rows it checks with formulas of its own, and does not run the script for that (assessment, K1).

## Assumptions

Read from the script and from report B; each is an assumption of the worksheet, `P3` for the register.

| Assumption | Value in the worksheet |
|---|---|
| Occupants | 104: 100 passengers and four crew. The author adopted the same reference on 2026-11-28 |
| Cabin setpoint | 297.15 K, dry air, `cp` 1.005 kJ/(kg K) |
| Fresh air | Set so that the supply carries the whole dry gain at 2 °C. On the hot stand that gives 1.809 kg/s, 4.2 times the ventilation floor; at FL 310, 0.7237 kg/s, 1.67 times |
| Recirculation | 40 % of the flow |
| Cabin gains | 40 kW on the hot stand, with 25 and 55 kW as brackets; 16 kW in cruise; invented for the worksheet |
| Compressor and drive | Isentropic efficiency 0.78; drive efficiency 0.94 |
| Option A | An open air cycle: approach of 8 K, no recuperation, expander efficiency 0.78, 85 % of the expander work returned to the compressor shaft |
| Option B | The aftercooler of the compressor stops at the cabin setpoint; the rest of the duty goes to the vapour cycle |
| Vapour cycle | 38 % of the Carnot coefficient: 1.96 on the stand, 2.97 in cruise |
| Sink air | Rise limited to 15 K at low speed and 25 K in flight, with at least 4 K at the hot end |
| Scope | Steady demand of the operating shipset at the bus of the packs; feeder peaks and essential loads apart; unknowns left blank |

## Limits

- The figures follow from the assumptions above; they are not figures of the eWTW.
- The fresh flow set by the 2 °C rule moves the levels of all options alike, more than their differences.
- Option A is an open air cycle without maps: the factor of two between options A and B on the stand is a property of the model. A real three-wheel machine needs its maps.
- In cruise option B pays for cooling that ram air could give, because its aftercooler stops at the setpoint.
- The one-pack rows do not show that one pack can carry the duty.
- The coincidence of packs and ice protection that report B adds uses the CSV of an earlier round and belongs to `KNOT-EWTW-SRC-001`; it is not in this folder.

## Recomputed by the review

| Quantity | Recomputed | Worksheet |
|---|---|---|
| Stand, hot day: fresh air, kg/s | 1.809 | 1.809 |
| Stand, option A: electrical power, kW; pressure ratio | 95.3; 1.965 | 95.3; 1.965 |
| Stand, option B: bus, kW | 54.77 | 54.77 |
| FL 310: inlet total temperature, °C | −29.4 | −29.4 |
| FL 310: fresh air, kg/s | 0.7237 | 0.7237 |
| FL 310: compressor of outside air, kW; pressure ratio | 59.55; 2.161 | 59.55; 2.161 |

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-28 | Deposited on the ruling of the author: the script and the CSV of report B unchanged, with their hashes, assumptions, limits and use |
