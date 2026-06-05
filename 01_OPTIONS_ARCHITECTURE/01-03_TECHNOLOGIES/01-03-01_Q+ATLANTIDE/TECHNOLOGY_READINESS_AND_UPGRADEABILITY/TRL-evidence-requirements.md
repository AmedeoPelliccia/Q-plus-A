# TRL Evidence Requirements

## 1. Purpose

This document defines the evidence required to support each Technology Readiness
Level (TRL) claim within `Q+ATLANTIDE`. A TRL value is an **evidence-based
maturity claim**. A TRL that is not supported by the required evidence is
**provisional**. No TRL shall be claimed as accepted without evidence.

## 2. Acceptable Evidence Types

- analysis
- test
- simulation
- supplier data
- qualification report

## 3. Evidence by TRL

| TRL   | Definition                                                                 | Minimum Evidence                                                                 |
| ----- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| TRL-1 | Basic principles observed and reported.                                    | Published or internal report documenting the observed basic principles.          |
| TRL-2 | Technology concept and/or application formulated.                          | Concept/application formulation document.                                        |
| TRL-3 | Analytical and experimental proof of concept.                              | Analysis and/or early experimental proof-of-concept results.                     |
| TRL-4 | Component and/or breadboard validation in laboratory environment.          | Laboratory test/simulation results for component or breadboard.                  |
| TRL-5 | Component and/or breadboard validation in relevant environment.            | Test results in a relevant environment; supplier data where applicable.          |
| TRL-6 | System/subsystem model or prototype demonstration in relevant environment. | Prototype demonstration report in a relevant environment.                        |
| TRL-7 | System prototype demonstration in operational environment.                 | Demonstration report in an operational environment.                              |
| TRL-8 | Actual system completed and qualified through test and demonstration.      | Qualification report; completed test and demonstration evidence.                 |
| TRL-9 | Actual system proven through successful mission operations.                | Operational/mission evidence demonstrating successful operations.                |

## 4. Evidence Effectivity

Architecture-level evidence supports a **programme-agnostic** TRL claim.
Programme-specific TRL claims shall additionally carry **programme, product,
configuration, lifecycle state, and evidence effectivity**, and shall be stored
separately from the generic architecture nodes (`QATL-TRL-PROGRAMME-001`).

## 5. Provisional TRL Handling

When evidence is incomplete:

- record the TRL value as **provisional**;
- record the specific evidence gap;
- do not promote the technology to a higher TRL until the gap is closed;
- do not treat a provisional TRL as authorization to insert the technology into
  a controlled product configuration.

## 6. References

- **[SEF-01]** *Systems Engineering Fundamentals* — Defense Acquisition
  University / DoD guide. MIT OCW 16.885J Aircraft Systems Engineering,
  Fall 2005.
  <https://ocw.mit.edu/courses/16-885j-aircraft-systems-engineering-fall-2005/resources/sefguide_01_01/>
- **[SE-PDF]** *SYSTEMS Engineering* — Comprehensive SE reference covering
  SE processes, architecture development, requirements analysis, verification
  & validation, and technology maturity assessment (`SYSTEMS_engineering.pdf`).
