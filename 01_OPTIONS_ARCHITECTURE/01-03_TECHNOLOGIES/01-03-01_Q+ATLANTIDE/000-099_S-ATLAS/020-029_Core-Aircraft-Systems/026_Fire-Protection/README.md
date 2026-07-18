# 026 — Fire Protection

**Chapter:** `026` ⇄ ATA **26**
**Master range:** `020-029_Core-Aircraft-Systems` · **Band:** `000-099_G-ATLAS`
**Owner:** Q-AIR · **Green overlay:** Q-GREENTECH (nodes `026-110` ⚡, `026-120` ⚡, `026-210` ⚡, `026-220` ⚡, `026-900` [G]) · **Status:** agnostic standard (SSOT)
**Version:** 1.0 · **Heritage:** ATA breakdown, Embraer 170/175/190/195 and Lineage 1000 (chapter 26)

Fire protection has two distinct green divergences. **Detection:** smoke/overheat in cabin, lavatory, cargo, recirculation bay, landing-gear bay, and e-racks are energy-neutral and carry forward. Engine/APU detection is normalized ⚡ to propulsion-module / auxiliary-power-module overheat detection. **Extinguishing:** cargo/portable/lavatory/monument extinguishing carry forward; engine/APU extinguishing is normalized ⚡ and the agent diverges (gaseous Halon-type agents do not suppress lithium thermal runaway). **Green delta `026-900`** adds the energy-system fire tier — battery thermal runaway, hydrogen fire, HV arc-fault — with no ATA equivalent; flagged safety-critical. See the master-range [`README.md`](../README.md) for conventions.

**Numbering map:** `ATA CC-SS-UU → G-ATLAS 0CC-SS0-UU0` (e.g. `26-21-03 → 026-210-030`)

## Section-nodes

- [`026-000_General`](026-000_General/) — General — Fire Protection (+ system test switch) | STD
- [`026-100_Fire-Smoke-Detection`](026-100_Fire-Smoke-Detection/) — Fire / smoke detection — detector panel, sonoalert audible-signal device | STD
- [`026-110_Propulsion-Module-Fire-Overheat-Detection`](026-110_Propulsion-Module-Fire-Overheat-Detection/) ⚡ — **Propulsion-module fire / overheat detection**
- [`026-120_Auxiliary-Power-Module-Fire-Overheat-Detection`](026-120_Auxiliary-Power-Module-Fire-Overheat-Detection/) ⚡ — **Auxiliary-power-module fire / overheat detection**
- [`026-130_Passenger-Cabin-Smoke-Detection`](026-130_Passenger-Cabin-Smoke-Detection/) — Passenger-cabin smoke detection | STD
- [`026-140_Lavatory-Smoke-Detection`](026-140_Lavatory-Smoke-Detection/) — Lavatory smoke detection — detector, relay | STD
- [`026-150_Cargo-Compartment-Smoke-Detection`](026-150_Cargo-Compartment-Smoke-Detection/) — Cargo-compartment smoke detection | STD
- [`026-160_Recirculation-Bay-Smoke-Detection`](026-160_Recirculation-Bay-Smoke-Detection/) — Recirculation-bay smoke detection | STD
- [`026-170_Landing-Gear-Bay-Fire-Detection`](026-170_Landing-Gear-Bay-Fire-Detection/) — Landing-gear-bay fire detection | STD
- [`026-180_Electronic-Equipment-Rack-Smoke-Detection`](026-180_Electronic-Equipment-Rack-Smoke-Detection/) — Electronic-equipment-rack smoke detection — maintenance/test panel, cooling indicator | STD
- [`026-200_Fire-Extinguishing`](026-200_Fire-Extinguishing/) — Fire extinguishing — extinguisher panel | STD
- [`026-210_Propulsion-Module-Fire-Extinguishing`](026-210_Propulsion-Module-Fire-Extinguishing/) ⚡ — **Propulsion-module fire extinguishing**
- [`026-220_Auxiliary-Power-Module-Fire-Extinguishing`](026-220_Auxiliary-Power-Module-Fire-Extinguishing/) ⚡ — **Auxiliary-power-module fire extinguishing**
- [`026-230_Cargo-Compartment-Fire-Extinguishing`](026-230_Cargo-Compartment-Fire-Extinguishing/) — Cargo-compartment fire extinguishing — bottle (HR/LR), cartridge, drier metering unit, discharge tubing/nozzle, swept-tee, pushbutton, relay | STD
- [`026-240_Portable-Fire-Extinguishing`](026-240_Portable-Fire-Extinguishing/) — Portable fire extinguishing | STD
- [`026-250_Lavatory-Auto-Discharge-Fire-Extinguishing`](026-250_Lavatory-Auto-Discharge-Fire-Extinguishing/) — Lavatory auto-discharge fire extinguishing — bottle | STD
- [`026-260_Monument-Auto-Discharge-Fire-Extinguishing`](026-260_Monument-Auto-Discharge-Fire-Extinguishing/) — Monument auto-discharge fire extinguishing | STD
- [`026-900_Energy-System-Fire-Protection`](026-900_Energy-System-Fire-Protection/) [G] — **Energy-System Fire Protection** (safety-critical)
