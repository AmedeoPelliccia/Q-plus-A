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

## Status

**STUB — no depth authored.**
