---
status: draft
standard_scope: governance
---

# 01-02 — Programmes

**Location:** `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/`
**Version:** 0.1.0 · **Date:** 2026-11-12

A programme applies the [Q+ATLANTIDE](../01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/) taxonomy to products. It states its mission, its models and the decisions that hold across them. Each model then holds its own breakdown structures and decision records. A programme mints no taxonomy: it refers to taxonomy addresses.

| Folder | Programme | On disk at this date |
|---|---|---|
| [`01-02-01_AMPEL360`](01-02-01_AMPEL360/) | AMPEL360 — a family of four aircraft models | The eWTW is the developed model: SBS, KNOT register, architecture relations |
| [`01-02-02_GAIA-AIR`](01-02-02_GAIA-AIR/) | GAIA-AIR | Folder scaffold. README not yet written |
| [`01-02-03_GAIA-SPACE`](01-02-03_GAIA-SPACE/) | GAIA-SPACE — space research, exploration and technology | Programme README and a proposed charter |
| [`01-02-04_ROBBBO-T`](01-02-04_ROBBBO-T/) | ROBBBO-T | Folder scaffold. README not yet written |

## What is recorded at which level

| Level | Holds | Example |
|---|---|---|
| Taxonomy | What is true of a technology for any programme | A propulsion battery requires thermal management |
| Programme | What the programme assigns, excludes or admits across its models | Liquid hydrogen is assigned to the BWB-Q100 |
| Model | What the model must decide, and the work that resolves it | `KNOT-EWTW-SRC-001`: which electrical sources |
| Product | What holds of a configured element | A station realizes an S-ATLAS address |

The levels and their relations are defined in [`AMPEL360-REL-CM-005`][CM-005] (proposed), piloted on the eWTW.

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-12 | First content: the four programmes as found on disk; the four levels of record |

[CM-005]: 01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-03_REL_Architecture-Relations/AMPEL360-REL-CM-005_Architecture-Relations.md
