# Research record — supply at the stand, start of a gas turbine, auxiliary units

| | |
|---|---|
| KNOT | `KNOT-EWTW-AUX-001` Auxiliary power and supply at the stand |
| Serves | `KNU-EWTW-AUX-001-01`. It gives `-02` its inputs on the stand and on a start, and `-03` seven criteria, drawn from certification, from rules and from two precedents |
| Produced by | Two research reports of 2026-11-26 on one brief. **A**: Claude, on the nine questions of the three KNUs. **B**: relayed by the author as produced with Grok, on the five questions of `-01`. Then an assessment of both by the reviewer, who read further sources for it, and a second reading of report A, relayed by the author, which does not name its producer. None of the four is filed here; report A and the assessment hold the links to the sources |
| Brief | The brief of the three KNUs as the register defines one: `model-context.yaml`, the KNOT and each KNU, as on pull request 75, register 0.11.26. The reviewer found no issue of the repository that carries it |
| Reviewed by | Claude, 2026-11-26. The reviewer is the producer of report A |
| Accepted | Thirty-seven statements: three read by two readers, one of them in part; thirty-four by the reviewer, thirteen of which the second reading endorses. Twelve more as reported, and twelve findings of absence. Proposed, not ratified |
| Figures | Unit conversions and three products, shown where they are used. No analysis folder holds them yet |

This record keeps what the review accepted from the two reports, from the assessment and from the second reading. It is a reading of public sources, written in our own words. It recommends no option, and it states no conformity of the eWTW with any rule.

**Safety first.** Nothing here ranks an option or sizes a unit. Three statements bear on persons before they bear on performance: a machine left running at the stand has people around it (statement 23); a battery that starts an auxiliary unit has a fire on record, on the ground (statement 37); and a start on batteries alone is avoided where an investigator describes it (statement 14). What certification asks of a unit depends on whether the aircraft needs it to fly, not on what it does at the stand (statement 33).

**Who read what.** In the last column of each table, *two readers* means that the reviewer and another reader each read the place cited, on their own: here the other reader is report B. *Reviewer* means the reviewer alone. *Endorsed* means that the second reading calls the statement correct. That second reading names no place it read, found none of the eight corrections the reviewer made to report A, and credits report A with one statement it does not make; its endorsement is recorded and is not counted as a reading. *As reported* means the reviewer did not read the source itself. The reviewer read through a tool that answers questions on a text and does not return it; every figure is to be read again at the document before it is used.

**Words.** The sources say *auxiliary power unit* for a gas turbine that drives no propulsor. The model says *auxiliary power module* at `049` and does not determine its technology. Each word is kept where it belongs. A rating in kVA is the ceiling of a power in kW.

---

## Accepted content

### Supply from the ground

| # | Statement | Source | Read |
|---|---|---|---|
| 1 | ISO 6858:2017, second edition, sets the output characteristics and the interface between an aircraft and ground electrical supplies, central or at the point of use, for a nominal 28 V DC and for 115/200 V or 230/400 V three-phase at 400 Hz, measured at the aircraft connector. A committee draft of a third edition is under review | ISO, catalogue pages of ISO 6858:2017, November 2017, and of ISO/CD 6858 | Two readers, of the abstract. The text of the standard was read by no one |
| 2 | ISO 1034:1973, confirmed in 2023, gives the ground air-conditioning connections of 127 mm and 203 mm | ISO, catalogue page of ISO 1034:1973 | Reviewer, of the abstract |
| 3 | The 737-600 to -900 have one electrical ground connection printed at 60 kVA, 200/115 V and 400 Hz, one conditioned-air port of 8 in and one pneumatic port of 3 in for the engine start and the packs. Their start curves assume a start of 90 s at sea level. The charts of conditioned airflow and of turnaround are images | Boeing, Next-Generation 737 Airplane Characteristics for Airport Planning, D6-58325-7, Rev C, October 2025, §5.4.8 and §5.5 | Reviewer |
| 4 | Ground power units on the market give 30 to 180 kVA of AC at 115/200 V and 400 Hz. DC units at 28.5 V give 400 A continuously and 1,600 A at the peak of a start, or 600 A and 2,000 A, with a current-limited start: 11 to 17 kW continuously and 46 to 57 kW at the peak | ITW GSE, page on the types of ground power units; AviationPros, product note on the Hobart GPU-400 and GPU-600, 26 June 2014 | Reviewer, of extracts |
| 5 | Point-of-use preconditioned-air units of 45 to 120 tons deliver 150 to 210 kg/min, which is 2.5 to 3.5 kg/s, at 10 kPa and down to 0 °C, through one or two outlets of 14 in, with an optional heater of 72 or 120 kW | ITW GSE, data sheet of the 3500 PCA, June 2023, Rev. B | Reviewer |
| 6 | At gates of San Francisco in 2019, regional jets — CRJ-200, CRJ-700, Embraer 175 — drew between 2 and 7 kW of ground power. Conditioned air is not in the meters | P. A. Antonelli, A Framework for Monitoring, Modeling, and Management of Airport Ground Power Systems During Aircraft Turnaround Operations, dissertation, University of California, Berkeley, 2023, §3.3.2 | Reviewer; endorsed |
| 7 | Regulation (EU) 2023/1804, Article 12, obliges airports of the TEN-T core and comprehensive networks to supply electricity to stationary aircraft at every contact stand by 31 December 2024 and at every remote stand by 31 December 2029. Remote stands may be exempted at airports under 10,000 commercial flight movements a year on a three-year average. From 1 January 2030 the electricity comes from the grid or is generated on site without fossil fuels. The article sets nothing for conditioned air and no rating | Regulation (EU) 2023/1804 of the European Parliament and of the Council, Article 12, read in German | Reviewer; endorsed |
| 8 | In a sample of 217 European airports of 2019, those under one million passengers a year have on average no contact gate and 4 remote stands; those of 1 to 5 million have 3 and 15; those of 5 to 15 million have 7 and 37. The study says it has no data on how many stands are already supplied | Oxera, for ACI EUROPE, Assessment of the impact of the Fit for 55 policies on airports, 30 May 2022, table 2.2 | Reviewer |

