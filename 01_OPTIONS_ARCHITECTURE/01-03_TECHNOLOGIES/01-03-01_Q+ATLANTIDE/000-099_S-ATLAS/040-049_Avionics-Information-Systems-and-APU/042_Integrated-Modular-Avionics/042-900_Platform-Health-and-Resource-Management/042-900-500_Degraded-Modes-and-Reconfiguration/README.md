# 042-900-005 — Degraded Modes and Reconfiguration

**Node:** 042-900_Platform-Health-and-Resource-Management · **Subject:** 005

- Reconfiguration doctrine: the platform moves only between pre-qualified configurations — selection among verified states, never synthesis of a new state in operation.
- Triggers, priorities and inhibitions are declared in the reconfiguration policy (042-400); this node evaluates triggers against correlated health state and commands the transition.
- Transitions are managed: ordered function migration or shedding, network contract continuity per 042-200, and positive confirmation of the reached state before annunciation of completion.
- Every transition is recorded with cause, path and confirmation — a reconfiguration without a record did not happen.

```mermaid
stateDiagram-v2
  [*] --> NOMINAL
  NOMINAL --> DEGRADED_1: qualified trigger<br/>(policy 042-400)
  DEGRADED_1 --> DEGRADED_2: further qualified trigger
  DEGRADED_1 --> NOMINAL: recovery confirmed
  DEGRADED_2 --> DEGRADED_1: partial recovery confirmed
  NOMINAL --> NOMINAL: contained event<br/>(no reconfiguration)
  note right of DEGRADED_2
    every target state is
    pre-qualified in 042-400
  end note
```

