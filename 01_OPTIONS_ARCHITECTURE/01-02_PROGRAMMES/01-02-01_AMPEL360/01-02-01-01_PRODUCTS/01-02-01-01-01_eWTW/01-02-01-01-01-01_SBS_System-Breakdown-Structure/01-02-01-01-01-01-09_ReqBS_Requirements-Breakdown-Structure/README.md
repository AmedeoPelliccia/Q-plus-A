---
status: draft
standard_scope: governance
---

# eWTW — Requirements Breakdown Structure (ReqBS)

**Product:** AMPEL360 · eWTW — regional electric Wide Tube and Wing
**Sibling of:** `01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/` … `…-08_IBS_Interface-and-Installation-Breakdown-Structure/`
**Location:** `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_PRODUCTS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-09_ReqBS_Requirements-Breakdown-Structure/`

---

## Purpose

The ReqBS controls **requirements** as dedicated, governed records inside the SBS. It exists so that requirements are not treated as static lifecycle-folder content. The SBS owns the *breakdown family* and may define a **generic requirements taxonomy** here; the **authoritative requirement state for a physical product item is recorded per PBS item revision** (`REV-X`), not inside this folder and not inside the LC maturity folders.

> Requirements are **revisioned artefacts** linked to each product baseline — they evolve across revisions and may branch with product configuration.

---

## Key architectural decision

```text
LC folders control lifecycle maturity.
REV folders control configuration state.
Breakdown structures control the engineering truth of each configuration.
```

So the hierarchy is:

```text
SBS    = framework of breakdowns
PBS    = physical item decomposition
REV-X  = configuration state
ReqBS / CBS / RBS / IBS / EBS = revision-specific engineering truth
LC-A/B/C = maturity gate of that revision
```

For each controlled product item:

```text
PBS item + REV-X = configuration-specific truth package
```

---

## What lives where

| Concern | Lives in | Carries |
|---|---|---|
| Generic requirements taxonomy and architecture-level requirement patterns | **ReqBS** (this structure) | Controlled `ReqBS-01..15` classes · governance rules |
| Authoritative requirement state for a physical item | **PBS item `REV-X`** | `ReqBS-<ITEM>-REV-X.yaml` + `.md` baseline |
| Lifecycle maturity gate of a revision | **LC-A/B/C** | maturity status only — not the requirement truth |

The decision rule:

```text
If it is the generic requirement taxonomy / pattern → it may live at SBS level (this folder).
If it is the authoritative requirement state of a physical item → it lives under the PBS item revision (REV-X), as ReqBS-<ITEM>-REV-X.
```

The PBS revision package keeps **breakdown type first, then revision**, for GitHub readability:

```text
eWTW-PBS-10-10-10-10-10_Radome/
└── 01_REQUIREMENTS/
    └── REV-A1/
        ├── ReqBS-RADOME-REV-A1.yaml
        └── ReqBS-RADOME-REV-A1.md
```

---

## Controlled ReqBS taxonomy

Each PBS item revision records its requirements under the following controlled classes:

| Class | Name |
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

`ReqBS-13 Technical Performance Measures` is the requirement-side entry point of the Technical Performance Measurement Structure (`…-10_TPMS`); TPM targets and tracking are controlled there.

---

## Formal rules

```yaml
revisioned_breakdown_structure_rule:
  id: SBS-REV-BREAKDOWN-001
  name: "Revisioned Breakdown Structures Rule"
  rule: >
    Each SBS shall include controlled breakdown structures for product,
    function, work, cost, risk, logistics, evidence, interfaces, requirements,
    and technical performance measurement. These structures may define generic
    architecture patterns at SBS level, but their authoritative state for a
    physical product item shall be recorded per PBS item revision. Therefore,
    each PBS revision shall maintain its own revision-specific ReqBS, IBS, CBS,
    RBS, EBS, BOM, CAD, and publication references as applicable.
```

```yaml
requirements_evolution_rule:
  id: REQBS-REV-001
  name: "Requirements Evolve by Product Revision"
  rule: >
    Requirements shall not be treated as static lifecycle-folder content.
    Requirements shall be controlled as revisioned artefacts linked to the
    applicable PBS item, product configuration, and lifecycle maturity state.
    A change in requirements that affects geometry, interfaces, cost, risk,
    evidence, certification, or operations shall create or update the
    corresponding REV-X ReqBS and trigger impact assessment across IBS, CBS,
    RBS, EBS, BOM, CAD, and PUB artefacts.
```

---

## Worked example — Radome

The first controlled requirements baseline for the radome conceptual CAD state (`RADOME-REV-A1`, `LC-A`) is recorded under the PBS item revision, not here:

```text
01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/
└── eWTW-PBS-00_Aircraft-Product/.../eWTW-PBS-10-10-10-10_Nose-Structure-and-Radome-Backup/
    └── eWTW-PBS-10-10-10-10-10_Radome/
        └── 01_REQUIREMENTS/
            └── REV-A1/
                ├── ReqBS-RADOME-REV-A1.yaml
                └── ReqBS-RADOME-REV-A1.md
```

It links upstream to `eWTW-PBS-10-10-10-10-10` and ATLAS-053, and downstream to the radome IBS, RBS, CBS, EBS, CAD (`RADOME-REV-A1`), and PUB artefacts.
