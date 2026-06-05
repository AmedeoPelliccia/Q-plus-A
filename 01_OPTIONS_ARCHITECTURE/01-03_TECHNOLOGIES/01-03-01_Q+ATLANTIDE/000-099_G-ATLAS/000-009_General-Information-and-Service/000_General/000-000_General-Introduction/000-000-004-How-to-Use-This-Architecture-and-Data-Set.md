---
document_id: G-ATLAS-000-000-004
title: "000-000-004 — How to Use This Architecture and Data Set"
node: 000-000
item: "004"
ata_ref: 00-00-04
owner: Q-DATAGOV
agnostic: true
status: baseline
---

# 000-000-004 — How to Use This Architecture and Data Set

> **Node:** `000-000` · **Item:** `004` · **ATA ref:** 00-00-04
> **Owner:** Q-DATAGOV · **Status:** baseline · **Agnostic:** yes

---

## 1. Who This Is For

| Reader | Primary use |
|---|---|
| **New contributor / engineer** | Understand the standard before reading any system band |
| **Programme integrator** | Identify applicable nodes, run an impact study, build the CSDB |
| **Certifier / authority** | Navigate to a specific node, verify traceability, check evidence anchor |
| **Auditor** | Check governance status, owner, change history, SHA-256 anchor |
| **System architect** | Find the agnostic function slot for a new technology |

---

## 2. Repository Navigation

### 2.1 Root Path to G-ATLAS

```text
01_OPTIONS_ARCHITECTURE/
└── 01-03_TECHNOLOGIES/
    └── 01-03-01_Q+ATLANTIDE/
        └── 000-099_G-ATLAS/              ← band index
            └── 000-009_General-Information-and-Service/   ← master range index
                └── 000_General/          ← chapter folder
                    └── 000-000_General-Introduction/      ← this node
```

### 2.2 Key Index Files

| File | Purpose |
|---|---|
| `000-099_G-ATLAS/README.md` (band) | Band overview, governance framework, all master ranges |
| `000-009_.../README.md` (master range) | Node register, numbering rules, green-delta table |
| `000_General/README.md` (chapter) | Chapter-level navigation |
| `000-000_.../README.md` (this node) | Node item set, governance, navigation |

Start at the **master-range README** to orient yourself to a chapter, then navigate to the **node README** for the item list.

---

## 3. Tags and Labels

Items carry the following navigation tags in their front matter:

| Tag | Meaning |
|---|---|
| `agnostic: true` | Item contains no programme- or product-specific assumption |
| `status: baseline` | Item is formally approved and under change control |
| `[G]` in node title | Agnostic green-architecture delta node (suffix `-900`) |
| `owner: Q-DATAGOV` | The Q-Division responsible for the item |

---

## 4. Reading Order

### 4.1 First-Time Reader (orientation sequence)

```text
000-000-000  →  000-000-001  →  000-000-002  →  000-000-003
          →  000-000-005  →  000-000-006  →  000-000-004  →  000-000-007  →  000-000-008
```

### 4.2 Programme Integrator

1. Read `000-000-003` (agnosticism principle).
2. Read `000-000-006` (ATA / iSpec 2200 / S1000D alignment).
3. Read `000-000-005` (numbering, to understand node IDs).
4. Run impact study against the master-range node register (`000-009/README.md §4`).
5. Map applicable nodes to programme DMCs.
6. Read `000-000-007` (change control) before creating CSDB entries.
7. Read `000-000-008` (traceability) to set up evidence links.

### 4.3 Auditor / Certifier

1. Read `000-000-007` (change control, configuration status).
2. Read `000-000-008` (traceability and evidence index).
3. Navigate directly to the node in question via the node register.
4. Verify SHA-256 anchor at baseline.

---

## 5. Conventions Used Throughout the Data Set

| Element | Convention | Example |
|---|---|---|
| Node identifier | `00X-Y00` | `000-000` |
| Item file | `<node>-<item>-<Title>.md` | `000-000-001-Scope-and-Definitions.md` |
| Delta node | suffix `-900`, tagged `[G]` | `000-900` |
| ATA mirror | `00X-Y00 ⇄ ATA 0X-Y0` | `000-000 ⇄ ATA 00-00` |
| Section scaling | ATA `Y0` → G-ATLAS `Y00` (×10) | `05-50 → 005-500` |
| Retired term | ~~code range~~ → **master range** | — |

---

```yaml
Last.MarkedDown:
  node: 000-000
  item: "004"
  ata_ref: 00-00-04
  file: 000-000-004-How-to-Use-This-Architecture-and-Data-Set.md
  owner: Q-DATAGOV
  status: baseline
  .YieldedAlgorithmicMachineLearning: true
```
