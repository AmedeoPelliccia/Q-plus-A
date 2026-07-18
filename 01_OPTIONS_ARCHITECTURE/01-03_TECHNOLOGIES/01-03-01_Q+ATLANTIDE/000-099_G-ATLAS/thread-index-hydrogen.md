# ATLAS Thread Index — Hydrogen

**Cross-cutting technology thread** · Owner: architecture authority (AM.PEL) · Date: 2026-07-18
**Status:** RATIFIED — first instance of the thread-index pattern (see §4).

---

## 1. Principle

The taxonomy assigns homes to **functions, never to molecules**. Hydrogen therefore has no chapter: each hydrogen function lives where that function class lives, and the thread index is the derived, one-glance map across them. Conversion class decides the range, not the molecule.

## 2. The hydrogen thread

| Function | Home | Notes |
|---|---|---|
| Technology domain: cells, stacks, H₂ propulsion technology | `400–499 EPTA` (`460–469`; storage technology `420–429`) | Encyclopedia level — the aircraft band documents *integration*, EPTA documents the *technology* |
| Aircraft storage and distribution | `028`-class (energy-carrier systems) | Cryogenic tanks, feed and conditioning, quantity gauging; owns the hosted supervision functions |
| Combustion conversion (propulsive) | `060` Sustainable-Fuel-Combustion-Propulsion | Hydrogen-burning turbomachinery, fuel-flexible combustors, contrail-aware combustion |
| Electrochemical conversion (propulsive) | `070` Electric-and-Hybrid-Electric-Propulsion | Fuel-cell-electric powertrains — electrochemical source, electric drive |
| Electrochemical conversion (auxiliary) | `049` Auxiliary Power | Fuel-cell auxiliary power module; water exhaust routed per `030-720` / `053` drainage provisions |
| Fire and overheat protection | `026` | Zone classification, detection, suppression around hydrogen installations |
| Leak detection and protective atmospheres | `026` ↔ `047` — **open ruling, recommendation in §3** | Detection versus atmosphere response |
| Venting and boil-off paths | `030-720` | Drain and vent masts, including their ice protection |
| Cryogenic zone insulation interfaces | `050-620` | Fitted-volumes doctrine: the compartment interface, not the tank |
| Structural bays and tank zones | `053` | Structure owns the bay; the system owns the tank |
| Cryogenic materials and inspection practices | `051-330` · `051-140` | Materials behavior at cryogenic temperature; NDI including cryogenic cases |
| Ground servicing interfaces | `010–019` | Refueling interfaces, servicing safety zones, ground-side coordination |
| Hosted supervision functions (hosting only) | `042-400` | Allocation, budgets and evidence for `028`-owned functions hosted on the platform |

## 3. Open ruling surfaced — leak detection (`026` vs `047`)

**Recommended default:** leak **detection** belongs to `026` — it is a detection-and-protection function, sibling of fire and overheat detection, sharing one sensing ecosystem, one containment logic and one crew-alerting philosophy. `047` owns the **atmosphere response**: inerting and protective-atmosphere management, *consuming* `026` detections as triggers. One detector family, one annunciation doctrine, two consumers. Ratification closes a ruling pending since the `047` chapter realization.

## 4. The thread-index pattern

Cross-cutting technologies (hydrogen, electrification, quantum enablement, …) get **derived thread indexes**: one table, function-by-function, homes and boundary notes, maintained beside the band register. Thread indexes never create homes — they map existing ones; a function missing a home is a register gap to fix in the register, not in the thread. Programme impact studies consume thread indexes as their starting checklist.
