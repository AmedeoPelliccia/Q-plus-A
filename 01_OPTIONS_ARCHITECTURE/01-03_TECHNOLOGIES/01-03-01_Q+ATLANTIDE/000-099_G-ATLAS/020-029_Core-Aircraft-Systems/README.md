---
node: 020-029
title: Core Aircraft Systems — G-ATLAS Green-Native Breakdown (020–024)
band: 000-099_G-ATLAS
master_range: 020-029
nodes_in_this_file: ["020 Standard Maintenance Practices", "021 Air Conditioning / Environmental Control", "022 Auto Flight", "023 Communications", "024 Electrical Power"]
view: green-native (canonical)
heritage_source: "ATA breakdown, Embraer 170/175/190/195 and Lineage 1000 (chapters 20–24)"
principle: "Energy-neutral sections carry forward; divergence nodes carry the green binding; conventional content is demoted to the heritage footprint (footnotes)."
numbering_map: "ATA CC-SS-UU  →  G-ATLAS 0CC-SS0-UU0"
owner: Q-AIR
green_overlay: Q-GREENTECH
governance: [DEGF-v1.0, LC-A..LC-N, No-AAA, SSOT+PUB]
status: baseline
version: "1.0"
---

# 020-029 — Core Aircraft Systems · Green-Native Breakdown (020–024)

Five nodes of the Core Aircraft Systems range, normalized from the Embraer ATA reference into the green-native G-ATLAS form. **Chapter 020** (Standard Maintenance Practices) is energy-neutral and carries forward whole, with an additive green delta for high-energy practices. **Chapter 021** (Air Conditioning / ECS) substitutes the conventional bleed-air air-cycle cooling pack with an electrically-driven, energy-integrated cooling architecture; the conventional pack is retained as heritage footprint. **Chapter 022** (Auto Flight) carries forward with one light substitution — Auto Throttle renamed to source-agnostic Autothrust. **Chapter 023** (Communications) carries forward whole. **Chapter 024** (Electrical Power) is the most divergent core system: the conventional engine-driven, AC-primary architecture is inverted to an HVDC-primary, fuel-cell/battery/regenerative one, and the engine IDG is fully footprinted.

---

## Index

- <a>Glossary</a>
- <a>1. Green-Native Doctrine for 020 / 021 / 022 / 023 / 024</a>
- <a>2. Numbering Map</a>
- <a>3. Chapter 020 — Standard Maintenance Practices</a>
- <a>4. Chapter 021 — Air Conditioning / Environmental Control</a>
- <a>5. Chapter 022 — Auto Flight</a>
- <a>6. Chapter 023 — Communications</a>
- <a>7. Chapter 024 — Electrical Power</a>
- <a>8. Programme Binding — eWTW / hBWB</a>
- <a>9. Governance</a>
- <a>References</a>
- <a>Conventional Heritage Footprint</a>

---

## Glossary

| Term | Meaning |
|---|---|
| **Green-native** | Primary binding is the sustainable energy architecture; conventional content is heritage. |
| **Energy-neutral** | A section unaffected by the energy architecture (carries forward unchanged). |
| **Divergence node ⚡** | A section whose conventional content is substituted by a green binding. |
| **EWIS** | Electrical Wiring Interconnection System — dominant content of ch. 20; extends to high-voltage under green. |
| **ECS** | Environmental Control System (ATA 21). |
| **ACM** | Air-Cycle Machine — the bleed-air cooling technology a bleedless aircraft replaces. |
| **Bleedless** | Architecture with no engine bleed air; ECS driven electrically (e-compressor) or by energy-system integration. |
| **IDG** | Integrated Drive Generator — engine-driven, oil-cooled AC generator; no equivalent in a battery-electric architecture. |
| **HVDC** | High-Voltage Direct Current — the primary power bus of an electric/H₂ aircraft. |
| **TRU** | Transformer Rectifier Unit (AC→DC). |
| **RAT** | Ram-Air Turbine (emergency power). |
| **SPDA / ICC** | Secondary Power Distribution Assembly / Integrated Control Center — load-distribution units. |
| **Autothrust** | Automatic power/thrust command; replaces "auto throttle" (source-agnostic). |
| **STD / STD-G** | Agnostic standard section / green-delta section. **G-subject** = green-native subject. |
| **Heritage footprint** | Conventional binding retained in footnotes, cited to the reference. |

---

## 1. Green-Native Doctrine for 020 / 021 / 022 / 023 / 024

