# 053-100-100-001 — Radome — SSOT Manifest (part-level TPuBS → standard binding)

> **Role:** binds this TPuBS **part** node to (a) the eWTW **PBS-side** Radome leaf
> (engineering truth) and (b) the **G-ATLAS standard** node it instantiates.
> Direction is one-way: **standard (SSOT) → publication (PUB)**. A value present
> in a published object but absent from the source is a publication defect.

```yaml
ssot_manifest:
  level: part
  atlas_part_code: 053-100-100-001
  title: Radome
  side: PUB
  standard: S1000D-Issue-4.2
  model_ident_code: EWTW
  ata_ref: 53-10-10-01

  # (a) Engineering truth — eWTW PBS Radome leaf
  pbs_ssot_source:
    pbs_leaf: eWTW-PBS-10-10-10-10-10_Radome
    path: "../../../../../../../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-10_Airframe-Structure/eWTW-PBS-10-10_Fuselage-Wide-Tube/eWTW-PBS-10-10-10_Forward-Fuselage-Section/eWTW-PBS-10-10-10-10_Nose-Structure-and-Radome-Backup/eWTW-PBS-10-10-10-10-10_Radome/"
    authority_rule: SSOT-AUTHORITY-001

  # (b) Standard node — Q+ATLANTIDE G-ATLAS Standard Numbering System
  gatlas_standard_node:
    master_range: 050-059_Primary-Structures-and-Programme-Interfaces
    chapter: 053_Fuselage
    node_section: 053-100
    registry: "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_G-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces"

  # Numbering grammar: node = ×10 from ATA; sub-assembly = ×10 continues; part = sequential NNN
  numbering:
    node_section: "053-100  ⇄ ATA 53-10"
    sub_assembly: "053-100-100  ⇄ SNS 53-10-10"
    part: "053-100-100-001  (sequential)"

  # DM → SSOT realisation
  realises:
    - dm: DMC-EWTW-053-100-100-001-040
      from: "G-ATLAS 050-059_Primary-Structures-and-Programme-Interfaces/053-100 (descriptive)"
    - dm: DMC-EWTW-053-100-100-001-520
      from: "G-ATLAS 050-059_Primary-Structures-and-Programme-Interfaces/053-100 (procedural)"
    - object: part-identity
      from: "PBS eWTW-PBS-10-10-10-10-10_Radome"

  object_classes: [SSOT, APPLIC, IMPACT, DM, ICN, PM, PUB-BASELINES]
  publication_baseline: PUB-BL-0001
  status: baseline
```
