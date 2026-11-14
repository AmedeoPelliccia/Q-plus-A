---
status: draft
standard_scope: governance
---

# MSN-EWTW-NRG-001 — Candidate missions and first-order closure

| | |
|---|---|
| KNOT | [`KNOT-EWTW-NRG-001`](../../KNOT-EWTW-NRG-001.yaml) Energy carrier |
| Serves | `KNU-EWTW-NRG-001-02` Design mission and reserve policy; a first input to `KNU-EWTW-NRG-001-03` |
| Version | 0.2.0 · 2026-11-14 |
| Prepared by | Claude, for review by `STK_SE` |
| State | Pending review. A proposal: the mission set is approved by the authority |

This analysis proposes three candidate stages for the eWTW and tests, at first order, which energy carrier flies each of them in an airframe of the class: batteries alone (option A), fuel for a turbogenerator (option B), or both (option C). It follows the direction given by the authority on 2026-11-14: carry forward the mission that the technologies available today can fly, and record what the candidates for more ambitious missions still have to reach.

It is a screening. It sizes no aircraft, it ranks no option, and it states no conformity of the eWTW with any rule.

---

## What changed in 0.2.0

Version 0.1.0 let the aircraft shrink with its mission and found take-off masses of 27 to 33 t. An [audit of 2026-11-14](../KNOT-EWTW-NRG-001_audit-of-mission-closure_2026-11-14.md) pointed out that this closed the model and not an aircraft of the class: no in-service type of 100 seats takes off at that mass, and the model had not reproduced the fuel of one. The audit was right.

This version is anchored to a reference type, the Embraer 190:

- **The energy is fitted to published block fuel.** Six sectors from 383 to 1,245 km give the cost of cruise and the cost of the terminal phases. The earlier version derived the terminal phases from the height and the speed of the cruise, and underestimated them by a factor of more than five.
- **The airframe is that of the reference.** Its empty mass is the published basic operating weight, and the limit is its highest certificated take-off mass. A sensitivity shows what changes when the empty mass grows with the take-off mass.
- **The pack of today has a source.** 177 Wh/kg, from the manufacturer of a type-certificated two-seat aeroplane.

## How to read it

