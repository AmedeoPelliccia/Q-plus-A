---
status: draft
standard_scope: governance
---

# eWTW — Technical Performance Measurement Structure (TPMS)

<!-- Generated 2026-09-06 - GitHub Copilot - SBS rework under CM-002 -->

## Purpose

The TPMS controls the technical performance measures of the eWTW: the quantified characteristics — mass, power, range, structural margins — whose planned, current and demonstrated values are tracked over the life cycle. A measure of a product scope has exactly one subject and is numbered after it; a programme-level measure spans many products and keeps its own identity with a typed scope.

## Id grammar (CM-002 §3)

> | **TPMS** (product measures) | derived | `TPM-<CSN>-<MEASURE>` | is the id | 1:1 with a product scope |
> | **TPMS** (programme measures) | sovereign | `TPM-PROG-<MEASURE>` | `scope:` | 1:n |

Product measures are derived views — the id embeds the CSN and regenerates with it (CM-002 §4.2). Programme measures are sovereign and bind through `scope:`.

## References into the PBS

A product measure references the PBS **by its derived id**: the CSN segment resolves to a station (for example a mass measure on the rear-fuselage zone would carry CSN `533001`, resolving to `eWTW-PBS-053-300-010`). A programme measure references the PBS through its **`scope:`** field — a list of resolvable node ids. Per CM-002 §4.4 a measure never restates the value recorded in `part.yaml`; it tracks planned versus demonstrated against it.

## Trigger

The workstream opens when the first measure is levied with a planned value and an owner — the natural first candidate is a mass-properties measure on chapter 053, whose stations already exist to carry it. Until then no measure, target or margin is authored here: an invented target value would be fabricated depth.

## Layout

One root folder, `eWTW-TPMS-000_Aircraft-Measures`, as the PBS has `eWTW-PBS-000_Aircraft-Product`. The measures of one product node — the aircraft, a system, a station — are one file in that folder, named after the node: `EWTW-000` for the aircraft, the CSN for a station. The PBS is mirrored in the file names, not in folders. A product measure keeps its derived id. A set is opened when its first record exists: no empty set mirrors the PBS ([CM-002](../AMPEL360-SBS-ID-CM-002_Cross-Structure-Identification.md), clarification C2.1).

## Status

**PILOT — first product measures recorded.** Each measure is read from committed evidence with the sha256 of its source; the geometry of record and its verification report are named per station. Targets are null except where the authority levied one.

**Sets**, in [`eWTW-TPMS-000_Aircraft-Measures`](eWTW-TPMS-000_Aircraft-Measures/README.md):

- [`TPM-CANDIDATES_EWTW-000.yaml`](eWTW-TPMS-000_Aircraft-Measures/TPM-CANDIDATES_EWTW-000.yaml) — the aircraft, `eWTW-PBS-000`: four candidates read from the mission screening and the essential load analysis of 2026-11-14, each a first-order estimate with its band. No measure is levied; the id of a measure of the whole aircraft is open, because the product root has no CSN.
- [`TPM_EWTW-533001.yaml`](eWTW-TPMS-000_Aircraft-Measures/TPM_EWTW-533001.yaml) — rear-fuselage zone, `eWTW-PBS-053-300-010`: `TPM-533001-MASS`, `-PARTS` and `-INTERF` (current 1, target 0 — the geometry of record fails its own interference check).
