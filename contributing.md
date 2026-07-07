# Contributing to Q+A

Thank you for your interest in contributing to **Q+A**, the collaborative engineering repository supporting the Q+ initiative, Q+ATLANTIDE, OPTIONS and the AMPEL360, GAIA-AIR, GAIA-SPACE and ROBBBO-T programme architectures.

Q+A is a **governed engineering address space**. Every contribution must be connected to an approved programme, system, product, part number, publication node, interface or evidence node. Contributors must not create independent parallel structures or place engineering artefacts in arbitrary directories.

> [!IMPORTANT]
> **The core rule in one line:** propose the object and its controlled location through an issue **before** doing the work; once the allocation is approved by the architecture authority, you become the engineering steward of that work package.

---

## 1. Core contribution rule

Before beginning a substantial engineering contribution, open a GitHub issue proposing:

1. the engineering object or question to be addressed;
2. the controlled node, part number or publication node involved;
3. the type of work to be performed;
4. the proposed repository location for the resulting artefacts;
5. the expected deliverables;
6. the assumptions, tools and methods to be used.

The proposed allocation must be reviewed and approved by the **architecture authority** — the repository owner, **Amedeo Pelliccia (AM.PEL)**, assisted by delegated reviewers as the contributor base grows — before the contribution is considered formally assigned.

Approval establishes the authorized repository location and prevents duplicated work, conflicting models, parallel part-number structures, uncontrolled publication branches, misplaced evidence and broken configuration traceability.

No contributor may unilaterally redefine the PBS, the TPuBS, the part-number grammar, the publication structure or the architectural ownership rules.

---

## 2. Contribution stewardship

A contributor may propose to take responsibility for one or more controlled engineering objects:

* a part number, assembly, subassembly or LH/RH variant;
* a structural or systems installation;
* a CAD model or engineering drawing;
* a simulation model or calculation package;
* an interface definition;
* an S1000D data module, illustration (ICN) or publication node;
* an evidence package;
* an unresolved engineering question.

Once approved, the contributor becomes the temporary **engineering steward** of the accepted work package.

Stewardship means responsibility for developing and documenting the contribution. It does **not** transfer ownership of the controlled identifier, nor authority to modify the surrounding architecture. A controlled part number remains part of the Q+A configuration architecture.

---

## 3. Issue-first allocation process

Every work package begins with an issue.

**Recommended title:**

```text
[WORK PACKAGE] <controlled node or part number> — <short contribution title>
```

**Examples** (G-ATLAS-coherent addresses):

```text
[WORK PACKAGE] EWTW-538001-010 — Forward pressure bulkhead web CAD model
[WORK PACKAGE] eWTW-PBS-053-200-020 — Wing-to-fuselage fairing surface model
[WORK PACKAGE] 021-200-010 — ECS duct pressure-loss simulation
[WORK PACKAGE] DMC EWTW-A-53-80-01-00A-040A-D — Forward pressure bulkhead descriptive DM
```

**Required issue content:**

```markdown
## Contributor
Name or GitHub username:

## Controlled engineering object
Programme:
Model:
Breakdown structure:
Node:
Part number or publication identifier:

## Proposed contribution
CAD / assembly / drawing / simulation / calculation / interface /
data module / ICN / evidence / other:

## Engineering objective
The question to be answered or the product definition to be created.

## Proposed repository location
Complete proposed path.

## Planned deliverables
Source files, neutral exports, reports, data, drawings, metadata.

## Tools and versions
CAD, CAE, solver, scripting or publication tools.

## Inputs and assumptions
Source geometry, requirements, materials, loads, interfaces, assumptions.

## Dependencies
Parent assemblies, adjacent systems, related publications, required inputs.

## Expected maturity
CONCEPT / PLANNED / DRAFT / IN-WORK / REVIEWED / VERIFIED / VALIDATED

## Licensing and provenance
Confirm the work can legally be shared and contains no restricted material.
```

---

## 4. Approval states

```text
PROPOSED · NEEDS-CLARIFICATION · APPROVED · ASSIGNED · IN-WORK ·
SUBMITTED · UNDER-REVIEW · ACCEPTED · CHANGES-REQUESTED · ON-HOLD · CLOSED
```

