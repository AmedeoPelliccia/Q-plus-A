# Research record — electrical sources and role of energy storage

| | |
|---|---|
| KNOTs | `KNOT-EWTW-SRC-001` Electrical sources · `KNOT-EWTW-STO-001` Role of energy storage |
| Serves | `KNU-EWTW-SRC-001-01` to `-03` · `KNU-EWTW-STO-001-01`, `-02` and `-04`. Background for `-03`, which runs only if a propulsion or buffer battery is retained |
| Produced by | A research report of 2026-11-14, relayed by the author. The report does not name its producer |
| Brief | The research briefs of the KNUs of the two KNOTs, register 0.10.0 |
| Reviewed by | Claude, 2026-11-14 |
| Accepted | Ten statements read by the reviewer, seven as reported, ten findings of absence |

This record keeps what the review accepted from the research report. It is a reading of public sources, written in our own words. It recommends no option, and it states no conformity of the eWTW with any rule.

Batteries as the only source are excluded by ruling R2 of `KNOT-EWTW-NRG-001`, and fuel cells by R1. What is open is turbogenerators alone or with batteries, and the role of a battery if one is carried. No figure below is measured on an aircraft of 100 passengers: each statement gives the class.

---

## Accepted content

### Loads and the environmental control system

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 1 | The one transport in service without bleed air for the cabin is the Boeing 787. It carries two generators of 250 kVA on each engine and two of 225 kVA on the auxiliary power unit, at 235 V AC, with distribution at ±270 V DC. Wing ice protection, engine start, the large hydraulic pumps and the cabin air are electrical; bleed air stays for cowl ice protection and for pressurising the hydraulic reservoirs. These are ratings installed, not loads drawn | Boeing, Aero magazine, fourth quarter of 2007 | As reported: the archived copy could not be opened |
| 2 | A study calculates the electrical power demand of six types, from the A320-200 to the A380-800, by flight phase. It is a calculation from methods in the literature; it computes the air conditioning as the electric scheme of the 787, with cabin air compressors. None of the six is an aircraft of 100 passengers. As reported: air conditioning between about 25 kW, for an A320-200 in taxi, and about 650 kW, for an A380-800 in cruise, or 0.25 to 1.28 kW for each passenger | Voth, Lübbe and Bertram, Aerospace 11(12), 958, 2024 | 2026-11-14 for the method and the types; the figures are in a part of the page that was not read |
| 3 | A design optimisation of an electric environmental control system for the CeRAS single-aisle gives about 190 kW of electric power, about 1,500 kg and about 200 N of drag. The sizing covers hot, cold and standard days and the failure of a pack. It is a preliminary design and reports no test | Planès, Delbecq, Pommier-Budinger and Bénard, Aerospace 10(3), 260, 2023 | 2026-11-14 |
| 4 | A paper sizes an electric environmental control system for a turboprop of 80 passengers and reports a better efficiency than with bleed air. Another models a system like that of the 787 and reports 66 % less power with energy recovery, against its own model | AIAA 2024-3626, abstract; Yang, Zhang and Yang, Applied Thermal Engineering, 2017 | As reported |

### Sizing of the sources

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 5 | A study of a regional jet with hybrid turboelectric distributed propulsion, for entry into service around 2030, calculates a fuel saving of 19.9 % on a mission of 600 nm. The update adds the efficiency of the generator, the losses and the mass of the cables, the cooling of the battery through the environmental control system and that of motors and inverters, and a redundancy strategy that the abstract does not describe. It gives no mass for the generator | Perullo and others, An Update on Sizing and Performance Analysis of a Hybrid Turboelectric Regional Jet for the NASA ULI Program, 2020, abstract | 2026-11-14 |
| 6 | A model of a regional aircraft with a parallel hybrid chain that depletes its battery names four uses of the electric side: shaving the peak of power, boosting the climb, recharging in flight and taxiing. As reported: at an electric share of 10 % the mass of the battery has a floor near 115 kg, set by the current at take-off and not by the energy | Cinar and others, Modeling and Simulation of a Parallel Hybrid Electric Regional Aircraft for the Electrified Powertrain Flight Demonstration Program, NASA, 2023, abstract | 2026-11-14 for the abstract; the figure is not in it |

