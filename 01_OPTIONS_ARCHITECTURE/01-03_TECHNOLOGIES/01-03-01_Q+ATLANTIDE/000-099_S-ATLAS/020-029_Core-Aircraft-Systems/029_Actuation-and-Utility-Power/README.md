# 029 — Actuation and Utility Power

**Chapter:** `029` ⇄ ATA **29**
**Master range:** `020-029_Core-Aircraft-Systems` · **Band:** `000-099_S-ATLAS`
**Owner:** Q-AIR · **Green overlay:** Q-GREENTECH (nodes `029-000` ⚡, `029-100` ⚡, `029-110` ⚡, `029-120` ⚡, `029-900` [G]) · **Status:** agnostic standard (SSOT)
**Version:** 1.0 · **Heritage:** ATA breakdown, Embraer 170/175/190/195 and Lineage 1000 (chapter 29 Hydraulic Power)

Conventional ATA-29 is entirely centralized hydraulics. Once flight-control actuation electrifies (`027-900` EHA/EMA) and landing-gear/brake actuation follows, the centralized hydraulic power system is largely eliminated. Green-native, actuation and utility power is drawn distributed-electric from the HVDC bus (`024-900`). The substituted ⚡ sections (`029-000`, `029-100`, `029-110`, `029-120`) retain agnostic titles; programmes that keep residual hydraulics bind those sections to that hardware. Green delta `029-900` carries the distributed-electric actuation and utility power architecture. Indicating nodes (`029-300`, `029-310`, `029-320`, `029-330`) and ground-service connections (`029-130`) are energy-neutral and carry forward. See the master-range [`README.md`](../README.md) and [`028-029_Green-Native-Breakdown.md`](../028-029_Green-Native-Breakdown.md) for full context.

**Numbering map:** `ATA CC-SS-UU → S-ATLAS 0CC-SS0-UU0` (e.g. `29-11-08 → 029-110-080`)

## Section-nodes

- [`029-000_General`](029-000_General/) ⚡ — General — Actuation and Utility Power | STD
- [`029-100_Main-Power-Generation`](029-100_Main-Power-Generation/) ⚡ — Main power generation (was main hydraulic power) | STD
- [`029-110_Primary-Power-Systems`](029-110_Primary-Power-Systems/) ⚡ — Primary power systems (was No.1/No.2 hydraulic) | STD
- [`029-120_Tertiary-Power-System`](029-120_Tertiary-Power-System/) ⚡ — Tertiary power system (was No.3 hydraulic) | STD
- [`029-130_Ground-Service-Connections`](029-130_Ground-Service-Connections/) — Ground-service connections | STD
- [`029-300_Indicating`](029-300_Indicating/) — Indicating | STD
- [`029-310_Pressure-State-Indicating`](029-310_Pressure-State-Indicating/) — Pressure / state indicating | STD
- [`029-320_Quantity-Indicating`](029-320_Quantity-Indicating/) — Quantity indicating | STD
- [`029-330_Temperature-Indicating`](029-330_Temperature-Indicating/) — Temperature indicating | STD
- [`029-900_Distributed-Electric-Actuation-and-Utility-Power`](029-900_Distributed-Electric-Actuation-and-Utility-Power/) [G] — **Distributed Electric Actuation and Utility Power**
