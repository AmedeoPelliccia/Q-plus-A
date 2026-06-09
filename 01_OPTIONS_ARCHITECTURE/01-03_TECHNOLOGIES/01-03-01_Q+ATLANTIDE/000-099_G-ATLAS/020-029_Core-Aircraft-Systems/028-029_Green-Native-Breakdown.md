---
node: 020-029
title: Core Aircraft Systems — G-ATLAS Green-Native Breakdown (028, 029)
band: 000-099_G-ATLAS
master_range: 020-029
ssot_path: "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_G-ATLAS/020-029_Core-Aircraft-Systems"
nodes_in_this_file: ["028 Energy-Carrier Storage and Distribution", "029 Actuation and Utility Power"]
view: green-native (canonical)
heritage_source: "ATA breakdown, Embraer 170/175/190/195 and Lineage 1000 (chapters 28 Fuel, 29 Hydraulic Power)"
principle: "The deepest substitutions in the band: Fuel -> energy carrier; centralized Hydraulics -> distributed electric. Conventional architecture demoted to heritage footprint."
numbering_map: "ATA CC-SS-UU  →  G-ATLAS 0CC-SS0-UU0"
owner_028: Q-GREENTECH
owner_029: Q-AIR
green_overlay: Q-GREENTECH
governance: [LC-A..LC-N, No-AAA, SSOT+PUB, G-ATLAS-NORM-TERM-001]
status: baseline
version: "1.0"
completes: "020-029 master range (020-029 all green-native)"
---

# 020-029 — Core Aircraft Systems · Green-Native Breakdown (028 · 029)

The two deepest substitutions in the band. **028** was "Fuel"; under a green architecture *fuel is the energy carrier*, so the chapter becomes **Energy-Carrier Storage and Distribution** — a near-total substitution. **029** was "Hydraulic Power"; once actuation electrifies (chapter 27 → EHA/EMA), the centralized hydraulic system gives way to **Actuation and Utility Power** drawn from the HVDC bus (`024-900`). Both conventional architectures move almost wholly to the heritage footprint.

---

## Index

- <a href="#glossary">Glossary</a>
- <a href="#1-green-native-doctrine-for-028--029">1. Green-Native Doctrine for 028 / 029</a>
- <a href="#2-numbering-map">2. Numbering Map</a>
- <a href="#3-chapter-028--energy-carrier-storage-and-distribution">3. Chapter 028 — Energy-Carrier Storage and Distribution</a>
- <a href="#4-chapter-029--actuation-and-utility-power">4. Chapter 029 — Actuation and Utility Power</a>
- <a href="#5-programme-binding--ewtw--hbwb">5. Programme Binding — eWTW / hBWB</a>
- <a href="#6-governance">6. Governance</a>
- <a href="#references">References</a>
- <a href="#conventional-heritage-footprint">Conventional Heritage Footprint</a>

---

## Glossary

| Term | Meaning |
|---|---|
| **Energy carrier** | Architecture-neutral term for the stored propulsion energy (electrical charge, cryogenic hydrogen, …). |
| **SoC / SoH** | State of Charge / State of Health — the energy-carrier analogues of fuel quantity and condition. |
| **BMS** | Battery Management System — cell monitoring, balancing, protection (no conventional analogue). |
| **Boil-off** | Evaporative loss from a cryogenic store; the H₂ analogue of tank venting. |
| **EHA / EMA** | Electro-Hydrostatic / Electro-Mechanical Actuator — distributed electric actuation replacing centralized hydraulics. |
| **Centralized hydraulics** | The conventional No.1/2/3 hydraulic systems with engine-driven and motor pumps. |
| **STD / STD-G / G-subject** | Agnostic standard section / green-delta section / green-native subject. |

---

## 1. Green-Native Doctrine for 028 / 029

- **028 — Energy-Carrier Storage and Distribution.** The conventional fuel system is liquid-hydrocarbon-specific, but its functional skeleton generalizes: **Storage → Distribution → Indicating**. Every section is substituted ⚡ to the energy-carrier form; the fuel-specific hardware (vents, flame arrestors, boost/ejector pumps, motive-flow, gravity refuel) is footprint. Green delta `028-900` adds the genuinely novel content with no fuel analogue (BMS/cell management, state-of-health, cryogenic boil-off control). This *is* the propulsion energy store — the green parallel to "fuel → 028, engine → 070-079".
- **029 — Actuation and Utility Power.** Conventional ATA-29 is entirely centralized hydraulics. Once flight-control actuation electrifies (`027-900` EHA/EMA) and gear/brakes follow, the centralized hydraulic power system is largely eliminated; actuation/utility power is drawn distributed-electric from the HVDC bus (`024-900`). The hydraulic architecture is footprint; green delta `029-900` carries the distributed-electric replacement.

---

## 2. Numbering Map

```text
ATA   CC - SS - UU      →   G-ATLAS  0CC - SS0 - UU0
e.g.  28-23-03  →  028-230-030   ·   29-11-08  →  029-110-080
```

---

## 3. Chapter 028 — Energy-Carrier Storage and Distribution

