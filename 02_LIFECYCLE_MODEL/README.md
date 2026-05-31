---
document_id: QPLUS-A-02-LIFECYCLE-MODEL-README
title: "Q-plus-A — Lifecycle Model"
repository: Q-plus-A
path: 02_LIFECYCLE_MODEL/README.md
register: Q-plus
architecture: OPTIONS_ARCHITECTURE
status: draft
version: "0.1.0"
revision: A
classification: open-governance-baseline
owner: AEROSPACEMODEL / Q-plus
lifecycle_model: "LC-letter CAD/product maturity model"
language: en
---

# 02_LIFECYCLE_MODEL — Lifecycle Model

## 1. Purpose

`02_LIFECYCLE_MODEL/` defines the controlled lifecycle maturity model used by Q-plus-A artefacts, products, CAD models, PLM records, publication modules, and evidence records.

This lifecycle model provides a common governance language for moving an artefact from early conceptual definition to preliminary design, detailed design, qualification, certification, operations, MRO, and final nature-sustainment.

---

## 2. Lifecycle Model Type

Q-plus-A uses an **LC-letter CAD/product maturity model** for product and CAD artefacts.

```text
LC-letter stage      = maturity phase
REV-letter-number    = iteration inside the maturity phase
*_RELEASED           = formal release gate closing that maturity phase
````

Example:

```text
LC-A Conceptual Design
├── REV-A0
├── REV-A1
├── REV-A2
└── REV-A_RELEASED

LC-B Preliminary Design
├── REV-B0
├── REV-B1
├── REV-B2
└── REV-B_RELEASED
```

The release gate of one lifecycle stage authorizes promotion to the next lifecycle stage.

---

## 3. Controlled LC-letter Stages

| LC     | Stage                                                 | Scope                                                                                          | Release Gate     |
| ------ | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------- |
| `LC-A` | Conceptual Design                                     | First concept, first geometry, early proportions, early feasibility placeholder.               | `REV-A_RELEASED` |
| `LC-B` | Preliminary Design                                    | Main geometry, architecture sizing, preliminary interfaces, major configuration decisions.     | `REV-B_RELEASED` |
| `LC-C` | Detailed Design                                       | Detailed CAD/product definition, material stack, BOM/CAD consistency, drawing preparation.     | `REV-C_RELEASED` |
| `LC-D` | Analysis / Verification Design                        | Analysis-ready geometry, verification setup, simulation models, test logic.                    | `REV-D_RELEASED` |
| `LC-E` | Release Candidate / Engineering Definition            | Engineering release candidate before physical mock-up, qualification, or certification use.    | `REV-E_RELEASED` |
| `LC-F` | PMU/PMA — Physical Mock-Up Article and  Wind Tunnel | Physical mock-up, installation mock-up, aerodynamic mock-up, wind-test preparation.            | `REV-F_RELEASED` |
| `LC-G` | Qualification                                         | Qualification test article, qualification evidence, test reports, compliance-relevant records. | `REV-G_RELEASED` |
| `LC-H` | Hardware & Softwareization                            | Hardware embodiment, digital configuration, software/data integration, product-data binding.   | `REV-H_RELEASED` |
| `LC-I` | Installation and Interface                            | Installation closure, interface maturity, aircraft or system integration readiness.            | `REV-I_RELEASED` |
| `LC-J` | Certification                                         | Certification configuration, compliance evidence, authority-facing artefacts.                  | `REV-J_RELEASED` |
| `LC-K` | First Flight and Industrialization                    | First-flight configuration, manufacturing readiness, industrialization transition.             | `REV-K_RELEASED` |
| `LC-L` | Operations                                            | In-service operational configuration, operator feedback, operational evidence.                 | `REV-L_RELEASED` |
| `LC-M` | MRO and Continuous Airworthiness                      | Maintenance, repair, overhaul, service bulletins, continued-airworthiness records.             | `REV-M_RELEASED` |
| `LC-N` | Nature Sustainment                                    | Circular economy, retirement, reuse, disposal, recycling, environmental sustainment.           | `REV-N_RELEASED` |

---

## 4. Revision Naming Pattern

Generic revision pattern:

```text
REV-<LC_LETTER><SEQUENCE>
```

Examples:

```text
REV-A0
REV-A1
REV-A2
REV-A_RELEASED

REV-B0
REV-B1
REV-B_RELEASED
```

For item-specific usage, the item name may be prefixed:

```text
RADOME-REV-A0
RADOME-REV-A1
RADOME-REV-A_RELEASED
```

---

## 5. Release Gate Rule

```yaml
release_gate_rule:
  id: QPLUS-LC-RELEASE-001
  rule: >
    A lifecycle stage is not closed until its corresponding *_RELEASED
    revision is approved. The next lifecycle stage shall not start as a
    controlled baseline while blocking findings remain open in the previous
    lifecycle stage.
```

---

## 6. Blocking Finding Rule

Any CAD/product revision may record findings.

Finding classes:

| Finding Class | Meaning                            | Gate Impact                                            |
| ------------- | ---------------------------------- | ------------------------------------------------------ |
| `F-INFO`      | Informational note.                | Does not block release.                                |
| `F-WARN`      | Warning or limitation.             | May block release depending on severity.               |
| `F-BLOCK`     | Blocking finding.                  | Blocks `*_RELEASED`.                                   |
| `F-DEFER`     | Deferred to later lifecycle stage. | Does not block current release if explicitly accepted. |

Controlled rule:

```yaml
finding_rule:
  id: QPLUS-LC-FINDING-001
  rule: >
    No revision shall be promoted to *_RELEASED while F-BLOCK findings remain
    open. Deferred findings shall identify the lifecycle stage in which they
    become mandatory.
