---
document_id: G-ATLAS-000-000-001
title: "000-000-001 — Scope and Definitions"
node: 000-000
item: "001"
ata_ref: 00-00-01
owner: Q-DATAGOV
agnostic: true
status: baseline
---

# 000-000-001 — Scope and Definitions

> **Node:** `000-000` · **Item:** `001` · **ATA ref:** 00-00-01
> **Owner:** Q-DATAGOV · **Status:** baseline · **Agnostic:** yes

---

## 1. Scope

### 1.1 What Is Covered

This item defines the scope of **master range `000–009` General Information and Service** and the controlled vocabulary used throughout that range and, by reference, throughout all of G-ATLAS band `000–099`.

The scope includes:

- The architectural standard layer (SSOT): G-ATLAS nodes, items, and their governance.
- The programme publication layer (PUB): CSDB instances derived from the SSOT via impact studies.
- The lifecycle governance model (Q+ATLANTIDE LC-letter stages, LC-A through LC-N) as it applies to nodes in this master range.
- The traceability linkage from items to requirements, evidence, and DMCs.

### 1.2 What Is Not Covered

- Programme-specific engineering requirements (these reside in programme CSDB instances).
- System-level design details (these reside in the relevant system bands, `010–099` and above).
- Regulatory compliance plans (these reside in the programme certification folder `01-02-XX-02_CERTIFICATION/`).

---

## 2. Definitions

### 2.1 Structural Terms

| Term | Definition |
|---|---|
| **Band** | The top-level numbering block of G-ATLAS. Band `000–099` is G-ATLAS. |
| **Master range** | A ten-chapter block within a band (e.g. `000–009`). Equivalent to a group of ATA chapters. |
| **Chapter** | A physical folder within a master range, numbering one ATA chapter (e.g. `000_General` ⇄ ATA 00). |
| **Node (code section)** | The primary addressable unit of G-ATLAS content; maps to an ATA chapter-section (e.g. `000-000` ⇄ ATA 00-00). |
| **Item (subject)** | A single markdown file inside a node; maps to an ATA subject (e.g. item `001` ⇄ ATA 00-00-01). |
| **Delta node** | A node with suffix `-900`, covering topics with no ATA equivalent (energy-carrier specifics, DPP, sustainability). |

### 2.2 Publication and Governance Terms

| Term | Definition |
|---|---|
| **SSOT** | Single Source of Truth. The authoritative G-ATLAS repository. Programmes may not modify it; they only publish derived instances. |
| **PUB** | Programme publication. A CSDB instance derived from SSOT by impact study, containing programme-applicable DMCs. |
| **DMC** | Data Module Code. An S1000D identifier assigned to a PUB instance of a G-ATLAS item. |
| **CSDB** | Common Source DataBase. The S1000D-compliant storage for programme data modules. |
| **Impact study** | The documented process by which a programme determines which G-ATLAS nodes/items apply, and maps them to DMCs. |
| **LC-letter stage** | A product/CAD maturity phase in the Q+ATLANTIDE lifecycle model (LC-A Conceptual Design … LC-N Nature Sustainment), each closed by a `REV-<LC>_RELEASED` gate. |

### 2.3 Doctrine Terms

| Term | Definition |
|---|---|
| **SSOT+PUB** | The two-layer publication architecture: SSOT (this standard) and PUB (programme CSDB). |
| **Agnostic** | A content attribute meaning the item contains no programme- or product-specific assumption. |
| **Baseline** | A governance status meaning the item is formally approved and under change control. |

### 2.4 Evidence Terms

| Term | Definition |
|---|---|
| **IEF** | Integrity Evidence Framework. The evidence anchoring scheme used across Q+ATLANTIDE. |
| **SHA-256 anchor** | A cryptographic hash stamped at baseline to make an item tamper-evident. |
| **Traceability record** | A structured link from an item to its parent requirement, applicable standard, owner, and DMC. |

---

```yaml
Last.MarkedDown:
  node: 000-000
  item: "001"
  ata_ref: 00-00-01
  file: 000-000-001-Scope-and-Definitions.md
  owner: Q-DATAGOV
  status: baseline
  .YieldedAlgorithmicMachineLearning: true
```
