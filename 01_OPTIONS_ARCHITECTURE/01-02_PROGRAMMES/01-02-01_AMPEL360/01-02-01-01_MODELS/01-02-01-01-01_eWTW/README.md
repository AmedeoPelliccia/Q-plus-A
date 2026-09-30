---
status: draft
standard_scope: governance
---

# AMPEL360 eWTW — Electric Wide Tube and Wing

The eWTW is the AMPEL360 model of the advanced tube-and-wing class (S-ATLAS `092`). Its breakdown structures live under [`SBS`](01-02-01-01-01-01_SBS_System-Breakdown-Structure/) — a federation of views over one identity system, governed by `AMPEL360-PBS-PN-CM-001` and `AMPEL360-SBS-ID-CM-002`. The fleet-level comparison between a conventional airliner and the AMPEL360 hydrogen-electric reference architecture is in the [root README](../../../../../README.md); this page states what of that reference the eWTW has **decided**, what it must **integrate**, and what it leaves **open**.

## Declared, integrated, open

**Declared so far:** the fuselage PBS `053` (sections `053-000 … 053-900`, identifiers PLANNED); the energy-carrier provisions `053-900` — bay structure (`053-900-010`) and crash protection and containment interface (`053-900-020`); the pack-bay and belly-fairing architecture; an **electric, bleedless ECS based on E-packs**.

**The one system-level change already identifiable** is the transfer of the ECS power source from the engine's pneumatic domain to the electrical domain. It couples E-pack sizing to generation, distribution, protection and heat rejection — before any propulsion decision is taken.

**Open decisions**, which together gate the preliminary-design baseline: the energy carrier · the propulsion chain · the electrical sources · the role of energy storage · the architecture of essential power. The structure of the energy-carrier bay does not determine its content: cryogenic tanks, conventional tanks and batteries would each require a different realisation.

## System decomposition

Status: **D** declared by the model · **I** integration need that follows from what is declared · **O** open decision.

| # | System | S-ATLAS | To be represented for eWTW | St. |
|---|---|---|---|:-:|
| 1 | Airframe | `051–059` | Fuselage, wings, empennage, propulsor attachments, doors, floors, compartments, fairings, equipment supports. Energy-carrier provisions, E-pack installation, penetrations, access and mass distribution | D·I |
| 2 | Energy-carrier storage and delivery | `028` · `064` | Carrier containment, supports, charging or refuelling interfaces, gauging, isolation, links to consumers | O |
| 3 | Propulsion | `061–069` · `071–077` | Propulsive units, installation, power transmission, control and monitoring. If electric: inverters, motors, optional gearboxes, propellers or fans; if hybrid with a thermal machine, its sub-systems too | O |
| 4 | Electrical generation and storage | `024` · `068` · `074` · `075` | Main sources, conversion, storage, start, energy management. The E-pack creates a significant demand; **it does not determine the kind of generation or the role of batteries** | I·O |
| 5 | Electrical distribution | `024` · `076` · `079` | Buses, switchgear, converters, protection, harnesses, segregation, essential supplies. E-pack supplies and protection must be allocated now; a propulsion HV network only if the propulsion chain requires it | I·O |
| 6 | Thermal management | `021` · `078` | Equipment cooling, heat exchangers, ventilation, liquid loops, air inlets and outlets — integrated with the E-pack installation; stack and propulsion-battery loops conditional on their presence | I·O |
| 7 | Flight controls | `027` · `022` | Computers, sensors, primary and secondary surfaces, actuators. No model-specific change declared; differential thrust only if distributed propulsion is chosen | O |
| 8 | Actuation and utility power | `029` | Pumps, accumulators, actuators, hydraulic lines, possible EHA and EMA. The electric ECS does not decide the fate of hydraulics — technology allocated function by function | O |
| 9 | ECS, pressurisation, pneumatics | `021` · `036` | E-packs, electric compressors, air treatment, distribution, recirculation, thermal regulation, cabin pressure. **Bleedless ECS declared**; any other pneumatic consumer is treated separately | D |
| 10 | Ice and rain protection | `030` | Surfaces and inlets, probes and windshield heating, rain removal. Technology open: **a bleedless ECS is not an aircraft without bleed** | O |
| 11 | Landing gear, braking, steering | `032` | Legs, retraction, wheels, brakes, anti-skid, steering, doors, structural interfaces. The NLG-bay structure (`053-100-020`) defines an integration scope, not the gear design | I |
| 12 | Avionics and flight management | `022` · `023` · `031` · `034` · `042` · `046` | Navigation, communication, surveillance, guidance, instruments, alerting, systems management; E-pack control and indication now, energy management once the sources are chosen | I·O |
| 13 | Cabin, cargo, equipment | `025` · `033` · `035` · `044` · `050` | Furnishings, seats, floors, lighting, oxygen, water and waste, holds, evacuation; interfaces with air distribution — floor beams (`053-700-020`) and seat tracks (`053-700-060`) are realized | I |
| 14 | Protection and emergency | `026` · `047` · `079` | Fire and smoke detection, source isolation, electrical protection, continuity of essential functions. **H₂ leak detection if hydrogen is present; thermal-propagation management if relevant batteries are present** | O |
| 15 | Auxiliary power and ground services | `049` · `012` | External power, auxiliary sources, start, emergency supplies, service interfaces — sized against E-pack demand and the energy configuration. The name *Auxiliary Power Module* does not determine its technology | I·O |
| 16 | Diagnostics and maintenance support | `045` | Monitoring, built-in test, fault recording, access, test points, support equipment — extending to the E-packs and to whatever equipment is selected; TPuBS follows its configuration and effectivity | I |

## SBS crosswalk — proposed allocations

The PBS nodes below exist; the functions and interfaces are **proposed allocations** to be formalised in the FBS and IBS under CM-002.

| Domain | FBS function to represent | PBS node | IBS interfaces to register |
|---|---|---|---|
| `053` forward structure | Support and restrain the radome on the airframe | `eWTW-PBS-053-100-040` (assembly `EWTW-531004-000`) | Mating geometry, fasteners, loads, tolerances, access |
| `053` NLG bay | Bound the bay and carry the loads assigned to its walls | `eWTW-PBS-053-100-020` | Surrounding structure, gear envelope, doors, penetrations |
| `053` floor | Support the passenger floor and carry its loads | `eWTW-PBS-053-700-020` | Beams, panels, side structure, installations |
| `053` seat tracks | Provide seat attachment and load transfer | `eWTW-PBS-053-700-060` | Seats, fasteners, floor, supporting structure |
| `053` pressure bulkhead | Close the pressurised volume and carry pressure loads | `eWTW-PBS-053-800-010` | Skin, frames, joints, seals, penetrations |
| `053-900` energy-carrier bay | Integrate the energy module and carry its loads in the assigned scenarios | `eWTW-PBS-053-900-010` · crash and containment `eWTW-PBS-053-900-020` | Supports, envelopes, access, load paths, system connections |
| `021` ECS | Condition and distribute air at the required state | Chapter `eWTW-PBS-021-000` exists as a stub — **the E-pack station and its part numbers are still to be realized under it** | Electrical supply, air, control, installation, exhaust, maintenance |

One distinction is deliberate: the TPuBS node `021-200-010` (*Distribution Ducting Architecture*) is a publication node. It describes the product; it can never identify an E-pack or give it a part number (CM-001 §9). The link runs from the product, with its configuration and effectivity, to the publication — never the other way round.
