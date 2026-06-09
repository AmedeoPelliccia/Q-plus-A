# 021-510-050 — Working fluid / refrigerant loop

**Subject node (⚡)** of chapter `021_Air-Conditioning-Environmental-Control`, PMC `PMC-EWTW-AMM`.

The subject is the real TPuBS node: a *directory* that contains the AMM info-code breakdown
per convention `AMPEL360-AMM-INFOCODE-CM-001`. Each info code holds its SSOT/PBS link
(`ssot-ref.yaml`) and configuration management (`config-management.yaml`), and resolves to one
folder per effectivity range (the solution/variant), each holding one S1000D data module.

No modification currently affects this subject; every info code resolves to a single `EFF-ALL` solution (MSN 0001-*).

| Info code | Name | Solutions |
|---|---|---|
| `040` | Description | `040A` |
| `200` | Servicing | `200A` |
| `520` | Remove procedures | `520A` |
| `720` | Install procedures | `720A` |

SSOT/PBS source: `eWTW-PBS-60-20_Environmental-Control-System-ECS-Electric` (one-way link, eWTW SSOT PBS:
`01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-60_Mechanical-and-Utility-Systems/eWTW-PBS-60-20_Environmental-Control-System-ECS-Electric`).
