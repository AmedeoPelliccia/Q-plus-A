---
document_id: "PM-EWTW-10-10-10-000"
title: "AMPEL360 eWTW — Forward Fuselage Publication Index"
programme: "AMPEL360"
product: "eWTW"
product_name: "AMPEL360 Electric Wide Tube-and-Wing"
aircraft_class: "100-passenger regional aircraft"
configuration: "Electric Wide Tube-and-Wing"

breakdown_context: "PBS-linked"
pbs_item: "eWTW-PBS-10-10-10_Forward-Fuselage-Section"
pbs_parent: "eWTW-PBS-10-10_Fuselage-Wide-Tube"
domain: "Airframe Structure"

publication_layer: "PUB/PM"
publication_object_type: "Publication Module"
pm_id: "PM-EWTW-10-10-10-000"
pm_type: "Publication Index"

related_breakdowns:
  pbs: "eWTW-PBS-10-10-10_Forward-Fuselage-Section"
  fbs: "TBD"
  ibs: "TBD"
  ebs: "TBD"

effectivity:
  product: "eWTW"
  configuration: "baseline"
  msn_range: "MSN-001..050"
  status: "active"

s1000d_status: "provisional_mapping"
csdb_ready: false
configuration_locked: false

status: "DRAFT"
version: "0.1.0"
classification: "open-technical-publication"
lifecycle_phase: "LC01 Concept Definition"
owner: "AEROSPACEMODEL / AMPEL360"
---

# AMPEL360 eWTW — Forward Fuselage Publication Index

## 1. Purpose

This document is the **Publication Index** for the **Forward Fuselage Section** of the **AMPEL360 eWTW** product breakdown structure.

It identifies the controlled publication modules planned for the forward fuselage section and defines their publication role, scope, traceability logic, maturity status, effectivity, and provisional S1000D / CSDB publication mapping.

This index does not contain the complete technical content of each publication module.

It acts as the controlled navigation and configuration entry point for the `PUB/PM` layer.

---

## 2. Controlled File Identification

| Field | Value |
|---|---|
| File name | `PM-EWTW-10-10-10-000_Forward-Fuselage-Publication-Index.md` |
| PM ID | `PM-EWTW-10-10-10-000` |
| PM title | `Forward Fuselage Publication Index` |
| Publication layer | `PUB/PM` |
| Publication object type | `Publication Module` |
| PM type | `Publication Index` |
| Breakdown context | `PBS-linked` |
| PBS item | `eWTW-PBS-10-10-10_Forward-Fuselage-Section` |
| Parent PBS item | `eWTW-PBS-10-10_Fuselage-Wide-Tube` |
| Aircraft product | `AMPEL360 eWTW` |
| Configuration | `Electric Wide Tube-and-Wing` |
| Aircraft class | `100-passenger regional aircraft` |
| Effectivity | `eWTW baseline, MSN-001..050` |
| S1000D status | `provisional_mapping` |
| CSDB ready | `false` |

---

## 3. Folder Position

