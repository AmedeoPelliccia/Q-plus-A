# 102_Systems-Engineering-and-Requirements-Management

**Band:** 100-199_S-STA · **Range:** 100-109 · **Status:** Register-derived chapter — sections cite their anchoring standards from the S-STA standards register; merge constitutes ratification of this chapter section register under S-STA-BAND-RULING v0.4 §6. Source governance: sections cite standards-register anchors where they exist; the absence of a direct anchor does not invalidate a section when its architectural need is established by the ruling, boundary analysis or multiple source classes.

## Scope

Systems-engineering discipline and requirements management for the band: SE management and planning, requirements engineering, functional and technical specification classes, architecture definition and trade discipline, analysis-model and simulation management, technology assessment and maturity in SE, the verification-planning interface, model-based systems engineering, and SE products with review readiness. This chapter owns requirement classes, grammars and the SE discipline — actual requirements are downstream artifacts and are never instantiated in the taxonomy. Mission concepts are 101 (102 consumes what 101-200 defines); programme structure, configuration, documentation and reviews are 103; verification execution and qualification are 105; interface control is 106; system and vehicle classes are 190-199.

## Concept flow

```mermaid
flowchart LR
  X101["101-200<br/>Concept of operations"] --> RQ["102-200 Requirements<br/>engineering"] --> SP["102-300 Functional and<br/>technical specifications"] --> AR["102-400 System architecture<br/>and trade studies"]
  SE["102-100 SE management<br/>and planning"] --- RQ
  MD["102-500 Engineering-analysis<br/>models and simulation"] --- AR
  TR["102-600 Technology-readiness<br/>assessment and SE integration"] --- AR
  MB["102-800 MBSE and<br/>digital continuity"] --- SE
  MB --- AR
  RQ --> VP["102-700 Requirement verifiability,<br/>verification-planning interface"] --> EV["102-900 SE products,<br/>evidence, review readiness"]
  AR --> EV
  VP -. "programme, execution,<br/>qualification" .-> X105["105"]
  SE -. "programme, configuration,<br/>information, reviews" .-> X103["103"]
  MB -. "baselines and<br/>controlled records" .-> X103
  AR -. "interface-control<br/>implementation" .-> X106["106"]
  AR -. "class constraints" .-> X190["190-199"]
  TR -. "shared maturity and<br/>graduation doctrine" .-> X100["100-500"]
```

## Section register

| Section | Title | Anchors |
|---|---|---|
| 102-000 | [General Information](102-000_General-Information/) | — |
| 102-100 | [Systems Engineering Management and Planning](102-100_Systems-Engineering-Management-and-Planning/) | ISO 18676 |
| 102-200 | [Requirements Engineering and Management](102-200_Requirements-Engineering-and-Management/) | ISO 16404 |
| 102-300 | [Functional and Technical Specifications](102-300_Functional-and-Technical-Specifications/) | ISO 21351 |
| 102-400 | [System Architecture Definition and Trade Study Discipline](102-400_System-Architecture-Definition-and-Trade-Study-Discipline/) | Register-derived; trade-study sources pending |
| 102-500 | [Engineering Analysis Models and Simulation Management](102-500_Engineering-Analysis-Models-and-Simulation-Management/) | ISO 14954 — dynamic/static model exchange; ISO 16781 — control-system simulation; broader engineering-analysis governance register-derived |
| 102-600 | [Technology Readiness Assessment and SE Integration](102-600_Technology-Readiness-Assessment-and-SE-Integration/) | ISO 16290 |
| 102-700 | [Requirement Verifiability and Verification Planning Interface](102-700_Requirement-Verifiability-and-Verification-Planning-Interface/) | ISO 23135 — verification programme owned by 105 |
| 102-800 | [Model Based Systems Engineering and Digital Continuity](102-800_Model-Based-Systems-Engineering-and-Digital-Continuity/) | Register-derived; MBSE sources pending |
| 102-900 | [SE Products Evidence and Review Readiness](102-900_SE-Products-Evidence-and-Review-Readiness/) | ISO 18676; ISO 21349 |

## Boundary summary

Mission concepts and ConOps: 101 — consumed here as the source of requirements derivation and architecture definition. Requirement instances: downstream programme artefacts; the taxonomy holds classes and grammars, never programme requirements — the same rule covers specification instances (102-300 owns document classes), architecture instances (102-400 owns the method), and executable models (102-500 owns model classes, assumptions, validation-state metadata and exchange governance). Maturity: shared doctrine 100-500; TRL assessment and SE integration 102-600. Verification split: verifiability, method allocation and the traceability interface 102-700; programme governance, execution, qualification, acceptance and evidence 105. MBSE split: model semantics, viewpoints and digital continuity 102-800; configuration status, baselines and records 103. Reviews: product readiness and evidence sufficiency 102-900; process, authorities, gates and records 103. Assurance and dependability: 104. Interface control: interface requirements originate through 102; ICD structures and controlled execution 106. Classes 190-199 constrain architecture definition and shall not duplicate the SE discipline.

