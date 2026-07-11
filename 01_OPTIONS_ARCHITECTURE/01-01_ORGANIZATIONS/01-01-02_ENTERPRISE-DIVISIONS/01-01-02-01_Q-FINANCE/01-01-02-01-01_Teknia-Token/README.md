# Teknia Token (TT)

**Q-FINANCE node `01-01-02-01-01_Teknia-Token` — protocol, ledger SSOT and tooling of the Teknia Token.**

## Identity

**Teknia Token (TT)** is the unit of **verified technical contribution** of the Q+ engineering ecosystem. TT are integer units (no decimals): workload points quoted ex ante map 1:1 to whole tokens. Every unit traces to an approved work package and a sha256 evidence hash — no evidence, no emission. At the current stage TT is **non-transferable** and is not offered, priced, redeemed or traded; it is an accounting unit for governed contribution settlement, not an investment product.

*"TEK-TOK" is an internal colloquial alias only — not for public branding (trademark clearance pending, gate G6).*

## What lives here — and what lives in TEKNIA-TOKENS

| Here (authoritative) | External repo [`TEKNIA-TOKENS`](https://github.com/AmedeoPelliccia/TEKNIA-TOKENS) |
|---|---|
| TT-PROTOCOL (quotation, pools, settlement rules) | Smart contracts (`TekniaTokenV0`, `TekniaLedgerAnchor`) |
| Ledger SSOT (`pools.yaml`, `emissions.yaml`) | Foundry tests and testnet deployment |
| Validation, derivation and anchoring tools | Gated release structure (`releases/v0.1 … v1.0`) |
| Anchor evidence log (`anchors.log`) | Audits (when gate G5 opens) |

`pinned-commit: TBD` — updated at every release that cross-references the two repositories.

The coupling is **cryptographic, not filesystem**: each row of `anchors.log` (`utc, merkle_root, emissions_sha256, ledger_ref`) is directly replayable on-chain via `TekniaLedgerAnchor.anchor(merkleRoot, ledgerSha256, ledgerRef)`.

## Node map

```text
01-01-02-01-01_Teknia-Token/
├── README.md                                   this file
├── TT-PROTOCOL.md                              Stage-0 normative protocol
├── GQAOA-QFIN-TT-REL-001_...Roadmap.md         staged release roadmap and gates
├── TT-LEDGER/
│   ├── pools.yaml                              authored SSOT — tender pools
│   ├── emissions.yaml                          authored SSOT — settled emissions
│   ├── anchors.log                             APPEND-ONLY evidence log (never edited,
│   │                                           never regenerated — outside derived/)
│   └── derived/                                GENERATED views — never hand-edited
│       ├── balances.yaml
│       └── balances.md
└── tools/
    ├── validate_ledger.py                      CI gate — schema, budgets, identities
    ├── build_balances.py                       derives balances (+ --check freshness)
    ├── build_merkle_root.py                    Merkle root + --anchor evidence rows
    └── tests/                                  pytest suite (16 tests)
```

## Stages and gates

| Stage | Where | Content |
|---|---|---|
| **0 — Protocol** | this node | TT-PROTOCOL frozen: ex-ante quotation, pools, reviewer separation |
| **1 — Ledger** | this node | Non-transferable ledger units; CI-validated emissions; anchoring |
| **2 — Testnet artifact** | TEKNIA-TOKENS | Contracts + tests deployed on testnet; mirror mints replay the ledger |
| **3 — Public release** | TEKNIA-TOKENS | **GATED** — opens only when G1–G6 are all closed |

Gates: **G1** issuing legal entity with counsel · **G2** MiCA classification memo and authority touchpoints · **G3** tax/labor framing of contributor settlement · **G4** AML/KYC posture if transferable · **G5** independent smart-contract audit · **G6** trademark clearance of the public name.

## How an emission happens

1. The contributor is **registered** in `TEAM-REGISTER.csv` (enrolment per `CONTRIBUTING.md` §2.1) — registration is a settlement precondition, enforced by CI.
2. A `[WORK PACKAGE]` issue is approved; its pool is **reserved ex ante** with the published quotation `Q = H × C × S × R` (irrevocable once assigned).
3. The work is delivered with evidence; acceptance review is remunerated from a **separate reviewer pool** (anti-capture).
4. The issue reaches **`ACCEPTED`**.
5. A pull request appends one row to `emissions.yaml`: `id, memberId, poolId, workPackage, amount, event, evidenceHash (sha256), date`.
6. CI validates (`validate_ledger.py --strict`) and checks derived freshness (`build_balances.py --check`).
7. Balances regenerate under `derived/`; periodically `build_merkle_root.py --anchor` appends an evidence row to `anchors.log` for on-chain replay.

## Tooling contract

All tools share one contract: `--root` is **this node directory** (CI passes `--root "$TT_NODE"`); `main(argv)` returns an int; all findings are collected, never early-exited.

```text
validate_ledger.py  [--root .] [--strict] [--register PATH]
    exit 1 on violations; --strict promotes warnings to violations
    (including a missing team register — no silent green checks)

build_balances.py   [--root .] [--check | --dry-run]
    regenerates derived/ deterministically; commit regenerated derived
    files together with ledger changes or --check fails in CI

build_merkle_root.py [--root .] [--anchor] [--ref REF]
    prints the canonical Merkle root (EMPTY_ROOT sentinel on empty ledger);
    --anchor appends to anchors.log with duplicate guard, UTC timestamp
    and ledger_ref (defaults to the short git commit)
```

Run the suite: `python3 -m pytest tools/tests` — validator messages are contractual API: they change only together with the tests.

## Governance pointers

Normative protocol: [`TT-PROTOCOL.md`](TT-PROTOCOL.md) · Roadmap and gates: [`GQAOA-QFIN-TT-REL-001`](GQAOA-QFIN-TT-REL-001_Teknia-Token-Release-Roadmap.md) · Work-package process: repository [`CONTRIBUTING.md`](../../../../../CONTRIBUTING.md) §1–3 · Founder/genesis work follows the same process from the GENESIS pool — no undocumented allocations.

## Instance governance roles (Stage 1)

| Role | Holder |
|---|---|
| Architecture authority / governance | AmedeoPelliccia |
| Emitter (ledger) | AmedeoPelliccia |
| Anchorer | AmedeoPelliccia |
| Independent reviewer | OPEN — see the TT-REVIEW-GENESIS work package |

Single-operator bootstrap is declared explicitly; the reviewer seat is an open
tender, not a self-review.
