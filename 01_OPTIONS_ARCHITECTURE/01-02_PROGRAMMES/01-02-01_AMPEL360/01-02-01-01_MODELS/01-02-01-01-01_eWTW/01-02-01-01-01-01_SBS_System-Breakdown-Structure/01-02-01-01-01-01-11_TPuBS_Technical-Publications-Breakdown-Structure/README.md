---
node: TPuBS (root)
canonical_path: "01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure/"
model: eWTW
mic: EWTW
sbs_member: "-11 (the PUB-side member of the SBS)"
side: PUB
organization: information-centric (single G-ATLAS instance; DMRL per node; PMCs as publication views)
type_authority: Publication-Type-DTD-Register (SSOT)
csdb: S1000D Issue 4.2
owner: Q-DATAGOV
governance: [DEGF-v1.0, LC-A..LC-N, No-AAA, SSOT+PUB]
status: baseline
version: "3.0"
supersedes: "TPuBS README v2.0 (manual-first; G-ATLAS replicated under each PMC)"
---

# eWTW · TPuBS — Technical Publications Breakdown Structure

The **root** of the eWTW model's technical information, and the `-11` (PUB) member of the SBS. The TPuBS is organized **information-centric**: a single canonical G-ATLAS information architecture with a **DMRL per node**, a common Data Module pool, and publications defined as **Publication Module compositions** that reference — never own — the Data Modules.

> **Correction (v3.0).** v2.0 organized the TPuBS manual-first, replicating the G-ATLAS/ATA breakdown under every PMC. That recreated the traditional book paradigm in which information is implicitly "owned" by the manual. Per the CSDB/S1000D principle, a Data Module is a standalone, reusable information unit identified by its DMC and managed in the CSDB; the manual is not the primary container of information but a **controlled composition of the common information pool**.

## Doctrine

> **The eWTW TPuBS is information-centric and organized by G-ATLAS. Every G-ATLAS node declares, through a local DMRL, the InfoCodes and Data Modules it requires. Manuals are not autonomous containers of information but publication views configured through Publication Modules that select, order and publish only the Data Modules applicable to their purpose.**

Equivalently:

> **G-ATLAS determines where information semantically belongs; the DMRL determines which Data Modules must exist; the Publication Modules determine in which publications, and in which order, those Data Modules are presented.**

---

## Index

