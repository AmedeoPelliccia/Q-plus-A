# CRP-EWTW-CRZ-001 — Screening of the candidate cruise points

**Version:** 0.3.0 · **Date:** 2026-11-16 · **Status:** third issue, proposed
**For:** `KNOT-EWTW-CRZ-001`, `KNU-EWTW-CRZ-001-02` Mission screening by cruise point. Its section on the gas turbines also serves `KNU-EWTW-GEN-001-02`, and its section on the carbon dioxide metric `KNU-EWTW-CRZ-001-04`
**Input:** [`cruise-points.yaml`](cruise-points.yaml), and the mission screening [`MSN-EWTW-NRG-001`](../MSN-EWTW-NRG-001/README.md), which is read and not changed
**Checked by:** [`tools/cruise_points.py`](../../../../../../../../../tools/cruise_points.py)

Four candidate cruise points, and what each costs at first order: time, fuel, power, the size of the gas turbines, the carbon dioxide metric, compression of the cabin air and insulation margin. The points come from the [research record](../KNOT-EWTW-CRZ-001_cruise-point_2026-11-15.md) of the cruise point. Two are the maximum cruise of the turboprops of the class in service, one is the point of a design study, one is the Mach of the charts of the reference jet.

This is a screening. It recommends no point and states no conformity with any rule.

*Note of 2026-11-18.* The authority has set the objective at 26 % below the new-type level, and beyond ([record](../KNOT-EWTW-CRZ-001_objective-and-premises_2026-11-18.md)). Item 7 and the section on the metric measure against the former objective, 11 % below. The [screening of the configurations](../CFG-EWTW-AER-001/README.md) gives each point its own polar and each option its own empty mass, and takes the metric at the best lift-to-drag ratio: it replaces items 2 and 7. This screening is kept as issued.

---

## What it shows

1. **Time.** On the requirement mission the jet point spends 144 minutes at cruise speed, against 180 at the fastest propeller point in service and 236 at the slowest. These are times at cruise speed, not block times.
2. **Fuel.** The screening can show one difference only, that of the propulsor efficiency. With a fan at 0.76 against a propeller at 0.85, the jet point loads 7,727 kg on the requirement mission against 6,839 kg, 13 % more, and takes off at 45.0 t against 44.1 t. The mission closes at every point at nominal values.
3. **Power: the cruise asks about as much as the take-off.** At the jet point the cruise asks 111 % of the nominal take-off power of the mission screening. At the two fast propeller points it asks about 80 %, and at the slow one 60 %. The check on a published point says the model is low: the Dash 8-400 uses 86 % of its take-off power at maximum cruise, and the model gives 72 % of the cruise power its sheet publishes.
4. **Cabin.** With the cabin at 8,000 ft, the pressure ratio of the compression goes from 1.6 at 20,000 ft to 3.2 at 35,000 ft. The ideal work on each kilogram of outside air goes from 37 to 85 kJ, 2.3 times.
5. **Insulation.** On the specimens measured, the inception voltage of partial discharge left at the cruise altitude is 82 % of its sea-level value at the lowest point and 70 % at the highest.
6. **Gas turbines.** The [research](../KNOT-EWTW-GEN-001_generation-architecture_2026-11-15.md) on the generation architecture gives no fall of power with altitude. The screening therefore states a rule and declares it an assumption: a gas turbine takes in air in proportion to the total pressure over the root of the total temperature, and gives the same work for each kilogram. The air flow at the four points is 56, 50, 47 and 38 % of that at sea level and at rest. The cruise power referred to sea level is then 9.6, 13.9, 15.3 and 26.1 MW, which is 109, 158, 173 and 290 % of the take-off power.
7. **Carbon dioxide metric.** The authority took the most stringent of the carbon dioxide requirements in law as the minimum objective of the aircraft: today 11 % below the new-type limit of ICAO Annex 16, Volume III, which is 0.60 kg/km at the take-off mass of the requirement mission. With an assumed cabin of 75 m², the screening gives 0.73 kg/km at the propeller points and 0.84 at the jet point: 23 % and 39 % above the objective. No point meets it at nominal values. The product of the efficiencies and of the lift-to-drag ratio is 4.02 where 4.92 is needed; the favourable values of the mission screening give 5.89.