### The transport with electric packs

| # | Statement | Source | Read |
|---|---|---|---|
| 9 | The 787 has two forward ground power receptacles and one mid-aft, each of 90 kVA at 200/115 V and 400 Hz, and no pneumatic ground connection. Its engines normally start from the auxiliary power unit. With that unit inoperative, a start asks at least two ground units of 90 kVA at the forward receptacles; three are recommended, to shed less of ventilation, in-flight entertainment and cabin lighting | Boeing, 787 Airplane Characteristics for Airport Planning, D6-58333, Rev Q, October 2025, §5.4 and §5.5 | Two readers |
| 10 | The 787-8 has one conditioned-air port of 8 in, and the 787-9 and 787-10 have two. With the auxiliary unit in use no air-conditioning vehicle is needed. Air from the ground port bypasses the air cycle machines. The document takes 103 °F and 80 °F ambient for its charts of steady cooling, whose values are images. It does not say whether the packs can run on external power, nor how many ground units a normal turnaround needs | The same, §5.1, §5.4.2, §5.4.4, §5.4.6 and §5.6 | Two readers for the ports; reviewer for the rest |
| 11 | The 787 has two packs, one on each side, each with two cabin air compressors that work together | FAA, notice of proposed rulemaking on the cabin air compressors of the 787, Federal Register, 6 October 2017 | Reviewer, of an extract |
| 12 | The auxiliary power unit of the 787 gives 450 kVA at sea level, and starts and runs up to 43,100 ft, by its maker | Pratt & Whitney, page of commercial auxiliary power units, read 2026-11-26 | Reviewer |

### Start

| # | Statement | Source | Read |
|---|---|---|---|
| 13 | The ATR 42-500 and 72-212A have two engine-driven starter-generators, a main and an emergency battery, and two propeller-driven generators at wild frequency; the report on the 42-500 gives 28 V DC, 24 V and 115 V for them. The ATR 72 carries no auxiliary power unit. The engine of the ATR 72-600 is of 2,750 shp, 2,051 kW. No report read says which source starts an engine | AAIB, report AAIB-28601, ATR 42-500 G-LMRC, published 5 March 2026; AAIB, report AAIB-28713, ATR 72-212A G-CMFI, Bulletin 1/2024; ATSB, occurrence brief AB-2025-009, 24 March 2025; ATR, brochure of the ATR 72-600 | Reviewer |
| 14 | On the Saab 340B, engine starts are normally made with a ground power unit connected, because repeated battery starts can damage the batteries and shorten their life. The left engine is started first on external power; the right one is then started on power fed across from the left generator. A start can use the batteries alone, and in flight this cuts their endurance markedly. The operating manual does not say how much charge one start takes. The starter disengages at 55 % of gas-generator speed. With one generator failed, a crew thought of relighting the other engine on the batteries and decided against it | AAIB, report AAIB-27678, Saab 340B G-NFLB, 14 September 2021, Bulletin 10/2022 | Reviewer |
| 15 | The DHC-8-402 carries an auxiliary power unit with a starter/generator tied to the right main bus. In the event read it was running before the engine start and was switched off after it. The bulletin does not say what starts the engines | AAIB, Bulletin 6/2020, DHC-8-402 G-PRPH | Reviewer |
| 16 | On the 787, a battery of 8 lithium-ion cells in series, 29.6 V nominal, 75 Ah and 61.8 lb, which is 28.0 kg, gives the power to start the auxiliary unit on the ground and in flight. A start power unit turns its DC into AC for the start | NTSB, Auxiliary Power Unit Battery Fire, Japan Airlines Boeing 787-8, JA829J, Boston, Massachusetts, January 7, 2013, NTSB/AIR-14/01, §1.2.1, §1.2.2 and table 1 | Reviewer |
| 17 | Tests for that investigation loaded the battery with 18 kW for 30 s for a start on the battery alone, with a note that the load had been shortened by 15 s, and with 66 A for 30 s for a start with the engines running. Three simulated starts on a battery soaked at its highest operating temperature raised a bus bar by 65 °C. The start on the battery alone is 0.15 to 0.23 kWh, 7 to 10 % of the 2.22 kWh the battery holds at its nominal voltage. These are figures of a unit of 450 kVA and carry to no other machine | NTSB, airworthiness factual report of the same investigation, addendum on testing, §D.1.1.2.4, §D.1.1.2.5 and §D.2.13 | Reviewer; endorsed |

