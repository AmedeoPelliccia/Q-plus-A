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

## Status

**STUB — no depth authored.**
