---
document_id: AMPEL360-eWTW-PBS-10-10-10-10-10-REQUIREMENTS-REV-A0
title: "eWTW · PBS-10-10-10-10-10 — Radome Requirements Snapshot (REV-A0)"
register: Q-plus
architecture: OPTIONS_ARCHITECTURE
options_axis: P-Programmes
programme: AMPEL360
product: eWTW

pbs_id: eWTW-PBS-10-10-10-10-10
pbs_title: "Radome"
parent_pbs_id: eWTW-PBS-10-10-10-10
parent_title: "Nose Structure and Radome Backup"

pnr_id: PNR-eWTW-PBS-10-10-10-10-10
part_number: PN-eWTW-5310-0001

lifecycle_model: "LC-letter CAD/product maturity model"
lifecycle_stage: LC-A
lifecycle_stage_name: "Conceptual Design"
revision: RADOME-REV-A0
revision_status: superseded
superseded_by: "01_REQUIREMENTS/REV-A1/ReqBS-RADOME-REV-A1.md"

governance_class: historical-requirements-snapshot
version: "0.1.0"
status: superseded
language: en
---

# eWTW · PBS-10-10-10-10-10 — Radome Requirements Snapshot (REV-A0)

![LC-A](https://img.shields.io/badge/maturity-LC--A%20Conceptual-5585b0)
![REV-A0](https://img.shields.io/badge/revision-REV--A0-888888)
![superseded](https://img.shields.io/badge/status-superseded-b02020)

## 1. Purpose

This document records the initial requirements snapshot associated with:

```text
RADOME-REV-A0
````

for:

```text
eWTW-PBS-10-10-10-10-10 — Radome
```

This file is retained as historical evidence of the first conceptual requirements state used during the creation of the initial FreeCAD radome body.

It is **not** the current authoritative requirements baseline.

The current authoritative revisioned requirements baseline is:

```text
01_REQUIREMENTS/REV-A1/ReqBS-RADOME-REV-A1.md
```

---

## 2. Authority Status

`Requirements_REV-A0.md` is a historical lifecycle-local requirements note.

It is superseded by the revisioned Requirements Breakdown Structure:

```text
ReqBS-RADOME-REV-A1
```

Controlled rule:

```yaml
requirements_authority:
  historical_file: "LC-A_Concept-Design/REV-A0/Requirements/Requirements_REV-A0.md"
  current_authoritative_reqbs: "01_REQUIREMENTS/REV-A1/ReqBS-RADOME-REV-A1.md"
  authority_status: "superseded"
  reason: >
    Requirements are no longer controlled as static LC-folder content.
    They are controlled as revisioned artefacts linked to the PBS item,
    product configuration, and lifecycle maturity state.
```

---

## 3. REV-A0 Configuration Context

| Field             | Value                               |
| ----------------- | ----------------------------------- |
| PBS item          | `eWTW-PBS-10-10-10-10-10`           |
| Item name         | Radome                              |
| Part number       | `PN-eWTW-5310-0001`                 |
| Lifecycle stage   | `LC-A — Conceptual Design`          |
| Revision          | `RADOME-REV-A0`                     |
| CAD status        | Initial conceptual placeholder      |
| Geometry basis    | Axisymmetric conceptual radome body |
| Current authority | Superseded by `ReqBS-RADOME-REV-A1` |

---

## 4. Initial REV-A0 Requirements Snapshot

### REQ-A0-001 — Aerodynamic fairing

The radome shall provide a conceptual aerodynamic forward fairing for the AMPEL360 eWTW nose structure.

| Attribute         | Value                              |
| ----------------- | ---------------------------------- |
| Requirement class | Functional                         |
| ReqBS mapping     | `ReqBS-10 Functional Requirements` |
| Status            | superseded                         |
| Superseded by     | `REQ-RADOME-A1-001`                |

---

### REQ-A0-002 — Weather-radar transparency placeholder

The radome shall be treated as a radio-frequency-transparent enclosure for candidate weather-radar or forward sensing equipment.

| Attribute         | Value                                |
| ----------------- | ------------------------------------ |
| Requirement class | Functional / Performance placeholder |
| ReqBS mapping     | `ReqBS-10`, `ReqBS-11`               |
| Status            | superseded                           |
| Superseded by     | `ReqBS-RADOME-REV-A1`                |

---

### REQ-A0-003 — Radome boundary

The radome boundary shall include the external radome shell and its conceptual attachment boundary to the nose structure and radome backup.

| Attribute         | Value                        |
| ----------------- | ---------------------------- |
| Requirement class | System Boundary              |
| ReqBS mapping     | `ReqBS-06 System Boundaries` |
| Status            | superseded                   |
| Superseded by     | `ReqBS-RADOME-REV-A1`        |

---

### REQ-A0-004 — Conceptual CAD geometry

The radome shall be represented by a preliminary FreeCAD conceptual body during `LC-A / REV-A0`.

| Attribute         | Value                               |
| ----------------- | ----------------------------------- |
| Requirement class | Physical Characteristics            |
| ReqBS mapping     | `ReqBS-14 Physical Characteristics` |
| Status            | superseded                          |
| Superseded by     | `RADOME-REV-A1` CAD record          |

---

### REQ-A0-005 — Lightning and bonding placeholder

The radome shall include conceptual consideration of lightning attachment and bonding provisions at the radome interface.

| Attribute         | Value                                                            |
| ----------------- | ---------------------------------------------------------------- |
| Requirement class | External Constraints / Interfaces                                |
| ReqBS mapping     | `ReqBS-03`, `ReqBS-07`                                           |
| Status            | superseded                                                       |
| Superseded by     | `pub/258_bonding-and-lightning-check/` and `ReqBS-RADOME-REV-A1` |

---

### REQ-A0-006 — Maintainability placeholder

The radome shall support future removal, inspection, and maintenance access definition.

| Attribute         | Value                                 |
| ----------------- | ------------------------------------- |
| Requirement class | Human Systems Integration / Lifecycle |
| ReqBS mapping     | `ReqBS-09`, `ReqBS-15`                |
| Status            | superseded                            |
| Superseded by     | `ReqBS-RADOME-REV-A1`                 |

---

## 5. Known REV-A0 Requirement Gaps

| Finding     | Description                                                                                                       | Status                                                                    |
| ----------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `REQ-A0-F1` | Requirements were stored inside the LC folder instead of a revisioned `ReqBS` structure.                          | closed by REV-A1 structure                                                |
| `REQ-A0-F2` | Requirement classes were not fully mapped to the controlled `ReqBS-01..15` class set.                             | closed by `ReqBS-RADOME-REV-A1`                                           |
| `REQ-A0-F3` | Interfaces, cost, risk, evidence, and TPM implications were not connected to revision-specific breakdown records. | open / to be closed by `IBS`, `CBS`, `RBS`, `EBS`, `TPMS` REV-A1 packages |
| `REQ-A0-F4` | Upgradeability and future technology insertion logic were not yet represented.                                    | closed by lifecycle model v0.2.0 / A1 and future upgrade register         |

---

## 6. Migration Rule

The authoritative requirements model has moved from:

```text
LC-A_Concept-Design/REV-A0/Requirements/
```

to:

```text
01_REQUIREMENTS/REV-A1/
```

Controlled rule:

```yaml
requirements_migration_rule:
  id: RADOME-REQ-MIGRATION-A0-A1
  from: "LC-A_Concept-Design/REV-A0/Requirements/Requirements_REV-A0.md"
  to: "01_REQUIREMENTS/REV-A1/ReqBS-RADOME-REV-A1.md"
  rule: >
    REV-A0 requirements are retained as historical evidence only.
    REV-A1 requirements are controlled through the revisioned ReqBS package.
    Future requirement changes shall update the applicable REV-X ReqBS and
    trigger impact assessment across IBS, CBS, RBS, EBS, BOM, CAD, TPMS, and PUB.
```

---

## 7. Relationship to Lifecycle Model

This document is governed by:

```text
02_LIFECYCLE_MODEL/README.md
```

Version `0.2.0 / A1` of the lifecycle model clarifies:

```text
LC folders control lifecycle maturity.
PBS REV-X packages control configuration-specific engineering truth.
ReqBS / IBS / CBS / RBS / EBS / TPMS records are revision-specific.
```

Therefore, this `REV-A0` requirements file remains useful as a historical record, but it does not remain the source of truth for active radome requirements.

---

## 8. Traceability

| Direction            | Artefact                                        |
| -------------------- | ----------------------------------------------- |
| Parent PBS           | `eWTW-PBS-10-10-10-10-10`                       |
| Previous CAD state   | `cad/freecad/LC-A_Concept-Design/REV-A0/`       |
| Current CAD state    | `cad/freecad/LC-A_Concept-Design/REV-A1/`       |
| Current ReqBS        | `01_REQUIREMENTS/REV-A1/ReqBS-RADOME-REV-A1.md` |
| Publication 040      | `pub/040_descriptive/`                          |
| Publication 258      | `pub/258_bonding-and-lightning-check/`          |
| Root lifecycle model | `02_LIFECYCLE_MODEL/README.md`                  |

---

## 9. Controlled Closure Statement

`Requirements_REV-A0.md` records the first conceptual requirements snapshot for the AMPEL360 eWTW radome.

It is retained for historical traceability only.

The active requirements authority is now:

```text
01_REQUIREMENTS/REV-A1/ReqBS-RADOME-REV-A1.md
```

No future requirements shall be authored as static LC-folder content unless they are explicitly marked as historical notes, migration records, or non-authoritative working material.

```
```
