---
document_id: AMPEL360-eWTW-IBS-10-10-10-10-20
title: "eWTW · IBS-10-10-10-10-20 — Radome to Weather Radar (WXR)"
ibs_id: eWTW-IBS-10-10-10-10-20
parent: eWTW-IBS-10-10-10-10
item_type: interface_record
interface_class: rf_and_access
side_a: eWTW-PBS-10-10-10-10-10
side_b: eWTW-PBS-50-30/40
status: draft
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · IBS-10-10-10-10-20 — Radome to Weather Radar (WXR)

- **Side A:** `eWTW-PBS-10-10-10-10-10` (Radome)
- **Side B:** `eWTW-PBS-50-30/40` (Weather-radar antenna — referenced, not owned)
- **Interface class:** RF window + access envelope + clearance
- **Effectivity:** eWTW · baseline · MSN-001..050 · active

## Interface definition

Controls the radio-frequency window and physical clearance between the radome and the weather-radar antenna behind it. The **RF transmission/boresight requirement flows in from the radar system** (Side B); the radome (Side A) must realize it. This interface carries that RF specification explicitly so the radome is verified against the radar's actual need.

| Attribute | Value |
|---|---|
| RF specification source | WXR system (`eWTW-PBS-50-30/40`) — referenced |
| Transmission loss / boresight budget | TBD (allocated from radar performance) |
| Antenna sweep envelope | TBD scan volume + clearance to radome inner wall |
| Access envelope | TBD clearance for antenna installation/removal |
| Ownership note | Radome owns the RF window realization; radar antenna owned by WXR (not contained) |

## Constraints

- The radome wall construction shall meet the transmission/boresight budget **referenced** from the WXR system; this IBS does not redefine the radar requirement.
- Moisture ingress into the core degrades transmission — sealing/drainage (radome-owned) is RF-critical at this interface.

## References

- PBS radome element — [`../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-10_Airframe-Structure/eWTW-PBS-10-10_Fuselage-Wide-Tube/eWTW-PBS-10-10-10_Forward-Fuselage-Section/eWTW-PBS-10-10-10-10_Nose-Structure-and-Radome-Backup/eWTW-PBS-10-10-10-10-10_Radome/README.md`](../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-10_Airframe-Structure/eWTW-PBS-10-10_Fuselage-Wide-Tube/eWTW-PBS-10-10-10_Forward-Fuselage-Section/eWTW-PBS-10-10-10-10_Nose-Structure-and-Radome-Backup/eWTW-PBS-10-10-10-10-10_Radome/README.md)
- Interface set index — [`README.md`](README.md)
