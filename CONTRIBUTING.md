# Contributing to Q+A

Q+A is a governed engineering architecture repository. All contributions must follow the processes described in this document and in the root [`README.md`](README.md).

---

## Join a Q+A division

Before taking responsibility for a controlled part number, assembly, simulation, data module, publication node or other formal work package, a contributor must register in at least one Q+A technical or enterprise division.

Division registration establishes the contributor's declared competence domain and organizational interface. It does not automatically authorize modifications to the repository architecture.

A contributor may request membership in more than one division when justified by their competencies and intended work.

### Membership request process

Open a GitHub issue with the title:

```text
[DIVISION MEMBERSHIP] <GitHub username> — <division code and name>
```

The issue must contain:

```markdown
## Applicant

GitHub username:
Public display name:

## Requested division

Division code:
Division name:
Technical or enterprise group:

## Proposed role

Member / contributor / reviewer / steward / coordinator / advisor:

## Competencies

Describe the relevant engineering, scientific, publication, software,
governance or enterprise competencies.

## Intended contribution areas

Identify the product nodes, technologies, publications, simulations,
programmes or organizational activities of interest.

## Public profile or evidence

Optional links to public repositories, publications, portfolios,
professional profiles or previous work.

## Declaration

I confirm that I will not contribute employer-confidential,
export-controlled, classified, proprietary or unlawfully obtained material.
```

Membership must be approved by the repository owner and architecture authority, **Amedeo Pelliccia** (`@AmedeoPelliccia`), before the contributor is added to [`TEAM-MEMBERS.csv`](01_OPTIONS_ARCHITECTURE/01-01_ORGANIZATIONS/TEAM-MEMBERS.csv).

After approval:

1. assign the next stable `member_id`;
2. add the approved row to `TEAM-MEMBERS.csv`;
3. update the human-readable `TEAM-MEMBERS.md`;
4. reference the approval issue;
5. set the initial status to `APPROVED` or `ACTIVE`.

A contributor may not add themselves directly to the registry without an approved membership issue.

### Relationship between membership and work packages

Division membership and work-package allocation are separate governance actions:

```text
division membership
        ↓
declared competence and organizational affiliation
        ↓
work-package proposal
        ↓
architectural allocation approval
        ↓
engineering stewardship
        ↓
pull request and technical review
```

Being registered as a team member does not automatically assign a part number or engineering node.

Each CAD model, assembly, simulation, data module, ICN, evidence package or other controlled contribution still requires an approved work-package issue.

The repository owner may approve a first membership request and a first work-package request within the same issue when both scopes are clearly described.

---

## Work-package allocation process

Before starting any controlled engineering contribution, open a `[WORK PACKAGE]` issue proposing:

* the specific controlled node, part number or architecture element;
* the type of artefact (CAD model, simulation, data module, evidence, etc.);
* the intended maturity level;
* the contributor's declared division membership.

Work begins only after the architecture authority approves the allocation.

---

## Pull request process

1. Reference the approved work-package issue in the pull request.
2. Place artefacts under the controlled directory corresponding to the approved node.
3. Include required metadata (status, maturity, assumptions, sources).
4. Do not modify unrelated architecture, part-number spaces or controlled structures.
5. The architecture authority reviews and merges governed contributions.

---

## What must not be contributed

Do not upload:

* employer-confidential information;
* export-controlled technical data;
* classified or restricted information;
* copyrighted CAD or documents without redistribution rights;
* personal data;
* results presented as validated when they are not;
* files whose origin or permissions cannot be established.

---

## Engineering maturity declaration

Every contribution must declare its maturity status:

```text
CONCEPT · PLANNED · DRAFT · IN-WORK · REVIEWED · VERIFIED · VALIDATED · RELEASED · SUPERSEDED
```

---

## Division registry

- [Technical Divisions](01_OPTIONS_ARCHITECTURE/01-01_ORGANIZATIONS/01-01-01_TECHNICAL-DIVISIONS/)
- [Enterprise Divisions](01_OPTIONS_ARCHITECTURE/01-01_ORGANIZATIONS/01-01-02_ENTERPRISE-DIVISIONS/)
- [Team member registry](01_OPTIONS_ARCHITECTURE/01-01_ORGANIZATIONS/TEAM-MEMBERS.md)
