# Research record — generation architecture

| | |
|---|---|
| KNOT | `KNOT-EWTW-GEN-001` Generation architecture |
| Serves | `KNU-EWTW-GEN-001-01` and `-03`. It gives `-02` the units on record and leaves it the fall of power with altitude |
| Produced by | A research report of 2026-11-15, relayed by the author. The report does not name its producer |
| Brief | The research briefs of the KNUs of `KNOT-EWTW-GEN-001`, register 0.11.3 |
| Reviewed by | Claude, 2026-11-15 |
| Accepted | Ten statements read by the reviewer, three as reported, six findings of absence |

This record keeps what the review accepted from the research report. It is a reading of public sources, written in our own words. It recommends no option, and it states no conformity of the eWTW with any rule.

A turbogenerator is a main source of the eWTW since ruling R1 of `KNOT-EWTW-SRC-001`. What is open here is how many units, of what rating, and where.

---

## Accepted content

### Units that have run

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 1 | A generator of 1 MW for hybrid-electric aircraft operated at 1.02 MVA, about 1 MW at unity power factor, and ran continuously at 900 kW. It weighs 280 lb. Its maker gives it about 8 kW/kg and about 97 % efficiency, and says it can be joined to the gas turbines it already builds to make a turbogenerator. Development and qualification were to follow. The release reports no flight | Honeywell, press release, Phoenix, 31 May 2022 | 2026-11-15 |
| 2 | The turbogenerator the maker proposes joins that generator to its HGT1700 auxiliary power unit. The generator weighs 280 lb, 127 kg | Aerospace Testing International, 6 June 2022 | 2026-11-15 |
| 3 | The HGT1700 is the auxiliary power unit of the Airbus A350. The generator measures 14 by 24 inches | Trade press | As reported |
| 4 | The TG600 is a turbogenerator that supplies 600 kW of electricity, built on the Arrano turboshaft. Its first bench test was in July 2026, at Bordes. It is developed and will be produced for the Electra EL9, for which a type certificate under Part 23 has been applied for; the first order is for 250 units | Safran, press release of 15 July 2026; Aviation International News, 15 July 2026 | 2026-11-15. That the EL9 has nine seats is as reported |
| 5 | A generator that has to deliver 2.5 MW, described as no bigger than a beer keg, was developed and tested in Trondheim and delivered in July 2021 to a test bed in Bristol, where it is driven by an AE2100 gas turbine, with power electronics at 3,000 V. The system delivered more than 1 MW there, and testing continued with the aim of 2.5 MW. No page read gives a mass or a dimension | Rolls-Royce, account of the power generation system, 2021; New Atlas, 27 July 2021; Aerospace Testing International, two articles whose pages give no date | 2026-11-15 |
| 6 | Rolls-Royce and Airbus agreed to conclude the E-Fan X programme, from which that system came. The ground tests of the power generation system were to be completed | Airframer, page dated 08/05/2020 | 2026-11-15 |
| 7 | The E-Fan X was to replace one of the four engines of a BAe 146 by an electric motor of 2 MW, with the gas turbine and the generator in the rear fuselage. It was cancelled in April 2020 before it flew | [Record of the propulsion chain](KNOT-EWTW-PRP-001_propulsion-chain_2026-11-14.md), statement 5, for the motor and the cancellation | As reported for the rear fuselage |

EcoPulse flew an auxiliary power unit of 100 kW that could feed its six electric propellers. It is statement 1 of the record of the propulsion chain, and it is not a machine of this class.

### Counts and failure cases in published concepts

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 8 | A study of a hybrid turboelectric regional jet for service in 2030 updates its conversion links, the efficiency of the generator, the cable losses and the redundancy strategy of the propulsion system, and gives a fuel saving of 19.9 % on a mission of 600 nmi against its baseline. Its abstract gives no number of generators and no number of seats | Perullo, Shi, Cinar, Alahmad, Sanders, Mavris and Benzakein, An Update on Sizing and Performance Analysis of a Hybrid Turboelectric Regional Jet for the NASA ULI Program, August 2020, record of the Georgia Tech repository | 2026-11-15, the abstract. The paper number AIAA 2020-3590 is as reported |
| 9 | The SUSAN concept carries 180 passengers at Mach 0.78 over a design range of 2,500 miles. One turbofan in the tail, which takes in the boundary layer, gives thrust and drives four main generators on its low-pressure shaft; up to 20 MW of electrical power can be taken from it. Sixteen electric fans, eight under each wing, take that power. A primary battery is used once, only when the turbine or a generator fails, and gives power for about 300 miles, some 30 minutes. The report says that a commercial aircraft with a single turbofan presents a certification problem, which the battery is meant to answer | NASA, TM-20210026061, Subsonic Single Aft Engine (SUSAN) Transport Aircraft Concept and Trade Space Exploration | 2026-11-15 |
| 10 | Fourteen airline pilots flew that concept in a simulator. The failures were of one electric engine, of four placed symmetrically and of eight not symmetrically, and of the turbine, complete and partial, in critical phases of flight | NASA, Flight Deck Design of a Hybrid Turbine/Electric Passenger Aircraft, NTRS 20240010871, library record; NASA, Flightcrew Thrust Control and Engine Display Concepts for the SUSAN Transport Aircraft, NTRS 20220016684, abstract | 2026-11-15 |

