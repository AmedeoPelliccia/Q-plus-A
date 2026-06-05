# 000-000 — General / Introduction

**G-ATLAS Node (Code Section) — Node README**

> **Canonical path**
> `01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_G-ATLAS/000-009_General-Information-and-Service/000_General/000-000_General-Introduction/`
>
> **Band:** `000–099` G-ATLAS (Green Aircraft Top-Level Architecture Schema)
> **Master range:** `000–009` General Information and Service
> **Chapter:** `000` ⇄ ATA 00 (General)
> **Node / code section:** `000-000` ⇄ **ATA 00-00**
> **Owner:** Q-DATAGOV · **Status:** baseline · **Agnostic:** yes (programme/product-neutral)

This node is the **orientation entry point** for the entire G-ATLAS data set. It tells a reader what the schema is, why it exists, how it is numbered, how it relates to ATA 100 / iSpec 2200, how it is controlled, and how every item ties back to evidence — **without assuming any energy carrier or airframe geometry**.

---

## Item Set

| Item | File | ATA ref | Purpose |
|---|---|---|---|
| `000` | `000-000-000-General-Introduction-Overview.md` | 00-00-00 | What this node is; map of the rest |
| `001` | `000-000-001-Scope-and-Definitions.md` | 00-00-01 | Scope of the master range + core terms |
| `002` | `000-000-002-Purpose-and-Mission.md` | 00-00-02 | Why the standard exists |
| `003` | `000-000-003-Programme-and-Product-Agnosticism.md` | 00-00-03 | The neutral-standard principle |
| `004` | `000-000-004-How-to-Use-This-Architecture-and-Data-Set.md` | 00-00-04 | Reading order, navigation, tags |
| `005` | `000-000-005-Numbering-and-Structure-Orientation.md` | 00-00-05 | Master range → chapter → node → item |
| `006` | `000-000-006-Standards-Alignment-ATA-iSpec-2200.md` | 00-00-06 | ATA / iSpec 2200 / S1000D relationship |
| `007` | `000-000-007-Document-Control-and-Configuration.md` | 00-00-07 | Versioning, change control, SSOT+PUB |
| `008` | `000-000-008-Traceability-and-Evidence-Index.md` | 00-00-08 | Item → requirement → evidence → DMC |

---

## Governance

Governed under the **SSOT+PUB** doctrine. Lifecycle stages follow the Q+ATLANTIDE LC-letter model (LC-A through LC-N). This node is **SSOT**; programme CSDBs are **PUB**.

---

## Navigation

| Up | Sideways |
|---|---|
| [`000_General/README.md`](../README.md) | [`000-100_Applicability-and-Effectivity/`](../000-100_Applicability-and-Effectivity/) |
| [`000-009_General-Information-and-Service/README.md`](../../README.md) | [`000-200_Identification-and-Designation/`](../000-200_Identification-and-Designation/) |
| [`000-099_G-ATLAS/`](../../../../../) | [`000-300_Vocabulary-Units-and-Reference-Frames/`](../000-300_Vocabulary-Units-and-Reference-Frames/) |

---

```yaml
Last.MarkedDown:
  node: 000-000
  ata_ref: 00-00
  master_range: 000-009_General-Information-and-Service
  chapter: 000_General
  owner: Q-DATAGOV
  agnostic: true
  items: [000, 001, 002, 003, 004, 005, 006, 007, 008]
  status: baseline
  .YieldedAlgorithmicMachineLearning: true
```