- **020 Standard Maintenance Practices — carries forward whole.** Torque, safetying, tubing, bearings, EWIS wiring, connectors, soldering, ESD, bonding, cleaning, and inspections are universal and architecture-neutral. EWIS in fact *expands* under electrification. No substitution; one additive green delta `020-900` for high-voltage / energy-storage / cryogenic-line practices.
- **021 Air Conditioning / ECS — one major substitution.** Distribution, ventilation, pressurization, relief, and temperature control are energy-neutral and carry forward. The **cooling pack** (`021-510`, conventional ACM/bleed) is substituted ⚡ by an electrically-driven / vapour-cycle / cryo-integrated cooling unit, and a green delta `021-900` adds energy-system thermal integration with no ATA equivalent. Heating (`021-400/410`) is already electric and stays.
- **022 Auto Flight — carries forward; one light substitution.** **Auto Throttle → Autothrust / Power Management** (`022-300`), source-agnostic. FGCS, autopilot servos and cables are flight-control actuation and stay STD.
- **023 Communications — carries forward whole, no substitution.** Radios, antennas, SATCOM, datalink, audio, and static dischargers are energy-neutral. Quantum communication is a separate band (`900-999 QCSAA`), not a green delta here.
- **024 Electrical Power — inverted to green-native.** Substituted ⚡: **AC Generation → Primary Power Generation** (`024-200`), **Generator Drive (IDG) → Generation-Source Drive & Conditioning** (`024-210`, IDG fully footprinted), **APU AC Generation → Auxiliary Power Generation** (`024-220`). Green delta `024-900` adds the **HVDC systems-power architecture & power electronics**. Distribution, breakers, batteries, external power, converters/inverters, and outlets carry forward. Traction/propulsion HVDC is **not** here — it lives in the propulsion band `070-079`.

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

## 5. Chapter 022 — Auto Flight

| G-ATLAS | ATA | Title | Layer |
|---|---|---|:--:|
| `022-000` | 22-00 | General — Auto Flight | STD |
| `022-100` | 22-10 | Autopilot | STD |
| `022-110` | 22-11 | Flight Guidance and Control System (FGCS) — guidance panel, AP/trim & TCS pushbuttons, aileron/elevator/rudder servos and cables | STD |
| `022-300` ⚡ | 22-30 | **Autothrust / Power Management**[^c-2230] | STD |
| `022-310` ⚡ | 22-31 | Autothrust function | STD |
| `022-310-010` | 22-31-… | Energy-source-agnostic power/thrust command | G-subject |

---

## 6. Chapter 023 — Communications

Energy-neutral throughout — carries forward whole. No substitution, no green delta.

| G-ATLAS | ATA | Title | Layer |
|---|---|---|:--:|
| `023-000` | 23-00 | General — Communications | STD |
| `023-010` | 23-01 | Communication antennas | STD |
| `023-100` | 23-10 | Speech communications | STD |
| `023-110` | 23-11 | HF communication system | STD |
| `023-120` | 23-12 | VHF communication system | STD |
| `023-140` | 23-14 | V/UHF communication system | STD |
| `023-150` | 23-15 | SATCOM system (Iridium, telephony, fax) | STD |
| `023-200` | 23-20 | Data transmission and automatic calling | STD |
| `023-210` | 23-21 | SELCAL | STD |
| `023-220` | 23-22 | Wireless aircraft data link (WADL) | STD |
| `023-230` | 23-23 | Wireless Gatelink system | STD |
| `023-240` | 23-24 | Communication management function | STD |
| `023-250` | 23-25 | Controller-Pilot Datalink Communications (CPDLC) | STD |
| `023-500` | 23-50 | Audio integrating | STD |
| `023-510` | 23-51 | Airborne audio system | STD |
| `023-520` | 23-52 | Ramp interphone | STD |
| `023-600` | 23-60 | Static discharging | STD |
| `023-610` | 23-61 | Static dischargers | STD |

---

## 7. Chapter 024 — Electrical Power

Section skeleton retained; generation ⚡ substituted; HVDC architecture as a first-class green delta. Distribution / breakers / outlets carry forward.

