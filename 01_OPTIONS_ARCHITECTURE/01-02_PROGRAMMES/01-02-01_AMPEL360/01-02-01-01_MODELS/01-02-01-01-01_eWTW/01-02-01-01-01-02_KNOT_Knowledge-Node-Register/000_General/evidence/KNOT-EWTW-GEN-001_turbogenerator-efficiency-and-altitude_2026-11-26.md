# Research record — gas turbine and turbogenerator: efficiency, power against altitude, mass

| | |
|---|---|
| KNOT | `KNOT-EWTW-GEN-001` Generation architecture |
| Serves | `KNU-EWTW-GEN-001-01` and `-02`, and two lines of the first budget of criterion `M5` in the [review record of 2026-11-24](KNOT-EWTW-CRZ-001_reference-and-interval_2026-11-24.md): the efficiency of the turbogenerator and the cruise altitude. It gives `-03` one input, on the size of the unit |
| Produced by | Three research reports of 2026-11-26 on one brief. **A**: Claude. **B**: relayed by the author as produced with ChatGPT. **C**: relayed by the author as produced with Grok. Then a second reading of report A, relayed by the author as produced with ChatGPT. None of the four is filed here; they hold the links to the sources |
| Brief | The research hand-off of 2026-11-24, issue 76 of the repository, on register 0.11.24 |
| Reviewed by | Claude, 2026-11-26. The reviewer is the producer of report A, and the second reader is the producer of report B |
| Accepted | Thirty-six statements: thirty-one read by two readers, three by the reviewer alone, and two as reported in part. Eight more as reported, and ten findings of absence. Proposed, not ratified |
| Figures | Recomputed in [`TGF-EWTW-GEN-001`](TGF-EWTW-GEN-001/README.md), by `tools/turbogenerator_figures.py` |

This record keeps what the review accepted from the three reports and from the second reading. It is a reading of public sources, written in our own words. It recommends no option, and it states no conformity of the eWTW with any rule.

**Safety first.** Nothing here ranks an option or sizes a unit. The failure cases, the rotor burst and the certification basis stay with `KNU-EWTW-GEN-001-02` and `-03` and with `KNOT-EWTW-CRT-001`.

**Who read what.** In the last column of each table, *two readers* means that the reviewer and another reader each read the place cited, on their own; *reviewer* means the reviewer alone; *as reported* means the reviewer did not read it. No reader is independent of every report: the reviewer wrote report A and checked reports B and C, and the second reader wrote report B and checked report A. What only one of them brings has one reader, and the table says so.

**Efficiency.** It is shaft work over the lower heating value of the fuel, taken at 43.0 MJ/kg; between 42.8 and 43.2 MJ/kg a figure moves by half a per cent. The two values of the budget, 0.350 and 0.389, run from the fuel to the terminals of the generator. A shaft efficiency is set beside them with a generator at 0.97, the value of the screening.

---

## Accepted content

### Engines of today

