---
subject: 021-230-010
title: Gasper Fan — Subject Package
pmc: PMC-EWTW-AMM
parent_node: 021-230
model: eWTW
mic: EWTW
side: PUB
owner: Q-AIR
feeds_tree: [AMM]
dm_set: ["040", "200", "300", "520", "720"]
sns_status: "PROVISIONAL — pending _CSDB-CONTROL/SNS-mapping.yaml"
status: scaffold
version: "1.0"
---

# 021-230-010 — Gasper Fan · Subject Package

TPuBS container for the **Gasper Fan** subject of chapter `021-230`, projected to the eWTW AMM. Structure mirrors the PMC-EWTW-ECHM subject package (`003-900-010`).

## Directory tree

```text
021-230-010_Gasper-Fan/
├── README.md
├── subject-metadata.yaml
├── dm-register.yaml
├── applicability.yaml
├── DM/                # S1000D 4.2 data modules
├── ICN/               # illustrations
├── evidence/          # leaf-level traceability
└── pub/               # publication-tree pointers
```

## DMC allocation

SNS (`systemCode 21 · subSystem 2 · subSubSystem 3 · assy 01`) is **derived** from the S-ATLAS triplet and **provisional** pending `_CSDB-CONTROL/SNS-mapping.yaml`.

| Short handle | Full DMC (provisional) | Info | Type |
|---|---|---|---|
| `DMC-EWTW-021-230-010-040` | `DMC-EWTW-A-21-23-01-00A-040A-A` | 040 | Description |
| `DMC-EWTW-021-230-010-200` | `DMC-EWTW-A-21-23-01-00A-200A-A` | 200 | Servicing |
| `DMC-EWTW-021-230-010-300` | `DMC-EWTW-A-21-23-01-00A-300A-A` | 300 | Scheduled maintenance |
| `DMC-EWTW-021-230-010-520` | `DMC-EWTW-A-21-23-01-00A-520A-A` | 520 | Remove procedures |
| `DMC-EWTW-021-230-010-720` | `DMC-EWTW-A-21-23-01-00A-720A-A` | 720 | Install procedures |

## References

1. S1000D — *International Specification for Technical Publications*, Issue 4.2. https://s1000d.org/
2. Convention `AMPEL360-AMM-INFOCODE-CM-001`.
