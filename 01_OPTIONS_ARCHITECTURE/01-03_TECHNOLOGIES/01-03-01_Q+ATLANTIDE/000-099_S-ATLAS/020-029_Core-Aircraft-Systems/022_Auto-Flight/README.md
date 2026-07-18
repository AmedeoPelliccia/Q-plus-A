# 022 — Auto Flight

**Chapter:** `022` ⇄ ATA **22**
**Master range:** `020-029_Core-Aircraft-Systems` · **Band:** `000-099_S-ATLAS`
**Owner:** Q-AIR · **Green overlay:** Q-GREENTECH (nodes `022-300` ⚡, `022-310` ⚡) · **Status:** agnostic standard (SSOT)

Carries forward energy-neutral; the only light substitution is **Auto Throttle → Autothrust / Power Management** (`022-300/310`), renamed source-agnostic. FGCS, autopilot servos and cables are flight-control actuation and stay STD. See the master-range [`README.md`](../README.md) for the full node register and conventions.

## Section-nodes

- [`022-000_General`](022-000_General/)
- [`022-100_Autopilot`](022-100_Autopilot/)
- [`022-110_Flight-Guidance-and-Control-System`](022-110_Flight-Guidance-and-Control-System/)
- [`022-300_Autothrust-Power-Management`](022-300_Autothrust-Power-Management/) ⚡
- [`022-310_Autothrust-Function`](022-310_Autothrust-Function/) ⚡
