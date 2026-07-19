# Evolutionary Acquisition Register — 100-199_S-STA / 120-129_Space-Propulsion

## 1. Architecture Band

| Field             | Value                       |
| ----------------- | --------------------------- |
| Architecture code | `S-STA`                 |
| Master range      | `100-199`               |
| Code range        | `120-129_Space-Propulsion`                |
| Architecture name | Sustainable Space Technology Architecture                     |
| Scope             | Code range within S-STA.                    |

## 2. Controlled Rules

- Evolutionary blocks, incremental capability releases, and associated product
  improvements shall be planned through controlled baselines, TRL assessment,
  evidence records, CM authority, and lifecycle gates (`QATL-EVO-ACQ-001`).
- The core system architecture shall emphasize openness, modularity, and stable
  interfaces to facilitate future upgrades (`QATL-OPEN-ARCH-UPGRADE-001`).
- Upgrade branches shall **not** overwrite released product baselines until
  configuration approval and lifecycle release gates are satisfied
  (`QATL-BASELINE-HIERARCHY-001`).
- A technology upgrade becomes **eligible** through TRL maturity; it becomes
  **installable** only through LC/REV maturity; it becomes **part of the
  operational baseline** only through configuration-control approval.

## 3. Root Control Folder

`../../00_TECHNOLOGY_READINESS_AND_UPGRADEABILITY/`

The structured records are maintained in `evolutionary-acquisition-register.yaml`
in this folder.