| # | Statement | Source | Read |
|---|---|---|---|
| 1 | The PW150A is certified at 3,781 kW for take-off and for maximum continuous power and at 3,415 kW for normal take-off, at sea level and at rest, flat rated to 37 °C, with a dry mass of 716.9 kg. The sheet holds no consumption and no cruise rating | EASA, type-certificate data sheet IM.E.049, Issue 01, 19 November 2014 | Two readers |
| 2 | A NASA model of an engine like the PW127E, without its propeller, is set on values the paper marks as published by the manufacturer: 2,400 shp, 0.474 lb/(hp h) and a pressure ratio of 14.7 at sea level and at rest. That is 0.290 on the shaft. At 20,000 ft and Mach 0.5 it gives 1,696 hp at full throttle with 0.430 lb/(hp h): 0.320 | NASA, Antcliff, Guynn, Marien, Wells, Schneider and Tong, AIAA 2016-1028, January 2016, table 2 | Two readers |
| 3 | A PW120A in airline service, from a flight data recorder at one instant of a cruise: 928.7 and 930.4 kW on the two shafts with 266.4 and 281.1 kg/h, at 15,616 ft, −23.5 °C and 198.7 kt indicated. That is 0.292 and 0.277, at 62 % of the take-off rating of 1,491 kW. The power is computed from recorded torque and propeller speed. The operator is not named and no uncertainty is given | Specific Range Solutions, SRS-TSD-002 Rev. 1, 20 July 2009, table 3.3. The document names a contact and no author | Two readers. The point is at about Mach 0.40, computed here |
| 4 | NASA quotes the AE1107 at 6,000 hp and 0.426 lb/(hp h) at sea level and at rest, and credits an engine yearbook of 2003. That is 0.323. It is a quoted specification, with no test point | NASA/TM-2010-216089, Snyder and Thurman, table 1 | Two readers |
| 5 | NASA models of the GE38 class at sea level and at rest: 0.385 lb/(hp h) in 2014, scaled to 7,500 hp; 0.394 in 2019 and 0.3909 in 2023, at 7,248 hp. That is 0.357, 0.349 and 0.352 | NASA, Snyder, 2014, table 2; Snyder and Tong, 2019, table 1; Chapman, Vegh, Nunez and Snyder, 2023, table 6 | Two readers |
| 6 | A T56 on a test bench at four power settings gave 2,198.7, 2,996.3, 3,256.3 and 3,442.0 kW on the shaft with 0.235, 0.294, 0.309 and 0.317 kg/s of fuel of 42.8 MJ/kg, at 93.6 kPa and 298 K. At that heating value the shaft efficiency is 0.219, 0.238, 0.246 and 0.254. The paper describes the bench, its dynamometer and its instruments, and gives a relative uncertainty of about 0.13 % for each efficiency. A second case, which adds the kinetic energy of the exhaust, reaches 0.281 at take-off | Balli and Hepbasli, Energy Conversion and Management 73, 2013, pages 106 to 120, tables 3 and 14; Özen, Uysal and Balli, 2020, tables 5 to 9 | The reviewer read the abstract, with 0.254 and 0.281 at take-off, and the paper of 2020, with the four fuel flows, the heating value and the ambient state. The three lower powers, the bench and the uncertainties are as reported by the second reader, from a copy on a third-party host |
| 7 | By its maker an ATR 72-600 burns 650 kg/h for both engines at 270 kt, at 95 % of its maximum take-off mass on a standard day: at flight level 240 in an earlier sheet and at flight level 200 in a later one. Neither gives a shaft power | ATR, product sheets of the ATR 72-600, two editions | Two readers |
| 8 | The English page of the maker of the D-27 gives 14,000 ehp, 10,294 kW, and 0.231 kg/kWh at take-off, at sea level and at rest, 15 K above the standard day and 730 mm Hg; 6,750 ehp, 4,963 kW, and 0.177 kg/kWh at maximum cruise, 11,000 m and Mach 0.7; and a dry mass of 1,730 kg. All of it is on equivalent power, which counts the jet thrust. The engine is of 10 MW, above the class | Motor Sich, product page of the D-27 | Reviewer, twice. Other editions disagree: statement 43 |

### Power against altitude and speed

