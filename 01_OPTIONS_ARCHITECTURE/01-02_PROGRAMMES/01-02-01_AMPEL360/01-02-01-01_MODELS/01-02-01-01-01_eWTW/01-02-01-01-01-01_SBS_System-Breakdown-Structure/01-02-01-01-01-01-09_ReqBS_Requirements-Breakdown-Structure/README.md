---
status: draft
standard_scope: governance
---

# eWTW — Requirements Breakdown Structure (ReqBS)

<!-- Generated 2026-09-06 - GitHub Copilot - SBS rework under CM-002 -->

## Purpose

The ReqBS controls the requirements of the eWTW: what the aircraft, its systems and its structures shall do and shall withstand, each requirement a governed record with its own identity, allocation and satisfaction trail. A requirement is allocated to several product elements and satisfied by evidence from elsewhere — an n:m graph — so the ReqBS keeps a sovereign identifier space and never numbers itself after the product tree.

## Id grammar (CM-002 §3)

> | **ReqBS** | sovereign | `REQ-<level>-<seq>` | `allocatedTo:` + `satisfies:` (function) | **n:m** |

Sovereign ids never change (CM-002 §4.2); the binding lives in the reference fields, not in the identifier.

## References into the PBS

A requirement references the product through its **`allocatedTo:`** list — PBS node ids (chapter `eWTW-PBS-050`, sections such as `eWTW-PBS-053-300-000`, stations such as `eWTW-PBS-053-300-010`) or part numbers — and references the function tree through **`satisfies:`** (FBS ids). Every entry must resolve on disk (CM-002 §4.1); a dangling allocation is a preflight fatal, exactly as in the PBS engines.

## Trigger

The workstream opens when the first requirement is formally levied on a realized item — the natural first candidates are structural requirements on chapter 053, whose stations and part numbers already exist to receive allocations. Until the owning authority levies one, no requirement text is authored here: fabricated requirement wording is depth this stub is forbidden to invent.

## Layout

One root folder, `eWTW-ReqBS-000_Aircraft-Requirements`, as the PBS has `eWTW-PBS-000_Aircraft-Product`. The requirements levied on one product node — the aircraft, a system, a station — are one file in that folder, named after the node: `EWTW-000` for the aircraft, the PBS-local code for a group or a chapter, the CSN for a station. The PBS is mirrored in the file names, not in folders. A requirement keeps its sovereign id and its `allocatedTo:` list; one that crosses product nodes belongs to the set of the lowest node that contains all its allocations. A set is opened when its first record exists: no empty set mirrors the PBS ([CM-002](../AMPEL360-SBS-ID-CM-002_Cross-Structure-Identification.md), clarification C2.1).

## Status

**STUB — candidates only.** Candidates carry their `allocatedTo:` and verification method. No requirement is authored: ids and wording await the authoring act.

**Sets**, in [`eWTW-ReqBS-000_Aircraft-Requirements`](eWTW-ReqBS-000_Aircraft-Requirements/README.md):

- [`REQUIREMENT-CANDIDATES_EWTW-000.yaml`](eWTW-ReqBS-000_Aircraft-Requirements/REQUIREMENT-CANDIDATES_EWTW-000.yaml) — the aircraft, `eWTW-PBS-000`: three candidates levied by ruling R2 of `KNOT-EWTW-NRG-001` on 2026-11-14 — the requirement mission of 2,000 km, 100 seats, the reserves. They are the first candidates at aircraft level.
- [`REQUIREMENT-CANDIDATES_EWTW-533001.yaml`](eWTW-ReqBS-000_Aircraft-Requirements/REQUIREMENT-CANDIDATES_EWTW-533001.yaml) — rear-fuselage zone, `eWTW-PBS-053-300-010`: five candidates (open gate of `BL-053-300-010-A2`).
