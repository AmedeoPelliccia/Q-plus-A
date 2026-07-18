# 027 — Flight Controls

**Chapter:** `027` ⇄ ATA **27**
**Master range:** `020-029_Core-Aircraft-Systems` · **Band:** `000-099_S-ATLAS`
**Owner:** Q-AIR · **Green overlay:** Q-GREENTECH (nodes `027-120` ⚡, `027-220` ⚡, `027-320` ⚡, `027-620` ⚡, `027-650` ⚡, `027-680` ⚡, `027-900` [G]) · **Status:** agnostic standard (SSOT)
**Version:** 1.0 · **Heritage:** ATA breakdown, Embraer 170/175/190/195 and Lineage 1000 (chapter 27)

Flight controls carry surfaces, mechanical components, sensors, trim, stall protection, fly-by-wire electronics, and flap/slat mechanics forward unchanged (energy-neutral). The six hydraulic-actuation sections are substituted ⚡ by agnostic **powered actuation** nodes (programme binds hydraulic or EHA/EMA). **Green delta `027-900`** adds the more-electric EHA/EMA architecture; actuator power is drawn from the HVDC bus in `024-900`. See the master-range [`README.md`](../README.md) for conventions.

**Numbering map:** `ATA CC-SS-UU → S-ATLAS 0CC-SS0-UU0` (e.g. `27-32-02 → 027-320-020`)

## Section-nodes

