---
document_id: AMPEL360-eWTW-IBS-10-10-10-10-10
title: "eWTW · IBS-10-10-10-10-10 — Radome to Backup Bulkhead"
ibs_id: eWTW-IBS-10-10-10-10-10
parent: eWTW-IBS-10-10-10-10
item_type: interface_record
interface_class: structural
side_a: eWTW-PBS-10-10-10-10-10
side_b: eWTW-PBS-10-10-10-10-20
status: draft
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · IBS-10-10-10-10-10 — Radome to Backup Bulkhead

- **Side A:** `eWTW-PBS-10-10-10-10-10` (Radome)
- **Side B:** `eWTW-PBS-10-10-10-10-20` (Radome Backup Bulkhead)
- **Interface class:** Structural / hinge-latch attachment
- **Effectivity:** eWTW · baseline · MSN-001..050 · active

## Interface definition

Controls the mechanical attachment of the radome to the backup bulkhead: the hinge/latch line that allows the radome to swing open for radar access, and the closed-position attachment pattern that reacts aerodynamic, bird-strike and handling loads.

| Attribute | Value |
|---|---|
| Interface type | Hinge-latch + bolted attachment pattern |
| Load path | Aero / bird-strike / handling reacted into backup bulkhead |
| Attachment pattern | TBD (fastener pitch, hinge axis, latch positions) |
| Clearance | TBD closed-gap and seal-land clearance |
| Ownership note | Hinge/latch fittings owned by the radome (PBS `…-10-10`); the bulkhead lands owned by PBS `…-10-20` |

## Constraints

- The attachment shall allow **repeated removal/installation** without degrading sealing or bonding performance (see `…-40` envelope and `…-30` LPS records).
- Closed-position attachment shall hold the radome within the datum/tolerance stack of `…-50`.

## References

- PBS radome element — [`../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-10_Airframe-Structure/eWTW-PBS-10-10_Fuselage-Wide-Tube/eWTW-PBS-10-10-10_Forward-Fuselage-Section/eWTW-PBS-10-10-10-10_Nose-Structure-and-Radome-Backup/eWTW-PBS-10-10-10-10-10_Radome/README.md`](../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-10_Airframe-Structure/eWTW-PBS-10-10_Fuselage-Wide-Tube/eWTW-PBS-10-10-10_Forward-Fuselage-Section/eWTW-PBS-10-10-10-10_Nose-Structure-and-Radome-Backup/eWTW-PBS-10-10-10-10-10_Radome/README.md)
- Interface set index — [`README.md`](README.md)