### Distribution and protection

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 7 | Three voltage levels are on record at three states of proof: ±270 V DC and 235 V AC in service on a wide-body; about 800 V DC flown on a six-seat aeroplane, with a battery that delivers up to 350 kW | Statement 1; Airbus, press release of 10 December 2024 ([record of the propulsion chain](KNOT-EWTW-PRP-001_propulsion-chain_2026-11-14.md), statement 1) | 2026-11-14 for the 800 V network |
| 8 | A solid-state circuit breaker for direct current of 1.2 kV and 1 kA was designed, built and tested, with targets of a response under 100 microseconds, an efficiency above 99.5 %, 100 kW/kg and operation at 35,000 ft. The programme states that it met or exceeded its metrics, in tests at steady load and in emulated altitude conditions. Commercial solid-state breakers are at 10 to 20 kW/kg and under 300 V | Raytheon Technologies for NASA, AC and DC Fault Management for Megawatt Electrified Aircraft Electrical Powertrains, task 1, June 2025, abstract | 2026-11-14 |
| 9 | The guidance on higher voltage in aircraft treats partial discharge and breakdown up to 1,500 V and 30 km, and was written for systems other than propulsion. The breakdown voltage of air falls with pressure, down to a minimum near 327 V at one product of pressure and gap | SAE AIR6127, reaffirmed in March 2023; Paschen's law | As reported: the page of the standard did not open |

### Batteries: service, rules and tests

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 10 | A propulsion battery is in service on a type-certificated two-seat aeroplane: two batteries, 24.8 kWh in total, about 70 kg each | Pipistrel, product page ([record of the energy carrier](KNOT-EWTW-NRG-001_energy-carrier_2026-11-14.md)) | 2026-11-14 |
| 11 | The fire of the auxiliary-power-unit battery of a Boeing 787 at Boston on 7 January 2013 began with an internal short circuit in one cell, and the thermal runaway spread to the cells beside it. The investigation finds that the design had no requirement to mitigate the most severe effects of such a short circuit, and that the certification did not identify the deficiency | NTSB, investigation DCA13IA037 | 2026-11-14 |
| 12 | The manufacturer had estimated that a cell would vent about once in ten million flight hours; two batteries failed before the fleet reached 52,000 hours. No test of thermal runaway had been asked for at certification. The aeroplane returned to service with a steel enclosure and a duct that vents it overboard, mandated in April 2013 | NTSB, incident report on the same event; FAA airworthiness directive | As reported |
| 13 | A special condition written for the lithium-ion batteries of the 787 requires safe cell temperature and pressure in normal and failed charging, no self-sustaining rise of temperature or pressure, and no accumulation of explosive or toxic gas in hazardous quantity | FAA special condition 25-359-SC | As reported |
| 14 | The minimum performance standard for rechargeable lithium batteries contains a test of containment of thermal runaway, triggered by overheat or overcharge. It records whether the trigger cells ran away, whether the case ruptured, what left the article, and voltages and temperatures against time. It is a test of an article for certification, not a method to correlate a cell model with a module | RTCA DO-311A, 19 December 2017 | As reported |
| 15 | The emergency-landing loads apply to any mass in the fuselage, and the safety assessment to its failure conditions | CS 25.561; CS 25.1309 | As reported |

### Demonstrators

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 16 | The E-Fan X, which would have put one electric fan on an airliner of about 100 seats, was cancelled before it flew | [Record of the propulsion chain](KNOT-EWTW-PRP-001_propulsion-chain_2026-11-14.md), statement 5 | 2026-11-14 |
| 17 | EcoPulse fed six wing propellers from a battery or from an auxiliary power unit on a six-seat aeroplane. The energy of the battery is not published | Same record, statement 1 | 2026-11-14 |

### Findings of absence

Ten statements say that a search found nothing. They are findings of the search, not properties of the world.

| # | Statement |
|---|---|
| 18 | No measured table of electrical loads, peak and continuous by phase, for a more-electric aircraft of 100 passengers |
| 19 | No figure for an electric environmental control system that is both measured and of this class |
| 20 | No published list of what is shed, by how much and in which failure, for an aircraft of this class |
| 21 | No weighed turbogenerator and no weighed battery for either open option at this class, and no published volume |
| 22 | No published hybrid of 100 passengers that states how many turbogenerators survive one failure, or whether a battery may be the survivor |
| 23 | No flight of a megawatt circuit breaker for direct current |
| 24 | No published segregation of the propulsion, systems and essential networks on an aircraft of this class |
| 25 | No replacement interval of a propulsion battery on a transport, and no public test that reports both a deep-discharge duty and a peak-shaving duty on one pack |
| 26 | No public test of containment and overboard venting of a pack large enough to propel an aircraft of 100 passengers |
| 27 | No programme that declared, before the test, the thresholds of correlation between a cell model and a module result; and no source that states a maturity an authority requires for each role of a battery |

---

## What follows for the eWTW

