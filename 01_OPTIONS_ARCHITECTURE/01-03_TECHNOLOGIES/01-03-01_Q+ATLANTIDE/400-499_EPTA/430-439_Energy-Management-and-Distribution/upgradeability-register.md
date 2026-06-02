# Upgradeability Register — 400-499_EPTA / 430-439_Energy-Management-and-Distribution

## 1. Architecture Band

| Field             | Value                       |
| ----------------- | --------------------------- |
| Architecture code | `EPTA`                 |
| Master range      | `400-499`               |
| Code range        | `430-439_Energy-Management-and-Distribution`                |
| Architecture name | Energy and Propulsion Technology Architecture                     |
| Scope             | Code range within EPTA.                    |

## 2. Controlled Rules

- A node may identify ready-to-use **baseline technologies** and future
  **alternative technologies**.
- Future alternatives shall **not** replace the baseline in a controlled
  programme configuration unless target TRL, interface compatibility, evidence
  delta, lifecycle insertion gate, and configuration approval are satisfied
  (`QATL-UPGRADE-001`).
- A technology upgrade becomes **eligible** through TRL maturity; it becomes
  **installable** only through LC/REV maturity.
- When an alternative reaches its target TRL, it shall start a new controlled
  revision cycle from its own concept baseline and shall **not** overwrite the
  current released baseline (`QATL-UPGRADE-REV-CYCLE-001`).

## 3. Root TRL and Upgradeability Control Folder

`../../00_TECHNOLOGY_READINESS_AND_UPGRADEABILITY/`

The structured records are maintained in `upgradeability-register.yaml` in
this folder.
