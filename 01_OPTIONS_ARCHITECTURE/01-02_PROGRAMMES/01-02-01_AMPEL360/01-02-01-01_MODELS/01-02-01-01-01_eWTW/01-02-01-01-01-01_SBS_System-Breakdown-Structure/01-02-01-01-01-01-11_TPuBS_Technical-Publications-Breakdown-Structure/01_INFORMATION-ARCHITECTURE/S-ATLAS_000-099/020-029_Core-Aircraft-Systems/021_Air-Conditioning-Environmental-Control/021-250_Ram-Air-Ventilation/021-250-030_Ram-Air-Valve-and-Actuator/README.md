---
subject: 021-250-030
title: Ram Air Valve and Actuator — Subject Package
pmc: PMC-EWTW-AMM
parent_node: 021-250
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

# 021-250-030 — Ram Air Valve and Actuator · Subject Package

TPuBS container for the **Ram Air Valve and Actuator** subject of chapter `021-250`, projected to the eWTW AMM. Structure mirrors the PMC-EWTW-ECHM subject package (`003-900-010`).

## Directory tree

```text
021-250-030_Ram-Air-Valve-and-Actuator/
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

SNS (`systemCode 21 · subSystem 2 · subSubSystem 5 · assy 03`) is **derived** from the S-ATLAS triplet and **provisional** pending `_CSDB-CONTROL/SNS-mapping.yaml`.

| Short handle | Full DMC (provisional) | Info | Type |
|---|---|---|---|
| `DMC-EWTW-021-250-030-040` | `DMC-EWTW-A-21-25-03-00A-040A-A` | 040 | Description |
| `DMC-EWTW-021-250-030-200` | `DMC-EWTW-A-21-25-03-00A-200A-A` | 200 | Servicing |
| `DMC-EWTW-021-250-030-300` | `DMC-EWTW-A-21-25-03-00A-300A-A` | 300 | Scheduled maintenance |
| `DMC-EWTW-021-250-030-520` | `DMC-EWTW-A-21-25-03-00A-520A-A` | 520 | Remove procedures |
| `DMC-EWTW-021-250-030-720` | `DMC-EWTW-A-21-25-03-00A-720A-A` | 720 | Install procedures |

## References

1. S1000D — *International Specification for Technical Publications*, Issue 4.2. https://s1000d.org/
2. Convention `AMPEL360-AMM-INFOCODE-CM-001`.