Work is not formally allocated until the issue is marked **APPROVED** or **ASSIGNED** by the architecture authority. An approval may define the authoritative node, the accepted path, identifier constraints, expected formats, interface boundaries, required metadata, review checkpoints, dependency conditions and maturity limitations.

---

## 5. Repository placement

The contributor proposes where the work should live; the final location follows the engineering nature and ownership of the artefact.

### Product definition (PBS)

Physical product artefacts belong under the relevant PBS part-number node, **alongside** its controlled files (`part.yaml`, registers, README — never renamed or moved):

```text
<PBS part-number node>/
├── part.yaml            (controlled — folder name is SSOT)
├── CAD/
│   ├── SOURCE/
│   ├── STEP/
│   ├── MESH/
│   └── PREVIEW/
├── DRAWINGS/
├── ANALYSIS/
├── SIMULATION/
├── INTERFACES/
└── EVIDENCE/
```

### Technical publications (TPuBS — information-centric)

Publication artefacts belong under the owning **information node** in `01_INFORMATION-ARCHITECTURE`:

```text
<G-ATLAS information node>/
├── DMRL-<node>.yaml     (node SSOT: required DMs, publicationTargets, ICN links)
├── DM/                  (S1000D data modules)
└── ICN/
    ├── source/          (publication-neutral vector masters)
    ├── metadata/        (governance sidecars)
    └── renditions/      (generated; publication-stamped; never canonical)
```

Publication Modules (`PMC-*`) are **editorial projections** living in `02_PUBLICATION-MODULES/` — they reference data modules, they never own content, and there is no per-node `PMC/` folder. ICN masters are publication-neutral: publication banners are stamped only at rendition time by the governance stamper. Reverse-pointer registers (`usedBy`, cross-section aggregations) are **derived, never authored**.

### Simulation and evidence

Simulation source models remain under the owning PBS or systems node; verification evidence may additionally be referenced from the EBS. A simulation package must not be separated from the engineering object it evaluates.

### Interfaces and functional work

Interface definitions are allocated to the relevant IBS node or linked from the owning product nodes; functional models and allocations connect to FBS nodes. The same artefact may be referenced by multiple controlled views, but it has **one** authoritative owner.

---

## 6. Part-number work packages

A contributor may request assignment of an existing controlled part number, specifying whether the work concerns product definition, conceptual or detailed geometry, assembly or constituent definition, LH/RH variants, installation, structural/thermal/fluid/electrical analysis, manufacturing definition, maintenance information, technical publication or evidence.

The contributor must use the existing identifier **exactly as defined**. Identifier grammar is controlled by `AMPEL360-PBS-PN-CM-001` (`EWTW-<CSN>-<item>`: items ×10, children `+1..+9` as LH/RH variants or constituents) and, for publications, by `AMPEL360-DMC-ID-001`.

**Not permitted without prior architectural approval:**

* inventing or changing a part number;
* renaming an authoritative folder or moving a controlled node;
* creating an alternative numbering grammar;
* duplicating a component in another PBS location;
* converting a planned item into an assembly without review;
* using `AAA` in any identifier, folder, code or taxonomy element (**No-AAA rule** — absolute).

Where a new identifier is genuinely necessary, it must be proposed in the issue and approved before use.

---

## 7. CAD contributions

Include, where applicable: authoritative source model; neutral **STEP** export; preview image; units; coordinate system; origin and reference planes; principal dimensions; materials; interfaces; parent assembly; design assumptions; known limitations; software and version; revision; contributor identification.

A CAD model must state its definition level:

```text
CONCEPTUAL · ENVELOPE · PARAMETRIC · PRELIMINARY-DESIGN · DETAILED-DESIGN · MANUFACTURING-DEFINITION
```

Visual plausibility alone is not sufficient to claim engineering validity.

---

## 8. Assembly contributions

Identify: top assembly; included part numbers; parent–child relationships; mating and interface conditions; coordinate systems; degrees of freedom; clearances; attachment concepts; installation sequence; excluded components; unresolved interfaces.

