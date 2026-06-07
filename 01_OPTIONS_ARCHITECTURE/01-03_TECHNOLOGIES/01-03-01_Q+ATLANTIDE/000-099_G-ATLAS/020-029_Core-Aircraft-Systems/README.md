---
node: 020-029
title: Core Aircraft Systems — G-ATLAS Green-Native Breakdown (020, 021)
band: 000-099_G-ATLAS
master_range: 020-029
nodes_in_this_file: ["020 Standard Maintenance Practices", "021 Air Conditioning / Environmental Control"]
view: green-native (canonical)
heritage_source: "ATA breakdown, Embraer 170/175/190/195 and Lineage 1000 (chapters 20, 21)"
principle: "Energy-neutral sections carry forward; divergence nodes carry the green binding; conventional content is demoted to the heritage footprint (footnotes)."
numbering_map: "ATA CC-SS-UU  →  G-ATLAS 0CC-SS0-UU0"
owner: Q-AIR
green_overlay: Q-GREENTECH
governance: [DEGF-v1.0, LC-A..LC-N, No-AAA, SSOT+PUB]
status: baseline
version: "1.0"
---

# 020-029 — Core Aircraft Systems · Green-Native Breakdown (020 · 021)

The first two nodes of the Core Aircraft Systems range, normalized from the Embraer ATA reference into the green-native G-ATLAS form. **Chapter 020** (Standard Maintenance Practices) is energy-neutral and carries forward whole, with an additive green delta for high-energy practices. **Chapter 021** (Air Conditioning / ECS) substitutes the conventional bleed-air air-cycle cooling pack with an electrically-driven, energy-integrated cooling architecture; the conventional pack is retained as heritage footprint.

---

## Index

- <a>Glossary</a>
- <a>1. Green-Native Doctrine for 020 / 021</a>
- <a>2. Numbering Map</a>
- <a>3. Chapter 020 — Standard Maintenance Practices</a>
- <a>4. Chapter 021 — Air Conditioning / Environmental Control</a>
- <a>5. Programme Binding — eWTW / hBWB</a>
- <a>6. Governance</a>
- <a>References</a>
- <a>Conventional Heritage Footprint</a>

---

## Glossary

| Term | Meaning |
|---|---|
| **Green-native** | Primary binding is the sustainable energy architecture; conventional content is heritage. |
| **Energy-neutral** | A section unaffected by the energy architecture (carries forward unchanged). |
| **Divergence node ⚡** | A section whose conventional content (bleed air, air-cycle) is substituted by a green binding. |
| **EWIS** | Electrical Wiring Interconnection System — dominant content of ch. 20; extends to high-voltage under green. |
| **ECS** | Environmental Control System (ATA 21). |
| **ACM** | Air-Cycle Machine — the bleed-air cooling technology a bleedless aircraft replaces. |
| **Bleedless** | Architecture with no engine bleed air; ECS driven electrically (e-compressor) or by energy-system integration. |
| **STD / STD-G** | Agnostic standard section / green-delta section. **G-subject** = green-native subject. |
| **Heritage footprint** | Conventional binding retained in footnotes, cited to the reference. |

---

## 1. Green-Native Doctrine for 020 / 021

- **020 Standard Maintenance Practices — carries forward whole.** Torque, safetying, tubing, bearings, EWIS wiring, connectors, soldering, ESD, bonding, cleaning, and inspections are universal and architecture-neutral. EWIS in fact *expands* under electrification. No substitution; one additive green delta `020-900` for high-voltage / energy-storage / cryogenic-line practices.
- **021 Air Conditioning / ECS — one major substitution.** Distribution, ventilation, pressurization, relief, and temperature control are energy-neutral and carry forward. The **cooling pack** (`021-510`, conventional ACM/bleed) is substituted ⚡ by an electrically-driven / vapour-cycle / cryo-integrated cooling unit, and a green delta `021-900` adds energy-system thermal integration with no ATA equivalent. Heating (`021-400/410`) is already electric and stays.

---

## 2. Numbering Map

```text
ATA   CC - SS - UU      →   G-ATLAS  0CC - SS0 - UU0
chapter left-pad · section ×10 · unit/subject ×10 · 900-lane = green
e.g.  21-51-05  →  021-510-050
```

---

## 3. Chapter 020 — Standard Maintenance Practices

Energy-neutral throughout. Owner Q-AIR; EWIS overlay applies.

