---
document_id: AMPEL360-eWTW-PBS-10-10-10-SSOT-README
title: "eWTW · PBS-10-10-10 — SSOT (Engineering Source of Truth)"
register: Q-plus
architecture: OPTIONS_ARCHITECTURE
options_axis: P-Programmes
programme: AMPEL360
product: eWTW
pbs_id: eWTW-PBS-10-10-10
pbs_title: "Forward Fuselage Section"
layer: SSOT
counterpart: "../../../../../../01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure/000-099_G-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces/053_Fuselage/053-100_Forward-Fuselage-Section/"
atlas_references:
  - "000-099_ATLAS / 050-059_Primary-Structures-and-Programme-Interfaces"
primary_q_division: Q-STRUCTURES
support_q_divisions:
  - Q-AIR
  - Q-DATAGOV
  - Q-MECHANICS
governance_class: baseline
version: "1.0.0"
status: draft
language: en
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · PBS-10-10-10 — SSOT (Engineering Source of Truth)

![SSOT](https://img.shields.io/badge/layer-SSOT-2d7a2d)
![draft](https://img.shields.io/badge/status-draft-c29c00)

## 1. Purpose

`SSOT/` holds the **authoritative engineering content** for the Forward Fuselage Section (`eWTW-PBS-10-10-10`). It is the single source of truth: the element definition, constituent registry, interface definitions, allocated requirements, and evidence anchors all originate here.

Its counterpart `../../../../../../01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure/000-099_G-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces/053_Fuselage/053-100_Forward-Fuselage-Section/` is a **projection** of this content into S1000D/CSDB form. Content flows **SSOT → PUB, never the reverse.** If `PUB/` and `SSOT/` disagree, `SSOT/` prevails and the publication is the defect.

## 2. SSOT → PUB authority rule

```yaml
ssot_authority_rule:
  id: SSOT-AUTHORITY-001
  rule: >
    SSOT/ is the sole originating source of engineering truth for this element.
    PUB/ and all derived artefacts reference SSOT/ and never originate content.
    A value present in PUB/ but absent from SSOT/ is a publication defect, not
    an engineering fact.
```

## 3. SSOT content index

| Source object | Holds | Projected to |
|---|---|---|
| `definition.md` | Element definition, boundary, structural role | PUB `040A` description DM |
| `constituents.md` | Constituent registry (child PBS items) | PUB `941A` IPD |
| `interfaces.md` | Authoritative interface definitions (IBS source) | PUB description / `dmRef` |
| `requirements.md` | Allocated requirements + drivers | PUB inspection/repair DMs |
| `evidence.md` | Evidence anchors (IEF) and substantiation refs | PUB `qualityAssurance` state |
| `qatlantide-roundtable.md` | Q+ATLANTIDE round table — impact analysis on the *Libro Unico delle Tecnologie* (which nodes this element impacts; typed + effectivity-filtered) | change-impact; PUB technology refs |

At baseline, the consolidated definition lives in this README §5–§6; the separate
files above are created as content matures. The README is the authoritative entry
point until then.

## 4. Constituent registry (authoritative)

The Forward Fuselage Section owns the following structural constituents. Each child PBS folder carries its own SSOT.

| PBS ID | Constituent | SSOT location |
|---|---|---|
| `eWTW-PBS-10-10-10-10` | Nose Structure and Radome Backup | `../eWTW-PBS-10-10-10-10_*/SSOT/` |
| `eWTW-PBS-10-10-10-20` | Forward Pressure Bulkhead | child SSOT |
| `eWTW-PBS-10-10-10-30` | Flight-Deck Structure | child SSOT |
| `eWTW-PBS-10-10-10-40` | Side-Window Structural Surrounds | child SSOT |
| `eWTW-PBS-10-10-10-50` | Nose-Landing-Gear Bay and Attach | child SSOT |
| `eWTW-PBS-10-10-10-60` | Forward Equipment Bay Structure | child SSOT |
| `eWTW-PBS-10-10-10-70` | Forward Barrel Skin/Stringer/Frame | child SSOT |
| `eWTW-PBS-10-10-10-80` | Forward Door/Hatch Surrounds | child SSOT |

## 5. Element definition (authoritative)

The Forward Fuselage Section is the structural assembly from the nose tip to the forward production join with the centre fuselage. It provides the pressurized crew volume (flight deck), closes the forward pressure boundary, carries nose-landing-gear loads, and houses the forward equipment (E/E) bay. It is part of the airframe structure (`eWTW-PBS-10`) and references ATLAS `050-059_Primary-Structures-and-Programme-Interfaces` for the structures domain.

Ownership boundary: this element owns **structure and installation provisions only**. Systems installed in or attached to it (avionics/IMA, ice/rain protection, weather radar, nose gear) are owned by their own PBS branches and referenced, never contained.

## 6. Traceability anchors

| Layer | Anchor |
|---|---|
| PBS | `eWTW-PBS-10-10-10` (this element) |
| Constituents | `eWTW-PBS-10-10-10-10 … -80` (§4) |
| Interfaces | child SSOT `interfaces.md` (IBS source) |
| Requirements | child SSOT `requirements.md` |
| CAD | per-leaf `cad/<tool>/<LC-stage>/<REV>/` (rule `CAD-REVDIR-001`) |
| Lifecycle | LC-letter model — `02_LIFECYCLE_MODEL/README.md` |
| Publication | `../../../../../../01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure/000-099_G-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces/053_Fuselage/053-100_Forward-Fuselage-Section/` (projection; rule `SSOT-AUTHORITY-001`) |
| Evidence | IEF anchor per object |

## 7. Footprint

| Field | Value |
|---|---|
| Document ID | `AMPEL360-eWTW-PBS-10-10-10-SSOT-README` |
| PBS ID | `eWTW-PBS-10-10-10` |
| Layer | SSOT (counterpart `../../../../../../01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure/000-099_G-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces/053_Fuselage/053-100_Forward-Fuselage-Section/`) |
| Register | Q-plus / OPTIONS |
| Owning Q-Division | Q-STRUCTURES |
| ATLAS reference | `050-059_Primary-Structures-and-Programme-Interfaces` |
| Effectivity | eWTW · baseline · MSN-001..050 · active |
| Version | 1.0.0 |
| Status | draft |
| Evidence anchor (IEF) | `<sha256: to-be-stamped-at-commit>` |

**Change log.**

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-05-31 | Initial SSOT authority README for the Forward Fuselage Section. |
