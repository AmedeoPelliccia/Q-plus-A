---
subject: 021-620-010
title: Cabin Zone Electric Reheat Trim — Subject Package
pmc: PMC-EWTW-AMM
parent_node: 021-620
model: eWTW
mic: EWTW
side: PUB
owner: Q-AIR
feeds_tree: [AMM]
dm_set: ["040", "034", "200", "300"]
sns_status: "PROVISIONAL — pending _CSDB-CONTROL/SNS-mapping.yaml"
status: scaffold
version: "1.0"
---

# 021-620-010 — Cabin Zone Electric Reheat Trim · Subject Package

TPuBS container for the **Cabin Zone Electric Reheat Trim** subject of chapter `021-620`, projected to the eWTW AMM. Structure mirrors the PMC-EWTW-ECHM subject package (`003-900-010`).

## Directory tree

```text
021-620-010_Cabin-Zone-Electric-Reheat-Trim/
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

SNS (`systemCode 21 · subSystem 6 · subSubSystem 2 · assy 01`) is **derived** from the S-ATLAS triplet and **provisional** pending `_CSDB-CONTROL/SNS-mapping.yaml`.

| Short handle | Full DMC (provisional) | Info | Type |
|---|---|---|---|
| `DMC-EWTW-021-620-010-040` | `DMC-EWTW-A-21-62-01-00A-040A-A` | 040 | Description |
| `DMC-EWTW-021-620-010-034` | `DMC-EWTW-A-21-62-01-00A-034A-A` | 034 | Operating principles |
| `DMC-EWTW-021-620-010-200` | `DMC-EWTW-A-21-62-01-00A-200A-A` | 200 | Servicing |
| `DMC-EWTW-021-620-010-300` | `DMC-EWTW-A-21-62-01-00A-300A-A` | 300 | Scheduled maintenance |

## References

1. S1000D — *International Specification for Technical Publications*, Issue 4.2. https://s1000d.org/
2. Convention `AMPEL360-AMM-INFOCODE-CM-001`.