| # | Statement | Source | Read |
|---|---|---|---|
| 9 | A Rolls-Royce engine of 2015, of 8,100 shp and scaled to 7,500 shp of maximum rated power at sea level, has a table of maximum continuous power at eight speeds from rest to 350 kt and five conditions: sea level, 5,000 ft on a day 20 K warm, and 10,000, 25,000 and 30,000 ft on a standard day. At rest: 5,900 shp at sea level, 3,657 at 25,000 ft, 3,005 at 30,000 ft. At 350 kt: 6,148, 4,002 and 3,303 | NASA/CR-2013-216593, Robuck, Wilkerson and Maciolek of Boeing and Vonderwell of Rolls-Royce, September 2013, table 4, page 35 | Two readers for nine values; reviewer for the other thirty-one |
| 10 | The NASA engine of the same study, of 7,500 shp of maximum rated power, has the same table at full power-turbine speed. At rest: 5,896, 3,089 and 2,605 shp. At 350 kt: 7,220, 3,843 and 3,294 | The same report, table 3, page 35 | Reviewer; two of its values by the second reader too |
| 11 | The report says that the two engines have significantly different lapse rates. For the Rolls-Royce engines of 2015, 2025 and 2035 it plots power against altitude, to about 35,000 ft, and Mach number, to 0.7, at three power-turbine speeds. It withholds their fuel consumption as proprietary, and says that the engine of 2035 promises over 25 % less | The same report, sections 4.4 and 4.7, figures 11 to 25 | Two readers for the figures; reviewer for the rest. No value was taken from a figure |
| 12 | In a second document the NASA engine, sized at 6,476 hp of maximum rated power and 5,105 hp of maximum continuous power at sea level and at rest, keeps 11,070 hp for four engines at 28,000 ft and 284 kt. Scaled to 7,500 shp that is 1.7 % below statement 10 read between its values. Table 4 of the document labels the 6,476 hp as maximum continuous power; its tables 3, 5 and 7 make it the maximum rated power | NASA/TM-2013-218101, Snyder, December 2013, tables 3 to 7 | Two readers |
| 13 | The model of statement 2 gives at 20,000 ft and Mach 0.5 0.707 of its take-off power, with 0.625 of its air flow | AIAA 2016-1028, table 2 | Two readers |
| 14 | A study engine of GE gives 6,450 hp to the propeller at Mach 0.80 and 35,000 ft on a day 10 K warm, and 12,500 hp at Mach 0.2 at sea level on a day 15 K warm, in the same table. The report also names 12,500 shp as its static design objective, and matches the cycle at the end of climb | NASA CR-168113, Sargisson of GE, June 1985, tables 3.4-2 and 4.4-2 and section 4.4.1 | Two readers, through a scan |
| 15 | At the working reference, 31,000 ft and 360 kt, the rule of the screening gives 0.398 of the power at sea level and at rest, and 5.6 MW become 14.1 MW. The brief has 14.2 MW, from rounded figures | Computed from the [screening of the cruise points](CRP-EWTW-CRZ-001/README.md) | Computed by reports A and B and by the second reader, each on its own |

### Forecasts

| # | Statement | Source | Read |
|---|---|---|---|
| 16 | The model of statement 2 with the technology it takes for 2030 has turbomachinery 2 to 3 points more efficient and uncooled ceramic vanes, at the same temperature and pressure ratio. It burns 0.427 lb/(hp h) at take-off and 0.398 at full throttle at 20,000 ft and Mach 0.5: 0.322 and 0.346 | AIAA 2016-1028, tables 1 and 2 | Two readers |
| 17 | A family of NASA and Army models gives consumption and weight by size and technology, at rated power at sea level and at rest. Advanced: 0.279 at 660 hp, 0.296 at 1,300 hp, 0.382 to 0.395 for three designs of 3,000 hp, 0.410 at 5,000 hp and 0.418 at 7,500 hp. The model of 7,500 hp is set at the goals of the FATE programme. Current: 0.258 at 650 hp, 0.295 at 1,895 hp, 0.279 at 5,000 hp and 0.395 at 11,000 hp. The names of the models are nominal: `ts650a` has 660 hp, `ts1900s` 1,895 hp and `ts7500s` 7,248 hp | NASA and US Army, Chapman, Vegh, Nunez and Snyder, Vertical Flight Society Forum 79, 2023, tables 4 to 6 | Two readers for the powers and the consumptions; reviewer for the weights |
| 18 | The engine of statement 12 has 0.399 at its maximum rated power and 0.383 at its maximum continuous power at sea level, and 0.413 to 0.425 in cruise at 28,000 ft. An engine that NASA gives the technology of 2035 has 0.3255 lb/(hp h), 0.423: a table of the paper calls it a cruise consumption and its text gives it at take-off power at sea level. Two further generations have 0.441 and 0.515 | NASA/TM-2013-218101, table 7; Acree and Snyder, 2012, table 2 and the section on gearbox weight; Snyder, 2014, table 2 | Two readers |
| 19 | A study of a regional turboprop of 40 seats for service after 2035 assumes 14 % less consumption for its turboshaft of 1.9 MW | Habermann and others of Bauhaus Luftfahrt, Aerospace 10(6), 529, 2023, table 2 | Two readers |
| 20 | Two engines of the FATE programme ran for more than 130 hours, and their maker reports the primary objectives as completed. A T901 flies on a helicopter since May 2025, and the Army dates the end of its preliminary flight rating tests to 24 June 2026. No consumption of either is public as an absolute figure | GE, US Army and Sikorsky, releases | Two readers |
| 21 | A NASA project for turbofan cores aims at 5 to 10 % less fuel than the best of 2020 and at up to 20 % of power extracted at altitude, with a core demonstration by the end of 2028. It is not a goal for a turboshaft | NASA, pages and overviews of the HyTEC project | Reviewer. Report C brought it with no source named |

