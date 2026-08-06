# 042-300_Remote-Interface-and-IO-Concentration

**Chapter:** 042_Integrated-Modular-Avionics · **Node:** 042-300

## Scope

Remote interface units and input/output concentration: zonal acquisition of sensor signals, signal conditioning and digitization, publication onto the deterministic network, command output toward effectors with wraparound monitoring and declared safe-state behavior. Sensors and effectors belong to their functional chapters; this node owns the interfacing and concentration function between them and the avionics network.

## Context

```mermaid
flowchart LR
  S["Sensors / Effectors<br/>(functional chapters)"]
  R["042-300<br/>Remote Interface Units"]
  N["042-200<br/>Deterministic Network"]
  P["042-100<br/>Core Processing Platform"]
  C["042-400<br/>Configuration Governance"]
  H["042-900<br/>Health & Resource Mgmt"]
  S <--> R
  R <--> N
  N <--> P
  C -. "configuration tables" .-> R
  R -. "BITE / health reports" .-> H
```

## Subject register

| Subject | Title | Folder |
|---|---|---|
| 000 | Remote Interface and IO Concentration Overview | [042-300-000](042-300-000_Remote-Interface-and-IO-Concentration-Overview/) |
| 100 | Scope and Definitions | [042-300-100](042-300-100_Scope-and-Definitions/) |
| 200 | Remote Unit Architecture and Installation Zones | [042-300-200](042-300-200_Remote-Unit-Architecture-and-Installation-Zones/) |
| 300 | Signal Acquisition Conditioning and Digitization | [042-300-300](042-300-300_Signal-Acquisition-Conditioning-and-Digitization/) |
| 400 | IO Concentration and Publication | [042-300-400](042-300-400_IO-Concentration-and-Publication/) |
| 500 | Command Output and Effector Interfaces | [042-300-500](042-300-500_Command-Output-and-Effector-Interfaces/) |
| 600 | Configuration and Data Loading | [042-300-600](042-300-600_Configuration-and-Data-Loading/) |
| 700 | Built In Test and Health Reporting | [042-300-700](042-300-700_Built-In-Test-and-Health-Reporting/) |
| 800 | Interfaces and Boundaries | [042-300-800](042-300-800_Interfaces-and-Boundaries/) |
| 900 | Evidence and Certification Data | [042-300-900](042-300-900_Evidence-and-Certification-Data/) |

## Boundary summary

Interfacing and concentration function: here. Sensors and effectors: functional chapters. Network contracts and time: 042-200. Consumer allocation: 042-400. Health consumption: 042-900. Data loading: 045. Harness and installation: wiring standard practices and structures.

