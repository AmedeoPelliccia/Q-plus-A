---
status: draft
standard_scope: governance
---

# MSN-EWTW-NRG-001 — Candidate missions and first-order closure

| | |
|---|---|
| KNOT | [`KNOT-EWTW-NRG-001`](../../KNOT-EWTW-NRG-001.yaml) Energy carrier |
| Serves | `KNU-EWTW-NRG-001-02` Design mission and reserve policy; a first input to `KNU-EWTW-NRG-001-03` |
| Version | 0.1.0 · 2026-11-14 |
| Prepared by | Claude, for review by `STK_SE` |
| State | Pending review. A proposal: the mission set is approved by the authority |

This analysis proposes three candidate design missions for the eWTW and tests, at first order, which energy carrier flies each of them: batteries alone (option A), fuel for a turbogenerator (option B), or both (option C). It follows the direction given by the authority on 2026-11-14: carry forward the mission that the technologies available today can fly, and record what the candidates for more ambitious missions still have to reach.

It is a screening. It sizes no aircraft, it ranks no option, and it states no conformity of the eWTW with any rule.

---

## How to read it

- [`missions.yaml`](missions.yaml) is the input: the missions, the reserves, the parameters and the pack levels. To change the analysis, change that file.
- The section [Screening](#screening) is the output of [`tools/mission_closure.py`](../../../../../../../../../tools/mission_closure.py). It is written by the tool and checked against the input.
- A mission *closes* when the take-off mass it needs stays within the limit. The test is a range equation: the share of the take-off mass that goes into energy follows from the distance, the lift-to-drag ratio and the efficiencies, and what is left after the empty aircraft carries the payload.
- Each result is given at three sets of parameters: *favourable*, *nominal* and *unfavourable* to closing the mission. The sets are judgement, not statistics.
- *Pack needed* is the specific energy at pack level, as installed, at which the mission just closes. It is not a cell figure.

## What the screening shows

1. **Fuel for a turbogenerator flies the three candidate missions.** Option B closes them at every set of parameters, at about 27 to 33 t of take-off mass at nominal values. It does not reach the range the class offers today, except at favourable values.
2. **Batteries alone fly none of them at a pack level that exists.** On the short mission, option A needs between about 470 and 1,420 Wh/kg at pack level, 850 at nominal values. With the one laboratory pack on record, 480.9 Wh/kg over 25 cycles, the longest trip at nominal values is under 100 km.
3. **The reserves decide for the battery.** The short mission is a trip of 500 km, and the aircraft has to carry the energy for about 1,000 km. Which reserve applies to an aeroplane with electric engines is not written in the rule (assumption A5).
4. **A battery beside the fuel does not save fuel at these pack levels.** Option C closes the short mission with a pack of the kind certificated today when the battery flies a tenth of the trip, and it burns more fuel than option B, because it is heavier. In this test the battery saves fuel only on the short mission, from about 1,000 Wh/kg. This agrees with the two NASA studies read (research record of 2026-11-14, statements 6 and 7).
5. **The propulsion is distributed.** Take-off needs between 5 and 7 MW. At the ratings on record that is eight or nine motors and six or seven turbogenerators. How many propulsors the aircraft has is the question of `KNOT-EWTW-PRP-001`.
6. **Three figures decide.** The lift-to-drag ratio, the empty mass fraction and the share of the pack that can be used move the pack that option A needs by a factor of three between the favourable and the unfavourable set.

## Reading proposed to the authority

| | Proposal | Why |
|---|---|---|
| Design mission of the baseline | Mission M, the average stage of about 1,100 km, with 100 passengers and the reserves of the planning rule | It is the one mission with a source. Option B flies it with margin at every set of parameters |
| Energy carrier that flies it with what is on record | Option B | The only option that closes a candidate mission without a pack level that does not exist. Its motor and its turbogenerator are on the bench, not in service |
| Missions kept as alternates | S and L | S is where options A and C would first close. L shows the margin of option B |
| Candidates for more ambitious solutions | Option C when a pack reaches about 1,000 Wh/kg; option A from about 850 Wh/kg on mission S and 1,400 on mission M | The level at which option C begins to save fuel on mission S, and the levels at which option A closes, at nominal values |

The proposal decides nothing. The mission set is approved by the authority (`KNU-EWTW-NRG-001-02`), and no option is scored while the criteria and the required maturity are proposed (CM-004, rule 5). The maturity proposed for each critical element is in the record of the KNOT, under `maturity_required`.

## Limits

- **Every aircraft parameter is an assumption.** The test is not calibrated against an in-service aircraft. That needs the masses and the fuel burned of a type of the class, which the brief of `KNU-EWTW-NRG-001-03` asks for. First-order tests of this kind tend to underestimate the energy.
- **Mass fractions are fixed.** A real aircraft grows its structure, its wing and its propulsion with its mass. The test only stops at the take-off mass limit.
- **Power is not sized.** The test counts units at take-off power. It does not check the power a battery can deliver, and it gives option C no credit for a thermal machine sized to cruise with a battery covering the peaks. That role of the battery is the question of `KNOT-EWTW-STO-001`.
- **One flight condition.** Cruise at 500 km/h and 7,600 m, slower and lower than the jets of the class.
- **The pack of today has no figure with a document.** 170 Wh/kg is an assumption. A type-certificated two-seat aeroplane flies on a dual battery system (EASA.A.573, manufacturer page read on 2026-11-14); the page gives neither its energy nor its mass.
- **Cost and emissions are not in the test.** Electricity is counted as no fuel, and its origin is not considered.

## How to verify

From the repository root:

```bash
REG="01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
python3 tools/mission_closure.py "$REG/000_General/evidence/MSN-EWTW-NRG-001" "$REG" --check
python3 tools/mission_closure_test.py
```

The tool checks the form of the input, and that options A, B and C stand in the KNOT. With `--check` it fails when the section below differs from what the input gives. `--write` replaces the section. The equations are in the class `Model`, and the tests compute them again by hand for the committed input.

---

## Screening

<!-- screening:begin -->
MSN-EWTW-NRG-001 0.1.0 for KNOT-EWTW-NRG-001: 3 candidate missions, 4 pack levels; 29 figures, 21 of them assumptions; rule failures: none

Scope: Three candidate design missions for an aircraft of 100 passengers, and a first-order test of which energy carrier closes each of them. The test is a range equation with mass fractions. It ranks nothing and sizes nothing: it shows the order of magnitude and which figures decide.

### Missions

| Key | Mission | Trip km | Flown with reserves km | Candidate | Basis | Source or note |
|---|---|---:|---:|---|---|---|
| S | Short stage | 500 | 996 | yes | assumption | Less than half of the average stage of mission M |
| M | Average stage | 1100 | 1626 | yes | source | Research record of 2026-11-14, statement 4: average stage of the United States fleet of 150 seats and fewer, about 1,110 to 1,140 km |
| L | Long stage | 2000 | 2571 | yes | assumption | Nearly twice the average stage |
| X | Range offered by the class | 6670 | 7475 | no | source | Research record of 2026-11-14, statement 5: up to 3,600 nm, as reported |

Payload: 100 passengers at 95 kg, 9500 kg. Reserves at nominal values: 385 km for the alternate and the final reserve, and 86 km for take-off and climb. A mission closes when the take-off mass stays within 60 t.

### Option B — fuel for a turbogenerator, no propulsion battery

| Mission | Take-off mass t, favourable · nominal · unfavourable | Fuel kg | Take-off power MW | Motors | Turbogenerators |
|---|---:|---:|---:|---:|---:|
| S | 22.7 · 26.8 · 33.3 | 1236 | 5.4 | 8 | 6 |
| M | 23.8 · 29.1 · 38.7 | 2159 | 5.8 | 8 | 6 |
| L | 25.6 · 33.3 · 50.1 | 3813 | 6.7 | 9 | 7 |
| X | 39.8 · over · none | — | — | — | — |

Fuel, power and units are at nominal values. Units are counted at 750 kW for a motor and 1000 kW for a turbogenerator, with all the take-off power from the turbogenerators.

### Option A — batteries alone

| Mission | Pack needed Wh/kg, favourable · nominal · unfavourable | Mass t at 170 | Mass t at 480.9 | Mass t at 650 | Mass t at 1000 |
|---|---:|---:|---:|---:|---:|
| S | 473 · 851 · 1419 | none | none | over | 46.0 |
| M | 767 · 1389 · 2325 | none | none | none | over |
| L | 1208 · 2196 · 3684 | none | none | none | none |
| X | 3495 · 6385 · 10736 | none | none | none | none |

| Pack Wh/kg | Level | Longest trip km at the mass limit, favourable · nominal · unfavourable | Basis | Source or note |
|---:|---|---:|---|---|
| 170 | Pack of the kind certificated today | 0 · 0 · 0 | assumption | No pack figure with a document is on record yet (brief of KNU-EWTW-NRG-001-04) |
| 480.9 | Laboratory pack, 25 cycles | 515 · 88 · 0 | source | Research record of 2026-11-14, statement 11 |
| 650 | Assumption of a NASA study | 860 · 276 · 0 | source | Research record of 2026-11-14, statement 8, as reported |
| 1000 | Level one study needs for economic feasibility | 1575 · 666 · 223 | source | Research record of 2026-11-14, statement 6 |

### Option C — both: the battery flies a share of the trip, fuel flies the rest and the reserves

| Mission | Battery share | Pack needed Wh/kg, favourable · nominal · unfavourable | Mass t at 170 · 480.9 · 650 · 1000 | Fuel burned against option B at 170 · 480.9 · 650 · 1000 |
|---|---:|---:|---:|---:|
| S | 10% | 45 · 89 · 188 | 38.3 · 30.5 · 29.6 · 28.8 | +34% · +7% · +4% · +1% |
| S | 25% | 110 · 218 · 449 | over · 36.0 · 33.2 · 30.8 | — · +14% · +5% · -3% |
| S | 50% | 216 · 421 · 833 | none · 51.8 · 41.5 · 34.7 | — · +35% · +8% · -10% |
| M | 10% | 96 · 209 · 547 | over · 37.9 · 35.3 · 33.1 | — · +21% · +12% · +5% |
| M | 25% | 233 · 498 · 1204 | none · over · 47.9 · 38.9 | — · — · +34% · +9% |
| M | 50% | 449 · 921 · 2004 | none · none · over · 54.9 | — · — · — · +18% |
| L | 10% | 187 · 476 · 2423 | none · 59.5 · 49.4 · 42.3 | — · +64% · +37% · +17% |
| L | 25% | 448 · 1070 · 3863 | none · none · over · over | — · — · — · — |
| L | 50% | 833 · 1830 · 4763 | none · none · none · over | — · — · — · — |
| X | 10% | 1432 · none · none | none · none · none · none | — · — · — · — |
| X | 25% | 2725 · none · none | none · none · none · none | — · — · — · — |
| X | 50% | 3849 · 15716 · none | none · none · none · none | — · — · — · — |

*over* means that the mission needs more than the take-off mass limit, and *none* that no take-off mass flies it. Masses are at nominal values. *Fuel burned against option B* compares kilograms of fuel on the same mission at nominal values: a plus sign means that the aircraft with a battery burns more.

### Parameters

| Parameter | Favourable | Nominal | Unfavourable | Basis | Note |
|---|---:|---:|---:|---|---|
| lift_to_drag | 22 | 18 | 16 | assumption | — |
| propulsor_efficiency | 0.88 | 0.85 | 0.8 | assumption | — |
| electric_chain_efficiency | 0.93 | 0.9 | 0.87 | assumption | From the terminals of the battery or of the generator to the shaft. A manufacturer states above 95 % for motor and electronics at cruise (statement 15) |
| turbogenerator_efficiency | 0.4 | 0.35 | 0.3 | assumption | From fuel to electricity |
| pack_usable_share | 0.85 | 0.72 | 0.65 | assumption | Nominal is 0.90 usable times 0.80 at the end of service life, as in ELA-EWTW-ESS-001 |
| empty_fraction_A | 0.46 | 0.52 | 0.58 | assumption | — |
| empty_fraction_B | 0.55 | 0.6 | 0.65 | assumption | — |
| empty_fraction_C | 0.56 | 0.61 | 0.66 | assumption | — |
| takeoff_kw_per_kg | 0.16 | 0.2 | 0.25 | assumption | — |

| Figure | Value | Basis | Source or note |
|---|---:|---|---|
| payload.kg_per_passenger | 95 | assumption | — |
| reserves.contingency_share | 0.05 | assumption | — |
| reserves.alternate_km | 185 | assumption | — |
| reserves.final_reserve_min | 30 | source | Regulation (EU) 2021/1296, CAT.OP.MPA.181(c)(5), for turbine-engined aeroplanes; research record of 2026-11-14, statement 2 |
| reserves.holding_speed_kmh | 400 | assumption | — |
| flight.cruise_altitude_m | 7600 | assumption | — |
| flight.cruise_speed_kmh | 500 | assumption | — |
| flight.descent_recovery_share | 0.5 | assumption | — |
| units.motor_kw | 750 | source | Research record of 2026-11-14, statement 15: offered rating of a motor tested in the laboratory |
| units.turbogenerator_kw | 1000 | source | Research record of 2026-11-14, statement 16, as reported: in development |
| fuel_energy_mj_per_kg | 43 | assumption | Lower heating value commonly used for jet fuel; not read at a source |
| takeoff_mass_limit_kg | 60000 | assumption | In-service types of about 100 seats are certificated at about 56 to 63 t; not read at a source |

### Assumptions

| Id | Assumption |
|---|---|
| A1 | The aircraft carries 100 passengers. The mass taken for each, with baggage, is an assumption until the standard masses of the air operations rules are read |
| A2 | A mission closes when the take-off mass it needs stays within the limit, which stands for the take-off mass of in-service types of the class |
| A3 | The empty mass, without payload and without energy carrier, is a fixed share of the take-off mass for each option. The share is higher where the aircraft carries turbogenerators as well as motors |
| A4 | Reserves are flown as distance at the cruise lift-to-drag ratio — the contingency as a share of the trip, the alternate as a distance, the final reserve as time at holding speed |
| A5 | The final reserve of an aeroplane with electric engines is taken as that of a turbine-engined one. The rule names no time for it (research record of 2026-11-14, statement 2) |
| A6 | Take-off and climb cost the energy to reach cruise speed and altitude. A share of the height is recovered in the descent |
| A7 | A battery delivers its specific energy reduced by one share, which covers the capacity held back and the capacity lost at the end of service life |
| A8 | In option C the battery supplies a stated share of the trip energy, and fuel supplies the rest of the trip and all the reserves |
| A9 | Option B loses the mass of the fuel it burns; the test credits it with the logarithmic form of the range equation. Options A and C are credited with no loss of mass for the battery |
| A10 | Take-off shaft power is a fixed power for each kilogram of take-off mass. Units are counted at the ratings that the research record gives for a motor and for a turbogenerator |
<!-- screening:end -->

---

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-14 | First issue: three candidate missions and one reference, four pack levels, three sets of parameters |
