---
document_id: QPLUS-A-02-LIFECYCLE-MODEL-README
title: "Q-plus-A — Lifecycle Model"
repository: Q-plus-A
path: 02_LIFECYCLE_MODEL/README.md
register: Q-plus
architecture: OPTIONS_ARCHITECTURE
status: draft
version: "0.4.0"
revision: D
classification: open-governance-baseline
owner: AEROSPACEMODEL / Q-plus
lifecycle_model: "LC-letter CAD/product maturity model"
language: en
---

# 02_LIFECYCLE_MODEL — Lifecycle Model

## 1. Purpose

`02_LIFECYCLE_MODEL/` defines the controlled lifecycle maturity model used by Q-plus-A artefacts, products, CAD models, PLM records, publication modules, requirements records, evidence records, upgrade branches, and configuration baselines.

This lifecycle model provides a common governance language for moving an artefact from early conceptual definition to preliminary design, detailed design, qualification, certification, operations, MRO, and final nature-sustainment.

Version `0.4.0` extends the lifecycle model with:

- Technology Readiness Level integration;
- upgradeability and technology insertion governance;
- upgrade revision-cycle restart rules;
- evolutionary block and incremental capability logic;
- SBS-level breakdown integration;
- revision-specific `ReqBS`, `IBS`, `CBS`, `RBS`, `EBS`, `TPMS`, BOM, CAD, and publication records.

It retains the single LC-letter lifecycle axis (no enterprise LC01–LC14 axis). The only orthogonal overlay is TRL (technology maturity), which is distinct from LC-letter (product/CAD maturity) by design — see §13.

---

## 2. Lifecycle Model Type

Q-plus-A uses an **LC-letter CAD/product maturity model** for product, CAD, PLM, publication, evidence, and configuration artefacts.

```text
LC-letter stage      = maturity phase
REV-letter-number    = iteration inside the maturity phase
*_RELEASED           = formal release gate closing that maturity phase
```

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

| LC | Stage | Scope | Release Gate |
|---|---|---|---|
| `LC-A` | Conceptual Design | First concept, first geometry, early proportions, early feasibility placeholder, initial requirements baseline, initial upgrade watch list. | `REV-A_RELEASED` |
| `LC-B` | Preliminary Design | Main geometry, architecture sizing, preliminary interfaces, major configuration decisions, first interface-controlled upgrade compatibility logic. | `REV-B_RELEASED` |
| `LC-C` | Detailed Design | Detailed CAD/product definition, material stack, BOM/CAD consistency, drawing preparation, detailed `ReqBS/IBS/CBS/RBS/EBS/TPMS` alignment. | `REV-C_RELEASED` |
| `LC-D` | Analysis / Verification Design | Analysis-ready geometry, verification setup, simulation models, test logic, requirements verification planning. | `REV-D_RELEASED` |
| `LC-E` | Release Candidate / Engineering Definition | Engineering release candidate before physical mock-up, qualification, or certification use. | `REV-E_RELEASED` |
| `LC-F` | PMA — Physical Mock-Up Article and Wind Tunnel | Physical mock-up, installation mock-up, aerodynamic mock-up, wind-tunnel preparation. | `REV-F_RELEASED` |
| `LC-G` | Qualification | Qualification test article, qualification evidence, test reports, compliance-relevant records. | `REV-G_RELEASED` |
| `LC-H` | Hardware & Software Embodiment | Hardware embodiment, digital configuration, software/data integration, product-data binding. | `REV-H_RELEASED` |
| `LC-I` | Installation and Interface | Installation closure, interface maturity, aircraft or system integration readiness. | `REV-I_RELEASED` |
| `LC-J` | Certification | Certification configuration, compliance evidence, authority-facing artefacts. | `REV-J_RELEASED` |
| `LC-K` | First Flight and Industrialization | First-flight configuration, manufacturing readiness, industrialization transition. | `REV-K_RELEASED` |
| `LC-L` | Operations | In-service operational configuration, operator feedback, operational evidence. | `REV-L_RELEASED` |
| `LC-M` | MRO and Continuous Airworthiness | Maintenance, repair, overhaul, service bulletins, continued-airworthiness records. | `REV-M_RELEASED` |
| `LC-N` | Nature Sustainment | Circular economy, retirement, reuse, disposal, recycling, environmental sustainment. | `REV-N_RELEASED` |

> [!NOTE]
> Naming reconciled in this revision: `LC-F` = **PMA** (Physical Mock-up Article — `PMU` collides with Power Management Unit in the electric programmes) and **Wind Tunnel** (not Wind Gallery); `LC-H` = **Software Embodiment**. The stage table (§3) and folder pattern (§7) now agree. If the prior terms are deliberate house terms, override here and record the decision.

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

