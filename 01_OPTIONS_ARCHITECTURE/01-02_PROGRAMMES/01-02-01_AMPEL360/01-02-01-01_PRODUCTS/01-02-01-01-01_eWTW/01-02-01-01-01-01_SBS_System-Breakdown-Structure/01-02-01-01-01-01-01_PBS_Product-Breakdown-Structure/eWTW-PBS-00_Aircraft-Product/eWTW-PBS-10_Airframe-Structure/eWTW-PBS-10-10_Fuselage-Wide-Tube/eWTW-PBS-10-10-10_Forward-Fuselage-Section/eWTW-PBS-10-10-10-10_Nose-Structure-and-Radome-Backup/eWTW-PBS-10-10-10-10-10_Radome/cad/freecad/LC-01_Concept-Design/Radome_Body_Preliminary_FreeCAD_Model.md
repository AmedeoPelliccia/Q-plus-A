---
document_id: AMPEL360-eWTW-CAD-RADOME-BODY-PRELIMINARY
title: "eWTW · Radome Body Preliminary FreeCAD Model"
register: Q-plus
architecture: OPTIONS_ARCHITECTURE
options_axis: P-Programmes
programme: AMPEL360
product: eWTW

pbs_id: eWTW-PBS-10-10-10-10-10
pbs_title: "Radome"
parent_pbs_id: eWTW-PBS-10-10-10-10
parent_title: "Nose Structure and Radome Backup"

pnr_id: PNR-eWTW-PBS-10-10-10-10-10
part_number: PN-eWTW-5310-0001

cad_item: Radome_Body
cad_file: eWTW-PBS-10-10-10-10-10-Radome.FCStd
cad_tool: FreeCAD 1.1.1
cad_workbench: Part Design
model_type: preliminary_parametric_placeholder
geometry_basis: wide_tube_and_wing

version: "0.1.0"
revision: A
status: draft
language: en

effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active

cad_status:
  rev_a_axisymmetric_placeholder_created: true
  cad_operation: "Part Design Additive Revolution / Girar"
  revolution_axis: "horizontal sketch axis"
  revolution_angle_deg: 360
  geometry_status: "conceptual_placeholder"
  wide_tube_final_geometry_required: true
  next_revision_target: "elliptical_loft_radome"
---

# eWTW · Radome Body Preliminary FreeCAD Model

## 1. Purpose

This document defines the preliminary FreeCAD modelling instructions for the `Radome_Body` associated with:

```text
eWTW-PBS-10-10-10-10-10 — Radome
````

The model is a **conceptual parametric placeholder** for a regional electric **Wide Tube-and-Wing** aircraft radome.

<img width="2850" height="1664" alt="image" src="https://github.com/user-attachments/assets/20a91fcf-97ec-47c6-b6a5-398eb6775e65" />
**figure-01** *Radome FreeCAD V.1.1.1 Conceptual Parametric Placeholder*

It is not an approved engineering drawing, manufacturing definition, certification substantiation, or released PLM geometry.

---

## 2. Controlled CAD Identity

| Field          | Value                                  |
| -------------- | -------------------------------------- |
| PBS ID         | `eWTW-PBS-10-10-10-10-10`              |
| PBS element    | Radome                                 |
| Parent PBS     | `eWTW-PBS-10-10-10-10`                 |
| Parent element | Nose Structure and Radome Backup       |
| PNR ID         | `PNR-eWTW-PBS-10-10-10-10-10`          |
| Part Number    | `PN-eWTW-5310-0001`                    |
| CAD tool       | FreeCAD 1.1.1                          |
| Workbench      | Part Design                            |
| Body name      | `Radome_Body`                          |
| Native file    | `eWTW-PBS-10-10-10-10-10-Radome.FCStd` |
| STEP export    | `eWTW-PBS-10-10-10-10-10-Radome.step`  |
| Status         | Draft                                  |
| Revision       | A                                      |

---

## 3. Modelling Assumption

Because `eWTW` is a **Wide Tube-and-Wing** aircraft, the final radome should not be treated as a narrow circular regional-jet radome.

The correct mature geometry should be a **lofted oval / elliptical radome**, compatible with a wide forward fuselage.

However, for the first FreeCAD placeholder, two modelling routes are allowed:

| Route                   | Use                           | Status                    |
| ----------------------- | ----------------------------- | ------------------------- |
| Axisymmetric revolution | Fast training placeholder     | Allowed for Rev A only    |
| Elliptical loft         | Wide-tube compatible geometry | Preferred mature approach |

The current model shall start as:

```text
Rev A — preliminary parametric placeholder
```

and later evolve toward:

```text
Rev B — lofted oval wide-tube-compatible radome
```

---

## 4. Reference Coordinate System

| Axis             | Definition                                                                  |
| ---------------- | --------------------------------------------------------------------------- |
| `X`              | Aircraft longitudinal axis. Positive aft from nose tip to attachment plane. |
| `Y`              | Aircraft lateral axis. Positive right-hand side.                            |
| `Z`              | Aircraft vertical axis. Positive upward.                                    |
| Origin           | Nose tip reference point for preliminary model.                             |
| Attachment plane | `X = L_radome`                                                              |
| Symmetry         | Symmetric about aircraft centre plane.                                      |

For the first FreeCAD sketch:

```text
Sketch plane: XZ_Plane
Profile type: half-section profile
Revolution axis: X-axis
```

---

## 5. Preliminary Geometry Parameters

Use these placeholder values for the first model.

```yaml
preliminary_parameters:
  L_radome:
    value: 1500
    unit: mm
    meaning: Radome longitudinal length from nose tip to attachment plane.
  W_base:
    value: 1300
    unit: mm
    meaning: Radome base width at attachment plane.
  H_base:
    value: 1100
    unit: mm
    meaning: Radome base height at attachment plane.
  R_base_y:
    value: 650
    unit: mm
    meaning: Half-width radius at attachment plane.
  R_base_z:
    value: 550
    unit: mm
    meaning: Half-height radius at attachment plane.
  R_tip:
    value: 100
    unit: mm
    meaning: Nose tip radius.
  t_outer_skin:
    value: 2
    unit: mm
    meaning: Outer RF-transparent laminate placeholder thickness.
  t_core:
    value: 14
    unit: mm
    meaning: Dielectric core placeholder thickness.
  t_inner_skin:
    value: 2
    unit: mm
    meaning: Inner RF-transparent laminate placeholder thickness.
  t_wall:
    value: 18
    unit: mm
    meaning: Total sandwich wall placeholder thickness.
  W_seal:
    value: 45
    unit: mm
    meaning: Seal land placeholder width.
  P_fastener:
    value: 90
    unit: mm
    meaning: Preliminary fastener pitch around attachment plane.
  N_fasteners:
    value: 32
    unit: count
    meaning: Preliminary number of fasteners or latch/attachment points.
