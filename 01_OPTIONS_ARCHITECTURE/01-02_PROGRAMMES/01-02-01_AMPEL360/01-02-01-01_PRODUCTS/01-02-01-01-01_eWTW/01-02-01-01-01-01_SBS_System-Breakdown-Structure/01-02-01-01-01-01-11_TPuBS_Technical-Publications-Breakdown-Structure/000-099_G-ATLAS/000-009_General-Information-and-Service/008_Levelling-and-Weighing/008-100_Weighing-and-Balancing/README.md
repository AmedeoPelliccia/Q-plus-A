# 008-100 — Weighing & Balancing — TPuBS Node (pattern)

> **TPuBS publication entry** following the worked `053-100` pattern.
> **Impact on:** `eWTW-PBS-10-10-10_Forward-Fuselage-Section` — Mass/CG contribution
> **G-ATLAS SNS:** `000-009_General-Information-and-Service` → `008_Levelling-and-Weighing` → `008-100` ⇄ **ATA 08-10**
> **Programme:** AMPEL360 / eWTW · **Standard:** S1000D Issue 4.2

This node section carries the seven S1000D object classes for Weighing & Balancing content
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
  node: 008-100
  title: Weighing & Balancing
  from_pbs: eWTW-PBS-10-10-10
  ata_ref: 08-10
  model_ident_code: EWTW
  impact: "Mass/CG contribution"
  status: pattern
```
