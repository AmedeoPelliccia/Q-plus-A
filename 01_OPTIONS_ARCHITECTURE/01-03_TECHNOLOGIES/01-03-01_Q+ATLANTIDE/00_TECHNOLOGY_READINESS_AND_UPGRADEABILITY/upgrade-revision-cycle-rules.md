# Upgrade Revision-Cycle Rules

## 1. Purpose

This document governs how a matured technology upgrade enters a controlled
product baseline within `Q+ATLANTIDE`. It ensures that an upgrade reaching its
target TRL does not overwrite an existing released baseline, but instead starts
its own controlled lifecycle and revision cycle.

## 2. Controlled Statement

> A technology upgrade becomes **eligible** through TRL maturity.
> It becomes **installable** only through LC/REV maturity.

## 3. Upgrade Revision Cycle Restart Rule

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

## 4. Minimum Upgrade Revision-Cycle Record Schema

```yaml
upgrade_revision_cycle_record:
  upgrade_id: "<UPGRADE-ID>"
  upgrade_name: "<upgrade name>"
  parent_baseline_configuration: "<baseline configuration id>"
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
    - "configuration-control approval"
    - "lifecycle release gate closed"
  operational_baseline_impact: "<none | optional | partial | replacement>"
  status: "<concept | iterating | released | inserted | rejected | superseded>"
```

## 5. TRL / Lifecycle Relationship

```yaml
trl_lifecycle_relationship:
  id: QATL-TRL-LC-001
  rule: >
    TRL measures technology maturity. LC-letter stages measure product, CAD,
    integration, and configuration maturity. A technology reaching a target TRL
    does not automatically authorize installation into a product baseline. It
    authorizes the start of a controlled product-specific upgrade revision cycle.
```

---

## 6. References

- **[SEF-01]** *Systems Engineering Fundamentals* — Defense Acquisition
  University / DoD guide. MIT OCW 16.885J Aircraft Systems Engineering,
  Fall 2005.
  <https://ocw.mit.edu/courses/16-885j-aircraft-systems-engineering-fall-2005/resources/sefguide_01_01/>
- **[SE-PDF]** *SYSTEMS Engineering* — Comprehensive SE reference covering
  SE processes, architecture development, requirements analysis, verification
  & validation, and technology maturity assessment (`SYSTEMS_engineering.pdf`).
