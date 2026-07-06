---
node: 003-900
title: Energy-Replenishment Ground Infrastructure — ECHM Subjects Breakdown
path: "…/01_INFORMATION-ARCHITECTURE/G-ATLAS_000-099/003-900_Energy-Replenishment-Ground-Infrastructure/"
pmc: PMC-EWTW-ECHM
model: eWTW
mic: EWTW
side: PUB
ssot_source: "G-ATLAS 003-900 (agnostic, SSOT) — Support chapter green delta"
projection: "eWTW electric/charging binding (H2 not applicable — see hBWB sibling)"
feeds_tree: [ECHM-10, ECHM-40, ECHM-60]
owner: Q-GREENTECH
governance: [DEGF-v1.0, LC-A..LC-N, No-AAA, SSOT+PUB]
status: baseline
version: "1.0"
---

# 003-900 — Energy-Replenishment Ground Infrastructure · ECHM Subjects Breakdown

The leaf of the ECHM pipeline. The agnostic SSOT node **`003-900`** (the infrastructure side of energy replenishment, sibling to the servicing-side `012-900`) is projected here into the **eWTW** charging binding: nine handling subjects, each allocated a DMC and an applicability rule, mapped to the ECHM publication tree.

---

## Index

- [Glossary](#glossary)
- [1. Derivation — SSOT to eWTW Subjects](#1-derivation--ssot-to-ewtw-subjects)
- [2. Subjects Breakdown](#2-subjects-breakdown)
- [3. Tree Mapping](#3-tree-mapping)
- [4. Applicability](#4-applicability)
- [References](#references)

---

## Glossary

| Term | Meaning |
|---|---|
| **Subject** | A documentation topic; one or more DMs are allocated to it. |
| **DMC** | Data Module Code — `DMC-EWTW-<node>-<item>-<infocode>`. |
| **Info code** | S1000D content class (040 descr · 034 operation · 200 servicing · 720 connect · 420 fault). Representative. |
| **Projection** | The eWTW (electric/charging) binding of the agnostic SSOT node. |
| **MCS** | Megawatt Charging System — emerging high-power conductive charging interface class (binding example). |

---

## 1. Derivation — SSOT to eWTW Subjects

SSOT node `003-900` is energy-carrier-**neutral** (it describes *replenishment infrastructure* without naming the carrier). Because this is `PMC-EWTW-ECHM`, the impact analysis binds it to the **electric/charging** form. The hydrogen form (cryogenic dispensing, LH₂ coupling) is **not applicable** here and is projected separately in the hBWB sibling manual. The subjects below are the eWTW projection; the agnostic function each derives from is named alongside.

---

## 2. Subjects Breakdown

| Subject (eWTW) | Agnostic function (SSOT) | Primary DMC | Info |
|---|---|---|:--:|
| `003-900-010` Ground charging connection interface (charging inlet / high-power coupling) | replenishment connection interface | `DMC-EWTW-003-900-010-040` | 040 |
| `003-900-020` Ground charging source and supply (charger, grid interface, MCS-class) | replenishment energy source | `DMC-EWTW-003-900-020-040` | 040 |
| `003-900-030` Charging process control and sequencing (profile, ramp, termination) | replenishment control & sequencing | `DMC-EWTW-003-900-030-034` | 034 |
| `003-900-040` Charging safety, isolation, grounding and bonding (HV interlocks) | replenishment safety & isolation | `DMC-EWTW-003-900-040-040` | 040 |
| `003-900-050` Charging communication protocol (aircraft ↔ charger handshake, smart charging) | replenishment communication | `DMC-EWTW-003-900-050-034` | 034 |
| `003-900-060` Battery thermal pre-conditioning during charging | replenishment thermal conditioning | `DMC-EWTW-003-900-060-200` | 200 |
| `003-900-070` Charge metering and energy-transfer verification | replenishment metering | `DMC-EWTW-003-900-070-034` | 034 |
| `003-900-080` Charging-infrastructure compatibility & interface standards | infrastructure compatibility | `DMC-EWTW-003-900-080-040` | 040 |
| `003-900-090` Abnormal charging & emergency disconnect | abnormal replenishment & disconnect | `DMC-EWTW-003-900-090-420` | 420 |

Each subject additionally spawns **handling-procedure DMs** under the connect/operate/disconnect info codes (720 / 200 / 730) — e.g. `DMC-EWTW-003-900-010-720` (connect procedure for the charging interface). The table lists the primary DM per subject; the full info-coded set is in `node-subject-register.yaml`.

---

## 3. Tree Mapping

A subject may be referenced by more than one ECHM publication-tree entry (DM reuse):

| ECHM tree entry | Subjects referenced |
|---|---|
| **ECHM-10** Energy-Carrier Replenishment | `010 · 020 · 030 · 050 · 060 · 070` |
| **ECHM-40** Hazards, Placards and Isolation | `040 · 090` |
| **ECHM-60** Ground-Infrastructure Interface | `010 · 020 · 080` |

---

## 4. Applicability

All subjects bind to **eWTW** (electrical-charge carrier). The hydrogen/cryogenic forms are **not applicable** and are excluded by the ECHM applicability study; they project in the hBWB ECHM. `003-900-060` (thermal pre-conditioning) and `003-900-040` (HV isolation) cross-reference the energy-store thermal/fire deltas `028-900-090` and `026-900`.

---

## References

1. S1000D — *International Specification for Technical Publications* (DM, DMC, info codes; baseline Issue 4.2). [https://s1000d.org/](https://s1000d.org/)
2. G-ATLAS SSOT — node `003-900` (Support chapter green delta), agnostic source.