```

---

## 6. FreeCAD Spreadsheet Parameters

Create a spreadsheet named:

```text
Parameters
```

Add these aliases and values.

| Alias          |  Value | Unit  | Note                          |
| -------------- | -----: | ----- | ----------------------------- |
| `L_radome`     | `1500` | mm    | Length from tip to base plane |
| `W_base`       | `1300` | mm    | Wide-tube base width          |
| `H_base`       | `1100` | mm    | Wide-tube base height         |
| `R_base_y`     |  `650` | mm    | Half width                    |
| `R_base_z`     |  `550` | mm    | Half height                   |
| `R_tip`        |  `100` | mm    | Nose tip radius               |
| `t_outer_skin` |    `2` | mm    | Outer laminate                |
| `t_core`       |   `14` | mm    | Dielectric core               |
| `t_inner_skin` |    `2` | mm    | Inner laminate                |
| `t_wall`       |   `18` | mm    | Total wall thickness          |
| `W_seal`       |   `45` | mm    | Attachment seal land          |
| `P_fastener`   |   `90` | mm    | Fastener pitch                |
| `N_fasteners`  |   `32` | count | Preliminary attachment count  |

Formula:

```text
t_wall = t_outer_skin + t_core + t_inner_skin
```

---

## 7. FreeCAD Object Naming

Use the following object names in FreeCAD.

```text
Document:
  eWTW-PBS-10-10-10-10-10-Radome

Spreadsheet:
  Parameters

Body:
  Radome_Body

Datum objects:
  Datum_Aircraft_X_Axis
  Datum_Attachment_Plane
  Datum_Centerline
  Datum_Base_Ellipse

Sketches:
  Sketch_Radome_Profile
  Sketch_Attachment_Ellipse
  Sketch_Seal_Land
  Sketch_Diverter_Reference_Paths

Features:
  Revolution_Radome_Outer_Surface
  Thickness_Radome_Wall
  Pad_Attachment_Flange
  Pocket_Seal_Land