Assembly models must not silently introduce unregistered parts. New constituents discovered during assembly development must be proposed through the approved issue.

---

## 9. Simulation contributions

Identify: engineering question; owning node; geometry source; simplifications; material properties; boundary and initial conditions; load cases; solver and version; numerical method; mesh or discretization; convergence criteria; input and result files; interpretation; uncertainty; limitations; reproduction instructions.

Keep the epistemic distinction explicit throughout:

```text
known · assumed · calculated · simulated · estimated · inferred · unresolved
```

A screenshot or result plot without model inputs and assumptions is not sufficient evidence.

---

## 10. Data-module contributions

Identify: owning TPuBS information node; related PBS or system node; data-module type and information code; applicability; preliminary DMC; source engineering data; required illustrations (ICN); BREX or business-rule assumptions; publication target (`publicationTargets` in the node DMRL); expected validation level.

The DMC and final CSDB location must be approved before the data module is treated as authoritative. A data module must not create a second product definition independent of the PBS: **the publication describes, supports or evidences the controlled product — it does not redefine it.**

---

## 11. Pull requests

After approval, create a branch and submit a pull request referencing the approved issue (`Closes #<issue-number>`).

The PR description should include: the approved work-package identifier; the controlled node or part number; the authoritative location; a summary of completed work; files added or modified; assumptions; verification performed; unresolved points; software dependencies; maturity status; recommended next step.

Pull requests submitted without a prior approved issue may be closed, redirected or reorganized.

---

## 12. Review authority

The architecture authority retains final decision over architectural allocation, identifier assignment, directory ownership, PBS and TPuBS structure, part-number grammar, publication placement, cross-view traceability and acceptance into the main branch. Technical contributors may review discipline-specific content; architectural approval remains separate from engineering verification.

Approval of a work package does **not** mean that the design is certified, the analysis validated, the component airworthy, the result production-ready, or the work approved by any aviation authority — and it does not transfer professional liability to the repository owner.

---

## 13. Reassignment and inactivity

An approved work package may be placed **ON-HOLD** or reassigned when progress stalls for an extended period, the contributor withdraws, dependencies change, the architecture is revised, duplicate work is discovered, or the agreed scope is no longer followed.

Contributors should update the issue periodically with status, completed outputs, blockers, changed assumptions and the expected next action. Stewardship is maintained through visible engineering progress and traceability.

---

## 14. Collaboration between contributors

Multiple contributors may work on the same controlled object when their scopes are distinct:

```text
Contributor A — CAD product definition
Contributor B — structural simulation
Contributor C — thermal analysis
Contributor D — S1000D descriptive data module
Contributor E — technical illustration (ICN)
```

Each contribution references the same authoritative node while keeping its own approved work package. Conflicting definitions are resolved through the issue and architecture review process, never through parallel implementations.

---

## 15. Restricted and prohibited material

Do not contribute: employer-confidential information; proprietary Airbus, supplier or customer data; export-controlled technical data; classified or restricted information; copyrighted CAD models without redistribution rights; leaked documentation; personal data; unlicensed third-party assets; unverifiable copied calculations; results falsely presented as validated.

Contributors must confirm in the allocation issue that they are authorized to publish their work.

---

## 16. Licensing (interim)

A repository-wide `LICENSE` and formal contributor terms are pending. Until they are published:

* contributors retain copyright in their contributions;
* by submitting a pull request, contributors grant the project the non-exclusive right to host, display and integrate the contribution within the repository's governed structures;
* no broader reuse rights are granted or implied in either direction;
* the licensing terms adopted later will be proposed to existing contributors, not imposed retroactively.

Identify the licensing status of any externally sourced material and contribute only work you are authorized to share.

---

## 17. Contribution principle

The repository already provides controlled engineering addresses. A contributor's task is not to upload a file, but to populate an approved address with traceable engineering content.

> **Propose the object, propose the location, obtain architectural approval, perform the work, preserve the evidence, and submit the result for review.**

This process ensures that CAD models, assemblies, simulations, publications and evidence evolve as parts of one governed aerospace data ecosystem.
