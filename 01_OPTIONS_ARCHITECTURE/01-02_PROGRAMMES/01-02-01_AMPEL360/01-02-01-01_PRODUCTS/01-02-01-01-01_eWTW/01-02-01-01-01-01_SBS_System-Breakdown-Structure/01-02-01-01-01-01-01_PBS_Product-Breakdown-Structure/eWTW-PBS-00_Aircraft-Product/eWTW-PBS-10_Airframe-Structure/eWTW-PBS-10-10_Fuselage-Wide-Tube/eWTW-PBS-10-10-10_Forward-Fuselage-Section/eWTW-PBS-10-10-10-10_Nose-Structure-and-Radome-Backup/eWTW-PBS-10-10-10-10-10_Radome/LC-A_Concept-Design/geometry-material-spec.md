---
document_id: AMPEL360-eWTW-PBS-10-10-10-10-10-GMS
title: "eWTW · PBS-10-10-10-10-10 — Radome · Geometry and Material Specification"
pbs_id: eWTW-PBS-10-10-10-10-10
part_number: PN-eWTW-5310-0001
revision: A
status: draft
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · PBS-10-10-10-10-10 — Radome · Geometry and Material Specification

- **PBS ID:** `eWTW-PBS-10-10-10-10-10`
- **Part Number:** `PN-eWTW-5310-0001`
- **Parent:** `eWTW-PBS-10-10-10-10` (Nose Structure and Radome Backup)
- **CAD authority:** `REV-A1/FreeCAD/eWTW-PBS-10-10-10-10-10-Radome.FCStd`
- **Exchange geometry:** `cad/step/eWTW-PBS-10-10-10-10-10-Radome.step`
- **Drawing:** `drawings/eWTW-PBS-10-10-10-10-10-Radome-Drawing.pdf`
- **Status:** draft — values TBC pending RF and structural substantiation

---

## 1. Geometry

### 1.1 Envelope

| Parameter | Value | Status |
|---|---|---|
| Max outer diameter at base (aft attach ring) | TBD mm | TBD |
| Axial length (tip to aft attach plane) | TBD mm | TBD |
| Nose apex geometry | Ogive / elliptical (TBC per RF opt.) | TBD |
| Wall thickness (nominal, A-sandwich) | TBD mm | TBD |
| Attachment interface | Hinge + latch; interface to `PBS-10-10-10-10-20` | TBD |

### 1.2 CAD Reference Frames

| Frame | Definition |
|---|---|
| Aircraft reference | Fuselage station (FS), waterline (WL), buttline (BL) — to be aligned with master geometry |
| Radome attach plane | FS TBD (aft face of attach ring) |
| Radar antenna clearance envelope | As defined by WXR interface ICD (PBS-50-30/40) |

### 1.3 Key Geometric Constraints

- Outer aero surface must be continuous with `PBS-10-10-10-10-30` (nose cap / forward fairing).
- Inner clearance envelope must satisfy WXR antenna swing and removal requirements.
- Attach-ring bore and latch provisions must match `PBS-10-10-10-10-20` radome backup bulkhead interface.

---

## 2. Wall Construction

The radome wall uses an **A-sandwich** architecture: two RF-transparent structural skins over a low-density dielectric core.

### 2.1 Outer Skin (`PN-eWTW-5310-0001-01`)

| Parameter | Baseline | Status |
|---|---|---|
| Material family | RF-transparent GFRP (glass/epoxy) | TBD |
| Fibre orientation | TBD (optimized for RF + bird-strike) | TBD |
| Nominal thickness | TBD mm | TBD |
| Surface finish (OML) | Per erosion-boot adhesion and aero spec | TBD |

### 2.2 Dielectric Core (`PN-eWTW-5310-0001-02`)

| Parameter | Baseline | Status |
|---|---|---|
| Material family | Low-density foam or Nomex honeycomb (TBC) | TBD |
| Relative permittivity (εr) | TBD (must be controlled to RF tolerance) | TBD |
| Loss tangent (tan δ) | TBD | TBD |
| Nominal thickness | TBD mm | TBD |

> [!IMPORTANT]
> The dielectric constant and loss tangent of the core are **RF-critical parameters**. They shall be controlled to tolerances specified by the WXR interface ICD (PBS-50-30/40). Material procurement shall include RF-property certification, not only mechanical certification.

### 2.3 Inner Skin (`PN-eWTW-5310-0001-03`)

| Parameter | Baseline | Status |
|---|---|---|
| Material family | RF-transparent GFRP (glass/epoxy) | TBD |
| Fibre orientation | TBD | TBD |
| Nominal thickness | TBD mm | TBD |

---

## 3. Protective Coatings and Provisions

### 3.1 Rain Erosion Boot / Coating (`PN-eWTW-5310-0001-04`)

| Parameter | Baseline | Status |
|---|---|---|
| Type | Elastomeric erosion boot or polyurethane coating (TBC) | TBD |
| Coverage zone | Full OML leading surface — TBD aft limit | TBD |
| RF impact | Must not degrade transmission loss / boresight error beyond ICD tolerance | TBD |
| Qualification | Combined structural + RF verification required | TBD |

### 3.2 Moisture Seal and Drainage (`PN-eWTW-5310-0001-06`)

| Parameter | Baseline | Status |
|---|---|---|
| Seal type | Perimeter seal at attach ring; drainage provision TBD | TBD |
| RF criticality | Water ingress into core degrades εr; sealing is RF-critical | — |

### 3.3 Bonding and Ground Provisions (`PN-eWTW-5310-0001-07`)

| Parameter | Note | Owner |
|---|---|---|
| Bonding pad locations | TBD per LPS ICD | LPS function (PBS-40-40) |
| Diverter-strip routing provisions | TBD | LPS function (PBS-40-40) |
| Ground bonding resistance | Per LPS requirement | LPS function |

> [!NOTE]
> Provisions are **radome-owned**; the diverter strips and bonding function are **LPS-owned** (`eWTW-PBS-40-40`).

---

## 4. Interface Specifications

| Interface | Parameter | ICD reference | Status |
|---|---|---|---|
| RF window — WXR antenna | Transmission loss ≤ TBD dB; boresight error ≤ TBD mrad | WXR ICD (PBS-50-30/40) | TBD |
| Structural attach to backup bulkhead | Interface loads, hinge geometry, latch force | Structural ICD (PBS-10-10-10-10-20) | TBD |
| Lightning diverters | Strip bonding geometry, pad conductivity | LPS ICD (PBS-40-40) | TBD |
| Aero continuity — nose cap | Surface profile tolerance at aft interface | Aero ICD (PBS-10-10-10-10-30) | TBD |

---

## 5. Verification Summary

| Requirement | Method | Status |
|---|---|---|
| RF transmission loss | RF range test | TBD |
| Boresight error | RF range test | TBD |
| Bird strike | Analysis + test (per CS-25 / FAR-25) | TBD |
| Lightning Zone 1A | Test + analysis (per CS-25 Appendix H) | TBD |
| Rain erosion qualification | Erosion tunnel test | TBD |
| Moisture ingress / RF after soak | Combined environmental + RF test | TBD |

---

## 6. Change Log

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-05-29 | Q-STRUCTURES | Initial draft geometry and material specification. All values TBD pending RF and structural substantiation. |
