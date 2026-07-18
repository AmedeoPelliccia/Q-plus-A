# S-ATLAS Thread Index — Hydrogen

**Cross-cutting technology thread** · Owner: architecture authority (AM.PEL) · Date: 2026-07-18
**Status:** v0.2 — RATIFIED allocations (three-layer leak model, venting and servicing splits).
**Supersedes:** ATLAS-THREAD-HYDROGEN v0.1.

---

## 1. Principle (general architecture rule)

The taxonomy assigns homes to **functions, never to molecules**. This is a general rule of the architecture, first instantiated by this thread: hydrogen has no chapter; each hydrogen function lives where that function class lives. Conversion class decides the range, not the molecule.

## 2. The hydrogen thread

| Function | Home | Notes |
|---|---|---|
| Technology domain: cells, stacks, H₂ propulsion technology | `400–499 EPTA` (`460–469`; storage technology `420–429`) | Encyclopedia level — S-ATLAS documents *aircraft-side integration*, EPTA the *technology* |
| Aircraft storage and distribution | `028`-class (energy-carrier systems) | Cryogenic tanks, feed and conditioning, quantity gauging; owns the hosted supervision functions |
| Loss-of-containment as a **system condition** | `028` | Concentration measurement, leak localization, system isolation, source shutdown |
| Aircraft-level **hazardous-condition** protection | `026` | Hazard determination, fire/overheat protection, crew warning, coordinated protection logic |
| **Protective-atmosphere response** | `047` | Inerting and dilution, executed when commanded by the applicable protection logic |
| Combustion conversion (propulsive) | `060` Sustainable-Energy-Carrier-Combustion-Propulsion | Hydrogen-combustion turbines, fuel-flexible combustors, contrail-aware combustion |
| Electrochemical conversion (propulsive) | `070` Electric-and-Hybrid-Electric-Propulsion | Fuel-cell-electric powertrains — electrochemical source, electric drive |
| Electrochemical conversion (auxiliary) | `049` Auxiliary Power | Fuel-cell auxiliary power module; water exhaust routed per drainage provisions |
| Venting and boil-off — **function** | `028` | Vent function, flow control, pressure relief, piping up to the aircraft interface |
| Venting and boil-off — **terminal path** | `030-720` | Drain/vent mast, discharge geometry, ice-protection provisions |
| Cryogenic zone insulation interfaces | `050-620` | Fitted-volumes doctrine: the compartment interface, not the tank |
| Structural bays and tank zones | `053` | Structure owns the bay; the system owns the tank |
| Cryogenic materials and inspection practices | `051-330` · `051-140` | Materials behavior at cryogenic temperature; NDI including cryogenic cases |
| Ground refuelling — **aircraft side** | `028` | Onboard receptacle, valves, transfer path, aircraft-side safety functions |
| Ground refuelling — **operation** | `010–019` | Servicing procedures, ground-equipment coordination, safety zones, operational constraints |
| Hosted supervision functions (hosting only) | `042-400` | Allocation, budgets and evidence for `028`-owned functions hosted on the platform |

## 3. Boundary rule — loss of containment (ratified three-layer model)

> **028 detects and manages loss of containment as a system condition. 026 determines and manages the resulting aircraft-level hazard. 047 provides protective-atmosphere response when commanded by the applicable protection logic.**

One integrated hazard-and-annunciation doctrine; three owners by layer. The rule generalizes to any fluid or energy-carrier system: the system owns its own condition sensing; protection owns the aircraft-level hazard; atmosphere management owns the atmospheric response. It also prevents `026` from becoming the owner of every fluid-system leak sensor.

## 4. The split doctrine

Where a function crosses a system and an operational or physical interface, **the system owns the function and hardware; the interfacing range owns the operation or terminal provision** — refuelling (028 / 010–019), venting (028 / 030-720). Declared here once, inherited everywhere.

## 5. The thread-index pattern

Cross-cutting technologies (hydrogen, electrification, cryogenics, quantum enablement, …) get **derived thread indexes**: one table, function-by-function, homes and boundary notes, maintained beside the band register. Thread indexes never create homes — they map existing ones; a function missing a home is a register gap to fix in the register, not in the thread. Programme impact studies consume thread indexes as their starting checklist.
