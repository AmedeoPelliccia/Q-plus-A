# 042-400-200 — Partition Allocation and Hosting Plan

**Node:** 042-400_Hosted-Function-Partitioning-and-Configuration · **Subject:** 002

- The hosting plan is a controlled architecture item: function-to-partition-to-module assignment with recorded rationale.
- Segregation and co-location rules are declared: independence requirements, mixed-criticality co-hosting conditions, and prohibited combinations.
- Spare partitions and growth capacity are declared reserves of the plan, consistent with platform reserves (042-100).
- Re-hosting a function is a plan change with its own re-verification scope (005), never a maintenance action.

```mermaid
flowchart TD
  subgraph CPMA["Module A"]
    P1["Partition 1<br/>Function F1"]
    P2["Partition 2<br/>Function F2"]
    PS1["Spare partition"]
  end
  subgraph CPMB["Module B"]
    P3["Partition 3<br/>Function F1 (redundant)"]
    P4["Partition 4<br/>Function F3"]
  end
  F1["F1 — high-integrity"] --> P1
  F1 --> P3
  F2["F2"] --> P2
  F3["F3"] --> P4
  P1 -. "segregation rule" .- P2
```

