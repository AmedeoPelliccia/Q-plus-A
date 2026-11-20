# Research record — the certified carbon dioxide metrics of EASA

| | |
|---|---|
| KNOT | `KNOT-EWTW-AER-001` Drag polar of the configuration |
| Serves | `KNU-EWTW-AER-001-01` and `KNU-EWTW-AER-001-02`; criterion `M5` of `KNOT-EWTW-CRZ-001` |
| Produced by | Claude, 2026-11-18, from the file the authority attached that day. The same hand read and reviewed: no second reader has checked this record |
| Source | EASA, *Aeroplane CO2 Emissions Database*, issue 12 of 30 September 2026, a spreadsheet of two sheets. The file itself is not in the repository |
| Read | Seven statements read in the file, four findings of absence |

Three records asked for this file and could not open it: the [drag data](KNOT-EWTW-AER-001_drag-data-and-forecasts_2026-11-17.md) of 2026-11-17, the [drag method](KNOT-EWTW-AER-001_drag-method-and-forecasts_2026-11-18.md) and the [technology goals](KNOT-EWTW-AER-001_icao-technology-goals_2026-11-18.md) of 2026-11-18. The authority attached it. It holds one turboprop and no regional jet of the generation the ICAO experts took as reference. The turboprop is the ATR 72-212A with PW127XT-M engines. The reviewer takes it as the ATR 72-600 of the other records, which is sold under that name; the file does not say so.

---

## Read in the file

| # | Statement | Kind |
|---|---|---|
| 1 | Issue 12 holds 113 records. Each gives the type and its variant, the maximum take-off mass, the engines and the propellers, the date of certification, the metric value in kg/km, the in-production limit and the new-type limit at that mass, and the metric as a percentage of each limit. It gives no reference geometric factor and no specific air range. Every record is certified against the in-production limit of CAEP/10; none against the new-type limit | Regulator |
| 2 | The ATR 72-212A with PW127XT-M engines and 568F-1 propellers is certified at a maximum take-off mass of 23,000 kg with a metric value of 0.404 kg/km. The in-production limit there is 0.525 kg/km and the new-type limit 0.507 kg/km: the metric is 77.0 % of the first and 79.7 % of the second. Certified on 3 June 2025, record `CO200040`. It is the only propeller-driven aeroplane in the file | Regulator |
| 3 | The Airbus A220-100 (BD-500-1A10), with PW1519G, PW1521G or PW1524G engines, is certified at 63,730 kg with a metric value of 0.677 kg/km, 88.6 % of a new-type limit of 0.764 kg/km. The A220-300 (BD-500-1A11) is certified at 70,896 kg with 0.731 kg/km, 95.3 % of a new-type limit of 0.767 kg/km. Both on 6 February 2026, records `CO200085` to `CO200090` | Regulator |
| 4 | Against the new-type limit, the other Airbus types stand at: A320neo, 73.5 to 79 t, 90.4 to 92.1 %; A319neo 94.1 to 95.3 %; A321neo, 89 to 97 t, 92.8 to 95.5 %; the A321 of 97 to 101 t (A321-253NY and -271NY) 95.0 to 96.5 %; A330-900 92.1 to 94.8 %; A330-800 94.7 to 97.3 %; A350-900 93.3 to 94.9 %; A350-1000 94.3 to 95.6 % | Regulator |
| 5 | Three business jets: the Falcon 8X, at 33,112 kg, stands at 93.9 % of the new-type limit; the Falcon 2000LXS, at 19,414 kg, at 90.2 %; the Challenger 650, at 21,863 kg, at 103.2 % of the new-type limit and 99.6 % of the in-production limit | Regulator |
| 6 | The notes of the file say that the date of certification is the later of the completion of the certification and of the approval of the type or of the modification; that EASA CS-CO2 was repealed by ED Decision 2025/005/R of 26 May 2025; and that *the CO2 MV as defined in ICAO Annex 16 does not correspond to specific emissions or fuel burn per km range* | Regulator |
| 7 | The new-type limits the file prints for its four types below 60,000 kg are 0.507, 0.594, 0.471 and 0.496 kg/km, at 23,000, 33,112, 19,414 and 21,863 kg. The limit formula that the screenings hold, from a copy of the Annex, gives 0.507, 0.594, 0.471 and 0.496 | Arithmetic of the reviewer on the file |

### Findings of absence