**What items 3 and 6 mean for the sources.** At the cruise speeds read, the generators and the motors are sized by the cruise at least as much as by the take-off (item 3). At the rule of item 6 the gas turbines are sized by the cruise at every point. The nine units of 1,000 kW that the mission screening counts for the take-off would give 5.0 MW at the slowest point, where the cruise asks 5.3 MW. A battery that only shaves the take-off peak then removes nothing from the rating of the turbogenerators. That is an input to `KNOT-EWTW-STO-001` and `KNOT-EWTW-GEN-001`, not a ruling on them, and it stands on an assumption.

## Limits

- **The propeller points are maximum cruise speeds**, read from the sheets of the manufacturers. A long-range cruise is slower and asks less power. The jet point is the Mach of the charts of the reference type.
- **One lift-to-drag ratio serves every point.** The mission screening sets it for its reference at long-range cruise. The check on point `P2` shows that it is too high at a maximum cruise speed.
- **The mass in cruise is taken as the take-off mass**, so the megawatts are an upper bound.
- **The fall of the power of a gas turbine with altitude is a rule, not a measurement.** The research found none for a turbogenerator. The rule holds the machine at one point of its map, behind an inlet that loses nothing, and keeps the work for each kilogram of air. A real machine gives more work for each kilogram in colder air, runs against limits of speed and temperature, and may have a take-off rating held below what it gives at sea level. The check on `P2` cannot tell these apart.
- **The published point takes a rating as a cruise power.** The sheet of the Dash 8-400 gives the maximum cruise power of its engines as a rating, without the altitude at which it is delivered. Both checks on `P2` take it at 25,000 ft and 360 kt. If the engines give less there, the model is nearer to the published point than the first check says, and the second check gives less than 172 %.
- **The carbon dioxide metric is of first order.** No cabin is on record, so its area is an assumption, 60 to 95 m², which moves the metric by about 5 % either way. The take-off mass of the requirement mission stands for the maximum take-off mass. The fuel in cruise is that of the mission screening at three reference masses, with its one lift-to-drag ratio; the standard lets the applicant choose the altitude and the speed of best range, which the screening does not search for. The exponent of the cabin area is as reported.
- **The climb is not sized.**
- **Fuel differs between points by the propulsor efficiency alone.** Drag, engine efficiency and the terminal phases are those of the mission screening at every point.
- **The work of compression is the ideal work on a kilogram of air.** It is not the power of a system: the air flow and the efficiency of the machine are not in it.
- **The inception voltages are those of twisted pairs of magnet wire**, not of a harness or a machine.
- **The take-off band of the mission screening is that of two turboprops** (research record, what follows). It is not a take-off power of an aircraft that cruises at Mach 0.78.

## The screening

Generated by the tool from the two inputs. Do not edit between the markers.

<!-- cruise:begin -->
CRP-EWTW-CRZ-001 0.3.0 for KNOT-EWTW-CRZ-001: 4 points on 3 missions of MSN-EWTW-NRG-001 0.3.0; 29 figures, 6 of them assumptions; rule failures: none

### Points

| Point | Option | Mach | True airspeed | Altitude | Ambient pressure | Propulsor efficiency | Basis of speed · altitude · efficiency |
|---|---|---|---|---|---|---|---|
| `P1` ATR 72-600 at maximum cruise | A | 0.45 | 275 kt · 509 km/h | 20,000 ft | 466 hPa | 0.85 | source · assumption · assumption |
| `P2` Dash 8-400 at maximum cruise | A | 0.60 | 360 kt · 667 km/h | 25,000 ft | 376 hPa | 0.85 | source · source · assumption |
| `P3` Turboprop design study | C | 0.62 | 370 kt · 685 km/h | 27,000 ft | 344 hPa | 0.85 | source · source · source |
| `P4` Jet of the class | B | 0.78 | 450 kt · 833 km/h | 35,000 ft | 238 hPa | 0.76 | source · assumption · source |

### Time at cruise speed

