# LC-A Concept Design — REV-AX

This revision folder contains all artifacts for the Radome PBS item at lifecycle phase LC-A Concept Design and revision REV-AX. Artifact-domain and tool-specific folders such as CAD, FreeCAD, Requirements, Analysis, Evidence, Manufacturing, and Validation must sit under this revision folder. They must not contain lifecycle folders inside them.

## Governance rule

```text
eWTW-PBS-10-10-10-10-10_Radome/
└── LC-A_Concept-Design/
    └── REV-AX/
        ├── CAD/
        ├── FreeCAD/
        ├── Requirements/
        ├── Analysis/
        ├── Evidence/
        ├── Manufacturing/
        └── Validation/
```

Lifecycle phase and revision govern the artifact-domain folders. Tool-specific folders (FreeCAD, CAD, etc.) are always subordinate to the lifecycle/revision level and must never contain lifecycle phase folders inside them.