- [`missions.yaml`](missions.yaml) is the input: the reference, the missions, the reserves, the parameters and the pack levels. To change the analysis, change that file.
- The section [Screening](#screening) is the output of [`tools/mission_closure.py`](../../../../../../../../../tools/mission_closure.py). It is written by the tool and checked against the input.
- The test is a range equation. The share of the take-off mass that goes into energy follows from the distance flown and from what a kilometre costs. A mission *closes* when the empty aircraft, the payload and the energy stay within the take-off mass limit.
- Each result is given at three sets of parameters: *favourable*, *nominal* and *unfavourable* to closing the mission. The sets are judgement, not statistics.
- *Pack needed* is the specific energy at pack level, as installed, at which the mission just closes. It is not a cell figure.

## What the screening shows

1. **The test reproduces the reference.** The fit matches the six published sectors within about 1 %. On a point outside the fit, the range the type is offered with, it asks for 7 % more fuel than the aircraft can load.
2. **On a short stage, half of the fuel is not cruise.** Taxi, take-off, climb, descent and approach cost the reference as much as about 480 km of cruise. With the reserves, a stage of 500 km is flown as about 1,400 km.
3. **Fuel flies the three candidate stages.** At nominal values option B takes off at 40 to 44 t with 3 to 7 t of fuel, reserves included. At unfavourable values the long stage does not close. At nominal values the cruise of option B is set equal to that of the reference: the test cannot say whether a turbogenerator with electric motors does better or worse than a turbofan.
4. **Batteries alone fly none of them.** On the short stage, option A needs between about 670 and 3,200 Wh/kg at pack level, 1,640 at nominal values. With the one laboratory pack on record, 480.9 Wh/kg over 25 cycles, the longest trip is zero at nominal values and under 200 km at favourable ones. The pack of today, 177 Wh/kg, flies no trip at any set.
5. **Whether a battery beside the fuel saves fuel depends on the airframe.** With the airframe of the reference as it is, a battery that flies a quarter of the short stage breaks even at about 480 Wh/kg and saves about 6 to 11 % of the fuel from 650 to 1,000 Wh/kg. If the empty mass grows with the take-off mass, the saving starts later: between 650 and 1,000 Wh/kg, or beyond. With the pack of today the battery can fly a tenth of the short stage, and the aircraft burns about 16 % more.
6. **Take-off needs 8 to 9 MW at nominal values.** At the ratings on record that is eleven or twelve motors and nine turbogenerators. How many propulsors the aircraft has is the question of `KNOT-EWTW-PRP-001`.

## Reading proposed to the authority

| | Proposal | Why |
|---|---|---|
| Stage carried forward as the baseline | Mission M, the average stage of about 1,100 km, with 100 passengers and the reserves of the planning rule | It is the one stage with a source. It is an average stage, not the range the class is offered with: the reference type is offered with 4,445 km |
| Energy carrier that flies it with what is on record | Option B | The only option that closes a candidate stage without a pack level that does not exist. Its motor and its turbogenerator are on the bench, not in service |
| Stages kept as alternates | S and L | S is where options A and C come closest. L shows where option B stops closing at unfavourable values |
| Candidates for more ambitious solutions | Option C from the level of a laboratory pack, about 480 Wh/kg; option A from about 1,600 Wh/kg on stage S | The levels at which option C stops burning more than option B, and at which option A closes, at nominal values and with the airframe of the reference |

The proposal decides nothing. Whether the design mission of the eWTW is an average stage or a range like the one the class is offered with is the decision of `KNU-EWTW-NRG-001-02`. No option is scored while the criteria and the required maturity are proposed (CM-004, rule 5). The maturity proposed for each critical element is in the record of the KNOT, under `maturity_required`.

## Limits

- **One reference, one source of block fuel.** The fit takes two quantities from six sectors of one type, published in 2009, flown at long-range cruise with 114 seats. One point outside the fit checks it. A second type would test it.
- **The eWTW is not the reference.** Its speed and altitude are not defined. The favourable set gives it 60 % of the terminal distance of the reference, for a lower and slower cruise: that share is an assumption.
- **The three options have the same empty mass.** What the electric chain adds and what the turbofans remove is not on record.
- **Power is not sized.** The test counts units at take-off power. It does not check the power a battery can deliver, and it gives option C no credit for a thermal machine sized to cruise with a battery covering the peaks. That role of the battery is the question of `KNOT-EWTW-STO-001`.
- **Reserves are an analogy.** The final reserve is that of a turbine-engined aeroplane. The reserves behind the published range of the reference are not stated by its manufacturer.
- **The pack of today is of another class.** 24.8 kWh on a two-seat aeroplane. It shows a specific energy, not a pack of megawatt-hour size, its cycle life or its containment.
- **Cost and emissions are not in the test.** Electricity is counted as no fuel, and its origin is not considered.

## How to verify

From the repository root:

```bash
REG="01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
python3 tools/mission_closure.py "$REG/000_General/evidence/MSN-EWTW-NRG-001" "$REG" --check
python3 tools/mission_closure_test.py
```

The tool checks the form of the input, and that options A, B and C stand in the KNOT. With `--check` it fails when the section below differs from what the input gives. `--write` replaces the section. The fit is in the function `fit` and the equations in the class `Model`; the tests compute both again by hand for the committed input.

---

## Screening

<!-- screening:begin -->
MSN-EWTW-NRG-001 0.2.0 for KNOT-EWTW-NRG-001: 3 candidate missions, 4 pack levels, 6 reference sectors; 31 figures, 16 of them assumptions; rule failures: none

Scope: Three candidate stages for an aircraft of 100 passengers, and a first-order test of which energy carrier flies each of them in an airframe of the class. The test is a range equation, fitted to the published block fuel of one in-service type of the class. It ranks nothing and sizes nothing: it shows the order of magnitude and which figures decide.

### Reference aircraft — Embraer 190

| Sector | Distance km | Take-off t | Block fuel published kg | Block fuel fitted kg | Difference |
|---|---:|---:|---:|---:|---:|
| SOU-CDG | 383 | 40.5 | 1924 | 1918 | -0.3% |
| CDG-SOU | 413 | 40.7 | 1985 | 1989 | +0.2% |
| EXT-EGC | 769 | 41.7 | 2796 | 2821 | +0.9% |
| EGC-EXT | 809 | 41.8 | 2951 | 2914 | -1.2% |
| BHX-TLS | 1124 | 42.8 | 3635 | 3677 | +1.2% |
| TLS-BHX | 1245 | 43.0 | 3990 | 3961 | -0.7% |

Source of the sectors: Aircraft Commerce, issue 64, June/July 2009, E-Jet family fuel-burn performance, E-190 with 114 seats and 22,800 lb of payload, long-range cruise, block fuel as trip and 20 minutes of taxi; read on 2026-11-14.

The fit has two results. Taxi, take-off, climb, descent and approach cost the fuel of 483 km of cruise. A thousand kilometres of cruise cost 5.6% of the take-off mass, which is an overall efficiency times lift-to-drag ratio of 4.08 at 43 MJ/kg.

Check on a point outside the fit: for 4445 km with 100 passengers and the reserves of this test, the fit asks for 13396 kg of fuel. At its take-off mass the aircraft can load 12547 kg. The fit asks for +7%. Source of the point: Embraer 190 specification sheet, read on 2026-11-14: range of the LR with full passengers at 100 kg, long-range cruise, typical mission reserves.

### Missions

| Key | Mission | Trip km | Flown with terminal phases and reserves km | Candidate | Basis | Source or note |
|---|---|---:|---:|---|---|---|
| S | Short stage | 500 | 1393 | yes | assumption | Less than half of the average stage of mission M |
| M | Average stage | 1100 | 2023 | yes | source | Research record of 2026-11-14, statement 4: average stage of the United States fleet of 150 seats and fewer, about 1,110 to 1,140 km |
| L | Long stage | 2000 | 2968 | yes | assumption | Nearly twice the average stage |
| X | Range the reference type is offered with | 4445 | 5535 | no | source | Embraer 190 specification sheet, read on 2026-11-14: 2,400 nm for the LR |

Payload: 100 passengers at 95 kg, 9500 kg. At nominal values the terminal phases count for 483 km and the alternate with the final reserve for 385 km. The empty mass is 27753 kg, and 0% of it grows with the take-off mass. A mission closes when the take-off mass stays within 51.8 t.

### Option B — fuel for a turbogenerator, no propulsion battery

| Mission | Take-off mass t, favourable · nominal · unfavourable | Fuel kg | Take-off power MW | Motors | Turbogenerators |
|---|---:|---:|---:|---:|---:|
| S | 33.2 · 40.3 · 46.0 | 3066 | 8.1 | 11 | 9 |
| M | 34.0 · 41.8 · 48.5 | 4535 | 8.4 | 12 | 9 |
| L | 35.3 · 44.1 · over | 6839 | 8.8 | 12 | 9 |
| X | 39.0 · 51.0 · over | 13758 | 10.2 | 14 | 11 |

Fuel, with reserves, power and units are at nominal values. Units are counted at 750 kW for a motor and 1000 kW for a turbogenerator, with all the take-off power from the turbogenerators. Against the cruise fitted to the reference, the cruise of option B costs 0.69 · 1.01 · 1.50 times as much fuel.

### Option A — batteries alone

| Mission | Pack needed Wh/kg, favourable · nominal · unfavourable | Mass t at 177 | Mass t at 480.9 | Mass t at 650 | Mass t at 1000 |
|---|---:|---:|---:|---:|---:|
| S | 673 · 1635 · 3186 | none | over | over | over |
| M | 1026 · 2375 · 4534 | none | none | none | over |
| L | 1556 · 3485 · 6555 | none | none | none | over |
| X | 2995 · 6499 · 12047 | none | none | none | none |

| Pack Wh/kg | Level | Longest trip km at the mass limit, favourable · nominal · unfavourable | Basis | Source or note |
|---:|---|---:|---|---|
| 177 | Pack of a type-certificated two-seat aeroplane, 24.8 kWh | 0 · 0 · 0 | source | Pipistrel, Velis Electro product page, read on 2026-11-14: two batteries, 24.8 kWh in total, about 70 kg each |
| 480.9 | Laboratory pack, 25 cycles | 174 · 0 · 0 | source | Research record of 2026-11-14, statement 11 |
| 650 | Assumption of a NASA study | 461 · 0 · 0 | source | Research record of 2026-11-14, statement 8, as reported |
| 1000 | Level one study needs for economic feasibility | 1056 · 0 · 0 | source | Research record of 2026-11-14, statement 6 |

### Option C — both: the battery flies a share of the trip, fuel flies the rest and the reserves

| Mission | Battery share | Pack needed Wh/kg, favourable · nominal · unfavourable | Mass t at 177 · 480.9 · 650 · 1000 | Fuel burned against option B at 177 · 480.9 · 650 · 1000 |
|---|---:|---:|---:|---:|
| S | 10% | 51 · 158 · 478 | 50.2 · 43.3 · 42.4 · 41.6 | +16% · -0% · -2% · -4% |
| S | 25% | 127 · 381 · 1069 | over · 48.7 · 46.0 · 43.6 | — · -0% · -6% · -11% |
| S | 50% | 248 · 717 · 1817 | over · over · over · 47.5 | — · — · — · -24% |
| M | 10% | 97 · 299 · 1223 | over · 47.3 · 45.6 · 44.0 | — · +5% · +1% · -3% |
| M | 25% | 236 · 699 · 2378 | over · over · over · 47.9 | — · — · — · -7% |
| M | 50% | 454 · 1257 · 3443 | none · over · over · over | — · — · — · — |
| L | 10% | 177 · 616 · 17403 | over · over · 51.3 · 48.2 | — · — · +7% · +1% |
| L | 25% | 423 · 1354 · 9050 | none · over · over · over | — · — · — · — |
| L | 50% | 791 · 2241 · 7602 | none · over · over · over | — · — · — · — |
| X | 10% | 497 · 5179 · none | none · over · over · over | — · — · — · — |
| X | 25% | 1118 · 6383 · none | none · none · over · over | — · — · — · — |
| X | 50% | 1905 · 6733 · none | none · none · none · none | — · — · — · — |

*over* means that the mission needs more than the take-off mass limit, and *none* that no take-off mass flies it. Masses are at nominal values. *Fuel burned against option B* compares kilograms of fuel on the same mission at nominal values: a plus sign means that the aircraft with a battery burns more.

### Sensitivity to the growth of the empty mass

| Share that grows with take-off mass | Option B on S, take-off t | Option A on S, pack needed Wh/kg | Option C on S at 25%, fuel burned against option B at 177 · 480.9 · 650 · 1000 |
|---:|---:|---:|---:|
| 0% | 40.3 | 1635 | — · -0% · -6% · -11% |
| 50% | 36.1 | 1683 | — · +9% · +0% · -8% |
| 100% | 25.5 | 1734 | — · +44% · +19% · +2% |

The test runs at 0%. At 100 % the empty mass is a fixed share of the take-off mass, and the aircraft shrinks with its mission.

### Parameters

| Parameter | Favourable | Nominal | Unfavourable | Basis | Note |
|---|---:|---:|---:|---|---|
| lift_to_drag | 18 | 15 | 13 | assumption | Nominal is set so that the cruise of option B costs what the fit gives for the reference |
| propulsor_efficiency | 0.88 | 0.85 | 0.8 | assumption | — |
| electric_chain_efficiency | 0.93 | 0.9 | 0.87 | assumption | From the terminals of the battery or of the generator to the shaft. A manufacturer states above 95 % for motor and electronics at cruise (statement 15) |
| turbogenerator_efficiency | 0.4 | 0.35 | 0.3 | assumption | From fuel to electricity |
| pack_usable_share | 0.85 | 0.72 | 0.65 | assumption | Nominal is 0.90 usable times 0.80 at the end of service life, as in ELA-EWTW-ESS-001 |
| terminal_share | 0.6 | 1 | 1.2 | assumption | Share of the terminal distance fitted to the reference. Favourable stands for a lower and slower cruise |
| empty_mass_share | 0.8 | 1 | 1.12 | assumption | Share of the basic operating weight of the reference |
| takeoff_kw_per_kg | 0.16 | 0.2 | 0.25 | assumption | — |

| Figure | Value | Basis | Source or note |
|---|---:|---|---|
| payload.kg_per_passenger | 95 | assumption | — |
| reserves.contingency_share | 0.05 | assumption | — |
| reserves.alternate_km | 185 | assumption | — |
| reserves.final_reserve_min | 30 | source | Regulation (EU) 2021/1296, CAT.OP.MPA.181(c)(5), for turbine-engined aeroplanes; research record of 2026-11-14, statement 2 |
| reserves.holding_speed_kmh | 400 | assumption | — |
| units.motor_kw | 750 | source | Research record of 2026-11-14, statement 15: offered rating of a motor tested in the laboratory |
| units.turbogenerator_kw | 1000 | source | Research record of 2026-11-14, statement 16, as reported: in development |
| reference.basic_operating_kg | 27753 | source | Embraer 190 specification sheet, read on 2026-11-14: basic operating weight, standard |
| reference.sizing_takeoff_kg | 50300 | source | Embraer 190 specification sheet, read on 2026-11-14: maximum take-off weight, LR |
| reference.takeoff_limit_kg | 51800 | source | Embraer 190 specification sheet, read on 2026-11-14: maximum take-off weight, AR |
| reference.fuel_lb_per_usg | 6.7 | source | Embraer 190 specification sheet, read on 2026-11-14: fuel density used by the manufacturer |
| fuel_energy_mj_per_kg | 43 | assumption | Lower heating value commonly used for jet fuel; not read at a source |
| empty_growth_share | 0 | assumption | Share of the empty mass that grows with the take-off mass. Zero keeps the airframe of the reference as it is |

### Assumptions

| Id | Assumption |
|---|---|
| A1 | The aircraft carries 100 passengers. The mass taken for each, with baggage, is an assumption until the standard masses of the air operations rules are read |
| A2 | The airframe is that of the reference type. Its empty mass is the basic operating weight of the reference, and a mission closes when the take-off mass stays within the highest take-off mass certificated for it |
| A3 | The airframe is not resized for the mission, so its empty mass is fixed. A sensitivity shows what changes when a share of the empty mass grows in proportion to the take-off mass. The three options have the same empty mass. What the electric chain adds and what the turbofans remove is not on record |
| A4 | Taxi, take-off, climb, descent and approach cost the energy of a fixed distance in cruise. The distance is fitted to the reference, and the eWTW takes a stated share of it |
| A5 | Reserves are flown as distance in cruise — the contingency as a share of the trip, the alternate as a distance, the final reserve as time at holding speed |
| A6 | The final reserve of an aeroplane with electric engines is taken as that of a turbine-engined one, by analogy. The rule names no time for it (research record of 2026-11-14, statement 2) |
| A7 | A battery delivers its specific energy reduced by one share, which covers the capacity held back and the capacity lost at the end of service life |
| A8 | In option C the battery supplies a stated share of the trip energy, and fuel supplies the rest of the trip and all the reserves |
| A9 | Fuel burned makes the aircraft lighter, and the test credits it with the logarithmic form of the range equation. A battery keeps its mass |
| A10 | Take-off shaft power is a fixed power for each kilogram of take-off mass. Units are counted at the ratings that the research record gives for a motor and for a turbogenerator |
<!-- screening:end -->

---

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-14 | First issue: three candidate missions and one reference, four pack levels, three sets of parameters |
| 0.2.0 | 2026-11-14 | After the audit of 2026-11-14: energy fitted to six published sectors of the Embraer 190 and checked on its published range; airframe, empty mass and take-off mass limit of that type; the pack of today from a manufacturer page; a sensitivity to the growth of the empty mass. Take-off masses of option B move from 27–33 t to 40–44 t, and the pack that option A needs on the short stage from about 850 to about 1,640 Wh/kg |
