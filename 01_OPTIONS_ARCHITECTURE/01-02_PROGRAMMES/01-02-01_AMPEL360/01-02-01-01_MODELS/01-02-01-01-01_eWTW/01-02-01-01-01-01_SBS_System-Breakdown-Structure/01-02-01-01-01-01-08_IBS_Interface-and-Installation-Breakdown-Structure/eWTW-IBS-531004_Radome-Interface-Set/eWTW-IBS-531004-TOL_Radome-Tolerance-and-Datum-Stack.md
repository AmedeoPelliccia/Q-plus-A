---
document_id: AMPEL360-eWTW-IBS-531004-TOL
title: "eWTW · IBS-531004-TOL — Radome Tolerance and Datum Stack"
ibs_id: eWTW-IBS-531004-TOL
parent: eWTW-IBS-531004
item_type: interface_record
interface_class: datum_tolerance
serves_pbs: eWTW-PBS-053-100-040
status: draft
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · IBS-531004-TOL — Radome Tolerance and Datum Stack

- **Serves PBS element:** `eWTW-PBS-053-100-040` (Radome and Diverters Attach Structure)
- **Interface class:** Datum alignment / tolerance stack
- **Effectivity:** eWTW · baseline · MSN-001..050 · active

## Interface definition

Controls the **datum reference frame and tolerance stack-up** that positions the radome relative to the nose datum and the radar boresight axis. Misalignment couples directly into boresight error, so the datum/tolerance budget is an RF-relevant interface, not only a structural fit.

| Attribute | Value |
|---|---|
| Primary datum | Nose / forward-fuselage datum frame — TBD |
| Boresight reference | Radar boresight axis (from WXR, see `…-034`) |
| Tolerance stack | TBD attachment-pattern, hinge-axis and seal-land budget |
| Aerodynamic continuity | TBD step/gap to nose cap (`EWTW-531004-000`) |
| Allocation note | Boresight budget allocated jointly with WXR interface `…-034` |

## Constraints

- Re-installation after removal (`…-INST`) shall return the radome within this stack without re-shimming beyond the allowed budget.
- Any change to the attachment pattern (`…-538001`) shall be re-checked against this datum/tolerance stack and the boresight allocation.

## References

- WXR interface (boresight source) — [`eWTW-IBS-531004-034_Radome-to-Weather-Radar.md`](eWTW-IBS-531004-034_Radome-to-Weather-Radar.md)
- Interface set index — [`README.md`](README.md)
