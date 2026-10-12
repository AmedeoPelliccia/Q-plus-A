---
document_id: QPLUS-A-02-LIFECYCLE-MODEL-README
title: "Q-plus-A — Lifecycle Model"
repository: Q-plus-A
path: 02_LIFECYCLE_MODEL/README.md
register: Q-plus
architecture: OPTIONS_ARCHITECTURE
status: draft
version: "0.7.0"
revision: H
classification: open-governance-baseline
owner: AEROSPACEMODEL / Q-plus
lifecycle_model: "LC-letter deliverable-layer maturity model (anchored letters, decoupled iteration)"
execution_method: "C-GROWTH (Q+A-METHOD-CGROWTH-SPEC-001)"
doctrine: "SICO.CA — Sustainable Industry Continuous Operations · Chained Algorithms"
language: en
---

# 02_LIFECYCLE_MODEL — Lifecycle Model

## 1. Purpose

`02_LIFECYCLE_MODEL/` defines the controlled lifecycle maturity model used by Q-plus-A artefacts, products, CAD models, PLM records, publication modules, requirements records, evidence records, upgrade branches, and configuration baselines.

This lifecycle model provides a common governance language for the deliverables of every lifecycle stage — from conceptual definition through preliminary design, detailed design, qualification, certification, operations, MRO, and final nature-sustainment.

Version `0.4.0` extended the lifecycle model with TRL integration, upgradeability and technology-insertion governance, upgrade revision-cycle restart rules, evolutionary block logic, SBS-level breakdown integration, and revision-specific `ReqBS`, `IBS`, `CBS`, `RBS`, `EBS`, `TPMS`, BOM, CAD, and publication records.

Version `0.5.0` bound the **C-GROWTH execution method** (`Q+A-METHOD-CGROWTH-SPEC-001`, co-located in this folder) as the controlled intra-stage execution engine.

Version `0.6.0` applies a **critical structural correction**: LC stages are **deliverable layers**, each with its REV letter **anchored**; iteration numbers are **decoupled** across layers; cross-layer consistency is maintained exclusively by **SSOT source-data pinning**; and **every stage may initiate its own C-GROWTH revolutions and work packages independently** of upstream stage activity. See §2.

Version `0.7.0` makes **partial maturation cycles** explicit. A product that is to incorporate future technologies does not mature uniformly: one scope — an E-pack, a tank, an inverter — may pass several times through concept, design, analysis and test while the rest of the product holds more mature baselines. The version adds the **scoped maturation cycle** (§13.1), **decision-relative maturity thresholds** (§13.2), **physical-article availability per scope** (§2.3), and **publication content classes** (§2.4), which separate publication planning, which may start at concept, from prescriptive manual content, which may not. It also binds the model to **AGES** (§2.5): ages bounded by ratified baselines, and an evolutionary memory that keeps every stage reconstructable — superseded baselines, rejected candidates and negative results included.

It retains the single LC-letter lifecycle axis (no enterprise LC01–LC14 axis). The only orthogonal overlay is TRL (technology maturity), which is distinct from LC-letter (deliverable maturity) by design — see §13.

---

## 2. Lifecycle Model Type

Q-plus-A uses an **LC-letter deliverable-layer maturity model**: each LC stage owns a deliverable set, and the deliverables of every stage carry that stage's letter permanently.

```text
LC-letter stage      = deliverable stage / layer (its deliverables carry that letter, always)
REV-<LETTER><n>      = iteration n of that stage's deliverable set
                       — the LETTER is anchored to the stage and never changes
                       — only the NUMBER iterates
*_RELEASED           = formal release baseline of that stage's deliverable set
```

### 2.1 Anchored Letters, Decoupled Numbers

The lifecycle has two distinct regimes:

**Staged initialization (sequential).** A stage's deliverable layer is first initialized only after the upstream layer reaches a usable released baseline. The first `REV-B0` exists only after `REV-A_RELEASED`; the first operations manual `REV-L0` exists only once there is a released design/certification baseline to document. Publication *architecture* — DMRL, business rules, identifiers, publication structure — is not manual content and is not bound by this rule; publication deliverables are classed by content in §2.4. Development articles of a scoped maturation cycle initialize `LC-F` on the controlled path of `QPLUS-LC-ARTICLE-SCOPE-001` (§2.3), not after an `LC-E` release.

**Concurrent evolution (decoupled).** Once initialized, **every layer iterates independently**. Iteration in one layer does not, by itself, create iterations in any other layer:

- A `REV-C3` in detailed design **may not generate** a new `REV-Lx` or `REV-Mx` in manuals, DMs, or infocodes. Whether it does is the outcome of an impact assessment, not an automatic propagation.
- A manual **may iterate without any design change**: service bulletins, document-structure improvements, infocode reorganizations, or regulatory editorial requirements create a new `REV-Mx` while the design SSOT remains unchanged.

```mermaid
flowchart LR
    subgraph LCC["LC-C layer — detailed design"]
        direction LR
        C2["REV-C2_RELEASED"] --> C3["REV-C3<br/>(iterating)"]
    end
    subgraph LCL["LC-L layer — operations documentation"]
        direction LR
        L1["REV-L1"] --> L2["REV-L2"]
    end
    subgraph LCM["LC-M layer — MRO documentation"]
        direction LR
        M4["REV-M4"] --> M5["REV-M5<br/>(SB-driven, no design change)"]
    end
    C2 -. "SSOT pin: source data" .-> L2
    C2 -. "SSOT pin: source data" .-> M4
    C2 -. "SSOT pin unchanged" .-> M5
```

In the figure: design iterates to `REV-C3` without forcing any documentation iteration; `REV-M5` iterates on a service bulletin while remaining pinned to the same released design source (`REV-C2_RELEASED`).

```yaml
rev_letter_anchoring_rule:
  id: QPLUS-LC-REVLETTER-001
  name: "REV Letter Anchoring Rule"
  rule: >
    The REV letter of a deliverable is anchored to its owning LC stage and
    shall never change over the deliverable's life. Design deliverables of
    LC-C are always REV-Cx; operations documentation of LC-L is always
    REV-Lx; MRO documentation of LC-M is always REV-Mx. Only the iteration
    number advances. The REV letter identifies the deliverable layer, not the
    product's current position on the lifecycle axis.

decoupled_iteration_rule:
  id: QPLUS-LC-DECOUPLE-001
  name: "Decoupled Iteration Rule"
  rule: >
    Iteration counters are independent per LC stage layer. An iteration in one
    layer shall not, by itself, create an iteration in any other layer.
    Cross-layer propagation occurs only through impact assessment: an upstream
    change either results in a downstream iteration with updated source-data
    pinning, or in a recorded no-action disposition. Both outcomes are
    controlled records.
```

### 2.2 SSOT Source-Data Pinning

Decoupling is safe only because coupling is moved into the SSOT: every downstream deliverable revision must declare exactly which upstream artefact revisions it consumed.

```yaml
ssot_source_pinning_rule:
  id: QPLUS-LC-SSOT-PIN-001
  name: "SSOT Source-Data Pinning Rule"
  rule: >
    Every REV of a downstream deliverable shall record in its SSOT stack the
    identified revisions of the upstream artefacts used as source data (the
    "pinned source set"). A REV-Lx or REV-Mx publication revision shall pin
    the relevant last design artefact used as source data (e.g.
    RADOME-REV-C2_RELEASED). A deliverable revision without a valid pinned
    source set is non-conformant. When an upstream artefact changes, each
    downstream layer shall perform an impact assessment and either (a) iterate
    and re-pin to the new source, or (b) record a no-action disposition with
    rationale, retaining the existing pin. When a deliverable iterates for
    layer-internal reasons (service bulletin, structure improvement), it shall
    re-validate and restate its pinned source set, which may be unchanged.
```

Minimum pinning metadata, carried per deliverable REV:

```yaml
pinned_source_set:
  deliverable_revision: "AMM-RADOME-REV-M5"
  iteration_driver: "service bulletin"      # enum: upstream-source-delta | service-bulletin | structure-improvement | regulatory | feedback-package | other
  pins:
    - artefact: "RADOME design baseline"
      pinned_revision: "RADOME-REV-C2_RELEASED"
      pin_status: "unchanged"               # enum: new | re-pinned | unchanged
    - artefact: "ReqBS"
      pinned_revision: "ReqBS-RADOME-REV-C2"
      pin_status: "unchanged"
  upstream_deltas_assessed:
    - upstream_change: "RADOME-REV-C3 (iterating, not released)"
      disposition: "no-action"
      rationale: "C3 not released; pin remains on last released design baseline"
```

