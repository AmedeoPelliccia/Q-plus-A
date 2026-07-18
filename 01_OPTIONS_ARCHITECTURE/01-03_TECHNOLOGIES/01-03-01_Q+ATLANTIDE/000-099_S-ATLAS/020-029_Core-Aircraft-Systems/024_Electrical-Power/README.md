# 024 — Electrical Power

**Chapter:** `024` ⇄ ATA **24**
**Master range:** `020-029_Core-Aircraft-Systems` · **Band:** `000-099_S-ATLAS`
**Owner:** Q-AIR · **Green overlay:** Q-GREENTECH (nodes `024-200` ⚡, `024-210` ⚡, `024-220` ⚡, `024-900`) · **Status:** agnostic standard (SSOT)

Inverted to green-native. Substituted ⚡: **AC Generation → Primary Power Generation** (`024-200`), **Generator Drive (IDG) → Generation-Source Drive & Conditioning** (`024-210`, IDG fully footprinted), **APU AC Generation → Auxiliary Power Generation** (`024-220`). Green delta `024-900` adds the **HVDC systems-power architecture & power electronics**. Distribution, breakers, batteries, external power, converters/inverters, and outlets carry forward. The propulsion HVDC bus and traction inverters are **not** here — they live in the propulsion band `070-079`. See the master-range [`README.md`](../README.md) for the full node register and conventions.

## Section-nodes

- [`024-000_General`](024-000_General/)
- [`024-010_Multi-System-Harness-01`](024-010_Multi-System-Harness-01/)
- [`024-020_Multi-System-Harness-02`](024-020_Multi-System-Harness-02/)
- [`024-030_Wing-Harness`](024-030_Wing-Harness/)
- [`024-200_Primary-Power-Generation`](024-200_Primary-Power-Generation/) ⚡
- [`024-210_Generation-Source-Drive-and-Conditioning`](024-210_Generation-Source-Drive-and-Conditioning/) ⚡
- [`024-220_Auxiliary-Power-Generation`](024-220_Auxiliary-Power-Generation/) ⚡
- [`024-230_Emergency-Backup-Power`](024-230_Emergency-Backup-Power/)
- [`024-240_Power-Electronics-Inversion`](024-240_Power-Electronics-Inversion/)
- [`024-250_AC-Conversion`](024-250_AC-Conversion/)
- [`024-300_DC-Power-Sourcing`](024-300_DC-Power-Sourcing/)
- [`024-310_DC-Rectification`](024-310_DC-Rectification/)
- [`024-330_DC-DC-Conversion`](024-330_DC-DC-Conversion/)
- [`024-360_Aircraft-Energy-Storage`](024-360_Aircraft-Energy-Storage/)
- [`024-400_External-Ground-Power`](024-400_External-Ground-Power/)
- [`024-410_External-DC-Power`](024-410_External-DC-Power/)
- [`024-420_External-AC-Power`](024-420_External-AC-Power/)
- [`024-500_AC-Electrical-Load-Distribution`](024-500_AC-Electrical-Load-Distribution/)
- [`024-510_AC-Power-Distribution`](024-510_AC-Power-Distribution/)
- [`024-520_AC-Circuit-Breakers`](024-520_AC-Circuit-Breakers/)
- [`024-540_AC-Electrical-Outlets`](024-540_AC-Electrical-Outlets/)
- [`024-600_DC-Electrical-Load-Distribution`](024-600_DC-Electrical-Load-Distribution/)
- [`024-610_DC-Power-Distribution`](024-610_DC-Power-Distribution/)
- [`024-640_DC-Circuit-Breakers`](024-640_DC-Circuit-Breakers/)
- [`024-660_DC-Electrical-Outlets`](024-660_DC-Electrical-Outlets/)
- [`024-900_High-Voltage-DC-Systems-Power-Architecture`](024-900_High-Voltage-DC-Systems-Power-Architecture/) [G]
