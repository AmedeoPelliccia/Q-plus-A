---
status: draft
standard_scope: governance
---

# eWTW — Interface-and-Installation Breakdown Structure (IBS)

**Product:** AMPEL360 · eWTW — regional electric Wide Tube and Wing
**Sibling of:** `01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/` … `…-07_EBS_Evidence-Breakdown-Structure/`
**Location:** `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-08_IBS_Interface-and-Installation-Breakdown-Structure/`

---

## Purpose

The IBS controls **interfaces and installation elements** as dedicated, governed nodes inside the SBS. It exists to keep the boundary between *physical product* (PBS) and *integration relationship* (IBS) explicit, so that interfaces, envelopes, clearances, datums, tolerances and installation constraints are controlled records — not informal entries scattered between PBS parts.

> Interface / Installation Elements are **integration nodes**, not always principal parts.

---

## What lives where

| Concern | Lives in | Carries |
|---|---|---|
| Physical hardware (shell, fitting, seal, bracket, fastener set, bonding jumper, rail) | **PBS** | PBS ID · PNR · PN · BOM row · CAD (if relevant) · effectivity |
| Interface relationship, envelope, clearance, datum, tolerance stack, ICD, installation constraint, removal/installation boundary | **IBS** (this structure) | Interface record · ICD · datum/tolerance data |
| Installation / removal **task** (torque sequence, access zone, procedure) | **PUB / DM** | Data module |

The decision rule:

```text
If the interface/installation element is installed physical hardware → it must have a PBS / PNR / BOM.
If it is only a relationship, datum, envelope, clearance or ICD → it lives as an interface record (IBS), not a PBS part.
```

Physical interface hardware is therefore represented **in both** structures: the part in the PBS, the interface it realizes in the IBS. Non-physical interfaces live **only** in the IBS and are *referenced by* PBS, WBS, PUB and EBS artefacts — never duplicated into them.

---

## Numbering convention

Governed by **`AMPEL360-SBS-ID-CM-002` §3**. The IBS id space is **derived**:

> | **IBS** | derived | `eWTW-IBS-<CSN>-<counterpart>` = the ICD id (A1.9) | is the id | 1:1 with a declared interface |

An interface dossier carries the CSN of the station that declares it plus the counterpart field — a counterpart CSN (`eWTW-IBS-531004-538001`), or a taxonomy chapter when the other side is a system chapter, not a product node (`eWTW-IBS-531004-034`). **Station-scoped dossiers** — removal/installation envelopes and tolerance-and-datum stacks that belong to a station as a whole — carry the station CSN with a reserved alphabetic suffix instead of a counterpart: `eWTW-IBS-<CSN>-INST` and `eWTW-IBS-<CSN>-TOL`. Derived ids are regenerated, never typed (CM-002 §4.2): if a CSN changes under a ratified act, the dossier ids regenerate with it.

---

## Formal rule

```yaml
sbs_decomposition_rule:
  id: SBS-INTERFACE-INSTALLATION-001
  rule: >
    Interface and installation elements shall be controlled under the SBS as a
    dedicated Interface-and-Installation Breakdown Structure. Physical interface
    hardware shall also be represented in the PBS with PNR, BOM, CAD and
    effectivity. Non-physical interfaces, envelopes, clearances, datums,
    tolerances and installation constraints shall be controlled as IBS records
    and referenced by PBS, WBS, PUB and EBS artefacts.
```

---

## Worked example — Radome

The physical radome and its installed hardware live in the PBS, as the part-number tree of the station that assembles them:

```text
01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/
└── eWTW-PBS-000_Aircraft-Product/
    └── eWTW-PBS-050_Airframe-Structure/
        └── eWTW-PBS-053-000_Fuselage-Wide-Tube/
            ├── eWTW-PBS-053-100-000_Nose-and-Forward-Fuselage-Structure/
            │   └── eWTW-PBS-053-100-040_Radome-and-Diverters-Attach-Structure/   ← station, CSN 531004
            │       └── part numbers EWTW-531004-000 … EWTW-531004-021, -030, -040
            └── … sections eWTW-PBS-053-200-000 … eWTW-PBS-053-900-000
```

The interfaces, envelopes and datums that *connect* the radome to its neighbours live here, in the IBS:

```text
01-02-01-01-01-01-08_IBS_Interface-and-Installation-Breakdown-Structure/
└── eWTW-IBS-531004_Radome-Interface-Set/
    ├── eWTW-IBS-531004-538001_Radome-to-Forward-Pressure-Bulkhead.md
    ├── eWTW-IBS-531004-034_Radome-to-Weather-Radar.md
    ├── eWTW-IBS-531004-024_Radome-to-Lightning-Protection.md
    ├── eWTW-IBS-531004-INST_Radome-Removal-Installation-Envelope.md
    └── eWTW-IBS-531004-TOL_Radome-Tolerance-and-Datum-Stack.md
```

The radome's attachment/hinge/latch and bonding hardware are **owned by the radome station in the PBS** (part numbers such as `EWTW-531004-021` under `eWTW-PBS-053-100-040`); the IBS records control the *interface they realize*, not the parts themselves.

---

## Index

- [`eWTW-IBS-531004_Radome-Interface-Set/`](eWTW-IBS-531004_Radome-Interface-Set/) — radome interface and installation records.
- [`eWTW-IBS-533001_Rear-Fuselage-Zone-Interface-Set/`](eWTW-IBS-533001_Rear-Fuselage-Zone-Interface-Set/) — rear-fuselage-zone interface records (pilot, stubs).
- [`ICD-REGISTER.yaml`](ICD-REGISTER.yaml) — register of every interface declared in the PBS `station.yaml` files.