### Auxiliary power units and what stands in for them

| # | Statement | Source | Read |
|---|---|---|---|
| 18 | Dry masses at makers. RE220, on the CRJ700 and 900: 200 to 250 lb, 91 to 113 kg; it gives 60 kVA from the ground to 45,000 ft. APS3200, on the A320 family: 136 kg; 399.7 kW at the shaft, 90 kVA, 1.8 kg/s of bleed air, and 148 kg/h of fuel under a heading of sea level and 15 °C, with no load named. HGT750, on the C919 and the MC-21: 419.7 lb, 190 kg. The maker's page of the APS2300, on the Embraer 170 to 195, gives no mass, no rating and no fuel | Honeywell Aerospace, product pages of the RE220 and of the HGT750; Pratt & Whitney Canada, APS3200 Fast Facts, data of May 2022; Pratt & Whitney, page of commercial auxiliary power units | Reviewer |
| 19 | NASA's design code takes the weight of the auxiliary power unit as 54 times the fuselage planform area in square feet to the power 0.3, plus 5.4 times the number of passengers to the power 0.9, in pounds. Its equations rest on 17 transports that are not listed, and the document does not say that the result is an installed weight. For the fuselages the register holds it gives 298 kg at 72 seats and 356 to 359 kg at 98 to 100 seats, 2.2 to 3.5 times two dry masses of statement 18, that of the RE220 at the middle of its range and that of the APS3200. It is an estimate and not a design value | D. P. Wells, B. L. Horvath, L. A. McCullers, The Flight Optimization System Weights Estimation Method, NASA/TM-2017-219627, Volume I, June 2017, equations 62 and 101 | Reviewer; endorsed as an estimate |
| 20 | The ICAO manual gives the fuel of auxiliary power units in kg/h by group and mode — start-up with no load, normal running with the air conditioning at its maximum, high load for a main engine start. Business and regional jets under 100 seats: 68, 101 and 110. From 100 to 199 seats, newer types: 77, 110 and 130; older types: 69, 122 and 130 | ICAO, Airport Air Quality Manual, Doc 9889, third edition, 2023, table 3-A1-6 | Reviewer; endorsed |
| 21 | The same manual gives times at load for a twin: 3 min of start-up, 3.6 min before departure, 35 s of main engine start, and 15 min after arrival by default, which is 22.18 min. On them a cycle burns 35.8 kg under 100 seats and 39.2 kg for newer types of 100 to 199 seats. Its simple approach takes 45 min and 80 kg for a short-haul cycle. An airline association estimates 0.23 to 0.26 h of auxiliary unit for a narrow-body with ground power at the gate, and 0.87 h without | The same, tables 3-A1-3, 3-A1-4 and 3-A1-5 | Reviewer; endorsed |
| 22 | Schiphol limits auxiliary power units to 5 min after arrival and to 5 or 10 min before departure by type, lets them run below −5 °C and above +25 °C, and enforces the rule since January 2026 under the AIP. ICAO notes that a number of airports set maximum running times, mainly for noise, and that its emission Standards do not cover these units | Schiphol, page *Minimising APU usage*, read 2026-11-26; ICAO, Doc 9889, third edition | Reviewer |
| 23 | Hotel mode of the ATR. A hydraulic brake holds the propeller of the right engine, which then gives electrical power and compressed air for the air conditioning. The maker's reason: auxiliary units are expensive, heavy and costly to maintain, and ground units ask a certain level of airport. The crew manual, as the AAIB gives it, forbids the mode with the aft service door open and during refuelling, limits the tailwind to 10 kt, keeps a pilot on the flight deck, and allows de-icing only if remote and briefed. The hazards named are noise and hot gases; with a tailwind the exhaust may blow back and raise a false fire alarm. On 29 January 2025 a crew used the mode to cool a cabin at about 38 °C | ATR, page on hotel mode, read 2026-11-26; AAIB, report AAIB-28713; ATSB, occurrence brief AB-2025-009 | Reviewer; endorsed |
| 24 | In February 2008 a fuel cell on hydrogen and oxygen gave up to 20 kW in flight on the A320 D-ATRA, drove the electric pump of the back-up hydraulic circuit and moved the ailerons. It stood in for an emergency source, not for the auxiliary unit | DLR, news of 26 May 2008; FlightGlobal, report of February 2008 on the release of Airbus | Reviewer, of extracts |
| 25 | In 2012 a regenerative fuel cell for onboard auxiliary power flew on a 737-800 of the ecoDemonstrator programme. Its power and its running time were not read | Boeing, fact sheet on hydrogen, undated; Aviation Wire, 5 October 2012, on the announcement of IHI | Reviewer, of extracts |

