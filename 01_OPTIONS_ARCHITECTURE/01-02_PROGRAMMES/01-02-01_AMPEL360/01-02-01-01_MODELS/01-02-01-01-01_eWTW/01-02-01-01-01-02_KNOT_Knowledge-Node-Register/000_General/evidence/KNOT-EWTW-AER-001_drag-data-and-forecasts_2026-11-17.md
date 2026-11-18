# Research record — published drag data and forecasts for the class

| | |
|---|---|
| KNOT | `KNOT-EWTW-AER-001` Drag polar of the configuration |
| Serves | `KNU-EWTW-AER-001-01`. It gives inputs to `-02` and to criterion `M5` of `KNOT-EWTW-CRZ-001` |
| Produced by | A research report of 2026-11-17, relayed by the author. The report does not name its producer |
| Brief | The research brief of `KNU-EWTW-AER-001-01`, register 0.11.14 |
| Reviewed by | Claude, 2026-11-17 |
| Accepted | Three statements read by the reviewer, four as reported, four findings of absence |

This record keeps what the review accepted from the research report. It is a reading of public sources, written in our own words. It recommends no option.

The report gives one range of lift-to-drag ratios without a source, and no figure from a forecast. The reviewer read one study of NASA that computes a lift-to-drag ratio for an advanced tube-and-wing of 98 seats, and the page of the database of EASA.

---

## Accepted content

### A computed lift-to-drag ratio for the class

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 1 | NASA computed an advanced tube-and-wing of 98 passengers for 2,400 nm at Mach 0.78. Its lift-to-drag ratio at the start of cruise is 19.8. The aircraft has hybrid laminar flow control on the wing and the tail, natural laminar flow on half the length of the nacelles, composite structure taken 23.5 % lighter than metal for the wing and tail and 14.5 % lighter for the fuselage, an aspect ratio held to 11.0 at most, and engines of a thrust specific fuel consumption of 0.49. The study aims at technologies that could reach readiness level 6 by 2020. The aircraft was sized with the FLOPS code of NASA; nothing is measured | Nickol, *Hybrid Wing Body Configuration Scaling Study*, NASA Langley Research Center, 2012 (NTRS 20120001452) | 2026-11-17 |
| 2 | The same study models the ERJ190 on that mission, with a payload of 21,605 lb: a take-off weight of 114,552 lb, an empty weight of 64,300 lb and a block fuel of 23,800 lb. The advanced tube-and-wing burns 12,520 lb, weighs 91,700 lb at take-off and 55,000 lb empty. The study gives no lift-to-drag ratio for its model of the ERJ190 | The same study | 2026-11-17 |

### Certified values of the carbon dioxide metric

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 3 | EASA publishes the EASA Aeroplane CO₂ Emissions Database: the values of the carbon dioxide metric of aeroplanes as EASA certified them under ICAO Annex 16 Volume III. The current file is issue 12, a spreadsheet, and the page was last updated on 6 October 2026. A type enters the database when its certification is complete. Certification is required of new designs from 1 January 2020, and of all aeroplanes in production from 1 January 2028. The reviewer could not open the file | EASA, page of the EASA Aeroplane CO₂ Emissions Database | 2026-11-17 |

### As reported

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 4 | The lift-to-drag ratios cited for regional jets in cruise, near Mach 0.78 and 35,000 ft, lie between 14 and 17 | The report, from design handbooks and literature it does not name | As reported |
| 5 | The handbooks of Torenbeek, Roskam and Raymer give ranges for the equivalent skin-friction coefficient and for the span efficiency factor of transport aircraft | The report | As reported: no value and no page is given |
| 6 | ICAO Doc 10127 and the technology appendix of the report on the long-term aspirational goal set technology goals for 2027, 2037 and 2050, with forecasts of lift-to-drag ratio and of engine efficiency for regional jets and turboprops | The report | As reported: neither the report nor the reviewer could open the documents |
| 7 | The database of statement 3 holds recent regional jets and some turboprops, and each entry gives the metric value, the maximum take-off mass and the reference geometric factor | The report | As reported: the entries were not read |

### Findings of absence

