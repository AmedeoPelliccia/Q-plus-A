````markdown
---
document_id: AMPEL360-EWTW-PBS-10-10-10-10-10-PUB-258-BONDING-LIGHTNING-CHECK-README
title: "eWTW · Radome — 258 Bonding and Lightning Check"
register: Q-plus
architecture: OPTIONS_ARCHITECTURE
options_axis: P-Programmes
programme: AMPEL360
product: eWTW
pbs_id: eWTW-PBS-10-10-10-10-10
pbs_title: "Radome"
part_number: PN-eWTW-5310-0001
publication_layer: pub
publication_category: 258_bonding-and-lightning-check
s1000d_info_code: "258"
s1000d_info_name: "Bonding and Lightning Check"
candidate_dmc: DMC-AMPEL360-A-53-10-10-00A-258A-D
status: draft
version: "0.1.0"
revision: A
language: en
---

# 258_bonding-and-lightning-check — Radome Lightning-Diverter Bonding Check

## 1. Purpose

This folder contains the publication artefacts for the radome lightning-diverter bonding check.

The check verifies that the radome bonding provisions, diverter attachment provisions, and lightning-protection interface remain suitable for continued safe operation.

This publication layer is applicable to:

```text
eWTW-PBS-10-10-10-10-10 — Radome
PN-eWTW-5310-0001
````

---

## 2. Publication Scope

The `258_bonding-and-lightning-check` publication covers:

* visual check of lightning diverter attachment condition;
* visual check of bonding provisions at radome interface;
* check of bonding continuity where applicable;
* check for damage, delamination, erosion, or moisture ingress near diverter paths;
* check for loose, missing, damaged, contaminated, or incorrectly seated bonding hardware;
* reporting of findings requiring maintenance action or engineering disposition.

---

## 3. Ownership Boundary

The radome owns the structural provisions and local bonding interface features.

The lightning diverter strips and aircraft lightning-protection network are owned by the lightning-protection system.

```text
Radome publication owns:
- radome-side provisions;
- local check of installed interface condition;
- inspection access and reporting.

LPS publication owns:
- diverter strip design;
- lightning current path design;
- bonding network architecture;
- certification substantiation.
```

---

## 4. Controlled Files

| File                                                                      | Purpose                            | Status  |
| ------------------------------------------------------------------------- | ---------------------------------- | ------- |
| `README.md`                                                               | Folder-level publication index.    | draft   |
| `DMC-AMPEL360-A-53-10-10-00A-258A-D_Lightning-Diverter-Bonding-Check.xml` | S1000D-oriented check data module. | planned |

---

## 5. S1000D-Oriented Mapping

| Field                 | Value                                |
| --------------------- | ------------------------------------ |
| Information code      | `258`                                |
| Information name      | Bonding and Lightning Check          |
| Candidate DMC         | `DMC-AMPEL360-A-53-10-10-00A-258A-D` |
| SNS / system code     | `53` — Fuselage / structural context |
| Product applicability | AMPEL360 eWTW baseline               |
| Item location code    | `D`                                  |
| QA status             | unverified draft                     |

---

## 6. Traceability

```text
PBS → PNR → PN → CAD → pub/258_bonding-and-lightning-check → Evidence → Lifecycle Gate
```

| Layer                | Identifier                                                                |
| -------------------- | ------------------------------------------------------------------------- |
| PBS                  | `eWTW-PBS-10-10-10-10-10`                                                 |
| PN                   | `PN-eWTW-5310-0001`                                                       |
| Description DM       | `DMC-AMPEL360-A-53-10-10-00A-040A-D_Radome-Description.xml`               |
| Check DM             | `DMC-AMPEL360-A-53-10-10-00A-258A-D_Lightning-Diverter-Bonding-Check.xml` |
| Current CAD maturity | `LC-A / RADOME-REV-A1`                                                    |
| Next CAD gate        | `RADOME-REV-A_RELEASED`                                                   |

---

## 7. Safety Status

This folder currently contains draft publication content only.

No maintenance action, inspection interval, acceptance limit, or return-to-service criterion is approved until the applicable engineering, safety, maintenance, and lightning-protection authorities review and release the procedure.

```
```