### Part load

| # | Statement | Source | Read |
|---|---|---|---|
| 22 | The engine of statement 12 burns 0.324 lb/(hp h) at 69 % and 0.333 at 61 % of the maximum continuous power available at 28,000 ft, and 0.471 at 34 % at 5,000 ft. Its text says 62 to 67 % for the cruise. Table 1 puts the point at 5,000 ft on a day 20 K warm, and table 6 on a standard day | NASA/TM-2013-218101, tables 1, 6 and 7 | Two readers |
| 23 | The model of statement 2 burns 0.5 % and 0.7 % more for each kilowatt-hour at 90 % and 80 % of the power available at its cruise point. Its version for 2030 burns 1.0 % and 1.8 % less | AIAA 2016-1028, table 2 | Two readers |
| 24 | On the bench of statement 6 the consumption for each kilowatt-hour is 3 %, 7 % and 16 % above that at take-off, at 95 %, 87 % and 64 % of the take-off power. The setting the paper calls 75 % gives 64 % of the take-off power. The engine has one shaft, and a model by one of the authors takes the same air flow, 14.75 kg/s, in the four settings | As statement 6 | As statement 6: the three lower powers are as reported |

### Generators and converters

| # | Statement | Source | Read |
|---|---|---|---|
| 25 | A generator of 1 MW was run by its maker at 1.02 MVA and continuously at 900 kW in 2022. It weighs 127.0 kg; 131.5 kg with its control unit; 154.2 kg with the rectifier bridge, for 300 or 600 V DC. Its design efficiency is 98 % in AC and 97 % in DC at rated load. In 2026 the maker writes that the 97 % is a DC design efficiency and that the 8 kW/kg is calculated from the rating and the weight | Honeywell: release of 31 May 2022; brochure of June 2020; article of 9 October 2026 | Two readers |
| 26 | A generator of 4 MW and 15,000 rpm for a 3 kV bus is designed at 232 kg, 17.3 kW/kg, with a predicted efficiency of 98.3 %. The prototype built has a silicon-iron core in place of the cobalt-iron of the design, and weighs 249 kg. It was tested at reduced power: its voltage at no load up to 3,000 rpm, a load at 500 rpm, and a circulating-power test at 7,500 rpm and 1.5 kV, half the rated speed and voltage. The efficiency measured there is of the machine and its converter together. The losses of the machine alone were not measured | Golovanov and others of the universities of Nottingham and Bologna, IEEE Transactions on Transportation Electrification 7(4), 2021, author manuscript | Two readers |
| 27 | The active rectifier for that generator is of 4 MW, 5 MVA, at 3 kV, and of 240 kg and 411 litres. Its efficiency of about 98.5 % comes from a simulation. The test ran at 1.5 kV with power circulating between two halves of the system, and the losses measured for the whole rig were about 85 kW. Neither the rated power nor the rated voltage was reached. This paper gives the circulating power as up to 1 MW, and the paper of statement 26 as 350 kW | Trentin and others of the University of Nottingham, IEEE Transactions on Industrial Electronics 68(12), 2021, author manuscript | Two readers; reviewer for the mass and the volume |
| 28 | A concept of a regional aircraft sizes a generator of 2.98 MW at 320.2 kg and its converter of 2.93 MW at 111.8 kg, at 341 V AC and 800 V DC. Its text gives 98.4 % and 99.5 % for them, and its table 98 % and 98.4 % | IMOTHEP, deliverable D3.4, version 5, June 2024, section 2.3.2, marked public | Two readers |
| 29 | A study of a regional jet assumes 97 % for its generator, 99 % for its rectifier and 99 % for its bus, and 5.46 kW/kg for its electrical system. For each wing it tabulates 5,859 hp at the generator, 7,274 lbm of electric propulsion system and 5,450 lbm of engine, 12,724 lbm in all, against 8,800 lbm for the engine of its baseline and 6,300 lbm for a conventional engine of the same year | Perullo, Shi, Cinar, Alahmad, Sanders and Mavris, AIAA, 2020, tables 2 and 3 | Two readers |
| 30 | The auxiliary power unit that the maker of statement 25 pairs with its generator weighs 762 lb, 345.6 kg. The maker announced the pairing for ground tests in March 2021 and gives no weight for the two together | Honeywell, product page of the HGT1700; release of March 2021 | Two readers for the mass; the release as reported by the second reader |
| 31 | An inverter of 1 MW with a 2.4 kV DC input is published at 99.1 % and above 18 kVA/kg. Its abstract gives neither the load nor the power factor of that point, and it is not a rectifier. NASA sets goals of 13.2 kW/kg and 96 % for megawatt machines and of 19 kW/kg and 99 % for their electronics | Zhang, He, Pan, Schutten and Dame, IEEE ECCE 2019, abstract; NASA, Woodworth, 2025 | Two readers |
| 32 | A machine of 1 MW of a university was tested as a generator at partial speed in 2021 and damaged before full power and speed. Another, of 1 MW, is designed at 17.1 kW/kg, with 10.5 kW/kg estimated for the whole drive | NASA release of August 2021; MIT, AIAA paper of 2023 | Two readers |

