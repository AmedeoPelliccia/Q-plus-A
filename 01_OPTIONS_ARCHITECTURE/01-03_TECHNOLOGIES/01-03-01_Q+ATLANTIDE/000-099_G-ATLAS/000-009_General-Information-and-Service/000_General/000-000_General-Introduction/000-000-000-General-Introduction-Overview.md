---
document_id: G-ATLAS-000-000-000
title: "000-000-000 — General Introduction: Overview"
node: 000-000
item: "000"
ata_ref: 00-00-00
owner: Q-DATAGOV
agnostic: true
status: baseline
---

# 000-000-000 — General Introduction: Overview

> **Node:** `000-000` · **Item:** `000` · **ATA ref:** 00-00-00
> **Owner:** Q-DATAGOV · **Status:** baseline · **Agnostic:** yes

This item is the map of node `000-000`. It orients a new reader to the purpose and layout of the entire G-ATLAS data set and to this node's role within it.

---

## 1. What G-ATLAS Is

**G-ATLAS** (Green Aircraft Top-Level Architecture Schema) is a programme- and product-**agnostic** architectural standard for aviation systems. It defines functions, limits, zones, and intervals in neutral terms — terms that hold true regardless of whether the aircraft uses battery-electric, hydrogen, ammonia, SAF, hybrid, or any other energy carrier, and regardless of airframe geometry (tube-and-wing, blended-wing-body, etc.).

G-ATLAS mirrors the structure of **ATA 100 / iSpec 2200** so that every chapter, section, and subject has a direct analogue in the existing aerospace documentation ecosystem. Where ATA has no equivalent — primarily for novel energy carriers and sustainability accounting — G-ATLAS adds **agnostic delta nodes** (suffix `-900`).

---

## 2. Why This Node Exists

Node `000-000` (ATA 00-00) is the **entry point**. It exists so that any stakeholder — engineer, certifier, supplier, auditor, or programme manager — can answer the following questions before reading any other item in the data set:

| Question | Item that answers it |
|---|---|
| What is G-ATLAS and what does it cover? | `000` (this item) |
| What terms and scope apply? | `001` |
| Why does this standard exist? | `002` |
| How is it kept neutral across programmes? | `003` |
| How do I navigate and use it? | `004` |
| How is it numbered? | `005` |
| How does it relate to ATA / iSpec 2200? | `006` |
| How is it version-controlled? | `007` |
| How does each item trace to evidence? | `008` |

---

## 3. Scope of This Data Set

G-ATLAS covers **band `000–099`** — the top-level architecture schema — and is organised into ten **master ranges** (`000–009` through `090–099`). This node resides in master range `000–009` (General Information and Service), chapter `000` (General), code section `000-000`.

The data set is:

- **A single-source-of-truth (SSOT)** standard. Programmes publish it into their own CSDBs (PUB) via impact studies; they do not modify the SSOT.
- **Lifecycle-governed**: artefact maturity follows the Q+ATLANTIDE LC-letter stages (LC-A Conceptual Design through LC-N Nature Sustainment).
- **Certification-ready**: every item is structured to support traceability from architecture to requirement, evidence, and Data Module Code (DMC).

---

## 4. Structure of This Node

```text
000-000_General-Introduction/
├── README.md                                                    ← node index
├── 000-000-000-General-Introduction-Overview.md                 ← this file
├── 000-000-001-Scope-and-Definitions.md
├── 000-000-002-Purpose-and-Mission.md
├── 000-000-003-Programme-and-Product-Agnosticism.md
├── 000-000-004-How-to-Use-This-Architecture-and-Data-Set.md
├── 000-000-005-Numbering-and-Structure-Orientation.md
├── 000-000-006-Standards-Alignment-ATA-iSpec-2200.md
├── 000-000-007-Document-Control-and-Configuration.md
└── 000-000-008-Traceability-and-Evidence-Index.md
```

---

## 5. Reading Order

For a first-time reader: `000` → `001` → `002` → `003` → `005` → `006` → `004` → `007` → `008`.

For a programme integrator binding G-ATLAS to a specific product: `003` → `006` → `007` → `008`.

For an auditor or certifier: `007` → `008` → `006`.

---

```yaml
Last.MarkedDown:
  node: 000-000
  item: "000"
  ata_ref: 00-00-00
  file: 000-000-000-General-Introduction-Overview.md
  owner: Q-DATAGOV
  status: baseline
  .YieldedAlgorithmicMachineLearning: true
```
