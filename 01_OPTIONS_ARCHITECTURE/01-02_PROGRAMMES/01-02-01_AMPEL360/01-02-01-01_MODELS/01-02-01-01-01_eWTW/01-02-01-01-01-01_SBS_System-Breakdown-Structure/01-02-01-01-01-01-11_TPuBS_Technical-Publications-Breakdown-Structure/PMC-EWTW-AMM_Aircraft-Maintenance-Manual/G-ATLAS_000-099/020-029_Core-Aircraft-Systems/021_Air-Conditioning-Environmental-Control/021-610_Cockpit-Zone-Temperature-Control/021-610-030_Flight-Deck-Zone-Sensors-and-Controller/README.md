---
subject: 021-610-030
title: Flight Deck Zone Sensors and Controller — Subject Package
pmc: PMC-EWTW-AMM
parent_node: 021-610
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

# 021-610-030 — Flight Deck Zone Sensors and Controller · Subject Package

TPuBS container for the **Flight Deck Zone Sensors and Controller** subject of chapter `021-610`, projected to the eWTW AMM. Structure mirrors the PMC-EWTW-ECHM subject package (`003-900-010`).

## Directory tree

```text
021-610-030_Flight-Deck-Zone-Sensors-and-Controller/
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

SNS (`systemCode 21 · subSystem 6 · subSubSystem 1 · assy 03`) is **derived** from the G-ATLAS triplet and **provisional** pending `_CSDB-CONTROL/SNS-mapping.yaml`.

| Short handle | Full DMC (provisional) | Info | Type |
|---|---|---|---|
| `DMC-EWTW-021-610-030-040` | `DMC-EWTW-A-21-61-03-00A-040A-A` | 040 | Description |
| `DMC-EWTW-021-610-030-034` | `DMC-EWTW-A-21-61-03-00A-034A-A` | 034 | Operating principles |
| `DMC-EWTW-021-610-030-200` | `DMC-EWTW-A-21-61-03-00A-200A-A` | 200 | Servicing |
| `DMC-EWTW-021-610-030-300` | `DMC-EWTW-A-21-61-03-00A-300A-A` | 300 | Scheduled maintenance |

## References

1. S1000D — *International Specification for Technical Publications*, Issue 4.2. https://s1000d.org/
2. Convention `AMPEL360-AMM-INFOCODE-CM-001`.