### What ran and what flew

| # | Statement | Source | Read |
|---|---|---|---|
| 33 | Megawatt-class motor-generators with their converters ran at conditions up to 45,000 ft in a NASA chamber, from June 2021 to early 2022. No gas turbine is named in it, and neither a voltage nor a power is given as a number | GE and NASA releases of July 2022; NASA, 20 July 2026 | Two readers |
| 34 | A Saab 340B flew above 30,000 ft on 20 May 2026 with a CT7 turboprop that carries megawatt-class motor-generators and a battery. The machines drove the propeller and charged the battery: it is a parallel hybrid, and its gas turbine gives thrust. Neither the power generated nor the voltage is published | GE Aerospace and NASA, 20 July 2026 | Two readers |

### Counts and installations

| # | Statement | Source | Read |
|---|---|---|---|
| 35 | The study of statement 29 is of 86 passengers, 1,980 nmi and Mach 0.8, for 2030. It has two turbogenerators at the wing tips and eight electric fans, with batteries under the floor. The engines are sized at the top of climb, 35,000 ft and Mach 0.8. Its text describes no failure case and no power to be left after one | Perullo and others, AIAA, 2020, sections II-A, II-B and II-F and table 3 | Two readers |
| 36 | A concept of a European project has one turbogenerator as a range extender, batteries and eight electric propellers. Its report analyses the loss of a propeller, of the gas turbine or the generator, of a battery pack and of a bus. After the loss of the gas turbine the aircraft has to reach an airport within its electric range | IMOTHEP, deliverable D3.4, section 2.3.3 | Two readers. Its 40 seats are as reported |

### As reported

These were not read by the reviewer at a source that can carry them. They have no class, and no figure of this record rests on them.

| # | Statement | From | Why it is not more |
|---|---|---|---|
| 37 | 0.433 lb/(hp h) for the PW150A at take-off | A, C | A teaching page in A, *published specifications* in C. Neither is the maker, and neither says whether the power is on the shaft |
| 38 | 0.35 lb for each equivalent horsepower-hour for the TP400 | A, the second reader | A paper of 2015 quotes it from an engine yearbook, marked as a cruise figure under a heading for take-off at sea level, with no altitude and no speed. The paper was read; the yearbook was not |
| 39 | 6,500 to 7,500 shp of thermodynamic power for the PW150A, and a cruise consumption for the CT7 | A | An encyclopaedia and a teaching page |
| 40 | Consumption at half power 1.19 and 1.15 times that at design power | B | Read by B off a chart of a NASA presentation, which prints no number. Its producer agrees that they are approximate readings |
| 41 | Four generator channels for the two turbogenerators of the study of statement 35 | B, the second reader | A figure of the paper. The reviewer could read only its caption. Four channels are not four turbines |
| 42 | A superconducting generator loaded to 1.3 MW, with about 97 % at 1 MW when its cryocooler is counted | B, the second reader | Not read. It is a cryogenic machine |
| 43 | For the D-27, a dry mass of 1,650 kg in a catalogue of its designer; 9.738 MW with 0.250 kg/kWh at take-off and 0.190 in cruise on the Ukrainian page of its maker; 13,240 ehp with 0.180 kg for each equivalent horsepower-hour in a brochure of its designer | The second reader | Not read. The reviewer saw the last pair in an extract of slides of the designer of 2015. The editions disagree with statement 8 and with each other |
| 44 | 4,637 hp printed with 3,458 kW, and 805.49 kg dry, for the AE 2100D2 | The second reader | EASA, data sheet IM.E.040. Not read |

