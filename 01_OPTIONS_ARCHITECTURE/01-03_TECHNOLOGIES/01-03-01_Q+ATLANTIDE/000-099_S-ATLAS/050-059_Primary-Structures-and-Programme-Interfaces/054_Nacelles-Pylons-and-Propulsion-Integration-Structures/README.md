# 054_Nacelles-Pylons-and-Propulsion-Integration-Structures

**Range:** 050-059_Primary-Structures-and-Programme-Interfaces · **Chapter:** 054

## Scope

Airframe-side propulsion integration structures: nacelle structures, pylons, mounts and support structures, dorsal and embedded propulsion integration, inlet and exhaust structural interfaces, load-transfer attachments, fire-thermal-acoustic protection structures, cowlings and fairings, aero-structural integration, and sustainable-installation provisions. Ownership rule: 054 owns the physical nacelle, pylon, fairing, mounting and propulsion-to-airframe structural integration; propulsion ranges 060-079 own the machines, powertrains and functional installation requirements; 053 and 057 own the receiving primary structure.

## Integration chain

```mermaid
flowchart LR
  M["Machine and powertrain<br>060-079<br>(061 · 077-500 installation discipline)"]
  I["054<br>Integration structures:<br>nacelle · pylon · dorsal fairing<br>mounts · inlet/exhaust structure"]
  P["Receiving primary structure<br>053 centerbody/fuselage · 057 wing"]
  C["Type-class constraints<br>091 BWB/BLI"]
  M --&gt;|"functional requirements<br>and interface loads"| I
  I --&gt;|"attachment reactions<br>and load transfer"| P
  C -. "constrains, never duplicates" .-&gt; I
```

## Section register

| Section | Title | Subjects |
|---|---|---|
| 054-000 | [General](054-000_General/) | 3 |
| 054-100 | [Nacelle Structures](054-100_Nacelle-Structures/) | 4 |
| 054-200 | [Pylons Mounts and Support Structures](054-200_Pylons-Mounts-and-Support-Structures/) | 5 |
| 054-300 | [Dorsal and Embedded Propulsion Integration](054-300_Dorsal-and-Embedded-Propulsion-Integration/) | 5 |
| 054-400 | [Inlet and Exhaust Structural Interfaces](054-400_Inlet-and-Exhaust-Structural-Interfaces/) | 4 |
| 054-500 | [Attachments and Load Transfer Interfaces](054-500_Attachments-and-Load-Transfer-Interfaces/) | 4 |
| 054-600 | [Fire Thermal and Acoustic Protection Structures](054-600_Fire-Thermal-and-Acoustic-Protection-Structures/) | 4 |
| 054-700 | [Cowlings Fairings and Access Provisions](054-700_Cowlings-Fairings-and-Access-Provisions/) | 4 |
| 054-800 | [Aerodynamic and Aeroelastic Integration](054-800_Aerodynamic-and-Aeroelastic-Integration/) | 3 |
| 054-900 | [Sustainable Propulsion Installation Provisions](054-900_Sustainable-Propulsion-Installation-Provisions/) | 5 |

## Boundary summary

Ownership rule: 054 owns the physical nacelle, pylon, fairing, mounting and propulsion-to-airframe structural integration. Propulsion ranges 060-079 own machines, powertrains, propulsion functions and functional installation requirements (061 combustion installation discipline, 077-500 electric-propulsor installation). 053 and 057 own the receiving centerbody, fuselage or wing primary structure and the corresponding airframe-side attachment provisions. Mount split: requirements, loads and failure cases 061-100 / 077-500; physical mount and support structure 054-200. Firewall split: zone definition, hazards and protection requirements 061-300 and 026; implementing firewall and segregation structure 054-600. Inlet and exhaust split: aerodynamic and functional requirements belong to 061-800, the relevant propulsion-machine chapters and 067; anti-ice and thermal provisions reference 030 and 065; physical structural interfaces, lips, ducts, load paths and surrounding structure belong to 054-400. Aerodynamic split: machine and installation effects 061-800; aerostructural and aeroelastic integration 054-800; configuration-class constraints 091. Protection split: 054-600 owns physical barriers, shields, liners, insulation supports and structural segregation; detection, extinguishing, environmental-control and source-noise functions remain in their functional chapters. Structural practices: 051. Type classes 090-099 constrain and reference this chapter and shall not duplicate it.
