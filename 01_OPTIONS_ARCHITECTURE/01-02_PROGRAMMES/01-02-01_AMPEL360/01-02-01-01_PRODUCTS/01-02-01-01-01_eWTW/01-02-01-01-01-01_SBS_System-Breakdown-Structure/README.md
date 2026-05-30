---
document_id: "OPT-ARCH-AMPEL360-EWTW-SBS-README"
title: "AMPEL360 eWTW — SBS System Breakdown Structure"
programme: "AMPEL360"
product: "eWTW"
product_name: "AMPEL360 Electric Wide Tube-and-Wing"
aircraft_class: "100-passenger regional aircraft"
configuration: "Electric Wide Tube-and-Wing"
architecture_layer: "01_OPTIONS_ARCHITECTURE"
parent_path: "01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_PRODUCTS/01-02-01-01-01_eWTW"
node_path: "01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_PRODUCTS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure"
status: "DRAFT"
version: "0.1.0"
classification: "open-technical-architecture"
lifecycle_phase: "LC01 Concept Definition"
owner: "AEROSPACEMODEL / AMPEL360"
---

# AMPEL360 eWTW — SBS System Breakdown Structure

## 1. Purpose

This folder defines the **System Breakdown Structure — SBS** for the **AMPEL360 eWTW**, an **Electric Wide Tube-and-Wing aircraft product option** in the approximately **100-passenger regional aircraft class**.

The SBS is the controlled decomposition layer used to organize the aircraft product into related breakdown views:

- product breakdown;
- functional breakdown;
- work breakdown;
- cost breakdown;
- risk breakdown;
- logistic breakdown;
- evidence breakdown;
- interface and installation breakdown.

This structure is intended to support deterministic architecture development, certification-oriented traceability, technical-publication readiness, and future S1000D / CSDB mapping.

---

## 2. Folder Position