For upgrade-specific usage, the upgrade identifier shall be included:

```text
RADOME-UPG-001-REV-A0
RADOME-UPG-001-REV-A1
RADOME-UPG-001-REV-A_RELEASED
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

Any CAD/product/configuration revision may record findings.

| Finding Class | Meaning | Gate Impact |
|---|---|---|
| `F-INFO` | Informational note. | Does not block release. |
| `F-WARN` | Warning or limitation. | May block release depending on severity. |
| `F-BLOCK` | Blocking finding. | Blocks `*_RELEASED`. |
| `F-DEFER` | Deferred to later lifecycle stage. | Does not block current release if explicitly accepted. |

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

Recommended lifecycle folder pattern (rule `CAD-REVDIR-001`): the CAD tree materializes the LC-letter model as directories; each `REV` folder holds the native model plus a stable-named `*-CAD-Record.md`.

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
    ├── LC-F_PMA-Physical-Mock-Up-and-Wind-Tunnel/
    ├── LC-G_Qualification/
    ├── LC-H_Hardware-and-Software-Embodiment/
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
  revision_status: "created"        # enum: created | iterating | released
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

For upgrade-specific records:

```yaml
upgrade_lifecycle_record:
  upgrade_id: "<ITEM>-UPG-<NNN>"
  parent_baseline: "<baseline id>"
  lifecycle_model: "LC-letter CAD/product maturity model"
  lc_stage: "LC-A"
  current_revision: "<ITEM>-UPG-<NNN>-REV-A0"
  next_release_gate: "<ITEM>-UPG-<NNN>-REV-A_RELEASED"
```

---

## 9. Traceability Chain

The lifecycle model shall preserve the following chain:

```text
PBS → PNR → PN → BOM → CAD → STEP → Drawing → Evidence → Lifecycle Gate
```

| Layer | Required |
|---|---|
| PBS item | Yes |
| PNR | Yes, for physical items |
| Part Number | Yes, for physical items |
| BOM | Yes, when composition is defined |
| CAD native file | Yes, when CAD exists |
| STEP/export file | Required when export is produced |
| Drawing | Required when drawing is produced |
| Evidence record | Yes |
| Release gate | Yes |

For engineering breakdown traceability, the revision shall also reference:

```text
PBS REV-X → ReqBS REV-X → IBS REV-X → CBS REV-X → RBS REV-X → EBS REV-X → TPMS REV-X
```

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

Lifecycle records may appear under product-specific folders, especially under `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/…`. The root lifecycle model remains the controlling reference.

---

## 11. SBS Integration and Revisioned Breakdown Structures

Each SBS acts as the parent integration layer for controlled breakdown structures.

```text
SBS_System-Breakdown-Structure/
├── PBS_Product-Breakdown-Structure/
├── FBS_Functional-Breakdown-Structure/
├── WBS_Work-Breakdown-Structure/
├── CBS_Cost-Breakdown-Structure/
├── RBS_Risk-Breakdown-Structure/
├── LBS_Logistic-Breakdown-Structure/
├── EBS_Evidence-Breakdown-Structure/
├── IBS_Interface-Breakdown-Structure/
├── ReqBS_Requirements-Breakdown-Structure/
└── TPMS_Technical-Performance-Measurement-Structure/
```

The SBS defines the breakdown family. The PBS defines the physical item. Each `PBS REV-X` defines the authoritative state of its associated revision-specific breakdowns.

```yaml
revisioned_breakdown_structure_rule:
  id: SBS-REV-BREAKDOWN-001
  name: "Revisioned Breakdown Structures Rule"
  rule: >
    Each SBS shall include controlled breakdown structures for product,
    function, work, cost, risk, logistics, evidence, interfaces, requirements,
    and technical performance measurement. These structures may define generic
    architecture patterns at SBS level, but their authoritative state for a
    physical product item shall be recorded per PBS item revision. Therefore,
    each PBS revision shall maintain its own revision-specific ReqBS, IBS, CBS,
    RBS, EBS, BOM, CAD, TPMS, and publication references as applicable.
