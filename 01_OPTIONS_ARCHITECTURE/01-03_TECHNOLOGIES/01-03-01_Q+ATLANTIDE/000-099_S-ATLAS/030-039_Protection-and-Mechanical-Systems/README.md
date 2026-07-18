---
node: 030-039
title: Protection and Mechanical Systems — S-ATLAS Green-Native Breakdown (030, 031)
band: 000-099_S-ATLAS
master_range: 030-039
ssot_path: "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_S-ATLAS/030-039_Protection-and-Mechanical-Systems"
nodes_in_this_file: ["030 Ice and Rain Protection", "031 Indicating and Recording Systems"]
view: green-native (canonical)
heritage_source: "ATA breakdown, Embraer 170/175/190/195 and Lineage 1000 (chapters 30 Ice and Rain Protection, 31 Indicating/Recording Systems)"
principle: "030: bleed-air anti-ice -> electrothermal (⚡), the band's sharpest bleed divergence; rest already-electric (carries). 031: avionics/information, carries whole + green delta for energy-system indicating/recording."
numbering_map: "ATA CC-SS-UU  →  S-ATLAS 0CC-SS0-UU0"
owner_030: Q-AIR
owner_031: Q-AIR
data_owner_031_900: Q-DATAGOV
green_overlay: Q-GREENTECH
governance: [DEGF-v1.0, LC-A..LC-N, No-AAA, SSOT+PUB, S-ATLAS-NORM-TERM-001]
status: baseline
version: "1.0"
---

# 030-039 — Protection and Mechanical Systems · Green-Native Breakdown (030 · 031)

Two chapters at opposite ends of the green divergence. **030** carries the band's sharpest bleed substitution — thermal anti-icing was bleed-air, and with no engine bleed it goes electrothermal — while everything already electric (probe, windshield, water-line heating; ice detection) carries unchanged. **031** is an avionics/information chapter: energy-neutral, it carries whole, with a green delta for indicating and recording the energy, high-voltage, and thermal state.

---

## Index

