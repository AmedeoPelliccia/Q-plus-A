---
status: draft
standard_scope: governance
---

# eWTW — Interface-and-Installation Breakdown Structure (IBS)

**Product:** AMPEL360 · eWTW — regional electric Wide Tube and Wing
**Sibling of:** `01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/` … `…-07_EBS_Evidence-Breakdown-Structure/`
**Location:** `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_PRODUCTS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-08_IBS_Interface-and-Installation-Breakdown-Structure/`

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

The IBS uses a **semantic interface identifier** (`eWTW-IBS-NN[-NN…]`), not the folder ordinal chain — mirroring the PBS "semantic ID, ordinals for sort only" rule. An interface set is keyed to the PBS element it serves (for example `eWTW-IBS-10-10-10-10` mirrors the radome's parent PBS node `eWTW-PBS-10-10-10-10`), so PBS ↔ IBS adjacency is read directly from the identifier.

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

The physical radome and its installed hardware live in the PBS:

```text
01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/
└── eWTW-PBS-00_Aircraft-Product/
    └── eWTW-PBS-10_Airframe-Structure/
        └── eWTW-PBS-10-10_Fuselage-Wide-Tube/
            └── eWTW-PBS-10-10-10_Forward-Fuselage-Section/
                └── eWTW-PBS-10-10-10-10_Nose-Structure-and-Radome-Backup/
                    ├── eWTW-PBS-10-10-10-10-10_Radome/
                    ├── eWTW-PBS-10-10-10-10-20_Radome-Backup-Bulkhead/
                    ├── eWTW-PBS-10-10-10-10-30_Nose-Cap-and-Forward-Fairing/
                    └── eWTW-PBS-10-10-10-10-40_Lightning-Diverter-Provisions/
```

The interfaces, envelopes and datums that *connect* the radome to its neighbours live here, in the IBS:

```text
01-02-01-01-01-01-08_IBS_Interface-and-Installation-Breakdown-Structure/
└── eWTW-IBS-10-10-10-10_Radome-Interface-Set/
    ├── eWTW-IBS-10-10-10-10-10_Radome-to-Backup-Bulkhead.md
    ├── eWTW-IBS-10-10-10-10-20_Radome-to-WXR.md
    ├── eWTW-IBS-10-10-10-10-30_Radome-to-LPS.md
    ├── eWTW-IBS-10-10-10-10-40_Radome-Removal-Installation-Envelope.md
    └── eWTW-IBS-10-10-10-10-50_Radome-Tolerance-and-Datum-Stack.md
```

The radome's attachment/hinge/latch and bonding hardware are **owned by the radome in the PBS** (constituents of `eWTW-PBS-10-10-10-10-10`); the IBS records control the *interface they realize*, not the parts themselves.

---

## Index

- [`eWTW-IBS-10-10-10-10_Radome-Interface-Set/`](eWTW-IBS-10-10-10-10_Radome-Interface-Set/) — radome interface and installation records.