### Findings of absence

Ten statements say that three searches and a second reading found nothing. They are findings of the search, not properties of the world.

| # | Not found |
|---|---|
| 45 | A measured cruise efficiency, with altitude, Mach number and power setting, for an engine of 2 to 6 MW in service. Statement 3 is of an engine of 1.5 MW, and statement 6 of a bench on the ground |
| 46 | A power chart or table of a maker or of a data sheet for an engine of the class in service, and any tabulated power at 31,000 or 35,000 ft. Statements 9 to 11 narrow it: two tables to 30,000 ft, and figures above |
| 47 | A measured consumption of an engine at the technology forecast for 2035 to 2037, on a bench or in flight, as an absolute figure |
| 48 | A measured part-load map at altitude for an engine of the class |
| 49 | A measured efficiency of a generator of 1 MW or more with its rectifier, with its boundary, its cooling and its uncertainty stated |
| 50 | A weighed mass of a complete turbogenerator of 1 MW or more: turbine, gearbox if any, generator, rectifier and their cooling |
| 51 | A gas turbine that only drives generators, of 1 MW or more, run in an altitude cell or flown |
| 52 | The power generated and the voltage of the systems of statements 33 and 34 |
| 53 | A concept of 70 to 100 seats that states the power to be left after the loss of a generating unit. It is finding 16 of the [record of 2026-11-15](KNOT-EWTW-GEN-001_generation-architecture_2026-11-15.md), again |
| 54 | An inlet, an exhaust, a fire zone or a rotor-burst geometry for such an installation, or the pressure recovery of its inlet. It is finding 18 of that record, again |

---

## Classes proposed

The brief asks for a class for each figure: `A` measured on hardware representative of this aircraft, `B` measured on similar hardware or published tests, `C` a method or a statistic, `D` an assumption or a forecast. These are proposals. No figure read is of class `A`.

| Evidence | Class | Why |
|---|---|---|
| Statement 3, the PW120A in flight | B | Measured on similar hardware: smaller, one instant, no uncertainty |
| Statements 6 and 24, the T56 on the bench | B, on the account of the second reader | A published test of an engine of 3.4 MW, on the ground. The reviewer could not read that the points are measurements |
| Statements 1 and 30: ratings and masses of products in service | B | Certified or declared by the maker |
| Statements 7 and 8: figures of a maker's sheet | None | A fuel flow of an aircraft with no shaft power; an engine sheet on equivalent power, whose editions disagree |
| Statements 2, 4, 5, 9, 13 and 23: models and quoted data of engines of today | C | Methods set on public data. They are not measurements |
| Statements 10, 12 and 22: the NASA engine | C for its ratios of power and of consumption; D for its efficiency | It is an advanced design. How its power falls and how its consumption moves with load is a method; the level of its efficiency is a forecast |
| Statements 14 and 16 to 19: study engines and advanced models | D | Forecasts |
| Statement 15, the rule of the screening | D | An assumption, as the register declares it |
| Statement 25: the run at 900 kW and the mass of the generator | B | A test and a mass, as the maker reports them |
| Statement 25: the 97 % and 98 %, and the mass with control unit and rectifier | D | Design values, in the words of the maker |
| Statement 26: the mass of the prototype, and that it ran at reduced power | B | Built and tested |
| Statement 26: the rated power over the mass of the prototype | C | The prototype did not run at that power |
| Statement 26: the mass and the efficiency of the design. Statement 27: its 98.5 % | D | Predicted |
| Statement 27: the 85 kW of the rig | B | Measured, on two machines and two converters together |
| Statement 27: the mass of the rectifier. Statement 31: the efficiency of the inverter | None | The papers do not say that the mass was weighed, nor at which load the efficiency holds |
| Statements 28, 29, 35 and 36 | D | Concept values |
| Statements 20, 33 and 34, and the test of statement 32 | B | Tests and flights, with no figure attached |
| Statement 21, the goals of statement 31 and the design of statement 32 | D | Goals and a design |
| The two values of the budget, 0.350 and 0.389 | D | No evidence read moves either |

---

## What follows for the eWTW

