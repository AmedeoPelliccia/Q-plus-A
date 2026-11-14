# Audit record — first-order closure of the candidate missions

| | |
|---|---|
| KNOT | `KNOT-EWTW-NRG-001` Energy carrier |
| Serves | `KNU-EWTW-NRG-001-02` · `KNU-EWTW-NRG-001-03` |
| Subject | [`MSN-EWTW-NRG-001`](MSN-EWTW-NRG-001/README.md) 0.1.0 |
| Produced by | An audit relayed by the author on 2026-11-14. The relay does not name its author |
| Reviewed by | Claude, 2026-11-14 |
| Outcome | The main finding is accepted. The analysis is reissued as 0.2.0 |

This record keeps what the review accepted from the audit, what it did not, and what changed in the analysis. It states no conformity of the eWTW with any rule.

---

## Accepted

| # | Finding of the audit | Read by the reviewer on 2026-11-14 | Effect on 0.2.0 |
|---|---|---|---|
| 1 | The take-off masses of 27 to 33 t closed the model, not an aircraft of the class. The model was not anchored to an in-service type of 100 seats | Embraer 190 specification sheet: basic operating weight 27,753 kg, maximum take-off weight 50,300 kg (LR) and 51,800 kg (AR). *Aircraft Commerce*, issue 64: take-off masses of 40.5 to 43.0 t on sectors of 383 to 1,245 km with 114 seats | The airframe is that of the reference: its empty mass and its take-off mass limit |
| 2 | The model has to reproduce the published block fuel of the type before its results are used to choose a carrier | *Aircraft Commerce*, issue 64, June/July 2009: six sectors with block fuel, block time and take-off mass, from flight plans at long-range cruise | The energy is fitted to the six sectors, within about 1 %, and checked on the published range of the type, within 7 % |
| 3 | One cruise point, lower and slower than the class, underestimates the short stages most, where climb weighs most | The fit: the terminal phases cost the reference as much fuel as 483 km of cruise | The fitted distance replaces a climb term derived from height and speed, which gave 86 km |
| 4 | The pack of a type-certificated two-seat aeroplane is published, and it is of another class | Pipistrel, Velis Electro product page: two batteries, 24.8 kWh in total, about 70 kg each | 177 Wh/kg replaces an assumption of 170. Its label says what it is. Maturity record `Q1` is restated |
| 5 | A take-off power of 5 to 7 MW belongs to an aircraft of about 30 t | — | At the masses of 0.2.0 the test gives 8 to 9 MW at nominal values |
| 6 | Mission M is an average stage, not the design mission of the class | Embraer 190 specification sheet: a range of 2,400 nm for the LR with full passengers | The proposal says so. The reference mission is the range the reference type is offered with |
| 7 | That a stage of 500 km is flown as twice its length is an output of the model, not a rule | — | The README says where the distance comes from: the fitted terminal phases and the reserves assumed |
| 8 | The comparison of option C with option B is incomplete, and part of the mass penalty of C came from the way it was calculated | The sensitivity of 0.2.0 | A table shows the result at three shares of empty-mass growth. The finding on option C is reworded |

## Not accepted, or not read

| Content of the audit | Reason |
|---|---|
| A maximum take-off mass of 45,995 kg and a cruise of Mach 0.78 at 460 kt for the type, from a EUROCONTROL database | The reviewer could not read the page. The sheet of the manufacturer gives 50,300 and 51,800 kg for the versions it lists, and Mach 0.82 as maximum cruise |
| A range of 1,850 nm from a brochure of June 2014 | Not read. The sheet read gives 2,400 nm for the LR and 2,450 nm for the AR |
| That an aircraft of the class weighs one and a half times the limit the model had set, and that the model burned tens of kilograms | The limit of 0.1.0 was 60 t, above the take-off masses of the reference, and 0.1.0 gave 1.2 to 3.8 t of fuel. Finding 1 stands without them |
| Block fuel converted at 0.80 kg/L, on two sectors | The source gives six sectors with their take-off masses, and the manufacturer states a density of 6.70 lb for each US gallon. 0.2.0 uses both |
| Shares of fuel by flight phase, average fuel flows of a mixed regional fleet, an estimate of secondary power of 2005, a note of a lessor | Not read, and not used |
| A motor test above 1 MW in a climate chamber in 2021, a fuel saving of 18 % for a turbogenerator, generator ratings of wide-body types, a pack band of 150 to 170 Wh/kg | Already not accepted in the [record of the energy carrier](KNOT-EWTW-NRG-001_energy-carrier_2026-11-14.md), for the reasons given there |

## Open

- **A second reference type.** The fit rests on one type and one publication. The audit names a second type of the class; its block fuel with take-off masses would test the fit.
- **The flight condition of the eWTW.** Its speed and its altitude are not defined, so the share of the terminal distance it takes is an assumption.
- **The empty mass of each option.** The test gives the three options the empty mass of the reference.
