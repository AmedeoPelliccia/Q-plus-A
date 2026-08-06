# 030-900_Bleedless-Energy-Integrated-Ice-Protection

**Chapter:** 030_Ice-and-Rain-Protection · **Node:** 030-900

## Scope

The bleedless / energy-integrated content of ice protection: the electrothermal anti-ice power architecture that replaces engine bleed, waste-heat anti-icing recovered from the energy system, the bleedless air interface, and integrated ice-detection and protection control. Cross-references the HVDC band (REF 024-900), ECS thermal integration (REF 021-900), and energy-store waste heat (REF 028-900).

## Context

```mermaid
flowchart LR
  H["024-900<br/>HVDC band"]
  E["030-900-100<br/>Electrothermal anti-ice<br/>power architecture"]
  W["030-900-300<br/>Waste-heat anti-icing"]
  A["030-900-500<br/>Bleedless anti-ice<br/>air interface"]
  C["030-900-700<br/>Integrated ice-detection<br/>and protection control"]
  T["021-900<br/>ECS thermal integration"]
  S["028-900<br/>Energy-store waste heat"]
  H --> E
  S -. "recovered heat" .-> W
  A -. "interface (021-900-070)" .-> T
  C --- E
  C --- W
```

## Subject register

| Subject | Title | Folder |
|---|---|---|
| 100 | Electrothermal Anti-Ice Power Architecture | [030-900-100](030-900-100_Electrothermal-Anti-Ice-Power-Architecture/) |
| 300 | Waste-Heat Anti-Icing | [030-900-300](030-900-300_Waste-Heat-Anti-Icing/) |
| 500 | Bleedless Anti-Ice Air Interface | [030-900-500](030-900-500_Bleedless-Anti-Ice-Air-Interface/) |
| 700 | Integrated Ice-Detection and Protection Control | [030-900-700](030-900-700_Integrated-Ice-Detection-and-Protection-Control/) |

## Boundary summary

Bleedless / energy-integrated ice-protection architecture and control: here. HVDC power source: 024-900. ECS thermal integration and bleedless air interface counterpart: 021-900. Energy-store waste heat: 028-900. Electric surface and probe heating that is already conventional: the STD section-nodes of this chapter (030-100 through 030-820).
