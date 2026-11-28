---
status: draft
standard_scope: governance
---

# ELA-EWTW-ESS-001 — Essential load analysis

| | |
|---|---|
| KNOT | [`KNOT-EWTW-ESS-001`](../../KNOT-EWTW-ESS-001.yaml) Essential power |
| Serves | `KNU-EWTW-ESS-001-01` Essential loads and duration |
| Version | 0.1.0 · 2026-11-14 |
| Prepared by | Claude, for review by `STK_SAF` |
| State | Pending review. Every load figure is an assumption |

This is a first list of the loads the eWTW keeps when its normal electrical generation is lost, with the power and the energy they need. Two research rounds found no published figure for an aircraft of the class ([record of 2026-11-14](../KNOT-EWTW-ESS-001_sources-and-precedents_2026-11-14.md), statement 10). The list is therefore built from the bottom up: the services that AMC 25.1351(d) normally names, one or more loads for each, and a low, a nominal and a high figure for each load.

The analysis gives an order of magnitude and shows which figures matter. It is not a requirement, and it states no conformity of the eWTW with any rule.

---

## How to read it

- [`essential-loads.yaml`](essential-loads.yaml) is the input: the scenario, the assumptions, the loads, the events and the parameters. To change the analysis, change that file.
- The section [Budget](#budget) is the output of [`tools/essential_loads.py`](../../../../../../../../../tools/essential_loads.py). It is written by the tool and checked against the input.
- A *load* is on for the whole endurance, or for the share given as duty. An *event* happens a counted number of times, at the landing or in manoeuvres.
- *Tier* follows CS 25.1351(d): services for immediate safety, which stay on without crew action; services for continued controlled flight; services for descent, approach and landing.
- *Feeds* is the number of independent essential feeds the load is assumed to need. It is an input to the segregation study, not its result.
- *Basis* says where a figure comes from: `assumption`, `source` or `design`. A figure with a source or a design value names its reference.

## What the budget shows

1. **The order of magnitude is a few kilowatts.** At nominal values the essential network draws between 4 and 5 kW from its source, and between 2 and 11 kW across the ranges. Peaks are about twice the continuous load.
2. **The power to move the flight controls decides the total.** It is over two fifths of the nominal load and more than half of the high one, and it is the least certain figure. Whether the surfaces keep hydraulic power is open (model README, section 3, row 8). It is the first figure to replace with a design value.
3. **The kind of source matters more than the list.** A store that covers the whole endurance is about six times the one that only bridges the start of another source. This is the difference between options A and E on one side and options B, C and D on the other, and it is where criterion `T1` is decided.
4. **A bridging store is sized by power.** A store with the energy for ten minutes discharges at nearly four times its capacity per hour, a rate that a store of that energy may not deliver. Its mass in the table is a lower bound.
5. **Little can wait.** About nine tenths of the nominal load is in the immediate tier. A source that takes time to start leaves nearly the whole load to the store meanwhile.
6. **Icing adds about a quarter.** Heating one windshield for half of the endurance raises the store from about 8 to about 10 kWh.
7. **The loads reach beyond the scope of the KNOT.** Ten chapters hold essential loads and are not in the `taxonomy` field of `KNOT-EWTW-ESS-001`. Extending the field is a decision of its owner.

## Limits

- **Every load figure is an assumption.** None comes from a source or from a design value. The two figures with a source are durations taken from the AMC as reported in the [record of 2026-11-13](../KNOT-EWTW-ESS-001_regulatory-basis_2026-11-13.md), which the reviewer did not read again at clause level.
- **The ranges are judgement.** They are not statistics, and the true value may lie outside them.
- **There is no flight profile.** A continuous load is an average over the endurance.
- **Mass is that of a battery alone.** The analysis gives no mass for a ram-air turbine, an auxiliary power module or a generator channel, and none for feeders and converters. It cannot rank the options.
- **Segregation is not analysed.** The analysis does not show that criteria `M3` and `M4` are met by any option.
- **Three demands are not sized:** the supply after an emergency landing (criterion `M6`), the motoring of a turbogenerator for a restart, and the load of the network before shedding.

*Note of 2026-11-27.* The research on ice protection has returned ([record](../KNOT-EWTW-ICE-001_ice-protection-without-bleed-air_2026-11-27.md)). It bears on assumption A6 and on the row *Wing, tail and propulsor ice protection* of what is not modelled, and it changes neither. The means of compliance says with what ice an aeroplane is shown after its ice protection fails: the ice of an unprotected part, or one half of it where the failure is announced and the crew is to leave icing as soon as possible, unless the agency agrees otherwise (statement 55). It is a rule on the ice to assume: it gives no time in icing, no power and no endurance. On two turboprops read, the procedure for an anomaly of a generator, and one event with both alternating-current buses lost, end with leaving icing (statements 41 and 67); their boots take their air from the engines and not from the network that was lost (statements 27 and 30). With electrical protection of wing and tail the protection is on that network. An eleventh mandatory criterion is proposed in `KNOT-EWTW-ICE-001` from that text. That the aircraft can leave icing conditions is still to be shown, by that KNOT, by `KNOT-EWTW-ESS-001` and by the propulsion together. This document is kept as issued.

*Note of 2026-11-28.* The research on the cooling cycle of the packs has returned ([record](../KNOT-EWTW-ECS-001_cooling-cycle-of-the-packs_2026-11-28.md)). On 2026-11-28 the author took the loss of one pack in flight as a design case of `LC-A` for `KNOT-EWTW-ECS-001`, with criterion E2 of that KNOT, and registered the assumption with `STK_SAF`, for whose review this document is prepared. The study takes 0.18 kg of fresh air per person and minute for periods over five minutes after a probable failure (statement 37). The formal classification of that failure condition stays open until the safety assessment, power supplies, controls and common causes included, and dispatch with one pack already inoperative is assessed apart. It changes no assumption of this analysis: assumption A5 is the loss of normal generation, after which the cabin is not pressurised by the alternate source and the packs are not supplied. This document is kept as issued.

## How to verify

From the repository root:

```bash
TAX="01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_S-ATLAS"
REG="01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
python3 tools/essential_loads.py "$REG/000_General/evidence/ELA-EWTW-ESS-001" "$REG" "$TAX" --check
python3 tools/essential_loads_test.py
```

The tool checks the form of the input: identifiers, S-ATLAS addresses, the order of low, nominal and high, duty, tiers, cases, the basis of each figure, and that the options named by a duration stand in the KNOT. With `--check` it fails when the section below differs from what the input gives. `--write` replaces the section. The arithmetic is in the function `budget`, and the tests compute it again by hand for the committed input.

---

## Budget

<!-- budget:begin -->
ELA-EWTW-ESS-001 0.1.0 for KNOT-EWTW-ESS-001: 23 loads, 5 events, 2 cases; 37 figures, 35 of them assumptions; rule failures: none

Scenario: In flight, the normal electrical generating system is lost. The alternate source supplies the essential network, and every load not listed here is shed. The flight continues to a descent, an approach and a landing, at least half of the time in instrument conditions. Thrust is not assumed either way: the list keeps the control power that lets the propulsion chain run or be recovered, and supplies no propulsive power.

### Loads

| Id | Service | Tier | Load | S-ATLAS | Low W | Nominal W | High W | Duty | Feeds | When | Basis |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| L01 | attitude-heading-airspeed-altitude | immediate | Flight displays of one pilot and the standby instrument | `031` Indicating and Recording Systems | 100 | 180 | 300 | 1 | 2 | always | assumption |
| L02 | attitude-heading-airspeed-altitude | immediate | Air data and inertial reference, one channel and the standby sensors | `034` Navigation | 60 | 120 | 200 | 1 | 2 | always | assumption |
| L03 | attitude-heading-airspeed-altitude | immediate | Probe heating: two pitot probes, one angle-of-attack vane, one temperature probe | `030` Ice and Rain Protection | 300 | 550 | 900 | 1 | 2 | always | assumption |
| L04 | communication | continued-flight | One VHF radio, receiving, with its transmissions averaged | `023` Communications | 20 | 40 | 80 | 1 | 1 | always | assumption |
| L05 | communication | continued-flight | Flight-deck audio, interphone and passenger address | `023` Communications | 30 | 60 | 120 | 1 | 1 | always | assumption |
| L06 | navigation | continued-flight | One navigation receiver: satellite navigation and instrument landing | `034` Navigation | 40 | 70 | 120 | 1 | 1 | always | assumption |
| L07 | navigation | continued-flight | One transponder — Not named by the AMC as recorded. Counted because the flight continues in controlled airspace | `034` Navigation | 25 | 45 | 80 | 1 | 1 | always | assumption |
| L08 | lighting | immediate | Flight-deck and instrument lighting | `033` Lights | 30 | 60 | 120 | 1 | 1 | always | assumption |
| L09 | flight-controls | immediate | Flight control computers and actuator electronics, the minimum channels | `027` Flight Control | 150 | 300 | 600 | 1 | 2 | always | assumption |
| L10 | flight-controls | immediate | Power to move the minimum set of surfaces, averaged over descent and approach — The largest figure and the least certain (A3). Its peaks are event E04 | `029` Actuation and Utility Power | 600 | 1500 | 5000 | 1 | 2 | always | assumption |
| L11 | propulsion-control-and-indication | immediate | Control electronics of the propulsors and of their converters — Stands for the engine control and engine instruments of the AMC | `077` Electric Propulsors Installation and Distributed Integration | 100 | 250 | 500 | 1 | 2 | always | assumption |
| L12 | propulsion-control-and-indication | immediate | Battery management, contactor holding and insulation monitoring of the propulsion storage — Applies where a propulsion battery is kept | `074` Propulsion Energy Storage Systems | 80 | 150 | 300 | 1 | 2 | always | assumption |
| L13 | warnings-and-cautions | immediate | Crew alerting and aural warnings | `031` Indicating and Recording Systems | 30 | 50 | 100 | 1 | 1 | always | assumption |
| L14 | platform | immediate | Integrated modular avionics: the cabinets that host the functions above | `042` Integrated Modular Avionics | 150 | 350 | 700 | 1 | 2 | always | assumption |
| L15 | platform | immediate | Essential distribution: bus controllers, contactors and data network | `024` Electrical Power | 60 | 120 | 250 | 1 | 2 | always | assumption |
| L16 | platform | continued-flight | Cooling of the essential avionics — Zero if natural convection is shown sufficient | `021` Air Conditioning Environmental Control | 0 | 150 | 400 | 1 | 1 | always | assumption |
| L17 | platform | immediate | Own consumption of the essential source: management and heating of its battery | `024-360` Aircraft Energy Storage | 20 | 60 | 200 | 1 | 1 | always | assumption |
| L18 | safe-landing | immediate | Fire and overheat detection: propulsion and battery bays, cargo, avionics | `026` Fire Protection | 30 | 60 | 120 | 1 | 1 | always | assumption |
| L19 | safe-landing | continued-flight | Cabin pressure control: outflow valve and controller | `021` Air Conditioning Environmental Control | 20 | 40 | 80 | 1 | 1 | always | assumption |
| L20 | safe-landing | continued-flight | Flight recorders | `031` Indicating and Recording Systems | 20 | 35 | 60 | 1 | 1 | always | assumption |
| L21 | safe-landing | continued-flight | Windshield heating, one pilot | `030` Ice and Rain Protection | 1500 | 2500 | 4000 | 0.5 | 1 | icing | assumption |
| L22 | propulsion-control-and-indication | continued-flight | Fuel delivery to one turbogenerator: boost pump and metering | `064` Carrier Delivery Metering and Conditioning | 150 | 400 | 800 | 1 | 1 | turbogenerator | assumption |
| L23 | propulsion-control-and-indication | immediate | Control unit of one turbogenerator, when it does not power itself | `068` Turbogenerators and Power Offtakes | 50 | 100 | 200 | 1 | 2 | turbogenerator | assumption |

### Events

| Id | Service | Tier | Event | S-ATLAS | Low W | Nominal W | High W | Seconds | Count | When | Basis |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| E01 | safe-landing | landing | Landing gear, alternate extension | `032` Landing Gear | 200 | 500 | 1500 | 15 | 1 | always | assumption |
| E02 | safe-landing | landing | Wheel braking on the landing roll | `032` Landing Gear | 1500 | 3000 | 6000 | 40 | 1 | always | assumption |
| E03 | flight-controls | landing | High-lift extension — Zero if the landing is made without high-lift | `027` Flight Control | 0 | 3000 | 6000 | 60 | 1 | always | assumption |
| E04 | flight-controls | immediate | Peaks of surface power above the average of L10 | `029` Actuation and Utility Power | 1500 | 4000 | 10000 | 5 | 20 | always | assumption |
| E05 | propulsion-control-and-indication | continued-flight | Ignition for a relight of one turbogenerator | `068` Turbogenerators and Power Offtakes | 150 | 300 | 500 | 60 | 2 | turbogenerator | assumption |

### Continuous load by service, base case

| Service | Loads | Low W | Nominal W | High W | Share of nominal |
|---|---:|---:|---:|---:|---:|
| attitude-heading-airspeed-altitude | 3 | 460 | 850 | 1400 | 20% |
| communication | 2 | 50 | 100 | 200 | 2% |
| navigation | 2 | 65 | 115 | 200 | 3% |
| lighting | 1 | 30 | 60 | 120 | 1% |
| flight-controls | 2 | 750 | 1800 | 5600 | 43% |
| propulsion-control-and-indication | 2 | 180 | 400 | 800 | 10% |
| warnings-and-cautions | 1 | 30 | 50 | 100 | 1% |
| platform | 4 | 230 | 680 | 1550 | 16% |
| safe-landing | 3 | 70 | 135 | 260 | 3% |
| **Total at the loads** | 20 | 1865 | 4190 | 10230 | 100% |

### Continuous load by tier, base case

| Tier | Loads | Nominal W | Share |
|---|---:|---:|---:|
| immediate | 13 | 3750 | 89% |
| continued-flight | 7 | 440 | 11% |

### Budget, base case

| | Low | Nominal | High |
|---|---:|---:|---:|
| Continuous load at the loads, kW | 1.86 | 4.19 | 10.23 |
| Continuous load at the source, kW | 2.07 | 4.66 | 11.37 |
| Peak demand at the source, kW | 3.74 | 9.10 | 22.48 |
| Events, kWh at the source | 0.07 | 0.22 | 0.50 |
| Energy for 60 min, kWh at the source | 2.14 | 4.87 | 11.87 |
| Energy for 30 min, kWh at the source | 1.10 | 2.55 | 6.18 |
| Energy for 10 min, kWh at the source | 0.35 | 0.78 | 1.89 |

### Battery by role, base case

| Role | Options | Minutes | Nameplate kWh, low · nominal · high loads | Mass kg | Range kg | Rate per hour |
|---|---|---:|---:|---:|---:|---:|
| Whole endurance on the store | A · E | 60 | 3.47 · 7.92 · 19.28 | 61 | 17–241 | 0.6 |
| Floor in instrument conditions | — | 30 | 1.79 · 4.14 · 10.05 | 32 | 9–126 | 1.1 |
| Bridge to a source that is not time-limited, events excluded | B · C · D | 10 | 0.56 · 1.26 · 3.08 | 10 | 3–38 | 3.7 |

Nameplate is the energy at the source divided by 0.9 × 0.95 × 0.8 × 0.9 = 0.616. Mass is at nominal loads and 130 Wh/kg. The range runs from low loads at 200 Wh/kg to high loads at 80 Wh/kg. It is the mass of the battery alone. Rate is the continuous power at the source over the nameplate energy.

### Cases

| Case | Average load added W | Continuous at the source kW | Nameplate for 60 min kWh | Mass kg at 130 Wh/kg |
|---|---:|---:|---:|---:|
| base | 0 | 4.66 | 7.92 | 61 |
| base + icing | 1250 | 6.04 | 10.17 | 78 |
| base + turbogenerator | 500 | 5.21 | 8.84 | 68 |
| base + icing + turbogenerator | 1750 | 6.60 | 11.09 | 85 |

Case `icing`: Instrument conditions with icing for half of the endurance.
Case `turbogenerator`: KNOT-EWTW-SRC-001 keeps a turbogenerator (its options B and C), which is controlled and can be relit.

### Assumptions

| Id | Assumption |
|---|---|
| A1 | CS-25 with its acceptable means of compliance is read as the certification basis. The basis of the eWTW and its amendment are not recorded yet |
| A2 | The services are those that AMC 25.1351(d) normally names, as recorded in the research record of 2026-11-13, statement 4, and not read again at clause level. Loads the AMC does not name are listed under the services platform and safe-landing |
| A3 | Flight controls are electrically signalled. How the surfaces are powered is open (model README, section 3, row 8). Load L10 stands for that power whatever the technology, electric actuators or an electric pump |
| A4 | Shedding is automatic. No load of the network before shedding is counted for the time the crew takes to recognise the failure |
| A5 | The cabin is not pressurised by the alternate source. The aircraft descends to an altitude where it is not needed, and oxygen needs no electrical power once released |
| A6 | The aircraft leaves icing conditions. Probes are heated. Wing, tail and propulsor ice protection is not supplied. Windshield heating is the case icing |
| A7 | The propulsion chain supplies its own cooling while it runs. If it is lost, it has nothing left to cool |
| A8 | One efficiency covers distribution and conversion for all loads |
| A9 | A continuous load is an average over the endurance. What happens only at landing is an event |
| A10 | Landing gear extension, braking and high-lift are electrically powered. Their technology is open (model README, section 3, rows 8 and 11) |

### Not modelled

| Item | S-ATLAS | Reason |
|---|---|---|
| Propulsive power | `077` Electric Propulsors Installation and Distributed Integration | Not an essential load: it is larger than the list by orders of magnitude. An option that supplies thrust from the essential source is another architecture |
| Cooling of the propulsion chain | `078` Thermal Management of Electric Propulsion | Supplied by the chain it cools (A7) |
| Motoring a turbogenerator for a restart | `068` Turbogenerators and Power Offtakes | No figure. If the essential source must supply it, it sizes the source. To be settled with KNOT-EWTW-SRC-001 |
| Cabin air supply and pressurisation | `021` Air Conditioning Environmental Control | Not supplied (A5) |
| Wing, tail and propulsor ice protection | `030` Ice and Rain Protection | Not supplied (A6). That the aircraft can leave icing conditions is to be shown |
| Automatic flight | `022` Auto Flight | Not supplied: the flight is flown by hand. The workload over the endurance in instrument conditions is to be assessed |
| Cabin emergency lighting and escape path marking | `033` Lights | Assumed to carry their own batteries |
| Supply after an emergency landing or a ditching (criterion M6) | `024-230` Emergency Backup Power | Not sized. It adds a reserve to a time-limited source |
| Inerting or venting of the energy-carrier bay | `047` Inerting and Protective Atmospheres | No figure. It follows the safety case of the bay |
| Load of the network before shedding | `024` Electrical Power | Not counted (A4). If shedding is manual, the unshed load runs for the recognition time |
| Galley, cabin systems and information systems | `046` Information Systems | Shed |

Chapters of loads outside the `taxonomy` field of `KNOT-EWTW-ESS-001`: `021` · `027` · `029` · `030` · `032` · `033` · `064` · `068` · `074` · `077`.
<!-- budget:end -->

---

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-14 | First issue: 23 loads and 5 events from the services of AMC 25.1351(d), two cases, three durations. Every load figure is an assumption |