```

---

## 8. Rev A Modelling Sequence — Axisymmetric Placeholder

Use this method only for the first training / placeholder model.

### Step 1 — Create document

Create and save:

```text
eWTW-PBS-10-10-10-10-10-Radome.FCStd
```

### Step 2 — Create Body

In `Part Design`:

```text
Create Body → rename to Radome_Body
```

### Step 3 — Create Spreadsheet

Switch to `Spreadsheet` workbench:

```text
Create Spreadsheet → rename to Parameters
```

Add parameters from section 6.

### Step 4 — Create profile sketch

Switch to `Part Design`.

Create a sketch on:

```text
XZ_Plane
```

Sketch name:

```text
Sketch_Radome_Profile
```

Draw a half-profile with:

* nose tip at `X = 0`;
* attachment plane at `X = L_radome`;
* maximum radius at base using preliminary circular placeholder:

  * `R_base_placeholder = H_base / 2 = 550 mm`;
* nose tip radius `R_tip = 100 mm`.

### Step 5 — Create revolution

Use:

```text
Part Design → Additive Revolution
```

Revolve the profile:

```text
Angle: 360 degrees
Axis: X-axis / aircraft longitudinal axis
```

### Step 6 — Add wall thickness

Use a preliminary wall thickness:

```text
t_wall = 18 mm
```

If shell/thickness operation is unstable, keep the radome as a solid outer placeholder and record:

```text
wall_thickness_pending = true
```

### Step 7 — Add attachment plane marker

Create a datum plane at:

```text
X = 1500 mm
```

Name:

```text
Datum_Attachment_Plane
```

### Step 8 — Add seal land placeholder

At attachment plane, add a simple ring/flange placeholder:

```text
W_seal = 45 mm
```

This is not final hardware. It is a geometric reference for the radome-to-backup-structure interface.

---

## 9. Rev B Modelling Sequence — Wide-Tube Elliptical Loft

The mature geometry should use a loft with elliptical sections.

Recommended sections:

| Section     | X position |     Width |    Height | Purpose                 |
| ----------- | ---------: | --------: | --------: | ----------------------- |
| Tip         |     `0 mm` |  `200 mm` |  `180 mm` | Rounded nose tip        |
| Forward-mid |   `450 mm` |  `700 mm` |  `600 mm` | Early growth section    |
| Mid         |   `900 mm` | `1100 mm` |  `900 mm` | Wide transition section |
| Base        |  `1500 mm` | `1300 mm` | `1100 mm` | Attachment interface    |

Create sketches:

```text
Sketch_Section_Tip
Sketch_Section_ForwardMid
Sketch_Section_Mid
Sketch_Section_Base
```

Then use:

```text
Part / Part Design → Loft
```

Loft output:

```text
Radome_Outer_Loft
```

The lofted model is preferred for wide-tube compatibility.

---

## 10. Material Placeholder

The CAD model may include material placeholders but shall not claim approved material definition.

```yaml
material_stack_placeholder:
  outer_skin:
    material_class: RF-transparent composite laminate
    thickness_mm: 2
    status: TBD
  core:
    material_class: low-density dielectric core
    thickness_mm: 14
    status: TBD
  inner_skin:
    material_class: RF-transparent composite laminate
    thickness_mm: 2
    status: TBD
  erosion_protection:
    material_class: rain erosion boot or coating
    thickness_mm: TBD
    status: TBD
```

Required future material properties:

* dielectric constant;
* loss tangent;
* density;
* moisture absorption;
* interlaminar shear strength;
* rain erosion resistance;
* bird-strike performance;
* lightning compatibility.

---

## 11. Interface Markers

The preliminary CAD shall include placeholders or reference geometry for:

| Interface               | CAD Representation                         |
| ----------------------- | ------------------------------------------ |
| Radome backup structure | Attachment plane and flange reference      |
| Weather radar           | Internal clearance envelope placeholder    |
| Lightning protection    | Diverter strip path reference curves       |
| Moisture seal           | Seal land placeholder                      |
| Maintenance access      | Hinge/latch reference zones                |
| Aerodynamic continuity  | Smooth transition to forward fuselage base |

Do not model final hardware until the interface control document is baselined.

---

## 12. Export Requirements

When the placeholder is complete, export:

```text
cad/freecad/eWTW-PBS-10-10-10-10-10-Radome.FCStd
cad/step/eWTW-PBS-10-10-10-10-10-Radome.step
drawings/eWTW-PBS-10-10-10-10-10-Radome-Drawing.pdf
```

Use STEP export only after the geometry regenerates without errors.

---

## 13. Evidence and Traceability

The CAD placeholder shall trace to:

| Layer    | Identifier                             |
| -------- | -------------------------------------- |
| PBS      | `eWTW-PBS-10-10-10-10-10`              |
| PNR      | `PNR-eWTW-PBS-10-10-10-10-10`          |
| PN       | `PN-eWTW-5310-0001`                    |
| BOM      | `BOM-eWTW-PBS-10-10-10-10-10`          |
| CAD      | `eWTW-PBS-10-10-10-10-10-Radome.FCStd` |
| STEP     | `eWTW-PBS-10-10-10-10-10-Radome.step`  |
| Evidence | `PBS-EVIDENCE-REGISTER.yaml`           |

---

## 14. Validation Status

```yaml
validation_status:
  geometry: conceptual_placeholder
  material_stack: TBD
  RF_performance: not_verified
  bird_strike: not_verified
  lightning_zone_1A: not_verified
  moisture_ingress: not_verified
  CAD_regeneration: pending
  STEP_export: pending
  drawing_release: pending
```

---

## 15. Controlled Closure Statement

`Radome_Body_Preliminary.md` defines the initial FreeCAD modelling authority for the preliminary radome body.

The file authorizes only a **conceptual parametric placeholder**.

It does not authorize production geometry, certified structure, final material selection, RF compliance, lightning compliance, bird-strike compliance, or released engineering drawing status.

All future geometry changes shall preserve the traceability chain:

```text
PBS → PNR → PN → BOM → CAD → STEP → Drawing → Evidence
```

