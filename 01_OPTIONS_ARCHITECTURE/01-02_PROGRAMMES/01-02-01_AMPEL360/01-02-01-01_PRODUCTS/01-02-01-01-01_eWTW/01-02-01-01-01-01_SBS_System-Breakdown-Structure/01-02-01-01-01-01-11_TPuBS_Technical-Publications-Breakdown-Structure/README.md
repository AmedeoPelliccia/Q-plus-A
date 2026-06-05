# 01-02-01-01-01-01-11 — TPuBS — Technical Publications Breakdown Structure (eWTW)

> **Canonical path**
> `…/01-02-01_AMPEL360/01-02-01-01_PRODUCTS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure/`
>
> **Programme:** AMPEL360 · **Product:** eWTW (electric wide tube-and-wing) · **Side:** PUB
> **Sibling of:** `…-01_PBS_Product-Breakdown-Structure` (SSOT-side)
> **Organising taxonomy:** `000-099_G-ATLAS` (SNS) · **Standard:** S1000D Issue 4.2

## 1. What this is

The **TPuBS** is the eWTW **publications** breakdown — an S1000D **CSDB** holding every technical-publication object for the product. It is the **PUB** counterpart to the **PBS** (SSOT-side product breakdown). Where the PBS answers *"what is the aircraft?"*, the TPuBS answers *"what do we publish about it, and where is the evidence?"*

Publications are **no longer nested inside the PBS**. Each `pub/`/`PUB` that previously lived under a PBS leaf (e.g. `eWTW-PBS-10-10-10_Forward-Fuselage-Section/PUB` and `…_Radome/LC-A_Concept-Design/pub/`) is relocated here. See `_MOVE-RECORD.md`.

## 2. Governing doctrine — SSOT+PUB separation

```text
Engineering revision  ≠  publication revision.
Engineering lifecycle ≠  publication lifecycle.
Engineering change    →  impact analysis  →  publication change only if required.
```

Publications are controlled by a **publication baseline / issue cycle** (`PUB-BASELINES/`). They **reference** engineering LC/REV, effectivity, and impact-analysis state — they are **never nested inside** engineering lifecycle (`LC-*`) or revision (`REV-*`) folders. A design revision change (e.g. `REV-A1 → REV-A2`) requires a publication change **only when** an `IMPACT/` analysis concludes the engineering change affects published content.

Consequently `DM/` is a **flat pool of info-code folders** — no `LC-*`/`REV-*` nesting. Engineering states are linked in `PUB-BASELINES/` YAML.

## 3. Organising principle

Publications are filed by the **G-ATLAS Standard Numbering System** under a `000-099_G-ATLAS/` root, following the standard's `master range → chapter → node/code-section` grammar and continuing below the node:

| Level | Code pattern | Scaling | Example | ATA / SNS |
|---|---|---|---|---|
| Chapter | `0CC` | chapter = ATA CC | `053` | 53 |
| Node / code section | `0CC-S00` | section ×10 | `053-100` | 53-10 |
| Sub-assembly | `<node>-S00` | ×10 **continues** | `053-100-100` | 53-10-10 |
| Part | `<sub-assy>-NNN` | **sequential** | `053-100-100-001` | 53-10-10-01 |

## 4. Object classes — node level vs part level

| Folder | Node (`053-100`) | Part (`053-100-100-001`) | Role |
|---|:--:|:--:|---|
| `SSOT/` | ✓ | ✓ | Traceability manifest → G-ATLAS standard + PBS |
| `APPLIC/` | ✓ | ✓ | Applicability model (ACT / CCT / PCT) |
| `BREX/` | ✓ | — | Business Rules Exchange DM (scopes the chapter-section) |
| `DMRL/` | ✓ | — | Data Module Requirement List (completeness) |
| `IMPACT/` | ✓ | ✓ | Impact-analysis records (engineering change → publication impact?) |
| `PM/` | ✓ | ✓ | Publication Modules (assembly) |
| `DM/` | — | ✓ | Data Modules — **flat** info-code folders |
| `ICN/` | — | ✓ | Graphics & multimedia (flat pool, by ICN id) |
| `PUB-BASELINES/` | — | ✓ | Publication baseline / issue records (YAML); links engineering baselines |

> **S1000D note:** `BREX`, `DMRL` and the `APPLIC` model are conventionally **project-wide singletons**. They are reproduced per node here for per-node traceability; they can be hoisted to a `_PROJECT/` folder at the TPuBS root if preferred.

## 5. Impacted ATLAS set — Forward Fuselage Section

Master ranges and node sections impacted by `eWTW-PBS-10-10-10_Forward-Fuselage-Section` (and the Radome part beneath it):

| Master range | Node section | ATA | Impact | Built |
|---|---|---|---|:--:|
| `050-059_Estructuras` | `053-100` Forward Fuselage Section | 53-10 | **Primary** | ✅ |
| └ part | `053-100-100-001` Radome | 53-10-10-01 | **Primary part** (pub relocated) | ✅ |
| `000-009_General-Information-and-Service` | `000-000` General / Introduction | 00-00 | Identification, general | pattern |
| `000-009_General-Information-and-Service` | `006-200` Stations, Zones & Areas | 06-20 | Fuselage stations | pattern |
| `000-009_General-Information-and-Service` | `007-100` Jacking Points | 07-10 | Jacking on fwd fuselage | pattern |
| `000-009_General-Information-and-Service` | `008-100` Weighing & Balancing | 08-10 | Mass/CG contribution | pattern |

The `053-100` node and the `053-100-100-001` Radome part are fully instantiated; the others follow the same pattern.

## 6. Governance

PBS (SSOT) ⇄ TPuBS (PUB) under the **SSOT+PUB** doctrine. The Q+ATLANTIDE lifecycle uses **LC-letter stages (LC-A … LC-N)**; publication baselines reference those engineering stages but are not governed by them. Each node's and part's `SSOT/` folder is the binding back to the standard.

```yaml
Last.MarkedDown:
  structure: TPuBS
  code: 01-02-01-01-01-01-11
  programme: AMPEL360
  product: eWTW
  side: PUB
  standard: S1000D-Issue-4.2
  sns_taxonomy: 000-099_G-ATLAS
  object_classes: [APPLIC, BREX, DM, DMRL, ICN, PM, SSOT, IMPACT, PUB-BASELINES]
  primary_impact: 000-099_G-ATLAS/050-059_Estructuras/053_Fuselage/053-100
  primary_part: 053-100-100-001_Radome
  doctrine: SSOT+PUB-separation (engineering rev ≠ publication rev)
  status: baseline
  .YieldedAlgorithmicMachineLearning: true
```