```

---

## 7. Artefact Folder Pattern

Recommended lifecycle folder pattern:

```text
cad/
└── freecad/
    ├── LC-A_Concept-Design/
    │   ├── REV-A0/
    │   ├── REV-A1/
    │   ├── REV-A2/
    │   └── REV-A_RELEASED/
    │
    ├── LC-B_Preliminary-Design/
    │   ├── REV-B0/
    │   ├── REV-B1/
    │   └── REV-B_RELEASED/
    │
    ├── LC-C_Detailed-Design/
    ├── LC-D_Analysis-Verification-Design/
    ├── LC-E_Release-Candidate-Engineering-Definition/
    ├── LC-F_PMU-Physical-Mock-Up-and-Wind-Gallery/
    ├── LC-G_Qualification/
    ├── LC-H_Hardware-and-Softwareization/
    ├── LC-I_Installation-and-Interface/
    ├── LC-J_Certification/
    ├── LC-K_First-Flight-and-Industrialization/
    ├── LC-L_Operations/
    ├── LC-M_MRO-and-Continuous-Airworthiness/
    └── LC-N_Nature-Sustainment/
```

---

## 8. Minimum Lifecycle Metadata

Every controlled CAD/product lifecycle record shall include:

```yaml
lifecycle_record:
  lifecycle_model: "LC-letter CAD/product maturity model"
  lc_stage: "LC-A"
  lc_stage_name: "Conceptual Design"
  current_revision: "REV-A0"
  revision_status: "draft"
  next_release_gate: "REV-A_RELEASED"
  blocking_findings: []
  deferred_findings: []
```

For item-specific records:

```yaml
item_lifecycle_record:
  pbs_id: "<PBS-ID>"
  part_number: "<PN>"
  lifecycle_model: "LC-letter CAD/product maturity model"
  lc_stage: "LC-A"
  current_revision: "<ITEM>-REV-A0"
  next_release_gate: "<ITEM>-REV-A_RELEASED"
```

---

## 9. Traceability Chain

The lifecycle model shall preserve the following chain:

```text
PBS → PNR → PN → BOM → CAD → STEP → Drawing → Evidence → Lifecycle Gate
```

Each lifecycle revision shall reference:

| Layer            | Required                          |
| ---------------- | --------------------------------- |
| PBS item         | Yes                               |
| PNR              | Yes, for physical items           |
| Part Number      | Yes, for physical items           |
| BOM              | Yes, when composition is defined  |
| CAD native file  | Yes, when CAD exists              |
| STEP/export file | Required when export is produced  |
| Drawing          | Required when drawing is produced |
| Evidence record  | Yes                               |
| Release gate     | Yes                               |

---

## 10. Relationship to OPTIONS Architecture

This lifecycle model supports the `OPTIONS_ARCHITECTURE` repository structure.

```text
OPTIONS =
O  Organizations
P  Programmes
T  Technologies
I  Infrastructures
O  Operations
N  Neural Networks
S  Standards
```

Lifecycle records may appear under product-specific folders, especially under:

```text
01_OPTIONS_ARCHITECTURE/
└── 01-02_PROGRAMMES/
    └── ...
```

The root lifecycle model remains the controlling reference.

---

## 11. Example — AMPEL360 eWTW Radome

Example item:

```text
eWTW-PBS-10-10-10-10-10 — Radome
```

Current lifecycle state:

```yaml
radome_lifecycle_example:
  pbs_id: "eWTW-PBS-10-10-10-10-10"
  part_number: "PN-eWTW-5310-0001"
  lc_stage: "LC-A"
  lc_stage_name: "Conceptual Design"
  current_revision: "RADOME-REV-A0"
  revision_status: "draft"
  next_release_gate: "RADOME-REV-A_RELEASED"
  next_revision: "RADOME-REV-A1"
```

Known REV-A0 gate findings:

| Finding | Meaning                                  | Gate Impact                     |
| ------- | ---------------------------------------- | ------------------------------- |
| `F1`    | Absolute scale must be resolved.         | Blocks `RADOME-REV-A_RELEASED`. |
| `F2`    | Solid body only; sandwich wall deferred. | Deferred to LC-C.               |
| `F3`    | Controlled metadata gaps.                | Blocks `RADOME-REV-A_RELEASED`. |

---

## 12. Governance Rules

1. The lifecycle model shall use LC-letter stages from `LC-A` through `LC-N`.
2. Revisions inside a lifecycle stage shall use the corresponding revision letter.
3. A lifecycle stage shall close only through its `*_RELEASED` gate.
4. Blocking findings shall prevent release-gate closure.
5. Deferred findings shall identify the lifecycle stage where they become mandatory.
6. CAD/product lifecycle records shall preserve PBS, PN, CAD, evidence, and release-gate traceability.
7. Product-specific lifecycle folders may extend this model but shall not contradict it.
8. The root `02_LIFECYCLE_MODEL/README.md` is the controlling lifecycle reference for Q-plus-A unless superseded by a higher governance document.

---

## 13. Controlled Closure Statement

`02_LIFECYCLE_MODEL/README.md` defines the root lifecycle maturity model for Q-plus-A CAD/product artefacts.

The model controls the progression from conceptual design through preliminary design, detailed design, qualification, certification, first flight, operations, MRO, and nature sustainment.

It shall be referenced by product-specific lifecycle records such as:

```text
cad/freecad/LC-A_Concept-Design/REV-A0/Radome-CAD-Record.md
```

```
```