### 2.3 Execution Method within a Stage Layer — C-GROWTH

The LC-letter axis defines **deliverable layers**; the REV cycle defines **iterations per layer**; **C-GROWTH** defines **how iterations are produced**. C-GROWTH (Circular Growing by Generation, Reviewing, Optimizing, Workflowing, Testing, Hardware) is the controlled execution method, materializing the SICO.CA doctrine in governed algorithms. Its normative definition is `Q+A-METHOD-CGROWTH-SPEC-001` (this folder); this section controls only the binding.

**Independent initiation.** Because layers iterate independently, **every LC stage may start new C-GROWTH revolutions and initiate work packages from stage-local inputs**, independent of upstream stage activity:

```yaml
cgrowth_independent_initiation_rule:
  id: QPLUS-LC-CG-INIT-001
  name: "Per-Stage C-GROWTH Initiation Rule"
  rule: >
    Each LC stage layer may initiate C-GROWTH revolutions and work packages
    from inputs local to that layer — upstream source-data deltas, service
    bulletins, document-structure improvements, operator feedback, regulatory
    change, or routed feedback packages — independent of whether any upstream
    or downstream layer is currently iterating. Every revolution executes
    within exactly one stage layer, and its gate records (G1–G6) attach to the
    REV of that layer. Revolutions in different layers are coordinated only
    through SSOT source-data pinning (QPLUS-LC-SSOT-PIN-001), never through
    forced co-revision.

cgrowth_binding_rule:
  id: QPLUS-LC-CGROWTH-001
  name: "C-GROWTH Binding Rule"
  rule: >
    The C-GROWTH gate family (G1–G6, loop transitions) and the lifecycle gate
    family (*_RELEASED, layer baseline release) are disjoint: neither
    substitutes for the other. A layer's baseline is released only by its
    approved *_RELEASED revision; a loop transition is authorized only by its
    G-gate.
```

**Feedback-package routing.** A CH→CG feedback package (in-service evidence, qualification correlation, teardown findings) may affect several layers at once. The package shall be routed to **every affected layer**, and each affected layer opens its own CG entry — e.g., an in-service anomaly may simultaneously seed a design fix revolution in the LC-C layer and a procedure revision revolution in the LC-M layer. Each resulting deliverable REV re-pins per §2.2.

**Gate family separation:**

| Gate family | Governs | Authority | Defined in |
|---|---|---|---|
| `G1–G6` | Loop transitions inside a revolution (per layer) | Per C-GROWTH gate matrix | `Q+A-METHOD-CGROWTH-SPEC-001` §5 |
| `*_RELEASED` | Layer baseline release | Per §5 of this README | This README |

The single deliberate coupling point is **G5 (CT→CH)**: placing an artefact on hardware requires both C-GROWTH test coverage and lifecycle authorization, because physical-article availability is a property of the programme state, declared per scope (`QPLUS-LC-ARTICLE-SCOPE-001`), not of the method.

**CH availability.** The CH loop activates only where physical articles exist. Physical-article availability is declared **per scope**. The table gives the programme-level default, consumed by all layers; a scoped maturation cycle (§13.1) may make development articles of its own scope available earlier:

| Programme state | C-GROWTH conformance mode | CH instantiation |
|---|---|---|
| No physical article (typically before `LC-F` deliverables exist) | **C-GROWTH/CT-bounded** — revolutions terminate at CT in every layer | None (digital-only; simulation under CT) |
| First physical article (`LC-F` PMA / Wind Tunnel deliverables) | **G5/G6 activation milestone** | Mock-up, wind-tunnel article |
| Qualification through industrialization (`LC-G`–`LC-K` articles) | Full C-GROWTH | Qualification articles, iron-bird, embodied hardware, flight-test asset |
| In service (`LC-L`/`LC-M` layers active) | Full C-GROWTH, terminal CH | The in-service vehicle as its own correlation instrument; feedback packages route to design and documentation layers |
| Retirement (`LC-N` layer) | CH closes | Teardown evidence as final feedback packages into circularity records |

```yaml
article_scope_rule:
  id: QPLUS-LC-ARTICLE-SCOPE-001
  name: "Physical-Article Availability per Scope"
  rule: >
    Physical-article availability, and with it CH instantiation, is declared
    per scope. A scoped maturation cycle (§13.1) may place development
    articles of its own scope — breadboard, brassboard, prototype, test rig —
    into CH before any programme-level physical article exists. Such articles
    and their test records are LC-F deliverables of that scope, and they
    initialize LC-F for the scope on a controlled path of their own rather
    than after an LC-E release: the definition the article embodies is
    released at the layer that defines it; the article's configuration is
    identified; test objectives and correlation thresholds are declared
    before execution; the hazards of the trial itself are assessed and
    controlled; and its P1 instructions carry a limit of use. G5 placement
    of each article is then authorized by the LC-phase authority for that
    scope alone, and does not change the C-GROWTH conformance mode declared
    for the rest of the programme.
```

**Findings coupling.** C-GROWTH CR dispositions and feedback packages produce findings in the classes of §6 (`F-INFO` / `F-WARN` / `F-BLOCK` / `F-DEFER`), raised against the REV of the layer in which the revolution ran. Open `F-BLOCK` findings block that layer's `*_RELEASED`.

**Upgrade branches.** C-GROWTH applies identically to upgrade branches (§14–§15): an upgrade branch starting at `<ITEM>-UPG-<NNN>-REV-A0` initializes its own layer set and runs its own revolutions; its records attach to the upgrade-specific REV identifiers.

### 2.4 Publication Content Classes

Planning publications early is sound; prescribing actions on a product that is still hypothetical is not. Every publication artefact therefore declares a **content class**, and each class has its own gate:

| Class | Content | May proceed | Carried as |
|---|---|---|---|
| `P0` Publication architecture | DMRL, business rules, SNS and data-module codes, publication-module structure, illustration planning, publication plan; data-module shells with no prescriptive content | From `LC-A` | TPuBS architecture records, controlled by issue — not `REV-Lx` / `REV-Mx` |
| `P1` Experimental instructions | Instructions to build, install, operate, test or maintain a development or qualification article | Only for an authorized experimental configuration, verified against it — procedures also validated — before use, with an explicit limit of use | Deliverables of the layer whose article they serve: `LC-F` (development), `LC-G` (qualification) |
| `P2` Released operational and maintenance content | Manuals; descriptive and procedural data modules for operational use | When the pinned source set consists of released product baselines applicable to the configuration served, all content has been verified against those sources, and each procedure has also been validated for its intended use | `LC-L` / `LC-M` deliverables, `REV-Lx` / `REV-Mx` |

```yaml
publication_content_class_rule:
  id: QPLUS-LC-PUBCLASS-001
  name: "Publication Content Classes and Gates"
  rule: >
    Every publication artefact declares one content class. P0 publication
    architecture may be created and iterated from LC-A onward; it plans
    publications, carries no prescriptive content (no procedural step,
    limit, value, warning or caution), and is never the authority for a
    product statement: the link runs from product to publication only. P1
    experimental instructions exist only for an authorized experimental
    configuration; they name the article and configuration they apply to,
    carry an explicit limit of use, and are verified against that article
    and configuration, with their procedures validated, before use. P2
    content is released only when its pinned source set
    (QPLUS-LC-SSOT-PIN-001) consists of released product baselines
    applicable to the configuration it serves, all of it — descriptive as
    well as procedural — has been verified against those sources, and each
    procedure has also been validated for its intended use. A
    data-module shell may exist as P0; it becomes P1 or P2 only by passing
    that class's gate, and its status states its class truthfully.
```

The classes are alternatives, not stages. A `P0` shell becomes `P1` or `P2` directly, at that class's own gate. `P1` instructions remain deliverables of `LC-F` / `LC-G` and never turn into `P2` content, although experience gained with them may inform the validation of `P2` procedures.

