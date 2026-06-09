---
artifact: 021 TPuBS Node Tree
chapter: "021"
title: Air Conditioning & Environmental Control — TPuBS Node Tree
home: "01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure/PMC-EWTW-AMM_Aircraft-Maintenance-Manual/G-ATLAS_000-099/020-029_Core-Aircraft-Systems/021_Air-Conditioning-Environmental-Control/"
pmc: PMC-EWTW-AMM
convention: AMPEL360-AMM-INFOCODE-CM-001
doctrine: green-native
owner: Q-AIR
status: scaffold
version: "1.0"
---

# 021 — TPuBS Node Tree

**The subject is the real TPuBS node.** A subject (`021-SSS-UUU`) is a *directory*, not a file — it **contains the AMM info-code breakdown**. Each info code holds its SSOT/PBS link and configuration management, and resolves to **one folder per effectivity range** (the solution/variant), each holding one S1000D data module. This document maps the chapter, with `021-510-010` developed to full depth.

---

## Legend

| Symbol | Meaning |
|---|---|
| `node/` | directory node |
| `STD` · `⚡` · `STD-G` | carries · electric substitution · green delta |
| `EFF-…/` | effectivity-range solution folder (= `infoCodeVariant`) |
| `▸ same anatomy` | subject node with the same internal structure, collapsed here |

---

## Chapter tree

```text
021_Air-Conditioning-Environmental-Control/
├── README.md
├── 021_TPuBS-Node-Tree.md                         ← this map
│
├── 021-000_General/                               STD
├── 021-200_Distribution/                          STD
├── 021-210_Cockpit-Distribution/                  STD
├── 021-220_Passenger-Cabin-Distribution/          STD
├── 021-230_Gasper/                                STD
├── 021-240_Recirculation/                         STD
├── 021-250_Ram-Air-Ventilation/                   STD
├── 021-260_Avionics-Compartment-Ventilation/      STD
├── 021-270_Cargo-Compartment-Ventilation/         STD
├── 021-280_Miscellaneous-Equipment-and-Chiller-Ventilation/  STD
├── 021-290_Low-Pressure-Ground-Supply/            STD
├── 021-300_Pressurization-Control/                STD
├── 021-310_Pressurization-Control-and-Indication/ STD
├── 021-320_Cabin-Pressure-Relief/                 STD
├── 021-330_Cargo-Compartment-Pressure-Equalization/ STD
├── 021-400_Heating/                               STD
├── 021-410_Floor-Panel-Heating/                   STD
├── 021-500_Environmental-Cooling-Electric-Integrated/   ⚡  [footprint: bleed-air pack]
│
├── 021-510_Environmental-Cooling-Unit-Electric/   ⚡  [footprint: air-cycle machine]
│   ├── README.md
│   │
│   ├── 021-510-010_Electrically-Driven-Cooling-Compressor/   ⚡  ◀── SUBJECT NODE (full depth below)
│   │   ├── README.md
│   │   ├── subject-infocode-breakdown.yaml        # 040×2, 200×1, 520×2, 720×2
│   │   │
│   │   ├── 040_Description/
│   │   │   ├── ssot-ref.yaml                       # PBS: eWTW-PBS-60-20 (ECS — Electric)
│   │   │   ├── config-management.yaml              # BASELINE → MOD-EWTW-021-001 ; affects=true
│   │   │   ├── 040A_EFF-PRE-MOD-021-001/           # MSN 0001-0049
│   │   │   │   └── DMC-EWTW-A-21-51-01-00A-040A-A_001-00_en-GB.xml
│   │   │   └── 040B_EFF-POST-MOD-021-001/          # MSN 0050-*
│   │   │       └── DMC-EWTW-A-21-51-01-00A-040B-A_001-00_en-GB.xml
│   │   │
│   │   ├── 200_Servicing/
│   │   │   ├── ssot-ref.yaml
│   │   │   ├── config-management.yaml              # affects=false → single solution
│   │   │   └── 200A_EFF-ALL/                       # MSN 0001-*
│   │   │       └── DMC-EWTW-A-21-51-01-00A-200A-A_001-00_en-GB.xml
│   │   │
│   │   ├── 520_Remove/
│   │   │   ├── ssot-ref.yaml
│   │   │   ├── config-management.yaml              # affects=true → two solutions
│   │   │   ├── 520A_EFF-PRE-MOD-021-001/
│   │   │   │   └── DMC-EWTW-A-21-51-01-00A-520A-A_001-00_en-GB.xml
│   │   │   └── 520B_EFF-POST-MOD-021-001/
│   │   │       └── DMC-EWTW-A-21-51-01-00A-520B-A_001-00_en-GB.xml
│   │   │
│   │   └── 720_Install/
│   │       ├── ssot-ref.yaml
│   │       ├── config-management.yaml              # affects=true → two solutions
│   │       ├── 720A_EFF-PRE-MOD-021-001/
│   │       │   └── DMC-EWTW-A-21-51-01-00A-720A-A_001-00_en-GB.xml
│   │       └── 720B_EFF-POST-MOD-021-001/
│   │           └── DMC-EWTW-A-21-51-01-00A-720B-A_001-00_en-GB.xml
│   │
│   ├── 021-510-030_Heat-Exchanger-Network/        ⚡   ▸ same anatomy
│   ├── 021-510-050_Working-Fluid-Refrigerant-Loop/ ⚡  ▸ same anatomy
│   ├── 021-510-070_Water-Extraction-and-Humidity-Control/ STD ▸ same anatomy
│   └── 021-510-090_Cooling-Control-Sensors-and-Protection/ ⚡ ▸ same anatomy
│
├── 021-600_Temperature-Control/                   STD
├── 021-610_Cockpit-Zone-Temperature-Control/      STD
├── 021-620_Passenger-Cabin-Zone-Temperature-Control/ STD
│
└── 021-900_Energy-System-Thermal-Integration/     STD-G
    ├── README.md
    ├── 021-900-010_Energy-Source-Waste-Heat-Recovery/    STD-G ▸ same anatomy
    ├── 021-900-030_Cryogenic-Cold-Sink-Utilization/      STD-G ▸ same anatomy
    ├── 021-900-050_ECS-Thermal-Management-System-Coupling/ STD-G ▸ same anatomy
    └── 021-900-070_Bleedless-Air-Supply-Interface/       STD-G ▸ same anatomy
```