### Rules

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 11 | The powerplants are arranged and isolated from each other so that the failure of an engine, or of a system that can affect it, does not prevent the continued safe operation of the other engines and does not require immediate action by the crew. For turbine engine installations, design precautions are taken to minimise the hazards to the aeroplane from an engine rotor failure and from a fire that starts in the engine and burns through its case. Each auxiliary power unit is approved, or meets the requirements of the category for its intended use | 14 CFR 25.903(b), (d)(1) and (f) | 2026-11-15. CS 25.903, which the report cites, was not read |
| 12 | An advisory circular gives one way to show that paragraph (d)(1) is met, for engines and for auxiliary power units; it is not mandatory. It models a single fragment of one third of a disc, thrown within 3 degrees either side of the plane of the rotor, an intermediate fragment within 5 degrees and small fragments within 15 degrees. Its design goals are not more than 1 chance in 20 of a catastrophe for the single one-third fragment, 1 in 40 for the intermediate fragment and 1 in 10 for several disc fragments. For an auxiliary power unit the installer also treats debris, up to a complete rotor, that leaves through the tailpipe | FAA, AC 20-128A, 25 March 1997 | 2026-11-15. AMC 20-128A, which the report cites, was not read |

### Criteria

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 13 | Published designs choose the number and the position of generating units by the mass of the installation, the redundancy needed to survive one failure, the difficulty of containing a rotor burst or a fire, noise, and access for maintenance | The report, from the designs it read | As reported: no design is named |

### Findings of absence

Six statements say that a search found nothing. They are findings of the search, not properties of the world.

| # | Statement |
|---|---|
| 14 | No turbogenerator of the megawatt class that has flown as the propulsive source of an aeroplane of 70 to 100 seats |
| 15 | No weighed mass and no measured volume for the generator of statement 5, and no mass of a turbine together with its generator for any unit above |
| 16 | No concept of 70 to 100 seats that publishes the number of its units together with the power to be left after the loss of one. No source says that the loss of one unit must leave the take-off power, nor that it may leave only the cruise power |
| 17 | No published fall of power with altitude for a turbogenerator, and no concept that publishes the altitude at which its units are sized |
| 18 | No published inlet, exhaust, fire zone or rotor-burst geometry for a turbogenerator installation of several megawatts on an aeroplane of 100 seats, in a fuselage bay or in a wing pod, and none shown against the rules of statements 11 and 12 |
| 19 | No weights for the criteria of a generation architecture that an authority has approved |

---

## What follows for the eWTW

- **Nothing on record is a turbogenerator of the size the eWTW needs.** What has run is a generator of 1 MW tested by itself (statement 1), a turbogenerator of 600 kW on a bench since July 2026 for an aircraft under Part 23 (statement 4), and a generator meant for 2.5 MW that had passed 1 MW with its turbine on a bench (statement 5). None has flown. The [screening of the cruise points](CRP-EWTW-CRZ-001/README.md) asks between 5.3 and 9.9 MW in cruise at the terminals of the generators. In either option of this KNOT the eWTW needs several units of a kind that has not flown.
- **The mass on record is that of a generator.** The 127 kg of statements 1 and 2 are the generator, and 1 MW over 127 kg is the 8 kW/kg its maker states. The turbine is not in it. The mass of installed generation stays without a source (finding 15, and finding 21 of the [record of the sources](KNOT-EWTW-SRC-001_sources-and-storage_2026-11-14.md)).
- **The research does not give the fall of power with altitude, so the screening now states a rule.** A gas turbine held at one point of its map takes in air in proportion to the total pressure at its inlet over the square root of the total temperature. At the four cruise points that air flow is 56, 50, 47 and 38 % of the flow at sea level and at rest. If the machines give the same work for each kilogram of air, the cruise power referred to sea level is 9.6, 13.9, 15.3 and 26.1 MW, against 8.8 to 9.0 MW at take-off. The rule is an assumption of first order, declared as one in the screening, and no machine on record confirms it (finding 17).
- **At that rule the cruise sizes the gas turbines at every point, and the count of nine units does not hold.** The mission screening counts nine turbogenerators of 1,000 kW for the take-off. At the slowest cruise point they would give 5.0 MW, below the 5.3 MW the cruise asks. Units of 1 MW would number between 10 and 27 by cruise point, and units of 2.5 MW between 4 and 11, before any failure case. These counts follow the rule and move with it.
- **A battery for the take-off peak does not reduce turbogenerators that the cruise sizes.** The record of the cruise point said so with a condition. The rule removes the condition: at every point the cruise referred to sea level is above the take-off power, by 9 % at the slowest and nearly three times at the jet point. It is an input to `KNOT-EWTW-STO-001`: a buffer battery then has to earn its mass elsewhere, in the failure case or in the transients.
- **A generating unit has two counts.** In statement 9 one turbine drives four generators. The loss of a generator and the loss of a turbine are different failure cases, and the options of this KNOT count turbogenerators as if they were one. `KNU-EWTW-GEN-001-02` has to count turbines and generators apart.
- **The one concept that states its failure cases has a single turbine and answers its loss with a battery.** It is not of the class: 180 passengers, and a turbofan that gives thrust itself. It shows a third answer to the failure case, a battery as the survivor, which finding 22 of the record of the sources left open and which belongs to `KNOT-EWTW-STO-001`.
- **Which rule governs a turbogenerator is not settled.** Statement 11 names engines and auxiliary power units, and statement 12 treats the two differently. A gas turbine that gives no thrust and drives generators for propulsion is named in neither. That is a question of the certification basis, and it is added to the brief of `KNU-EWTW-CRT-001-02`. Note of the same day: the [record of the certification basis](KNOT-EWTW-CRT-001_certification-basis_2026-11-15.md) reads a certification memorandum that puts a turbogenerator used for propulsion under the definition of an engine (its statement 13).
- **The method for rotor burst gives the geometry of the position question.** Fragments leave within a few degrees of the plane of each rotor (statement 12). The positions `P1` and `P2` differ in what lies in those planes: other units, the pressure cabin, the fuel. No published installation gives it (finding 18), so it is work of the programme, with `KNOT-EWTW-FUL-001`, which places the fuel.

