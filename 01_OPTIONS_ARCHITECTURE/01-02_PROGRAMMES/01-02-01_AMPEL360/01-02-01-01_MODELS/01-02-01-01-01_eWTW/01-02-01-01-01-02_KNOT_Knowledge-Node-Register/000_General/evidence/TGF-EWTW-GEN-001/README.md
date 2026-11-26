# TGF-EWTW-GEN-001 — Turbogenerator figures: read at sources, and recomputed

**Version:** 0.1.0 · **Date:** 2026-11-26 · **Status:** first issue, proposed
**For:** `KNOT-EWTW-GEN-001`, `KNU-EWTW-GEN-001-01` Unit ratings, counts and installations on record and `KNU-EWTW-GEN-001-02` Generation sizing by failure case
**Input:** [`turbogenerator-figures.yaml`](turbogenerator-figures.yaml). It takes the rule of the [screening of the cruise points](../CRP-EWTW-CRZ-001/README.md), which is read and not changed
**Checked by:** [`tools/turbogenerator_figures.py`](../../../../../../../../../tools/turbogenerator_figures.py)

The figures of gas turbines and of generators that the [research record of 2026-11-26](../KNOT-EWTW-GEN-001_turbogenerator-efficiency-and-altitude_2026-11-26.md) accepted, kept as data, with the arithmetic that the record draws on. The input holds two published tables of power against altitude and speed, in full; consumptions of engines and of engine models; part-load points; and masses. Each figure names its source, who read it, and the class the record proposes for it.

This is not a screening. It sizes nothing, it recommends no option, and it states no conformity with any rule. The record says what was accepted and why; this folder only computes.

---

## What it shows

1. **The rule against two tables.** On a standard day at 25,000 and 30,000 ft the two engines give 1.01 to 1.07 and 1.08 to 1.20 times the power of the rule, when the sea-level figure is the maximum rated power, and 1.28 to 1.53 times when it is the maximum continuous power at rest.
2. **The speed.** From rest to 350 kt at those altitudes one engine gains 24 to 26 % and the other 9 to 10 %, where the rule gives 22 to 23 %.
3. **The working reference.** At the nearest tabulated point, 30,000 ft and 350 kt, 5.6 MW ask 12.7 to 12.8 MW of maximum rated power at sea level, or 10.0 MW of maximum continuous power at rest. The rule gives 13.7 MW there, and 14.1 MW at 31,000 ft and 360 kt.
4. **Efficiency.** Twenty-five consumptions turned into shaft efficiency at one heating value, each beside the product with a generator at 0.97. The values of the budget, 0.350 and 0.389 at the terminals, ask 0.361 and 0.401 on the shaft.
5. **Size.** In one family of models the advanced engines go from 0.279 on the shaft at 0.49 MW to 0.418 at 5.59 MW, and from 4.7 to 16.0 kW for each kilogram.
6. **Part load.** A model of a regional engine loses under 1 % at 80 % of its cruise power; an engine of one shaft on a bench loses 14 % at 64 % of its take-off power.
7. **Masses.** Nine masses of parts, from 5 to 26 kW for each kilogram by what each one bounds. None is a turbine with its generator.

## Limits

- **The two tables are an engine deck and a model.** Neither is a measurement, and neither engine is in regional service. They are for 7,500 shp; nothing says that their shape holds at another size.
- **The tables stop at 30,000 ft and 350 kt.** The working reference is beyond both. The figure carried there uses the shape of the rule, and is marked as a hypothesis.
- **The rule is taken as the screening states it**, with an inlet that loses nothing. The tool takes it from `tools/cruise_points.py`; if the screening changes its rule, the check of this folder fails until it is issued again.
- **The power between the values of a table is read by straight lines.** It serves one comparison, between two documents on the same engine.
- **One heating value serves every consumption**: 43.0 MJ/kg, with 42.8 and 43.2 in brackets. The bench test used fuel of 42.8 MJ/kg, and its own efficiencies are printed beside.
- **The product with a generator at 0.97 is arithmetic.** No source read gives an efficiency from the fuel to the terminals. A rectifier is not in it.
- **A model at sea level and at rest is not an engine in cruise.** The table by size holds rated points only.
- **The straight line of fuel flow is an assumption.** Its values below the lowest point of a set are extrapolations, and they are marked.
- **The masses do not add.** Each has its own boundary: with or without gearbox, control unit, rectifier, cooling. None is installed.
- **Thirty figures are read at sources and eight are assumptions.** Of those read, twenty-seven have two readers, two have the reviewer alone and one is as reported. The readers are not independent of the reports: see the record.

