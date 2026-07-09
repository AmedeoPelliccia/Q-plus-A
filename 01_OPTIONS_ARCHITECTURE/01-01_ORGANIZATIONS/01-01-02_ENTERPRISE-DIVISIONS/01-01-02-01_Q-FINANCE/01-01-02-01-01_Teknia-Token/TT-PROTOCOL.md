# TT-PROTOCOL — Teknia Token Stage-0 Economic-Operational Protocol

Status: Stage 0 (protocol) / Stage 1 (ledger). TT is a unit of verified technical
contribution. This protocol uses normative language: **MUST**, **MUST NOT**, **MAY**.

## 1. Ex-ante quotation

Every work package **MUST** be quoted before assignment in workload points:

```
Q = H × C × S × R
```

where:

| Symbol | Meaning |
| --- | --- |
| `H` | estimated hours |
| `C` | complexity coefficient |
| `S` | specialization coefficient |
| `R` | responsibility coefficient |

The coefficient table **MUST** be published in the tender **BEFORE** acceptance.
The quotation is **contestable before assignment** and **non-discretionary after
delivery**: once the work is delivered, the quoted `Q` **MUST NOT** be renegotiated.

## 2. Pool distribution

Within a tender, each work package `i` receives:

```
TT_i = TT_pool × Q_i / ΣQ_j
```

where `ΣQ_j` is the sum of workload points of all work packages settled from the
same pool.

## 3. Irrevocable reservation

Once a work package is `ASSIGNED`, its allocation **MUST NOT** be reduced.

## 4. Reviewer-pool separation

Acceptance reviewers **MUST** be remunerated from a pool distinct from the work pool
of the same tender (anti-capture). A pool's `reviewerPoolId` in
`TT-LEDGER/pools.yaml` records this separation.

## 5. Evidence-anchored emission

Emission occurs **only** on the verified lifecycle event of the work package, and
every emission row **MUST** reference the evidence hash (sha256 of the commit or
artifact).

Event vocabulary:

```
EVENTS = [QUOTED, ASSIGNED, ACCEPTED, RELEASED]
# TODO: bind to GQAOA-QFIN-TT-KLT-001 four-event grammar at merge review
```

## 6. Settlement

- Settlement trigger: `ACCEPTED`.
- Milestone-based partial settlements **MAY** be used; every partial **MUST** carry
  its own evidence hash.

## 7. Stage semantics

TT is **non-transferable** at Stage 0/1. Nothing in this protocol creates
convertibility, redemption or value promises.

## 8. Founder/genesis work

Retroactive architecture work packages **MUST** be quoted and settled through the
**SAME** process (issue, quotation, evidence, review) from the GENESIS pool
(`POOL-GENESIS-ARCHITECTURE`). There are **no undocumented allocations**.

---
No-AAA compliant.