- [1. The Four Layers](#1-the-four-layers)
- [2. Logical Model](#2-logical-model)
- [3. DMRL per G-ATLAS Node](#3-dmrl-per-g-atlas-node)
- [4. Publication Modules Separated from the G-ATLAS Tree](#4-publication-modules-separated-from-the-g-atlas-tree)
- [5. Not Every Node Needs Every Manual](#5-not-every-node-needs-every-manual)
- [6. G-ATLAS Is the Allocation Backbone, Not a Mandatory TOC](#6-g-atlas-is-the-allocation-backbone-not-a-mandatory-toc)
- [7. The 19 PMCs](#7-the-19-pmcs)
- [8. SSOT + PUB Preserved](#8-ssot--pub-preserved)
- [9. Governance](#9-governance)
- [References](#references)

---

## 1. The Four Layers

```text
01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure/
├── README.md                        ← this root doctrine
├── 00_TPUBS-GOVERNANCE/             ← BREX, DMRL control, schemas, applicability, publication policy
├── 01_INFORMATION-ARCHITECTURE/     ← single canonical G-ATLAS instance + common DM pool
│   ├── G-ATLAS_000-099/
│   ├── EPTA_400-499/
│   └── AMTA_500-599/
├── 02_PUBLICATION-MODULES/          ← one PMC per publication; references only
│   ├── PMC-EWTW-AMM_Aircraft-Maintenance-Manual/
│   ├── PMC-EWTW-FIM_Fault-Isolation-Manual/
│   ├── PMC-EWTW-SDS_System-Description-Section/
│   └── … (19 PMCs)
├── 03_GENERATED-PUBLICATIONS/       ← rendered / distributed outputs
└── 04_CONSOLIDATED-REGISTERS/       ← generated global aggregations (DMRL-EWTW, DML-EWTW)
```

| Layer | Function |
|---|---|
| `00_TPUBS-GOVERNANCE` | Cross-cutting CSDB rules (BREX, DMRL control, schemas, applicability, publication policy) |
| `01_INFORMATION-ARCHITECTURE` | Canonical classification by G-ATLAS/SNS; local DMRL per node; common DM pool |
| `02_PUBLICATION-MODULES` | Composition of publications by reference |
| `03_GENERATED-PUBLICATIONS` | Rendered or distributed outputs |
| `04_CONSOLIDATED-REGISTERS` | Generated global aggregations |

---

## 2. Logical Model

```text
                    eWTW PRODUCT
                         │
                         ▼
                G-ATLAS / SNS TREE
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
       NODE DMRL                 NODE DMRL
      021-510-010               021-510-030
             │                       │
             └───────────┬───────────┘
                         ▼
                 COMMON DM POOL / CSDB
                         │
       ┌─────────┬───────┼───────┬─────────┐
       ▼         ▼       ▼       ▼         ▼
      AMM       SDS     FIM     IPC       CMM
       │         │       │       │         │
       └──── Publication Modules / views ──┘
```

The hierarchy is:

```text
eWTW product/model → G-ATLAS/SNS → information nodes → node DMRLs
   → common Data Modules → Publication Modules → AMM, FIM, SDS, IPC, FCOM, …
```

---

## 3. DMRL per G-ATLAS Node

Every node in `01_INFORMATION-ARCHITECTURE` carries a `DMRL-<code>.yaml`. Not every node must author its own Data Modules, but **every node must be able to declare** whether it holds its own information requirements, inherited requirements, or none:

* `information-authoring-node` — declares its own `dataModuleRequirements` (InfoCode, schemaType, status, publicationTargets, authored DMs);
* `placeholder-node` — declares no requirements yet;
* `information-rollup-node` — section/chapter aggregation, generated from child DMRLs.

The relation is deliberately many-to-many:

```text
one G-ATLAS node → several DM requirements / InfoCodes
                 → several Data Modules
                 → several Publication Modules
```

There is **no** `one node = one manual` relation and **no** `one Data Module = one manual` relation. Modular reuse is precisely one of the central benefits of S1000D.

Effectivity forks inside a node (e.g. `040A_EFF-PRE-MOD-…` / `040B_EFF-POST-MOD-…`) remain governed by the fork rule: a new info-code variant is valid only when the mod changes DM content; an effectivity-only change is a stack update.

---

## 4. Publication Modules Separated from the G-ATLAS Tree

Inside `02_PUBLICATION-MODULES`, a PMC contains the **editorial structure of the publication and references to the DMs** — never a material copy of the information tree:

```text
02_PUBLICATION-MODULES/
└── PMC-EWTW-AMM_Aircraft-Maintenance-Manual/
    ├── PMC-EWTW-AMM.yaml                     ← publication configuration / selection rules
    ├── PM-EWTW-AMM-021_AIR-CONDITIONING.yaml ← editorial projection of chapter 021
    ├── pm.xml · publication-baseline.yaml · applicability.yaml · dm-reference-index.yaml
    └── …
```

A PM is generated (regenerable) from the DMRL rows that satisfy its selection, e.g.:

```text
publicationTargets contains PMC-EWTW-AMM  AND  G-ATLAS chapter = 021
```

The PMCs keep their role as: publication identity, publication configuration, editorial structure, PM sequence, selection rules, applicability, release baseline, DM references, front matter and delivery configuration. They do **not** own canonical content.

Terminology: the **manual/publication** is identified by a PMC; it may be structured through a hierarchy of Publication Modules; the PMs reference the Data Modules; the Data Modules come from the common pool; the DMRL governs their necessity and planning. So: *"define the DMRL for each G-ATLAS node and organize the publications through Publication Modules"* — not *"organize the manuals inside the publication modules."*

---

## 5. Not Every Node Needs Every Manual

The DM ↔ publication matrix is metadata, not folders:

```yaml
publicationTargets:
  - PMC-EWTW-AMM
  - PMC-EWTW-SDS
```

```text
absence of a publicationTarget  =  the Data Module does not enter that publication
```

No `AMM/ FIM/ IPC/ SDS/ …` folders exist under information nodes: that would materialize a sparse matrix in the filesystem. Example allocation:

| Node / content | SDS | AMM | FIM | IPC | FCOM | MPD |
|---|--:|--:|--:|--:|--:|--:|
| ECS general architecture | ✓ | ✓ | | | ✓ | |
| Compressor removal | | ✓ | | | | |
| Compressor fault isolation | | possible reference | ✓ | | | |
| Compressor illustrated parts | | | | ✓ | | |
| Scheduled inspection | | ✓ | | | | ✓ |
| Cockpit ECS operation | | | | | ✓ | |

The DMRL determines this matrix — not the pre-emptive presence of a manual folder under every node.

---

## 6. G-ATLAS Is the Allocation Backbone, Not a Mandatory TOC

AMM, SDS, FIM and IPC can largely follow the ATA/G-ATLAS breakdown (`chapter → section → subject`). Other publications follow purpose-specific editorial axes while keeping the G-ATLAS link through DM references:

| Publication | Primary editorial axes |
|---|---|
| MPD | maintenance task, threshold, interval, zone, access, applicability, MRBR/ALS/CMR source, programme logic |
| MMEL | item, number installed, number required for dispatch, rectification interval, operational/maintenance procedure, dispatch condition |
| SB | modification, event, effectivity, compliance category, embodiment, configuration delta |
| CMM | component, part number, vendor, shop maintenance breakdown, disassembly level |
| DPP-Pub | asset, serial number, material, provenance, lifecycle event, compliance evidence, maintenance state |

```text
G-ATLAS = semantic allocation backbone
Publication Module = purpose-specific projection
```

Not: `G-ATLAS = identical mandatory table of contents of every manual`.

---

## 7. The 19 PMCs

13 heritage (AMM, CMM, CPM, FCOM, FIM, IPC, MMEL, MPD, SB, SBI, SDS, SRM, TEM), 2 green-native propulsion-module (PM-IPC, PMM), 4 green-delta (DPP-Pub, ECHM, ESMM, HVSM). The set is authorized by the SSOT **Publication-Type (DTD) Register**; the TPuBS may instantiate only types defined there. All live under `02_PUBLICATION-MODULES/` as publication definitions.

---

## 8. SSOT + PUB Preserved

The SSOT (the Q+ATLANTIDE standard nodes plus engineering content) remains the single source. The information architecture derives its scope from the SSOT (per-node `ssot-ref.yaml` / impact analyses); it never writes back. Publications are derived projections of the common pool: change an SSOT node, update the affected node DMRLs and DMs, regenerate only the affected PMs. *Engineering revision ≠ publication revision.*

---

## 9. Governance

Inherits **DEGF v1.0**; governed across **LC-A … LC-N**; bound by **No-AAA** and **SSOT+PUB**. Publication types authorized by the SSOT DTD register; terminology by **G-ATLAS-NORM-TERM-001**. Cross-cutting CSDB rules live in `00_TPUBS-GOVERNANCE/`. Owner **Q-DATAGOV**.

---

## References

1. S1000D — *International Specification for Technical Publications Using a Common Source Data Base* (DM, PM, DMRL, BREX, SNS, applicability; baseline Issue 4.2). <https://s1000d.org/>
2. ATA / Airlines for America — *iSpec 2200* (publication-type origin). <https://publications.airlines.org/>

<!--
Last.MarkedDown:
  artifact: TPuBS/README.md (root)
  revision: v3.0 — information-centric; single G-ATLAS instance; DMRL per node; PMCs as publication views
  supersedes: v2.0 (manual-first; G-ATLAS replicated under each PMC)
  version: "3.0"
.YieldedAlgorithmicMachineLearning: true
-->
