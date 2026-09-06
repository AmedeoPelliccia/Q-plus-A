---
status: draft
standard_scope: governance
---

# eWTW — Risk Breakdown Structure (RBS)

<!-- Generated 2026-09-06 - GitHub Copilot - SBS rework under CM-002 -->

## Purpose

The RBS controls the risk register of the eWTW programme: technical, schedule and integration risks, each carried as a governed record with its own identity and life cycle. A risk is not a property of a part — it spans items, interfaces and work — so the register keeps its own identifier space and binds to the product through references, not through numbering.

## Id grammar (CM-002 §3)

> | **RBS** | sovereign | `R-<CSN>-<seq>` when the risk is confined to one station, else `R-<seq>` | `affects:` | 1:1 or n:m |

RBS is the instructive middle case of CM-002: a risk confined to one station may carry the CSN for legibility (`R-533001-02`), but the field that binds is `affects:` — the day the risk widens, the id stays and the reference list grows.

## References into the PBS

A risk record references the product through its **`affects:`** list: PBS node ids (chapter, section or station) or part numbers, every entry resolvable on disk (CM-002 §4.1). No risk score or mitigation text restates product data; the record points at what it threatens.

## Trigger

The workstream opens when the first risk is formally raised against a realized item — the natural first candidates are the rear-fuselage-zone declarations already marked as not yet demonstrated (the zone-level rear-pressure-bulkhead load path). Until a risk is raised by the owning authority, no risk entry is authored here — a fabricated risk score would be depth this stub is forbidden to invent.

## Status

**STUB — no depth authored.**
