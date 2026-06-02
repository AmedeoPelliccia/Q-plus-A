---
document_id: AMPEL360-eWTW-PBS-10-10-10-10-10-ReqBS-REV-A1
title: "eWTW · PBS-10-10-10-10-10 — Radome ReqBS Baseline (REV-A1)"
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
reqbs_id: ReqBS-RADOME-REV-A1
revision: RADOME-REV-A1
lifecycle_stage: LC-A
governance_class: baseline
version: "0.1.0"
status: draft
language: en
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
requirements_authority:
  owner: Q-STRUCTURES
  supporting_authorities:
    - Q-DATAGOV
    - Q-AIR
    - Q-SCIRES
  approval_status: unapproved
related_revision_package:
  cad_revision: RADOME-REV-A1
  cad_record: "REV-A1/FreeCAD/Radome-CAD-Record.md"
  publication_040: "pub/040_descriptive/DMC-AMPEL360-A-53-10-10-00A-040A-D_Radome-Description.xml"
---

# eWTW · PBS-10-10-10-10-10 — Radome ReqBS Baseline (REV-A1)

![LC-A](https://img.shields.io/badge/maturity-LC--A%20Conceptual-5585b0)
![REV-A1](https://img.shields.io/badge/revision-REV--A1-c29c00)
![ReqBS](https://img.shields.io/badge/breakdown-ReqBS-1f883d)

- **Item:** `eWTW-PBS-10-10-10-10-10` (Radome)
- **Part number:** `PN-eWTW-5310-0001`
- **Revision:** `RADOME-REV-A1` · **Lifecycle stage:** `LC-A — Conceptual Design`
- **Effectivity:** eWTW · baseline · MSN-001..050 · active
- **Requirements authority:** `Q-STRUCTURES` (supporting: `Q-DATAGOV`, `Q-AIR`, `Q-SCIRES`) · approval `unapproved`
- **Record:** [`ReqBS-RADOME-REV-A1.yaml`](ReqBS-RADOME-REV-A1.yaml)

---

## 1. Purpose

This is the **first controlled requirements baseline** for the radome, defined for the conceptual CAD state `RADOME-REV-A1` (`LC-A`). It fixes the radome's requirements as **revisioned artefacts** linked to the PBS item and its configuration, in line with `SBS-REV-BREAKDOWN-001` and `REQBS-REV-001`.

Requirements are **not** static lifecycle-folder content. The authoritative requirement state for the radome lives here — under the PBS item revision — not inside the LC maturity folders. LC folders control maturity gates; this `REV-A1` baseline controls the engineering requirement truth of the configuration.

## 2. Position

```text
eWTW-PBS-10-10-10-10-10_Radome/
└── LC-A_Concept-Design/
    └── REV-A1/
        └── Requirements/
            ├── ReqBS-RADOME-REV-A1.yaml   ← controlled record
            └── ReqBS-RADOME-REV-A1.md     ← this document
```

The lifecycle phase (`LC-A_Concept-Design`) governs the revision (`REV-A1`), which governs the artifact-domain folder (`Requirements/`). This mirrors the CAD layout (`REV-A1/FreeCAD/`) and follows the canonical governance rule: `<PBS item>/<LC>/<REV>/<artifact-domain>/`.

## 3. Requirement classes (ReqBS-01..15)

The baseline records one or more requirements per controlled class. Radome examples:

| Class | Name | Radome example |
|---|---|---|
| `ReqBS-01` | Customer Expectations | Maintain aerodynamic continuity and support weather-radar operation. |
| `ReqBS-02` | Project and Enterprise Constraints | Use open FreeCAD-compatible CAD records and repository traceability. |
| `ReqBS-03` | External Constraints | CS-25,[^cs25] lightning, bird strike, maintainability, environmental constraints. |
| `ReqBS-04` | Operational Scenarios | Normal flight, rain, lightning exposure, bird strike, maintenance access. |
| `ReqBS-05` | Measures of Effectiveness | RF transparency, aerodynamic continuity, maintainability, damage tolerance. |
| `ReqBS-06` | System Boundaries | Radome shell and provisions only; WXR and LPS are referenced systems. |
| `ReqBS-07` | Interfaces | Backup structure, WXR envelope, LPS diverters, seal, latches. |
| `ReqBS-08` | Utilization Environments | Ground, taxi, take-off, cruise, rain, hail, lightning zone, maintenance. |
| `ReqBS-09` | Lifecycle Requirements | Concept, preliminary, detailed, qualification, certification, MRO, retirement. |
| `ReqBS-10` | Functional Requirements | Protect radar, provide RF window, provide aerodynamic fairing. |
| `ReqBS-11` | Performance Requirements | Transmission loss, boresight error, impact resistance, erosion resistance. |
| `ReqBS-12` | Modes of Operation | Installed closed, opened for maintenance, removed, post-lightning inspection. |
| `ReqBS-13` | Technical Performance Measures | Mass, RF loss, boresight error, bonding resistance, erosion life. |
| `ReqBS-14` | Physical Characteristics | Length, base envelope, wall stack, attachment geometry. |
| `ReqBS-15` | Human Systems Integration | Safe maintainability, access, tool clearance, technician handling. |

`ReqBS-13` declarations are tracked as quantified targets and margins under the TPMS (`…-10_TPMS_Technical-Performance-Measurement-Structure/`). The `ReqBS-01..15` class set is the 15 IEEE P1220 requirements analysis task areas.[^sef][^ieee1220]

## 4. Traceability

| Direction | Linked artefacts |
|---|---|
| Upstream | `eWTW-PBS-10-10-10-10-10` · `ATLAS-053` |
| Downstream | `IBS-RADOME-REV-A1` · `RBS-RADOME-REV-A1` · `CBS-RADOME-REV-A1` · `EBS-RADOME-REV-A1` · `CAD-RADOME-REV-A1` · `PUB-040-RADOME` |

## 5. Governing rules

```yaml
revisioned_breakdown_structure_rule: SBS-REV-BREAKDOWN-001   # per-revision breakdown ownership
requirements_evolution_rule:        REQBS-REV-001            # requirements are revisioned artefacts
```

> [!IMPORTANT]
> A change to these requirements that affects geometry, interfaces, cost, risk, evidence, certification, or operations shall create or update the corresponding `REV-X` ReqBS and trigger impact assessment across `IBS`, `CBS`, `RBS`, `EBS`, `BOM`, `CAD`, and `PUB` artefacts (`REQBS-REV-001`).

## 6. Footprint

| Field | Value |
|---|---|
| Document ID | `AMPEL360-eWTW-PBS-10-10-10-10-10-ReqBS-REV-A1` |
| ReqBS ID | `ReqBS-RADOME-REV-A1` |
| PBS ID | `eWTW-PBS-10-10-10-10-10` |
| Part number | `PN-eWTW-5310-0001` |
| Revision · Stage | `RADOME-REV-A1` · `LC-A` |
| Effectivity | eWTW · baseline · MSN-001..050 · active |
| Requirements authority | `Q-STRUCTURES` · approval `unapproved` |
| Version | 0.1.0 |
| Status | draft |

**Change log.**

| Version | Date | Author / Division | Change |
|---|---|---|---|
| 0.1.0 | 2026-06-02 | Q-STRUCTURES | Initial draft ReqBS baseline for the radome conceptual CAD state (`RADOME-REV-A1`). |

## 7. References

[^sef]: Defense Acquisition University (DAU) Press. *Systems Engineering Fundamentals*. Fort Belvoir, VA, January 2001. — Ch. 4 *Requirements Analysis* (Fig. 4-3, the 15 requirements analysis task areas defining `ReqBS-01..15`).
[^ieee1220]: IEEE Std 1220, *IEEE Standard for Application and Management of the Systems Engineering Process* — source of the 15 requirements analysis task areas.
[^cs25]: EASA CS-25, *Certification Specifications and Acceptable Means of Compliance for Large Aeroplanes* — applicable airworthiness basis referenced by `ReqBS-03`.
