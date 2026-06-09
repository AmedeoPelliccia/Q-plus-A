# 021-510-010 — Electrically driven cooling compressor

**Subject node (⚡)** of chapter `021_Air-Conditioning-Environmental-Control`, PMC `PMC-EWTW-AMM`.

The subject is the real TPuBS node: a *directory* that contains the AMM info-code breakdown
per convention `AMPEL360-AMM-INFOCODE-CM-001`. Each info code holds its SSOT/PBS link
(`ssot-ref.yaml`) and configuration management (`config-management.yaml`), and resolves to one
folder per effectivity range (the solution/variant), each holding one S1000D data module.

`MOD-EWTW-021-001` forks info codes `040`, `520` and `720` into PRE/POST solutions; `200` Servicing is unaffected and keeps a single `EFF-ALL` solution.

| Info code | Name | Solutions |
|---|---|---|
| `040` | Description | `040A`, `040B` |
| `200` | Servicing | `200A` |
| `520` | Remove procedures | `520A`, `520B` |
| `720` | Install procedures | `720A`, `720B` |

SSOT/PBS source: `EWTW-PBS-21-51-10-01` (one-way link, G-ATLAS SSOT chapter 021).