| G-ATLAS | ATA | Title | Layer |
|---|---|---|:--:|
| `020-000` | 20-00 | General — Standard Practices, Airframe | STD |
| `020-010` | 20-01 | Wire and cable identification — description | STD |
| `020-100` | 20-10 | General maintenance practices (torque, safetying, tubing, screws, bearings, clamps, grease) | STD |
| `020-130` | 20-13 | Electrical-components maintenance practices (degaussing, mounting trays, antenna covers, bonding) | STD |
| `020-200` | 20-20 | Flight-controls maintenance practices | STD |
| `020-210` | 20-21 | Tooling — crimpers, contact insertion/removal | STD |
| `020-300` | 20-30 | Consumables | STD |
| `020-350` | 20-35 | Electrical components — maintenance practices (junction modules) | STD |
| `020-380` | 20-38 | Component data — coaxial / triaxial / quadrax connectors | STD |
| `020-390` | 20-39 | Modular plug connector — maintenance practices | STD |
| `020-400` | 20-40 | Electrostatic discharge (ESD) and static grounding | STD |
| `020-410` | 20-41 | Assembly practices — wire termination, splices, stripping, spare wire | STD |
| `020-430` | 20-43 | Soldering procedures | STD |
| `020-450` | 20-45 | Harness ties | STD |
| `020-500` | 20-50 | Installation practices — description | STD |
| `020-510` | 20-51 | Clamping | STD |
| `020-520` | 20-52 | Electrical connector mating | STD |
| `020-600` | 20-60 | Maintenance practices — description | STD |
| `020-610` | 20-61 | Harness and electrical-connector cleaning | STD |
| `020-620` | 20-62 | EWIS components inspections / checks | STD |
| `020-670` | 20-67 | Preventive maintenance | STD |
| `020-900` | — | **High-Energy / Green Standard Practices** | STD-G |
| `020-900-010` | — | High-voltage EWIS standard practices | G-subject |
| `020-900-030` | — | Energy-storage component safe-handling practices | G-subject |
| `020-900-050` | — | Cryogenic-line and composite-tank standard practices | G-subject |
| `020-900-070` | — | High-current bonding and grounding practices | G-subject |

> Full conventional subject enumeration (bolt torque data, safetying, tubing, V-band clamps, coaxial/triaxial/quadrax contacts, splices, etc.) is programme-bound and transcribed in the reference;[^ref] the section skeleton above is the agnostic standard.

---

## 4. Chapter 021 — Air Conditioning / Environmental Control

Distribution / ventilation / pressurization / temperature control carry forward; cooling ⚡ is substituted; thermal integration is a first-class green delta.

| G-ATLAS | ATA | Title | Layer |
|---|---|---|:--:|
| `021-000` | 21-00 | General — Air Conditioning (incl. AMS controller modules) | STD |
| `021-200` | 21-20 | Distribution — main ducts, check valves, air-mix H-duct | STD |
| `021-210` | 21-21 | Cockpit distribution — ducts, outlets, foot-outlet shutoff valves | STD |
| `021-220` | 21-22 | Passenger-cabin distribution — ducts, outlets, plenums | STD |
| `021-230` | 21-23 | Gasper — shutoff/check valves, ducts, outlet | STD |
| `021-240` | 21-24 | Recirculation — fans, filters, ducts, relays | STD |
| `021-250` | 21-25 | Ram-air ventilation — emergency ram-air valve, NACA inlets, ducts | STD |
| `021-260` | 21-26 | Avionics-compartment ventilation — fwd/mid/aft fans, sensors, ducts, mission/entertainment rack | STD |
| `021-270` | 21-27 | Cargo-compartment ventilation — fans, valves, ducts, aft baggage | STD |
| `021-280` | 21-28 | Miscellaneous-equipment & chiller ventilation | STD |
| `021-290` | 21-29 | Low-pressure ground supply — nipple, check-valve, duct | STD |
| `021-300` | 21-30 | Pressurization control — control panel | STD |
| `021-310` | 21-31 | Pressurization control / indication — CPCS controller, outflow valve, EICAS indications | STD |
| `021-320` | 21-32 | Cabin pressure relief — positive/negative relief valves, static ports | STD |
| `021-330` | 21-33 | Cargo-compartment pressure equalization — fwd/aft valves | STD |
| `021-400` | 21-40 | **Heating** (electric — already green) | STD |
| `021-410` | 21-41 | Floor-panel heating — control module, heated panels | STD |
| `021-500` ⚡ | 21-50 | **Environmental Cooling (Electric / Integrated)**[^c-2150] | STD |
| `021-510` ⚡ | 21-51 | **Environmental Cooling Unit (Electric / Vapour-Cycle / Cryo-Integrated)**[^c-2151] | STD |
| `021-510-010` | 21-51-… | Electrically-driven cooling compressor / unit | G-subject |
| `021-510-030` | 21-51-… | Heat-exchanger network | G-subject |
| `021-510-050` | 21-51-… | Working-fluid / refrigerant loop (vapour-cycle) · or cryogenic cold-sink interface | G-subject |
| `021-510-070` | 21-51-… | Water extraction and humidity control | G-subject |
| `021-510-090` | 21-51-… | Cooling-control sensors and protection | G-subject |
| `021-600` | 21-60 | Temperature control | STD |
| `021-610` | 21-61 | Cockpit-zone temperature control — zone/duct sensors | STD |
| `021-620` | 21-62 | Passenger-cabin-zone temperature control — trim-air system[^c-2162] | STD |
| `021-900` | — | **Energy-System Thermal Integration** | STD-G |
| `021-900-010` | — | Energy-source waste-heat recovery (heating) | G-subject |
| `021-900-030` | — | Cryogenic cold-sink utilization (cooling) | G-subject |
| `021-900-050` | — | ECS ↔ thermal-management-system coupling | G-subject |
| `021-900-070` | — | Bleedless air-supply interface (e-compressor / process air) | G-subject |

