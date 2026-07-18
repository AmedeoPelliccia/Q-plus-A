# 029-900_Distributed-Electric-Actuation-and-Utility-Power

**Chapter:** 029_Actuation-and-Utility-Power · **Node:** 029-900

## Scope

Distributed-electric actuation and utility power. Centralized hydraulics (No.1/2/3 systems) are footprint: this node draws actuation and utility power distributed-electric from the HVDC bus (REF 024-900) and conditions it for flight-control actuation (EHA/EMA, REF 027-900) and utility actuation (gear, brakes, doors). Where a local EHA hydraulic loop or a single backup circuit is retained, it binds under `029-110` / `029-120`; a fully more-electric configuration routes all actuation power through this node.

## Context

```mermaid
flowchart LR
  H["024-900<br/>HVDC bus (source)"]
  C["029-900<br/>Actuation power conditioning"]
  A["027-900<br/>EHA/EMA actuators"]
  U["Utility actuation<br/>(gear, brakes, doors)"]
  R["029-110 / 029-120<br/>Residual hydraulic circuits<br/>(where retained)"]
  H --> C
  C --> A
  C --> U
  C -. "local EHA loop /<br/>backup circuit binding" .-> R
```

## Subject register

| Subject | Title | Folder |
|---|---|---|
| 010 | Distributed Electric Actuation Power | [029-900-010](029-900-010_Distributed-Electric-Actuation-Power/) |
| 030 | Local EHA Hydraulic Loop | [029-900-030](029-900-030_Local-EHA-Hydraulic-Loop/) |
| 050 | Utility Actuation Electric Power | [029-900-050](029-900-050_Utility-Actuation-Electric-Power/) |
| 070 | Actuation Power Conditioning from HVDC | [029-900-070](029-900-070_Actuation-Power-Conditioning-from-HVDC/) |

## Boundary summary

Actuation and utility power conditioning and distribution: here. HVDC generation and systems-power architecture: 024-900. EHA/EMA actuator architecture: 027-900. Residual hydraulic circuits: 029-110 / 029-120. Indicating: 029-300 series. Ground-service connections: 029-130.