### Published concepts

| # | Statement | Source | Read |
|---|---|---|---|
| 26 | Five documents on concepts of 40 to 154 seats were read. The NASA paper on a single-aisle with a tail fan of 3,500 hp fed by generators on two turbofans does not name an auxiliary unit, nor a start, nor the ground. The roadmap of IMOTHEP names none in the part read; its parallel hybrid of 40 seats gives the non-propulsive systems, 167 kW, to the batteries on the typical mission and taxis on them, and its turboelectric aircraft of 150 seats has two turbogenerators at the rear of the fuselage. An ONERA study of 150 passengers has the unit once, in the name of a line of its mass breakdown. A NASA overview of narrow-body concepts names none. A master's thesis on a series hybrid drawn from the ATR 72 leaves the unit out of its electrical model because the generator takes its place | J. R. Welstead, J. L. Felder, Conceptual Design of a Single-Aisle Turboelectric Commercial Transport with Fuselage Boundary Layer Ingestion, NASA, 2016; Ph. Novelli, IMOTHEP deliverable D6.9, version 2, 2 July 2024; A. Sgueglia and others, AIAA SciTech 2018; C. L. Bowman, J. L. Felder, T. V. Marien, AIAA/IEEE Electric Aircraft Technologies Symposium, July 2018; S. J. Reid, master's thesis, Royal Military College of Canada, 2022 | Reviewer; the absence it shows is endorsed and shared with report B |

### Load cases and conditions

| # | Statement | Source | Read |
|---|---|---|---|
| 27 | In an electrical load analysis, *ground operation and loading* is the time spent preparing the aircraft before the engines start, supplied by an auxiliary unit, by the batteries or by an external source. An advisory circular gives as an example 30 min for it, 5 min for the engine start and 10 min for the taxi; it takes the most severe loading at night and in icing and loads a generator to 80 %. Neither names the stand as a sizing case, and neither gives a hot or a cold day | ASTM, F2490-05, Standard Guide for Aircraft Electrical Load and Power Source Capacity Analysis, §3.1.7, as previewed; CASA, Advisory Circular AC 21-38 v2.1, December 2022, §1.2, §4.3.3 and §4.4.3.3 | Reviewer |
| 28 | A thesis sizes an electrically driven air-conditioning pack on the ground on a hot and humid day, which it takes as the critical condition: sea level, 38 °C, a water mass fraction of 0.009. Across the designs it keeps, one pack draws 59 to 82 kW with 0.5 kg/s of fresh air; the design chosen draws 61.2 kW. The aircraft is a single-aisle on the mission of an A320. It is an estimate of another class and not a sizing case for the eWTW | M. P. J. van der Lof, Design and Optimization of an Electrically Driven Hybrid Environment Control System, master's thesis, Delft University of Technology, July 2024 | Reviewer; endorsed as an estimate |
| 29 | Thresholds in rules read. On the 787, with certain equipment-cooling items inoperative, ground operations at 30 °C or more need both packs on or conditioned air supplied; with a ram air fan inoperative the auxiliary unit must work and ground operations stay below 49 °C. Schiphol lets the auxiliary unit run below −5 °C and above +25 °C | FAA, Master Minimum Equipment List, Boeing 787, Revision 19, 20 May 2025, ATA 21; Schiphol, page *Minimising APU usage* | Reviewer |
| 30 | At San Francisco in 2019, on 21,486 operations metered every five minutes at 49 gates, 64 % of turnarounds used some ground power, for 62.5 % of their time on average, and the mean over all turnarounds was 40.3 %. The auxiliary unit is inferred to have run 43.98 min on average, 21.18 min of them before departure. Regional jets used ground power little and ran their auxiliary units briefly, without numbers. The abstract says about 20 % of turnarounds used no ground power where the body says 36 % | P. A. Antonelli, dissertation of statement 6, §3.2.4, §3.3 and §3.5 | Reviewer; endorsed. One airport; a third of the document was not read |