These are consequences drawn by the reviewer. They are not quotations.

## Not accepted

| Content of the report | Reason |
|---|---|
| A mass of 127 kg for the power unit, the generator with the HGT1700 | The press release gives 280 lb as the weight of the generator. The article the report follows gives the same figure once for the generator and once for the power unit |
| That the generator of 2.5 MW ran on a bench in Trondheim in 2019 | No page read gives 2019. The maker places the end of the generator trials in Trondheim and the first run with the turbine in Bristol in 2021. That the system reached 2.5 MW was not read |
| The SUSAN concept among the concepts of the class | It carries 180 passengers, and its one turbine is a turbofan that gives thrust |
| That CS 25.903(b) and (d) and AMC 20-128A apply to the turbogenerators | The texts read name engines and auxiliary power units. Which of them governs a gas turbine that only drives generators for propulsion is for `KNOT-EWTW-CRT-001` |
| Thrust at 35,000 ft of the order of 20 to 30 % of its static value at sea level, as the fall of power of the units | No source is named, and the figure is for the thrust of turbojets and turbofans, not for shaft power. The report itself calls it an order of magnitude |
| That the screening is consistent with the direction of the fall of power | The cruise power of the screening is what the aircraft asks, from its speed and drag. It says nothing of what a machine gives at altitude |
| Parallel-hybrid regional models of NASA with 10 % of the take-off power electric | No document is identified |
| That the failure case examined most often is the loss of one generating unit or of one propulsor | One concept read states its failure cases (statement 10). There is no count behind "most often" |

The [record of the sources](KNOT-EWTW-SRC-001_sources-and-storage_2026-11-14.md) did not accept a distribution at 3,000 V for the E-Fan X, for want of a source. Statement 5 now gives 3,000 V, read at the maker, for the power electronics of the system on the bench.

## Open

Research can still give:

- the power of a turboshaft or of an auxiliary power unit of the megawatt class against altitude and speed, from a type-certificate data sheet, an installation manual or a chart of the maker, to replace the rule of the screening;
- the altitude and speed at which the maximum cruise power of the Dash 8-400 is delivered, which the check of the screening on its published point takes at the cruise point;
- the mass of a turbine together with its generator, for the units of statements 2, 4 and 5;
- the redundancy strategy and the number of units of the study of statement 8, in the full paper;
- CS 25.903 and AMC 20-128A at the amendment in force, read at the source.

The rest is work of the programme and decisions of the authority:

- the sizing by failure case, at each cruise point and for each role of storage, with turbines and generators counted apart (`KNU-EWTW-GEN-001-02`);
- the power to be left after the loss of one unit, which is a criterion to approve and not a result of research (`KNU-EWTW-GEN-001-03`);
- the count of nine turbogenerators in the mission screening and in the candidates of the TPMS view, to be restated when that sizing exists;
- the rule that governs a turbogenerator, in the certification basis (`KNOT-EWTW-CRT-001`);
- the coupling of the position of the units with the place of the fuel (`KNOT-EWTW-FUL-001`), which the records do not yet state.
