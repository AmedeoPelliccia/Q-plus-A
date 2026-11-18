# Research record — the wings now in service, propellers at the wingtip, and the braced wing

| | |
|---|---|
| KNOT | `KNOT-EWTW-WNG-001` Wing planform: span, aspect ratio and area |
| Serves | `KNU-EWTW-WNG-001-01`. It gives inputs to `-02`, to `KNOT-EWTW-MAS-001` and to `KNOT-EWTW-PRP-001` |
| Produced by | Claude, 2026-11-18, at the request of the authority, by reading the sources named. The same hand researched and reviewed: no second reader has checked this record |
| Brief | The research brief of `KNU-EWTW-WNG-001-01`, register 0.11.15, and the points the [record of 2026-11-17](KNOT-EWTW-WNG-001_wings-and-span-limits_2026-11-17.md) left open |
| Read | Six statements read at the source on 2026-11-18, three findings of absence |

This record adds to the record of 2026-11-17, and corrects one of its consequences. It is a reading of public sources, written in our own words. It recommends no option.

---

## Read at the source

| # | Statement | Source | Kind |
|---|---|---|---|
| 1 | The Embraer E190-E2 has a span of 33.72 m and the E195-E2 of 35.12 m. Both have a wing reference area of 103 m² and a reference aspect ratio of 9.4. Their maximum take-off masses are 56,400 kg and 61,500 kg, and their maximum usable fuel 13,500 kg and 13,690 kg | Embraer, Airport Planning Manual of the E-Jets E2, APM-5824, revision 25 of 29 November 2024, section 2 | Manufacturer |
| 2 | The Airbus A220 has a wing area of 112.3 m², by the definition that includes the area within the fuselage. The maximum take-off mass of the A220-100 is 63,730 kg for most serial numbers | Airbus, A220 Aircraft Characteristics Publication, issue 003-01 of 23 May 2024 | Manufacturer |
| 3 | A propeller mounted at the wingtip, turning against the tip vortex, was compared in a wind tunnel with the same propeller mounted inboard. At a lift coefficient of 0.5 and a thrust coefficient of 0.09 to 0.13, the drag of the wing is 5 to 15 % lower, 15 to 40 counts. At a lift coefficient of 0.7 and higher thrust it is 25 to 50 % lower. With the propeller off, the wingtip layout has the higher drag. The test ran at 40 m/s, at a Reynolds number of about 650,000, on a model of low aspect ratio with a propeller of 0.237 m. The authors did not study the structure, the failure of one engine or aeroelasticity, and write that the benefit for an aircraft needs a multidisciplinary analysis | Sinnige, van Arnhem, Stokkermans, Eitelberg and Veldhuis, *Wingtip-Mounted Propellers: Aerodynamic Analysis of Interaction Effects and Comparison with Conventional Layout*, Journal of Aircraft 56(1), 2019, Delft University of Technology | Wind tunnel, small scale |
| 4 | The EcoPulse demonstrator flew about 100 hours in about 50 flights, between 29 November 2023 and July 2024, with a network of about 800 V and 350 kW. The partners report that phasing the propellers can reduce the noise in the cabin, and that the flight control computer can steer the aircraft by the power it gives to each propeller. They list as challenges the batteries, the management of voltages above 400 V, weight and noise, and the complexity of the system. The text read reports no aerodynamic gain | CompositesWorld, report of the end of the campaign, announced by Daher, Safran and Airbus on 10 December; the page gives no year, and the dates of the flights place it in 2024 | Secondary; flight campaign |
| 5 | A handbook method for the mass of a wing takes a braced wing as 30 % lighter than a cantilever one, the brace being about a tenth of the wing mass. It takes 5 % off for two engines on the wing and 10 % off for four. The ratio of the structural span to the root thickness is about 40 for cantilever wings and about 70 for braced ones | Scholz, *Aircraft Design* lecture notes, chapter 10, after Torenbeek, Hamburg University of Applied Sciences | Handbook method |
| 6 | A project of the Clean Aviation programme studies a strut-braced composite wing of high aspect ratio, with morphing edges, for a successor of the regional turboprops | FlightGlobal, 5 September 2024, headline and lead only | Secondary |

### Findings of absence

| # | Statement |
|---|---|
| 7 | No figure for the braced wing of statement 6: the article is behind a paywall, and no report of the project was read |
| 8 | No aerodynamic result of the flight campaign of statement 4, in what was read |
| 9 | No test of wingtip propellers at the Reynolds number, the aspect ratio or the power of an aircraft of 100 seats |

---

## What follows for the eWTW

Figures in this section that are not in a statement above are arithmetic of the reviewer.

- **A correction to the record of 2026-11-17.** It said that the class is well inside code letter C, on three types with spans of 27 to 29 m. Those are the types of the previous generation. The jets now in production span 33.72 m and 35.12 m (statement 1), and the limit stops short of 36 m. The class has already used the room. The record of 2026-11-17 carries a dated note.
- **The class has moved to an aspect ratio of 11 to 12.** The square of the span over the reference area is 11.0 for the E190-E2 and 12.0 for the E195-E2; the manual gives a reference aspect ratio of 9.4, which answers to a reference span of 31.1 m. The same ratio was 8.9 for the Embraer 190. Option A of this KNOT, the aspect ratio of the class, is this value and not that of the older wing.
- **On a jet-size wing the limit of letter C now binds.** With 103 m², a span just under 36 m gives 12.6. A higher aspect ratio inside the letter needs a smaller wing: 14 at 92.5 m², 21 at 61 m². Option B is open only to a design that needs less wing area, which the cruise point decides.
- **The wings in service carry 550 to 600 kg/m² and 131 kg of fuel for each square metre.** 548 kg/m² for the E190-E2, 597 kg/m² for the E195-E2, 567 kg/m² for the A220-100. These are the references of `KNU-EWTW-WNG-001-02` for a jet cruise; the turboprop wing of the earlier record carries 377 kg/m².
- **Wingtip propellers: a gain in a wind tunnel, none shown in flight.** The measured gain is on the drag of the wing, at small scale, and it becomes a loss with the propeller off (statement 3). The flight campaign on record reports no aerodynamic result (statement 4). The screening gives no credit for it at nominal values. The coupling with `KNOT-EWTW-PRP-001` stays an assumption.
- **Motors along the span relieve the wing.** The handbook takes 5 to 10 % off the wing mass for engines on the wing (statement 5). That is a gain in mass that distributed propulsors can claim without a new aerodynamic effect, and it belongs to the mass by option (`KNOT-EWTW-MAS-001`).
- **A slower cruise is what lets the aspect ratio rise inside the same span.** The study of the D8 holds the span at 118 ft, 36.0 m, and goes from an aspect ratio of 10.59 to 13.29 by cruising at Mach 0.72 with a wing of low sweep ([record of the wide sections](KNOT-EWTW-FUS-001_wide-sections-and-hydrogen-tanks_2026-11-18.md), statement 7). This is the coupling with `KNOT-EWTW-CRZ-001` in figures, at another size and by calculation.

These are consequences drawn by the reviewer. They are not quotations.

## Open

Research can still give:

- the wing area of the Dash 8-400, and the span of the Airbus A220 with its label;
- the take-off and landing field lengths of the Embraer 190 and of the E2, which the manuals give as charts;
- the results of the Clean Aviation project of statement 6, in its own reports;
- the aerodynamic results of the EcoPulse campaign, if the partners publish them.

The rest is work of the programme:

- the wing area and the span each cruise point gives, and the fuel the box holds (`KNU-EWTW-WNG-001-02`).
