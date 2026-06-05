---
document_id: G-ATLAS-000-000-006
title: "000-000-006 — Standards Alignment: ATA 100 / iSpec 2200 / S1000D"
node: 000-000
item: "006"
ata_ref: 00-00-06
owner: Q-DATAGOV
agnostic: true
status: baseline
---

# 000-000-006 — Standards Alignment: ATA 100 / iSpec 2200 / S1000D

> **Node:** `000-000` · **Item:** `006` · **ATA ref:** 00-00-06
> **Owner:** Q-DATAGOV · **Status:** baseline · **Agnostic:** yes

---

## 1. Purpose of This Item

This item documents how G-ATLAS aligns to, extends, and differs from the three principal technical publication and architecture standards used in aerospace: **ATA 100**, **iSpec 2200**, and **S1000D**.

---

## 2. ATA 100 Alignment

### 2.1 Chapter Mirror

G-ATLAS mirrors ATA 100 chapter numbering across its first nine bands (`000–099` through `800–899`). Each G-ATLAS chapter `00X` corresponds directly to ATA chapter `0X`.

| G-ATLAS chapter | ATA chapter | Title |
|---|---|---|
| `000` | ATA 00 | General / Introduction |
| `001` | ATA 01 | Maintenance Policy |
| `002` | ATA 02 | Operations |
| `004` | ATA 04 | Airworthiness Limitations |
| … | … | … |

### 2.2 Section Mirror

G-ATLAS section numbers are ATA section numbers scaled by ×10 (three-digit suffix). This preserves full bijective mapping while allowing item codes beyond 99.

| ATA section | G-ATLAS node |
|---|---|
| ATA 00-00 | `000-000` |
| ATA 05-10 | `005-100` |
| ATA 05-50 | `005-500` |

### 2.3 What G-ATLAS Adds

ATA 100 does not define architecture content for:
- Novel energy carriers (batteries, cryogenic hydrogen, ammonia, fuel cells)
- Digital Product Passports
- Lifecycle-phase sustainability accounting (LC-letter stages LC-A through LC-N)
- Post-retirement nature-sustainment

G-ATLAS adds **agnostic delta nodes** (`00X-900`) for each of these. These nodes are formally labelled `[G]` and have no ATA equivalent.

### 2.4 Chapters Reserved by ATA for Operators

ATA chapters 00–03 are reserved by ATA 100 for operator use; ATA does not standardise their sections. G-ATLAS defines sections within these chapters as **G-ATLAS-defined** (not ATA standard). They are marked `†` in the node register.

---

## 3. iSpec 2200 Alignment

iSpec 2200 (ATA) extends ATA 100 with structured authoring rules, module types, and publication specifications for S1000D-compatible content.

G-ATLAS aligns to iSpec 2200 by:

1. Using the ATA/iSpec 2200 chapter–section–subject numbering as the basis for node and item identifiers.
2. Structuring items as **data-module-equivalent content units**, each with a defined purpose, owner, and evidence anchor.
3. Ensuring every item has a natural mapping to an S1000D System/Sub-system/Subject (SNS) code.

G-ATLAS does **not** prescribe iSpec 2200 mark-up tags within markdown files; mark-up is applied at PUB (CSDB) stage by the programme toolchain.

---

## 4. S1000D Alignment

### 4.1 Data Module Codes

Each G-ATLAS item maps to a Data Module Code (DMC) in the programme CSDB. The canonical short form is:

```text
DMC-<PROGRAMME>-<node>-<item>
```

Examples:
- `DMC-EWTW-000-000-001` — eWTW CSDB module for item `001` of node `000-000`
- `DMC-HBWB-004-900-002` — hBWB CSDB module for item `002` of node `004-900`

Full S1000D Issue 4.2 DMC format adds Model Identification Code (MIC), System/Sub-system code, Disassembly Code, Information Code, and Applicability code; these are determined by the programme at PUB stage.

### 4.2 Issue Alignment

G-ATLAS is aligned to **S1000D Issue 4.2** as the baseline. Later issues may be adopted by individual programmes without requiring amendment to the SSOT, provided the SNS mapping remains valid.

### 4.3 CSDB and SSOT+PUB

```text
G-ATLAS SSOT (this repository)
    └── impact study (programme)
        └── Programme CSDB / PUB (S1000D data modules)
```

The SSOT is not itself an S1000D CSDB. It is the upstream source that programmes transform into S1000D data modules. This separation is the **SSOT+PUB doctrine**.

---

## 5. Standards Hierarchy

```text
ICAO Annex 8 / CS-25 / Special Conditions   (regulatory, supreme for airworthiness)
    └── ATA 100 / iSpec 2200                 (documentation structure standard)
        └── G-ATLAS (SSOT)                   (agnostic architecture standard — this data set)
            └── Programme CSDB (PUB)         (programme-specific instantiation, S1000D)
```

G-ATLAS sits between iSpec 2200 and the programme CSDB. It does not override regulatory standards; it provides the architectural framework within which programme documentation is organised.

---

```yaml
Last.MarkedDown:
  node: 000-000
  item: "006"
  ata_ref: 00-00-06
  file: 000-000-006-Standards-Alignment-ATA-iSpec-2200.md
  owner: Q-DATAGOV
  status: baseline
  .YieldedAlgorithmicMachineLearning: true
```
