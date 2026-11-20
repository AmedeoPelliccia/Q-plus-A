---
status: draft
standard_scope: governance
---

# AMPEL360 — Models

**Location:** `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/`
**Version:** 0.1.1 · **Date:** 2026-11-14

| Folder | Model | On disk at this date |
|---|---|---|
| [`01-02-01-01-01_eWTW`](01-02-01-01-01_eWTW/README.md) | Electric Wide Tube and Wing, 100 passengers. Conventional fuel in a thermal machine that generates electricity, with or without a propulsion battery; batteries alone excluded until reopened (ruling R2) | Model README 0.3.30; SBS with eleven views; KNOT register 0.11.21 — 22 KNOTs, 67 KNUs; architecture relations 0.3.2 |
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
| Liquid hydrogen is assigned to the BWB-Q100 and excluded from the eWTW | Ruling R1 of `KNOT-EWTW-NRG-001`, `COMPLETE` since 2026-11-14 | The BWB-Q100 README does not yet state it |
| The MRTT-Q300 targets commonality with the eWTW family under a liquid-hydrogen baseline | `KNOT-MRTT-CMA-001`, in the MRTT-Q300 README | The eWTW no longer offers that premise. To be revisited in the MRTT-Q300 model |

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-12 | First content: the four models as found on disk; the three nodes of a model; the two couplings between models |
| 0.1.1 | 2026-11-14 | The eWTW row follows its nodes: KNOT register 0.9.0 with three more KNOTs for the 3D models, proposed criteria for essential power and for the energy carrier, five options and a load analysis for essential power, missions and required maturity for the energy carrier, approved by ruling R2; architecture relations 0.3.0 |
