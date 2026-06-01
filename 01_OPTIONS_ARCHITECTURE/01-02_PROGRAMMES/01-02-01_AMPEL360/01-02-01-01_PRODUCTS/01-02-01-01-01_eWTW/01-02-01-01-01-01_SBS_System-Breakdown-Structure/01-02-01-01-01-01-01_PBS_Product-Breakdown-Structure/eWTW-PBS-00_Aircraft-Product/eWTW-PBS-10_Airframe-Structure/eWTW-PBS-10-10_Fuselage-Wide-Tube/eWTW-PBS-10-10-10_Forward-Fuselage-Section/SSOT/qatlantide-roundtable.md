---
document_id: AMPEL360-eWTW-PBS-10-10-10-QATL-ROUNDTABLE
title: "eWTW · PBS-10-10-10 — Q+ATLANTIDE Round Table (Impact Analysis)"
register: Q-plus
architecture: OPTIONS_ARCHITECTURE
options_axis: P-Programmes
programme: AMPEL360
product: eWTW
pbs_id: eWTW-PBS-10-10-10
pbs_title: "Forward Fuselage Section"
layer: SSOT
artefact_type: qatlantide_impact_analysis
source_register: "Q+ATLANTIDE1000 (Libro Unico delle Tecnologie)"
generation: snapshot                 # snapshot | live-query
primary_q_division: Q-STRUCTURES
support_q_divisions:
  - Q-DATAGOV
  - Q-HORIZON
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

# eWTW · PBS-10-10-10 — Q+ATLANTIDE Round Table (Impact Analysis)

![SSOT](https://img.shields.io/badge/layer-SSOT-2d7a2d)
![impact-analysis](https://img.shields.io/badge/type-Q%2BATLANTIDE%20impact-6d4c9e)
![snapshot](https://img.shields.io/badge/generation-snapshot-0075ca)

## 1. Purpose

The **Q+ATLANTIDE round table** records which nodes of the *Libro Unico delle Tecnologie* (`Q+ATLANTIDE1000`) the Forward Fuselage Section impacts, **how** (typed relation), and **under which effectivity**. It is the element's projection onto the technology register — an applicability-filtered impact analysis, not a technology definition.

It **references** Q+ATLANTIDE node IDs; it never redefines them. The technology truth lives in `01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/`. This artefact is the *edge*, not the *node*.

## 2. Rules

```yaml
qatlantide_roundtable_rules:
  - id: QATL-RT-001
    rule: >
      The round table references Q+ATLANTIDE node IDs only. It shall not contain
      technology definitions. Cross-reference, never cross-containment.
  - id: QATL-RT-002
    rule: >
      Every impacted node carries a typed impact relation and an effectivity
      filter. An untyped or effectivity-less impact row is invalid.
  - id: QATL-RT-003
    rule: >
      This is a stored snapshot regenerable from Q+ATLANTIDE + effectivity +
      impact analysis. It carries a provenance stamp and a regeneration trigger:
      any change to a referenced Q+ATLANTIDE node re-opens this table for review.
```

### Impact-relation vocabulary

| Relation | Meaning |
|---|---|
| `used-by` | The element uses this technology domain as-is. |
| `constrained-by` | The element's design is constrained by this domain (interface/provision). |
| `modified-for` | The element is modified relative to baseline because of this domain. |
| `newly-required-by` | This domain newly requires something of the element. |
| `retired-by` | This domain retires/removes a prior element feature. |

## 3. Round table — impacted Q+ATLANTIDE nodes

Element: `eWTW-PBS-10-10-10` Forward Fuselage Section · effectivity `eWTW · baseline · MSN-001..050`.

| Q+ATLANTIDE node | Band | Relation | Criticality | Basis |
|---|---|---|---|---|
| `050-059_Estructuras` | ATLAS | `used-by` | high | Primary structural domain; the element *is* airframe structure. |
| Fuselage / forward-section node *(TBC)* | ATLAS | `used-by` | high | Section-level structural node; node consolidation pending. |
| `030-039_Proteccion-y-Sistemas-Mecanicos` | ATLAS | `constrained-by` | high | Lightning Zone 1A and ice/rain protection on nose/radome drive structural provisions. |
| `040-049_Avionica-Informacion-y-APU` | ATLAS | `constrained-by` | medium | E/E bay structure sized and accessed for avionics/IMA install. |
| `020-029_Sistemas-Core-de-Aeronave` | ATLAS | `constrained-by` | medium | Local routing/bonding provisions for wiring and ducting. |
| `010-019_Manejo-en-Tierra-Servicio` | ATLAS | `used-by` | low | Forward access and servicing interfaces. |
| `500-599_AMTA` (advanced materials) | AMTA | `used-by` | high | Composite skins, frames, and sandwich materials (cross-band). |
| `800-899_CYB` | CYB | `constrained-by` | low | E/E bay EMI/HIRF shielding provisions (interface to cyber-resilient avionics). |

### Electric-architecture-specific impact

| Q+ATLANTIDE node | Relation | Criticality | Basis |
|---|---|---|---|
| `040-049_Avionica` + `800-899_CYB` | `modified-for` | medium | The eWTW electric architecture raises avionics/power-electronics density, so the E/E bay structure is **modified-for** elevated thermal and HIRF-shielding provisions relative to a conventional regional aircraft. |

No `newly-required-by` or `retired-by` rows at baseline. The `modified-for` row is the one genuine deviation the electric configuration imposes on this structural element.

## 4. Provenance and regeneration

```yaml
provenance:
  generated_from:
    - "Q+ATLANTIDE1000 node register (referenced IDs above)"
    - "element effectivity: eWTW / baseline / MSN-001..050"
    - "impact analysis: Q-STRUCTURES, 2026-05-31"
  regeneration_trigger: >
    Any change to a referenced Q+ATLANTIDE node, or to the element effectivity,
    re-opens this table for review (rule QATL-RT-003).
  evidence_anchor: "<sha256: to-be-stamped-at-commit>"
```

## 5. Change-impact use

This table is the element's entry in the change-impact spine: a change to any referenced Q+ATLANTIDE node can be queried back to every element that references it. For this element, a change to `030-039 Protección` (e.g. revised lightning zoning) or `500-599 AMTA` (e.g. material substitution) directly re-opens the structural provisions — high-criticality edges flagged accordingly.

## 6. Footprint

| Field | Value |
|---|---|
| Document ID | `AMPEL360-eWTW-PBS-10-10-10-QATL-ROUNDTABLE` |
| PBS ID | `eWTW-PBS-10-10-10` |
| Artefact type | Q+ATLANTIDE impact analysis (round table) |
| Source register | `Q+ATLANTIDE1000` (Libro Unico delle Tecnologie) |
| Generation | snapshot (regenerable; provenance §4) |
| Layer | SSOT |
| Owning Q-Division | Q-STRUCTURES |
| Effectivity | eWTW · baseline · MSN-001..050 · active |
| Version | 1.0.0 |
| Status | draft |
| Evidence anchor (IEF) | `<sha256: to-be-stamped-at-commit>` |

**Change log.**

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-05-31 | Initial Q+ATLANTIDE round table for the Forward Fuselage Section; typed, effectivity-filtered, snapshot generation. |
