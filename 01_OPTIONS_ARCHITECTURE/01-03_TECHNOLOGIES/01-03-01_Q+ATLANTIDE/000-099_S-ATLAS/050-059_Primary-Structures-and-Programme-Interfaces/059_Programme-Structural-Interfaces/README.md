# 059_Programme-Structural-Interfaces

**Range:** 050-059_Primary-Structures-and-Programme-Interfaces · **Chapter:** 059

## Scope

The interface doctrine of the structures range toward downstream mapping layers: the layer model, applicability and effectivity grammar, interface-definition schema classes, assembly and station convention classes, crosswalk doctrine, the structural evidence interface, change propagation, interface governance and machine-readable automation. Rule of the chapter: schemas and doctrine live here; instances live downstream. This chapter declares no applicability and names no programme — it defines how programmes declare applicability onto chapters 050-058, in their impact studies, product breakdown structures and data-module mappings.

## Integration chain

```mermaid
flowchart LR
  T["Taxonomy layer<br>050-058 chapters<br>(technology, agnostic)"]
  C["Type-class layer<br>090-099<br>(configuration constraints)"]
  D["Downstream layer<br>impact studies · PBS · DMC<br>(instances, effectivity)"]
  S["059<br>Interface doctrine<br>and schema classes"]
  T --&gt; D
  C -. "constrains" .-&gt; D
  S -. "defines how the mapping<br>is declared" .-&gt; D
  S -. "governs crosswalks<br>and change propagation" .-&gt; T
```

## Section register

| Section | Title | Subjects |
|---|---|---|
| 059-000 | [General and Layer Doctrine](059-000_General-and-Layer-Doctrine/) | 3 |
| 059-100 | [Downstream Mapping Model](059-100_Downstream-Mapping-Model/) | 4 |
| 059-200 | [Effectivity and Declaration Grammar](059-200_Effectivity-and-Declaration-Grammar/) | 4 |
| 059-300 | [Downstream Interface Definition Schemas](059-300_Downstream-Interface-Definition-Schemas/) | 4 |
| 059-400 | [Assembly and Station Convention Classes](059-400_Assembly-and-Station-Convention-Classes/) | 3 |
| 059-500 | [Crosswalks and Legacy Mapping Doctrine](059-500_Crosswalks-and-Legacy-Mapping-Doctrine/) | 3 |
| 059-600 | [Structural Evidence Interface](059-600_Structural-Evidence-Interface/) | 3 |
| 059-700 | [Change Propagation and Impact Doctrine](059-700_Change-Propagation-and-Impact-Doctrine/) | 3 |
| 059-800 | [Interface Governance and Ratification](059-800_Interface-Governance-and-Ratification/) | 3 |
| 059-900 | [Machine Readable Interfaces and Automation](059-900_Machine-Readable-Interfaces-and-Automation/) | 4 |

## Boundary summary

Rule of the chapter: schemas and doctrine here; instances downstream. This chapter names no programme and declares no applicability — it defines how downstream layers declare theirs. Taxonomy content: chapters 050-058 own their technology and evidence subjects. Type classes: 090-099 constrain configurations; their relationship to downstream layers is 090-500. Publication-standard applicability constructs: referenced as standards, never re-specified. Passport channel: 045. Practices: 051. Misplaced downstream instance files relocate to their layer — the taxonomy hosts their schema classes only (059-300).
