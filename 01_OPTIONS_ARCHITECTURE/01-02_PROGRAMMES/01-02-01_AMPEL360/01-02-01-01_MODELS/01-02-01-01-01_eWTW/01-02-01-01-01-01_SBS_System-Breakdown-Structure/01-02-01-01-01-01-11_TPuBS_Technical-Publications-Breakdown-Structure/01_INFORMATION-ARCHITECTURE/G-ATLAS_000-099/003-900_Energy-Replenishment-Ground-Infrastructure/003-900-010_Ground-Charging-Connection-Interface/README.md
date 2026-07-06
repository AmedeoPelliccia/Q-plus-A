---
subject: 003-900-010
title: Ground Charging Connection Interface — Subject Package
path: "01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure/01_INFORMATION-ARCHITECTURE/G-ATLAS_000-099/003-900_Energy-Replenishment-Ground-Infrastructure/003-900-010_Ground-Charging-Connection-Interface/"
pmc: PMC-EWTW-ECHM
parent_node: 003-900
model: eWTW
mic: EWTW
side: PUB
owner: Q-GREENTECH
feeds_tree: [ECHM-10, ECHM-60]
dm_set: ["040", "034", "720", "730"]
excluded: ["420 (FIM scope)"]
sns_status: "PROVISIONAL — pending _CSDB-CONTROL/SNS-mapping.yaml"
governance: [DEGF-v1.0, LC-A..LC-N, No-AAA, SSOT+PUB]
status: baseline
version: "1.0"
---

# 003-900-010 — Ground Charging Connection Interface · Subject Package

The authoritative TPuBS container for the on-aircraft charging interface: the physical and operational connection between the eWTW aircraft and the ground charging infrastructure. The carrier-neutral SSOT subject `003-900-010` (*replenishment connection interface*) is projected here to the **electric** form; four S1000D data modules realise it, feeding the **ECHM-10** and **ECHM-60** publication-tree entries.

---

## Index

