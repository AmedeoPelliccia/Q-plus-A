# 042-400-005 — Configuration Data Set and Change Control

**Node:** 042-400_Hosted-Function-Partitioning-and-Configuration · **Subject:** 005

- The integrated configuration is one versioned, consistency-checked data set: partition tables, budget tables, network contract references and IO mapping references — generated, rule-checked, never hand-assembled.
- Generation rules and consistency checks are themselves controlled items; a configuration is releasable only when all checks pass.
- Change classes are enumerated — add function, rebudget, re-host, remove — each with a declared re-verification scope.
- Loading and version verification follow the onboard-maintenance interfaces (REF 045); partial or mixed configurations are prohibited by doctrine.

```mermaid
flowchart LR
  S1["Hosting plan"] --> GEN["Generation tool"]
  S2["Budget tables"] --> GEN
  S3["042-200 contracts"] --> GEN
  S4["042-300 IO maps"] --> GEN
  GEN --> CHK["Rule & consistency checks"]
  CHK -- "all pass" --> CFG["Integrated configuration vN"]
  CHK -- "any fail" --> S1
  CFG --> LOAD["Load & verify via 045"]
```

