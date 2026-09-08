---
status: draft
standard_scope: governance
---

# eWTW — Cost Breakdown Structure (CBS)

<!-- Generated 2026-09-06 - GitHub Copilot - SBS rework under CM-002 -->

## Purpose

The CBS controls the cost objects of the eWTW programme: recurring cost carried by the things that are made or bought, and non-recurring cost carried by the work that is performed. It exists so that cost is accounted exactly once, on the object that incurs it, and rolled up along the structures that already exist — the PBS for recurring cost, the WBS for non-recurring cost — instead of maintaining a third, parallel tree of cost lines.

## Id grammar (CM-002 §3)

> | **CBS** (recurring) | derived | `eWTW-CBS-<CSN>-<item>` | is the id | 1:1 with a make/buy item |
> | **CBS** (non-recurring) | sovereign | `eWTW-CBS-<WBS id>` | `incurredBy:` | n:m with work |

Recurring cost objects are views over product items: the id is derived from the CSN and is regenerated, never typed (CM-002 §4.2). Non-recurring cost objects keep a sovereign id keyed to the WBS and bind through a typed reference.

## References into the PBS

A recurring cost object references its make/buy item **by its derived id** (the embedded CSN and item resolve to the part-number tree of a station). It holds no engineering content of its own: per CM-002 §4.4 a cost object may not restate a quantity — it reads it from `part.yaml`.

## Trigger

The workstream opens when the first make/buy decision is recorded against a realized station (chapter 053 today), or when the first WBS work package requires non-recurring cost capture. Until then no cost figure is authored here — inventing one would violate the no-fabrication rule of the governing brief.

## Status

**STUB — no depth authored.**