```text
01_OPTIONS_ARCHITECTURE/
└── 01-02_PROGRAMMES/
    └── 01-02-01_AMPEL360/
        └── 01-02-01-01_PRODUCTS/
            └── 01-02-01-01-01_eWTW/
                └── 01-02-01-01-01-01_SBS_System-Breakdown-Structure/
````

---

## 3. Controlled Folder Structure

```text
01-02-01-01-01-01_SBS_System-Breakdown-Structure/
├── 01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/
├── 01-02-01-01-01-01-02_FBS_Functional-Breakdown-Structure/
├── 01-02-01-01-01-01-03_WBS_Work-Breakdown-Structure/
├── 01-02-01-01-01-01-04_CBS_Cost-Breakdown-Structure/
├── 01-02-01-01-01-01-05_RBS_Risk-Breakdown-Structure/
├── 01-02-01-01-01-01-06_LBS_Logistic-Breakdown-Structure/
├── 01-02-01-01-01-01-07_EBS_Evidence-Breakdown-Structure/
├── 01-02-01-01-01-01-08_IBS_Interface-and-Installation-Breakdown-Structure/
├── .gitkeep
└── README.md
```

---

## 4. Breakdown Structure Definitions

| Code                   | Folder                                               | Controlled Meaning                                                                                                                                    |
| ---------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `01-02-01-01-01-01-01` | `PBS_Product-Breakdown-Structure`                    | Physical product decomposition: aircraft, major assemblies, systems, subsystems, components, LRUs, SRUs, structural items, and installation items.    |
| `01-02-01-01-01-01-02` | `FBS_Functional-Breakdown-Structure`                 | Functional decomposition: what the aircraft must do, independent of the selected physical implementation.                                             |
| `01-02-01-01-01-01-03` | `WBS_Work-Breakdown-Structure`                       | Programme work decomposition: engineering, design, validation, certification, manufacturing, support, and publication work packages.                  |
| `01-02-01-01-01-01-04` | `CBS_Cost-Breakdown-Structure`                       | Cost decomposition: non-recurring cost, recurring cost, manufacturing cost, support cost, certification cost, and lifecycle cost.                     |
| `01-02-01-01-01-01-05` | `RBS_Risk-Breakdown-Structure`                       | Risk decomposition: technical, certification, industrial, operational, safety, supply-chain, cost, and schedule risks.                                |
| `01-02-01-01-01-01-06` | `LBS_Logistic-Breakdown-Structure`                   | Logistic decomposition: supportability, spares, maintainability, ground support equipment, training, documentation, and service operations.           |
| `01-02-01-01-01-01-07` | `EBS_Evidence-Breakdown-Structure`                   | Evidence decomposition: requirements evidence, design evidence, verification evidence, compliance evidence, test evidence, and publication evidence.  |
| `01-02-01-01-01-01-08` | `IBS_Interface-and-Installation-Breakdown-Structure` | Interface and installation decomposition: mechanical, electrical, digital, thermal, functional, physical, installation, and aircraft-zone interfaces. |

---

## 5. Architecture Role

The SBS is not a single aircraft system. It is the **controlled breakdown container** for the product-level architecture.

It provides the decomposition logic required to connect:

```text
Product Option
→ Aircraft Architecture
→ System Breakdown
→ Function Breakdown
→ Physical Product Items
→ Work Packages
→ Costs
→ Risks
→ Logistics
→ Evidence
→ Interfaces
→ S1000D / CSDB Data Modules
```

---

## 6. eWTW Product Context

The SBS applies to the following controlled product baseline:

| Field                  | Value                                               |
| ---------------------- | --------------------------------------------------- |
| Programme              | `AMPEL360`                                          |
| Product                | `eWTW`                                              |
| Product meaning        | `Electric Wide Tube-and-Wing`                       |
| Aircraft class         | `Approximately 100 passengers`                      |
| Aircraft configuration | `Tube-and-wing`                                     |
| Propulsion posture     | `Electric / hybrid-electric candidate architecture` |
| Documentation posture  | `S1000D / CSDB-ready`                               |
| Certification posture  | `Civil-certification-oriented`                      |
| Lifecycle phase        | `LC01 Concept Definition`                           |

---

## 7. Traceability Logic

Each breakdown structure shall preserve traceability to the others.

| Source View | Traceability Target                                                  |
| ----------- | -------------------------------------------------------------------- |
| PBS         | Physical items, assemblies, systems, LRUs, SRUs                      |
| FBS         | Aircraft-level and system-level functions                            |
| WBS         | Engineering and programme work packages                              |
| CBS         | Cost objects and lifecycle cost drivers                              |
| RBS         | Risks, mitigations, owners, and closure evidence                     |
| LBS         | Supportability and logistics requirements                            |
| EBS         | Verification, validation, compliance, and publication evidence       |
| IBS         | Interfaces, installation constraints, zones, and integration records |

The intended traceability chain is:

```text
Requirement
→ Function
→ Product Item
→ Interface
→ Work Package
→ Risk
→ Cost Object
→ Logistic Support Item
→ Evidence Record
→ S1000D Data Module
```

---

## 8. Governance Rules

1. The SBS shall remain product-specific to `AMPEL360 eWTW`.
2. Shared AMPEL360 programme definitions shall not be duplicated locally unless required for product effectivity.
3. PBS and FBS shall be developed before detailed WBS, CBS, RBS, LBS, EBS, and IBS closure.
4. Cost, risk, logistics, evidence, and interface breakdowns shall reference the PBS and FBS baselines.
5. Any item introduced in PBS shall have a corresponding function, interface, and evidence strategy unless explicitly marked as provisional.
6. Any function introduced in FBS shall be allocated to at least one physical or logical product element.
7. Any certification-relevant claim shall be linked to EBS.
8. Any installation-sensitive item shall be linked to IBS.
9. S1000D / CSDB mapping shall only be generated from controlled SBS/PBS/FBS baselines.

---

## 9. Initial Maturity Status

```yaml
status: DRAFT
maturity: LC01 Concept Definition
pbs_defined: false
fbs_defined: false
wbs_defined: false
cbs_defined: false
rbs_defined: false
lbs_defined: false
ebs_defined: false
ibs_defined: false
s1000d_mapping_ready: false
configuration_locked: false
```

---

## 10. Next Actions

1. Create `README.md` files inside each SBS child folder.
2. Define the first PBS physical product decomposition.
3. Define the first FBS aircraft-level functional decomposition.
4. Align PBS and FBS through a requirement-function-product traceability table.
5. Create the first WBS work-package baseline.
6. Derive preliminary cost, risk, logistic, evidence, and interface breakdowns.
7. Prepare the future S1000D / CSDB mapping layer.

---

## 11. Short Definition

The **AMPEL360 eWTW SBS** is the controlled product-level breakdown container for the **100-passenger Electric Wide Tube-and-Wing aircraft option**, organizing physical, functional, work, cost, risk, logistic, evidence, and interface structures into a traceable architecture baseline.

```
```
