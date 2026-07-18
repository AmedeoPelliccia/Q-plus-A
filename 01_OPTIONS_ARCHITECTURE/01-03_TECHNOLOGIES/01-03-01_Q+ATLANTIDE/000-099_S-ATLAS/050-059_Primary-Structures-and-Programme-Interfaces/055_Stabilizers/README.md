# 055_Stabilizers

**Range:** 050-059_Primary-Structures-and-Programme-Interfaces · **Chapter:** 055

## Scope

Empennage structures as programme-agnostic classes: horizontal stabilizer including trimmable-stabilizer structure, elevator structures, vertical stabilizer including dorsal fin, rudder structures, leading edges, tips and fairings, hinges, fittings and attachments, systems installation provisions, aeroelastic and balance characteristics, and advanced sustainable empennage architectures. Control-surface structure lives here; actuation, control laws and trim function are 027; the receiving fuselage structure is 053; instance geometry and tail arrangements are class and downstream matters.

## Integration chain

```mermaid
flowchart LR
  subgraph EMP["Empennage structure"]
    H["055-100 Horizontal<br>Stabilizer"] --- E["055-200<br>Elevators"]
    V["055-300 Vertical<br>Stabilizer"] --- RU["055-400<br>Rudders"]
  end
  L["055-500 Leading Edges,<br>Tips and Fairings"] --- EMP
  F["055-600 Hinges, Fittings<br>and Attachments"] --- EMP
  P["055-700 Systems Installation<br>Provisions"] --- EMP
  A["055-800 Aeroelastic, Balance<br>and Dynamics"] --- EMP
  N["055-900 Advanced and Sustainable<br>Empennage Architectures"] -. "applies across" .-&gt; EMP
  F --&gt;|"attachment reactions<br>and load transfer"| R053["Receiving structure<br>053 (fittings 053-800;<br>tailcone zone 053-400)"]
  EMP -. "actuation, control and<br>trim function" .-&gt; X027["027"]
```

## Section register

| Section | Title | Subjects |
|---|---|---|
| 055-000 | <a>General</a> | 4 |
| 055-100 | <a>Horizontal Stabilizer Structure</a> | 6 |
| 055-200 | <a>Elevator Structures</a> | 5 |
| 055-300 | <a>Vertical Stabilizer Structure</a> | 5 |
| 055-400 | <a>Rudder Structures</a> | 5 |
| 055-500 | <a>Leading Edges Tips and Fairings</a> | 4 |
| 055-600 | <a>Hinges Fittings and Attachments</a> | 5 |
| 055-700 | <a>Empennage Systems Installation Provisions</a> | 4 |
| 055-800 | <a>Aeroelastic Balance and Dynamic Characteristics</a> | 3 |
| 055-900 | <a>Advanced and Sustainable Empennage Architectures</a> | 6 |

## Boundary summary

Control surfaces: structure here; actuation, control laws and trim function 027 (trimmable-stabilizer drive 027-400; pivot and attach structure 055-140/630). Receiving structure: 053 owns the fuselage opening, reinforcement and fittings (053-800); the tailcone and auxiliary-power zone boundary is 053-400. Auxiliary-power intake: function 049-300, leading-edge structural surrounds 055-520. Ice protection: function 030, provisions 055-540. Static dischargers: system 023-600, provisions 055-720. Lights 033 and antennas 023/034: provisions 055-730. Aft and dorsal propulsion: integration structure 054-300, empennage-side provisions 055-940. Trim-volume storage: provisions 055-160, carrier system 028. Structural practices: 051. Type classes 090-099 constrain tail arrangements and geometry and shall not duplicate this chapter.
