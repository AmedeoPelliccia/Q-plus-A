---
document_id: AMPEL360-eWTW-IBS-10-10-10-10-30
title: "eWTW · IBS-10-10-10-10-30 — Radome to Lightning Protection (LPS)"
ibs_id: eWTW-IBS-10-10-10-10-30
parent: eWTW-IBS-10-10-10-10
item_type: interface_record
interface_class: lightning_bonding
side_a: eWTW-PBS-10-10-10-10-10
side_b: eWTW-PBS-40-40
status: draft
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · IBS-10-10-10-10-30 — Radome to Lightning Protection (LPS)

- **Side A:** `eWTW-PBS-10-10-10-10-10` (Radome)
- **Side B:** `eWTW-PBS-40-40` (Lightning Protection System — referenced, not owned)
- **Interface class:** Bonded diverter / lightning provision
- **Effectivity:** eWTW · baseline · MSN-001..050 · active

## Interface definition

Controls the bonded interface between the radome and the lightning-protection system. The composite radome is non-conductive, so lightning protection relies on **diverter strips owned by the LPS** (Side B) bonded to the radome surface. The radome (Side A) provides only the **mounting and bonding provisions**.

| Attribute | Value |
|---|---|
| Diverter strips | Owned by LPS (`eWTW-PBS-40-40`) — referenced, not radome-owned |
| Radome provision | Bonding pads / diverter routing land — radome-owned provision |
| Zone | Forward nose, lightning Zone 1A |
| Bonding resistance | TBD continuity to airframe ground |
| Ownership note | Provision-only interface; diverters and bonding function owned by LPS |

## Constraints

- The radome shall **not** become a preferred lightning attachment path that bypasses the diverters — a safety defect even if structurally sound.
- Any change to diverter provisions requires re-verification of the lightning Zone 1A case (coupled with the bird-strike and RF cases on the radome).

## References

- PBS radome element — [`../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-10_Airframe-Structure/eWTW-PBS-10-10_Fuselage-Wide-Tube/eWTW-PBS-10-10-10_Forward-Fuselage-Section/eWTW-PBS-10-10-10-10_Nose-Structure-and-Radome-Backup/eWTW-PBS-10-10-10-10-10_Radome/README.md`](../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-10_Airframe-Structure/eWTW-PBS-10-10_Fuselage-Wide-Tube/eWTW-PBS-10-10-10_Forward-Fuselage-Section/eWTW-PBS-10-10-10-10_Nose-Structure-and-Radome-Backup/eWTW-PBS-10-10-10-10-10_Radome/README.md)
- Interface set index — [`README.md`](README.md)
