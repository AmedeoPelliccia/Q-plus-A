---
node: 010-019
title: Ground Handling and Servicing — S-ATLAS Green-Native Breakdown
band: 000-099_S-ATLAS
master_range: 010-019
view: green-native (canonical)
heritage_crosswalk: "010-019_ATA-Aligned-Breakdown.md (conventional-primary, v2.0)"
principle: "Divergence nodes carry the green energy-architecture binding; the conventional ATA content is demoted to the heritage footprint (footnotes)."
numbering_map: "ATA CC-SS-UU  →  S-ATLAS 0CC-SS0-UU0"
owner: Q-GROUND
green_overlay: Q-GREENTECH
governance: [DEGF-v1.0, LC-A..LC-N, No-AAA, SSOT+PUB]
status: baseline
version: "3.0"
---

# 010-019 — Ground Handling and Servicing · S-ATLAS Green-Native Breakdown

The canonical S-ATLAS view. Where a conventional aircraft would service kerosene, engine oil, and accessory lubricants, this schema services the **energy carrier**, **propulsion-module lubricants/coolant**, and **thermal-management fluids** instead. The conventional binding is preserved as a **heritage footprint** in the footnotes, cross-walked to the Embraer ATA reference — never lost, but no longer primary.

---

## Index

- <a>Glossary</a>
- <a>1. Green-Native Doctrine</a>
- <a>2. Numbering Map</a>
- <a>3. Chapter 010 — Parking, Mooring, Storage &amp; Return to Service</a>
- <a>4. Chapter 011 — Placards and Markings</a>
- <a>5. Chapter 012 — Servicing</a>
- <a>6. Programme Binding — eWTW / hBWB</a>
- <a>7. Governance</a>
- <a>References</a>
- <a>Conventional Heritage Footprint</a>

---

## Glossary

| Term | Meaning |
|---|---|
| **Green-native** | The schema's primary binding is the sustainable energy architecture; conventional content is heritage, not default. |
| **Energy carrier** | Architecture-neutral term for the stored energy form (electrical charge, cryogenic hydrogen, …). |
| **Divergence node** | A section whose conventional content (fuel, oil, engine) is **substituted** by a green binding. Marked ⚡. |
| **Heritage footprint** | The conventional ATA binding, retained in footnotes and cited to the reference — the schema's provenance trail. |
| **STD / STD-G** | Agnostic standard section / green-delta section. |
| **G-subject** | Green-native, energy-carrier-neutral subject at a substituted node. |

---

## 1. Green-Native Doctrine

Three rules govern the substitution:

1. **Only divergence nodes are substituted.** Mooring, hydraulics, water/waste, gaseous, cleaning, disinfect, airframe, cold-weather, and placard *locations* are energy-neutral and carry forward unchanged.
2. **Green bindings stay agnostic.** The primary rows name functions in energy-carrier-neutral terms ("energy-carrier replenishment", "thermal-management fluid"); the eWTW/hBWB specifics live in the programme-binding table (§6).
3. **The conventional binding is never deleted — it is footprinted.** Each substituted node carries a footnote to its conventional ATA equivalent, cited to the Embraer 170/175/190/195 + Lineage 1000 breakdown.[^ref]

Substituted (⚡): `011-250-010`, `011-260-010`, `012-110`, `012-130`. Promoted to first-class green deltas: `010-900`, `011-900`, `012-900`.

---

## 2. Numbering Map

```text
ATA   CC - SS - UU      →   S-ATLAS  0CC - SS0 - UU0
chapter left-pad · section ×10 · unit/subject ×10 · 900-lane = green
```

---

## 3. Chapter 010 — Parking, Mooring, Storage &amp; Return to Service

Energy-neutral throughout; the only green addition is the storage energy-state delta.

| S-ATLAS | ATA | Title | Layer |
|---|---|---|:--:|
| `010-000` | 10-00 | General | STD |
| `010-100` | 10-10 | Parking and Storage | STD |
| `010-100-010` | 10-10-01 | Normal parking | STD |
| `010-100-030` | 10-10-03 | Prolonged parking | STD |
| `010-100-050` | 10-10-05 | Parking in adverse weather | STD |
| `010-200` | 10-20 | Mooring | STD |
| `010-300` | 10-30 | Return to Service | STD |
| `010-900` | — | **Energy-State Preservation During Storage** | STD-G |
| `010-900-010` | — | Energy-carrier state management during storage | G-subject |
| `010-900-030` | — | Energy-carrier loss / boil-off control during storage | G-subject |
| `010-900-050` | — | Energy-system re-activation for return to service | G-subject |