- [1. Location](#1-location)
- [2. Directory Tree](#2-directory-tree)
- [3. Package Contents](#3-package-contents)
- [4. DMC Allocation](#4-dmc-allocation)
- [5. Data Modules](#5-data-modules)
- [6. Illustrations (ICN)](#6-illustrations-icn)
- [7. Evidence](#7-evidence)
- [8. Applicability & BREX](#8-applicability--brex)
- [9. Scope Boundaries](#9-scope-boundaries)
- [10. Cross-References](#10-cross-references)
- [References](#references)

---

## 1. Location

```text
…/01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure/
  └── PMC-EWTW-ECHM_Energy-Carrier-Handling-Manual/
      └── 000-099_G-ATLAS/
          └── 003-900_Energy-Replenishment-Ground-Infrastructure/
              └── 003-900-010_Ground-Charging-Connection-Interface/   ← this package
```

---

## 2. Directory Tree

```text
003-900-010_Ground-Charging-Connection-Interface/
├── README.md                          # this file
├── subject-metadata.yaml              # subject definition, projection, ownership
├── dm-register.yaml                   # DM allocation (040/034/720/730); 420 excluded → FIM
├── applicability.yaml                 # eWTW binding; hydrogen excluded
├── DM/                                # data-module store (flat — CSDB convention)
│   ├── DMC-EWTW-A-03-90-01-00A-040A-A_001-00_en-GB.xml   # Description
│   ├── DMC-EWTW-A-03-90-01-00A-034A-A_001-00_en-GB.xml   # Operating principles
│   ├── DMC-EWTW-A-03-90-01-00A-720A-A_001-00_en-GB.xml   # Connect procedure
│   └── DMC-EWTW-A-03-90-01-00A-730A-A_001-00_en-GB.xml   # Disconnect procedure
├── ICN/                               # illustrations (ICN-coded)
│   ├── ICN-EWTW-003900010-001-01.svg                     # inlet location
│   ├── ICN-EWTW-003900010-002-01.svg                     # engagement sequence / contacts
│   └── ICN-EWTW-003900010-003-01.svg                     # grounding / bonding sequence
├── evidence/                          # leaf-level traceability
│   ├── interface-requirements-matrix.md
│   ├── standards-cross-reference.md
│   └── verification-status.yaml
└── pub/                               # PM pointers (link index — not copies)
    ├── ECHM-10.link
    └── ECHM-60.link
```

---

## 3. Package Contents

| File | Purpose |
|---|---|
| `subject-metadata.yaml` | Subject definition, eWTW projection, ownership, tree feed. |
| `dm-register.yaml` | DM allocation and ICN register; `420` exclusion recorded. |
| `applicability.yaml` | Binds all DMs to eWTW; excludes the hydrogen form. |
| `DM/…-040A-A_001-00_en-GB.xml` | Description — the interface as installed. |
| `DM/…-034A-A_001-00_en-GB.xml` | Operating principles — readiness / enable logic. |
| `DM/…-720A-A_001-00_en-GB.xml` | Connect procedure. |
| `DM/…-730A-A_001-00_en-GB.xml` | Disconnect procedure. |
| `ICN/ICN-EWTW-003900010-001-01.svg` | Inlet location and access. |
| `ICN/ICN-EWTW-003900010-002-01.svg` | Engagement sequence / contact arrangement. |
| `ICN/ICN-EWTW-003900010-003-01.svg` | Grounding / bonding sequence and latch. |
| `evidence/interface-requirements-matrix.md` | Requirement → DM → verification trace. |
| `evidence/standards-cross-reference.md` | Standards map (TBDs flagged, none invented). |
| `evidence/verification-status.yaml` | Per-DM QA state and LC gates. |
| `pub/ECHM-10.link` | Pointer to ECHM-10 PM entry. |
| `pub/ECHM-60.link` | Pointer to ECHM-60 PM entry. |

---

## 4. DMC Allocation

SNS (`systemCode 03 · subSystem 9 · subSubSystem 0 · assy 01`) is **derived** from the G-ATLAS triplet and **provisional** pending `_CSDB-CONTROL/SNS-mapping.yaml`. The short handle is the stable identifier.

| Short handle | Full DMC (provisional) | Info | Type |
|---|---|---|---|
| `DMC-EWTW-003-900-010-040` | `DMC-EWTW-A-03-90-01-00A-040A-A` | 040 | Description |
| `DMC-EWTW-003-900-010-034` | `DMC-EWTW-A-03-90-01-00A-034A-A` | 034 | Operating principles |
| `DMC-EWTW-003-900-010-720` | `DMC-EWTW-A-03-90-01-00A-720A-A` | 720 | Connect procedure |
| `DMC-EWTW-003-900-010-730` | `DMC-EWTW-A-03-90-01-00A-730A-A` | 730 | Disconnect procedure |

> **`420` (fault isolation) is excluded** from this package: fault isolation is FIM scope, not handling. It projects in the FIM PMC; connection-related abnormal handling stays at sibling subject `003-900-090`.

---

## 5. Data Modules

- **`040` Description** — the interface as installed: high-power conductive coupling (MCS-class), location/access, contact arrangement (HV power, first-make/last-break protective earth, pilot contacts), latch/lock, cover and seal, bonding point, path to the HV charging input (`028-900`).
- **`034` Operating principles** — readiness and enable logic only: the conditions under which transfer is enabled (mated, locked, earthed, bonded, interlock closed, handshake established) and the connection status states. The protocol itself is `003-900-050`.
- **`720` Connect** — area-safety → bonding → mate/latch → interlock → handshake → authorise. HV / arc-flash warnings; no-mate-under-load.
- **`730` Disconnect** — terminate → verify de-energised → confirm zero-voltage interlock → unlatch → demate → cap/stow → remove bonding → post-check.

---

## 6. Illustrations (ICN)

| ICN | Caption | Used by |
|---|---|---|
| `ICN-EWTW-003900010-001-01` | Charging inlet location and access | `040` |
| `ICN-EWTW-003900010-002-01` | Connector engagement sequence / contacts | `040`, `034`, `720` |
| `ICN-EWTW-003900010-003-01` | Grounding / bonding sequence and latch | `720`, `730` |

> SVGs are placeholder stubs pending illustration.

---

## 7. Evidence

The `evidence/` folder closes leaf-level traceability: the requirements matrix links each interface requirement to the DM(s) documenting it and its verification method; the standards cross-reference maps topics to standards (with TBDs flagged, none invented); `verification-status.yaml` records per-DM QA state. These gate the subject from `unverified` to validated.

---

## 8. Applicability & BREX

All DMs bind to **eWTW** (electrical-charge carrier); the hydrogen/cryogenic coupling form is **not applicable** and projects in the hBWB ECHM sibling without changing the SSOT. Each DM references the programme BREX `DMC-EWTW-A-00-00-00-00A-022A-D`. Security `01` (unclassified); issue `001-00`, `inWork`, quality `unverified`.

---

## 9. Scope Boundaries

**Included:** aircraft charging inlet · ground connector engagement · mechanical locking · HV enable conditions · grounding sequence · connection status indication · handshake initiation · connect/disconnect procedures.

**Excluded → routed to:**

| Out of scope | Subject |
|---|---|
| Energy source / supply architecture | `003-900-020` |
| Charging sequencing logic | `003-900-030` |
| HV isolation philosophy | `003-900-040` |
| Communication protocol specification | `003-900-050` |
| Infrastructure compatibility policy | `003-900-080` |
| Emergency charging disconnect | `003-900-090` |
| Fault isolation (`420`) | FIM PMC |

---

## 10. Cross-References

- `028-900` — aircraft energy store the interface feeds (HV charging input).
- `024-900` — HVDC architecture downstream of the charging input.
- `003-900-050` — charging communication handshake confirmed during connect.
- `003-900-040` / `026-900` — HV isolation, bonding, fire/arc-flash.
- `003-900-060` — battery thermal pre-conditioning that may run during charge.

---

## References

1. S1000D — *International Specification for Technical Publications*, Issue 4.2. [https://s1000d.org/](https://s1000d.org/)
2. G-ATLAS SSOT — node `003-900`, subject `003-900-010` (agnostic source).