| G-ATLAS | ATA | Title | Layer |
|---|---|---|:--:|
| `024-000` | 24-00 | General — Electrical Power (control panel, breakers, relay supports, multi-system harnesses) | STD |
| `024-010` | 24-01 | Multi-system harness | STD |
| `024-020` | 24-02 | Multi-system harness | STD |
| `024-030` | 24-03 | Wing harness | STD |
| `024-200` ⚡ | 24-20 | **Primary Power Generation**[^c-2420] | STD |
| `024-200-010` | 24-20-… | Primary power-source output and control | G-subject |
| `024-200-030` | 24-20-… | Generation control unit (GCU equivalent) | G-subject |
| `024-200-050` | 24-20-… | Generation line contactor | G-subject |
| `024-210` ⚡ | 24-21 | **Generation-Source Drive and Conditioning**[^c-2421] | STD |
| `024-210-010` | 24-21-… | Source power conditioning (rectify / invert) | G-subject |
| `024-210-030` | 24-21-… | Source thermal-management interface | G-subject |
| `024-220` ⚡ | 24-22 | **Auxiliary Power Generation**[^c-2422] | STD |
| `024-220-010` | 24-22-… | Auxiliary power source (fuel-cell / battery / e-APU) | G-subject |
| `024-220-030` | 24-22-… | Auxiliary generation control and contactors | G-subject |
| `024-230` | 24-23 | Emergency / Backup Power (RAT or battery) | STD |
| `024-240` | 24-24 | Power-electronics inversion (static inverter) | STD |
| `024-250` | 24-25 | AC conversion (converters) | STD |
| `024-300` | 24-30 | DC power sourcing | STD |
| `024-310` | 24-31 | DC rectification (TRU) | STD |
| `024-330` | 24-33 | DC–DC conversion | STD |
| `024-360` | 24-36 | Aircraft energy storage (systems batteries) | STD |
| `024-400` | 24-40 | External / ground power | STD |
| `024-410` | 24-41 | External DC power | STD |
| `024-420` | 24-42 | External AC power | STD |
| `024-500` | 24-50 | AC electrical load distribution | STD |
| `024-510` | 24-51 | AC power distribution (ICCs, SPDA) | STD |
| `024-520` | 24-52 | AC circuit breakers | STD |
| `024-540` | 24-54 | AC electrical outlets | STD |
| `024-600` | 24-60 | DC electrical load distribution | STD |
| `024-610` | 24-61 | DC power distribution (SPDA) | STD |
| `024-640` | 24-64 | DC circuit breakers | STD |
| `024-660` | 24-66 | DC electrical outlets | STD |
| `024-900` | — | **High-Voltage DC Systems-Power Architecture & Power Electronics** | STD-G |
| `024-900-010` | — | High-voltage DC systems bus | G-subject |
| `024-900-030` | — | Systems-power conversion from propulsion HVDC (DC–DC) | G-subject |
| `024-900-050` | — | Regenerative systems-power recovery | G-subject |
| `024-900-070` | — | Systems energy-storage management | G-subject |
| `024-900-090` | — | High-power ground-charging interface | G-subject |

> The propulsion HVDC bus, traction inverters, and main propulsion energy storage are **not** in ATA 24 here — they belong to the propulsion band `070-079`. `024-900` covers only the *systems* HVDC architecture and its coupling to that bus.

---

## 8. Programme Binding — eWTW / hBWB

| Node | Agnostic green binding | **eWTW** (electric) | **hBWB** (hydrogen) |
|---|---|---|---|
| `021-510` Cooling unit | electric / vapour-cycle / cryo-integrated | motor-driven compressor + vapour-cycle | cryogenic-H₂ cold-sink heat exchanger |
| `021-900` Thermal integration | waste-heat + cold-sink + ECS coupling | battery/inverter waste-heat → cabin heat | fuel-cell waste-heat + LH₂ cold sink |
| `021-900-070` Air supply | bleedless e-compressor / process air | electric compressor | fuel-cell process-air + e-compressor |
| `021-620` Trim air (minor div.) | electric trim heating | resistive / heat-pump trim | fuel-cell heat trim |
| `021-400` Heating | electric (carried) | floor-panel + waste-heat | floor-panel + FC waste-heat |
| `020-900` High-energy practices | HV-EWIS, storage handling, cryo lines | HVDC EWIS, battery handling | cryo-line, H₂ EWIS practices |
| `022-300` Autothrust | power/thrust command | motor-power command | fuel-flow / FC-power command |
| `024-200` Primary generation | source-agnostic primary power | battery-primary + regenerative | fuel-cell stack + turbine-generator |
| `024-210` Source drive & conditioning | power-electronic (no mechanical CSD) | inverter/converter chain | FC + generator power conditioning |
| `024-220` Auxiliary power | fuel-cell / battery / e-APU | battery / e-APU | fuel-cell APU |
| `024-230` Emergency / backup | battery or RAT | battery backup | battery + RAT |
| `024-360` Systems energy storage | aircraft batteries | LV battery fed from HVDC | LV battery fed from FC/HVDC |
| `024-900` HVDC systems architecture | HVDC bus + DC–DC + regen | HVDC tapped from traction bus | HVDC tapped from fuel-cell bus |