---

## 4. Chapter 011 — Placards and Markings

Placard *locations* are unchanged; the energy-system placards (⚡) are substituted, and the energy-carrier hazard delta is first-class.

| S-ATLAS | ATA | Title | Layer |
|---|---|---|:--:|
| `011-000` | 11-00 | General | STD |
| `011-100` | 11-10 | Exterior Colour Schemes and Markings | STD |
| `011-200` | 11-20 | Exterior Placards and Markings | STD |
| `011-210` | 11-21 | Fuselage placards | STD |
| `011-230` | 11-23 | Landing-gear placards | STD |
| `011-250` | 11-25 | Wing placards | STD |
| `011-250-010` ⚡ | 11-25-01 | **Wing energy-system placards** (HV / cryogenic)[^c-1125] | G-subject |
| `011-250-030` | 11-25-03 | Wing-to-fuselage fairing | STD |
| `011-250-050` | 11-25-05 | Wing jack point | STD |
| `011-250-070` | 11-25-07 | Wing safety points | STD |
| `011-260` | 11-26 | Propulsion-module and pylon placards | STD |
| `011-260-010` ⚡ | 11-26-01 | **Propulsion-module energy / lubricant servicing placards**[^c-1126] | G-subject |
| `011-260-030` | 11-26-03 | Hoisting point | STD |
| `011-260-050` | 11-26-05 | Module cowl / housing | STD |
| `011-260-070` | 11-26-07 | Thrust / reverse device | STD |
| `011-260-090` | 11-26-09 | Inlet / intake | STD |
| `011-260-110` | 11-26-11 | Pylon | STD |
| `011-300` | 11-30 | Interior Placards | STD |
| `011-310` | 11-31 | Cockpit placards and markings | STD |
| `011-320` | 11-32 | Passenger-cabin placards and markings | STD |
| `011-330` | 11-33 | Cargo-compartment placards and markings | STD |
| `011-900` | — | **Energy-Carrier Hazard Placards** | STD-G |
| `011-900-010` | — | High-voltage hazard placards | G-subject |
| `011-900-030` | — | Cryogenic / low-temperature hazard placards | G-subject |
| `011-900-050` | — | Flammable / asphyxiant-gas hazard placards | G-subject |
| `011-900-070` | — | Emergency energy-isolation / cut-off markings | G-subject |

---

## 5. Chapter 012 — Servicing

The heart of the substitution. `012-110` (energy-carrier servicing) replaces fuel servicing; `012-130` (lubricant &amp; thermal-fluid) replaces oil servicing; `012-900` carries novel ground-energy operations with no ATA equivalent.

| S-ATLAS | ATA | Title | Layer |
|---|---|---|:--:|
| `012-000` | 12-00 | General | STD |
| `012-100` | 12-10 | Replenishing | STD |
| `012-110` ⚡ | 12-11 | **Energy-Carrier Servicing**[^c-1211] | STD |
| `012-110-010` | 12-11-01 | Energy-carrier replenishment (transfer-in) | G-subject |
| `012-110-030` | 12-11-03 | Energy-carrier recovery / removal (transfer-out) | G-subject |
| `012-110-050` | 12-11-05 | Energy-carrier draining and venting | G-subject |
| `012-110-070` | 12-11-07 | Energy-carrier quantity and state indication | G-subject |
| `012-120` | 12-12 | Hydraulic servicing | STD |
| `012-130` ⚡ | 12-13 | **Lubricant and Thermal-Fluid Servicing**[^c-1213] | STD |
| `012-130-010` | 12-13-01 | Propulsion-module lubricant | G-subject |
| `012-130-050` | 12-13-05 | Auxiliary-power-module lubricant | G-subject |
| `012-130-090` | 12-13-09 | Power-electronics / generator coolant | G-subject |
| `012-130-110` | 12-13-11 | Thermal-management fluid | G-subject |
| `012-140` | 12-14 | Water / waste servicing | STD |
| `012-150` | 12-15 | Gaseous servicing | STD |
| `012-200` | 12-20 | Scheduled Servicing | STD |
| `012-210` | 12-21 | Lubricating servicing | STD |
| `012-220` | 12-22 | Cleaning servicing | STD |
| `012-240` | 12-24 | Disinfect servicing | STD |
| `012-250` | 12-25 | Airframe servicing | STD |
| `012-300` | 12-30 | Unscheduled Servicing | STD |
| `012-310` | 12-31 | Cold-weather servicing | STD |
| `012-900` | — | **Energy Conditioning and Smart-Replenishment Operations** | STD-G |
| `012-900-010` | — | Energy-carrier thermal pre-conditioning | G-subject |
| `012-900-030` | — | Smart / scheduled replenishment management | G-subject |
| `012-900-050` | — | Ground-grid interaction (import / export) | G-subject |
| `012-900-070` | — | Energy-system state-of-health check on ground | G-subject |