```

---

## 12. Requirements Evolution Rule

Requirements shall not be treated as static lifecycle-folder content. They shall be revisioned artefacts linked to the applicable PBS item, product configuration, and lifecycle maturity state.

```yaml
requirements_evolution_rule:
  id: REQBS-REV-001
  name: "Requirements Evolve by Product Revision"
  rule: >
    Requirements shall be controlled as revisioned artefacts linked to the
    applicable PBS item, product configuration, and lifecycle maturity state.
    A change in requirements that affects geometry, interfaces, cost, risk,
    evidence, certification, operations, maintainability, or sustainability
    shall create or update the corresponding REV-X ReqBS and trigger impact
    assessment across IBS, CBS, RBS, EBS, BOM, CAD, TPMS, and PUB artefacts.
```

Minimum ReqBS class set:

| ReqBS Class | Name |
|---|---|
| `ReqBS-01` | Customer Expectations |
| `ReqBS-02` | Project and Enterprise Constraints |
| `ReqBS-03` | External Constraints |
| `ReqBS-04` | Operational Scenarios |
| `ReqBS-05` | Measures of Effectiveness |
| `ReqBS-06` | System Boundaries |
| `ReqBS-07` | Interfaces |
| `ReqBS-08` | Utilization Environments |
| `ReqBS-09` | Lifecycle Requirements |
| `ReqBS-10` | Functional Requirements |
| `ReqBS-11` | Performance Requirements |
| `ReqBS-12` | Modes of Operation |
| `ReqBS-13` | Technical Performance Measures |
| `ReqBS-14` | Physical Characteristics |
| `ReqBS-15` | Human Systems Integration |

---

## 13. TRL, Upgradeability, and Technology Insertion

Q-plus-A distinguishes technology maturity from product lifecycle maturity.

```text
TRL        = technology maturity            (overlay; see 01-03 Q+ATLANTIDE TRL layer)
LC-letter  = product/CAD/configuration maturity
REV cycle  = controlled design iteration inside a lifecycle stage
```

```yaml
trl_lifecycle_relationship:
  id: QATL-TRL-LC-001
  rule: >
    TRL measures technology maturity. LC-letter stages measure product, CAD,
    integration, and configuration maturity. A technology reaching a target TRL
    does not automatically authorize installation into a product baseline. It
    authorizes the start of a controlled product-specific upgrade revision cycle.
```

```yaml
technology_insertion_rule:
  id: QATL-TICC-001
  name: "Technology Insertion and Configuration Compatibility"
  rule: >
    Product and architecture designs shall define a baseline configuration
    using technology mature enough for the current lifecycle stage, while
    maintaining controlled compatibility paths for future alternatives with
    higher sustainability, efficiency, maintainability, safety, circularity,
    or performance potential. No future technology shall be inserted into a
    controlled product configuration without TRL assessment, interface
    compatibility assessment, evidence delta analysis, lifecycle insertion
    gate definition, and configuration-control approval.
```

---

## 14. Upgrade Revision-Cycle Restart Rule

When a future upgrade or alternative technology reaches the target TRL required for insertion, it shall not overwrite the existing released baseline. It shall start its own controlled concept baseline.

```yaml
upgrade_revision_cycle_rule:
  id: QATL-UPGRADE-REV-CYCLE-001
  name: "Upgrade Revision Cycle Restart Rule"
  rule: >
    When an alternative technology reaches the target TRL required for product
    insertion, it shall not overwrite the current released baseline. The upgrade
    shall start a new controlled revision cycle from its own concept baseline,
    beginning at LC-A / REV-A0 or an equivalent upgrade-specific concept state.
    The upgrade may only modify or replace the current product baseline after
    interface compatibility, evidence delta, configuration-control approval,
    and lifecycle release gates are satisfied.
```

```text
A technology upgrade becomes eligible through TRL maturity.
It becomes installable only through LC/REV maturity.
It becomes part of the operational baseline only through configuration-control approval.
```

---

## 15. Upgrade Branch Record

```yaml
upgrade_branch_record:
  upgrade_id: "<UPGRADE-ID>"
  upgrade_name: "<upgrade name>"
  parent_product_baseline: "<baseline id>"
  parent_block: "<block id>"
  triggering_condition: "target TRL reached"
  triggering_trl: "TRL-<1..9>"
  starts_at_lifecycle_stage: "LC-A"
  starts_at_revision: "<ITEM>-UPG-<NNN>-REV-A0"
  current_revision: "<ITEM>-UPG-<NNN>-REV-A0"
  next_release_gate: "<ITEM>-UPG-<NNN>-REV-A_RELEASED"
  baseline_relation: "<replacement | modification | optional block upgrade | service bulletin candidate>"
  insertion_allowed_only_after:
    - "interface compatibility approved"
    - "evidence delta closed"
    - "requirements validation completed"
    - "risk assessment accepted"
    - "configuration-control approval"
    - "lifecycle release gate closed"
  operational_baseline_impact: "<none | optional | partial | replacement>"
  status: "<concept | iterating | released | inserted | rejected | superseded>"
