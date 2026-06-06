---
document_id: AMPEL360-eWTW-PBS-10-10-10-10-10-CAD-REV-A0
title: "eWTW · PBS-10-10-10-10-10 — Radome CAD Record (REV-A0)"
register: Q-plus
architecture: OPTIONS_ARCHITECTURE
options_axis: P-Programmes
programme: AMPEL360
product: eWTW
pbs_id: eWTW-PBS-10-10-10-10-10
part_number: PN-eWTW-5310-0001
cad_lifecycle:
  lifecycle_model: "LC-letter CAD/product maturity model"
  lc_stage: "LC-A"
  lc_stage_name: "Conceptual Design"
  current_revision: "RADOME-REV-A0"
  revision_status: "iterating"
  next_release_gate: "RADOME-REV-A_RELEASED"
cad_source:
  native_model: "eWTW-PBS-10-10-10-10-10-Radome.FCStd"
  tool: "FreeCAD 1.1.1"
  workbench: "Part Design"
  created_by: "Amedeo Pelliccia"
  created: "2026-05-30T11:51:21+02:00"
  last_modified: "2026-05-31T08:45:36+02:00"
governance_class: baseline
version: "1.0.0"
status: draft
language: en
---

# eWTW · PBS-10-10-10-10-10 — Radome CAD Record (REV-A0)

![LC-A](https://img.shields.io/badge/CAD%20maturity-LC--A%20Conceptual-5585b0)
![REV-A0](https://img.shields.io/badge/revision-REV--A0-c29c00)
![FreeCAD](https://img.shields.io/badge/tool-FreeCAD%201.1.1-0075ca)

## 1. Artefact confirmation

The uploaded `eWTW-PBS-10-10-10-10-10-Radome.FCStd` is confirmed as the **LC-A / REV-A0** conceptual CAD artefact for the radome part (`eWTW-PBS-10-10-10-10-10`, `PN-eWTW-5310-0001`).

| Field | Value (read from file) |
|---|---|
| Document label | `eWTW-PBS-10-10-10-10-10-Radome` |
| Tool | FreeCAD 1.1.1, Part Design |
| Body | `Radome_Body` (PartDesign::Body) |
| Feature | `Revolution` of `Sketch`, 360° |
| Created by | Amedeo Pelliccia |
| Created | 2026-05-30 11:51 |
| Last modified | 2026-05-31 08:45 |

## 2. Extracted geometry

The body is a full revolution of a planar profile (axis line + base line + ogive arc).

| Parameter | Model value (units as modelled) | Note |
|---|---|---|
| Axial length, L | 1,500,000 | tip to base |
| Base radius, Rb | 550,000 | base diameter D = 1,100,000 |
| Ogive arc radius, ρ | 1,772,628 | arc centre (1,294,759, −1,210,706) |
| Revolution angle | 360° | full body of revolution |
| Fineness ratio, L/D | **1.36** | scale-independent — this is the real design parameter |
| Ogive type | **secant** | model ρ (1,772,628) < tangent-ogive ρ (2,320,455) |

The **fineness ratio (1.36)** and the **secant-ogive form** are the meaningful conceptual outputs of REV-A0 — both are scale-independent and both are sensible for a regional-aircraft weather radome. These are the parameters that carry forward; the absolute dimensions do not yet (see §3).

## 3. Findings — resolve before LC-B promotion

> [!IMPORTANT]
> **F1 — Absolute scale appears ~1000× oversize.** Modelled L = 1,500,000 and Rb = 550,000. If the document unit is millimetres (FreeCAD default), that is a 1500 m long, 1100 m diameter radome — physically impossible. A regional-aircraft radome is ~1.5 m long / ~1.1 m base diameter, i.e. exactly the modelled numbers ÷ 1000. The **proportions are correct**; only the absolute scale is wrong. At LC-A this is tolerable (proportion is the deliverable), but it **must be resolved before LC-B**, where the radome has to mate to the radome backup bulkhead (`eWTW-PBS-10-10-10-10-20`) at real dimensions. Decide: rescale ÷1000, or confirm the intended document unit.

> [!IMPORTANT]
> **F2 — Solid body, no wall.** The revolution produces a **solid** ogive. The radome BOM (§4.8 of the element doc) defines a sandwich: outer skin / dielectric core / inner skin (`PN-eWTW-5310-0001-01..03`). A solid is acceptable for LC-A conceptual envelope, but **LC-C detailed design requires the wall/sandwich** (shell or multi-body) so the RF-transparent laminate, core thickness, and erosion boot can be represented. The current model is the outer mould line only.

> [!WARNING]
> **F3 — Controlled metadata gaps.** The file carries `License: All rights reserved` with the FreeCAD-default Wikipedia URL, empty `Company`, and empty `Id`. For a controlled artefact these should be set: `Company` → GQAOA / AMPEL360; `License` → programme classification (`open-technical-publication` per the element doc, or as governed); `Id` → the PNR/PN (`PN-eWTW-5310-0001`) or the CAD document_id. Set these before `REV-A_RELEASED`.

## 4. Binding to the product record

| Layer | Identifier | This artefact |
|---|---|---|
| PBS | `eWTW-PBS-10-10-10-10-10` | Radome element |
| PN | `PN-eWTW-5310-0001` | Part number |
| CAD (native) | `eWTW-PBS-10-10-10-10-10-Radome.FCStd` | this file, REV-A0 |
| CAD maturity | `LC-A` / `RADOME-REV-A0` | conceptual, iterating |
| Next gate | `RADOME-REV-A_RELEASED` → `LC-B` | blocked by F1, F2, F3 |

The geometry models constituent `PN-eWTW-5310-0001` at outer-mould-line level only. The owned sub-constituents (skins, core, erosion boot, fittings) are **not yet represented** — they enter at LC-C. The provision/reference items (diverter strips, radar antenna) are correctly **absent** from the CAD body, consistent with the BOM ownership boundary.

## 5. Release-gate readiness (REV-A_RELEASED)

| Criterion | State |
|---|---|
| Conceptual outer mould line defined | ✅ done (secant ogive, L/D 1.36) |
| Absolute scale resolved | ❌ F1 open |
| Wall/sandwich representation | n/a at LC-A (required at LC-C) |
| Controlled metadata set | ❌ F3 open |
| Mate interface to backup bulkhead defined | ❌ deferred to LC-B |

`REV-A0` cannot promote to `REV-A_RELEASED` until F1 and F3 are closed. F2 is an LC-C requirement, recorded now so it is not lost.

## 6. Footprint

| Field | Value |
|---|---|
| Document ID | `AMPEL360-eWTW-PBS-10-10-10-10-10-CAD-REV-A0` |
| PBS ID | `eWTW-PBS-10-10-10-10-10` |
| Part Number | `PN-eWTW-5310-0001` |
| CAD revision | `RADOME-REV-A0` |
| CAD maturity | `LC-A` Conceptual Design |
| Source file | `eWTW-PBS-10-10-10-10-10-Radome.FCStd` (FreeCAD 1.1.1) |
| Status | draft |
| Evidence anchor (IEF) | `<sha256: to-be-stamped-at-commit>` |

**Change log.**

| Version | Date | Author / Division | Change |
|---|---|---|---|
| 1.0.0 | 2026-05-31 | Q-STRUCTURES | CAD record for REV-A0; geometry extracted from FCStd; findings F1–F3 logged. |