The bleed-air *source* a conventional ECS depends on (ATA 36 Pneumatic) has no green supplier here — under the bleedless binding it is replaced by the `021-900-070` interface and cross-references the propulsion/energy bands. The conventional engine **IDG** (`024-210`) has no battery-electric equivalent and is dropped, not adapted; in the hybrid/H₂ binding it is replaced by power-electronic conditioning of the e-machine and generator sources.

---

## 9. Governance

Inherits **DEGF v1.0**; governed across **LC-A … LC-N**; bound by **No-AAA** and **SSOT+PUB**. STD/STD-G nodes are the SSOT standard; programme carriers (§8) project into the programme CSDB (PUB). Owner **Q-AIR**; green overlay **Q-GREENTECH**. Cross-references the propulsion band `070-079` for traction HVDC and main energy storage.

---

## References

1. ATA / Airlines for America — *iSpec 2200: Information Standards for Aviation Maintenance*. <a href="https://publications.airlines.org/">https://publications.airlines.org/</a>
2. Embraer — *ATA breakdown, EMB 170/175/190/195 and Lineage 1000* (heritage footprint source, chapters 20–24).
3. S1000D — *International Specification for Technical Publications* (SNS; baseline Issue 4.2). <a href="https://s1000d.org/">https://s1000d.org/</a>

---

## Conventional Heritage Footprint

[^ref]: Embraer, *ATA Breakdown — EMB 170/175/190/195 and Lineage 1000*, chapters 20–24 (uploaded reference). Conventional bindings are transcribed for heritage cross-walk only and are **not** part of the green-native G-ATLAS standard.

[^c-2150]: **Conventional `21-50` — Cooling.** The conventional cooling source is engine **bleed air** processed by an air-cycle pack. Superseded green-native by electrically-driven / energy-integrated environmental cooling.

[^c-2151]: **Conventional `21-51` — Cooling Pack (air-cycle).** Subjects: pack flow-control valves; flow-sensing venturis; venturi DP sensors; dual heat exchangers; **air-cycle machines (ACM)**; condenser/reheaters; water collectors and spray nozzles; fan/pack/low-limit bypass valves; primary-HX-outlet, compressor-outlet, condenser-inlet, pack inlet/outlet temperature sensors; add-heat valves; pack inlet/bypass and outlet ducts; ACM vibration isolators. Superseded green-native by an electrically-driven compressor with vapour-cycle or cryogenic cold-sink heat exchange.

[^c-2162]: **Conventional `21-62` — Trim air.** Hot **bleed-air** trim: trim-air system leak detectors, modulating valves, mufflers, ejectors, ducts, servo lines. Superseded green-native by electric (resistive / heat-pump) zone trim heating.

[^c-2230]: **Conventional `22-30/31` — Auto Throttle.** Automatic command of engine thrust levers (auto throttle function). Superseded green-native by source-agnostic autothrust / power-command management.

[^c-2420]: **Conventional `24-20` — AC Generation.** Engine-driven 115 VAC generation with main Generator Control Unit (GCU) and Generator Line Contactor (GLC). Superseded green-native by source-agnostic primary power generation (fuel-cell / battery / regenerative).

[^c-2421]: **Conventional `24-21` — Generator Drive System (IDG).** Integrated Drive Generator: constant-speed mechanical drive plus generator, with IDG oil system, air/oil and fuel/oil heat exchangers, oil-out filter element, differential-pressure indicator, overflow and case drain-plug assemblies, V-band clamp, cable grounding fitting, main GCU and GLC. Engine-mechanical and oil-cooled; **no equivalent in a battery-electric architecture** — dropped, not adapted. In hybrid/H₂ bindings replaced by power-electronic conditioning of the e-machine / fuel-cell source.

[^c-2422]: **Conventional `24-22` — APU AC Generation.** APU-driven AC generator with AGCU, ALC, APU start contactor (ASC), APU start bus contactor (ABC). Superseded green-native by fuel-cell / battery / electric auxiliary power.
