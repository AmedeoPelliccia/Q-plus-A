# Evolutionary Acquisition Planning

## 1. Purpose

This document defines the evolutionary acquisition planning framework for
`Q+ATLANTIDE` and associated programmes. Evolutionary acquisition structures
capability delivery into planned, controlled, technology-realistic blocks, so
that an operationally suitable core system is delivered first while future
capabilities are inserted through controlled upgrade branches, not uncontrolled
baseline overwrites.

---

## 2. Core Governance Principles

> **Design for current certifiable feasibility, but architect for future
> substitution.**

> **The core system architecture shall be designed to accommodate change through
> open architecture, modular design, functional partitioning, stable interfaces,
> and controlled configuration baselines. Future upgrades shall be planned as
> evolutionary blocks or upgrade branches, not as uncontrolled overwrites of the
> current baseline.**

Controlled statement:

> A technology upgrade becomes **eligible** through TRL maturity.
> It becomes **installable** only through LC/REV maturity.
> It becomes **part of the operational baseline** only through
> configuration-control approval.

---

## 3. Evolutionary Acquisition Characterization

The following table defines the four characterization levels for evolutionary
acquisition planning:

| Characterization | System Level | Programme Level | Documentation Required | Baseline | CM Authority |
|---|---|---|---|---|---|
| Overall Need | Major Programme / Portfolio / Business Area | Capstone or Sub-Portfolio | Capstone Acquisition Documentation | Top-Level Functional Baseline | PMO |
| Core and Evolutionary Blocks | Build or Block of Major Programme | Acquisition Programme | Full Programme Documentation | Cumulative Functional and Allocated Baseline | PMO with Contractor Support |
| Incremental Delivery of Capability | Release or Version of Block | Internal to Acquisition Programme | Separate Acquisition Documentation Not Required unless required by programme rules | Product Baseline | Contractor / Delivery Authority; must meet Allocated Baseline |
| Associated Product Improvements | Application, Bridge, Upgrade Branch, or Product Improvement | Parallel Product Improvement / Technology Insertion Candidate | Component-Level or Lower-Decision-Level Processing | Functional, Allocated, and Product Baselines | PMO / Contractor / Responsible Q-Division |

### 3.1 Overall Need

- **System level:** Major programme, portfolio, or business area.
- **Acquisition programme level:** Capstone or sub-portfolio.
- **Documentation required:** Capstone acquisition documentation.
- **Baseline:** Top-level functional baseline.
- **Configuration-management authority:** PMO.

### 3.2 Core and Evolutionary Blocks

- **System level:** Build or block of a major programme.
- **Acquisition programme level:** Acquisition programme.
- **Documentation required:** Full programme documentation.
- **Baseline:** Cumulative functional and allocated baseline.
- **Configuration-management authority:** PMO with contractor support.

### 3.3 Incremental Delivery of Capability

- **System level:** Release or version of a block.
- **Acquisition programme level:** Internal to acquisition programme.
- **Documentation required:** Separate acquisition documentation not required
  unless required by programme rules.
- **Baseline:** Product baseline.
- **Configuration-management authority:** Contractor or delivery authority, but
  must meet allocated baseline.

### 3.4 Associated Product Improvements

- **System level:** Application, bridge, upgrade branch, or product improvement.
- **Acquisition programme level:** Parallel product improvement or technology
  insertion candidate.
- **Documentation required:** Component-level or lower-decision-level
  acquisition processing.
- **Baseline:** Functional, allocated, and product baselines as applicable.
- **Configuration-management authority:** PMO / contractor / responsible
  Q-Division as applicable.

---

## 4. Controlled Rules

### 4.1 Evolutionary Acquisition Rule

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

### 4.2 Evolutionary Planning Rule

```yaml
evolutionary_planning_rule:
  id: QATL-EVO-PLAN-001
  rule: >
    Evolutionary acquisition planning shall define how core and evolutionary
    blocks are structured, how operational feedback and technology advancements
    are captured, how upgrade candidates are evaluated, how requirements are
    validated, how upgrades are initiated, and how risks are managed technically
    and managerially.
```

### 4.3 Open Architecture and Upgrade Rule

```yaml
open_architecture_upgrade_rule:
  id: QATL-OPEN-ARCH-UPGRADE-001
  rule: >
    The core system architecture shall emphasize openness, modularity,
    functional partitioning, stable interfaces, and open-system design so that
    future upgrades can be inserted through controlled modification rather than
    uncontrolled redesign wherever technically and economically feasible.
```

### 4.4 Baseline Hierarchy Rule

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

### 4.5 TRL / Lifecycle Relationship

```yaml
trl_lifecycle_relationship:
  id: QATL-TRL-LC-001
  rule: >
    TRL measures technology maturity. LC-letter stages measure product, CAD,
    integration, and configuration maturity. A technology reaching a target TRL
    does not automatically authorize installation into a product baseline. It
    authorizes the start of a controlled product-specific upgrade revision cycle.
```

### 4.6 Upgrade Revision-Cycle Restart Rule

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

---

## 5. Programme Planning Requirements

Evolutionary acquisition programme planning shall define:

1. A clear description of an operationally suitable core system, including
   identification of subsystems and components most likely to evolve.
2. A process for obtaining, evaluating, and integrating operational feedback,
   technology advancements, and emerging commercial products.
3. Planning for evolutionary block upgrade evaluation, requirements validation,
   and programme initiation.
4. A management approach for evolutionary upgrades within a block and the
   constraints and controls associated with incremental delivery of capability.
5. Risk analysis of the developmental approach, both technical and managerial.

---

## 6. Systems Engineering Planning Requirements

Systems engineering planning shall emphasize:

1. Openness and modularity of the core system architecture to facilitate
   modification and upgrades.
2. Baseline documentation structured to improve flexibility for upgrade.
3. The impact of evolutionary acquisition planning on baseline development and
   documentation control.
4. Technical reviews structured to support acquisition decision points.
5. Risk management to monitor and control technical and managerial complexity
   introduced by evolutionary development.

---

## 7. Minimum Record Schemas

### 7.1 Evolutionary Block Record Schema

```yaml
evolutionary_block_record:
  block_id: "<BLOCK-ID>"
  block_name: "<block name>"
  programme: "<programme>"
  product: "<product or product family>"
  characterization: "<overall_need | core_block | incremental_release | product_improvement>"
  system_level: "<portfolio | programme | block | release | application | bridge | upgrade>"
  baseline_type: "<functional | allocated | product | upgrade_branch>"
  parent_baseline: "<baseline id>"
  current_baseline: "<baseline id>"
  cm_authority: "<PMO | contractor | Q-Division | joint>"
  documentation_required:
    - "<capstone | full_programme | product_baseline | component_level | evidence_delta>"
  trl_dependencies:
    - qatl_reference: "<Q+ATLANTIDE node>"
      current_trl: "TRL-<1..9>"
      target_trl: "TRL-<1..9>"
      evidence_record: "<link or TBD>"
  upgrade_candidates: []
  operational_feedback_sources: []
  risks:
    technical: []
    managerial: []
  status: "<planned | active | under_review | released | superseded>"
```

### 7.2 Upgrade Branch Record Schema

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