### Criteria in use

| # | Statement | Source | Read |
|---|---|---|---|
| 31 | On the Embraer 170 to 195, one of the two engine-driven generators may be inoperative, extended-range operations apart, only if the generator of the auxiliary unit works and is used throughout the flight, at or below FL 330, with repair within 2 flight days. The generator of the auxiliary unit is itself not required for dispatch, extended-range operations apart | FAA, Master Minimum Equipment List, Embraer ERJ-170 and ERJ-190, Revision 19, draft, items 24-21-01 and 24-22-01 | Reviewer. A draft; its page on the auxiliary unit was not read |
| 32 | On the 787, the auxiliary power unit is not required for dispatch if the systems of the engine starter-generators work and the flight stays within 180 minutes of a suitable airport. One of the four engine starter-generators may be inoperative only if both generators of the auxiliary unit and its battery work and the unit is started before departure and runs throughout the flight, with repair within 3 flight days. The battery of the auxiliary unit may be inoperative if the unit is not used, and none of the three external power systems is required. One of the two packs is required | FAA, Master Minimum Equipment List, Boeing 787, Revision 19, 20 May 2025, items 49-11-01, 24-22-01, 24-31-01, 24-41-01 and 21-52-01; its pages of ATA 49 are of Revision 15 of 2017 | Reviewer |

### Certification and rules

| # | Statement | Source | Read |
|---|---|---|---|
| 33 | CS 25J901(b): an essential auxiliary power unit is one whose function is needed for the dispatch of the aeroplane or for continued safe flight; a non-essential one is a convenience that may be shut down without hazard. CS 25J903: an essential unit is of Category 1; it has a means to start in flight and a demonstrated envelope of altitude and airspeed for it, which accounts for cold soak | EASA, Easy Access Rules for Large Aeroplanes (CS-25), Subpart J | Reviewer; endorsed. The same paragraphs are statement 8 of the [record of the certification basis](KNOT-EWTW-CRT-001_certification-basis_2026-11-15.md) |
| 34 | 14 CFR 25.903(e) asks a means to restart any engine in flight, an envelope of altitude and airspeed for it, and, where windmilling after all engines have stopped does not give the electrical power for ignition, a source independent of the engine-driven generating system. 25.901(d) puts an auxiliary power unit installation under the applicable provisions of the powerplant subpart | Electronic Code of Federal Regulations, 14 CFR 25.901 and 25.903, as of 14 September 2026 | Reviewer, of an extract; endorsed |
| 35 | A Category 1 auxiliary power unit is for installations where running in flight is necessary, as when the unit backs up electrical power in flight; Category 2 where it is not. Category 1 meets subparts A to D of CS-APU, Category 2 subparts A to C | FAA, page *Category 1 and Category 2 APU*; EASA, CS-APU, initial issue, CS-APU 10 | Reviewer, of extracts |
| 36 | In the UK text of CAT.OP.MPA.200, in force from 30 October 2025, refuelling with an engine running is *special refuelling*: it needs established procedures, approved by the authority before use | UK Civil Aviation Authority, Regulatory Library, CAT.OP.MPA.200 | Reviewer, of an extract |
| 37 | On 7 January 2013, at Boston, the battery of statement 16 burned on a parked 787-8. The NTSB found that an internal short circuit in one cell led to thermal runaway that spread to the others. The battery had been certified under special conditions 25-359-SC | NTSB, report of statement 16, §1.7.1 and §2.1 | Reviewer; endorsed. The event is statement 11 of the [record of the sources](KNOT-EWTW-SRC-001_sources-and-storage_2026-11-14.md), and the special conditions are statement 14 of the record of the certification basis |

### As reported

