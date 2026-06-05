# 000-000 — SSOT Manifest (TPuBS → standard binding)

> **Role:** binds this TPuBS node section back to the eWTW **PBS-side SSOT**
> (engineering truth) and the **G-ATLAS standard** node it instantiates.
> Content flows **SSOT → PUB, never the reverse.**

```yaml
ssot_manifest:
  node: 000-000
  title: General / Introduction
  side: PUB
  standard: S1000D-Issue-4.2
  model_ident_code: EWTW
  ata_ref: 00-00
  impact: "Identification, general"
  pbs_ssot_source:
    pbs_item: eWTW-PBS-10-10-10_Forward-Fuselage-Section
    path: "../../../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-10_Airframe-Structure/eWTW-PBS-10-10_Fuselage-Wide-Tube/eWTW-PBS-10-10-10_Forward-Fuselage-Section/SSOT/README.md"
    authority_rule: SSOT-AUTHORITY-001
  gatlas_standard_node:
    master_range: 000-009_General-Information-and-Service
    chapter: 000_General
    node_section: 000-000
    registry: "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_G-ATLAS/000-009_General-Information-and-Service/000_General/000-000_General-Introduction"
  object_classes: [APPLIC, BREX, DM, DMRL, ICN, PM, SSOT]
  status: pattern
```
