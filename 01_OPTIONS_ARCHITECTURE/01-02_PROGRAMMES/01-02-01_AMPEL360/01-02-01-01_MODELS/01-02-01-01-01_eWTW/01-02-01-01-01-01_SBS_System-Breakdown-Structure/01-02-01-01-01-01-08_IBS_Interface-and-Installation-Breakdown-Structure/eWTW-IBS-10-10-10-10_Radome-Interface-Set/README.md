---
status: draft
ibs_id: eWTW-IBS-10-10-10-10
parent: eWTW-PBS-10-10-10-10
serves_pbs: eWTW-PBS-10-10-10-10-10
item_type: interface_set
item_name: Radome Interface Set
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · IBS-10-10-10-10 — Radome Interface Set

- **Serves PBS element:** `eWTW-PBS-10-10-10-10-10` (Radome)
- **Parent PBS node:** `eWTW-PBS-10-10-10-10` (Nose Structure and Radome Backup)
- **Effectivity:** eWTW · baseline · MSN-001..050 · active

## Scope

Controls the **interfaces and installation envelope** of the radome — the integration relationships that connect the radome to its neighbouring product elements and systems. These are interface *records* (ICDs, envelopes, datums, tolerances), not parts: the physical radome and its installed hardware are owned in the PBS (`eWTW-PBS-10-10-10-10-10`).

Per rule **SBS-INTERFACE-INSTALLATION-001**, the radome's diverter-strip bonding interface and weather-radar RF window are controlled here, while the diverter strips (LPS, `eWTW-PBS-40-40`) and the radar antenna (WXR, `eWTW-PBS-50-30/40`) remain owned by their own systems.

## Interface records

| IBS ID | Record | Interface type | Other side |
|---|---|---|---|
| `eWTW-IBS-10-10-10-10-10` | [Radome → Backup Bulkhead](eWTW-IBS-10-10-10-10-10_Radome-to-Backup-Bulkhead.md) | Structural / hinge-latch attachment | `eWTW-PBS-10-10-10-10-20` |
| `eWTW-IBS-10-10-10-10-20` | [Radome → WXR](eWTW-IBS-10-10-10-10-20_Radome-to-WXR.md) | RF window + access envelope + clearance | `eWTW-PBS-50-30/40` |
| `eWTW-IBS-10-10-10-10-30` | [Radome → LPS](eWTW-IBS-10-10-10-10-30_Radome-to-LPS.md) | Bonded diverter / lightning provision | `eWTW-PBS-40-40` |
| `eWTW-IBS-10-10-10-10-40` | [Radome Removal/Installation Envelope](eWTW-IBS-10-10-10-10-40_Radome-Removal-Installation-Envelope.md) | Access / removal clearance | maintenance envelope |
| `eWTW-IBS-10-10-10-10-50` | [Radome Tolerance and Datum Stack](eWTW-IBS-10-10-10-10-50_Radome-Tolerance-and-Datum-Stack.md) | Datum alignment / tolerance stack | nose datum frame |

## Cross-references

- **PBS** — radome element [`…/eWTW-PBS-10-10-10-10-10_Radome/README.md`](../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-10_Airframe-Structure/eWTW-PBS-10-10_Fuselage-Wide-Tube/eWTW-PBS-10-10-10_Forward-Fuselage-Section/eWTW-PBS-10-10-10-10_Nose-Structure-and-Radome-Backup/eWTW-PBS-10-10-10-10-10_Radome/README.md) — owns the physical radome and its provisions.
- **PUB / DM** — radome remove/install data modules (`…-520A` remove, `…-720A` install) control the installation *task*; this IBS controls the installation *boundary*.