- **Three KNOTs now hold one open question.** Fuel with or without a propulsion battery (`NRG`, options B and C), turbogenerators alone or combined (`SRC`, options B and C), and the role of storage (`STO`) differ only in this: whether a propulsion battery is carried, and whether it carries energy of the flight or power at the peaks.
- **The mission screening tests one of the two roles.** Its option C makes the battery fly a share of the trip, which is the role of propulsive energy. A battery that only shaves the peak at take-off is a question of power and current (statement 6), and the screening does not size it.
- **Without a propulsion battery, option E of essential power has nothing to partition.** Turbogenerators alone leave the essential battery (`024-360`) and remove the propulsion one (`074`); the energy-carrier bay then holds no battery.
- **The role of a battery decides its failure condition.** A battery whose loss is also a loss of thrust is a different case, in the safety assessment, from one whose loss leaves the turbogenerators driving the propulsors. That is a criterion for `KNOT-EWTW-STO-001`, not a weight.
- **The environmental control system is the largest unknown among the loads other than propulsion.** The one sizing read, about 190 kW, is for a larger single-aisle and is a design result (statement 3). Against it stand an essential load of about 5 kW and a take-off power near 8.8 MW in our analyses. The profile by phase for this aircraft does not exist in the literature: it is ours to build.
- **The cruise altitude is missing here too.** It sets the margin against partial discharge, and so the voltage (statement 9), and the pressure ratio of the cabin air compressors. The record of the propulsion chain found the cruise Mach missing for the same reason.
- **A breaker of the right order exists on the bench.** At 1.2 kV and 1 kA it interrupts 1.2 MW. Nothing read has flown at that level, and a network above 1,500 V is outside the guidance read.
- **The propagation test has no public method to borrow.** The standard gives a certification test of an article. The thresholds of correlation that `KNU-EWTW-STO-001-03` asks for are ours to declare.

These are consequences drawn by the reviewer. They are not quotations.

## Not accepted

| Content of the report | Reason |
|---|---|
| That the source of the essential loads cannot share the electrical path of propulsion, as a finding on record | In the record it is criterion `M7` of `KNOT-EWTW-ESS-001`, proposed and not approved. Options C and E of that KNOT, a channel on the turbogenerator and a partition of the propulsion battery, are open |
| A distribution at 3,000 V and a battery of about 2 t for the E-Fan X | No source is given for either figure |
| A laboratory series of 2017 on cells below 2 Wh, with a vessel of 21.7 litres and heating at 20 °C a minute | The document is not identified by title or link |
| A trade article citing NASA for the breakdown minimum | Not identified. The value is kept in statement 9 as a property of air |
| The figures of the breaker as test results | The abstract gives them as targets and states that the programme met or exceeded its metrics; the measured values are not in it |
| An EASA special condition on non-rechargeable lithium batteries | The report itself does not use it for a rechargeable pack |

## Open

Research can still give:

- the article on the 787 and the standard AIR6127, read at the source. *Note of 2026-11-26: the research on the stand did not read the article at the source either; it has it as a forum quotes it. The 450 kVA of the auxiliary unit were read at its maker, and the three ground receptacles of 90 kVA in the airport planning document ([record of 2026-11-26](KNOT-EWTW-AUX-001_stand-supply-start-and-auxiliary-units_2026-11-26.md), statements 9, 12 and 39).*
- the figures of statement 2, and whether its method can be run for an aircraft of 100 passengers;
- the report of the investigation behind statement 12, with the special condition in full. *Note of 2026-11-26: the incident report was read for the research on the stand, in its parts on the battery and on the event, with a factual report of its docket on the tests; the figures of statement 12 were not checked in it ([record of 2026-11-26](KNOT-EWTW-AUX-001_stand-supply-start-and-auxiliary-units_2026-11-26.md), statements 16, 17 and 37). The special conditions were read on 2026-11-15 ([record of the certification basis](KNOT-EWTW-CRT-001_certification-basis_2026-11-15.md), statement 14).*
- sized electric environmental control systems for aircraft of 70 to 100 seats, with their cruise and cabin altitudes.

The rest is work of the programme and decisions of the authority:

- the cruise altitude and Mach of the eWTW;
- the load table by phase, starting from how the environmental control system is operated (`KNU-EWTW-SRC-001-01`);
- whether a propulsion battery is carried and in which role, and the size that follows (`KNU-EWTW-STO-001-01`);
- the number of turbogenerators and what survives a failure (`KNU-EWTW-SRC-001-02`);
- the voltage of the propulsion network and the diagram of the three networks (`KNU-EWTW-SRC-001-03`);
- the criteria of both KNOTs, with weights and thresholds, and their maturity records (`KNU-EWTW-STO-001-04`; `KNU-EWTW-PRP-001-01` for the sources).
