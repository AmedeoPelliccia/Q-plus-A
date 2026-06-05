---
document_id: G-ATLAS-000-000-008
title: "000-000-008 — Traceability and Evidence Index"
node: 000-000
item: "008"
ata_ref: 00-00-08
owner: Q-DATAGOV
agnostic: true
status: baseline
---

# 000-000-008 — Traceability and Evidence Index

> **Node:** `000-000` · **Item:** `008` · **ATA ref:** 00-00-08
> **Owner:** Q-DATAGOV · **Status:** baseline · **Agnostic:** yes

---

## 1. Purpose

This item is the **traceability and evidence index** for node `000-000`. It records:

- The parent requirement that each item satisfies.
- The applicable standard(s) each item references.
- The IEF (Integrity Evidence Framework) anchor for each item at baseline.
- The canonical DMC short-form for programme publications.

---

## 2. Traceability Structure

Each G-ATLAS item has a four-link traceability chain:

```text
Item (SSOT)
  └── Parent requirement (DEGF / Model Digital Constitution / governing standard)
      └── Applicable standard reference (ATA chapter, CS-25 article, …)
          └── IEF evidence anchor (SHA-256 at baseline)
              └── Programme DMC (in programme CSDB / PUB)
```

---

## 3. Item Traceability Register — Node 000-000

| Item | File | Parent requirement | Applicable standard | IEF anchor | DMC short-form |
|---|---|---|---|---|---|
| `000` | `000-000-000-…-Overview.md` | DEGF v1.0 — Orientation entry point | ATA 00-00-00; iSpec 2200 §0 | `<sha256: TBS>` | `DMC-<PROG>-000-000-000` |
| `001` | `000-000-001-…-Definitions.md` | DEGF v1.0 — Scope and vocabulary control | ATA 00-00-01 | `<sha256: TBS>` | `DMC-<PROG>-000-000-001` |
| `002` | `000-000-002-…-Mission.md` | MDC Art. 2 — Mission and foundational values | ATA 00-00-02 | `<sha256: TBS>` | `DMC-<PROG>-000-000-002` |
| `003` | `000-000-003-…-Agnosticism.md` | DEGF v1.0 — Agnosticism principle | ATA 00-00-03 | `<sha256: TBS>` | `DMC-<PROG>-000-000-003` |
| `004` | `000-000-004-…-Use.md` | DEGF v1.0 — Navigation and usage guide | ATA 00-00-04 | `<sha256: TBS>` | `DMC-<PROG>-000-000-004` |
| `005` | `000-000-005-…-Numbering.md` | DEGF v1.0 — Numbering convention | ATA 00-00-05; iSpec 2200 SNS rules | `<sha256: TBS>` | `DMC-<PROG>-000-000-005` |
| `006` | `000-000-006-…-ATA-iSpec.md` | DEGF v1.0 — Standards alignment | ATA 100; iSpec 2200; S1000D Issue 4.2 | `<sha256: TBS>` | `DMC-<PROG>-000-000-006` |
| `007` | `000-000-007-…-Control.md` | DEGF v1.0 — Document control; MDC Art. 4 | SSOT+PUB doctrine; IEF | `<sha256: TBS>` | `DMC-<PROG>-000-000-007` |
| `008` | `000-000-008-…-Index.md` (this) | DEGF v1.0 — Evidence index | IEF; S1000D DMC rules | `<sha256: TBS>` | `DMC-<PROG>-000-000-008` |

> **TBS** — To Be Stamped at formal baseline by Q-DATAGOV IEF tooling.
> **MDC** — Model Digital Constitution (`00_MODEL-DIGITAL-CONSTITUTION/`).
> **`<PROG>`** — Replace with programme identifier (e.g. `EWTW`, `HBWB`) in programme CSDB.

---

## 4. Evidence Anchor Protocol

At each formal baseline event:

1. Q-DATAGOV computes `SHA-256(<file-content>)` for each item.
2. The hash is recorded in the item's `ief_anchor` front-matter block.
3. The hash is also recorded in this index (column *IEF anchor*) and in the band-level evidence register.
4. The baseline timestamp and authorising officer are appended to the item's change log.

Anchors marked `<sha256: TBS>` indicate the item is approved in content but awaiting the formal stamping ceremony.

---

## 5. DMC Mapping Notes

| Rule | Detail |
|---|---|
| Short-form DMC | `DMC-<PROG>-<node>-<item>` — for internal cross-referencing |
| Full S1000D DMC | Constructed by the programme at PUB stage (adds MIC, disassembly code, info code, applicability) |
| Issue alignment | S1000D Issue 4.2 baseline; programme may adopt later issue in PUB without SSOT amendment |
| SNS alignment | Node prefix `00X` aligns to S1000D SNS system `0X`; sub-system and subject codes follow item numbering |

---

## 6. Upstream Evidence References

| Upstream artefact | Location | Relevance |
|---|---|---|
| Model Digital Constitution | `00_MODEL-DIGITAL-CONSTITUTION/` | Constitutional authority for G-ATLAS |
| DEGF v1.0 | `000-099_G-ATLAS/README.md` (band) | Eleven mandatory inheritance traits |
| SSOT+PUB doctrine | `000-000-007` (item 007) | Change-control and publication rules |
| IEF (Integrity Evidence Framework) | `01-07-04-03_EVIDENCE-AND-PROVENANCE-IEF/` | Evidence anchoring scheme |
| ATA 100 / iSpec 2200 | `01-07-02-02_ATA-iSpec-2200/` | Numbering and structure reference |
| S1000D Issue 4.2 | `01-07-02-01_S1000D/` | Data module and DMC rules |

---

```yaml
Last.MarkedDown:
  node: 000-000
  item: "008"
  ata_ref: 00-00-08
  file: 000-000-008-Traceability-and-Evidence-Index.md
  owner: Q-DATAGOV
  status: baseline
  ief_anchor:
    sha256: <to-be-stamped-at-baseline>
    stamped_at: <ISO-8601 timestamp>
    stamped_by: Q-DATAGOV
  .YieldedAlgorithmicMachineLearning: true
```
