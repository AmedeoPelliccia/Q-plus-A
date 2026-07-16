# 042-900-000 — Platform Health and Resource Management Overview

**Node:** 042-900_Platform-Health-and-Resource-Management · **Subject:** 000

- This node is the runtime guardian of the avionics platform: it collects health evidence from every layer, contains faults, watches resource margins, and — when needed — moves the platform between pre-qualified configurations.
- Its authority is bounded by construction: it executes decisions within the envelope declared in the hosting plan and reconfiguration policy (042-400); it never invents a configuration.
- Everything it observes becomes either annunciation, maintenance record, or both — silence is not a failure mode.

