# Baseline and Block Governance

## 1. Purpose

This document defines the controlled baseline hierarchy and block governance
framework for `Q+ATLANTIDE` and associated programmes. It ensures that
evolutionary blocks, incremental releases, and upgrade branches are tracked
through controlled baselines, configuration-management authority assignments,
and lifecycle gates.

---

## 2. Baseline Hierarchy

```text
Top-Level Functional Baseline
└── Cumulative Functional and Allocated Baseline (per block)
    └── Product Baseline (per incremental release)
        └── Upgrade Branch Baseline (per upgrade candidate)
```

| Baseline Type                            | When Established                         | CM Authority                                  |
| ---------------------------------------- | ---------------------------------------- | --------------------------------------------- |
| Top-Level Functional Baseline            | Capstone / overall need                  | PMO                                           |
| Cumulative Functional/Allocated Baseline | Per block, after requirements allocation | PMO with contractor support                   |
| Product Baseline                         | Per incremental release / delivery       | Contractor / delivery authority               |
| Upgrade Branch Baseline                  | When upgrade enters concept stage        | PMO / contractor / Q-Division as applicable   |

---

## 3. Baseline Hierarchy Rule

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

## 4. Block Governance Principles

1. **Core blocks** establish the operationally suitable system with technologies
   mature enough for the current lifecycle stage.
2. **Evolutionary blocks** extend capability through controlled addition, not
   uncontrolled redesign.
3. **Incremental releases** deliver portions of a block's allocated capability
   as product baselines, each meeting the cumulative allocated baseline.
4. **Upgrade branches** start a new concept baseline when a technology candidate
   reaches its target TRL; they do not overwrite the released product baseline.

---

## 5. Open Architecture Rule

```yaml
open_architecture_upgrade_rule:
  id: QATL-OPEN-ARCH-UPGRADE-001
  rule: >
    The core system architecture shall emphasize openness, modularity,
    functional partitioning, stable interfaces, and open-system design so that
    future upgrades can be inserted through controlled modification rather than
    uncontrolled redesign wherever technically and economically feasible.
```

---

## 6. Programme Separation

Architecture-level baseline definitions shall remain **programme-agnostic**.
Programme-specific baseline records shall be stored separately with programme,
product, configuration, lifecycle state, and evidence effectivity.

---

## 7. Cross-References

| Document                                                          | Content                                            |
| ----------------------------------------------------------------- | -------------------------------------------------- |
| `evolutionary-acquisition-planning.md`                            | Characterization, planning, and SE requirements.  |
| `upgrade-revision-cycle-rules.md`                                 | Upgrade revision-cycle restart rules and schemas. |
| `technology-insertion-and-configuration-compatibility.md`         | Technology insertion and compatibility rules.     |
| `TRL-controlled-vocabulary.yaml`                                  | TRL scale (TRL-1 to TRL-9).                       |

---

## 8. References

- **[SEF-01]** *Systems Engineering Fundamentals* — Defense Acquisition
  University / DoD guide. MIT OCW 16.885J Aircraft Systems Engineering,
  Fall 2005.
  <https://ocw.mit.edu/courses/16-885j-aircraft-systems-engineering-fall-2005/resources/sefguide_01_01/>
- **[SE-PDF]** *SYSTEMS Engineering* — Comprehensive SE reference covering
  SE processes, architecture development, requirements analysis, verification
  & validation, and technology maturity assessment (`SYSTEMS_engineering.pdf`).