| # | Finding |
|---|---|
| 8 | No Embraer type, no Dash 8-400 and no ATR 42 in the file. The E190-E2, the reference of the ICAO experts for regional jets, has no certified value in it |
| 9 | No reference geometric factor. Statement 7 of the [record of 2026-11-17](KNOT-EWTW-AER-001_drag-data-and-forecasts_2026-11-17.md), as reported, said that each entry gives one and that the file holds recent regional jets and some turboprops: neither is so |
| 10 | No specific fuel consumption of the PW127XT-M in cruise, in what was read. The certified metric gives the product of the efficiency and of the lift-to-drag ratio of the type, and not each of them |
| 11 | No lift-to-drag ratio and no engine efficiency for the A220 |

## What follows for the eWTW

Figures in this section that are not in a statement above are arithmetic of the reviewer, in the [screening of the configurations](CFG-EWTW-AER-001/README.md), which now carries the two types as checks. The floor of each type is not in the file: it is computed by the cabin rule of the screening, and a floor 10 % larger or smaller moves the products below by 2 %.

- **A turboprop in service stands 20.3 % below the new-type level.** The objective of 26 % asks 7 % less metric than the ATR 72-212A as certified in 2025.
- **The jets nearest to the class stand 11.4 % and 4.7 % below.** The margin of the A220-100 is the one the ICAO experts give to their regional-jet reference of 2017, the E190-E2, which is not in the file. Where the references of the experts are certified, the certified values are better than their models: 8 to 10 % below the level for the A320neo, where the experts have 4 %; 5 to 7 % for the A350-900, where they have 4 % ([record of the technology goals](KNOT-EWTW-AER-001_icao-technology-goals_2026-11-18.md), statement 2).
- **The limit formula of the screenings is confirmed** on four certified types (statement 7).
- **On the scale of the screening the two types are far apart, and the turboprop is the lower.** The certified metric of the ATR 72-212A is a product of efficiency and lift-to-drag of 4.14, with a floor of 54.5 m². That of the A220-100 is 6.03, with a floor of 87.1 m². The turboprop stands better on the metric because it is light: 422 kg of take-off mass for each square metre of floor, against 732.
- **The nominal chain of the eWTW has the efficiency of the turboprop in service.** If the best lift-to-drag ratio of the ATR 72 is the 15.74 of the statistic the propeller points are set on, the certified type turns 0.263 of the energy of its fuel into thrust work. The nominal chain of the screenings turns 0.268: a thermal machine better than the engine of the type, and an electrical chain that takes the difference back. With the drag set on the same type, the nominal eWTW then differs from the certified turboprop by its mass alone: 629 to 724 kg for each square metre of floor.
- **What the objective asks is between the two.** For the best aircraft of the second and third technology sets, at 38 to 39 t and 79 m², the objective asks a product of 5.4 to 5.5: a third more than the turboprop certified in 2025 has, and less than the jet certified in 2026 has. The file does not say why the jet has the higher product (finding 11).
- **The cruise at speed costs about a tenth, on the type itself.** The factsheet on record gives 638 kg for a block of 200 nm and 879 kg for one of 300 nm, at 275 kt ([record of the cruise point](KNOT-EWTW-CRZ-001_cruise-point_2026-11-15.md), statement 1): 1.30 kg for each kilometre more. The certified metric is 1.05 kg/km at the mean of its reference masses, 19.1 t. If the blocks are flown at 21 to 22 t, which the factsheet does not say, the cruise at 275 kt costs 7 to 12 % more than the condition of the metric, at equal mass. The polar the screening sets on the type gives it 4 to 15 % less lift-to-drag at 275 kt than at its best, between 24,000 and 17,000 ft, and 10 % at 20,000 ft. The factsheet is of 2020, before the engine of the certified aeroplane.
- **The statistic is not replaced, it is bounded.** The record of the objective expected the file to replace the best ratio of 15.74. It gives the product, and the product agrees with that ratio if the engines of the type turn about 31 % of the energy of the fuel into shaft work, with the propeller efficiency of 0.86 of the same source. That consumption was not read (finding 10).

These are consequences drawn by the reviewer. They are not quotations.

## Not accepted

| Claim | Why |
|---|---|
| That the file gives the reference geometric factor of each type, and holds the regional jets of the class | It does not (findings 8 and 9). The claim was recorded as reported on 2026-11-17 |

## Open

- the specific fuel consumption of the PW127XT-M in cruise, which would turn the certified metric into a best lift-to-drag ratio of the type;
- the reference geometric factors of the ATR 72-212A and of the A220-100, which the applicants hold;
- the certified values of the E190-E2 and of the Dash 8-400, when they enter the file: certification is required of all aeroplanes in production from 1 January 2028.
