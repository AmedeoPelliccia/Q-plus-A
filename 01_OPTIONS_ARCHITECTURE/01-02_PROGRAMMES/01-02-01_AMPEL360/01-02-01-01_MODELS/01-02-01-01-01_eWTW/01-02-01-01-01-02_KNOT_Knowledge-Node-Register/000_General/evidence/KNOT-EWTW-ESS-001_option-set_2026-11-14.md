# Option set — essential power

| | |
|---|---|
| KNOT | `KNOT-EWTW-ESS-001` Essential power |
| Serves | `KNU-EWTW-ESS-001-02` Essential source options |
| Prepared by | Claude, 2026-11-14, for review by `STK_SAF` |
| Rests on | The research records of [2026-11-13](KNOT-EWTW-ESS-001_regulatory-basis_2026-11-13.md) and [2026-11-14](KNOT-EWTW-ESS-001_sources-and-precedents_2026-11-14.md), and the [essential load analysis](ELA-EWTW-ESS-001/README.md) |
| State | Pending review. Five options registered as `open`. None is scored |

This record defines the option set of the KNOT. It says what each option is, with which electrical sources it can exist, and what it shares with the propulsion chain. It does not rank the options: the criteria of the KNOT are proposed, and no option is scored before they are approved (CM-004, rule 5). It states no conformity of the eWTW with any rule.

---

## The five options

| Option | Source | Limited in time | Store it needs | Product elements |
|---|---|---|---|---|
| A | A dedicated essential battery | Yes. It carries the whole endurance of criterion `M5` | Itself | Updates `essential-battery-installation` at `024-360` |
| B | A ram-air turbine | No, while airspeed holds | A battery that bridges its deployment and takes over at low speed | Creates `ram-air-turbine-installation`, filed at `024-230`. Updates the essential battery |
| C | A segregated generator channel on the turbogenerator | No, while the turbogenerator runs | A battery that bridges the transfer | Updates `turbogenerator-installation` at `068`. Updates the essential battery |
| D | An auxiliary power module | No, while it has its energy carrier | A battery that bridges its start | Creates `auxiliary-power-module` at `049`. Updates the essential battery |
| E | A reserved partition of the propulsion battery | Yes. It carries the whole endurance | None of its own | Updates `propulsive-battery-installation` at `074`. Creates `propulsion-battery-essential-feed` at `076-700` |

The essential battery is created by option C of `KNOT-EWTW-STO-001`. The turbogenerator belongs to `KNOT-EWTW-SRC-001` and the propulsion battery to `KNOT-EWTW-NRG-001`. The [architecture relations](../../../01-02-01-01-01-03_REL_Architecture-Relations/README.md#projections) check these footprints against the candidates of the taxonomy.

## With which electrical sources each option can exist

`KNOT-EWTW-SRC-001` has three options: A, batteries alone; B, a turbogenerator; C, both. Ruling R2 of `KNOT-EWTW-NRG-001`, of the same day, excludes option A; its column stays for the record.

| Option | `SRC` A, batteries | `SRC` B, turbogenerator | `SRC` C, both | Condition |
|---|:-:|:-:|:-:|---|
| A dedicated battery | Yes | Yes | Yes | — |
| B ram-air turbine | Yes | Yes | Yes | — |
| C generator channel | No | Yes | Yes | There is a turbogenerator to carry the channel |
| D auxiliary power module | Yes | Yes | Yes | Where the aircraft carries no fuel, the module needs an energy carrier of its own. Its technology is open (model README, section 3, row 15) |
| E battery partition | Yes | No | Yes | There is a propulsion battery to partition |

## What each option shares with the propulsion chain

This is the question of the proposed criterion `M7`. The table is the reviewer's analysis of each architecture. It is not drawn from a source, and it is not a safety assessment.

| Option | Independent of the propulsion chain in | Shares with it | On record |
|---|---|---|---|
| A | Cells, protection and feeders, when it is installed outside the propulsion battery bay and charged through an isolating charger | The charging supply. The cell chemistry and the bay, if they are those of the propulsion battery | Batteries as the time-limited source are the case AMC 25.1351(d) describes (record of 2026-11-13, statements 5 and 6) |
| B | Prime mover and generator: it is driven by the airflow | Nothing electrical upstream of the essential network. It depends on airspeed, and on its deployment | Fitted to the Embraer 190, where it supplied the essential buses about eight seconds after the loss (record of 2026-11-14, statements 1 to 3) |
| C | Windings, converter and feeders of the channel | The prime mover and its fuel. A failure that stops the turbogenerator removes the normal source and the channel together, unless a second turbogenerator carries another channel | No authority is known to have ruled on a generator of the propulsion chain as the alternate source (record of 2026-11-14, statement 9) |
| D | Prime mover and generator | The fuel, where it draws from the tanks that feed the turbogenerator. It depends on starting at altitude after a cold soak | AMC 25.1351(d) names an auxiliary power unit and asks for its limits of speed, attitude and altitude (record of 2026-11-13, statement 7) |
| E | The feed to the essential network, if segregated | Cells, bay, battery management and high-voltage protection. A thermal event or a fault that removes the propulsion battery can remove the partition | SC E-19 lets a propulsion battery power aircraft systems and does not say whether it can be the alternate source. No precedent is known (record of 2026-11-14, statements 4, 8 and 9) |

## What the load analysis adds

At nominal values the essential network draws between 4 and 5 kW from its source ([`ELA-EWTW-ESS-001`](ELA-EWTW-ESS-001/README.md), where every load figure is an assumption).

- **Options A and E carry the whole endurance.** The store is about 8 kWh at nominal loads, and between about 3 and 19 kWh across the ranges.
- **Options B, C and D carry a bridge.** The store is about a sixth of that. It is sized by power, because about nine tenths of the load cannot wait for the source to start.
- **The analysis gives no mass for a turbine, a module or a generator channel.** It cannot compare the two groups on criterion `T1`.

## Open

| Point | For |
|---|---|
| The `taxonomy` field of the KNOT does not include `068` and `074`, where options C and E have footprints | Owner of the KNOT, on accepting this set |
| The ram-air turbine has no S-ATLAS node. Option B files it at the nearest one | Taxonomy owner |
| The essential battery exists in the register only through option C of `KNOT-EWTW-STO-001`. Four options here update it. An essential battery may be needed whatever role storage is given | Owners of the two KNOTs |
| Mass, rating and installation of a ram-air turbine, of an auxiliary power module and of a generator channel for a load of this size | A study of each, with sources that can be checked. Two research rounds found none |
| Whether an authority accepts a generator of the propulsion chain, or a partition of the propulsion battery, as the alternate source | The authority, through the certification basis |
| Criteria, weights, thresholds and the maturity required of each source | `KNU-EWTW-ESS-001-03` |
