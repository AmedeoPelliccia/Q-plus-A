# 028 — Energy-Carrier Storage and Distribution

**Chapter:** `028` ⇄ ATA **28**
**Master range:** `020-029_Core-Aircraft-Systems` · **Band:** `000-099_G-ATLAS`
**Owner:** Q-GREENTECH · **Green overlay:** Q-GREENTECH (all sections ⚡ except `028-250`, `028-420`) · **Status:** agnostic standard (SSOT)
**Version:** 1.0 · **Heritage:** ATA breakdown, Embraer 170/175/190/195 and Lineage 1000 (chapter 28 Fuel)

This chapter is a **near-total substitution**: the functional skeleton of ATA 28 (Storage / Distribution / Indicating) is retained and re-expressed in energy-carrier-agnostic terms. Every fuel-specific section is substituted ⚡. Green delta `028-900` carries genuinely novel content with no fuel analogue: cell/module management, state-of-health monitoring, cryogenic boil-off control, charge/discharge protection, and thermal management interface. The conventional liquid-hydrocarbon fuel system is demoted to the heritage footprint. See the master-range [`README.md`](../README.md) and the companion breakdown [`028-029_Green-Native-Breakdown.md`](../028-029_Green-Native-Breakdown.md) for full context and numbering conventions.

**Numbering map:** `ATA CC-SS-UU → G-ATLAS 0CC-SS0-UU0` (e.g. `28-23-03 → 028-230-030`)

## Section-nodes

- [`028-000_General`](028-000_General/) ⚡ — General — Energy-Carrier Storage and Distribution | STD
- [`028-100_Energy-Carrier-Storage`](028-100_Energy-Carrier-Storage/) ⚡ — **Energy-Carrier Storage** | STD
- [`028-110_Primary-Storage-Unit`](028-110_Primary-Storage-Unit/) ⚡ — Primary storage unit (was wing tank) | STD
- [`028-120_Storage-Venting-Conditioning`](028-120_Storage-Venting-Conditioning/) ⚡ — Storage venting / conditioning (was tank vent) | STD
- [`028-130_Auxiliary-Storage-Unit`](028-130_Auxiliary-Storage-Unit/) ⚡ — Auxiliary storage unit (was auxiliary fuel tank) | STD
- [`028-140_Auxiliary-Storage-Venting-Conditioning`](028-140_Auxiliary-Storage-Venting-Conditioning/) ⚡ — Auxiliary storage venting / conditioning | STD
- [`028-200_Energy-Carrier-Distribution`](028-200_Energy-Carrier-Distribution/) ⚡ — **Energy-Carrier Distribution** | STD
- [`028-210_Propulsion-Feed-Delivery`](028-210_Propulsion-Feed-Delivery/) ⚡ — Propulsion feed / delivery (was engine feed) | STD
- [`028-220_Auxiliary-Power-Feed-Delivery`](028-220_Auxiliary-Power-Feed-Delivery/) ⚡ — Auxiliary-power feed / delivery (was APU feed) | STD
- [`028-230_Pressure-Replenishment`](028-230_Pressure-Replenishment/) ⚡ — Pressure replenishment (was pressure refueling) | STD
- [`028-240_Gravity-Manual-Replenishment`](028-240_Gravity-Manual-Replenishment/) ⚡ — Gravity / manual replenishment (was gravity refueling) | STD
- [`028-250_Energy-Pump-Converter-Wiring-Connectors`](028-250_Energy-Pump-Converter-Wiring-Connectors/) — Energy-pump / converter wiring & connectors | STD
- [`028-260_Energy-Transfer-and-Balancing`](028-260_Energy-Transfer-and-Balancing/) ⚡ — Energy transfer and balancing (was auxiliary fuel transfer) | STD
- [`028-400_Energy-Carrier-Quantity-and-State-Indication`](028-400_Energy-Carrier-Quantity-and-State-Indication/) ⚡ — **Energy-Carrier Quantity and State Indication** | STD
- [`028-410_Electrical-Quantity-State-Indication-SoC`](028-410_Electrical-Quantity-State-Indication-SoC/) ⚡ — Electrical quantity / state indication — SoC (was fuel-quantity-indicating) | STD
- [`028-420_Direct-Level-Indication`](028-420_Direct-Level-Indication/) — Direct level indication (was magnetic level) | STD
- [`028-430_Energy-Carrier-Temperature-Indication`](028-430_Energy-Carrier-Temperature-Indication/) ⚡ — Energy-carrier temperature indication | STD
- [`028-440_Low-Energy-Level-Warning`](028-440_Low-Energy-Level-Warning/) ⚡ — Low-energy-level warning (was fuel-low-level warning) | STD
- [`028-900_Energy-Carrier-Management`](028-900_Energy-Carrier-Management/) [G] — **Energy-Carrier Management (no fuel analogue)** · Safety-critical (couples to `026-900`)