The classes govern technical publications — TPuBS items. Engineering and certification records — compliance reports, certification plans, type-design data — are deliverables of their own layers (for example `LC-J`) under release gates, not publications. Authority-approved operational and maintenance publications, such as the flight manual or the airworthiness limitations, are `P2`.

**Where the P2 gate falls.** Not at TRL 9 (actual system proven through successful mission operations): operational and maintenance content must exist before the operation it governs. For a type-certificated product the instructions for continued airworthiness are a certification deliverable — sufficient instructions must be available at design approval, and any remainder only under a programme that completes them before entry into service. The P2 gate of maintenance publications therefore falls within `LC-J`–`LC-K`, ahead of `LC-L` operations.

*Informative references:* 14 CFR 25.1529 — instructions for continued airworthiness may be incomplete at type certification if a programme ensures their completion before delivery of the first aeroplane or issue of a standard certificate of airworthiness, whichever is later; EASA Certification Memorandum CM-ICA-001 Issue 01 (2017), *Completeness and Timely Availability of Instructions for Continued Airworthiness*.

### 2.5 Ages and Evolutionary Memory — AGES Binding

Q-plus-A products are artificial evolutive systems in the sense of [AGES](https://github.com/AmedeoPelliccia/AGES) (Artificial General Evolutive Systems): *"An artificial evolutive system is not a photograph of one configuration. It is the governed continuity of its ratified states."* AGES places the ratified transition history inside identity itself — Identity(t) = ⟨Bₙ, 𝒯₀:ₙ, ℐₙ, E_f, Pₙ⟩: active baseline, ratified transition history, invariant set, effectivity, provenance. A product without a reconstructable memory of its stages has no evolutive identity.

This model adopts the AGES definitions below (AGES `GLOSSARY.md` and `architecture/02-state-and-transition-model.md`, both exploratory) and makes the Q-plus-A repository — Git history, SBS registers, EBS index — an AGES **underlying record system**: AGES baselines reference its records by immutable identifier, without duplicating them.

| AGES concept | AGES definition (abridged) | In this lifecycle model |
|---|---|---|
| Artefact revision | A change to tracked digital artefacts, e.g. a commit — not by itself an evolution transition | A `REV` iteration, a commit, a C-GROWTH revolution, a maturation-cycle pass |
| Candidate change | A proposed modification; it may be rejected, blocked, revised, withdrawn, validated but not authorised, and so on | A proposed baseline; an upgrade branch (§15); a maturation cycle before its exit decision (§13.1) |
| Controlled trial | Bounded experimentation under its own explicit, traceable authority | G5 placement of a development article for one scope (§2.3), with `P1` instructions (§2.4) |
| Ratification | The event through which a verified configuration becomes the canonical successor baseline and opens a new age | The recorded release decision — act, date, authority — of a scope's integrated baseline, by the authority designated for the scope, with its membership pinned |
| Age | Ageₙ = [ratify(Bₙ), ratify(Bₙ₊₁)) | The interval during which a ratified baseline remains canonical, per scope and effectivity |
| Ratified transition history 𝒯₀:ₙ | Part of identity | The chain of release decisions and `supersedes` links of a scope |
| Effectivity · invariants · provenance | E_f · ℐₙ · Pₙ | Applicability; the invariants declared with a baseline; pinned source sets, run records and content hashes |

```yaml
age_rule:
  id: QPLUS-LC-AGE-001
  name: "Age Rule (AGES binding)"
  rule: >
    Ages are kept per baseline scope and effectivity. An age is the interval
    during which a ratified baseline remains canonical: Age_n =
    [ratify(B_n), ratify(B_n+1)), as defined by AGES. The baseline that
    opens an age is the integrated baseline of its scope: it binds the
    released revisions of its member layers and views by immutable
    reference (commit and content hash), declares its effectivity and
    invariants, and names the baseline it supersedes — except the first
    baseline of a scope, whose ratification is the scope's genesis.
    Ratification is the recorded release decision — act, date, authority —
    of the ratification authority designated for the scope. For a given
    scope and effectivity at most one baseline is canonical at a time:
    ratifications are serialized, and a ratification is valid only if the
    baseline it supersedes is the one canonical at that moment. A layer's
    *_RELEASED revision is a member of a baseline and does not by itself
    open an age; whether it requires a new ratification is decided by the
    impact assessment of §2.1–§2.2, and a change to identity-relevant
    configuration (design, airworthiness limitations, invariants,
    effectivity) requires one. Nested scopes keep their own ages, and a
    parent baseline pins the child baselines it includes. Before genesis a
    scope has no canonical baseline and no age: its work forms the
    candidate history of its first baseline. REV iterations, commits,
    C-GROWTH revolutions and maturation-cycle passes do not by themselves
    open an age. A ratified concept baseline may govern an age of research;
    its use as a source of P2 content still requires the P2 gate (§2.4).

evolutionary_memory_rule:
  id: QPLUS-LC-MEMORY-001
  name: "Evolutionary Memory Rule"
  rule: >
    The evolutionary memory of every scope shall remain verifiable and
    usable. Superseded baselines remain reconstructable from their pinned
    references; candidate changes keep their final status (rejected,
    blocked, withdrawn, validated but not authorised, stopped); negative
    results, falsified findings and stopped maturation cycles are retained
    with their evidence. A correction supersedes and never overwrites, and
    no later event erases a ratification record. Where content may not be
    republished — protected third-party material, personal data — memory
    retains the fact, its reference and its hash, not a copy. A decision
    record cites the memory it relies on, including any superseded
    assumption or negative result that bears on it.
```

AGES leaves concurrent scope-specific ages and inheritance between scopes as open questions (AGES `models/temporal-model.md`; `architecture/README.md` §13). The scope, effectivity and composition provisions of `QPLUS-LC-AGE-001` are the Q-plus-A answer for its products, consistent with the AGES temporal model — every instant after genesis belongs to exactly one age per effectivity scope.

Reconstructable is not the same as reversible. A physical embodiment may not be undone: AGES-CPS distinguishes rollback, compensation, safe-state transition, containment and recovery baselines, and the reversibility class of a change is declared with it. Publications sit on ages through their pinned sources: a `P2` publication's pinned source set identifies the age it describes, and when a new age opens its disposition follows the impact assessment of §2.1–§2.2.

---

## 3. Controlled LC-letter Stages

Each stage is a **deliverable layer**. The "Scope" column describes the deliverable set whose REVs permanently carry that stage's letter.

| LC | Stage / Layer | Deliverable scope | Release Gate |
|---|---|---|---|
| `LC-A` | Conceptual Design | First concept, first geometry, early proportions, early feasibility placeholder, initial requirements baseline, initial upgrade watch list. | `REV-A_RELEASED` |
| `LC-B` | Preliminary Design | Main geometry, architecture sizing, preliminary interfaces, major configuration decisions, first interface-controlled upgrade compatibility logic. | `REV-B_RELEASED` |
| `LC-C` | Detailed Design | Detailed CAD/product definition, material stack, BOM/CAD consistency, drawing preparation, detailed `ReqBS/IBS/CBS/RBS/EBS/TPMS` alignment. | `REV-C_RELEASED` |
| `LC-D` | Analysis / Verification Design | Analysis-ready geometry, verification setup, simulation models, test logic, requirements verification planning. | `REV-D_RELEASED` |
| `LC-E` | Release Candidate / Engineering Definition | Engineering release candidate before physical mock-up, qualification, or certification use. | `REV-E_RELEASED` |
| `LC-F` | PMA — Physical Mock-Up Article and Wind Tunnel | Physical mock-up, installation mock-up, aerodynamic mock-up, wind-tunnel preparation; development test articles of scoped maturation cycles — breadboard, brassboard, prototype, test rig (§2.3, §13.1). | `REV-F_RELEASED` |
| `LC-G` | Qualification | Qualification test article, qualification evidence, test reports, compliance-relevant records. | `REV-G_RELEASED` |
| `LC-H` | Hardware & Software Embodiment | Hardware embodiment, digital configuration, software/data integration, product-data binding. | `REV-H_RELEASED` |
| `LC-I` | Installation and Interface | Installation closure, interface maturity, aircraft or system integration readiness. | `REV-I_RELEASED` |
| `LC-J` | Certification | Certification configuration, compliance evidence, authority-facing artefacts. | `REV-J_RELEASED` |
| `LC-K` | First Flight and Industrialization | First-flight configuration, manufacturing readiness, industrialization transition. | `REV-K_RELEASED` |
| `LC-L` | Operations | In-service operational configuration and operations documentation (manuals, DMs, infocodes for operation), operator feedback, operational evidence. | `REV-L_RELEASED` |
| `LC-M` | MRO and Continuous Airworthiness | Maintenance, repair, overhaul documentation (AMM-class DMs and infocodes), service bulletins, continued-airworthiness records. | `REV-M_RELEASED` |
| `LC-N` | Nature Sustainment | Circular economy, retirement, reuse, disposal, recycling, environmental sustainment. | `REV-N_RELEASED` |

> [!NOTE]
> Naming reconciled in revision D: `LC-F` = **PMA** (Physical Mock-up Article — `PMU` collides with Power Management Unit in the electric programmes) and **Wind Tunnel** (not Wind Gallery); `LC-H` = **Software Embodiment**. The stage table (§3) and folder pattern (§7) now agree. If the prior terms are deliberate house terms, override here and record the decision.

---

## 4. Revision Naming Pattern

Generic revision pattern:

```text
REV-<LC_LETTER><SEQUENCE>
```

The `<LC_LETTER>` is the anchored letter of the deliverable's owning layer (`QPLUS-LC-REVLETTER-001`); the `<SEQUENCE>` is the layer-local iteration number (`QPLUS-LC-DECOUPLE-001`).

Examples:

```text
REV-A0
REV-A1
REV-A2
REV-A_RELEASED

REV-B0
REV-B1
REV-B_RELEASED
```

For item-specific usage, the item name may be prefixed:

```text
RADOME-REV-A0
RADOME-REV-A1
RADOME-REV-A_RELEASED
```

For deliverable-specific usage in documentation layers:

```text
AMM-RADOME-REV-M4
AMM-RADOME-REV-M5
AMM-RADOME-REV-M_RELEASED
```

For upgrade-specific usage, the upgrade identifier shall be included:

```text
RADOME-UPG-001-REV-A0
RADOME-UPG-001-REV-A1
RADOME-UPG-001-REV-A_RELEASED
```

---

## 5. Release Gate Rule

```yaml
release_gate_rule:
  id: QPLUS-LC-RELEASE-001
  rule: >
    A stage layer's deliverable baseline is released only through its approved
    *_RELEASED revision. The FIRST initialization of the next stage layer
    shall not start as a controlled baseline while blocking findings remain
    open in the upstream layer's pending release. Once a layer has been
    initialized, it iterates independently per QPLUS-LC-DECOUPLE-001, and a
    new iteration cycle within an already-initialized layer does not require
    re-authorization from upstream layers — only valid source-data pinning
    per QPLUS-LC-SSOT-PIN-001.
```

> [!NOTE]
> `*_RELEASED` gates are lifecycle gates. They are distinct from the C-GROWTH loop gates `G1–G6` (§2.3) and are never satisfied by them: completing revolutions does not release a baseline; only the approved `*_RELEASED` revision does.

---

## 6. Blocking Finding Rule

Any deliverable revision in any layer may record findings.

| Finding Class | Meaning | Gate Impact |
|---|---|---|
| `F-INFO` | Informational note. | Does not block release. |
| `F-WARN` | Warning or limitation. | May block release depending on severity. |
| `F-BLOCK` | Blocking finding. | Blocks `*_RELEASED` of the owning layer. |
| `F-DEFER` | Deferred to a later layer or iteration. | Does not block current release if explicitly accepted. |

```yaml
finding_rule:
  id: QPLUS-LC-FINDING-001
  rule: >
    No revision shall be promoted to *_RELEASED while F-BLOCK findings remain
    open against it. Deferred findings shall identify the layer and condition
    in which they become mandatory. Findings may originate from any source,
    including C-GROWTH CR dispositions and routed feedback packages (§2.3),
    and are raised against the REV of the layer in which they were found.
```

---

## 7. Artefact Folder Pattern

Recommended lifecycle folder pattern (rule `CAD-REVDIR-001`): each layer materializes as a directory family; each `REV` folder holds the native deliverable plus a stable-named `*-Record.md`. The CAD tree shown is the LC-A–LC-E design example; documentation layers follow the same pattern under their own roots (e.g., `pub/`).

```text
cad/
└── freecad/
    ├── LC-A_Concept-Design/
    │   ├── REV-A0/
    │   ├── REV-A1/
    │   ├── REV-A2/
    │   └── REV-A_RELEASED/
    │
    ├── LC-B_Preliminary-Design/
    │   ├── REV-B0/
    │   ├── REV-B1/
    │   └── REV-B_RELEASED/
    │
    ├── LC-C_Detailed-Design/
    ├── LC-D_Analysis-Verification-Design/
    ├── LC-E_Release-Candidate-Engineering-Definition/
    ├── LC-F_PMA-Physical-Mock-Up-and-Wind-Tunnel/
    ├── LC-G_Qualification/
    ├── LC-H_Hardware-and-Software-Embodiment/
    ├── LC-I_Installation-and-Interface/
    ├── LC-J_Certification/
    ├── LC-K_First-Flight-and-Industrialization/
    ├── LC-L_Operations/
    ├── LC-M_MRO-and-Continuous-Airworthiness/
    └── LC-N_Nature-Sustainment/
```

---

## 8. Minimum Lifecycle Metadata

Every controlled lifecycle record shall include:

```yaml
lifecycle_record:
  lifecycle_model: "LC-letter deliverable-layer maturity model"
  lc_layer: "LC-A"
  lc_layer_name: "Conceptual Design"
  current_revision: "REV-A0"
  revision_status: "created"        # enum: created | iterating | released
  next_release_gate: "REV-A_RELEASED"
  iteration_driver: "<see pinned_source_set enum>"
  pinned_source_set: []             # per QPLUS-LC-SSOT-PIN-001; empty only for root LC-A concept seeds
  blocking_findings: []
  deferred_findings: []
```

For item-specific records:

```yaml
item_lifecycle_record:
  pbs_id: "<PBS-ID>"
  part_number: "<PN>"
  lifecycle_model: "LC-letter deliverable-layer maturity model"
  lc_layer: "LC-A"
  current_revision: "<ITEM>-REV-A0"
  next_release_gate: "<ITEM>-REV-A_RELEASED"
  pinned_source_set: []
```

For upgrade-specific records:

```yaml
upgrade_lifecycle_record:
  upgrade_id: "<ITEM>-UPG-<NNN>"
  parent_baseline: "<baseline id>"
  lifecycle_model: "LC-letter deliverable-layer maturity model"
  lc_layer: "LC-A"
  current_revision: "<ITEM>-UPG-<NNN>-REV-A0"
  next_release_gate: "<ITEM>-UPG-<NNN>-REV-A_RELEASED"
  pinned_source_set:
    - artefact: "parent product baseline"
      pinned_revision: "<baseline id>"
      pin_status: "new"
```

Where C-GROWTH conformance is declared, the record may additionally carry:

```yaml
cgrowth_execution_record:
  cgrowth_conformance: "full | CT-bounded"        # per Q+A-METHOD-CGROWTH-SPEC-001 §8
  revolutions_completed_this_rev: 0
  open_feedback_packages: []
  last_gate_passed: "G0-none"                     # G1..G6
```

---

## 9. Traceability Chain

The lifecycle model shall preserve the following chain:

```text
PBS → PNR → PN → BOM → CAD → STEP → Drawing → Evidence → Lifecycle Gate
```

| Layer | Required |
|---|---|
| PBS item | Yes |
| PNR | Yes, for physical items |
| Part Number | Yes, for physical items |
| BOM | Yes, when composition is defined |
| CAD native file | Yes, when CAD exists |
| STEP/export file | Required when export is produced |
| Drawing | Required when drawing is produced |
| Evidence record | Yes |
| Release gate | Yes |

For engineering breakdown traceability, the revision shall also reference:

```text
PBS REV-X → ReqBS REV-X → IBS REV-X → CBS REV-X → RBS REV-X → EBS REV-X → TPMS REV-X
```

For cross-layer traceability, every downstream deliverable REV additionally references its pinned source set per `QPLUS-LC-SSOT-PIN-001`:

```text
AMM-<ITEM>-REV-Mx → pinned_source_set → <ITEM>-REV-C?_RELEASED (+ ReqBS, IBS, … as applicable)
```

---

## 10. Relationship to OPTIONS Architecture

This lifecycle model supports the `OPTIONS_ARCHITECTURE` repository structure.

```text
OPTIONS =
O  Organizations
P  Programmes
T  Technologies
I  Infrastructures
O  Operations
N  Neural Networks
S  Standards
```

Lifecycle records may appear under product-specific folders, especially under `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/…`. The root lifecycle model remains the controlling reference.

---

## 11. SBS Integration and Revisioned Breakdown Structures

Each SBS acts as the parent integration layer for controlled breakdown structures.

```text
SBS_System-Breakdown-Structure/
├── PBS_Product-Breakdown-Structure/
├── FBS_Functional-Breakdown-Structure/
├── WBS_Work-Breakdown-Structure/
├── CBS_Cost-Breakdown-Structure/
├── RBS_Risk-Breakdown-Structure/
├── LBS_Logistic-Breakdown-Structure/
├── EBS_Evidence-Breakdown-Structure/
├── IBS_Interface-Breakdown-Structure/
├── ReqBS_Requirements-Breakdown-Structure/
├── TPMS_Technical-Performance-Measurement-Structure/
└── TPuBS_Technical-Publications-Breakdown-Structure/
```

The SBS defines the breakdown family. The PBS defines the physical item. Each `PBS REV-X` defines the authoritative state of its associated revision-specific breakdowns.

The **TPuBS** structures the technical-publications deliverable set (PMCs, subject nodes, DMs, infocodes) per programme. It is the breakdown home of the documentation layers (`LC-L`/`LC-M` deliverables, `REV-Lx`/`REV-Mx`): publication REVs are TPuBS items, and their `pinned_source_set` records (`QPLUS-LC-SSOT-PIN-001`) are carried at TPuBS level — making the TPuBS the place where the decoupled documentation layers declare which PBS/design revisions they sit on. It also holds the publication architecture (class `P0`, §2.4), controlled by issue rather than by layer REVs, and may hold experimental instructions (class `P1`) for the articles of `LC-F` and `LC-G`.

```yaml
revisioned_breakdown_structure_rule:
  id: SBS-REV-BREAKDOWN-001
  name: "Revisioned Breakdown Structures Rule"
  rule: >
    Each SBS shall include controlled breakdown structures for product,
    function, work, cost, risk, logistics, evidence, interfaces, requirements,
    technical performance measurement, and technical publications. These
    structures may define generic architecture patterns at SBS level, but
    their authoritative state for a physical product item shall be recorded
    per PBS item revision. Therefore, each PBS revision shall maintain its own
    revision-specific ReqBS, IBS, CBS, RBS, EBS, BOM, CAD, and TPMS records as
    applicable. TPuBS items, being deliverables of the decoupled documentation
    layers, revise on their own layer-local counters and reference the
    applicable PBS revisions through their pinned source sets rather than
    revising in lockstep with the PBS.
```

---

## 12. Requirements Evolution Rule

Requirements shall not be treated as static lifecycle-folder content. They shall be revisioned artefacts linked to the applicable PBS item, product configuration, and lifecycle maturity state.

```yaml
requirements_evolution_rule:
  id: REQBS-REV-001
  name: "Requirements Evolve by Product Revision"
  rule: >
    Requirements shall be controlled as revisioned artefacts linked to the
    applicable PBS item, product configuration, and lifecycle maturity state.
    A change in requirements that affects geometry, interfaces, cost, risk,
    evidence, certification, operations, maintainability, or sustainability
    shall create or update the corresponding REV-X ReqBS and trigger impact
    assessment across IBS, CBS, RBS, EBS, BOM, CAD, TPMS, and PUB artefacts.
    Per QPLUS-LC-DECOUPLE-001, the impact assessment determines per layer
    whether to iterate and re-pin or to record a no-action disposition.
```

Minimum ReqBS class set:

| ReqBS Class | Name |
|---|---|
| `ReqBS-01` | Customer Expectations |
| `ReqBS-02` | Project and Enterprise Constraints |
| `ReqBS-03` | External Constraints |
| `ReqBS-04` | Operational Scenarios |
| `ReqBS-05` | Measures of Effectiveness |
| `ReqBS-06` | System Boundaries |
| `ReqBS-07` | Interfaces |
| `ReqBS-08` | Utilization Environments |
| `ReqBS-09` | Lifecycle Requirements |
| `ReqBS-10` | Functional Requirements |
| `ReqBS-11` | Performance Requirements |
| `ReqBS-12` | Modes of Operation |
| `ReqBS-13` | Technical Performance Measures |
| `ReqBS-14` | Physical Characteristics |
| `ReqBS-15` | Human Systems Integration |

---

## 13. TRL, Upgradeability, and Technology Insertion

Q-plus-A distinguishes technology maturity from deliverable lifecycle maturity.

```text
TRL        = technology maturity            (overlay; see 01-03 Q+ATLANTIDE TRL layer)
LC-letter  = deliverable layer (anchored letter per stage's deliverable set)
REV cycle  = controlled iteration inside a layer (decoupled numbers)
C-GROWTH   = execution method producing iterations and their evidence (§2.3)
```

```yaml
trl_lifecycle_relationship:
  id: QATL-TRL-LC-001
  rule: >
    TRL measures technology maturity. LC-letter layers measure deliverable,
    CAD, integration, and configuration maturity. A technology reaching a
    target TRL does not automatically authorize installation into a product
    baseline. It authorizes the start of a controlled product-specific upgrade
    revision cycle.
```

```yaml
trl_evidence_rule:
  id: QATL-TRL-EVIDENCE-001
  name: "TRL Claims Require Digested Evidence"
  rule: >
    TRL promotion claims shall be backed by accumulated, dispositioned evidence:
    completed C-GROWTH revolutions, closed feedback packages, and met
    correlation thresholds, as recorded in the EBS and TPMS revision packages.
    Where schedule pressure and evidence diverge, the TRL control layer shall
    report the evidence-based maturity state, and the divergence shall be
    recorded in the RBS as a programme risk record.
```

```yaml
technology_insertion_rule:
  id: QATL-TICC-001
  name: "Technology Insertion and Configuration Compatibility"
  rule: >
    Product and architecture designs shall define a baseline configuration
    using technology mature enough for the current lifecycle stage, while
    maintaining controlled compatibility paths for future alternatives with
    higher sustainability, efficiency, maintainability, safety, circularity,
    or performance potential. No future technology shall be inserted into a
    controlled product configuration without TRL assessment, interface
    compatibility assessment, evidence delta analysis, lifecycle insertion
    gate definition, and configuration-control approval.
```

### 13.1 Scoped Maturation Cycles

Products that are to incorporate future technologies do not mature uniformly. One scope — a technology element, component or subsystem, such as an E-pack, a tank or an inverter — may pass several times through concept, design, analysis and test while the rest of the product holds more mature baselines. The model represents this as a **scoped maturation cycle**: a declared, bounded sequence of passes over a subset of layers, with a maturity objective and exit criteria.

A maturation cycle is not a layer and has no REV letter. Its work is done as ordinary revisions of the layers it involves — anchored letters, decoupled numbers, C-GROWTH revolutions executing one layer at a time. The cycle record binds those revisions to an objective and records the exit decision.

```mermaid
flowchart LR
    subgraph MC["Scoped maturation cycle — one scope, e.g. an E-pack"]
        D["Concept, design and analysis<br/>revisions · LC-A … LC-D"] --> T["Development articles and tests<br/>LC-F of the scope · CH active"]
        T --> G{"Exit criteria met?"}
        G -->|"not yet"| D
    end
    G -->|"met"| X["Exit decision recorded<br/>release · insertion · new cycle · stop"]
    G -->|"unattainable or<br/>objective changed"| X
    X -->|"release or insertion"| B["Released product<br/>baseline of the scope"]
    B --> P2["P2 — released operational and<br/>maintenance content · LC-L / LC-M"]
    P0["P0 — publication architecture<br/>from LC-A · no prescriptive content"] -.-> P2
    T -.-> P1["P1 — experimental instructions<br/>article-bound · limit of use"]
```

```yaml
maturation_cycle_rule:
  id: QPLUS-LC-MATCYCLE-001
  name: "Scoped Maturation Cycle Rule"
  rule: >
    A partial lifecycle cycle that repeats over a subset of layers to mature
    one scope shall be declared by a maturation cycle record before its
    first revision, under an identifier allocated through the scope's cycle
    register — unique per scope and never reused. The record names the
    scope, the layers involved, the
    critical technology elements with their entry and target TRL, the
    evidence each target requires under the TRL control layer, the exit
    criteria, and the decision the exit will support. Revisions inside the
    cycle follow the ordinary layer rules (QPLUS-LC-REVLETTER-001,
    QPLUS-LC-DECOUPLE-001, QPLUS-LC-SSOT-PIN-001). Iterating CAD and
    simulation does not raise TRL: from TRL 4 upward, hardware maturity
    requires test evidence on physical articles in the environment the level
    names (QATL-TRL-EVIDENCE-001; Q+A-METHOD-CGROWTH-SPEC-001 §1.5).
    Reaching the target TRL does not by itself demonstrate integration,
    installation compatibility, safety or compliance; each is an exit
    criterion of its own where the decision needs it. A cycle ends only by
    a recorded exit decision: release, insertion, a new cycle with a revised
    objective, or stop.
```

Minimum maturation cycle record:

```yaml
maturation_cycle_record:
  cycle_id: "<SCOPE>-MC-<NN>"                  # e.g. EPACK-MC-01; allocated through the scope's cycle register, never reused
  scope: "<PBS id, part number or Q+ATLANTIDE technology node>"
  branch: "<product baseline | technology maturation | upgrade id per §15>"
  layers_involved: ["LC-A", "LC-B", "LC-D", "LC-F"]
  critical_technology_elements:
    - element: "<technology>"
      qatl_node: "<Q+ATLANTIDE node>"
      trl_entry: "TRL-3"
      trl_target: "TRL-5"
      evidence_required: "<per TRL-evidence-requirements, e.g. test results in a relevant environment>"
      articles: ["<breadboard | brassboard | prototype id>"]
  integration_criteria: []                     # interface, installation and safety evidence the decision needs
  exit_criteria: []                            # measurable, declared before the first pass
  decision_supported: "<scope REV-x_RELEASED | insertion | G5 placement | stop>"
  passes: []                                   # one entry per pass: revisions produced, evidence added, verdict
  exit_decision: {decision: null, date: null, authority: null}
```

Before it reaches its insertion TRL, a future technology matures in cycles scoped to the technology itself (branch `technology maturation`); programme-specific maturity claims carry effectivity, as the TRL control layer requires (`QATL-TRL-PROGRAMME-001`). The upgrade branch of §14–§15 starts only when the target TRL is reached: it pins the maturation evidence as source data, and insertion into a product baseline follows `QATL-TICC-001` and `QATL-UPGRADE-REV-CYCLE-001`. TRL makes a technology eligible; LC/REV maturity makes it installable. Documentation follows its own revisions and pinned sources (§2.1–§2.2): a design iteration inside a maturation cycle triggers a documentation impact assessment, never an automatic manual revision.

### 13.2 Decision-Relative Maturity

Maturity thresholds are not universal; they depend on the decision being authorized. A concept may legitimately be released with immature technology and recorded assumptions; inserting the same technology into a product baseline requires much more.

```yaml
decision_maturity_rule:
  id: QPLUS-LC-DECISION-MATURITY-001
  name: "Decision-Relative Maturity Thresholds"
  rule: >
    Each programme shall declare, per decision, the maturity it requires of
    each critical technology element and of the integration the decision
    depends on. The declaration covers at least: release of a concept
    baseline, release of a preliminary-design baseline, G5 placement of an
    article in CH, insertion into a product baseline, first flight, and
    release of P2 publications. A decision taken below its declared
    threshold requires a waiver recorded by the accountable decision
    authority, stating the deficit, its rationale, the condition that would
    invalidate it, the associated risk record (RBS), and the limits —
    effectivity and duration — within which the decision holds. An
    assumption or an F-DEFER finding documents a deficit; it never waives
    one. A threshold that implements a regulatory requirement cannot be
    waived by the programme. A provisional TRL is never an authorization.
```

| Decision | What it requires (illustrative — each programme declares its own thresholds) |
|---|---|
| `REV-A_RELEASED` of a scope | Concept feasibility; immature elements allowed, with their TRL and assumptions recorded |
| `REV-B_RELEASED` of a scope | Critical technology elements at the programme's preliminary-design threshold, or an approved maturation cycle with a fallback |
| G5 placement of an article | Article configuration identified; test objectives and correlation thresholds declared before execution |
| Insertion into a product baseline | Target TRL reached on evidence; interface compatibility, evidence delta and configuration-control approval (`QATL-TICC-001`) |
| First flight | Flight-clearance evidence for the configuration flown |
| Release of `P2` publications | Released, applicable product sources; procedures verified and validated (§2.4) |

---

## 14. Upgrade Revision-Cycle Restart Rule

When a future upgrade or alternative technology reaches the target TRL required for insertion, it shall not overwrite the existing released baseline. It shall start its own controlled concept baseline.

```yaml
upgrade_revision_cycle_rule:
  id: QATL-UPGRADE-REV-CYCLE-001
  name: "Upgrade Revision Cycle Restart Rule"
  rule: >
    When an alternative technology reaches the target TRL required for product
    insertion, it shall not overwrite the current released baseline. The upgrade
    shall start a new controlled revision cycle from its own concept baseline,
    beginning at LC-A / REV-A0 or an equivalent upgrade-specific concept state.
    The upgrade may only modify or replace the current product baseline after
    interface compatibility, evidence delta, configuration-control approval,
    and lifecycle release gates are satisfied.
```

```text
A technology upgrade becomes eligible through TRL maturity.
It becomes installable only through LC/REV maturity.
It becomes part of the operational baseline only through configuration-control approval.
```

---

## 15. Upgrade Branch Record

```yaml
upgrade_branch_record:
  upgrade_id: "<UPGRADE-ID>"
  upgrade_name: "<upgrade name>"
  parent_product_baseline: "<baseline id>"
  parent_block: "<block id>"
  triggering_condition: "target TRL reached"
  triggering_trl: "TRL-<1..9>"
  starts_at_lifecycle_stage: "LC-A"
  starts_at_revision: "<ITEM>-UPG-<NNN>-REV-A0"
  current_revision: "<ITEM>-UPG-<NNN>-REV-A0"
  next_release_gate: "<ITEM>-UPG-<NNN>-REV-A_RELEASED"
  baseline_relation: "<replacement | modification | optional block upgrade | service bulletin candidate>"
  insertion_allowed_only_after:
    - "interface compatibility approved"
    - "evidence delta closed"
    - "requirements validation completed"
    - "risk assessment accepted"
    - "configuration-control approval"
    - "lifecycle release gate closed"
  operational_baseline_impact: "<none | optional | partial | replacement>"
  status: "<concept | iterating | released | inserted | rejected | superseded>"
```

---

## 16. Evolutionary Acquisition and Baseline Structuring

```text
Core baseline → evolutionary blocks → incremental capability releases → associated product improvements
```

| Characterization | System Level | Programme Level | Documentation Required | Baseline | CM Authority |
|---|---|---|---|---|---|
| Overall Need | Major Programme / Portfolio / Business Area | Capstone or Sub-Portfolio | Capstone Acquisition Documentation | Top-Level Functional Baseline | PMO |
| Core and Evolutionary Blocks | Build or Block of Major Programme | Acquisition Programme | Full Programme Documentation | Cumulative Functional and Allocated Baseline | PMO with Contractor Support |
| Incremental Delivery of Capability | Release or Version of Block | Internal to Acquisition Programme | Separate Acquisition Documentation not required unless required by programme rules | Product Baseline | Contractor / Delivery Authority; must meet Allocated Baseline |
| Associated Product Improvements | Application, Bridge, Upgrade Branch, or Product Improvement | Parallel Product Improvement / Technology Insertion Candidate | Component-Level or Lower-Decision-Level Processing | Functional, Allocated, and Product Baselines | PMO / Contractor / Responsible Q-Division |

```yaml
evolutionary_acquisition_rule:
  id: QATL-EVO-ACQ-001
  name: "Evolutionary Acquisition and Baseline Structuring Rule"
  rule: >
    Programmes shall define an operationally suitable core baseline and identify
    the subsystems, components, technologies, interfaces, and documentation sets
    most likely to evolve. Evolutionary blocks, incremental capability releases,
    and associated product improvements shall be planned through controlled
    baselines, TRL assessment, evidence records, configuration-management
    authority, and lifecycle gates.
```

---

## 17. Open Architecture Upgrade Rule

```yaml
open_architecture_upgrade_rule:
  id: QATL-OPEN-ARCH-UPGRADE-001
  rule: >
    The core system architecture shall emphasize openness, modularity,
    functional partitioning, stable interfaces, and open-system design so that
    future upgrades can be inserted through controlled modification rather than
    uncontrolled redesign wherever technically and economically feasible.
```

```yaml
baseline_hierarchy_rule:
  id: QATL-BASELINE-HIERARCHY-001
  rule: >
    Q+ATLANTIDE and programme baselines shall distinguish top-level functional
    baselines, allocated baselines, product baselines, and upgrade branch
    baselines. Incremental capability releases shall meet the allocated baseline.
    Upgrade branches shall not overwrite released product baselines until
    configuration approval and lifecycle release gates are satisfied.
```

---

## 18. Example — AMPEL360 eWTW Radome

```text
eWTW-PBS-10-10-10-10-10 — Radome
```

```yaml
radome_lifecycle_example:
  pbs_id: "eWTW-PBS-10-10-10-10-10"
  part_number: "PN-eWTW-5310-0001"
  lc_layer: "LC-A"
  lc_layer_name: "Conceptual Design"
  current_revision: "RADOME-REV-A1"
  revision_status: "iterating"
  next_release_gate: "RADOME-REV-A_RELEASED"
  next_revision: "RADOME-REV-A2"
  cgrowth_conformance: "CT-bounded"   # no physical article yet; G5/G6 planned at LC-F
```

Current revision-specific breakdown package:

```yaml
radome_rev_a1_breakdown_package:
  pbs_revision: "RADOME-REV-A1"
  reqbs: "01_REQUIREMENTS/REV-A1/ReqBS-RADOME-REV-A1.md"
  ibs: "02_INTERFACES/REV-A1/IBS-RADOME-REV-A1.md"
  cbs: "03_COST/REV-A1/CBS-RADOME-REV-A1.md"
  rbs: "04_RISK/REV-A1/RBS-RADOME-REV-A1.md"
  ebs: "05_EVIDENCE/REV-A1/EBS-RADOME-REV-A1.md"
  cad: "LC-A_Concept-Design/REV-A1/FreeCAD/"
  pub_040: "pub/040_descriptive/"
  pub_258: "pub/258_bonding-and-lightning-check/"
```

Known REV-A1 gate findings:

| Finding | Class | Meaning | Gate Impact |
|---|---|---|---|
| `F1` | `F-BLOCK` | Absolute scale must be verified or closed. | Blocks `RADOME-REV-A_RELEASED`. |
| `F2` | `F-DEFER` | Solid body only; sandwich wall deferred. | Becomes mandatory at LC-C. |
| `F3` | `F-BLOCK` | Controlled metadata must be completed. | Blocks `RADOME-REV-A_RELEASED`. |
| `F4` | `F-WARN` | ReqBS exists; IBS/CBS/RBS/EBS/TPMS revision packages pending. | Blocks full configuration release if not completed or explicitly deferred. |

### 18.1 Decoupled-Iteration Example (illustrative, future state)

Once the radome programme is in service, the layers iterate independently under pinning:

```yaml
# Design layer iterates; documentation does not (automatically) follow:
radome_design_iteration:
  lc_layer: "LC-C"
  current_revision: "RADOME-REV-C3"
  revision_status: "iterating"
  note: >
    REV-C3 in work. Per QPLUS-LC-DECOUPLE-001 this does not create REV-Lx or
    REV-Mx iterations. Documentation layers assess impact only at C3 release.

# Documentation layer iterates without any design change:
radome_amm_iteration:
  lc_layer: "LC-M"
  deliverable: "AMM radome subject-node DMs and infocodes"
  current_revision: "AMM-RADOME-REV-M5"
  iteration_driver: "service-bulletin"
  pinned_source_set:
    - artefact: "RADOME design baseline"
      pinned_revision: "RADOME-REV-C2_RELEASED"
      pin_status: "unchanged"
  note: >
    M5 driven by SB-eWTW-5310-002 procedure change; design SSOT unchanged;
    pin re-validated and restated per QPLUS-LC-SSOT-PIN-001.
```

Example upgrade candidate:

```yaml
radome_upgrade_candidate_example:
  upgrade_id: "RADOME-UPG-001"
  upgrade_name: "Recyclable Low-Loss Dielectric Core"
  baseline_configuration: "RADOME-CONF-A"
  baseline_technology: "Conventional RF-transparent sandwich laminate"
  qatl_reference: "AMTA material node TBD (material maturity owned by AMTA); ATLAS 050-059 integration, node TBC"
  current_trl: "TRL-5"
  target_trl_for_insertion: "TRL-6"
  decision_status: "watched"
  expected_benefit:
    sustainability: "high"
    efficiency: "medium"
    circularity: "high"
    weight_reduction: "medium"
    maintainability: "medium"
    safety: "medium"
  compatibility_constraints:
    - "radome backup mechanical interface"
    - "RF transparency"
    - "bird-strike resistance"
    - "lightning diverter compatibility"
    - "moisture ingress resistance"
    - "certification basis"
  upgrade_revision_cycle:
    trigger: "target TRL reached"
    starts_at: "LC-A / RADOME-UPG-001-REV-A0"
    next_release_gate: "RADOME-UPG-001-REV-A_RELEASED"
    baseline_relation: "candidate replacement or modification to RADOME-CONF-A"
```

---

## 19. Governance Rules

1. The lifecycle model shall use LC-letter layers from `LC-A` through `LC-N`.
2. The REV letter is anchored to the deliverable's owning layer and shall never change; only the iteration number advances (`QPLUS-LC-REVLETTER-001`).
3. Iteration numbers are decoupled across layers; cross-layer propagation occurs only through impact assessment (`QPLUS-LC-DECOUPLE-001`).
4. Every downstream deliverable REV shall carry a valid pinned source set in its SSOT stack (`QPLUS-LC-SSOT-PIN-001`).
5. A layer's deliverable baseline shall be released only through its `*_RELEASED` gate; first initialization of the next layer requires the upstream release, but already-initialized layers iterate independently (`QPLUS-LC-RELEASE-001`).
6. Blocking findings (`F-BLOCK`) shall prevent release-gate closure of the owning layer.
7. Deferred findings (`F-DEFER`) shall identify the layer and condition where they become mandatory.
8. Lifecycle records shall preserve PBS, PN, CAD, evidence, release-gate, and pinned-source traceability.
9. Product-specific lifecycle folders may extend this model but shall not contradict it.
10. Each SBS shall define the controlled breakdown family for PBS, FBS, WBS, CBS, RBS, LBS, EBS, IBS, ReqBS, TPMS, and TPuBS.
11. Each PBS revision shall maintain its own revision-specific breakdown records where applicable.
12. Requirements shall evolve by product revision and shall not be stored only as static LC-folder content.
13. TRL maturity shall not be treated as product installation maturity.
14. A mature upgrade shall start its own LC/REV concept baseline before insertion.
15. Upgrade branches shall not overwrite released product baselines without configuration-control approval.
16. The root `02_LIFECYCLE_MODEL/README.md` is the controlling lifecycle reference for Q-plus-A unless superseded by a higher governance document.
17. C-GROWTH (`Q+A-METHOD-CGROWTH-SPEC-001`) is the controlled execution method; every revolution executes within exactly one layer, its gate records (G1–G6) attach to that layer's REV, and G-gates never substitute for `*_RELEASED` gates (`QPLUS-LC-CGROWTH-001`).
18. Every layer may initiate C-GROWTH revolutions and work packages from layer-local inputs, independent of upstream or downstream activity (`QPLUS-LC-CG-INIT-001`).
19. C-GROWTH conformance while no physical article exists shall be declared CT-bounded, with G5/G6 activation planned at the first physical article of each scope (default: `LC-F` deliverables; `QPLUS-LC-ARTICLE-SCOPE-001`).
20. TRL promotion claims shall be evidence-based per `QATL-TRL-EVIDENCE-001`; schedule–evidence divergence shall be recorded in the RBS.
21. A partial cycle that repeats over a subset of layers to mature one scope shall be declared by a maturation cycle record — with an identifier unique per scope, scope, layers, entry and target TRL, required evidence, exit criteria — and shall end only by a recorded exit decision (`QPLUS-LC-MATCYCLE-001`).
22. Maturity thresholds shall be declared per decision. A decision below its threshold requires a waiver recorded by the accountable decision authority; assumptions and `F-DEFER` findings document deficits but never waive them; regulatory thresholds cannot be waived by the programme; a provisional TRL never authorizes (`QPLUS-LC-DECISION-MATURITY-001`).
23. Physical-article availability shall be declared per scope; development articles of a maturation cycle are `LC-F` deliverables of that scope, initialized on their own controlled path rather than after an `LC-E` release (`QPLUS-LC-ARTICLE-SCOPE-001`).
24. Every technical publication shall declare a content class. `P1` instructions are verified, and their procedures validated, before use; `P2` content is verified in full and its procedures validated before release (`QPLUS-LC-PUBCLASS-001`).
25. Ages are kept per baseline scope and effectivity. Only the integrated baseline of a scope opens an age; at most one baseline is canonical per scope and effectivity; ratifications are serialized; the first ratification is the scope's genesis (`QPLUS-LC-AGE-001`).
26. Evolutionary memory shall remain verifiable and usable: superseded baselines reconstructable, final statuses of candidates kept, negative results retained, corrections superseding and never overwriting, ratification records never erased; content that may not be republished is retained by reference and hash (`QPLUS-LC-MEMORY-001`).

---

## 20. Controlled Closure Statement

`02_LIFECYCLE_MODEL/README.md` defines the root lifecycle maturity model for Q-plus-A artefacts, on a single LC-letter axis of **deliverable layers** with anchored REV letters and decoupled iteration numbers.

Version `0.6.0` additionally controls the relationship between:

```text
LC-letter deliverable layers (anchored REV letters)
REV-controlled configuration states (decoupled iteration numbers)
SSOT source-data pinning (the sole cross-layer coupling mechanism)
C-GROWTH per-layer execution (revolutions, gates G1–G6, feedback-package routing)
SBS breakdown families (including TPuBS for technical publications)
PBS revision-specific engineering truth
ReqBS / IBS / CBS / RBS / EBS / TPMS revision packages
TPuBS publication items (layer-local REVs, pinned to PBS/design sources)
TRL maturity (orthogonal overlay; evidence-based promotion)
upgradeability
evolutionary acquisition blocks
upgrade branch baselines
```

Version `0.7.0` adds:

```text
scoped maturation cycles (partial cycles over a subset of layers, per scope, to a maturity objective)
decision-relative maturity thresholds
physical-article availability per scope (development articles as LC-F deliverables)
publication content classes P0 / P1 / P2 and their gates
ages bounded by ratified baselines, and evolutionary memory (AGES binding)
```

It shall be referenced by product-specific lifecycle records such as:

```text
LC-A_Concept-Design/REV-A1/FreeCAD/Radome-CAD-Record.md
01_REQUIREMENTS/REV-A1/ReqBS-RADOME-REV-A1.md
```

Companion controlled document in this folder:

```text
02_LIFECYCLE_MODEL/C-GROWTH-METHOD-SPEC.md   (Q+A-METHOD-CGROWTH-SPEC-001)
```

---

## Revision history

| Version | Date | Change |
|---|---|---|
| `0.1.0` | 2026-05-30 | Initial root lifecycle model. |
| `0.2.0` | 2026-05-31 | (Branch) two-axis orthogonality + revision_status enum + naming reconciliations. |
| `0.3.0` | 2026-05-31 | Removed the two-axis distinction and all LC01–LC14 references. Single LC-letter lifecycle. |
| `0.4.0` | 2026-05-31 | Major extension (renumbered from the shared 0.2.0/A1 draft to keep versioning monotonic above 0.3.0): TRL integration (§13), technology insertion & upgrade revision-cycle rules (§13–§15), evolutionary acquisition & open-architecture baselines (§16–§17), SBS breakdown families & revisioned breakdown structures (§11), requirements evolution & ReqBS classes (§12). Single LC-letter axis retained; TRL is the only orthogonal overlay. §3↔§7 naming aligned (PMA / Wind Tunnel / Software Embodiment). |
| `0.5.0` | 2026-06-11 | C-GROWTH binding (rev E): bound `Q+A-METHOD-CGROWTH-SPEC-001` as the controlled intra-stage execution method; gate family separation (G1–G6 vs `*_RELEASED`); CH availability mapped per LC stage; findings coupling; `cgrowth_execution_record` metadata; `QATL-TRL-EVIDENCE-001`. |
| `0.6.0` | 2026-06-11 | **Critical structural correction (rev F)**: LC stages redefined as deliverable layers with anchored REV letters (`QPLUS-LC-REVLETTER-001`); iteration numbers decoupled across layers (`QPLUS-LC-DECOUPLE-001`) — a REV-C3 design iteration does not force REV-Lx/REV-Mx documentation iterations, and documentation may iterate (service bulletins, structure improvements) with design SSOT unchanged; SSOT source-data pinning made the sole cross-layer coupling mechanism (`QPLUS-LC-SSOT-PIN-001`, `pinned_source_set` metadata); release gate rule reframed (first initialization sequential, thereafter independent iteration); every layer may initiate C-GROWTH revolutions and work packages from layer-local inputs (`QPLUS-LC-CG-INIT-001`); feedback-package routing across layers defined; decoupled-iteration radome example added (§18.1); governance rules renumbered and extended (1–20). |
| `0.6.1` | 2026-06-11 | TPuBS added to the SBS breakdown family (rev G): `TPuBS_Technical-Publications-Breakdown-Structure` registered in §11 as the breakdown home of the documentation layers (`REV-Lx`/`REV-Mx` publication items: PMCs, subject nodes, DMs, infocodes); TPuBS items revise on layer-local counters and carry their `pinned_source_set` records at TPuBS level per `QPLUS-LC-SSOT-PIN-001`; `SBS-REV-BREAKDOWN-001` extended accordingly (replacing the informal "publication references" wording); governance rule 10 and closure statement updated. |
| `0.7.0` | 2026-10-12 | Partial maturation cycles (rev H): scoped maturation cycles over a subset of layers with entry and target TRL, required evidence, exit criteria and a recorded exit decision (§13.1, `QPLUS-LC-MATCYCLE-001`, `maturation_cycle_record`); decision-relative maturity thresholds (§13.2, `QPLUS-LC-DECISION-MATURITY-001`); physical-article availability declared per scope, with development articles as `LC-F` deliverables (§2.3, §3, `QPLUS-LC-ARTICLE-SCOPE-001`); publication content classes `P0` architecture / `P1` experimental instructions / `P2` released content, with the `P2` gate placed before operational use rather than at TRL 9 (§2.4, `QPLUS-LC-PUBCLASS-001`); AGES binding (§2.5): ages bounded by ratified baselines (`QPLUS-LC-AGE-001`) and evolutionary memory (`QPLUS-LC-MEMORY-001`), with the repository as an AGES underlying record system and a correspondence table to AGES concepts; §2.1 and §11 aligned; governance rule 19 amended and 21–26 added. Incorporates the review of PR #62: waivers for below-threshold decisions; verification of all `P1` and `P2` content; a controlled `LC-F` initialization path for development articles; genesis, serialized ratification and integrated baselines as the only age openers, per scope and effectivity; technology-scoped maturation before the upgrade branch; unique cycle identifiers; content classes limited to technical publications. No section renumbered. |
