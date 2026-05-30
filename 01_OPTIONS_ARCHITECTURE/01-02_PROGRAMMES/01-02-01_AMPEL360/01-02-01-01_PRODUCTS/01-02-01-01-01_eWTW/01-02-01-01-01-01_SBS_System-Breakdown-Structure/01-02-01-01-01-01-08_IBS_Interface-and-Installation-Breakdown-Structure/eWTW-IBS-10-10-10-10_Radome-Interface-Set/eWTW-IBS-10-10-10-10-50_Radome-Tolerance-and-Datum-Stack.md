---
document_id: AMPEL360-eWTW-IBS-10-10-10-10-50
title: "eWTW · IBS-10-10-10-10-50 — Radome Tolerance and Datum Stack"
ibs_id: eWTW-IBS-10-10-10-10-50
parent: eWTW-IBS-10-10-10-10
item_type: interface_record
interface_class: datum_tolerance
serves_pbs: eWTW-PBS-10-10-10-10-10
status: draft
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · IBS-10-10-10-10-50 — Radome Tolerance and Datum Stack

- **Serves PBS element:** `eWTW-PBS-10-10-10-10-10` (Radome)
- **Interface class:** Datum alignment / tolerance stack
- **Effectivity:** eWTW · baseline · MSN-001..050 · active

## Interface definition

Controls the **datum reference frame and tolerance stack-up** that positions the radome relative to the nose datum and the radar boresight axis. Misalignment couples directly into boresight error, so the datum/tolerance budget is an RF-relevant interface, not only a structural fit.

| Attribute | Value |
|---|---|
| Primary datum | Nose / forward-fuselage datum frame — TBD |
| Boresight reference | Radar boresight axis (from WXR, see `…-20`) |
| Tolerance stack | TBD attachment-pattern, hinge-axis and seal-land budget |
| Aerodynamic continuity | TBD step/gap to nose cap (`eWTW-PBS-10-10-10-10-30`) |
| Allocation note | Boresight budget allocated jointly with WXR interface `…-20` |

## Constraints

- Re-installation after removal (`…-40`) shall return the radome within this stack without re-shimming beyond the allowed budget.
- Any change to the attachment pattern (`…-10`) shall be re-checked against this datum/tolerance stack and the boresight allocation.

## References

- WXR interface (boresight source) — [`eWTW-IBS-10-10-10-10-20_Radome-to-WXR.md`](eWTW-IBS-10-10-10-10-20_Radome-to-WXR.md)
- Interface set index — [`README.md`](README.md)