Figures in this section that are not in a statement above are arithmetic of the reviewer, in the tables of [`TGF-EWTW-GEN-001`](TGF-EWTW-GEN-001/README.md). These are consequences drawn by the reviewer. They are not quotations, and they choose no option.

- **The rule of the screening now has two tables beside it, to 30,000 ft, and they do not confirm it.** On a standard day at 25,000 and 30,000 ft the NASA engine gives 1 to 7 % more than the rule and the Rolls-Royce engine 8 to 20 % more, when the sea-level figure is the maximum rated power. Both give 28 to 53 % more when it is the maximum continuous power at rest. In the model of statement 2 the engine takes 1.09 times the air of the rule and gives 1.13 times its work for each kilogram: there both halves of the rule are low.
- **For the working reference the cruise still sizes the turbines.** At the nearest tabulated point, 30,000 ft and 350 kt, 5.6 MW ask 12.7 to 12.8 MW of maximum rated power at sea level, or 10.0 MW of maximum continuous power at rest, against 13.7 MW by the rule there and against 7.9 to 10 MW at take-off. Carried to 31,000 ft and 360 kt by the shape of the rule, a hypothesis, that is 13.1 MW against 14.1 MW. The climb, the installation, and the rating allowed after a failure with its duration are not in these figures.
- **A power referred to sea level has to name its rating.** The same 5.6 MW are 12.7 MW of one rating and 10.0 MW of another. The rule gives one number and cannot tell them apart.
- **The speed term of the rule is the least certain.** From rest to 350 kt at 25,000 and 30,000 ft the Rolls-Royce engine gains 9 to 10 %, the NASA engine 24 to 26 %, and the rule 22 to 23 %. The working reference is at 360 kt, where the term weighs most.
- **Above 30,000 ft the evidence is figures, not tables.** The working reference stands just outside what is tabulated, and 35,000 ft well outside.
- **Nothing read in regional service shows 0.350 from the fuel to the terminals.** With a generator at 0.97: 0.27 to 0.28 for the PW120A in flight, 0.31 for the model of the PW127E in cruise, 0.31 for the AE1107 as quoted, 0.34 to 0.35 for the models of the GE38 class at sea level, and 0.25 for the T56 on the bench. The value asks 0.361 on the shaft. A model of a current engine of 8.2 MW, above the class, has 0.395 on the shaft and 0.38 at the terminals.
- **The value for 2037 moves with the size of the unit, in the one family of models read.** With a generator at 0.97, its advanced models give 0.29 at 1 MW, 0.37 to 0.38 at 2.2 MW, 0.40 at 3.7 MW and 0.41 at 5.6 MW, all at sea level and at rest. Option B of this KNOT, many units of about 1 MW, and option A, few units of 2 MW or more, would not carry the same value on that line of the budget. It is one family of models, in which the technology and the layout change with the size: it gives no law for the count of the units.
- **A value of the budget has to name its boundary.** The shaft, the AC terminals and the DC bus differ by the generator and by the rectifier, and the electrical chain of the screening starts at the terminals. A rectifier counted on both sides is counted twice.
- **Part load weighs outside the cruise.** Turbines sized by the cruise give 7.9 to 10 MW of 12.7 MW at take-off, 62 to 79 % of their rating. Near its cruise rating the model of statement 2 loses under 1 % at 80 % of the power. The T56, a machine of one shaft, loses 14 % at 64 % on the ground. A straight line through the two points of the NASA engine, an assumption, loses 7 % at 70 %. No measurement at altitude settles it.
- **No turbogenerator has a mass on record, and the mass ratio of the budget compares two generations.** What is read are parts: a generator of 1 MW at 7 to 8 kW/kg, a prototype of 4 MW at 16 kW/kg for a power it has not run at, engine models at 6 to 16 kW/kg by size, a turboprop in service at 5.3 kW/kg with its gearbox. The 1.45 of the line *Mass of the propulsion system* divides a propulsion system of 2030 by an engine of today; against the conventional engine of the same year in the same table it is 2.02. The study is of a jet at Mach 0.8 with electric fans.
- **One concept of the class by its seats publishes its count: two units, at the wing tips, sized at the top of climb.** It is a jet at Mach 0.8. It narrows findings 16 and 17 of the record of 2026-11-15, and it gives no failure case.
- **Megawatt machines have run at conditions up to 45,000 ft and flown above 30,000 ft, in a chamber and in a parallel hybrid.** Neither is a gas turbine that only drives generators, and neither publishes a power or a voltage.
- **No scenario of the first budget changes.** A scenario stops being credible when the evidence of its line changes class. The two values of the turbogenerator and the mass ratio stay in class D.

