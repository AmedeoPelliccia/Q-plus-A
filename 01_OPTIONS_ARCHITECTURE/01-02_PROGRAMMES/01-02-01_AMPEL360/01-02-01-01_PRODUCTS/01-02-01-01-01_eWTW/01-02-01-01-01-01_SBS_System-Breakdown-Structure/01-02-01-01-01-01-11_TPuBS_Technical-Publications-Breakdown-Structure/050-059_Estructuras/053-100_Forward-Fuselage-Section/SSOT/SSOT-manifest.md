# 053-100 — SSOT Manifest (TPuBS → standard binding)

> **Role:** binds this TPuBS node section back to (a) the eWTW **PBS-side SSOT**
> (engineering truth) and (b) the **G-ATLAS standard** node it instantiates.
> Content flows **SSOT → PUB, never the reverse.** A value present in a TPuBS
> object but absent from the SSOT source is a publication defect.

```yaml
ssot_manifest:
  node: 053-100
  title: Forward Fuselage Section
  side: PUB
  standard: S1000D-Issue-4.2
  model_ident_code: EWTW
  ata_ref: 53-10

  # (a) Engineering truth — eWTW PBS-side SSOT element document
  pbs_ssot_source:
    pbs_item: eWTW-PBS-10-10-10_Forward-Fuselage-Section
    path: "../../../../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-10_Airframe-Structure/eWTW-PBS-10-10_Fuselage-Wide-Tube/eWTW-PBS-10-10-10_Forward-Fuselage-Section/SSOT/README.md"
    authority_rule: SSOT-AUTHORITY-001

  # (b) Standard node — Q+ATLANTIDE G-ATLAS Standard Numbering System
  gatlas_standard_node:
    master_range: 050-059_Estructuras
    chapter: 053_Fuselage
    node_section: 053-100
    registry: "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_G-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces"

  object_classes: [APPLIC, BREX, DM, DMRL, ICN, PM, SSOT]
  status: baseline
```
