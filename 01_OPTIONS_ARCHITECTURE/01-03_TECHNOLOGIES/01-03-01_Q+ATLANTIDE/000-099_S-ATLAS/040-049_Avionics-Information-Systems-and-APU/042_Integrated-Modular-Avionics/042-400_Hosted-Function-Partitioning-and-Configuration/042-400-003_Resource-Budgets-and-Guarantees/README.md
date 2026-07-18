# 042-400-003 — Resource Budgets and Guarantees

**Node:** 042-400_Hosted-Function-Partitioning-and-Configuration · **Subject:** 003

- Every hosted function operates under an ex-ante budget: time windows and periodicity, memory, network contract consumption (042-200) and IO allocations (042-300).
- Budget accounting is arithmetic and auditable: the sum of allocated budgets never exceeds characterized platform capacity, margins included — allocation is bounded by construction, not by testing alone.
- Margins policy is declared per resource class; consuming margin is a configuration event.
- Budget verification artifacts are evidence items (009).

