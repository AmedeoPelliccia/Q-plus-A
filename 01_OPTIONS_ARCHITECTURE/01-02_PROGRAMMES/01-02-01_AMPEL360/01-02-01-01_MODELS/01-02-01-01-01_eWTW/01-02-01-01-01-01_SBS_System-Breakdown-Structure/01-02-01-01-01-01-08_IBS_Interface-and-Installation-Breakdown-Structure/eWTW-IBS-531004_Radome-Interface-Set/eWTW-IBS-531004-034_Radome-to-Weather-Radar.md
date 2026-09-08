---
document_id: AMPEL360-eWTW-IBS-531004-034
title: "eWTW · IBS-531004-034 — Radome to Weather Radar"
ibs_id: eWTW-IBS-531004-034
parent: eWTW-IBS-531004
item_type: interface_record
interface_class: rf_and_access
side_a: eWTW-PBS-053-100-040
side_b: "034"
side_b_space: taxonomy
status: draft
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · IBS-531004-034 — Radome to Weather Radar

- **Side A:** `eWTW-PBS-053-100-040` (Radome and Diverters Attach Structure)
- **Side B:** taxonomy chapter `034` (Weather-radar antenna — referenced, not owned)
- **Interface class:** RF window + access envelope + clearance
- **Effectivity:** eWTW · baseline · MSN-001..050 · active

## Interface definition

Controls the radio-frequency window and physical clearance between the radome and the weather-radar antenna behind it. The **RF transmission/boresight requirement flows in from the radar system** (Side B); the radome (Side A) must realize it. This interface carries that RF specification explicitly so the radome is verified against the radar's actual need.

| Attribute | Value |
|---|---|
| RF specification source | WXR system (taxonomy chapter `034`) — referenced |
| Transmission loss / boresight budget | TBD (allocated from radar performance) |
| Antenna sweep envelope | TBD scan volume + clearance to radome inner wall |
| Access envelope | TBD clearance for antenna installation/removal |
| Ownership note | Radome owns the RF window realization; radar antenna owned by WXR (not contained) |

## Constraints

- The radome wall construction shall meet the transmission/boresight budget **referenced** from the WXR system; this IBS does not redefine the radar requirement.
- Moisture ingress into the core degrades transmission — sealing/drainage (radome-owned) is RF-critical at this interface.

## References

- PBS radome station — [`../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-000_Aircraft-Product/eWTW-PBS-050_Airframe-Structure/eWTW-PBS-053-000_Fuselage-Wide-Tube/eWTW-PBS-053-100-000_Nose-and-Forward-Fuselage-Structure/eWTW-PBS-053-100-040_Radome-and-Diverters-Attach-Structure/README.md`](../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-000_Aircraft-Product/eWTW-PBS-050_Airframe-Structure/eWTW-PBS-053-000_Fuselage-Wide-Tube/eWTW-PBS-053-100-000_Nose-and-Forward-Fuselage-Structure/eWTW-PBS-053-100-040_Radome-and-Diverters-Attach-Structure/README.md)
- Interface set index — [`README.md`](README.md)
