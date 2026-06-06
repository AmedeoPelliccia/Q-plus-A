---
document_id: AMPEL360-eWTW-PBS-10-10-10-10-10-DEF
title: "eWTW · PBS-10-10-10-10-10 — Radome · Product Definition"
pbs_id: eWTW-PBS-10-10-10-10-10
parent: eWTW-PBS-10-10-10-10
part_number: PN-eWTW-5310-0001
item_class: physical_part
item_name: Radome
owning_q_division: Q-STRUCTURES
support_q_divisions:
  - Q-AIR
  - Q-DATAGOV
  - Q-HORIZON
revision: A
status: draft
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
related_files:
  pnr: pnr.yaml
  bom_yaml: bom.yaml
  bom_csv: bom.csv
  geometry_material: geometry-material-spec.md
  evidence: evidence/evidence-register.yaml
  pub: pub/README.md
  cad_native: REV-A1/FreeCAD/eWTW-PBS-10-10-10-10-10-Radome.FCStd
  cad_step: cad/step/eWTW-PBS-10-10-10-10-10-Radome.step
  drawing: drawings/eWTW-PBS-10-10-10-10-10-Radome-Drawing.pdf
---

# eWTW · PBS-10-10-10-10-10 — Radome · Product Definition

- **PBS ID:** `eWTW-PBS-10-10-10-10-10`
- **Part Number:** `PN-eWTW-5310-0001`
- **Parent:** `eWTW-PBS-10-10-10-10` — Nose Structure and Radome Backup
- **Owning division:** Q-STRUCTURES
- **Status:** draft · Rev A · eWTW baseline · MSN-001..050 · active

---

## 1. Product Identity

The **Radome** (`eWTW-PBS-10-10-10-10-10`) is the RF-transparent nose fairing of the eWTW forward fuselage. It is the forwardmost structural element, enclosing the weather-radar antenna and providing the aircraft nose aerodynamic surface.

| Field | Value |
|---|---|
| PBS ID | `eWTW-PBS-10-10-10-10-10` |
| Part Number | `PN-eWTW-5310-0001` |
| Item class | Physical part |
| Item type | Detail part |
| Revision | A |
| Lifecycle state | draft |
| Make / buy | TBD |
| CAD required | Yes |
| BOM required | Yes |

---

## 2. Product Role

The radome performs three concurrent product roles:

1. **Aerodynamic nose surface** — provides the forward fuselage aero contour.
2. **Radio-frequency window** — the composite wall is designed to be transparent to the weather-radar signal; wall construction (A-sandwich, core permittivity, skin thickness) is tuned to the radar frequency band.
3. **Forward bird-strike and lightning-attachment surface** — the radome is the forwardmost surface and is in Lightning Zone 1A.

> [!IMPORTANT]
> The radome sits **forward of the forward pressure bulkhead (FPB)** and is therefore **unpressurized**. Cabin pressurization is **not** a structural driver for the radome. Treating it as part of the pressure boundary is an error.

The central design tension: the radome is owned as *structure* (Q-STRUCTURES) but its governing performance requirement — RF transmission efficiency and boresight error — is **set by the weather-radar system** (`eWTW-PBS-50-30/40`, Q-AIR/avionics). The radome realizes a requirement it does not own; the interface is tightly governed via the WXR ICD.

---

## 3. Constituent Summary

| Child PN | Constituent | Ownership |
|---|---|---|
| `PN-eWTW-5310-0001-01` | Outer RF-transparent laminate skin | Owned |
| `PN-eWTW-5310-0001-02` | Dielectric core A-sandwich | Owned; permittivity RF-critical |
| `PN-eWTW-5310-0001-03` | Inner RF-transparent laminate skin | Owned |
| `PN-eWTW-5310-0001-04` | Rain erosion boot / coating | Owned |
| `PN-eWTW-5310-0001-05` | Attachment, hinge, and latch fittings | Owned; interface to `PBS-10-10-10-10-20` |
| `PN-eWTW-5310-0001-06` | Moisture seal and drainage provisions | Owned; RF-critical |
| `PN-eWTW-5310-0001-07` | Bonding and ground provisions | Provision only — LPS function (`PBS-40-40`) |
| `REF-eWTW-LPS-DIVERTER` | Lightning diverter strips | **LPS-owned** — reference only |
| `REF-eWTW-WXR-ANTENNA` | Weather radar antenna | **WXR-owned** — reference only |

See `bom.yaml` and `bom.csv` for full BOM records.

---

## 4. Interfaces

