# Evolutionary Acquisition Register — 600-699_OGATA / 670-679_Autonomous-Services-in-Closed-Environments

## 1. Architecture Band

| Field             | Value                       |
| ----------------- | --------------------------- |
| Architecture code | `OGATA`                 |
| Master range      | `600-699`               |
| Code range        | `670-679_Autonomous-Services-in-Closed-Environments`                |
| Architecture name | On-Ground Automation Technology Architecture                     |
| Scope             | Code range within OGATA.                    |

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
