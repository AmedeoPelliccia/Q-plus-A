---
document_id: AMPEL360-eWTW-IBS-531004-538001
title: "eWTW · IBS-531004-538001 — Radome to Forward Pressure Bulkhead"
ibs_id: eWTW-IBS-531004-538001
parent: eWTW-IBS-531004
item_type: interface_record
interface_class: structural
side_a: eWTW-PBS-053-100-040
side_b: eWTW-PBS-053-800-010
status: draft
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · IBS-531004-538001 — Radome to Forward Pressure Bulkhead

- **Side A:** `eWTW-PBS-053-100-040` (Radome and Diverters Attach Structure)
- **Side B:** `eWTW-PBS-053-800-010` (Forward Pressure Bulkhead)
- **Interface class:** Structural / hinge-latch attachment
- **Effectivity:** eWTW · baseline · MSN-001..050 · active

## Interface definition

Controls the mechanical attachment of the radome to the forward pressure bulkhead: the hinge/latch line that allows the radome to swing open for radar access, and the closed-position attachment pattern that reacts aerodynamic, bird-strike and handling loads.

| Attribute | Value |
|---|---|
| Interface type | Hinge-latch + bolted attachment pattern |
| Load path | Aero / bird-strike / handling reacted into the forward pressure bulkhead |
| Attachment pattern | TBD (fastener pitch, hinge axis, latch positions) |
| Clearance | TBD closed-gap and seal-land clearance |
| Ownership note | Hinge/latch fittings owned by the radome station (`eWTW-PBS-053-100-040`, PNs `EWTW-531004-020` / `EWTW-531004-030`); the bulkhead lands owned by `eWTW-PBS-053-800-010` |

## Constraints

- The attachment shall allow **repeated removal/installation** without degrading sealing or bonding performance (see `…-INST` envelope and `…-024` LPS records).
- Closed-position attachment shall hold the radome within the datum/tolerance stack of `…-TOL`.

## References

- PBS radome station — [`../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-000_Aircraft-Product/eWTW-PBS-050_Airframe-Structure/eWTW-PBS-053-000_Fuselage-Wide-Tube/eWTW-PBS-053-100-000_Nose-and-Forward-Fuselage-Structure/eWTW-PBS-053-100-040_Radome-and-Diverters-Attach-Structure/README.md`](../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-000_Aircraft-Product/eWTW-PBS-050_Airframe-Structure/eWTW-PBS-053-000_Fuselage-Wide-Tube/eWTW-PBS-053-100-000_Nose-and-Forward-Fuselage-Structure/eWTW-PBS-053-100-040_Radome-and-Diverters-Attach-Structure/README.md)
- Interface set index — [`README.md`](README.md)
