# 101_Mission-Architecture-and-Operational-Concepts

**Band:** 100-199_S-STA · **Range:** 100-109 · **Status:** Register-derived chapter at dual grain — sections and subjects cite standards-register anchors; merge constitutes ratification of this chapter register under S-STA-BAND-RULING v0.4 §6. Source governance: a declared absence is preferred to a false anchor.

## Scope

Mission-level architecture and operational concepts as discipline doctrine: mission classes and typologies, concept-of-operations doctrine, mission phases and lifecycle model, design reference missions and profiles, operability doctrine, serviced and revisitable mission architectures, crewed and uncrewed concepts, multi-element and campaign architectures, and concept-phase evidence. This chapter owns concepts and doctrine; operational execution is 170-179 (commissioning doctrine here, commissioning operations 171); programme structure and reviews are 103; system and vehicle classes are 190-199 — mission classes cut across them and never duplicate them.

## Concept flow

```mermaid
flowchart LR
  MC["101-100 Mission architecture<br/>classes and segments"] --> CO["101-200<br/>Concept of operations"] --> PH["101-300 Mission phases and<br/>multi-cycle timeline"] --> PR["101-400 Profiles and<br/>design reference missions"]
  OP["101-500 Operability and<br/>operations-driven design"] --- CO
  CM["101-600 Commissioning and<br/>early-operations doctrine"] --- PH
  SV["101-700 Serviced and<br/>revisitable architectures"] --- PH
  ME["101-800 Multi-element, fleet<br/>and campaign concepts"] --- PR
  PR --> EV["101-900 Concept products,<br/>evidence, review readiness"]
  PH -. "operational execution" .-> X170["170-179"]
  CM -. "commissioning execution" .-> X171["171"]
  PH -. "phase gates and reviews" .-> X103["103"]
  MC -. "class constraints" .-> X190["190-199"]
  SV -. "RPO/OOS execution" .-> X172["172-174"]
  EV -. "maturity application" .-> X100["100-500"]
```

## Section register

| Section | Title | Subjects | Anchors |
|---|---|---|---|
| 101-000 | [General Information](101-000_General-Information/) | 2 | — |
| 101-100 | [Mission Architecture Classes and Segments](101-100_Mission-Architecture-Classes-and-Segments/) | 4 | Register-derived; direct architecture source pending |
| 101-200 | [Concept of Operations Doctrine](101-200_Concept-of-Operations-Doctrine/) | 3 | ISO 14711 |
| 101-300 | [Mission Phases and Multi Cycle Timeline Model](101-300_Mission-Phases-and-Multi-Cycle-Timeline-Model/) | 4 | ISO 14300-1; ISO 21349 |
| 101-400 | [Mission Profiles and Design Reference Missions](101-400_Mission-Profiles-and-Design-Reference-Missions/) | 3 | — |
| 101-500 | [Operability and Operations Driven Design](101-500_Operability-and-Operations-Driven-Design/) | 3 | ISO 14950 — uncrewed-spacecraft baseline |
| 101-600 | [Commissioning and Early Operations Doctrine](101-600_Commissioning-and-Early-Operations-Doctrine/) | 3 | ISO 10784-1/-2/-3 |
| 101-700 | [Serviced and Revisitable Mission Architectures](101-700_Serviced-and-Revisitable-Mission-Architectures/) | 3 | ISO 24330 — RPO/OOS anchor |
| 101-800 | [Multi Element Fleet and Campaign Concepts](101-800_Multi-Element-Fleet-and-Campaign-Concepts/) | 3 | — |
| 101-900 | [Mission Concept Products Evidence and Review Readiness](101-900_Mission-Concept-Products-Evidence-and-Review-Readiness/) | 3 | ISO 14711; ISO 16290; ISO 21349; ISO 23135 |

## Boundary summary