The stage length divided by the true airspeed, in minutes. It is not a block time: climb, descent and taxi are not in it.

| Point | S, 500 km | M, 1,100 km | L, 2,000 km |
|---|---|---|---|
| `P1` | 59 | 130 | 236 |
| `P2` | 45 | 99 | 180 |
| `P3` | 44 | 96 | 175 |
| `P4` | 36 | 79 | 144 |

### Option B at each point

The mission screening at its nominal values, with the propulsor efficiency of the point in place of its own. Nothing else changes with the point, so the differences below are those of that one figure.

| Point | Propulsor efficiency | Take-off mass on S, t | Fuel on S, kg | Take-off mass on M, t | Fuel on M, kg | Take-off mass on L, t | Fuel on L, kg |
|---|---|---|---|---|---|---|---|
| `P1` | 0.85 | 40.3 | 3,066 | 41.8 | 4,535 | 44.1 | 6,839 |
| `P2` | 0.85 | 40.3 | 3,066 | 41.8 | 4,535 | 44.1 | 6,839 |
| `P3` | 0.85 | 40.3 | 3,066 | 41.8 | 4,535 | 44.1 | 6,839 |
| `P4` | 0.76 | 40.7 | 3,446 | 42.4 | 5,107 | 45.0 | 7,727 |

### Power in cruise against take-off

Electrical power at the terminals of the generators for each kilogram of mass, at a lift-to-drag ratio of 15 and an electric chain of 0.90. The take-off power of the screening is 0.20 kW/kg, between 0.16 and 0.25. The megawatts are for the take-off mass of mission L, so they are an upper bound for the cruise.

| Point | Cruise, kW/kg | Cruise, MW | Take-off, MW | Cruise against take-off |
|---|---|---|---|---|
| `P1` | 0.121 | 5.3 | 8.8 | 60% |
| `P2` | 0.158 | 7.0 | 8.8 | 79% |
| `P3` | 0.163 | 7.2 | 8.8 | 81% |
| `P4` | 0.221 | 9.9 | 9.0 | 111% |

**Check on a published point, `P2`.** De Havilland Canada, specification sheet of the Dash 8-400, issue 11, two engines at maximum cruise power and at normal take-off power, at the maximum take-off mass: 0.199 kW of shaft power in cruise for each kilogram of take-off mass, 86% of the take-off power of the same engines. At the same speed the model gives 0.142 kW/kg at the shaft, 72% of the published figure: the published point implies a product of lift-to-drag and propulsor efficiency of 9.1, against 12.8 in the model. With the published figure and the electric chain, the cruise of this point asks 0.221 kW/kg, 111% of the nominal take-off power.

### Gas turbines: the cruise power referred to sea level

A gas turbine held at one point of its map takes in air in proportion to the total pressure at its inlet and to the inverse of the square root of the total temperature. The second column is that air flow at the cruise point against the flow at sea level and at rest, in the standard atmosphere, behind an inlet that loses nothing. The cruise power divided by it is the power at sea level of machines that give the same work for each kilogram of air at both conditions. That rule is an assumption of this screening, of first order. It is not the fall of power of a machine, and none is on record for a turbogenerator.

| Point | Air flow against sea level at rest | Cruise, MW | Referred to sea level, MW | Against take-off power |
|---|---|---|---|---|
| `P1` | 56% | 5.3 | 9.6 | 109% |
| `P2` | 50% | 7.0 | 13.9 | 158% |
| `P3` | 47% | 7.2 | 15.3 | 173% |
| `P4` | 38% | 9.9 | 26.1 | 290% |

**The same rule on the published point, `P2`.** The sheet rates its engines at 7,894 shp at maximum cruise. If they give it at this point, where the air flow is 50% of that at sea level, the rule above makes them machines of 15,734 shp at sea level and at rest, 172% of the take-off power the sheet gives. The sheet does not say at what altitude the rating is given, nor how much of the difference is a take-off rating held below what the engines give at sea level.

### Carbon dioxide metric against the minimum objective