---

## 6. Programme Binding — eWTW / hBWB

The agnostic green rows above bind to concrete carriers per programme:

| Substituted node | Agnostic green binding | **eWTW** (electric) | **hBWB** (hydrogen) |
|---|---|---|---|
| `012-110` Energy-carrier servicing | replenish / recover / vent / indicate | charge / discharge / balance / SoC | LH₂ fuel / defuel / boil-off / quantity |
| `012-130` Lubricant &amp; thermal-fluid | module lubricant + coolant | e-motor &amp; gearbox lube, battery coolant | fuel-cell / turbine lube, cryo-pump lube |
| `011-250-010` Wing energy placards | HV / cryogenic | high-voltage battery-bay placards | cryogenic / H₂ placards |
| `011-260-010` Propulsion-module placards | energy / lubricant servicing | motor &amp; inverter servicing | fuel-cell / turbine servicing |
| `010-900` Storage energy-state | preserve / control / re-activate | battery SoC, preservation charge | LH₂ boil-off, tank inerting |
| `011-900` Energy hazard placards | HV / cryo / gas / isolation | high-voltage / thermal | cryogenic / flammable-gas |
| `012-900` Conditioning &amp; smart-replenishment | precondition / schedule / grid / SoH | thermal preconditioning, smart-charge, V2G | cryo conditioning, H₂ logistics |

The infrastructure side of replenishment is `000-009 → 003-900`; the servicing side is here. The two cross-reference.

---

## 7. Governance

Inherits **DEGF v1.0**; governed across **LC-A … LC-N**; bound by **No-AAA** and **SSOT+PUB**. Green-native STD/STD-G nodes are the SSOT standard; programme carriers (§6) project into the programme CSDB (PUB). Owner **Q-GROUND**; green overlay **Q-GREENTECH**.

---

## References

1. ATA / Airlines for America — *iSpec 2200: Information Standards for Aviation Maintenance*. <a href="https://publications.airlines.org/">https://publications.airlines.org/</a>
2. Embraer — *ATA breakdown, EMB 170/175/190/195 and Lineage 1000* (heritage footprint source).
3. S1000D — *International Specification for Technical Publications* (SNS; baseline Issue 4.2). <a href="https://s1000d.org/">https://s1000d.org/</a>

---

## Conventional Heritage Footprint

The conventional kerosene binding the green rows replace — retained for provenance and cross-walk, cited to the reference.[^ref]

[^ref]: Embraer, *ATA Breakdown — EMB 170/175/190/195 and Lineage 1000*, chapters 10–12 (uploaded reference). Conventional bindings below are transcribed from it for heritage cross-walk only; they are **not** part of the green-native S-ATLAS standard.

[^c-1125]: **Conventional `11-25-01` — Wing fuel system placards.** Markings for the wing fuel tank system. Superseded green-native by wing energy-system placards (high-voltage battery-bay for eWTW, cryogenic/H₂ for hBWB).

[^c-1126]: **Conventional `11-26-01` — Engine oil servicing placards** (within Powerplant and Pylon: engine oil servicing, hoisting point, fan cowl, thrust reverser, engine inlet, pylon). Superseded green-native by propulsion-module energy/lubricant servicing placards.

[^c-1211]: **Conventional `12-11` — Fuel Servicing.** Subjects: `01` fuel tank fueling/defueling · `03` fuel tank gravity refueling · `05` fuel tank draining · `07` fuel magnetic level. Superseded green-native by Energy-Carrier Servicing (replenishment / recovery / draining-venting / quantity-and-state).

[^c-1213]: **Conventional `12-13` — Oil Servicing.** Subjects: `01` engine oil · `05` APU oil · `09` integrated drive generator oil · `11` air turbine starter oil. Superseded green-native by Lubricant and Thermal-Fluid Servicing (propulsion-module lubricant / auxiliary-power lubricant / power-electronics coolant / thermal-management fluid).