> **No `021-100`** — the conventional bleed/compression section is footprinted out (no engine bleed in the green architecture); cooling is electric at `021-500/510`.

---

## Subject-node anatomy (the deep node, explained)

`021-510-010_Electrically-Driven-Cooling-Compressor` is the real node. Its internal layout is the convention `AMPEL360-AMM-INFOCODE-CM-001`:

```text
subject node
 └── <infocode>/                       AMM info code (040/200/520/720…)
       ├── ssot-ref.yaml               one-way PBS source link
       ├── config-management.yaml      modification stack → resulting effectivity
       └── <ic><variant>_EFF-<id>/     one folder per effectivity range  ← solution/variant
             └── DMC-…-<ic><variant>-…xml   the data module (carries <applic>)
```

### Info-code resolution for `021-510-010`

`MOD-EWTW-021-001` (vapour-cycle compressor upgrade, embodied MSN 0050) forks only the info codes whose content it changes:

| Info code | Affected by mod | Solutions | Effectivity |
|---|:--:|---|---|
| `040` Description | yes | `040A`, `040B` | MSN 0001-0049 · 0050-* |
| `200` Servicing | no | `200A` | MSN 0001-* (all) |
| `520` Remove | yes | `520A`, `520B` | MSN 0001-0049 · 0050-* |
| `720` Install | yes | `720A`, `720B` | MSN 0001-0049 · 0050-* |

Each DM carries `<applic>` matching its range, so an IETP filtered to a given MSN resolves to exactly one solution per info code. `infoCodeVariant` (A/B) is the S1000D variant key; the folder name binds it to the effectivity.

> **Fork rule** — a new solution exists only where the mod changes the DM **content** (text, steps or illustration). Each PRE/POST DM pair carries a concrete technical delta (centrifugal → scroll compressor, remote → integrated SiC controller, refrigerant recovery/charge steps), recorded as `content_delta` in the info code's `config-management.yaml`. An effectivity update alone does **not** generate a new solution — it is only a stack update.

---

## References

1. `AMPEL360-AMM-INFOCODE-CM-001` — info-code / effectivity-variant convention.
2. S1000D Issue 4.2 — DM, DMC, info codes, applicability.
3. eWTW SSOT PBS — `eWTW-PBS-60-20_Environmental-Control-System-ECS-Electric` (under `01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-60_Mechanical-and-Utility-Systems/`).
4. G-ATLAS SSOT — chapter 021 (green-native).
