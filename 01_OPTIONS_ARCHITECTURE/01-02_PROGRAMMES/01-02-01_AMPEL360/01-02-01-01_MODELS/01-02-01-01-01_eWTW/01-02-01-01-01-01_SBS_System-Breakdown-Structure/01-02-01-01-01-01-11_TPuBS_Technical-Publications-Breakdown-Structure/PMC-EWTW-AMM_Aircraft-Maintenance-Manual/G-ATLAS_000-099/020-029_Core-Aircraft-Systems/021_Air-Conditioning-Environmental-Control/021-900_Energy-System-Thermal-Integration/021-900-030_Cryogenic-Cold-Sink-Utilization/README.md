# 021-900-030 — Cryogenic cold sink utilization

**Subject node (STD-G)** of chapter `021_Air-Conditioning-Environmental-Control`, PMC `PMC-EWTW-AMM`.

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

SSOT/PBS source: `EWTW-PBS-21-90-30-01` (one-way link, G-ATLAS SSOT chapter 021).