```

---

## 16. Evolutionary Acquisition and Baseline Structuring

```text
Core baseline → evolutionary blocks → incremental capability releases → associated product improvements
```

| Characterization | System Level | Programme Level | Documentation Required | Baseline | CM Authority |
|---|---|---|---|---|---|
| Overall Need | Major Programme / Portfolio / Business Area | Capstone or Sub-Portfolio | Capstone Acquisition Documentation | Top-Level Functional Baseline | PMO |
| Core and Evolutionary Blocks | Build or Block of Major Programme | Acquisition Programme | Full Programme Documentation | Cumulative Functional and Allocated Baseline | PMO with Contractor Support |
| Incremental Delivery of Capability | Release or Version of Block | Internal to Acquisition Programme | Separate Acquisition Documentation not required unless required by programme rules | Product Baseline | Contractor / Delivery Authority; must meet Allocated Baseline |
| Associated Product Improvements | Application, Bridge, Upgrade Branch, or Product Improvement | Parallel Product Improvement / Technology Insertion Candidate | Component-Level or Lower-Decision-Level Processing | Functional, Allocated, and Product Baselines | PMO / Contractor / Responsible Q-Division |

```yaml
evolutionary_acquisition_rule:
  id: QATL-EVO-ACQ-001
  name: "Evolutionary Acquisition and Baseline Structuring Rule"
  rule: >
    Programmes shall define an operationally suitable core baseline and identify
    the subsystems, components, technologies, interfaces, and documentation sets
    most likely to evolve. Evolutionary blocks, incremental capability releases,
    and associated product improvements shall be planned through controlled
    baselines, TRL assessment, evidence records, configuration-management
    authority, and lifecycle gates.
```

---

## 17. Open Architecture Upgrade Rule

```yaml
open_architecture_upgrade_rule:
  id: QATL-OPEN-ARCH-UPGRADE-001
  rule: >
    The core system architecture shall emphasize openness, modularity,
    functional partitioning, stable interfaces, and open-system design so that
    future upgrades can be inserted through controlled modification rather than
    uncontrolled redesign wherever technically and economically feasible.
```

```yaml
baseline_hierarchy_rule:
  id: QATL-BASELINE-HIERARCHY-001
  rule: >
    Q+ATLANTIDE and programme baselines shall distinguish top-level functional
    baselines, allocated baselines, product baselines, and upgrade branch
    baselines. Incremental capability releases shall meet the allocated baseline.
    Upgrade branches shall not overwrite released product baselines until
    configuration approval and lifecycle release gates are satisfied.
```

---

## 18. Example — AMPEL360 eWTW Radome

```text
eWTW-PBS-10-10-10-10-10 — Radome
```

```yaml
radome_lifecycle_example:
  pbs_id: "eWTW-PBS-10-10-10-10-10"
  part_number: "PN-eWTW-5310-0001"
  lc_stage: "LC-A"
  lc_stage_name: "Conceptual Design"
  current_revision: "RADOME-REV-A1"
  revision_status: "iterating"
  next_release_gate: "RADOME-REV-A_RELEASED"
  next_revision: "RADOME-REV-A2"
```

Current revision-specific breakdown package:

```yaml
radome_rev_a1_breakdown_package:
  pbs_revision: "RADOME-REV-A1"
  reqbs: "01_REQUIREMENTS/REV-A1/ReqBS-RADOME-REV-A1.md"
  ibs: "02_INTERFACES/REV-A1/IBS-RADOME-REV-A1.md"
  cbs: "03_COST/REV-A1/CBS-RADOME-REV-A1.md"
  rbs: "04_RISK/REV-A1/RBS-RADOME-REV-A1.md"
  ebs: "05_EVIDENCE/REV-A1/EBS-RADOME-REV-A1.md"
  cad: "cad/freecad/LC-A_Concept-Design/REV-A1/"
  pub_040: "pub/040_descriptive/"
  pub_258: "pub/258_bonding-and-lightning-check/"
