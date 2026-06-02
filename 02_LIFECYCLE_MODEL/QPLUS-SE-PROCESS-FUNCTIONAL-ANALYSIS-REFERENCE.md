---
document_id: QPLUS-SE-PROCESS-FUNCTIONAL-ANALYSIS-REFERENCE
title: "Systems Engineering Process & Functional Analysis — Reference Diagrams"
register: Q-plus
architecture: OPTIONS_ARCHITECTURE
options_axis: S-Standards
governance_class: methodology-reference
status: draft
version: "0.1.0"
language: en
source:
  title: "Systems Engineering Fundamentals"
  publisher: "Defense Acquisition University Press, Fort Belvoir VA"
  date: "January 2001"
  rights: "U.S. Government work — public domain"
  figures_adapted: ["Fig 3-1 SE Process", "Fig 5-4 FFBD Format", "Fig 5-5 IDEF0 Box Format"]
---

# Systems Engineering Process & Functional Analysis — Reference Diagrams

![methodology](https://img.shields.io/badge/governance-methodology%20reference-2d7a2d)
![source-DAU](https://img.shields.io/badge/source-DAU%20SE%20Fundamentals%202001-0075ca)

## 1. Purpose and source

This reference renders the foundational systems-engineering diagrams used across Q-plus-A as **Mermaid**, so they live in the controlled repository rather than as external images. The diagrams are adapted from the *Systems Engineering Fundamentals* text (Defense Acquisition University Press, January 2001), a U.S. Government work in the public domain.

These diagrams are the methodological origin of several Q-plus constructs: the **ReqBS class set**, the **breakdown structures** (FBS/IBS/TPMS), the **requirements evolution rule**, and **System Analysis & Control** (risk/CM/TPM). §5 maps each diagram to the rule it underpins.

---

## 2. The Systems Engineering Process (adapted from Fig 3-1)

The process is iterative and recursive: inputs are analyzed into requirements, decomposed into functions, synthesized into a physical design, and verified — with three feedback loops (requirements, design, verification) and a balancing control activity acting across all steps.

```mermaid
flowchart TB
    IN["<b>Process Input</b><br/>Customer needs, objectives,<br/>requirements, constraints<br/>Technology base · prior outputs<br/>Specifications & standards"]
    RA["<b>Requirements Analysis</b><br/>Analyze missions & environments<br/>Identify functional requirements<br/>Define / refine performance &<br/>design-constraint requirements"]
    FA["<b>Functional Analysis / Allocation</b><br/>Decompose to lower-level functions<br/>Allocate performance to all levels<br/>Define / refine functional interfaces<br/>Integrate functional architecture"]
    SY["<b>Synthesis</b><br/>Transform functional → physical<br/>Define alternative concepts, CIs,<br/>system elements<br/>Define / refine physical interfaces"]
    OUT["<b>Process Output</b><br/>Decision database<br/>System / CI architecture<br/>Specifications & baselines"]
    SAC["<b>System Analysis &amp; Control (Balance)</b><br/>Trade-off studies · effectiveness analyses<br/>Risk · configuration · interface · data mgmt<br/>Performance measurement — SEMS / TPM / reviews"]

    IN --> RA
    RA --> FA
    FA --> SY
    SY --> OUT
    FA -. "Requirements Loop" .-> RA
    SY -. "Design Loop" .-> FA
    SY -. "Verification" .-> RA
    RA <--> SAC
    FA <--> SAC
    SY <--> SAC

    classDef control fill:#efe9f5,stroke:#6d4c9e,stroke-width:2px;
    classDef io fill:#eef4fb,stroke:#0075ca;
    class SAC control;
    class IN,OUT io;
```

---

## 3. Functional Flow Block Diagram — FFBD format (adapted from Fig 5-4)

The FFBD describes **what** the system does and in **what sequence**, functionally — not how it is built. Grammar: each function is a single block with a consistent number (`1.0`, `1.1`, `1.1.1`); circular **summing gates** carry `AND` (parallel — all paths required) or `OR` (alternative paths); **GO / NO-GO** branches (`G` / `G̅`) leave a function to indicate conditional paths; **reference blocks** point to other diagrams; a **tentative function** is drawn dashed.

```mermaid
flowchart LR
    R35["3.5<br/>(Ref)"]:::ref
    R112["1.1.2<br/>(Ref)"]:::ref
    A1(("AND")):::gate
    F1["9.2.1<br/>First function"]
    A2(("AND")):::gate
    O1(("OR")):::gate
    F2["9.2.2<br/>Parallel<br/>function"]
    F3["9.2.3<br/>Alternate<br/>function"]
    F4["9.2.4<br/>Sys malf."]
    A3(("AND")):::gate
    O2(("OR")):::gate
    FC["9.2.5<br/>Function"]
    O3(("OR")):::gate
    FN["9.2.6<br/>No-go<br/>function"]
    O4(("OR")):::gate
    R1131["11.3.1<br/>(Ref)"]:::ref
    TENT["Tentative<br/>function"]:::tentative

    R35 --> A1
    R112 --> A1
    A1 --> F1
    F1 --> A2
    F1 --> O1
    A2 --> F2
    O1 --> F3
    O1 --> F4
    F2 --> A3
    F3 --> O2
    F4 --> O2
    A3 --> FC
    O2 --> FC
    FC -- "GO (G)" --> O3
    FC -- "NO-GO" --> O4
    O3 --> R1131
    O4 --> FN
    FN --> O4
    O3 --> TENT

    classDef ref fill:#fff,stroke:#333,stroke-dasharray:0,stroke-width:1px;
    classDef gate fill:#dfe9f7,stroke:#0075ca,stroke-width:1px;
    classDef tentative fill:#eee,stroke:#999,stroke-dasharray:5 4;
```

**Gate semantics.** `AND` = parallel functions, all conditions must be satisfied to proceed. `OR` = alternative paths, any one satisfies. `G` / `G̅` = go / no-go conditions placed on the lines leaving a function. `(Ref)` blocks connect this diagram to higher- or lower-level FFBDs (the second-level flow designator and title block are omitted here for clarity).

### 3.1 Applied micro-example (Q-plus domain — not from source)

A small FFBD fragment for radome operational functions, using the same grammar:

```mermaid
flowchart LR
    S["3.0<br/>(Ref)<br/>Power on"]:::ref
    G1(("AND")):::gate
    F1["3.1<br/>Energize<br/>weather radar"]
    F2["3.2<br/>Transmit / receive<br/>through radome"]
    D(("OR")):::gate
    F3["3.3<br/>Detect<br/>moisture / damage"]
    OK["3.4<br/>Continue<br/>scan"]
    NG["3.5<br/>Flag RF<br/>degradation"]
    E["4.0<br/>(Ref)<br/>Maintenance"]:::ref

    S --> G1
    G1 --> F1
    F1 --> F2
    F2 --> F3
    F3 -- "GO: nominal" --> OK
    F3 -- "NO-GO: degraded" --> D
    D --> NG
    NG --> E

    classDef ref fill:#fff,stroke:#333,stroke-width:1px;
    classDef gate fill:#dfe9f7,stroke:#0075ca,stroke-width:1px;
```

---

## 4. IDEF0 box — ICOM format (adapted from Fig 5-5)

Where the FFBD shows functional flow, **IDEF0** shows data/control flow and lifecycle-process flow. Each function box has four sides — the **ICOM** convention: **I**nputs enter from the left, **C**ontrols from the top, **O**utputs leave to the right, **M**echanisms join at the bottom. Edge labels below name the true ICOM side.

```mermaid
flowchart TB
    C["<b>Control</b><br/>constraints, guidance, standards"]
    I["<b>Input</b><br/>data / objects acted upon"]
    FN["<b>Function Name</b><br/><i>Function Number</i>"]:::fn
    O["<b>Output</b><br/>result of the operation"]
    M["<b>Mechanism</b><br/>supporting means / resources"]

    C -- "top" --> FN
    I -- "left" --> FN
    FN -- "right" --> O
    M -- "bottom" --> FN

    classDef fn fill:#dfe9f7,stroke:#0075ca,stroke-width:2px;
```

---

## 5. Mapping to the Q-plus framework

Each diagram is the method behind a controlled rule already in the repository.

| Source diagram | Q-plus construct it underpins |
|---|---|
| SE Process — Requirements Loop & Design Loop (Fig 3-1) | `REQBS-REV-001` (requirements evolve by revision); the loops are *why* ReqBS/IBS/CBS/RBS/EBS are revisioned, not static. |
| SE Process — System Analysis & Control (Fig 3-1) | `RBS` (risk), `TPMS` (technical performance measures = TPM/SEMS), and configuration-management authority in the lifecycle model. |
| SE Process — Synthesis → Output baselines (Fig 3-1) | `QATL-BASELINE-HIERARCHY-001` (functional / allocated / product baselines). |
| FFBD (Fig 5-4) | Functional Analysis/Allocation → `FBS` and `ReqBS-10` (Functional Requirements), `ReqBS-12` (Modes of Operation). |
| IDEF0 / ICOM (Fig 5-5) | Interface and data/control flow → `IBS` and `ReqBS-07` (Interfaces). |

---

## 6. Footprint

| Field | Value |
|---|---|
| Document ID | `QPLUS-SE-PROCESS-FUNCTIONAL-ANALYSIS-REFERENCE` |
| Register | Q-plus / OPTIONS (S-Standards) |
| Source | DAU *Systems Engineering Fundamentals*, Jan 2001 (public domain) |
| Diagrams | SE Process, FFBD format, IDEF0 box, applied FFBD micro-example |
| Version | 0.1.0 |
| Status | draft |
| Evidence anchor (IEF) | `<sha256: to-be-stamped-at-commit>` |

**Change log.**

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-05-31 | Initial Mermaid renderings of SE Process (Fig 3-1), FFBD format (Fig 5-4), IDEF0 box (Fig 5-5); framework mapping to ReqBS/FBS/IBS/TPMS/RBS and the requirements-evolution and baseline-hierarchy rules. |
