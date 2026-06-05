# 006-200 — Stations, Zones & Major Areas — TPuBS Node (pattern)

> **TPuBS publication entry** following the worked `053-100` pattern.
> **Impact on:** `eWTW-PBS-10-10-10_Forward-Fuselage-Section` — Fuselage stations
> **G-ATLAS SNS:** `000-009_General-Information-and-Service` → `006_Dimensions-and-Areas` → `006-200` ⇄ **ATA 06-20**
> **Programme:** AMPEL360 / eWTW · **Standard:** S1000D Issue 4.2

This node section carries the seven S1000D object classes for Stations, Zones & Major Areas content
impacted by the forward fuselage section. It follows the `053-100` worked
pattern identically; object folders are seeded and populated as DMs are authored.

| Folder | Contents |
|---|---|
| `APPLIC/` | Applicability (ACT / CCT / PCT) |
| `BREX/` | Business Rules Exchange DM |
| `DM/` | Data Modules (descriptive / procedural / fault / IPD) |
| `DMRL/` | Data Module Requirement List |
| `ICN/` | Illustrations & multimedia |
| `PM/` | Publication Modules |
| `SSOT/` | Traceability manifest → G-ATLAS standard nodes |

```yaml
Last.MarkedDown:
  node: 006-200
  title: Stations, Zones & Major Areas
  from_pbs: eWTW-PBS-10-10-10
  ata_ref: 06-20
  model_ident_code: EWTW
  impact: "Fuselage stations"
  status: pattern
```