```

Known REV-A1 gate findings:

| Finding | Class | Meaning | Gate Impact |
|---|---|---|---|
| `F1` | `F-BLOCK` | Absolute scale must be verified or closed. | Blocks `RADOME-REV-A_RELEASED`. |
| `F2` | `F-DEFER` | Solid body only; sandwich wall deferred. | Becomes mandatory at LC-C. |
| `F3` | `F-BLOCK` | Controlled metadata must be completed. | Blocks `RADOME-REV-A_RELEASED`. |
| `F4` | `F-WARN` | ReqBS exists; IBS/CBS/RBS/EBS/TPMS revision packages pending. | Blocks full configuration release if not completed or explicitly deferred. |

Example upgrade candidate:

```yaml
radome_upgrade_candidate_example:
  upgrade_id: "RADOME-UPG-001"
  upgrade_name: "Recyclable Low-Loss Dielectric Core"
  baseline_configuration: "RADOME-CONF-A"
  baseline_technology: "Conventional RF-transparent sandwich laminate"
  qatl_reference: "AMTA material node TBD (material maturity owned by AMTA); ATLAS 050-059 integration, node TBC"
  current_trl: "TRL-5"
  target_trl_for_insertion: "TRL-6"
  decision_status: "watched"
  expected_benefit:
    sustainability: "high"
    efficiency: "medium"
    circularity: "high"
    weight_reduction: "medium"
    maintainability: "medium"
    safety: "medium"
  compatibility_constraints:
    - "radome backup mechanical interface"
    - "RF transparency"
    - "bird-strike resistance"
    - "lightning diverter compatibility"
    - "moisture ingress resistance"
    - "certification basis"
  upgrade_revision_cycle:
    trigger: "target TRL reached"
    starts_at: "LC-A / RADOME-UPG-001-REV-A0"
    next_release_gate: "RADOME-UPG-001-REV-A_RELEASED"
    baseline_relation: "candidate replacement or modification to RADOME-CONF-A"
```

---

## 19. Governance Rules

1. The lifecycle model shall use LC-letter stages from `LC-A` through `LC-N`.
2. Revisions inside a lifecycle stage shall use the corresponding revision letter.
3. A lifecycle stage shall close only through its `*_RELEASED` gate.
4. Blocking findings (`F-BLOCK`) shall prevent release-gate closure.
5. Deferred findings (`F-DEFER`) shall identify the lifecycle stage where they become mandatory.
6. CAD/product lifecycle records shall preserve PBS, PN, CAD, evidence, and release-gate traceability.
7. Product-specific lifecycle folders may extend this model but shall not contradict it.
8. Each SBS shall define the controlled breakdown family for PBS, FBS, WBS, CBS, RBS, LBS, EBS, IBS, ReqBS, and TPMS.
9. Each PBS revision shall maintain its own revision-specific breakdown records where applicable.
10. Requirements shall evolve by product revision and shall not be stored only as static LC-folder content.
11. TRL maturity shall not be treated as product installation maturity.
12. A mature upgrade shall start its own LC/REV concept baseline before insertion.
13. Upgrade branches shall not overwrite released product baselines without configuration-control approval.
14. The root `02_LIFECYCLE_MODEL/README.md` is the controlling lifecycle reference for Q-plus-A unless superseded by a higher governance document.

---

## 20. Controlled Closure Statement

`02_LIFECYCLE_MODEL/README.md` defines the root lifecycle maturity model for Q-plus-A CAD/product artefacts, on a single LC-letter axis.

Version `0.4.0` additionally controls the relationship between:

```text
LC-letter lifecycle maturity
REV-controlled configuration states
SBS breakdown families
PBS revision-specific engineering truth
ReqBS / IBS / CBS / RBS / EBS / TPMS revision packages
TRL maturity (orthogonal overlay)
upgradeability
evolutionary acquisition blocks
upgrade branch baselines
```

It shall be referenced by product-specific lifecycle records such as:

```text
cad/freecad/LC-A_Concept-Design/REV-A1/Radome-CAD-Record.md
01_REQUIREMENTS/REV-A1/ReqBS-RADOME-REV-A1.md
```

---

## Revision history

| Version | Date | Change |
|---|---|---|
| `0.1.0` | 2026-05-30 | Initial root lifecycle model. |
| `0.2.0` | 2026-05-31 | (Branch) two-axis orthogonality + revision_status enum + naming reconciliations. |
| `0.3.0` | 2026-05-31 | Removed the two-axis distinction and all LC01–LC14 references. Single LC-letter lifecycle. |
| `0.4.0` | 2026-05-31 | Major extension (renumbered from the shared 0.2.0/A1 draft to keep versioning monotonic above 0.3.0): TRL integration (§13), technology insertion & upgrade revision-cycle rules (§13–§15), evolutionary acquisition & open-architecture baselines (§16–§17), SBS breakdown families & revisioned breakdown structures (§11), requirements evolution & ReqBS classes (§12). Single LC-letter axis retained; TRL is the only orthogonal overlay. §3↔§7 naming aligned (PMA / Wind Tunnel / Software Embodiment). |