| # | Statement | Source | Read |
|---|---|---|---|
| 38 | Each receptacle of the 787 gives 90 kVA continuously and 112 kVA for up to five minutes. A normal gate turn runs on two units of 90 kVA; a third is recommended for a non-normal engine start with the auxiliary unit inoperative | Boeing, 787 Electrical Requirements, brochure, September 2011 | As reported: extracts of a search |
| 39 | The 787 has two starter-generators of 250 kVA on each engine and two of 225 kVA on the auxiliary unit. An engine start draws from the generators of the auxiliary unit, from those of the other engine, or from two forward ground sources. The auxiliary unit itself starts from the airplane battery, from a ground source or from an engine-driven generator | FlightGlobal, *787 special: electric dream*; Boeing, AERO, fourth quarter 2007, *787 No-Bleed Systems*, as a forum quotes it | As reported. The record of the sources has the same ratings as reported, its statement 1 |
| 40 | The packs of the 787 do not run on external power, by a post of a pilots' forum; another post speaks of a maintenance function that runs one pack from it | Two forum posts | As reported, at forum level |
| 41 | In a survey of ACI EUROPE of 2018, 42 of 51 airports gave fixed electrical ground power on stand. Since 2021, 20 projects of the Connecting Europe Facility at 63 airports have had more than 160 million euros of grants, partly for electricity and preconditioned air to stationary aircraft. Bordeaux has 400 Hz at all 29 passenger stands and 20 mobile preconditioned-air units | Oxera, study of statement 8, citing a staff working document of the Commission; EASA, European Aviation Environmental Report 2025, page on airport infrastructure; Bordeaux Airport, press release | As reported; the EASA page read in part |
| 42 | A US handbook gives defaults by category. Electricity at the point of use, in two tables that differ in cooling: for a regional jet 13.30 kW of ground power, 39.33 kW of cooling in the first table and 16.68 kW of heating; for a turboprop 26.60, 31.16 and 12.72; for a narrow body 23.88, 68.64 or 48.84, and 46.71. Fuel flow of the auxiliary unit of a narrow body: 0.021 kg/s in one mode and 0.038 kg/s in another. Time of auxiliary unit in a cycle of a narrow body: 22.18 min, of which ground systems can take over 18.6 min | Transportation Research Board, ACRP Report 64, Handbook for Evaluating Emissions and Costs of APUs and Alternative Systems, 2012, chapter 3 | As reported: a dissertation and extracts of a search. What separates the two tables, and the rows of the second for regional aircraft, were not read |
| 43 | Smaller aircraft with quick turns stay at the gate as little as 20 minutes. Airlines set a time to connect ground power and air, for example within 5 or 10 minutes of arrival; when it is missed, or the turn is very short, crews may leave the auxiliary unit running. Cabins need heating below 45 °F and cooling above 50 °F, by a technical report of a programme of the FAA | Transportation Research Board, ACRP Research Report 207, 2019 | As reported: extracts of a search |
| 44 | Bristol allows no restart of the auxiliary unit until 10 minutes before departure. Le Bourget allows 5 minutes after arrival on stands with ground air and power and 20 minutes without | Bristol Airport, instruction BRS-OSI-ENV-005, version B; OPSGROUP, note on the AIP of Le Bourget | As reported |
| 45 | The auxiliary unit of the Dash 8-400 is an option, gives bleed air and 28 V DC, cannot be run in flight, and starts from the main battery or from external power | Training material, not opened | As reported |
| 46 | A fuel-cell system of 0.5 MW was to take the place of the auxiliary unit of an A330-200 and to fly for an hour at 25,000 ft on 10 kg of gaseous hydrogen, by an announcement of 20 June 2023. Later, by its chief technology officer, it is not to fly and is tested on the ground | Airbus, press release of 20 June 2023; FlightGlobal, two reports | As reported; the date of the second statement was not read |
| 47 | An auxiliary unit of an A320 at the gate burns about 80 to 130 kg/h, in the literature a dissertation reviews | P. A. Antonelli, dissertation of statement 6, §2.2 | As reported |
| 48 | A full electric air-conditioning system needs about 400 kW for 350 passengers at 40,000 ft on a hot day; the bar for 100 passengers is not legible. One sentence of a US patent puts an auxiliary unit on the ground at about 260 kW in an architecture part electric and part bleed, the aircraft not being named in the passage | J. Herzog, Electrification of the Environmental Control System, ICAS 2006, paper 344; US patent 7,970,497 | As reported in part |
| 49 | ICAO Annex 16, Volume I, Attachment C gives guidance on the noise of auxiliary power units on the ground. Lists of phases for a load analysis go back to a US military specification, MIL-E-7016F | SAE International, ARP1307C, scope; Tech Briefs, article on electrical compliance | As reported. The levels were not read |

### Findings of absence

