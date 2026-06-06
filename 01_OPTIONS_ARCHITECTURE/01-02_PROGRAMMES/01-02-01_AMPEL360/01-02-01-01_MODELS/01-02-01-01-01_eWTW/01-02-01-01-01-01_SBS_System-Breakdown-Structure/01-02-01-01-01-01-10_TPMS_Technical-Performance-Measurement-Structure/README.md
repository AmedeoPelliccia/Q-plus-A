---
status: draft
standard_scope: governance
---

# eWTW — Technical Performance Measurement Structure (TPMS)

**Product:** AMPEL360 · eWTW — regional electric Wide Tube and Wing
**Sibling of:** `01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/` … `…-09_ReqBS_Requirements-Breakdown-Structure/`
**Location:** `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-10_TPMS_Technical-Performance-Measurement-Structure/`

---

## Purpose

The TPMS controls **Technical Performance Measures (TPMs)** as dedicated, governed records inside the SBS. TPMs are the quantified technical parameters tracked against targets and thresholds across the lifecycle — mass, RF loss, boresight error, bonding resistance, erosion life, and similar. They are too important to leave embedded only in Markdown prose or CAD records.

> TPMs are **tracked, revisioned quantities**: each has a target, a threshold, a current estimate, and a margin that evolves with the product revision.

---

## Relationship to ReqBS

TPMs are the measurable expression of `ReqBS-13 Technical Performance Measures` (see `…-09_ReqBS_Requirements-Breakdown-Structure/`). The ReqBS class declares *which* parameters are controlled; the TPMS tracks *their value, target, threshold and margin* per PBS item revision.

```text
ReqBS-13 (declares the TPM)  →  TPMS (tracks target / threshold / current / margin per REV-X)
```

As with all breakdown structures, the **authoritative TPM state for a physical item is recorded per PBS item revision** (`REV-X`); this folder defines the generic measurement framework and governance.

---

## What lives where

| Concern | Lives in | Carries |
|---|---|---|
| Generic TPM framework, definitions, and tracking convention | **TPMS** (this structure) | Parameter definitions · units · governance |
| Declaration that a parameter is a controlled TPM | **ReqBS `ReqBS-13`** (per `REV-X`) | Requirement reference |
| Authoritative TPM value / target / threshold / margin | **PBS item `REV-X`** | Tracked TPM record alongside the revision ReqBS |

---

## Formal rule

```yaml
tpms_tracking_rule:
  id: SBS-TPMS-001
  name: "Technical Performance Measurement Structure Rule"
  rule: >
    Technical Performance Measures shall be controlled under the SBS as a
    dedicated Technical Performance Measurement Structure. Each TPM shall carry
    a parameter definition, unit, target, threshold, and current estimate, and
    shall trace to its ReqBS-13 declaration. The authoritative TPM state for a
    physical product item shall be recorded per PBS item revision and shall be
    re-assessed whenever the corresponding REV-X ReqBS, CAD, or interface state
    changes.
```

---

## Radome TPM examples

For the radome (`eWTW-PBS-10-10-10-10-10`), the controlled TPMs include:

| TPM | Unit | Source requirement |
|---|---|---|
| Mass | kg | Physical characteristics / performance |
| RF transmission loss | dB | RF performance (from WXR, PBS-50) |
| Boresight error | mrad | RF performance (from WXR, PBS-50) |
| Bonding resistance | mΩ | Lightning protection provisions (LPS, PBS-40-40) |
| Erosion life | flight-hours | Rain-erosion durability |

The radome TPM targets and margins are tracked against the revision baseline declared in `ReqBS-RADOME-REV-A1` (`ReqBS-13`).

---

## References

[^sef]: Defense Acquisition University (DAU) Press. *Systems Engineering Fundamentals*. Fort Belvoir, VA, January 2001. — Ch. 4 *Requirements Analysis*, Task 13 *Technical Performance Measures (TPMs)*; Ch. 14 *Metrics*.
[^ieee1220]: IEEE Std 1220, *IEEE Standard for Application and Management of the Systems Engineering Process* — defines Technical Performance Measures within the requirements analysis task areas.
[^iso15288]: ISO/IEC/IEEE 15288, *Systems and software engineering — System life cycle processes*.
[^incose]: INCOSE. *Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities* — Technical Performance Measurement.
