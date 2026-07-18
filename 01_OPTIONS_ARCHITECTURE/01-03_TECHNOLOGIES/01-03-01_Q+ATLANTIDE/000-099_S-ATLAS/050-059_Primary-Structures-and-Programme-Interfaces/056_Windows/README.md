# 056_Windows

**Range:** 050-059_Primary-Structures-and-Programme-Interfaces · **Chapter:** 056

## Scope

Transparency assemblies as programme-agnostic classes: flight-compartment windows including openable direct-vision classes, passenger-cabin windows, door and hatch windows, sensor and special apertures, retention and sealing systems, transparency materials and optical properties, environmental protection and heating interfaces, monitoring and inspection, and advanced sustainable window architectures. 056 owns the transparency assembly — panes, interlayers, assembly-integral frame, retainers and seals; the receiving structure owns the opening, posts, surround reinforcement and load path (053 fuselage; 052 where the carrier is a door or hatch leaf). Instance counts and arrangements are downstream matters.

## Integration chain

```mermaid
flowchart LR
  subgraph CLASSES["Transparency classes"]
    W["056-100 Flight-Compartment<br>Windows"]
    P["056-200 Passenger-Cabin<br>Windows"]
    D["056-300 Door and<br>Hatch Windows"]
    A["056-400 Sensor and<br>Special Apertures"]
  end
  R["056-500 Retention, Seals<br>and Pressure Boundary"] --- CLASSES
  M["056-600 Materials and<br>Optical Properties"] --- CLASSES
  E["056-700 Environmental Protection<br>and Heating Interfaces"] --- CLASSES
  H["056-800 Monitoring, Inspection<br>and Health"] --- CLASSES
  N["056-900 Advanced and Sustainable<br>Window Architectures"] -. "applies across" .-&gt; CLASSES
  CLASSES --&gt;|"interface loads and<br>attachment reactions"| RS["Receiving structure<br>053 fuselage · 052 door/hatch leaf"]
  E -. "heating, wiping and<br>ice function" .-&gt; X030["030-4xx"]
  N -. "virtual-window and dimming<br>control functions" .-&gt; X044["044"]
```

## Section register

| Section | Title | Subjects |
|---|---|---|
| 056-000 | [General](056-000_General/) | 4 |
| 056-100 | [Flight Compartment Windows](056-100_Flight-Compartment-Windows/) | 5 |
| 056-200 | [Passenger Cabin Windows](056-200_Passenger-Cabin-Windows/) | 5 |
| 056-300 | [Door and Hatch Windows](056-300_Door-and-Hatch-Windows/) | 4 |
| 056-400 | [Sensor and Special Apertures](056-400_Sensor-and-Special-Apertures/) | 4 |
| 056-500 | [Retention Seals and Pressure Boundary](056-500_Retention-Seals-and-Pressure-Boundary/) | 4 |
| 056-600 | [Transparency Materials and Optical Properties](056-600_Transparency-Materials-and-Optical-Properties/) | 5 |
| 056-700 | [Environmental Protection and Heating Interfaces](056-700_Environmental-Protection-and-Heating-Interfaces/) | 4 |
| 056-800 | [Monitoring Inspection and Health](056-800_Monitoring-Inspection-and-Health/) | 3 |
| 056-900 | [Advanced and Sustainable Window Architectures](056-900_Advanced-and-Sustainable-Window-Architectures/) | 6 |

## Boundary summary

Assembly versus receiving structure: 056 owns panes, interlayers, assembly-integral frames, retainers and seals; 053 owns fuselage openings, windshield posts and surround reinforcement; 052 owns the door or hatch leaf carrying a window assembly. Heating, demist, wiping and rain-removal functions: 030-4xx; assembly-side provisions 056-150/7xx. Cabin-pressure function: 021-3xx; boundary implementation 056-5xx. Cabin reveals, shades and furnishings: 025. Vision and sensing systems: 034 and their chapters; apertures 056-400. Display and dimming control functions: 044; window-side implementation 056-910/920. Materials practices: 051-3xx generic, transparency-specific behavior 056-600; NDI standards 051-140. Lights and lenses: 033. Placards: 011. Type classes 090-099 constrain window arrangements and shall not duplicate this chapter.