| # | Not found | Readers |
|---|---|---|
| 50 | An installed mass of an auxiliary power unit of the class, and any mass of the APS2300 | Two; endorsed |
| 51 | The fuel of a main engine in hotel mode, in a source that can be used | One |
| 52 | The electrical power and the energy of a start of a gas turbine of 1 to 5 MW | Two; endorsed |
| 53 | What the electric packs of the 787 draw at the stand. Whether they run on external power is in no primary source read either, which only the reviewer looked for | Two for the draw; endorsed |
| 54 | A published electrical load analysis of a transport with electric packs, and a cold-day design condition | One; endorsed |
| 55 | The length of a turnaround of 100 seats on regional networks, and the share of it on ground supply, for any airport but one | One; endorsed |
| 56 | The share of stands with ground power by size of airport, and any survey of conditioned air | Two; endorsed |
| 57 | A battery module or a fuel cell flown as the supply of a stand | Two |
| 58 | A published concept of the band that carries an auxiliary unit and gives its reason, or that says how its turbogenerators start | Two; endorsed |
| 59 | Fuel flow, noise and exhaust of a turbogenerator at a few percent of its rating | One; endorsed |
| 60 | A primary source that says which source starts the engines of the ATR 72, or of any transport of 70 to 150 seats without an auxiliary unit | Two |
| 61 | The text of CS 25.903(e), the levels of Attachment C of Annex 16, the text of the Union on special refuelling, and the page of the master list of statement 31 on the auxiliary unit | One |

---

## Status proposed

The exit of `KNU-EWTW-AUX-001-01` asks whether each figure is measured, published or estimated. The reviewer proposes; the authority assigns.

| Status | Statements |
|---|---|
| A norm or a rule in force | 1, 2, 7, 22, 32 to 36; 31 once issued |
| Published by a maker or an authority, of aircraft or equipment in service | 3, 4, 5, 9 to 16, 18, 23 |
| Published by an association, on a sample of airports | 8 |
| Measured in service or in test | 6, 17, 30 for the use of ground power, 37 as an event |
| Demonstrated in flight test | 24, 25 |
| Published defaults, how measured not read | 20, 21 |
| Estimated: a model, a regression or an inference | 19, 28, 30 for the time of auxiliary unit |
| Projected concepts | 26 |
| Examples in guidance | 27 |
| A threshold in a rule | 29 |

---

## What follows for the eWTW

Each point is a derivation of the reviewer and ranks nothing.

- **"The ground alone" is two supplies, and the rule of the Union assures one.** At the airports of the TEN-T networks electricity at the stand is owed by dates, and remote stands may be exempted at the smaller ones; conditioned air is not owed (statement 7), and small airports have remote stands (statement 8). The one transport with electric packs asks the ground for conditioned air as well as for power (statements 9, 10), and with items of equipment cooling inoperative its master list ties ground operations at 30 °C or more to packs or conditioned air (statement 29).
- **The sockets of the class are sized for an aircraft whose packs are off.** 60 kVA is printed for the 737, and regional jets are seen to draw 2 to 7 kW (statements 3, 6). The only figure for an electric pack on the ground is of another class and is an estimate (statement 28): as an order of magnitude and no more, two packs of that size would ask more than one socket of the class gives. It is no load for the eWTW. That load is the work of `KNU-EWTW-AUX-001-02` with `KNOT-EWTW-ECS-001`.
- **Dispatch, more than the stand, is what the two master lists give the auxiliary unit.** On the 787 the unit is not required for dispatch, and on the Embraer its generator is not; on both it must run when an engine generator is out (statements 31, 32). An aircraft with nothing at `049` needs another answer to that case; it belongs to `KNOT-EWTW-GEN-001` and `KNOT-EWTW-ESS-001` as much as to this KNOT.
- **A start on batteries is a matter of battery life and of fire.** Where an investigator describes it, it is possible and avoided (statement 14); the one battery read that starts an auxiliary unit, a lithium-ion one in service, has burned on the ground (statement 37). Both bear on the battery of options A and C, which `KNOT-EWTW-STO-001` owns. The start read is short and hard: 18 kW from 2.22 kWh (statement 17). For a machine of 2 to 5 MW nothing was found (finding 52).
- **The condition of option C is the split of Subpart J.** A module that is an emergency source, as option D of `KNOT-EWTW-ESS-001` has it in the [record of 2026-11-14](KNOT-EWTW-ESS-001_option-set_2026-11-14.md), is essential: Category 1, with a start envelope in flight after cold soak (statement 33). A module for the stand alone is not. The two have different footprints at `049` and should not share one mass. Subpart J speaks of an auxiliary power unit: no text read says what stands in its place for a module of another technology.
- **The precedent of option B is not a turbogenerator.** Hotel mode is a propulsion engine with a brake on its propeller, under limits that keep it off during refuelling (statements 23, 36). A turbogenerator at the stand would run at a few percent of its rating, where no figure of fuel, noise or exhaust was found (finding 59); the part-load figures of the [record of 2026-11-26](KNOT-EWTW-GEN-001_turbogenerator-efficiency-and-altitude_2026-11-26.md) go no lower than 34 % of the power available (its statement 22).
- **The fuel of an auxiliary unit at the stand is 101 kg in an hour under 100 seats, by the one table read** (statement 20). Report B gives 68 kg from tables it does not identify; the handbook that could settle it was not read (statement 42).
- **Seven criteria come from certification, from rules and from two precedents, before any preference.** A unit needed to fly is essential, with what follows (statement 33). A restart in flight has its means and, where windmilling gives none, its independent source (statement 34). The limits of an alternate source are named and shown, as the record of 2026-11-14 holds from a text that the register has as reported. A lithium battery for a start is installed under conditions of its own and its failure is contained (statement 37). Refuelling with a machine running needs approved procedures (statement 36). Running time and noise at the stand are limited locally (statements 22, 49). Persons at the stand are kept clear of a running machine and the flight deck is manned (statement 23). The battery and the persons at the stand rest on a precedent, an accident and the limits of hotel mode, and not on a rule. The second reading proposes the seven for the `criteria` of the KNOT as proposed; whether the last three reach a turbogenerator in a ground mode is settled by no document read.

