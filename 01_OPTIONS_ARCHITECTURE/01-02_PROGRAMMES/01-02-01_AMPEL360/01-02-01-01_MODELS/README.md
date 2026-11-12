---
status: draft
standard_scope: governance
---

# AMPEL360 — Models

**Location:** `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/`
**Version:** 0.1.0 · **Date:** 2026-11-12

| Folder | Model | On disk at this date |
|---|---|---|
| [`01-02-01-01-01_eWTW`](01-02-01-01-01_eWTW/README.md) | Electric Wide Tube and Wing, about 100 passengers. All-electric, or hybrid-electric with conventional fuel | Model README 0.3.3; SBS with eleven views; KNOT register 0.5.0 — 14 KNOTs, 41 KNUs; architecture relations 0.1.1 |
| [`01-02-01-01-02_BWB-Q100`](01-02-01-01-02_BWB-Q100/) | Blended wing body. The model assigned liquid hydrogen | SBS scaffold. README not yet written; the node is a protected area, so writing it is an act of its author |
| [`01-02-01-01-03_MRTT-Q300`](01-02-01-01-03_MRTT-Q300/README.md) | Medical · Relief · Tanker · Transport: a humanitarian-only wide-body relief aircraft | Concept README 0.3.0 |
| [`01-02-01-01-04_Q10`](01-02-01-01-04_Q10/) | Q10 | README not yet written |

## What a model node holds

| Node | Holds | Convention |
|---|---|---|
| `…-01_SBS_System-Breakdown-Structure` | The breakdown views over one identity system | `AMPEL360-PBS-PN-CM-001` · `AMPEL360-SBS-ID-CM-002` |
| `…-02_KNOT_Knowledge-Node-Register` | What the model must decide or satisfy, and the knowledge units that resolve it | `AMPEL360-KNOT-CM-004` (proposed) |
| `…-03_REL_Architecture-Relations` | Taxonomy and programme relations, projected onto the KNOT register | `AMPEL360-REL-CM-005` (proposed) |

The eWTW holds all three. The conventions are listed with their status in the [programme README](../README.md#conventions).

## Couplings between models

| Coupling | Record | Open point |
|---|---|---|
| Liquid hydrogen is assigned to the BWB-Q100 and excluded from the eWTW | Ruling R1 of `KNOT-EWTW-NRG-001`, `PROVISIONAL` | The BWB-Q100 README does not yet state it |
| The MRTT-Q300 targets commonality with the eWTW family under a liquid-hydrogen baseline | `KNOT-MRTT-CMA-001`, in the MRTT-Q300 README | The eWTW no longer offers that premise. To be revisited in the MRTT-Q300 model |

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-12 | First content: the four models as found on disk; the three nodes of a model; the two couplings between models |