- [`027-000_General`](027-000_General/) — General — Flight Controls (+ electrical harness, FLT CTRL fault) | STD
- [`027-030_Flight-Controls-Electrical-System`](027-030_Flight-Controls-Electrical-System/) — Flight-controls electrical system — FCM, primary actuator-control electronics, trim panel, fly-by-wire backup battery, FCS power/backup relays | STD
- [`027-100_Aileron`](027-100_Aileron/) — Aileron | STD
- [`027-110_Aileron-Mechanical-Components`](027-110_Aileron-Mechanical-Components/) — Aileron mechanical components — yoke, cable, feel unit, torque tube, sectors, surface, pulley, override, disconnect | STD
- [`027-120_Aileron-Powered-Actuation`](027-120_Aileron-Powered-Actuation/) ⚡ — **Aileron powered actuation**
- [`027-130_Aileron-Electrical-System`](027-130_Aileron-Electrical-System/) — Aileron electrical system — surface position sensor | STD
- [`027-140_Aileron-Trim`](027-140_Aileron-Trim/) — Aileron trim — actuator | STD
- [`027-200_Rudder`](027-200_Rudder/) — Rudder | STD
- [`027-210_Rudder-Mechanical-Components`](027-210_Rudder-Mechanical-Components/) — Rudder mechanical components — pedal assembly, damper, feel unit, surface | STD
- [`027-220_Rudder-Powered-Actuation`](027-220_Rudder-Powered-Actuation/) ⚡ — **Rudder powered actuation**
- [`027-230_Rudder-Electrical-System`](027-230_Rudder-Electrical-System/) — Rudder electrical system — pedal/surface position sensors, pedal adjustment actuator, hinge-moment limiter relays | STD
- [`027-240_Rudder-Trim`](027-240_Rudder-Trim/) — Rudder trim — actuator | STD
- [`027-300_Elevator`](027-300_Elevator/) — Elevator | STD
- [`027-310_Elevator-Mechanical-Components`](027-310_Elevator-Mechanical-Components/) — Elevator mechanical components — control column, damper, feel unit, torque tube, surface, disconnect, rod assy | STD
- [`027-320_Elevator-Powered-Actuation`](027-320_Elevator-Powered-Actuation/) ⚡ — **Elevator powered actuation**
- [`027-330_Elevator-Electrical-System`](027-330_Elevator-Electrical-System/) — Elevator electrical system — position sensors, thrust compensation, tail-strike avoidance | STD
- [`027-360_Stall-Warning-and-Protection`](027-360_Stall-Warning-and-Protection/) — Stall warning and protection — stick shaker, stick pusher | STD
- [`027-400_Horizontal-Stabilizer`](027-400_Horizontal-Stabilizer/) — Horizontal stabilizer | STD
- [`027-410_Horizontal-Stabilizer-Mechanical-Components`](027-410_Horizontal-Stabilizer-Mechanical-Components/) — Horizontal-stabilizer mechanical components — trim actuator, surface, auto-config trim | STD
- [`027-430_Horizontal-Stabilizer-Electrical-System`](027-430_Horizontal-Stabilizer-Electrical-System/) — Horizontal-stabilizer electrical system — actuator control electronics, pitch-trim switch, actuator motor assembly | STD
- [`027-500_Flap`](027-500_Flap/) — Flap | STD
- [`027-510_Flap-Mechanical-Drive-Line`](027-510_Flap-Mechanical-Drive-Line/) — Flap mechanical drive line — actuator, angle gearbox, torque tube, bearing support, power-drive unit, panels, rollers, skew | STD
- [`027-530_Flap-Electrical-System`](027-530_Flap-Electrical-System/) — Flap electrical system — slat/flap control-lever unit, actuator control electronic unit, electric motor, position/skew sensors | STD
- [`027-600_Spoilers-and-Air-Brakes`](027-600_Spoilers-and-Air-Brakes/) — Spoilers and air brakes | STD
- [`027-610_Ground-Spoiler-Mechanical-Components`](027-610_Ground-Spoiler-Mechanical-Components/) — Ground-spoiler mechanical components — panel sections, proximity-sensor target | STD
- [`027-620_Ground-Spoiler-Powered-Actuation`](027-620_Ground-Spoiler-Powered-Actuation/) ⚡ — **Ground-spoiler powered actuation**
- [`027-630_Ground-Spoiler-Electrical-System`](027-630_Ground-Spoiler-Electrical-System/) — Ground-spoiler electrical system — proximity sensor | STD
- [`027-640_Multifunction-Spoiler-Mechanical-Components`](027-640_Multifunction-Spoiler-Mechanical-Components/) — Multifunction-spoiler mechanical components — panel sections | STD
- [`027-650_Multifunction-Spoiler-Powered-Actuation`](027-650_Multifunction-Spoiler-Powered-Actuation/) ⚡ — **Multifunction-spoiler powered actuation**
- [`027-660_Multifunction-Spoiler-Electrical-System`](027-660_Multifunction-Spoiler-Electrical-System/) — Multifunction-spoiler electrical system — yoke position sensor, speed-brake handle | STD
- [`027-670_Ventral-Air-Brake-Mechanical-Components`](027-670_Ventral-Air-Brake-Mechanical-Components/) — Ventral-air-brake mechanical components — panel | STD
- [`027-680_Ventral-Air-Brake-Powered-Actuation`](027-680_Ventral-Air-Brake-Powered-Actuation/) ⚡ — **Ventral-air-brake powered actuation**
- [`027-690_Ventral-Air-Brake-Electrical-System`](027-690_Ventral-Air-Brake-Electrical-System/) — Ventral-air-brake electrical system — position sensor, command wrap relay | STD
- [`027-800_Slat`](027-800_Slat/) — Slat | STD
- [`027-810_Slat-Mechanical-Components`](027-810_Slat-Mechanical-Components/) — Slat mechanical components — actuator, angle gearbox, torque tube, bearing support, panels, power-drive unit, skew | STD
- [`027-830_Slat-Electrical-System`](027-830_Slat-Electrical-System/) — Slat electrical system — skew sensors, electric motor, position-sensor unit, harness | STD
- [`027-900_More-Electric-Flight-Control-Actuation`](027-900_More-Electric-Flight-Control-Actuation/) [G] — **More-Electric Flight-Control Actuation**