## To run it

From the repository root, with `REG` set as in the [register](../../../README.md#how-to-verify):

```bash
python3 tools/turbogenerator_figures.py "$REG/000_General/evidence/TGF-EWTW-GEN-001" "$REG" --check
python3 tools/turbogenerator_figures_test.py
```

## Tables

Written by the tool. Do not edit between the markers.

<!-- figures:begin -->
TGF-EWTW-GEN-001 0.1.0 for KNOT-EWTW-GEN-001: 38 figures, 8 of them assumptions; of those read at a source, 27 by two readers, 2 by the reviewer alone, 1 as reported; rule failures: none

### The rule of the screening at the candidate points

The air a gas turbine takes in, against sea level at rest, by the rule the screening of the cruise points states: total pressure over the root of total temperature, in the standard atmosphere, behind an inlet that loses nothing. The screening takes the same work for each kilogram of air, so this is also its share of the sea-level power.

| Altitude | Mach | True airspeed | Share of sea level at rest |
|---|---|---|---|
| 25,000 ft | 0.50 | 301 kt | 0.472 |
| 25,000 ft | 0.60 | 361 kt | 0.502 |
| 25,000 ft | 0.65 | 391 kt | 0.520 |
| 31,000 ft | 0.50 | 293 kt | 0.370 |
| 31,000 ft | 0.60 | 352 kt | 0.394 |
| 31,000 ft | 0.65 | 381 kt | 0.408 |
| 35,000 ft | 0.50 | 288 kt | 0.313 |
| 35,000 ft | 0.60 | 346 kt | 0.333 |
| 35,000 ft | 0.65 | 375 kt | 0.344 |

At the working reference, 31,000 ft and 360 kt, Mach 0.614, the share is 0.3976: 5.6 MW at the gas turbines are 14.1 MW referred to sea level, against 7.9 to 10.0 MW at take-off.

### Two published tables beside the rule

Each cell gives the power of the table in shp, then that power over the power the rule gives, twice: first with the maximum rated power as the sea-level figure, then with the maximum continuous power at sea level and at rest. Above 1, the engine of the table gives more than the rule.

**NASA engine of the LCTR2 study.** Maximum continuous power for each engine, at 100 % of the power-turbine speed. Maximum rated power at sea level and at rest: 7,500 shp; maximum continuous power there: 5,896 shp.

| True airspeed | Sea level | 5,000 ft, ISA+20 | 10,000 ft | 25,000 ft | 30,000 ft |
|---|---|---|---|---|---|
| 0 kt | 5,896 · 0.79 · 1.00 | 4,420 · 0.72 · 0.92 | 4,743 · 0.89 · 1.13 | 3,089 · 1.01 · 1.28 | 2,605 · 1.04 · 1.33 |
| 50 kt | 5,922 · 0.79 · 1.00 | 4,438 · 0.72 · 0.92 | 4,763 · 0.89 · 1.13 | 3,103 · 1.01 · 1.29 | 2,618 · 1.04 · 1.33 |
| 100 kt | 5,997 · 0.79 · 1.00 | 4,495 · 0.72 · 0.92 | 4,824 · 0.89 · 1.13 | 3,146 · 1.01 · 1.29 | 2,657 · 1.04 · 1.33 |
| 150 kt | 6,125 · 0.79 · 1.01 | 4,590 · 0.73 · 0.92 | 4,926 · 0.89 · 1.13 | 3,219 · 1.01 · 1.29 | 2,723 · 1.05 · 1.33 |
| 200 kt | 6,307 · 0.80 · 1.01 | 4,726 · 0.73 · 0.93 | 5,071 · 0.90 · 1.14 | 3,323 · 1.02 · 1.29 | 2,817 · 1.05 · 1.34 |
| 250 kt | 6,547 · 0.80 · 1.02 | 4,905 · 0.74 · 0.94 | 5,263 · 0.90 · 1.14 | 3,459 · 1.02 · 1.30 | 2,942 · 1.06 · 1.35 |
| 300 kt | 6,850 · 0.81 · 1.03 | 5,130 · 0.74 · 0.95 | 5,504 · 0.90 · 1.15 | 3,632 · 1.03 · 1.31 | 3,100 · 1.07 · 1.36 |
| 350 kt | 7,220 · 0.82 · 1.04 | 5,407 · 0.75 · 0.96 | 5,800 · 0.91 · 1.16 | 3,843 · 1.03 · 1.31 | 3,294 · 1.07 · 1.37 |

On a standard day at 25,000 ft and above, the table gives 1.01 to 1.07 times the rule on the first reading and 1.28 to 1.37 times on the second.

**Rolls-Royce engine of 2015, scaled from 8,100 to 7,500 shp.** Maximum continuous power for each engine, scaled to 7,500 shp of maximum rated power. Maximum rated power at sea level and at rest: 7,500 shp; maximum continuous power there: 5,900 shp.

| True airspeed | Sea level | 5,000 ft, ISA+20 | 10,000 ft | 25,000 ft | 30,000 ft |
|---|---|---|---|---|---|
| 0 kt | 5,900 · 0.79 · 1.00 | 5,487 · 0.89 · 1.14 | 5,296 · 0.99 · 1.26 | 3,657 · 1.20 · 1.52 | 3,005 · 1.20 · 1.53 |
| 50 kt | 5,916 · 0.79 · 1.00 | 5,501 · 0.89 · 1.14 | 5,311 · 0.99 · 1.26 | 3,679 · 1.20 · 1.52 | 3,023 · 1.20 · 1.53 |
| 100 kt | 5,931 · 0.78 · 0.99 | 5,514 · 0.89 · 1.13 | 5,326 · 0.98 · 1.25 | 3,701 · 1.19 · 1.51 | 3,041 · 1.20 · 1.52 |
| 150 kt | 5,947 · 0.77 · 0.98 | 5,527 · 0.87 · 1.11 | 5,341 · 0.97 · 1.23 | 3,722 · 1.17 · 1.49 | 3,059 · 1.18 · 1.50 |
| 200 kt | 5,963 · 0.75 · 0.96 | 5,541 · 0.86 · 1.09 | 5,356 · 0.95 · 1.20 | 3,744 · 1.15 · 1.46 | 3,078 · 1.15 · 1.46 |
| 250 kt | 6,006 · 0.74 · 0.94 | 5,575 · 0.84 · 1.06 | 5,405 · 0.92 · 1.17 | 3,817 · 1.13 · 1.43 | 3,143 · 1.13 · 1.44 |
| 300 kt | 6,072 · 0.72 · 0.91 | 5,636 · 0.82 · 1.04 | 5,469 · 0.90 · 1.14 | 3,894 · 1.10 · 1.40 | 3,208 · 1.10 · 1.40 |
| 350 kt | 6,148 · 0.70 · 0.88 | 5,702 · 0.79 · 1.01 | 5,546 · 0.87 · 1.11 | 4,002 · 1.08 · 1.37 | 3,303 · 1.08 · 1.37 |

On a standard day at 25,000 ft and above, the table gives 1.08 to 1.20 times the rule on the first reading and 1.37 to 1.53 times on the second.

### What the speed is worth

Power at 350 kt over power at rest, at the same altitude.

| Condition | NASA engine of the LCTR2 study | Rolls-Royce engine of 2015, scaled from 8,100 to 7,500 shp | The rule |
|---|---|---|---|
| Sea level | 1.225 | 1.042 | 1.178 |
| 5,000 ft, ISA+20 | 1.223 | 1.039 | 1.171 |
| 10,000 ft | 1.223 | 1.047 | 1.191 |
| 25,000 ft | 1.244 | 1.094 | 1.217 |
| 30,000 ft | 1.264 | 1.099 | 1.227 |

### The cruise power of the working reference, referred to sea level by each table

The tables stop below the working reference. The nearest tabulated point is taken, and 5.6 MW are asked of the engine there.

| Engine | Nearest tabulated point | Maximum continuous power there, for 7,500 shp rated | Maximum rated power at sea level | Maximum continuous power at sea level, at rest | By the rule at that point |
|---|---|---|---|---|---|
| NASA engine of the LCTR2 study | 30,000 ft, 350 kt | 2.456 MW | 12.8 MW | 10.0 MW | 13.7 MW |
| Rolls-Royce engine of 2015, scaled from 8,100 to 7,500 shp | 30,000 ft, 350 kt | 2.463 MW | 12.7 MW | 10.0 MW | 13.7 MW |

Carried from that point to the working reference by the shape of the rule, which is a hypothesis, the maximum rated power becomes 13.1 and 13.1 MW, against 14.1 MW by the rule alone.

### Two documents on one engine

The NASA engine in a second document, sized at 6,476 hp: 11,070 hp available for 4 engines at 28,000 ft and 284 kt, Mach 0.478, which is 0.427 of its maximum rated power. Scaled to the rated power of the table, that is 3,205 shp. The table, read between its four nearest values by straight lines, gives 3,260 shp. The second document is -1.7% from the table.

### Consumption turned into efficiency

Shaft work over the heating value of the fuel, at 43.0 MJ/kg; in brackets, at 43.2 and at 42.8 MJ/kg. The next column multiplies by a generator at 0.97: the boundary of the values of the budget, the terminals of the generator. No source read gives that product.

| Figure | As published | kg/kWh | Shaft efficiency | With a generator at 0.97 | Read by | Class proposed |
|---|---|---|---|---|---|---|
| NASA model of an engine like the PW127E, state of the art: sea level, at rest, take-off, 1,790 kW | 0.474 lb/(hp h) | 0.2883 | 0.290 (0.289 to 0.292) | 0.282 | two readers | C |
| NASA model of an engine like the PW127E, state of the art: 20,000 ft, Mach 0.5, full throttle, 1,265 kW | 0.430 lb/(hp h) | 0.2616 | 0.320 (0.319 to 0.322) | 0.310 | two readers | C |
| NASA model of an engine like the PW127E, state of the art: 20,000 ft, Mach 0.5, 90 %, 1,139 kW | 0.432 lb/(hp h) | 0.2628 | 0.319 (0.317 to 0.320) | 0.309 | two readers | C |
| NASA model of an engine like the PW127E, state of the art: 20,000 ft, Mach 0.5, 80 %, 1,012 kW | 0.433 lb/(hp h) | 0.2634 | 0.318 (0.316 to 0.319) | 0.308 | two readers | C |
| The same model with the technology it takes for 2030: sea level, at rest, take-off, 1,790 kW | 0.427 lb/(hp h) | 0.2597 | 0.322 (0.321 to 0.324) | 0.313 | two readers | D |
| The same model with the technology it takes for 2030: 20,000 ft, Mach 0.5, full throttle, 1,196 kW | 0.398 lb/(hp h) | 0.2421 | 0.346 (0.344 to 0.347) | 0.335 | two readers | D |
| The same model with the technology it takes for 2030: 20,000 ft, Mach 0.5, 90 %, 1,076 kW | 0.394 lb/(hp h) | 0.2397 | 0.349 (0.348 to 0.351) | 0.339 | two readers | D |
| The same model with the technology it takes for 2030: 20,000 ft, Mach 0.5, 80 %, 957 kW | 0.391 lb/(hp h) | 0.2378 | 0.352 (0.350 to 0.354) | 0.341 | two readers | D |
| PW120A in airline service, one instant of a cruise: engine 1, 928.7 kW, 62% of its take-off rating | 266.4 kg/h | 0.2869 | 0.292 (0.291 to 0.293) | 0.283 | two readers | B |
| PW120A in airline service, one instant of a cruise: engine 2, 930.4 kW, 62% of its take-off rating | 281.1 kg/h | 0.3021 | 0.277 (0.276 to 0.278) | 0.269 | two readers | B |
| T56 on a test bench, four power settings: 75 % mode, 2,198.7 kW | 0.235 kg/s | 0.3848 | 0.218 (0.217 to 0.219) | 0.211 | as reported | B |
| T56 on a test bench, four power settings: 100 % mode, 2,996.3 kW | 0.294 kg/s | 0.3532 | 0.237 (0.236 to 0.238) | 0.230 | as reported | B |
| T56 on a test bench, four power settings: military, 3,256.3 kW | 0.309 kg/s | 0.3416 | 0.245 (0.244 to 0.246) | 0.238 | as reported | B |
| T56 on a test bench, four power settings: take-off, 3,442.0 kW | 0.317 kg/s | 0.3316 | 0.253 (0.251 to 0.254) | 0.245 | as reported | B |
| AE1107 as NASA quotes it, 6,000 hp, sea level at rest | 0.426 lb/(hp h) | 0.2591 | 0.323 (0.322 to 0.325) | 0.313 | two readers | C |
| GE38 class in a NASA model of 2014, scaled to 7,500 hp, sea level at rest | 0.385 lb/(hp h) | 0.2342 | 0.357 (0.356 to 0.359) | 0.347 | two readers | C |
| GE38 class in a NASA model of 2019, 7,248 hp, sea level at rest | 0.394 lb/(hp h) | 0.2397 | 0.349 (0.348 to 0.351) | 0.339 | two readers | C |
| GE38 class in the NASA and Army model of 2023, 7,248 hp, sea level at rest | 0.3909 lb/(hp h) | 0.2378 | 0.352 (0.350 to 0.354) | 0.342 | two readers | C |
| LCTR2 engine, 6,476 hp of maximum rated power, sea level at rest | 0.345 lb/(hp h) | 0.2099 | 0.399 (0.397 to 0.401) | 0.387 | two readers | D |
| LCTR2 engine, 5,105 hp of maximum continuous power, sea level at rest | 0.359 lb/(hp h) | 0.2184 | 0.383 (0.382 to 0.385) | 0.372 | two readers | D |
| LCTR2 engine, cruise start, 28,000 ft and 284 kt | 0.324 lb/(hp h) | 0.1971 | 0.425 (0.423 to 0.427) | 0.412 | two readers | D |
| LCTR2 engine, cruise end, 28,000 ft and 272 kt | 0.333 lb/(hp h) | 0.2026 | 0.413 (0.411 to 0.415) | 0.401 | two readers | D |
| Engine of the technology of 2035 in a NASA study, sea level, take-off | 0.3255 lb/(hp h) | 0.1980 | 0.423 (0.421 to 0.425) | 0.410 | two readers | D |
| First further generation in a NASA study of 2014, sea level at rest | 0.312 lb/(hp h) | 0.1898 | 0.441 (0.439 to 0.443) | 0.428 | two readers | D |
| Second further generation in the same study | 0.267 lb/(hp h) | 0.1624 | 0.515 (0.513 to 0.518) | 0.500 | two readers | D |

The bench test is on fuel of 42.8 MJ/kg, at 93.6 kPa and 298.15 K. At its own heating value its efficiencies are 0.219, 0.238, 0.246, 0.254. The cruise point of the flight datum is at Mach 0.40, with its indicated airspeed taken as calibrated.

The values of the budget run from the fuel to the terminals of the generator. 0.350 asks 0.361 at the shaft with a generator at 0.97, a consumption of 0.381 lb/(hp h). 0.389 asks 0.401 at the shaft with a generator at 0.97, a consumption of 0.343 lb/(hp h).

NASA model of an engine like the PW127E, state of the art, at full throttle at its cruise point against take-off: power 0.707, air 0.625, work for each kilogram of air 1.131. The rule gives 0.573 there. The model gives 1.23 times the rule: 1.09 times its air and 1.13 times its work.

The same model with the technology it takes for 2030, at full throttle at its cruise point against take-off: power 0.668, air 0.608, work for each kilogram of air 1.100. The rule gives 0.573 there. The model gives 1.17 times the rule: 1.06 times its air and 1.10 times its work.

### Efficiency and weight against the size of the unit, in one family of models

Engines without a reduction gearbox, at their rated power at sea level and at rest. A model is not an engine, and the advanced rows are forecasts.

| Model | Technology | Rated power | lb/(hp h) | Shaft efficiency | With a generator at 0.97 | Weight | Power for each kilogram | Class proposed |
|---|---|---|---|---|---|---|---|---|
| `ts650s` | current | 650 hp, 0.48 MW | 0.5341 | 0.258 | 0.250 | 110 kg | 4.4 kW/kg | C |
| `ts650a` | advanced | 660 hp, 0.49 MW | 0.4926 | 0.279 | 0.271 | 105 kg | 4.7 kW/kg | D |
| `ts1300a` | advanced | 1,300 hp, 0.97 MW | 0.465 | 0.296 | 0.287 | 155 kg | 6.2 kW/kg | D |
| `ts1900s` | current | 1,895 hp, 1.41 MW | 0.4661 | 0.295 | 0.286 | 208 kg | 6.8 kW/kg | C |
| `ts3000a1_25` | advanced | 3,000 hp, 2.24 MW | 0.3601 | 0.382 | 0.371 | 208 kg | 10.8 kW/kg | D |
| `ts3000a1_18` | advanced | 3,000 hp, 2.24 MW | 0.3598 | 0.383 | 0.371 | 209 kg | 10.7 kW/kg | D |
| `ts3000a2` | advanced | 3,000 hp, 2.24 MW | 0.3484 | 0.395 | 0.383 | 206 kg | 10.8 kW/kg | D |
| `ts5000s` | current | 5,000 hp, 3.73 MW | 0.4942 | 0.279 | 0.270 | 373 kg | 10.0 kW/kg | C |
| `ts5000a` | advanced | 5,000 hp, 3.73 MW | 0.3358 | 0.410 | 0.398 | 265 kg | 14.1 kW/kg | D |
| `ts7500s` | mid | 7,248 hp, 5.40 MW | 0.3909 | 0.352 | 0.342 | 492 kg | 11.0 kW/kg | C |
| `ts7500a` | advanced | 7,500 hp, 5.59 MW | 0.3293 | 0.418 | 0.405 | 351 kg | 16.0 kW/kg | D |
| `ts11000s` | current | 11,000 hp, 8.20 MW | 0.3481 | 0.395 | 0.384 | 840 kg | 9.8 kW/kg | C |
| `ts15000a` | advanced | 15,000 hp, 11.19 MW | 0.3295 | 0.418 | 0.405 | 809 kg | 13.8 kW/kg | D |

### Part load

Consumption for each kilowatt-hour at a part of the power, over that at the reference of the same set: full throttle at the same flight condition, or take-off on the bench.

| Set | Point | Share of the reference power | Consumption over the reference | Efficiency lost |
|---|---|---|---|---|
| NASA model of an engine like the PW127E, state of the art | 20,000 ft, Mach 0.5, 90 % | 0.900 | 1.005 | 0.5% |
| NASA model of an engine like the PW127E, state of the art | 20,000 ft, Mach 0.5, 80 % | 0.800 | 1.007 | 0.7% |
| The same model with the technology it takes for 2030 | 20,000 ft, Mach 0.5, 90 % | 0.900 | 0.990 | a gain of 1.0% |
| The same model with the technology it takes for 2030 | 20,000 ft, Mach 0.5, 80 % | 0.800 | 0.982 | a gain of 1.8% |
| T56 on a test bench, four power settings | 75 % mode | 0.639 | 1.161 | 13.8% |
| T56 on a test bench, four power settings | 100 % mode | 0.871 | 1.065 | 6.1% |
| T56 on a test bench, four power settings | Military | 0.946 | 1.030 | 2.9% |

NASA engine of the LCTR2 study, power used over the maximum continuous power available. No point at full power is published at its cruise condition.

| Point | Share of the power available | lb/(hp h) |
|---|---|---|
| Cruise start, 28,000 ft, 284 kt | 0.688 | 0.324 |
| Cruise end, 28,000 ft, 272 kt | 0.613 | 0.333 |

A straight line of fuel flow against power through two points of a set is an assumption, not a reading. It gives the columns below. A value marked * is below the lowest point of its set: an extrapolation.

| Set | Line through | Fuel flow at no power, as a share of full power | Consumption over full power at 70 % | at 60 % | at 50 % |
|---|---|---|---|---|---|
| NASA model of an engine like the PW127E, state of the art | full throttle and its lowest point, at 20,000 ft | 0.028 | 1.012* | 1.019* | 1.028* |
| The same model with the technology it takes for 2030 | full throttle and its lowest point, at 20,000 ft | -0.070 | 0.970* | 0.953* | 0.930* |
| T56 on a test bench, four power settings | take-off and its lowest mode, on the ground | 0.284 | 1.122 | 1.189* | 1.284* |
| NASA engine of the LCTR2 study, power used over the maximum continuous power available | its two cruise points at 28,000 ft | 0.168 | 1.072 | 1.112* | 1.168* |

### Masses

Rated power over mass, as each source bounds the mass. No row is a turbine with its generator, and none is an installed mass.

| Item | Power | Mass | Power for each kilogram | Read by | Class proposed |
|---|---|---|---|---|---|
| Generator of 1 MW, alone, 280 lb | 1,000 kW | 127.0 kg | 7.87 kW/kg | two readers | B |
| The same at the 900 kW it ran continuously | 900 kW | 127.0 kg | 7.09 kW/kg | two readers | B |
| The same with its control unit and rectifier bridge, 340 lb | 1,000 kW | 154.2 kg | 6.48 kW/kg | two readers | D |
| Generator of 4 MW, as designed | 4,000 kW | 232.0 kg | 17.24 kW/kg | two readers | D |
| The same, prototype as built, at its rated power | 4,000 kW | 249.0 kg | 16.06 kW/kg | two readers | C |
| Active rectifier for that generator, 5 MVA, taken at 4 MW | 4,000 kW | 240.0 kg | 16.67 kW/kg | the reviewer | none |
| Concept generator of 2.98 MW | 2,979 kW | 320.2 kg | 9.30 kW/kg | two readers | D |
| Its converter of 2.93 MW | 2,932 kW | 111.8 kg | 26.22 kW/kg | two readers | D |
| PW150A turboprop with its reduction gearbox, dry | 3,781 kW | 716.9 kg | 5.27 kW/kg | two readers | B |

Hybrid turboelectric regional jet of a university study, for each wing: a generator of 4,369 kW, 3,299 kg of electric propulsion system and 2,472 kg of engine, 5,772 kg together. That is 1.45 times the engine of its baseline of today and 2.02 times its conventional engine of the same year. With the electric system doubled it is 2.27 times the engine of the baseline.
<!-- figures:end -->