| Interface | Type | Other-side owner |
|---|---|---|
| Radome backup bulkhead | Structural / hinge-latch | `eWTW-PBS-10-10-10-10-20` |
| Nose cap / forward fairing | Aerodynamic surface continuity | `eWTW-PBS-10-10-10-10-30` |
| Weather-radar antenna | RF window + access + clearance envelope | `eWTW-PBS-50-30/40` |
| Lightning protection (diverters / bonding) | Provision / bonded strip interface | `eWTW-PBS-40-40` |

---

## 5. Key Requirements

| Requirement | Driver | Owner of requirement |
|---|---|---|
| RF transmission efficiency | Weather-radar system performance | `eWTW-PBS-50-30/40` (WXR) |
| Boresight error | Weather-radar system performance | `eWTW-PBS-50-30/40` (WXR) |
| Bird strike | CS-25 / FAR-25 | Certification basis |
| Lightning — Zone 1A | CS-25 Appendix H | Certification basis |
| Rain erosion | Surface durability / RF degradation | Q-STRUCTURES |
| Moisture ingress | RF-critical (core εr degrades when wet) | Q-STRUCTURES |
| Removability / access | Radar maintenance cycle | Q-AIR / MRO |

---

## 6. Geometry and Material

See [`geometry-material-spec.md`](geometry-material-spec.md) for wall construction baseline, dielectric properties, interface envelopes, and verification summary. All dimensional values are TBD pending RF and structural substantiation.

**CAD authority:**
- Native model: `REV-A1/FreeCAD/eWTW-PBS-10-10-10-10-10-Radome.FCStd`
- Exchange: `cad/step/eWTW-PBS-10-10-10-10-10-Radome.step`
- Drawing: `drawings/eWTW-PBS-10-10-10-10-10-Radome-Drawing.pdf`

---

## 7. Part Number Register

See [`pnr.yaml`](pnr.yaml).

> **Rule:** The PBS ID (`eWTW-PBS-10-10-10-10-10`) is the architecture/product-structure identifier. The part number (`PN-eWTW-5310-0001`) is the PLM-controlled manufacturing and procurement identifier. They shall not be collapsed.

---

## 8. Evidence

See [`evidence/evidence-register.yaml`](evidence/evidence-register.yaml).

Evidence anchors are stamped at commit under the IEF (Integrated Evidence Framework). Planned evidence items: RF range test, bird-strike test, lightning test, rain-erosion qualification, moisture + RF combined test.

---

## 9. Publication Hooks

See [`pub/README.md`](pub/README.md).

| Publication folder | Info-code | Topic |
|---|---|---|
| `pub/040_descriptive/` | 040 | Radome description |
| `pub/258_bonding-and-lightning-check/` | 258 | Lightning-diverter bonding check |
| `pub/310_inspection-general/` | 310 | General visual inspection |
| `pub/520_removal/` | 520 | Radome removal |
| `pub/720_installation/` | 720 | Radome installation |
| `pub/941_illustrated-parts-data/` | 941 | Illustrated parts data |

---

## 10. Traceability Map

| Layer | Identifier | File |
|---|---|---|
| PBS | `eWTW-PBS-10-10-10-10-10` | `README.md` (this folder) |
| Product definition | `AMPEL360-eWTW-PBS-10-10-10-10-10-DEF` | `eWTW-PBS-10-10-10-10-10_Radome.md` |
| PNR | `PNR-eWTW-PBS-10-10-10-10-10` | `pnr.yaml` |
| PN | `PN-eWTW-5310-0001` | `pnr.yaml` |
| BOM | `BOM-eWTW-PBS-10-10-10-10-10` | `bom.yaml` / `bom.csv` |
| Geometry & material | `AMPEL360-eWTW-PBS-10-10-10-10-10-GMS` | `geometry-material-spec.md` |
| CAD native | `eWTW-PBS-10-10-10-10-10-Radome.FCStd` | `REV-A1/FreeCAD/` |
| CAD exchange | `eWTW-PBS-10-10-10-10-10-Radome.step` | `cad/step/` |
| Drawing | `eWTW-PBS-10-10-10-10-10-Radome-Drawing.pdf` | `drawings/` |
| Evidence | `EVID-eWTW-PBS-10-10-10-10-10` | `evidence/evidence-register.yaml` |
| Publication | — | `pub/` |

---

## 11. Change Log

| Version | Date | Author / Division | Change |
|---|---|---|---|
| 1.0.0 | 2026-05-29 | Q-STRUCTURES | Initial product definition document for `eWTW-PBS-10-10-10-10-10` Radome. |
