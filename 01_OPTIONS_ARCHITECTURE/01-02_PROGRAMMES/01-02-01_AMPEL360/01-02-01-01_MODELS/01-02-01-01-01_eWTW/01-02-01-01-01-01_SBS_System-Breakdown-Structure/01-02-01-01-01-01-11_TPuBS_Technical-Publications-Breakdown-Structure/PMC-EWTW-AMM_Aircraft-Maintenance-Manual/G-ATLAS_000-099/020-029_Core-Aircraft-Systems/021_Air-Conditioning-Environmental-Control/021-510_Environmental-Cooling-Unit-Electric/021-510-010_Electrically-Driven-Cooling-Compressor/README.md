# 021-510-010 — Electrically driven cooling compressor

**Subject node (⚡)** of chapter `021_Air-Conditioning-Environmental-Control`, PMC `PMC-EWTW-AMM`.

The subject is the real TPuBS node: a *directory* that contains the AMM info-code breakdown
per convention `AMPEL360-AMM-INFOCODE-CM-001`. Each info code holds its SSOT/PBS link
(`ssot-ref.yaml`) and configuration management (`config-management.yaml`), and resolves to one
folder per effectivity range (the solution/variant), each holding one S1000D data module.

`MOD-EWTW-021-001` forks info codes `040`, `520` and `720` into PRE/POST solutions; `200` Servicing is unaffected and keeps a single `EFF-ALL` solution. Each fork carries a concrete content delta (recorded as `content_delta` in the info code's `config-management.yaml`): the pre-mod two-stage centrifugal compressor with remote 540 V DC motor controller is replaced by a hermetic scroll compressor with an integrated SiC controller in the vapour-cycle loop, changing the description and the remove/install procedures (refrigerant recovery, evacuation and charge). An effectivity update alone does not generate a new solution — it is only a stack update.

| Info code | Name | Solutions |
|---|---|---|
| `040` | Description | `040A`, `040B` |
| `200` | Servicing | `200A` |
| `520` | Remove procedures | `520A`, `520B` |
| `720` | Install procedures | `720A`, `720B` |

SSOT/PBS source: `eWTW-PBS-60-20_Environmental-Control-System-ECS-Electric` (one-way link, eWTW SSOT PBS:
`01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/eWTW-PBS-00_Aircraft-Product/eWTW-PBS-60_Mechanical-and-Utility-Systems/eWTW-PBS-60-20_Environmental-Control-System-ECS-Electric`).
