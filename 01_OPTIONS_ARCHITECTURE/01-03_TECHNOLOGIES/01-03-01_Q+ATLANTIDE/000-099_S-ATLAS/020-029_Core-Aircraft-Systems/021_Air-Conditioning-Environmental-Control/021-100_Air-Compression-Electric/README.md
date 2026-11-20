# 021-100 ⚡ — Air Compression (Electric)

**Node:** `021-100` ⇄ ATA **21-10** (conventional: Compression — not in the heritage reference, whose air supply is bleed air)[^c-2110]
**Chapter:** `021_Air-Conditioning-Environmental-Control` · **Layer:** STD
**Owner:** Q-AIR · **Divergence node (⚡):** all subjects are G-subjects · **Green overlay:** Q-GREENTECH

The supply of compressed outside air to the cabin where no bleed air is taken: the compressors, their electric drive, their inlet and ducting, and their control. It is the green-native home of what a conventional aircraft takes from the pneumatic system (chapter `036`).

## Subjects

- [`021-100-010-Electrically-Driven-Air-Compressor.md`](021-100-010-Electrically-Driven-Air-Compressor.md) ⚡ — Electrically-driven air compressor [G-subject]
- [`021-100-030-Compressor-Drive-Motor-and-Motor-Controller.md`](021-100-030-Compressor-Drive-Motor-and-Motor-Controller.md) ⚡ — Compressor drive — motor and motor controller [G-subject]
- [`021-100-050-Outside-Air-Inlet-and-Compressor-Ducting.md`](021-100-050-Outside-Air-Inlet-and-Compressor-Ducting.md) ⚡ — Outside-air inlet and compressor ducting [G-subject]
- [`021-100-070-Compressor-Flow-and-Surge-Control.md`](021-100-070-Compressor-Flow-and-Surge-Control.md) ⚡ — Compressor flow and surge control [G-subject]
- [`021-100-090-Compression-Control-Sensors-and-Protection.md`](021-100-090-Compression-Control-Sensors-and-Protection.md) ⚡ — Compression-control sensors and protection [G-subject]

## Boundaries

- The interface of the air supply with the energy system — electrical supply, heat rejected — and process air for an energy source: [`021-900-070`](../021-900_Energy-System-Thermal-Integration/021-900-070-Bleedless-Air-Supply-Interface.md).
- The compressor of a cooling unit works on the cooling loop, not on the air supply: [`021-510-010`](../021-510_Environmental-Cooling-Unit-Electric/021-510-010-Electrically-Driven-Cooling-Compressor.md).
- Cooling and water extraction of the compressed air: `021-500` and `021-510`. Distribution: `021-200`. Cabin pressure control: `021-300`.
- Ozone conversion of the supply air migrates into this chapter from `036-300`; no subject is assigned to it yet.

[^c-2110]: **Conventional `21-10` — Compression.** In the ATA Spec 100 numbering, as the FAA JASC table carries it (code 2110, *Cabin Compressor System*), section 10 of chapter 21 is the system that supplies compressed air to the cabin. The breakdown transcribed from the heritage reference has no `21-10`: its air supply is engine and APU **bleed air**, chapter 36. Superseded green-native by outside air compressed by electrically-driven compressors.
