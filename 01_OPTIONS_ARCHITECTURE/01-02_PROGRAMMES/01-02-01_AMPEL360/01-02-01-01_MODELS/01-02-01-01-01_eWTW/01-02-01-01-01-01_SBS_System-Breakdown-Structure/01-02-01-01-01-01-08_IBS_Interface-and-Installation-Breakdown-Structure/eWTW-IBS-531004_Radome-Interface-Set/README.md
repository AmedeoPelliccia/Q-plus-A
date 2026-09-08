---
status: draft
ibs_id: eWTW-IBS-531004
parent: eWTW-PBS-053-100-000
serves_pbs: eWTW-PBS-053-100-040
item_type: interface_set
item_name: Radome Interface Set
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · IBS-531004 — Radome Interface Set

- **Serves PBS element:** `eWTW-PBS-053-100-040` (Radome and Diverters Attach Structure)
- **Parent PBS node:** `eWTW-PBS-053-100-000` (Nose and Forward Fuselage Structure)
- **Effectivity:** eWTW · baseline · MSN-001..050 · active

## Scope

Controls the **interfaces and installation envelope** of the radome — the integration relationships that connect the radome to its neighbouring product elements and systems. These are interface *records* (ICDs, envelopes, datums, tolerances), not parts: the physical radome and its installed hardware are owned in the PBS as the PN tree of the station (`EWTW-531004-000` under `eWTW-PBS-053-100-040`).

Per rule **SBS-INTERFACE-INSTALLATION-001**, the radome's diverter-strip bonding interface and weather-radar RF window are controlled here, while the lightning-protection function (taxonomy chapter `024`) and the radar antenna (weather radar, taxonomy chapter `034`) remain owned by their own chapters.

## Interface records

| IBS ID | Record | Interface type | Other side |
|---|---|---|---|
| `eWTW-IBS-531004-538001` | [Radome → Forward Pressure Bulkhead](eWTW-IBS-531004-538001_Radome-to-Forward-Pressure-Bulkhead.md) | Structural / hinge-latch attachment | `eWTW-PBS-053-800-010` |
| `eWTW-IBS-531004-034` | [Radome → Weather Radar](eWTW-IBS-531004-034_Radome-to-Weather-Radar.md) | RF window + access envelope + clearance | taxonomy `034` |
| `eWTW-IBS-531004-024` | [Radome → Lightning Protection](eWTW-IBS-531004-024_Radome-to-Lightning-Protection.md) | Bonded diverter / lightning provision | taxonomy `024` |
| `eWTW-IBS-531004-INST` | [Radome Removal/Installation Envelope](eWTW-IBS-531004-INST_Radome-Removal-Installation-Envelope.md) | Access / removal clearance | maintenance envelope |
| `eWTW-IBS-531004-TOL` | [Radome Tolerance and Datum Stack](eWTW-IBS-531004-TOL_Radome-Tolerance-and-Datum-Stack.md) | Datum alignment / tolerance stack | nose datum frame |

## Cross-references

- **PBS** — radome station [`…/eWTW-PBS-053-100-040_Radome-and-Diverters-Attach-Structure/README.md`](../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-000_Aircraft-Product/eWTW-PBS-050_Airframe-Structure/eWTW-PBS-053-000_Fuselage-Wide-Tube/eWTW-PBS-053-100-000_Nose-and-Forward-Fuselage-Structure/eWTW-PBS-053-100-040_Radome-and-Diverters-Attach-Structure/README.md) — owns the physical radome attach structure and its provisions.
- **PUB / DM** — radome remove/install data modules (`…-520A` remove, `…-720A` install) control the installation *task*; this IBS controls the installation *boundary*.
