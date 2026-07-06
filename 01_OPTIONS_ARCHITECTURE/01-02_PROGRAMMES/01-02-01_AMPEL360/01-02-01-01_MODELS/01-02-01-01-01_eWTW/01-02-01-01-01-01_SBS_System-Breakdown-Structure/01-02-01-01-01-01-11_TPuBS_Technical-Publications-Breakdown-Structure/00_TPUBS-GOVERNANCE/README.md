---
node: 00_TPUBS-GOVERNANCE
model: eWTW
mic: EWTW
side: PUB
csdb: S1000D Issue 4.2
owner: Q-DATAGOV
status: baseline
---

# 00_TPUBS-GOVERNANCE — CSDB Governance Layer

Cross-cutting rules that govern the whole eWTW TPuBS. Nothing in this folder
belongs to a single node or a single publication: these are the constraints
every DMRL, Data Module and Publication Module must satisfy.

| Folder | Content |
|---|---|
| `BREX/` | Business Rules Exchange Data Modules (project business rules). |
| `DMRL-CONTROL/` | DMRL authoring rules: requirementId grammar, status vocabulary, roll-up generation rules. |
| `SCHEMAS/` | Local schema references and validation profiles (S1000D Issue 4.2). |
| `APPLICABILITY/` | Product attribute and condition cross-reference (ACT/CCT/PCT) governance. |
| `PUBLICATION-POLICY/` | Rules for how Publication Modules may select, order and render Data Modules. |

## Governing principle

> G-ATLAS determines where information semantically belongs; the DMRL
> determines which Data Modules must exist; the Publication Modules determine
> in which publications, and in which order, those Data Modules are presented.