---

## Not accepted

| Content | Report | Reason |
|---|---|---|
| Ground units of 90 kVA as typical for regional aircraft, with ISO 6858 as the source | B | The abstract of the standard gives no rating. For the class the sources give less (statements 3, 4, 6, 13) |
| That fixed units are frequent at hubs and less so at small regional airports | B | No source. Statement 8 points the same way and does not measure it |
| That the packs of the 787 are inoperative on the forward external power alone and that full pack operation needs more sources; and that report A notes it | B; second reading | No source in B. The planning document is silent (statement 10). Report A does not say it. Kept at forum level as statement 40 |
| 0.012 and 0.019 kg/s for auxiliary units under 100 seats, with ICAO and the handbook as sources | B | The ICAO table gives 68, 101 and 110 kg/h (statement 20), which the second reading endorses. B's figure with the air conditioning is ICAO's with no load. The rows of the handbook for regional aircraft were not read |
| 100 to 200 kg/h for narrow-body auxiliary units on the ground with packs | B | No source. Statements 18, 20 and 47 give 110 to 148 kg/h |
| Dry masses of 100 to 150 kg in design studies | B | No study is named. Statement 18 has the masses at makers |
| Classes A to D for the figures | B | They belong to another brief. The exit of this KNU asks measured, published or estimated |
| That no investigation report says which source starts an engine | A | Wrong for the Saab 340B (statement 14). It stays true of the ATR |
| The electricity at the point of use as one table of the handbook | A | The handbook has two (statement 42) |
| A comparison of the stand with electric packs against sockets and against a turbogenerator, as a statement | A | It joins figures of different aircraft. Report A calls it an order of magnitude and the second reading asks that it not be read as a sizing case. Kept in words only, in *What follows* |
| That report A stays inside the band of 70 to 150 seats | Second reading | It uses types outside the band as precedents and names each: the Saab 340B, the 787, the units of the A320 family and of the C919 |
| To archive report A as evidence for the three KNUs | Second reading | The register files records and not reports. This record is what is filed |
| Figures of the airport planning manual of the Embraer 190, and the fuel of hotel mode from a brochure of ATR | — | Both documents carry a notice of confidentiality. Set aside until the authority decides whether a document its owner publishes is public material whatever its notice says. The register already cites the first, in two records of 2026-11-17 and in the configuration analysis |

---

## Open

Research can still give:

- chapter 3 of the handbook of statement 42, which settles the fuel of auxiliary units of regional aircraft and what separates its two tables;
- which source starts the engines of an ATR 72, and whether the packs of the 787 run on external power, each in a primary source;
- a mass of the APS2300, and an installed mass of any unit of the class, from a weight statement that separates the unit from its installation;
- the start of a gas turbine of 2 to 5 MW: the power and energy at the starter-generator, from a maker or a test;
- turnaround times by aircraft type for Europe, which EUROCONTROL publishes and the reviewer could not open;
- a cold-day condition for an electric pack on the ground, and the practice of SAE on air conditioning, which is not public;
- the texts of finding 61;
- the sentence of AMC 25.1351(d) on the limits of a source that is not limited in time, which the register has as reported since 2026-11-13 and on which the third criterion rests;
- statements 38 to 49 at a place the reviewer can read;
- every figure of this record, read again at its document.

A second reader has read the places cited for three statements. The other thirty-four have one, and so have all the statements that serve `KNU-EWTW-AUX-001-02` and `-03`.

The authority decides:

- whether documents their owners publish with a notice of confidentiality are public material for the brief;
- the hot day and the cold day of the stand, among the thresholds of statements 10, 22, 28 and 29;
- whether the seven criteria of *What follows*, written into the KNOT as proposed with this record, are approved, and in which words.
