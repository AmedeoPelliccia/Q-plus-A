# TRL Assessment Rules

## 1. Scope

This document defines the rules for assigning and maintaining Technology
Readiness Level (TRL) values within `Q+ATLANTIDE`. TRL is a claim about
**technology maturity** only. It is not a claim about product, CAD,
integration, or configuration maturity (which are governed by LC-letter
lifecycle stages and REV cycles).

## 2. General Rules

1. TRL values are **evidence-based maturity claims**. Each assigned TRL must be
   traceable to supporting evidence (see `TRL-evidence-requirements.md`).
2. A TRL value that is **not** supported by the required evidence is
   **provisional** and shall be marked as such. No TRL shall be claimed as
   accepted without evidence.
3. A technology shall be assessed against the **lowest** TRL whose evidence
   criteria are fully satisfied; a higher TRL may only be claimed once every
   lower-level criterion is also met.
4. Architecture-level TRL values shall remain **programme-agnostic**.
   Programme-specific TRL values shall be recorded separately with programme,
   product, configuration, lifecycle state, and evidence effectivity
   (`QATL-TRL-PROGRAMME-001`).
5. TRL maturity shall not be mixed with LC-letter lifecycle maturity
   (`QATL-TRL-LC-001`). Reaching a target TRL authorizes the start of a
   controlled upgrade revision cycle, not direct installation into a product
   baseline.

## 3. Assessment Procedure

1. Identify the technology and its `Q+ATLANTIDE` node reference.
2. Collect the evidence available for the technology.
3. Map the evidence to the TRL scale (TRL-1 through TRL-9).
4. Assign the supported TRL; if evidence is incomplete, record the TRL as
   provisional with the evidence gap noted.
5. Record the assessment in the relevant architecture-band `TRL-register.yaml`.

## 4. TRL Scale (Reference)

| TRL   | Definition                                                                 |
| ----- | -------------------------------------------------------------------------- |
| TRL-1 | Basic principles observed and reported.                                    |
| TRL-2 | Technology concept and/or application formulated.                          |
| TRL-3 | Analytical and experimental proof of concept.                              |
| TRL-4 | Component and/or breadboard validation in laboratory environment.          |
| TRL-5 | Component and/or breadboard validation in relevant environment.            |
| TRL-6 | System/subsystem model or prototype demonstration in relevant environment. |
| TRL-7 | System prototype demonstration in operational environment.                 |
| TRL-8 | Actual system completed and qualified through test and demonstration.      |
| TRL-9 | Actual system proven through successful mission operations.                |