The functional skeleton (Storage / Distribution / Indicating) is retained and substituted to the energy-carrier form.

| G-ATLAS | ATA | Title | Layer |
|---|---|---|:--:|
| `028-000` ⚡ | 28-00 | **General — Energy-Carrier Storage and Distribution**[^c-2800] | STD |
| `028-100` ⚡ | 28-10 | **Energy-Carrier Storage**[^c-2810] | STD |
| `028-110` ⚡ | 28-11 | Primary storage unit (was wing tank) | STD |
| `028-120` ⚡ | 28-12 | Storage venting / conditioning (was tank vent) | STD |
| `028-130` ⚡ | 28-13 | Auxiliary storage unit (was auxiliary fuel tank) | STD |
| `028-140` ⚡ | 28-14 | Auxiliary storage venting / conditioning | STD |
| `028-200` ⚡ | 28-20 | **Energy-Carrier Distribution**[^c-2820] | STD |
| `028-210` ⚡ | 28-21 | Propulsion feed / delivery (was engine feed) | STD |
| `028-220` ⚡ | 28-22 | Auxiliary-power feed / delivery (was APU feed) | STD |
| `028-230` ⚡ | 28-23 | Pressure replenishment (was pressure refueling) | STD |
| `028-240` ⚡ | 28-24 | Gravity / manual replenishment (was gravity refueling) | STD |
| `028-250` | 28-25 | Energy-pump / converter wiring & connectors | STD |
| `028-260` ⚡ | 28-26 | Energy transfer and balancing (was auxiliary fuel transfer) | STD |
| `028-400` ⚡ | 28-40 | **Energy-Carrier Quantity and State Indication**[^c-2840] | STD |
| `028-410` ⚡ | 28-41 | Electrical quantity / state indication — SoC (was fuel-quantity-indicating) | STD |
| `028-420` | 28-42 | Direct level indication (was magnetic level) | STD |
| `028-430` ⚡ | 28-43 | Energy-carrier temperature indication | STD |
| `028-440` ⚡ | 28-44 | Low-energy-level warning (was fuel-low-level warning) | STD |
| `028-900` | — | **Energy-Carrier Management (no fuel analogue)** | STD-G |
| `028-900-010` | — | Cell / module management and balancing (BMS) | G-subject |
| `028-900-030` | — | State-of-health and degradation monitoring | G-subject |
| `028-900-050` | — | Cryogenic boil-off management and re-liquefaction interface | G-subject |
| `028-900-070` | — | Charge / discharge control and protection | G-subject |
| `028-900-090` | — | Energy-store thermal management interface | G-subject |

> 028 is a **near-total substitution**: almost nothing of the liquid-fuel system survives as primary content. The conventional architecture is preserved in full in the footprint.

---

## 4. Chapter 029 — Actuation and Utility Power

Conventional centralized hydraulics → footprint; the green binding is distributed electric.

| G-ATLAS | ATA | Title | Layer |
|---|---|---|:--:|
| `029-000` ⚡ | 29-00 | **General — Actuation and Utility Power**[^c-2900] | STD |
| `029-100` ⚡ | 29-10 | Main power generation (was main hydraulic power)[^c-2910] | STD |
| `029-110` ⚡ | 29-11 | Primary power systems (was No.1/No.2 hydraulic) | STD |
| `029-120` ⚡ | 29-12 | Tertiary power system (was No.3 hydraulic) | STD |
| `029-130` | 29-13 | Ground-service connections | STD |
| `029-300` | 29-30 | Indicating | STD |
| `029-310` | 29-31 | Pressure / state indicating | STD |
| `029-320` | 29-32 | Quantity indicating | STD |
| `029-330` | 29-33 | Temperature indicating | STD |
| `029-900` | — | **Distributed Electric Actuation and Utility Power** | STD-G |
| `029-900-010` | — | Distributed electric actuation power (EHA/EMA, hydraulic-less) | G-subject |
| `029-900-030` | — | Local EHA hydraulic loop (where retained) | G-subject |
| `029-900-050` | — | Utility-actuation electric power (gear, brakes, doors) | G-subject |
| `029-900-070` | — | Actuation power conditioning from HVDC | G-subject |

> Where a programme retains *some* hydraulics (e.g. local EHA loops or a single backup circuit), `029-110/120` bind to that residual; a fully more-electric eWTW binds them empty and routes all actuation power through `029-900`.

---

## 5. Programme Binding — eWTW / hBWB

| Node | Agnostic green binding | **eWTW** (electric) | **hBWB** (hydrogen) |
|---|---|---|---|
| `028-100` Storage | energy-carrier store | battery packs / modules | cryogenic LH₂ tanks |
| `028-120` Storage venting | gas / thermal management | cell off-gas venting, thermal | LH₂ boil-off venting |
| `028-210` Propulsion feed | energy delivery | HVDC power to propulsion | LH₂ feed to fuel cell / turbine |
| `028-230` Replenishment | replenishment interface | conductive / inductive charging | LH₂ fueling / defueling |
| `028-260` Transfer & balancing | inter-store balancing | pack balancing | tank-to-tank transfer |
| `028-410` Quantity / state | quantity & state | SoC / SoH | LH₂ mass / level |
| `028-900` Management | carrier-specific management | BMS, cell balancing, SoH | cryo management, boil-off, re-liquefaction |
| `029-900` Actuation power | distributed electric | EHA/EMA from traction HVDC | EHA/EMA from fuel-cell HVDC |