## Not accepted

| Content | Report | Reason |
|---|---|---|
| That the data sheets list a consumption of 0.433 lb/(hp h) for the PW150A | C | The EASA sheet holds no consumption. The Canadian sheet was read by no one |
| Class A for the take-off power of the PW150A | C | Class A is for hardware representative of this aircraft |
| A cruise efficiency of 25 to 35 % for the class; a paper of 1993 with 36 % as a target; parametric studies of the PW127E; a conceptual turboshaft; Rolls-Royce turbogenerators of 500 to 1,200 kW | C | No source is named. The reviewer takes the conceptual turboshaft to be a paper of 2022 and read its abstract only |
| That the rule is consistent with the behaviour of published engine models | C | The tables read differ from it by 1 to 53 %, by engine and by the sea-level rating taken |
| Improvements of 1 to 2 % a year in summaries of ICAO | C | The [record of 2026-11-18](KNOT-EWTW-AER-001_icao-technology-goals_2026-11-18.md) holds 0.77 % and 1.03 % a year for the regional jet |
| That no megawatt hardware is reported at altitude | C | Statements 33 and 34. Its narrower finding, on a complete turbogenerator, stands as finding 51 |
| Class B, measured on hardware, for the efficiency and the specific power of the generator | A, C | Statement 25: the maker calls them a design value and a calculation |
| That no primary source tabulates power against altitude | A | Statements 9 and 10 |
| That the rule agrees within 3 % when the sea-level figure is the take-off rating | A | It held for one model at one point. Three models give 1 to 7 %, 8 to 20 % and 23 % more than the rule |
| 0.33 for the PW127XT-M in cruise | A | An inference from the fuel flow of statement 7 and a model point of another engine |
| Powers referred to sea level by scaling one published pair; 83 to 95 % of its cruise rating for the Dash 8-400 at 25,000 ft; a specific power for a turbine added to a generator | A | Each rests on one pair, on a figure of an encyclopaedia or on parts with different boundaries. They are illustrations |
| Half-load consumptions taken from two patents | A | An example in a patent is not a measurement |
| An author for the report of statement 3 | B | The document names none. The producer of B agrees |
| To hold the mass of 1,730 kg of the D-27 as unverified | The second reader | The reviewer read it twice on the English page of the maker. The disagreement between editions is kept, as statement 43 |
| Class B without reserve for the bench of statement 6 | The second reader | The reviewer could not read the paper in full, and the copy read is on a third-party host. The class is proposed on that account alone |

The method that report B proposes for the sizing by failure case is not a finding of sources, and B says so. It goes to `KNU-EWTW-GEN-001-02` as a proposal.

## Open

Research can still give:

- the power at 31,000 and 35,000 ft, read from figures 11 to 25 of the contractor report and reconciled with its tables;
- the paper of statement 6 at a copy of its publisher or of a library, to confirm the three lower powers, the uncertainties, and that the points are measurements;
- the Canadian data sheet of the PW150A, which report C cites and no one read;
- statements 41 to 44 at a place the reviewer can read;
- the altitude and the speed at which the maximum cruise power of the Dash 8-400 is delivered, open since the record of 2026-11-15 and not found.

Not public: the fuel consumption of the Rolls-Royce engines of statement 11, which the report withholds. Asking the maker is a decision of the programme.

The rest is work of the programme and decisions of the authority:

- whether the rule stays in the screening, with which sea-level rating, or whether the tables replace it up to 30,000 ft, when the screening is issued again;
- which engine stands for *today* on the line of the budget, and at which boundary: shaft, AC terminals or DC bus;
- how the size of the unit enters the line for 2037 and the criteria of this KNOT (`KNU-EWTW-GEN-001-03`);
- the basis of the mass ratio of the propulsion system;
- whether the footer that the data sheets of the Agency carry in their current layout, *Proprietary document. Copies are not controlled*, puts them under the rule of the brief on documents marked as proprietary. The second reader excluded one data sheet on that ground and read two others. The sheet of statement 1 is in the earlier layout, and the extract read shows no such line;
- the classes: this record proposes them and ratifies none.
