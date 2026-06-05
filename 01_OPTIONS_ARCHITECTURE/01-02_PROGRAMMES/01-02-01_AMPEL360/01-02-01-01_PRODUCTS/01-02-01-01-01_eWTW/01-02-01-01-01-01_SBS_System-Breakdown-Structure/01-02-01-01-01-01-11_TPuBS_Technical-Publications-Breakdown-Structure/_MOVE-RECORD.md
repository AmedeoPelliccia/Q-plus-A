# `_MOVE-RECORD.md` — PUB → TPuBS relocation

> Records the relocation of eWTW publication objects out of the PBS and into the
> **TPuBS — Technical Publications Breakdown Structure** (`01-02-01-01-01-01-11`).
> Publications are **no longer nested inside the PBS**.

## What moved

| From (PBS leaf) | To (TPuBS node section) |
|---|---|
| `…/eWTW-PBS-10-10-10_Forward-Fuselage-Section/PUB/DM/*.xml` | `050-059_Estructuras/053-100_Forward-Fuselage-Section/DM/` |
| `…/eWTW-PBS-10-10-10_Forward-Fuselage-Section/PUB/PM/*` | `050-059_Estructuras/053-100_Forward-Fuselage-Section/PM/` |
| `…/eWTW-PBS-10-10-10_Forward-Fuselage-Section/PUB/{APPLIC,BREX,DMRL,ICN}/` | seeded under `053-100_Forward-Fuselage-Section/` (same object classes) |

The old `…/eWTW-PBS-10-10-10_Forward-Fuselage-Section/PUB/` folder is removed; its
publication content now lives under the TPuBS, filed by the **G-ATLAS SNS**.

## Mapping rule

`eWTW-PBS-10-10-10` (Forward Fuselage Section) ⇄ G-ATLAS node `050-059_Estructuras/053-100`
(⇄ ATA 53-10). The PBS-side `SSOT/` folder **stays** in the PBS leaf (engineering
truth); the publication projection moves here (PUB side) and references the SSOT.

## Object classes per node section

`APPLIC` · `BREX` · `DM` · `DMRL` · `ICN` · `PM` · `SSOT`

## Impacted set (Forward Fuselage Section)

| Master range | Node section | ATA | Built |
|---|---|---|:--:|
| `050-059_Estructuras` | `053-100` Forward Fuselage Section | 53-10 | ✅ instantiated |
| `000-009_General-Information-and-Service` | `000-000` General / Introduction | 00-00 | pattern |
| `000-009_General-Information-and-Service` | `006-200` Stations, Zones & Major Areas | 06-20 | pattern |
| `000-009_General-Information-and-Service` | `007-100` Jacking Points | 07-10 | pattern |
| `000-009_General-Information-and-Service` | `008-100` Weighing & Balancing | 08-10 | pattern |