- [Glossary](#glossary)
- [1. Green-Native Doctrine for 030 / 031](#1-green-native-doctrine-for-030--031)
- [2. Numbering Map](#2-numbering-map)
- [3. Chapter 030 — Ice and Rain Protection](#3-chapter-030--ice-and-rain-protection)
- [4. Chapter 031 — Indicating and Recording Systems](#4-chapter-031--indicating-and-recording-systems)
- [5. Programme Binding — eWTW / hBWB](#5-programme-binding--ewtw--hbwb)
- [6. Governance](#6-governance)
- [References](#references)
- [Conventional Heritage Footprint](#conventional-heritage-footprint)

---

## Glossary

| Term | Meaning |
|---|---|
| **Anti-ice (thermal)** | Ice prevention by heating a surface; conventionally bleed-air, green-native electrothermal. |
| **Electrothermal** | Anti-ice/de-ice by electric heating elements (bleedless). |
| **Propulsion module** | Agnostic term for the engine/powerplant (S-ATLAS-NORM-TERM-001). |
| **CAS** | Crew Alerting System — vendor-neutral term for EICAS-class crew messages (S-ATLAS-NORM-TERM-001). |
| **DPP** | Digital Product Passport — lifecycle health/parameter record. |
| **STD / ⚡ / ◇ / STD-G** | carries · substitution · green overlay on a carrying section · green delta. |

---

## 1. Green-Native Doctrine for 030 / 031

- **030 — Ice and Rain Protection.** The function (keep surfaces and probes ice-free) carries; the *source* of two systems diverges. Wing thermal anti-icing (`030-100`) and engine/nacelle anti-icing (`030-200`) are conventionally **bleed-air**; with no engine bleed they become **⚡ electrothermal**, powered from the HVDC bus. All bleed hardware (anti-ice valves, piccolo/telescopic tubes, swirl nozzles, muscle lines, ducts) drops to footprint. Pitot/static/AOA heating, windshield heating, door heating, water/waste freeze protection, and ice detection are already electric and **carry (STD)**. Green delta `030-900` adds the bleedless/energy-integrated content: electrothermal power architecture, waste-heat anti-icing, the bleedless interface.
- **031 — Indicating and Recording Systems.** Panels, instruments, recorders, central computers, warning, and displays are **energy-neutral electronics** that carry whole. The green content is additive: the indicating/recording must now show and log the energy state (SoC/SoH), HV bus status, and thermal state, and carry new CAS messages for energy/HV/thermal faults. This is green delta `031-900`; the carrying sections that surface it (recorders, warning, display) are marked ◇.

---

## 2. Numbering Map

```text
ATA   CC - SS - UU      →   S-ATLAS  0CC - SS0 - UU0
e.g.  30-11-05  →  030-110-050   ·   31-53-00  →  031-530-000
```

---

## 3. Chapter 030 — Ice and Rain Protection

| S-ATLAS | ATA | Title | Layer |
|---|---|---|:--:|
| `030-000` | 30-00 | **General — Ice and Rain Protection** | STD |
| `030-100` ⚡ | 30-10 | **Airfoil Anti-Ice** (was wing thermal, bleed)[^c-3010] | ⚡ |
| `030-110` ⚡ | 30-11 | Wing anti-ice — electrothermal (was bleed thermal)[^c-3011] | ⚡ |
| `030-200` ⚡ | 30-20 | **Propulsion-Module Inlet Anti-Ice** (was air intakes, bleed)[^c-3020] | ⚡ |
| `030-210` ⚡ | 30-21 | Propulsion-module anti-ice — electric (was engine thermal, bleed)[^c-3021] | ⚡ |
| `030-300` | 30-30 | **Pitot and Static (heating)** | STD |
| `030-310` | 30-31 | Integrated pitot/static/AOA sensor heating | STD |
| `030-320` | 30-32 | Static-port heating | STD |
| `030-330` | 30-33 | TAT-sensor heating | STD |
| `030-400` | 30-40 | **Windows, Windshields and Doors** | STD |
| `030-410` | 30-41 | Windshield wiper | STD |
| `030-420` | 30-42 | Windshield heating | STD |
| `030-430` | 30-43 | Passenger-door heating | STD |
| `030-440` | 30-44 | EFVS window heating | STD |
| `030-700` | 30-70 | **Water/Waste-Line Freeze Protection** | STD |
| `030-710` | 30-71 | Potable-water heating | STD |
| `030-720` | 30-72 | Grey-water heating | STD |
| `030-730` | 30-73 | Recirculating WSP-valve heating | STD |
| `030-740` | 30-74 | Vacuum-waste heating | STD |
| `030-800` | 30-80 | **Ice Detection** | STD |
| `030-810` | 30-81 | Ice detector | STD |
| `030-820` | 30-82 | Super-large-droplet ice detector | STD |
| `030-900` | — | **Bleedless / Energy-Integrated Ice Protection** | STD-G |
| `030-900-010` | — | Electrothermal anti-ice power architecture (from HVDC `024-900`) | G-subject |
| `030-900-030` | — | Waste-heat anti-icing (energy-system recovery; ↔ `021-900`) | G-subject |
| `030-900-050` | — | Bleedless anti-ice air interface (↔ `021-900-070`) | G-subject |
| `030-900-070` | — | Integrated ice-detection and protection control | G-subject |

> The two ⚡ sections are the whole green story of 030. Everything else carries because it was already electric — the chapter is a clean illustration of "substitute the bleed source, leave the electric content alone."

---

## 4. Chapter 031 — Indicating and Recording Systems

| S-ATLAS | ATA | Title | Layer |
|---|---|---|:--:|
| `031-000` | 31-00 | **General — Indicating/Recording** | STD |
| `031-100` | 31-10 | **Instrument and Control Panels** | STD |
| `031-110…170` | 31-11…17 | Main / glareshield / lighting / pedestal / overhead / circuit-breaker / multifunction panels | STD |
| `031-200` | 31-20 | **Independent Instruments** | STD |
| `031-210` | 31-21 | Clock | STD |
| `031-220` | 31-22 | Chronometer | STD |
| `031-300` ◇ | 31-30 | **Recorders** (DVDR / QAR)[^c-3130] | STD |
| `031-310` | 31-31 | Digital voice-data recorder | STD |
| `031-320` | 31-32 | Quick-access recorder | STD |
| `031-400` | 31-40 | **Central Computers** (MAU / ASCB / A429) | STD |
| `031-410` | 31-41 | Modular avionics unit | STD |
| `031-420` | 31-42 | ASCB bus | STD |
| `031-430` | 31-43 | General-purpose A429 bus | STD |
| `031-500` ◇ | 31-50 | **Central Warning** (aural / master / CAS)[^c-3150] | STD |
| `031-510` | 31-51 | Aural warning | STD |
| `031-520` | 31-52 | Master warning/caution | STD |
| `031-530` | 31-53 | Visual warning function (CAS) | STD |
| `031-600` ◇ | 31-60 | **Central Display** | STD |
| `031-610` | 31-61 | Displays | STD |
| `031-620` | 31-62 | Cursor control | STD |
| `031-900` | — | **Energy-System Indicating and Recording** | STD-G |
| `031-900-010` | — | Energy-state indication (SoC/SoH) and display pages (↔ `028-900`) | G-subject |
| `031-900-030` | — | High-voltage system status indication (↔ `024-900`) | G-subject |
| `031-900-050` | — | Green-system CAS message infrastructure (↔ `026-900`, `024-900`, `021-900`) | G-subject |
| `031-900-070` | — | Green-parameter recording for condition monitoring / DPP | G-subject |

> 031 carries whole, like Communications (`023`). The ◇ sections (recorders, warning, display) are the surfaces through which the `031-900` green delta appears; the hardware itself is unchanged.

---

## 5. Programme Binding — eWTW / hBWB

| Node | Agnostic green binding | **eWTW** (electric) | **hBWB** (hydrogen) |
|---|---|---|---|
| `030-110` Wing anti-ice | electrothermal | electrothermal mats from HVDC | electrothermal; waste-heat option from fuel cell |
| `030-210` Propulsion-module anti-ice | electric inlet anti-ice | ducted-fan inlet electrothermal | turbine/fuel-cell inlet anti-ice |
| `030-900-030` Waste-heat anti-icing | energy-system recovery | battery/converter waste heat | fuel-cell / cryo-loop waste heat |
| `031-900-010` Energy-state indication | quantity/state | SoC/SoH pages | LH₂ mass + fuel-cell health pages |
| `031-900-030` HV status | HV bus status | traction HVDC | fuel-cell HVDC |

030 cross-references the HVDC band `024` (anti-ice power), `021-900` (bleedless air / thermal), and `028-900` (waste heat). 031 cross-references `028-900` (SoC/SoH), `024-900` (HV), `026-900`/`021-900` (fire/thermal CAS), and the Digital Product Passport.

---

## 6. Governance

Inherits **DEGF v1.0**; governed across **LC-A … LC-N**; bound by **No-AAA**, **SSOT+PUB**, and **S-ATLAS-NORM-TERM-001** (engine → propulsion module; EICAS → CAS). Owners: **030 → Q-AIR**, **031 → Q-AIR** with **Q-DATAGOV** for the `031-900` recording/DPP delta; green overlay **Q-GREENTECH**. Electrothermal anti-ice power (`030-900-010`) and the green CAS infrastructure (`031-900-050`) couple to safety-critical chapters and carry that flag.

---

## References

1. ATA / Airlines for America — *iSpec 2200*. <a href="https://publications.airlines.org/">https://publications.airlines.org/</a>
2. Embraer — *ATA breakdown, EMB 170/175/190/195 and Lineage 1000* (heritage footprint source, chapters 30–31; internal/proprietary programme reference, no public URL).
3. S1000D — *International Specification for Technical Publications* (SNS; baseline Issue 4.2). <a href="https://s1000d.org/">https://s1000d.org/</a>

---

## Conventional Heritage Footprint

[^c-3010]: **Conventional `30-10/11` — Wing thermal anti-icing (bleed).** Wing anti-ice valve; backwall-temperature and pressure sensors; telescopic tube; piccolo tubes; slat hose; ducts; anti-icing leak detectors; fence tube; A-I wing valve-open-status and no-dispatch-caution EICAS messages. Bleed-air-specific; superseded green-native by electrothermal wing anti-ice. EICAS → CAS.

[^c-3011]: **Conventional `30-11-xx` piccolo/telescopic hardware.** The piccolo-tube/telescopic-tube/slat-hose distribution exists only to carry hot bleed air along the leading edge; it has no electrothermal analogue and is footprint in full.

[^c-3020]: **Conventional `30-20` — Air intakes / engine anti-ice provisions (bleed).** Air intakes; interbulkhead assembly; engine anti-ice shroud leak-detector switch. Superseded by propulsion-module inlet electrothermal anti-ice; "engine" → "propulsion module".

[^c-3021]: **Conventional `30-21` — Engine thermal anti-icing (bleed).** Engine anti-ice valve; pressure transducer; anti-ice duct; piccolo tube; swirl nozzle; muscle line; inlet "D" duct; A-I engine valve-open-status EICAS message. Bleed-specific; superseded by electric propulsion-module inlet anti-ice. EICAS → CAS.

[^c-3130]: **Conventional `31-30` — Recorders.** Digital voice-data recorder (unit, underwater locator beacon, triaxial accelerometer, load cells, impact switch, area microphone, control panel, independent power supply); quick-access recorder. Carries; green-native overlay `031-900-070` adds green-parameter recording for condition monitoring / DPP.

[^c-3150]: **Conventional `31-50/60` — Warning and display.** Aural warning; master warning/caution indication and pushbuttons/annunciators; visual warning function (CAS); displays (unit, reversionary panel, advanced graphics module, "EICAS full panel"); cursor control. Carries; "EICAS full panel" → "CAS full panel". Green overlay `031-900` adds energy/HV/thermal pages and messages.
