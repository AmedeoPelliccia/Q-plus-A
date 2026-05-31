---
document_id: AMPEL360-eWTW-PBS-10-10-10-10-10-CAD-REV-A1
title: "eWTW · PBS-10-10-10-10-10 — Radome CAD Record (REV-A1)"
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

cad_lifecycle:
  lifecycle_model: "LC-letter CAD/product maturity model"
  lc_stage: "LC-A"
  lc_stage_name: "Conceptual Design"
  previous_revision: "RADOME-REV-A0"
  current_revision: "RADOME-REV-A1"
  revision_status: "iterating"
  next_release_gate: "RADOME-REV-A_RELEASED"
  next_lc_stage: "LC-B"
  next_lc_stage_name: "Preliminary Design"

cad_source:
  native_model: "eWTW-PBS-10-10-10-10-10-Radome.FCStd"
  tool: "FreeCAD 1.1.1"
  workbench: "Part Design"
  body: "Radome_Body"
  feature: "Revolution"
  created_by: "Amedeo Pelliccia"

revision_intent:
  - "Resolve REV-A0 finding F1: absolute scale verification/correction."
  - "Resolve REV-A0 finding F3: controlled FreeCAD document metadata."
  - "Preserve REV-A0 conceptual geometry logic: secant-ogive axisymmetric placeholder."
  - "Do not yet introduce wall/sandwich, seal land, flange, or wide-tube elliptical loft."

governance_class: baseline
version: "0.1.0"
status: draft
language: en
---

# eWTW · PBS-10-10-10-10-10 — Radome CAD Record (REV-A1)

![LC-A](https://img.shields.io/badge/CAD%20maturity-LC--A%20Conceptual-5585b0)
![REV-A1](https://img.shields.io/badge/revision-REV--A1-c29c00)
![FreeCAD](https://img.shields.io/badge/tool-FreeCAD%201.1.1-0075ca)

## 1. Artefact confirmation

`RADOME-REV-A1` is the second controlled CAD iteration of:

```text
eWTW-PBS-10-10-10-10-10 — Radome
````

It remains inside:

```text
LC-A — Conceptual Design
```

This revision is intended to correct the blocking findings identified in `RADOME-REV-A0` before promotion to `RADOME-REV-A_RELEASED`.

---

## 2. REV-A1 Purpose

`REV-A1` shall:

1. verify or correct the absolute CAD scale;
2. preserve the conceptual radome outer mould line;
3. keep the model as an axisymmetric conceptual placeholder;
4. complete controlled FreeCAD metadata;
5. prepare the artefact for possible `RADOME-REV-A_RELEASED`.

---

## 3. Geometry Status

| Parameter                |                          Target Value | Unit | Status           |
| ------------------------ | ------------------------------------: | ---- | ---------------- |
| Axial length, `L_radome` |                                  1500 | mm   | to verify        |
| Base radius, `R_base_z`  |                                   550 | mm   | to verify        |
| Base diameter, `D_base`  |                                  1100 | mm   | derived          |
| Revolution angle         |                                   360 | deg  | retained         |
| Geometry type            | secant-ogive / conceptual placeholder | n/a  | retained         |
| Wide-tube final geometry |                       elliptical loft | n/a  | deferred to LC-B |

---

## 4. REV-A0 Findings Closure

| Finding | REV-A0 Finding                                         | REV-A1 Action                                                           | Status   |
| ------- | ------------------------------------------------------ | ----------------------------------------------------------------------- | -------- |
| `F1`    | Absolute scale appears approximately `×1000` oversize. | Verify sketch dimensions and correct to `1500 mm × 550 mm` if required. | open     |
| `F2`    | Solid body, no sandwich wall.                          | Accepted as LC-A limitation; deferred to LC-C.                          | deferred |
| `F3`    | Controlled metadata gaps.                              | Complete FreeCAD document metadata.                                     | open     |

---

## 5. Controlled Metadata Requirements

Before `RADOME-REV-A1` can support `RADOME-REV-A_RELEASED`, the FreeCAD file shall carry controlled metadata.

| FreeCAD Property | Required Value                                                                    |
| ---------------- | --------------------------------------------------------------------------------- |
| Document label   | `eWTW-PBS-10-10-10-10-10-Radome`                                                  |
| Company          | `Q-plus / AMPEL360 / AEROSPACEMODEL`                                              |
| Id               | `AMPEL360-eWTW-PBS-10-10-10-10-10-CAD-REV-A1`                                     |
| License          | `open-technical-publication` or repository-controlled licence                     |
| Comment          | `LC-A Conceptual Design / RADOME-REV-A1 / corrected-scale conceptual placeholder` |

---

## 6. Release Readiness

`RADOME-REV-A1` may proceed toward `RADOME-REV-A_RELEASED` only if:

| Criterion                      | Required State |
| ------------------------------ | -------------- |
| CAD opens in FreeCAD 1.1.1     | required       |
| CAD regenerates without errors | required       |
| Scale is verified or corrected | required       |
| Metadata is controlled         | required       |
| Preview image recorded         | required       |
| Evidence anchor prepared       | required       |
| F1 closed                      | required       |
| F3 closed                      | required       |
| F2 deferred to LC-C            | accepted       |

---

## 7. Traceability

| Layer             | Identifier                             |
| ----------------- | -------------------------------------- |
| PBS               | `eWTW-PBS-10-10-10-10-10`              |
| PNR               | `PNR-eWTW-PBS-10-10-10-10-10`          |
| PN                | `PN-eWTW-5310-0001`                    |
| CAD               | `eWTW-PBS-10-10-10-10-10-Radome.FCStd` |
| CAD maturity      | `LC-A / RADOME-REV-A1`                 |
| Previous revision | `RADOME-REV-A0`                        |
| Next release gate | `RADOME-REV-A_RELEASED`                |

---

## 8. Controlled Closure Statement

`RADOME-REV-A1` is a corrective LC-A conceptual CAD revision.

It shall resolve the scale and metadata findings from `RADOME-REV-A0` while preserving the conceptual ogive radome geometry.

It shall not introduce LC-B wide-tube elliptical loft geometry, LC-C sandwich wall definition, or released engineering drawing status.

```
```