The metric of ICAO Annex 16, Volume III, is the fuel for each kilometre in cruise, averaged over three reference masses, divided by the area of the cabin to the power 0.24. The screening takes the take-off mass of the requirement mission as the maximum take-off mass, and the fuel of its own cruise, which is of first order and has one lift-to-drag ratio for every point. No cabin is on record, so the metric is given for three cabin areas; they are an assumption. The minimum objective is the most stringent of the limits below, by decision of the authority.

| Limit | Below the new-type limit | Source |
|---|---|---|
| New-type limit of ICAO Annex 16, Volume III, first edition | 0% | Research record of the environmental measure, 2026-11-16, statement 1 |
| Standard adopted by ICAO in March 2026, small aeroplanes, new types from 31 December 2031 | 3% | Research record of the environmental measure, 2026-11-16, statement 2 |
| Standard adopted by ICAO in March 2026, large aeroplanes, new types from 31 December 2031 | 10% | Research record of the environmental measure, 2026-11-16, statement 2 |
| EU taxonomy, take-off mass above 5.7 t and up to 60 t — the most stringent | 11% | Research record of the environmental measure, 2026-11-16, statement 3 |

| Point | Take-off mass, t | Fuel in cruise, kg/km | Metric at 60, 75 and 95 m², kg/km | New-type limit, kg/km | Minimum objective, kg/km | Metric against the objective, at 75 m² | Efficiency times lift-to-drag: has, needs |
|---|---|---|---|---|---|---|---|
| `P1` | 44.1 | 2.06 | 0.77, 0.73 and 0.69 | 0.67 | 0.60 | 123% | 4.02, 4.92 |
| `P2` | 44.1 | 2.06 | 0.77, 0.73 and 0.69 | 0.67 | 0.60 | 123% | 4.02, 4.92 |
| `P3` | 44.1 | 2.06 | 0.77, 0.73 and 0.69 | 0.67 | 0.60 | 123% | 4.02, 4.92 |
| `P4` | 45.0 | 2.36 | 0.88, 0.84 and 0.79 | 0.68 | 0.60 | 139% | 3.59, 4.98 |

Points that meet the minimum objective at the nominal cabin area: none. The last column is the product of the efficiencies from the fuel to the propulsor and of the lift-to-drag ratio: what the screening has at its nominal values with the propulsor of the point, and what the objective needs. The mission screening has 5.89 at its favourable values.

### Cabin and insulation

Pressure ratio from the ambient pressure to a cabin at 8,000 ft, the ideal work to compress a kilogram of outside air through it, and the inception voltage of partial discharge left at the ambient pressure, as a share of its value at sea level on the specimens measured.

| Point | Pressure ratio | Ideal work, kJ/kg of air | Inception voltage against sea level |
|---|---|---|---|
| `P1` | 1.62 | 37 | 82% |
| `P2` | 2.00 | 53 | 78% |
| `P3` | 2.19 | 59 | 77% |
| `P4` | 3.16 | 85 | 70% |
<!-- cruise:end -->

## How to verify

From the repository root:

```bash
REG="01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
python3 tools/cruise_points.py "$REG/000_General/evidence/CRP-EWTW-CRZ-001" "$REG" --check
python3 tools/cruise_points_test.py
```

The tool first runs the mission screening through its own check. Its tests compare the standard atmosphere with the published table, and compute by hand the speed, the time, the mission at the jet point, the cruise power, the published point, the air flow of a gas turbine, the power referred to sea level, the carbon dioxide metric with its limit and its objective, the compression and the interpolation of the inception voltage.

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-15 | First issue: four points on the three missions of the eWTW. 19 figures, 4 of them assumptions |
| 0.2.0 | 2026-11-15 | Gas turbines: a declared rule for the air a machine takes in, and the cruise power referred to sea level, for `KNU-EWTW-GEN-001-02`. The published point is said to take a rating as a cruise power. 20 figures, 5 of them assumptions |
| 0.3.0 | 2026-11-16 | The carbon dioxide metric of ICAO Annex 16, Volume III, at first order with an assumed cabin area, against the minimum objective decided by the authority, for `KNU-EWTW-CRZ-001-04`. 29 figures, 6 of them assumptions |