```text
01_OPTIONS_ARCHITECTURE/
└── 01-02_PROGRAMMES/
    └── 01-02-01_AMPEL360/
        └── 01-02-01-01_MODELS/
            └── 01-02-01-01-01_eWTW/
                └── 01-02-01-01-01-01_SBS_System-Breakdown-Structure/
                    └── 01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/
                        └── eWTW-PBS-00_Aircraft-Product/
                            └── eWTW-PBS-10_Airframe-Structure/
                                └── eWTW-PBS-10-10_Fuselage-Wide-Tube/
                                    └── eWTW-PBS-10-10-10_Forward-Fuselage-Section/
                                        └── PUB/
                                            └── PM/
                                                └── PM-EWTW-10-10-10-000_Forward-Fuselage-Publication-Index.md
````

---

## 4. Publication Index Scope

This index covers publication modules related to the forward fuselage section, including:

* structural description;
* maintenance publication;
* inspection publication;
* repair publication;
* access and panel publication;
* non-destructive testing publication;
* illustrated parts publication;
* safety and limitations publication;
* traceability and evidence publication.

The publication index shall be updated when a new forward fuselage publication module is created, revised, superseded, withdrawn, or transferred to a controlled S1000D / CSDB object.

---

## 5. Controlled Publication Module List

| PM ID                  | File                                                                             | Title                                                  | Status  |
| ---------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------ | ------- |
| `PM-EWTW-10-10-10-000` | `PM-EWTW-10-10-10-000_Forward-Fuselage-Publication-Index.md`                     | Forward Fuselage Publication Index                     | DRAFT   |
| `PM-EWTW-10-10-10-010` | `PM-EWTW-10-10-10-010_Forward-Fuselage-Description-Publication.md`               | Forward Fuselage Description Publication               | PLANNED |
| `PM-EWTW-10-10-10-020` | `PM-EWTW-10-10-10-020_Forward-Fuselage-Maintenance-Publication.md`               | Forward Fuselage Maintenance Publication               | PLANNED |
| `PM-EWTW-10-10-10-030` | `PM-EWTW-10-10-10-030_Forward-Fuselage-Inspection-Publication.md`                | Forward Fuselage Inspection Publication                | PLANNED |
| `PM-EWTW-10-10-10-040` | `PM-EWTW-10-10-10-040_Forward-Fuselage-Repair-Publication.md`                    | Forward Fuselage Repair Publication                    | PLANNED |
| `PM-EWTW-10-10-10-050` | `PM-EWTW-10-10-10-050_Forward-Fuselage-Access-and-Panels-Publication.md`         | Forward Fuselage Access and Panels Publication         | PLANNED |
| `PM-EWTW-10-10-10-060` | `PM-EWTW-10-10-10-060_Forward-Fuselage-NDT-Publication.md`                       | Forward Fuselage NDT Publication                       | PLANNED |
| `PM-EWTW-10-10-10-070` | `PM-EWTW-10-10-10-070_Forward-Fuselage-Illustrated-Parts-Publication.md`         | Forward Fuselage Illustrated Parts Publication         | PLANNED |
| `PM-EWTW-10-10-10-080` | `PM-EWTW-10-10-10-080_Forward-Fuselage-Safety-and-Limitations-Publication.md`    | Forward Fuselage Safety and Limitations Publication    | PLANNED |
| `PM-EWTW-10-10-10-090` | `PM-EWTW-10-10-10-090_Forward-Fuselage-Traceability-and-Evidence-Publication.md` | Forward Fuselage Traceability and Evidence Publication | PLANNED |

---

## 6. Publication Module Scope Definitions

### 6.1 `PM-EWTW-10-10-10-010` — Description Publication

Defines the descriptive publication package for the forward fuselage section.

Expected content references:

* structural overview;
* section boundaries;
* nose structure;
* flight deck structure;
* forward pressure shell;
* radome interface;
* avionics bay structural provisions;
* nose landing gear bay interface;
* systems routing zones.

---

### 6.2 `PM-EWTW-10-10-10-020` — Maintenance Publication

Defines the maintenance publication package for the forward fuselage section.

Expected content references:

* scheduled maintenance tasks;
* access requirements;
* zone preparation;
* structural checks;
* fastener and fitting checks;
* sealing and protection tasks;
* maintenance precautions;
* return-to-service conditions.

---

### 6.3 `PM-EWTW-10-10-10-030` — Inspection Publication

Defines the inspection publication package for the forward fuselage section.

Expected content references:

* general visual inspection;
* detailed inspection;
* special detailed inspection;
* corrosion inspection;
* damage inspection;
* lightning strike inspection;
* impact damage inspection;
* fatigue-sensitive area inspection.

---

### 6.4 `PM-EWTW-10-10-10-040` — Repair Publication

Defines the repair publication package for the forward fuselage section.

Expected content references:

* allowable damage limits;
* repair category references;
* structural repair classification;
* temporary repair references;
* permanent repair references;
* bonded repair references;
* fastened repair references;
* engineering disposition references.

---

### 6.5 `PM-EWTW-10-10-10-050` — Access and Panels Publication

Defines the access and panels publication package for the forward fuselage section.

Expected content references:

* access panels;
* service panels;
* avionics bay access;
* crew access interface;
* inspection openings;
* panel removal and installation references;
* access precautions;
* panel identification logic.

---

### 6.6 `PM-EWTW-10-10-10-060` — NDT Publication

Defines the non-destructive testing publication package for the forward fuselage section.

Expected content references:

* ultrasonic inspection;
* tap test inspection;
* thermographic inspection;
* eddy-current inspection;
* visual enhanced inspection;
* composite bond inspection;
* metallic fitting inspection;
* acceptance criteria references.

---

### 6.7 `PM-EWTW-10-10-10-070` — Illustrated Parts Publication

Defines the illustrated parts publication package for the forward fuselage section.

Expected content references:

* structural panels;
* frames;
* stringers;
* brackets;
* fittings;
* access panels;
* seals;
* fasteners;
* replaceable structural items;
* local installation items.

---

### 6.8 `PM-EWTW-10-10-10-080` — Safety and Limitations Publication

Defines the safety and limitations publication package for the forward fuselage section.

Expected content references:

* structural limitations;
* access limitations;
* maintenance safety notes;
* warning and caution references;
* pressurization-related limitations;
* electrical bonding precautions;
* composite handling precautions;
* lifting and support limitations.

---

### 6.9 `PM-EWTW-10-10-10-090` — Traceability and Evidence Publication

Defines the traceability and evidence publication package for the forward fuselage section.

Expected content references:

* requirement links;
* PBS links;
* FBS links;
* IBS links;
* EBS links;
* verification records;
* compliance references;
* configuration-control records;
* publication approval records.

---

## 7. Forward Fuselage Publication Boundary

The forward fuselage publication set applies to the aircraft structure located in the forward fuselage section of the eWTW product.

The publication boundary includes candidate coverage for:

| Area                                       | Included |
| ------------------------------------------ | -------- |
| Nose structural shell                      | Yes      |
| Flight deck structural support             | Yes      |
| Forward pressure shell                     | Yes      |
| Radome structural interface                | Yes      |
| Avionics bay structural provisions         | Yes      |
| Nose landing gear bay interface            | Yes      |
| Forward passenger / crew access interfaces | Yes      |
| Local systems-routing structural supports  | Yes      |
| Forward fuselage access panels             | Yes      |
| Forward fuselage inspection zones          | Yes      |

The publication boundary excludes, unless specifically cross-referenced:

| Area                                         | Exclusion Logic                                  |
| -------------------------------------------- | ------------------------------------------------ |
| Complete avionics system design              | Owned by avionics system publication layer       |
| Complete nose landing gear design            | Owned by landing gear system publication layer   |
| Complete environmental-control system design | Owned by ECS publication layer                   |
| Complete electrical-power system design      | Owned by electrical-power publication layer      |
| Complete cabin interior design               | Owned by cabin and furnishings publication layer |

---

## 8. Related Breakdown Traceability

The publication index is linked to the physical PBS item and shall later be connected to FBS, IBS, and EBS objects.

| Breakdown | Current Link                                 | Status  |
| --------- | -------------------------------------------- | ------- |
| PBS       | `eWTW-PBS-10-10-10_Forward-Fuselage-Section` | Defined |
| FBS       | `TBD`                                        | Pending |
| IBS       | `TBD`                                        | Pending |
| EBS       | `TBD`                                        | Pending |

The related breakdowns are also declared in machine-readable YAML frontmatter.

---

## 9. Effectivity

The current publication index applies to the following provisional effectivity baseline:

| Field         | Value          |
| ------------- | -------------- |
| Product       | `eWTW`         |
| Configuration | `baseline`     |
| MSN range     | `MSN-001..050` |
| Status        | `active`       |

This effectivity is provisional and shall be revised when aircraft configuration, serial-number applicability, modification standards, or publication applicability rules are baselined.

---

## 10. Traceability Model

Each publication module shall preserve traceability to the relevant architecture layers.

```text
PBS Item
→ Function / Requirement
→ Interface
→ Maintenance or Inspection Need
→ Evidence Record
→ Data Module
→ Publication Module
→ IETP / CSDB Output
```

The forward fuselage publication index shall remain aligned with:

| Layer         | Required Link                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| PBS           | `eWTW-PBS-10-10-10_Forward-Fuselage-Section`                                                                             |
| FBS           | Forward fuselage structural, access, safety, inspection, and support functions                                           |
| IBS           | Interfaces with cockpit, avionics bay, radome, nose landing gear bay, ECS routing, wiring routing, and pressure boundary |
| EBS           | Verification, inspection, compliance, and publication evidence                                                           |
| S1000D / CSDB | Future DMC and publication-module mapping                                                                                |

---

## 11. Provisional S1000D / CSDB Mapping

The following S1000D / CSDB mapping is provisional and shall not be treated as a controlled DMC baseline until the product PBS, FBS, IBS, and EBS records are mature.

| Publication Area       | Candidate S1000D Object Type            | Status      |
| ---------------------- | --------------------------------------- | ----------- |
| Description            | Descriptive data module                 | Provisional |
| Maintenance procedure  | Procedural data module                  | Provisional |
| Inspection procedure   | Procedural data module                  | Provisional |
| NDT inspection         | Procedural / process data module        | Provisional |
| Illustrated parts      | Illustrated parts data / IPD object     | Provisional |
| Safety and limitations | Descriptive / procedural safety content | Provisional |
| Traceability           | Project-controlled evidence record      | Provisional |

Current machine-readable status:

```yaml
s1000d_status: "provisional_mapping"
csdb_ready: false
configuration_locked: false
```

---

## 12. Configuration Control

All publication modules listed in this index shall be configuration-managed.

Minimum configuration fields:

| Field                     | Requirement                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------- |
| `pm_id`                   | Shall be unique inside the forward fuselage PM set                                      |
| `title`                   | Shall match the controlled publication title                                            |
| `status`                  | Shall use controlled status values                                                      |
| `version`                 | Shall follow semantic versioning where applicable                                       |
| `breakdown_context`       | Shall indicate the architecture context, e.g. `PBS-linked`                              |
| `pbs_item`                | Shall reference `eWTW-PBS-10-10-10_Forward-Fuselage-Section`                            |
| `publication_layer`       | Shall be `PUB/PM`                                                                       |
| `publication_object_type` | Shall be `Publication Module`                                                           |
| `related_breakdowns`      | Shall identify linked PBS, FBS, IBS, and EBS records where available                    |
| `effectivity`             | Shall identify product, configuration, MSN range, and effectivity status                |
| `s1000d_status`           | Shall identify whether the S1000D mapping is provisional, controlled, or not applicable |
| `csdb_ready`              | Shall indicate whether the object is ready for CSDB integration                         |
| `lifecycle_phase`         | Shall identify the active lifecycle phase                                               |

---

## 13. Controlled Status Values

| Status       | Meaning                                                              |
| ------------ | -------------------------------------------------------------------- |
| `PLANNED`    | Publication module has been identified but not drafted.              |
| `DRAFT`      | Publication module exists but is not yet controlled.                 |
| `REVIEW`     | Publication module is under technical or editorial review.           |
| `CONTROLLED` | Publication module is accepted as a controlled baseline.             |
| `SUPERSEDED` | Publication module has been replaced by a later object.              |
| `WITHDRAWN`  | Publication module has been removed from the active publication set. |

---

## 14. Governance Rules

1. This index shall remain the master PM list for the forward fuselage publication layer.
2. New PM files shall not be added without updating this index.
3. PM files shall not duplicate authoritative engineering data.
4. PM files shall reference controlled PBS, FBS, IBS, EBS, and data-module records.
5. Safety-critical publication content shall require evidence linkage before controlled release.
6. Repair, inspection, and NDT publication content shall remain provisional until approved by the relevant structural authority.
7. S1000D / CSDB mapping shall remain provisional until DMC rules are formally defined.
8. Any superseded PM shall remain listed with its replacement reference.
9. Any withdrawn PM shall remain listed with withdrawal rationale.
10. This publication index shall be reviewed whenever the forward fuselage PBS item changes.
11. Effectivity shall be reviewed whenever product configuration, MSN range, or modification standard changes.
12. `breakdown_context` shall be used instead of `breakdown_type` for publication-layer objects located inside engineering breakdown structures.

---

## 15. Maturity Status

```yaml
status: "DRAFT"
maturity: "LC01 Concept Definition"
pm_index_defined: true
pm_files_created: false
pbs_link_defined: true
fbs_link_defined: false
ibs_link_defined: false
ebs_link_defined: false
effectivity_defined: true
s1000d_status: "provisional_mapping"
s1000d_mapping_defined: false
csdb_ready: false
configuration_locked: false
```

---

## 16. Revision History

| Version |       Date | Change                                                                                                                                                    | Author                    |
| ------- | ---------: | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| `0.1.0` | 2026-05-30 | Initial draft publication index for the AMPEL360 eWTW forward fuselage section.                                                                           | AEROSPACEMODEL / AMPEL360 |
| `0.1.1` | 2026-05-30 | Replaced `breakdown_type` with `breakdown_context`; added `effectivity`, `related_breakdowns`, `s1000d_status`, `csdb_ready`, and `configuration_locked`. | AEROSPACEMODEL / AMPEL360 |

---

## 17. Short Definition

`PM-EWTW-10-10-10-000_Forward-Fuselage-Publication-Index.md` is the controlled publication index for the **AMPEL360 eWTW Forward Fuselage Section**, listing and governing the planned publication modules for description, maintenance, inspection, repair, access, NDT, illustrated parts, safety, limitations, traceability, and evidence.

It is a **PBS-linked publication-layer object**, not a physical product breakdown object.

```text
PBS = physical product
PUB/PM = publication index and package
DM/DMC = S1000D data modules as they mature
EBS/IEF = evidence
```

```
```