| # | Statement |
|---|---|
| 8 | No table in the documents of the manufacturers that gives lift-to-drag ratio with Mach number, altitude and mass for the Embraer 190, the ATR 72-600 or the Dash 8-400 |
| 9 | No single public table of wetted areas by component for aircraft of 70 to 130 seats |
| 10 | No measured polar of a lifting fuselage or of a wing of high aspect ratio near 100 seats |
| 11 | No full text of ICAO Doc 10127 or of the technology appendix available to the search |

---

## What follows for the eWTW

Figures in this section that are not in a statement above are arithmetic of the reviewer.

- **A published computation puts the class above the lift-to-drag ratio the minimum objective needs.** The [screening of the cruise points](CRP-EWTW-CRZ-001/README.md) uses 15, and finds that about 18.4 would close the gap to the minimum objective by itself. Statement 1 computes 19.8 for 98 seats. The two are not the same quantity: 19.8 is at the start of cruise, on an aircraft with laminar flow control that no regional type in service has, and it is calculated. It is a forecast of what the airframe could give, not evidence that it does.
- **The same study cuts the fuel of its reference by 47 %.** Its advanced tube-and-wing burns 12,520 lb where its model of the ERJ190 burns 23,800 lb (statement 2). The cut comes from the airframe, the engines and the lower mass together; how the study splits it was not read. It is the only figure on record for what the technologies of a forecast do to the fuel of this class.
- **The polar cannot be checked against a published lift-to-drag ratio.** No manufacturer publishes one with its conditions (finding 8), and the range of statement 4 has no source. The check of `KNU-EWTW-AER-001-02` has to go through fuel: the polar, with an engine, has to return the fuel a manufacturer publishes for a stated mission.
- **Drag has to be carried with mass.** The blended body of the same study gains in lift-to-drag ratio and burns more fuel, because it is heavier ([record of the sections and cabins](KNOT-EWTW-FUS-001_sections-and-cabins_2026-11-17.md), statement 4). The screening that uses the polar has to carry the empty mass each option changes.
- **The certified values exist, and the class may not be in them yet.** Types in production need no certification before 2028 (statement 3), so the Embraer 190, the ATR 72-600 and the Dash 8-400 may be absent. The file settles it. It is a spreadsheet the reviewer could not open; the author can attach it.
- **The forecasts of ICAO are still unread.** They are the source for the levels the technologies are expected to reach by 2027 and 2037. This is the second search that could not open them. *Note of 2026-11-18: a third could not either ([record of 2026-11-18](KNOT-EWTW-AER-001_drag-method-and-forecasts_2026-11-18.md), finding 5).*

These are consequences drawn by the reviewer. They are not quotations.

## Not accepted

| Content of the report | Reason |
|---|---|
| That turboprops have higher lift-to-drag ratios, consistent with the lower induced drag of propeller propulsion | A propeller does not lower induced drag, and no value or source is given. The turboprop wing read has an aspect ratio of 12.0 against 8.1 ([record of the wings](KNOT-EWTW-WNG-001_wings-and-span-limits_2026-11-17.md)) |
| That the zero-lift drag from the handbook ranges, applied to a tube-and-wing of the size of the reference type, is consistent with a lift-to-drag ratio of 15 | No calculation is shown. That calculation is `KNU-EWTW-AER-001-02` |
| That a lift-to-drag ratio of about 16.5 to 18 would close most of the gap to the minimum objective, with modest gains in the turbogenerator | Not a finding of the research. The screening on record gives 18.4 for the lift-to-drag ratio alone |
| Goals of ICAO of several per cent in each decade | No summary is named and no figure is given |
| That the certified values of the types of the class provide the comparison | It is not shown that the class is in the database (statement 3) |
| The lift-to-drag ratios of concepts between a tube-and-wing and a blended wing body as higher than the baseline | No study is named. The braced wing read is in the record of the wings, statements 5 and 6 |

## Open

Research can still give:

- the entries of the database of EASA for the types of the class: metric value, maximum take-off mass and reference geometric factor;
- the goals of ICAO Doc 10127 for regional jets and turboprops in 2027 and 2037, read in the document;
- the handbook ranges of statement 5, with their values and pages;
- the fuel a manufacturer publishes for a stated mission, with payload, distance, speed and altitude, for the check of the polar.

The rest is work of the programme:

- the dimensions and areas of record (`KNU-EWTW-AER-001-03`);
- the polar of the eWTW at each cruise point, with the empty mass each option changes (`KNU-EWTW-AER-001-02`).
