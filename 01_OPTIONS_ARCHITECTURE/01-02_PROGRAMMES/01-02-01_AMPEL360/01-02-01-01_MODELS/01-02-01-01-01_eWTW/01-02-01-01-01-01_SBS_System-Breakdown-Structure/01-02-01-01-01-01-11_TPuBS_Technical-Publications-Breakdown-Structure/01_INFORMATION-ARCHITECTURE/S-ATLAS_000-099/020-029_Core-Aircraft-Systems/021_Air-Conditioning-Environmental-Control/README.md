# 021 — Air Conditioning & Environmental Control

**Chapter node** of `PMC-EWTW-AMM` (Aircraft Maintenance Manual), S-ATLAS master range
`020-029_Core-Aircraft-Systems`, programme eWTW (AMPEL360), doctrine **green-native**, owner **Q-AIR**.

This chapter holds the TPuBS directory nodes for air conditioning and environmental control.
The full map — sections, subject nodes and the info-code / effectivity-variant anatomy — is in
[`021_TPuBS-Node-Tree.md`](./021_TPuBS-Node-Tree.md).

## Structure

- **Sections `021-000` … `021-620`** — standard (STD) carries: distribution, pressurization,
  heating and temperature control directory nodes (currently scaffold placeholders).
- **`021-500` / `021-510`** — ⚡ electric substitution: environmental cooling is electric
  (footprints: bleed-air pack / air-cycle machine). `021-510` contains the developed subject
  nodes, with `021-510-010_Electrically-Driven-Cooling-Compressor` at full depth.
- **`021-900`** — STD-G green delta: energy-system thermal integration subject nodes.

> **No `021-100`** — the conventional bleed/compression section is footprinted out
> (no engine bleed in the green architecture); cooling is electric at `021-500/510`.

## Conventions

- Subject nodes (`021-SSS-UUU`) are **directories** that contain the AMM info-code breakdown
  per `AMPEL360-AMM-INFOCODE-CM-001`: each info code carries `ssot-ref.yaml` (one-way PBS
  source link), `config-management.yaml` (modification stack → resulting effectivity) and one
  `EFF-…` solution folder per effectivity range, each holding one S1000D Issue 4.2 data module.
- `MOD-EWTW-021-001` (vapour-cycle compressor upgrade, embodied MSN 0050) forks only the
  info codes of `021-510-010` whose content it changes (`040`, `520`, `720`).

Status: **scaffold** · Version: **1.0**
