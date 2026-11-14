# Research record — emergency sources of the class and precedents

| | |
|---|---|
| KNOT | `KNOT-EWTW-ESS-001` Essential power |
| Serves | `KNU-EWTW-ESS-001-01` · `KNU-EWTW-ESS-001-02` · `KNU-EWTW-ESS-001-03` |
| Produced by | Grok 4.7 with its research agents, report of 2026-11-14 |
| Brief | The research briefs of the three KNUs as revised on 2026-11-13, register 0.6.0 |
| Reviewed by | Claude, 2026-11-14 |
| Accepted | Two sources read by the reviewer, and three findings of absence as reported |

This record follows the [record of 2026-11-13](KNOT-EWTW-ESS-001_regulatory-basis_2026-11-13.md). It keeps what the review accepted from the second report. It states no conformity of the eWTW with any rule.

---

## Accepted content

| # | Statement | Source | Read by the reviewer |
|---|---|---|---|
| 1 | On the Embraer 190, a ram-air turbine is commanded to deploy automatically when the main AC buses lose power, and it can be deployed by hand. It powers the AC essential bus and the two DC essential buses | TSB Canada, Aviation Investigation Report A16O0066, *Electrical system description* | 2026-11-14 |
| 2 | In that occurrence the turbine was supplying the essential buses about eight seconds after the main buses lost power | TSB Canada A16O0066, *Sequence of electrical failure and fire* | 2026-11-14 |
| 3 | If the turbine does not deploy, the batteries of that aircraft maintain essential power for a minimum of ten minutes, as demonstrated in certification tests | TSB Canada A16O0066, *Electrical system description* | 2026-11-14 |
| 4 | A propulsion battery is a battery meant to power the electric engines. It can also power other sub-systems of the propulsion system or systems of the aircraft | EASA SC E-19, Issue 1, definitions | 2026-11-14 |
| 5 | The electrical generation, distribution and wiring of the propulsion system meet the type-certification basis of the aircraft and supply the connected loads in all intended operating conditions | EASA SC E-19, Issue 1, EHPS.370 | 2026-11-14 |
| 6 | The propulsion battery and its management system meet the type-certification basis of the aircraft and supply the power the electric engines need for the mission | EASA SC E-19, Issue 1, EHPS.380 | 2026-11-14 |
| 7 | For CS-25 aircraft the special condition is to be complemented with emissions requirements that are not defined yet. CS-25 is not excluded from it | EASA SC E-19, Issue 1 | 2026-11-14 |
| 8 | The special condition does not say whether a propulsion battery can be the alternate source of CS 25.1351(d) | EASA SC E-19, Issue 1 | As reported |
| 9 | No certification authority is known to have accepted, refused or conditioned a propulsion battery, or a generator of the propulsion chain, as that alternate source on a CS-25 aircraft | Absence of a source | As reported |
| 10 | No public source gives the essential loads in kilowatts for an aircraft of the regional class, electric or not | Absence of a source | As reported |
| 11 | No public source gives a maturity that an authority has accepted for a new essential source, or weights and thresholds for the trade between sources | Absence of a source | As reported |

Statements 9 to 11 report that a search found nothing. They are not proof that nothing exists.

## What follows for the eWTW

- **Endurance depends on the kind of source.** Where the architecture has a source that is not time-limited, as on the Embraer 190, the batteries only bridge its start and cover a short demonstrated time. Where batteries are the only alternate source, the floor of criterion `M5` falls on them in full. Endurance, and with it mass (`T1`), is the main difference between the two kinds of option.
- **A propulsion battery as the alternate source has no precedent.** The special condition allows a propulsion battery to power aircraft systems and is silent on the alternate source. An option that relies on it carries the whole burden of showing criterion `M7`.
- **The load list is ours to build.** With no published figure, the essential loads of the eWTW are estimated bottom-up from the functions of AMC 25.1351(d), with every assumption stated.

These are consequences drawn by the reviewer. They are not quotations.

## Not accepted

| Content of the report | Reason |
|---|---|
| Ratings of the ram-air turbines and air-driven generators of regional types | Taken from descriptions of operating manuals. The investigation report cited for one of them does not give the rating |
| Battery capacities and endurance of two turboprop types | The sources are training descriptions or are not identified |
| That SC E-19 excludes CS-25 aircraft | The special condition says otherwise (statement 7) |

## Open

Research has given what it can. What remains is work of the programme and decisions of the authority:

- the essential load analysis of the eWTW (`KNU-EWTW-ESS-001-01`);
- the option set of the KNOT, with the product footprint of each option (`KNU-EWTW-ESS-001-02`);
- approval of the criteria, with weights, thresholds and the maturity required of each source (`KNU-EWTW-ESS-001-03`).
