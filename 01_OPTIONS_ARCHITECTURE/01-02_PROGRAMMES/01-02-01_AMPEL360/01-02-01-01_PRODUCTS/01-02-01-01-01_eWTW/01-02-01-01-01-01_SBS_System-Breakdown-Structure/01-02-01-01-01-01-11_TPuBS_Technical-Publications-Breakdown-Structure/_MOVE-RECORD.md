# `_MOVE-RECORD.md` — PUB → TPuBS relocation

> Records the relocation of eWTW publication objects out of the PBS and into the
> **TPuBS — Technical Publications Breakdown Structure** (`01-02-01-01-01-01-11`).
> Publications are **no longer nested inside the PBS**.

## What moved

| From (PBS leaf) | To (TPuBS node section) |
|---|---|
| `…/eWTW-PBS-10-10-10_Forward-Fuselage-Section/PUB/DM/*.xml` | `000-099_G-ATLAS/050-059_Estructuras/053_Fuselage/053-100_Forward-Fuselage-Section/DM/` |
| `…/eWTW-PBS-10-10-10_Forward-Fuselage-Section/PUB/PM/*` | `000-099_G-ATLAS/050-059_Estructuras/053_Fuselage/053-100_Forward-Fuselage-Section/PM/` |
| `…/eWTW-PBS-10-10-10_Forward-Fuselage-Section/PUB/{APPLIC,BREX,DMRL,ICN}/` | seeded under `053-100_Forward-Fuselage-Section/` (same object classes) |

### Radome part — `pub/` relocated (corrected migration)

| From (PBS leaf) | To (TPuBS part) |
|---|---|
| `…_Radome/LC-A_Concept-Design/pub/040_descriptive/` | `…/053-100_Forward-Fuselage-Section/053-100-100_Nose-Structure-and-Radome-Backup/053-100-100-001_Radome/DM/040_descriptive/` |
| `…_Radome/LC-A_Concept-Design/pub/258_bonding-and-lightning-check/` | `…/053-100-100-001_Radome/DM/258_bonding-and-lightning-check/` |
| `…_Radome/LC-A_Concept-Design/pub/310_inspection-general/` | `…/053-100-100-001_Radome/DM/310_inspection-general/` |
| `…_Radome/LC-A_Concept-Design/pub/520_removal/` | `…/053-100-100-001_Radome/DM/520_removal/` |
| `…_Radome/LC-A_Concept-Design/pub/720_installation/` | `…/053-100-100-001_Radome/DM/720_installation/` |
| `…_Radome/LC-A_Concept-Design/pub/941_illustrated-parts-data/` | `…/053-100-100-001_Radome/DM/941_illustrated-parts-data/` |
| `…_Radome/LC-A_Concept-Design/pub/README.md` | `…/053-100-100-001_Radome/PUB-Layer-Notes.md` |

The Radome `pub/` content lands **flat** in `DM/` (info-code folders only — **no `LC-*`/`REV-*` nesting**). Engineering lifecycle/revision states are referenced (not nested) in `…/053-100-100-001_Radome/PUB-BASELINES/PUB-BL-0001/*.yaml`. The PBS `pub/` folder is removed and replaced by a `pub.link` pointer at `…_Radome/LC-A_Concept-Design/pub.link`.

The old `…/eWTW-PBS-10-10-10_Forward-Fuselage-Section/PUB/` folder is removed; its
publication content now lives under the TPuBS, filed by the **G-ATLAS SNS**.

## Mapping rule

`eWTW-PBS-10-10-10` (Forward Fuselage Section) ⇄ G-ATLAS node `050-059_Estructuras/053_Fuselage/053-100`
(⇄ ATA 53-10). Below the node the ×10 SNS grammar continues for the sub-assembly
(`eWTW-PBS-10-10-10-10` ⇄ `053-100-100`, ATA 53-10-10) and parts use **sequential**
identifiers (`eWTW-PBS-10-10-10-10-10_Radome` ⇄ `053-100-100-001`, ATA 53-10-10-01).
The PBS-side `SSOT/` folder **stays** in the PBS leaf (engineering
truth); the publication projection moves here (PUB side) and references the SSOT.

## Object classes per node section

Node: `APPLIC` · `BREX` · `DMRL` · `IMPACT` · `PM` · `SSOT`
Part: `SSOT` · `APPLIC` · `IMPACT` · `DM` (flat) · `ICN` · `PM` · `PUB-BASELINES`

## Impacted set (Forward Fuselage Section)

| Master range | Node section | ATA | Built |
|---|---|---|:--:|
| `050-059_Estructuras` | `053-100` Forward Fuselage Section | 53-10 | ✅ instantiated |
| `050-059_Estructuras` | `053-100-100-001` Radome (part) | 53-10-10-01 | ✅ instantiated |
| `000-009_General-Information-and-Service` | `000-000` General / Introduction | 00-00 | pattern |
| `000-009_General-Information-and-Service` | `006-200` Stations, Zones & Major Areas | 06-20 | pattern |
| `000-009_General-Information-and-Service` | `007-100` Jacking Points | 07-10 | pattern |
| `000-009_General-Information-and-Service` | `008-100` Weighing & Balancing | 08-10 | pattern |
