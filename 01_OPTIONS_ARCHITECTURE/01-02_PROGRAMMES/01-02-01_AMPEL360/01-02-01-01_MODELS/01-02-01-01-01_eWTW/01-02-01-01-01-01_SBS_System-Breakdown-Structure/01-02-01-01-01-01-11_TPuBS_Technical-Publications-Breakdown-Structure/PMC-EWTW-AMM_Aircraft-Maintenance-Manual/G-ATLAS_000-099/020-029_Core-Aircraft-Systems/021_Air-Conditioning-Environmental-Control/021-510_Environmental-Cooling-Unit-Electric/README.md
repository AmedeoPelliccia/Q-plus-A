# 021-510 — Environmental Cooling Unit (Electric)

**Section node (⚡)** of chapter `021_Air-Conditioning-Environmental-Control`, PMC `PMC-EWTW-AMM`.

Electric environmental cooling unit — green-native substitution for the conventional
air-cycle machine (footprint: air-cycle machine). Cooling is electric; there is no engine
bleed in the green architecture (no `021-100`).

## Subject nodes

| Subject | Title | Carries |
|---|---|---|
| `021-510-010` | Electrically-Driven Cooling Compressor | ⚡ |
| `021-510-030` | Heat Exchanger Network | ⚡ |
| `021-510-050` | Working Fluid / Refrigerant Loop | ⚡ |
| `021-510-070` | Water Extraction and Humidity Control | STD |
| `021-510-090` | Cooling Control, Sensors and Protection | ⚡ |

Each subject node follows convention `AMPEL360-AMM-INFOCODE-CM-001`
(info-code breakdown → effectivity-range solution folders → S1000D data modules).
`MOD-EWTW-021-001` (vapour-cycle compressor upgrade, embodied MSN 0050) forks only the
info codes of `021-510-010` whose content it changes (`040`, `520`, `720`).
