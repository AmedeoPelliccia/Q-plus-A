# 01-02-01-01-01-01-11 — TPuBS — Technical Publications Breakdown Structure (eWTW)

> **Canonical path**
> `…/01-02-01_AMPEL360/01-02-01-01_PRODUCTS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure/`
>
> **Programme:** AMPEL360 · **Product:** eWTW (electric wide tube-and-wing) · **Side:** PUB
> **Sibling of:** `…-01_PBS_Product-Breakdown-Structure` (SSOT-side)
> **Organising taxonomy:** `000-099_G-ATLAS` (SNS) · **Standard:** S1000D Issue 4.2

## 1. What this is

The **TPuBS** is the eWTW **publications** breakdown — an S1000D **CSDB** holding every technical-publication object for the product. It is the **PUB** counterpart to the **PBS** (SSOT-side product breakdown). Where the PBS answers *"what is the aircraft?"*, the TPuBS answers *"what do we publish about it, and where is the evidence?"*

Publications are **no longer nested inside the PBS**. Each `PUB` that previously lived under a PBS leaf (e.g. `eWTW-PBS-10-10-10_Forward-Fuselage-Section/PUB`) is relocated here. See `_MOVE-RECORD.md`.

## 2. Organising principle

Publications are filed by the **G-ATLAS Standard Numbering System** (the same `master range → chapter → node/code-section` grammar as the standard), restricted to the **ATLAS master ranges and node sections impacted** by the eWTW product. Each impacted node section carries the seven S1000D object classes.

## 3. The seven object classes (per impacted node section)

| Folder | S1000D object | Role |
|---|---|---|
| `APPLIC/` | Applicability model (ACT / CCT / PCT) | Which product/config a DM applies to |
| `BREX/` | Business Rules Exchange DM | Project business rules the DMs must satisfy |
| `DM/` | Data Modules | The content units (descriptive, procedural, fault, IPD) |
| `DMRL/` | Data Module Requirement List | The planned/required set of DMs (completeness) |
| `ICN/` | Information Control Number objects | Graphics & multimedia referenced by DMs |
| `PM/` | Publication Modules | Assemble DMs into deliverable publications |
| `SSOT/` | Single-Source-of-Truth manifest | Traceability back to the G-ATLAS standard node/item |

> **S1000D note:** `BREX`, `DMRL` and the `APPLIC` model are conventionally **project-wide singletons** (one BREX, one applicability model, one DMRL per publication). They are reproduced per node section here for per-node traceability; if you prefer, hoist them to a `_PROJECT/` folder at the TPuBS root — say the word and I'll refactor.

## 4. Impacted ATLAS set — Forward Fuselage Section

Master ranges and node sections impacted by `eWTW-PBS-10-10-10_Forward-Fuselage-Section`:

| Master range | Node section | ATA | Impact | Built |
|---|---|---|---|:--:|
| `050-059_Estructuras` | `053-100` Forward Fuselage Section | 53-10 | **Primary** | ✅ |
| `000-009_General-Information-and-Service` | `000-000` General / Introduction | 00-00 | Identification, general | pattern |
| `000-009_General-Information-and-Service` | `006-200` Stations, Zones & Areas | 06-20 | Fuselage stations | pattern |
| `000-009_General-Information-and-Service` | `007-100` Jacking Points | 07-10 | Jacking on fwd fuselage | pattern |
| `000-009_General-Information-and-Service` | `008-100` Weighing & Balancing | 08-10 | Mass/CG contribution | pattern |

The `053-100` node is fully instantiated below as the worked pattern; the others follow it identically.

## 5. Governance

PBS (SSOT) ⇄ TPuBS (PUB) under the **SSOT+PUB** doctrine. Inherits **DEGF v1.0**; governed across **LC01–LC14**; **No-AAA** applies. Each node section's `SSOT/` folder is the binding back to the standard.

```yaml
Last.MarkedDown:
  structure: TPuBS
  code: 01-02-01-01-01-01-11
  programme: AMPEL360
  product: eWTW
  side: PUB
  standard: S1000D-Issue-4.2
  sns_taxonomy: 000-099_G-ATLAS
  object_classes: [APPLIC, BREX, DM, DMRL, ICN, PM, SSOT]
  primary_impact: 050-059_Estructuras/053-100
  status: baseline
  .YieldedAlgorithmicMachineLearning: true
```
