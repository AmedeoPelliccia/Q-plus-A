---
document_id: AMPEL360-eWTW-IBS-531004-024
title: "eWTW · IBS-531004-024 — Radome to Lightning Protection"
ibs_id: eWTW-IBS-531004-024
parent: eWTW-IBS-531004
item_type: interface_record
interface_class: lightning_bonding
side_a: eWTW-PBS-053-100-040
side_b: "024"
side_b_space: taxonomy
status: draft
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · IBS-531004-024 — Radome to Lightning Protection

- **Side A:** `eWTW-PBS-053-100-040` (Radome and Diverters Attach Structure)
- **Side B:** taxonomy chapter `024` (bonding and lightning protection — referenced, not owned)
- **Interface class:** Bonded diverter / lightning provision
- **Effectivity:** eWTW · baseline · MSN-001..050 · active

## Interface definition

Controls the bonded interface between the radome and the lightning-protection system. The composite radome is non-conductive, so lightning protection relies on **diverter strips owned by the LPS** (Side B) bonded to the radome surface. The radome (Side A) provides only the **mounting and bonding provisions**.

| Attribute | Value |
|---|---|
| Diverter strips | Carried by the station (PN `EWTW-531004-040`); the protection function is owned by taxonomy chapter `024` — referenced |
| Radome provision | Bonding pads / diverter routing land — radome-owned provision |
| Zone | Forward nose, lightning Zone 1A |
| Bonding resistance | TBD continuity to airframe ground |
| Ownership note | Provision-only interface; diverters and bonding function owned by LPS |

## Constraints

- The radome shall **not** become a preferred lightning attachment path that bypasses the diverters — a safety defect even if structurally sound.
- Any change to diverter provisions requires re-verification of the lightning Zone 1A case (coupled with the bird-strike and RF cases on the radome).

## References

- PBS radome station — [`../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-000_Aircraft-Product/eWTW-PBS-050_Airframe-Structure/eWTW-PBS-053-000_Fuselage-Wide-Tube/eWTW-PBS-053-100-000_Nose-and-Forward-Fuselage-Structure/eWTW-PBS-053-100-040_Radome-and-Diverters-Attach-Structure/README.md`](../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-000_Aircraft-Product/eWTW-PBS-050_Airframe-Structure/eWTW-PBS-053-000_Fuselage-Wide-Tube/eWTW-PBS-053-100-000_Nose-and-Forward-Fuselage-Structure/eWTW-PBS-053-100-040_Radome-and-Diverters-Attach-Structure/README.md)
- Interface set index — [`README.md`](README.md)
