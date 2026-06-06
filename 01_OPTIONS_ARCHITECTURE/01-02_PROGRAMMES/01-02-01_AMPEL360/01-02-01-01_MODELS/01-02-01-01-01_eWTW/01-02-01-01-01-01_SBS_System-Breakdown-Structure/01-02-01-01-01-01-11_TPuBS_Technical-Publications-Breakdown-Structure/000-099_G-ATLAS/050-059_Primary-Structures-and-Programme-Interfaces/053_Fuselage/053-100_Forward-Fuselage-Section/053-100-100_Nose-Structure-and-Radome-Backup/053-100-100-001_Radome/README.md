# 053-100-100-001 — Radome — TPuBS Part Node

> **TPuBS publication entry (part level)** for the eWTW Radome.
> **Maps from PBS:** `eWTW-PBS-10-10-10-10-10_Radome`
> **G-ATLAS SNS:** `050-059_Primary-Structures-and-Programme-Interfaces` → `053_Fuselage` → `053-100` → `053-100-100` → **`053-100-100-001`** ⇄ **ATA 53-10-10-01**
> **Programme:** AMPEL360 / eWTW · **Standard:** S1000D Issue 4.2

This part node holds the S1000D objects published for the Radome. Its `pub/`
folder was relocated here from the PBS leaf under the **SSOT+PUB separation**
doctrine: *engineering revision ≠ publication revision*. Engineering LC/REV
states are **referenced** in `PUB-BASELINES/`, never nested in `DM/`.

| Folder | Contents |
|---|---|
| `SSOT/` | Traceability manifest → G-ATLAS node + PBS Radome leaf |
| `APPLIC/` | Part-level applicability (ACT / CCT / PCT) |
| `IMPACT/` | Impact-analysis records (engineering change → publication impact?) |
| `DM/` | Data Modules — **flat** info-code folders (`040`, `258`, `310`, `520`, `720`, `941`) |
| `ICN/` | Illustrations & multimedia (flat pool, by ICN id) |
| `PM/` | Publication Modules (part assembly) |
| `PUB-BASELINES/` | Publication baseline / issue records (YAML); links engineering baselines |

## Numbering grammar

| Level | Code | Rule | ATA / SNS |
|---|---|---|---|
| Node / code section | `053-100` | ×10 from ATA | 53-10 |
| Sub-assembly | `053-100-100` | ×10 continues | 53-10-10 |
| Part | `053-100-100-001` | sequential `NNN` | 53-10-10-01 |

## Data-module set

| Info code | DM type | Canonical short DMC | Full S1000D DMC |
|---|---|---|---|
| `040` | descript | `DMC-EWTW-053-100-100-001-040` | `DMC-EWTW-A-53-10-10-01A-040A-D-EN-US_001-00.xml` |
| `258` | proced | `DMC-EWTW-053-100-100-001-258` | `DMC-EWTW-A-53-10-10-01A-258A-D-EN-US_001-00.xml` |
| `310` | proced | `DMC-EWTW-053-100-100-001-310` | `DMC-EWTW-A-53-10-10-01A-310A-D-EN-US_001-00.xml` |
| `520` | proced | `DMC-EWTW-053-100-100-001-520` | `DMC-EWTW-A-53-10-10-01A-520A-D-EN-US_001-00.xml` |
| `720` | proced | `DMC-EWTW-053-100-100-001-720` | `DMC-EWTW-A-53-10-10-01A-720A-D-EN-US_001-00.xml` |
| `941` | ipd | `DMC-EWTW-053-100-100-001-941` | `DMC-EWTW-A-53-10-10-01A-941A-D-EN-US_001-00.xml` |

```yaml
Last.MarkedDown:
  level: part
  node: 053-100-100-001
  title: Radome
  from_pbs: eWTW-PBS-10-10-10-10-10_Radome
  ata_ref: 53-10-10-01
  model_ident_code: EWTW
  publication_baseline: PUB-BL-0001
  doctrine: SSOT+PUB separation (LC/REV referenced, not nested)
  status: baseline
```