028 cross-references the propulsion band `070-079` (which consumes the stored energy), the electrical band `024` (distribution), and `400-499 EPTA`. 029 cross-references `024-900` (HVDC source) and `027-900` (the EHA/EMA actuators it powers). The energy-store thermal interface (`028-900-090`) couples to `021-900` and the fire-protection delta `026-900`.

---

## 6. Governance

Inherits **DEGF v1.0**; governed across **LC-A … LC-N**; bound by **No-AAA**, **SSOT+PUB**, and **G-ATLAS-NORM-TERM-001** (fuel → energy carrier; engine/APU → propulsion/auxiliary-power module). STD/STD-G nodes are the SSOT standard; subjects project per programme into the CSDB (PUB). Owners: **028 → Q-GREENTECH** (energy store is the green heart), **029 → Q-AIR**; green overlay **Q-GREENTECH** throughout. `028-900` energy-carrier management is flagged safety-critical (couples to `026-900`).

---

## References

1. ATA / Airlines for America — *iSpec 2200: Information Standards for Aviation Maintenance*. <https://publications.airlines.org/>
2. Embraer — *ATA breakdown, EMB 170/175/190/195 and Lineage 1000* (heritage footprint source, chapters 28–29).
3. S1000D — *International Specification for Technical Publications* (SNS; baseline Issue 4.2). <https://s1000d.org/>

---

## Conventional Heritage Footprint

[^c-2800]: **Conventional `28-00` — Fuel (general).** The conventional energy carrier is liquid hydrocarbon (Jet-A). Superseded green-native by an energy-carrier-agnostic store (electrical charge for eWTW; cryogenic hydrogen for hBWB).

[^c-2810]: **Conventional `28-10/11/12/13/14` — Storage.** Wing tanks (baffle/oval check valves, access panels, drain valves, grounding receptacle); tank vents (pressure-relief valve, float-actuated drain valve, float vent valve, vent plumbing, NACA air inlet, flame-arrestor/surge-relief valve); auxiliary fuel tanks (fwd/aft, drain valves, dry drain lines, covers); auxiliary-tank vent system (vent shutoff valves/actuators, delta-P pressure-relief backup switches, air filters, second-barrier air filters, vent control box). All liquid-fuel-specific; superseded by energy-carrier storage units and their venting/thermal conditioning.

[^c-2820]: **Conventional `28-20/21/22/23/24/26` — Distribution.** Engine feed (check valve, AC auxiliary boost-pump cartridge/canister, AC fuel-pump relays/pressure switch, engine & cross-feed shutoff-valve actuators 28 VDC, ejector pump, motive-flow supply/relief/check, fuel-feed line, scavenger ejector, fuel control panel); APU feed (DC start pump, DC pump pressure switch/relay, APU feed SOV with actuator, fuel-feed line/shroud); pressure refueling (refueling/defueling control panel, refueling/defueling SOVs and actuators, control solenoid, fuel-quantity repeater, adapter assembly/cap, float pilot valve, refueling pressure switch, restrictor, diffuser, refuel shutoff valves, indication lights); gravity refueling (adapter, fill-cap seal/cap); auxiliary fuel transfer (transfer shutoff valves/actuators, AC transfer pumps, transfer-line check valves, isolation shutoff valves, transfer control boxes). Superseded by energy delivery, replenishment (charging/H₂ fueling), and inter-store balancing.

[^c-2840]: **Conventional `28-40/41/42/43/44` — Indicating.** Electrical fuel-quantity indicating (probes/compensator, fuel conditioning unit, tank-unit/quantity-indication harnesses), magnetic level indicating, fuel temperature indication, fuel-low-level warning. Superseded by energy quantity/state (SoC/SoH), level, temperature, and low-energy warning.

[^c-2900]: **Conventional `29-00` — Hydraulic Power (general).** Hydraulic fluid, electrical hardware. The conventional realization of actuation/utility power is centralized hydraulics; superseded green-native by distributed electric power.

[^c-2910]: **Conventional `29-10/11/12/13` + `29-30s` — Centralized hydraulics.** Main hydraulic power (control panel, system tubing/support); No.1/No.2 systems (engine-driven pump, AC-motor-driven pumps, power-transfer unit, filter manifolds/elements, reservoirs, accumulators, heat exchangers and bypass/check valves, priority valves, dump/thermal-relief valves, pressure/suction attenuators, quick-disconnects, pump contactors and shutoff relays); No.3 system (AC-motor pump, filters, reservoir, accumulator, priority/flow-limiter/unloader valves, attenuators, contactors); ground-service connections (pressure/return/fill quick-disconnects); indicating (pressure transducers/switches, fluid-quantity, temperature). Superseded by distributed electric actuation/utility power (EHA/EMA from HVDC); residual local hydraulics, if any, bind to `029-900-030`.
