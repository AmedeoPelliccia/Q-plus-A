---
status: draft
standard_scope: governance
---

# AMPEL360 — Programme

**Location:** `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/`
**Version:** 0.1.0 · **Date:** 2026-11-12

AMPEL360 is a family of four aircraft models on one identity system: S-ATLAS addresses above the assembly station, configuration-controlled part numbers below it.

| Folder | Role | On disk at this date |
|---|---|---|
| [`01-02-01-01_MODELS`](01-02-01-01_MODELS/) | One node per model: breakdown structures, decisions, relations | eWTW developed; MRTT-Q300 concept README; BWB-Q100 SBS scaffold; Q10 not yet written |
| [`01-02-01-02_CERTIFICATION`](01-02-01-02_CERTIFICATION/) | Certification | README not yet written |
| [`01-02-01-03_LIFECYCLE-GATES`](01-02-01-03_LIFECYCLE-GATES/) | Lifecycle gates | README not yet written |
| [`01-02-01-04_IMPACT-STUDIES`](01-02-01-04_IMPACT-STUDIES/) | Impact studies | README not yet written |

## Decisions that hold across models

| Decision | Record | State |
|---|---|---|
| The eWTW is all-electric, or hybrid-electric with conventional fuel, and carries no hydrogen. Liquid hydrogen is assigned to the BWB-Q100 | Ruling R1 of [`KNOT-EWTW-NRG-001`][NRG], 2026-11-07 | `PROVISIONAL`: rationale and evidence not yet recorded |

Programme relations — what is assigned to a model, excluded from it or admitted in combination — are recorded in [`programme-relations.yaml`][PROG-REL] under [`AMPEL360-REL-CM-005`][CM-005]. The file sits in the eWTW model while the eWTW pilot is its only content.

## Conventions

Those on disk are held in the eWTW model, where they were first applied.

| Convention | Governs | Status |
|---|---|---|
| [`AMPEL360-PBS-PN-CM-001`][CM-001] Issue 2 | Assembly station, identity boundary, part numbers | On `main`; the header reads *PROPOSED* and names no approval act |
| [`AMPEL360-SBS-ID-CM-002`][CM-002] Issue 1 | Identification across the breakdown structures | On `main`; the header reads *PROPOSED* and names no approval act |
| `AMPEL360-SBS-LC-CM-003` | Artefact lifecycle in the SBS; integrated baselines | Not on `main` |
| [`AMPEL360-KNOT-CM-004`][CM-004] Issue 1 | Knowledge nodes and knowledge units | *PROPOSED* |
| [`AMPEL360-REL-CM-005`][CM-005] Issue 1 | Architecture relations and their projection onto a KNOT register | *PROPOSED* |

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-12 | First content: folders as found on disk; the cross-model decision and its record; the five conventions |

[NRG]: 01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-02_KNOT_Knowledge-Node-Register/000_General/KNOT-EWTW-NRG-001.yaml
[PROG-REL]: 01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-03_REL_Architecture-Relations/programme-relations.yaml
[CM-001]: 01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/AMPEL360-PBS-PN-CM-001_Assembly-Station-and-Part-Number-Breakdown.md
[CM-002]: 01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/AMPEL360-SBS-ID-CM-002_Cross-Structure-Identification.md
[CM-004]: 01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-02_KNOT_Knowledge-Node-Register/AMPEL360-KNOT-CM-004_Knowledge-Nodes-and-Units.md
[CM-005]: 01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-03_REL_Architecture-Relations/AMPEL360-REL-CM-005_Architecture-Relations.md
