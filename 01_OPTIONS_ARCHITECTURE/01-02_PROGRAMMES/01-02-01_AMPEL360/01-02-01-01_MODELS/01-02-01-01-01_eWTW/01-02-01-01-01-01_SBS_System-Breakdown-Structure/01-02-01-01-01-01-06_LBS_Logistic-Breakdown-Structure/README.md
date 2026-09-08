---
status: draft
standard_scope: governance
---

# eWTW — Logistic Breakdown Structure (LBS)

<!-- Generated 2026-09-06 - GitHub Copilot - SBS rework under CM-002 -->

## Purpose

The LBS controls the provisioned items of the eWTW: spares, consumables and ground-support items, each keyed to the product element it provisions. A provisioned item has exactly one subject in the product tree, so the LBS does not invent a second identity for it — it is a product-indexed view, and its rows inherit the crossing trace that the CSN already provides.

## Id grammar (CM-002 §3)

> | **LBS** | derived | `eWTW-LBS-<CSN>-<item>` | is the id | 1:1 with a provisioned item |

The id **is** the reference: the embedded CSN resolves to the declaring station and the item field to the provisioned part. Derived ids are regenerated, never typed (CM-002 §4.2) — if a CSN changes under a ratified act, the LBS rows regenerate with it.

## References into the PBS

An LBS row references the PBS **by its derived id** — the CSN segment resolves to a station directory and the item to a part number beneath it. Per CM-002 §4.4 the row holds no restated attributes: nomenclature, quantity and interchangeability are read from `part.yaml`, never copied.

## Trigger

The workstream opens when the first provisioning decision is taken against a realized station (chapter 053 today) — the first spared assembly or first listed consumable. Until then no provisioning row is authored here; a fabricated spares list would be invented depth.

## Status

**STUB — no depth authored.**
