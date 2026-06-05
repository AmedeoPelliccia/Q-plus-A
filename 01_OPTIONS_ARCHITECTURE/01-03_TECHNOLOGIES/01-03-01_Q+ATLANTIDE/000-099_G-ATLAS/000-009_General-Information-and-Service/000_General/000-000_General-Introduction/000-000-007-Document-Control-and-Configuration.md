---
document_id: G-ATLAS-000-000-007
title: "000-000-007 — Document Control and Configuration"
node: 000-000
item: "007"
ata_ref: 00-00-07
owner: Q-DATAGOV
agnostic: true
status: baseline
---

# 000-000-007 — Document Control and Configuration

> **Node:** `000-000` · **Item:** `007` · **ATA ref:** 00-00-07
> **Owner:** Q-DATAGOV · **Status:** baseline · **Agnostic:** yes

---

## 1. Purpose

This item defines how G-ATLAS content (nodes, items, and indices) is version-controlled, change-controlled, and configuration-managed under the **SSOT+PUB** doctrine.

---

## 2. SSOT+PUB Doctrine

| Layer | Name | Who controls it | What it contains |
|---|---|---|---|
| **SSOT** | Single Source of Truth | Q-DATAGOV | All G-ATLAS standard nodes and items (this repository) |
| **PUB** | Programme publication | Programme (e.g. eWTW, hBWB) | S1000D data modules derived from SSOT via impact study |

Only Q-DATAGOV may modify SSOT content. A programme may never modify an SSOT file; it creates its own PUB (CSDB) entries.

---

## 3. Versioning

### 3.1 Version Format

```text
<major>.<minor>.<patch>
```

| Component | Triggers a change |
|---|---|
| `major` | Structural change (new node, retired node, numbering change) |
| `minor` | Content addition or substantive revision to an existing item |
| `patch` | Editorial correction, typo fix, clarification without substantive change |

### 3.2 Status Values

| Status | Meaning |
|---|---|
| `draft` | Work in progress; not under formal change control |
| `baseline` | Formally approved; changes require a Change Request (CR) |
| `superseded` | Replaced by a newer baseline; retained for traceability |
| `withdrawn` | Removed from the standard; reason recorded in change log |

---

## 4. Change Control

### 4.1 Change Request (CR)

All changes to SSOT content at status `baseline` require a **Change Request**:

1. Originator raises CR, citing the affected node/item and the reason.
2. Q-DATAGOV reviews for scope, agnosticism compliance, and governance impact.
3. If approved, Q-DATAGOV applies the change, updates the version, and records the CR reference in the item's change log.
4. The updated item is re-baselined with a new SHA-256 anchor (see §5).

### 4.2 Fast-Track Corrections

Patch-level corrections (editorial, typos) may be applied directly by Q-DATAGOV without a full CR cycle, provided no normative content changes. A note is added to the change log.

### 4.3 No Programme Override

Programmes may not apply their own changes to SSOT items. If a programme finds a defect or gap in the SSOT, it raises a CR. Until the CR is resolved, the programme documents the gap in its impact study.

---

## 5. Configuration and Evidence Anchor

Each item at status `baseline` is stamped with a **SHA-256 hash** of its content at the time of baseline. This hash is the **integrity evidence anchor** under the IEF (Integrity Evidence Framework).

```yaml
ief_anchor:
  sha256: <to-be-stamped-at-baseline>
  stamped_at: <ISO-8601 timestamp>
  stamped_by: Q-DATAGOV
```

The anchor is recorded in the item's front matter and in the master evidence index (`000-000-008`).

---

## 6. Lifecycle Gate Control

Nodes in master range `000–009` are governed across **LC01–LC14**. The following nodes are **gate-critical** (their baseline status is verified at named lifecycle gates):

| Node | Gate-critical at |
|---|---|
| `004-xxx` (Airworthiness Limitations) | LC05, LC07, LC09, LC11 |
| `005-xxx` (Time Limits) | LC05, LC07, LC09, LC11 |
| `000-000` (this node) | LC01 (first formal baseline) |

---

## 7. Change Log (this item)

| Version | Date | Change | CR ref |
|---|---|---|---|
| 0.1.0 | 2026-06-05 | Initial baseline | — |

---

```yaml
Last.MarkedDown:
  node: 000-000
  item: "007"
  ata_ref: 00-00-07
  file: 000-000-007-Document-Control-and-Configuration.md
  owner: Q-DATAGOV
  status: baseline
  ief_anchor:
    sha256: <to-be-stamped-at-baseline>
    stamped_at: <ISO-8601 timestamp>
    stamped_by: Q-DATAGOV
  .YieldedAlgorithmicMachineLearning: true
```