---

## 5. Programme Binding — eWTW / hBWB

| Node | Agnostic green binding | **eWTW** (electric) | **hBWB** (hydrogen) |
|---|---|---|---|
| `021-510` Cooling unit | electric / vapour-cycle / cryo-integrated | motor-driven compressor + vapour-cycle | cryogenic-H₂ cold-sink heat exchanger |
| `021-900` Thermal integration | waste-heat + cold-sink + ECS coupling | battery/inverter waste-heat → cabin heat | fuel-cell waste-heat + LH₂ cold sink |
| `021-900-070` Air supply | bleedless e-compressor / process air | electric compressor | fuel-cell process-air + e-compressor |
| `021-620` Trim air (minor div.) | electric trim heating | resistive / heat-pump trim | fuel-cell heat trim |
| `021-400` Heating | electric (carried) | floor-panel + waste-heat | floor-panel + FC waste-heat |
| `020-900` High-energy practices | HV-EWIS, storage handling, cryo lines | HVDC EWIS, battery handling | cryo-line, H₂ EWIS practices |

The bleed-air *source* a conventional ECS depends on (ATA 36 Pneumatic) has no green supplier here — under the bleedless binding it is replaced by the `021-900-070` interface and cross-references the propulsion/energy bands.

---

## 6. Governance

Inherits **DEGF v1.0**; governed across **LC-A … LC-N**; bound by **No-AAA** and **SSOT+PUB**. STD/STD-G nodes are the SSOT standard; programme carriers (§5) project into the programme CSDB (PUB). Owner **Q-AIR**; green overlay **Q-GREENTECH**.

---

## References

1. ATA / Airlines for America — *iSpec 2200: Information Standards for Aviation Maintenance*. <a href="https://publications.airlines.org/">https://publications.airlines.org/</a>
2. Embraer — *ATA breakdown, EMB 170/175/190/195 and Lineage 1000* (heritage footprint source, chapters 20–21).
3. S1000D — *International Specification for Technical Publications* (SNS; baseline Issue 4.2). <a href="https://s1000d.org/">https://s1000d.org/</a>

---

## Conventional Heritage Footprint

[^ref]: Embraer, *ATA Breakdown — EMB 170/175/190/195 and Lineage 1000*, chapters 20–21 (uploaded reference). Conventional bindings are transcribed for heritage cross-walk only and are **not** part of the green-native G-ATLAS standard.

[^c-2150]: **Conventional `21-50` — Cooling.** The conventional cooling source is engine **bleed air** processed by an air-cycle pack. Superseded green-native by electrically-driven / energy-integrated environmental cooling.

[^c-2151]: **Conventional `21-51` — Cooling Pack (air-cycle).** Subjects: pack flow-control valves; flow-sensing venturis; venturi DP sensors; dual heat exchangers; **air-cycle machines (ACM)**; condenser/reheaters; water collectors and spray nozzles; fan/pack/low-limit bypass valves; primary-HX-outlet, compressor-outlet, condenser-inlet, pack inlet/outlet temperature sensors; add-heat valves; pack inlet/bypass and outlet ducts; ACM vibration isolators. Superseded green-native by an electrically-driven compressor with vapour-cycle or cryogenic cold-sink heat exchange.

[^c-2162]: **Conventional `21-62` — Trim air.** Hot **bleed-air** trim: trim-air system leak detectors, modulating valves, mufflers, ejectors, ducts, servo lines. Superseded green-native by electric (resistive / heat-pump) zone trim heating.
