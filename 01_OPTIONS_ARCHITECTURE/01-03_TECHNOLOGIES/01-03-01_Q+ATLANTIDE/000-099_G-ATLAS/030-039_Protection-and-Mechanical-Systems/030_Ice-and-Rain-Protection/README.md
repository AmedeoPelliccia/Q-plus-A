# 030 — Ice and Rain Protection

**Chapter:** `030` ⇄ ATA **30**
**Master range:** `030-039_Protection-and-Mechanical-Systems` · **Band:** `000-099_G-ATLAS`
**Owner:** Q-AIR · **Green overlay:** Q-GREENTECH (nodes `030-100` ⚡, `030-110` ⚡, `030-200` ⚡, `030-210` ⚡, `030-900`) · **Status:** agnostic standard (SSOT)

The function — keep surfaces and probes ice-free — carries; the *source* of two systems diverges. Wing thermal anti-icing (`030-100`) and propulsion-module inlet anti-icing (`030-200`) are conventionally bleed-air; with no engine bleed they become ⚡ electrothermal, powered from the HVDC bus, and all bleed hardware drops to footprint. Pitot/static/AOA heating, windshield/door heating, water-line freeze protection, and ice detection are already electric and carry (STD). Thermal integration / bleedless content is captured by the green delta `030-900`. See the master-range [`README.md`](../README.md) for the full node register, doctrine, and heritage footprint.

## Section-nodes

- [`030-000_General`](030-000_General/)
- [`030-100_Airfoil-Anti-Ice`](030-100_Airfoil-Anti-Ice/) ⚡
- [`030-110_Wing-Anti-Ice-Electrothermal`](030-110_Wing-Anti-Ice-Electrothermal/) ⚡
- [`030-200_Propulsion-Module-Inlet-Anti-Ice`](030-200_Propulsion-Module-Inlet-Anti-Ice/) ⚡
- [`030-210_Propulsion-Module-Anti-Ice-Electric`](030-210_Propulsion-Module-Anti-Ice-Electric/) ⚡
- [`030-300_Pitot-and-Static`](030-300_Pitot-and-Static/)
- [`030-310_Integrated-Pitot-Static-AOA-Sensor-Heating`](030-310_Integrated-Pitot-Static-AOA-Sensor-Heating/)
- [`030-320_Static-Port-Heating`](030-320_Static-Port-Heating/)
- [`030-330_TAT-Sensor-Heating`](030-330_TAT-Sensor-Heating/)
- [`030-400_Windows-Windshields-and-Doors`](030-400_Windows-Windshields-and-Doors/)
- [`030-410_Windshield-Wiper`](030-410_Windshield-Wiper/)
- [`030-420_Windshield-Heating`](030-420_Windshield-Heating/)
- [`030-430_Passenger-Door-Heating`](030-430_Passenger-Door-Heating/)
- [`030-440_EFVS-Window-Heating`](030-440_EFVS-Window-Heating/)
- [`030-700_Water-Waste-Line-Freeze-Protection`](030-700_Water-Waste-Line-Freeze-Protection/)
- [`030-710_Potable-Water-Heating`](030-710_Potable-Water-Heating/)
- [`030-720_Grey-Water-Heating`](030-720_Grey-Water-Heating/)
- [`030-730_Recirculating-WSP-Valve-Heating`](030-730_Recirculating-WSP-Valve-Heating/)
- [`030-740_Vacuum-Waste-Heating`](030-740_Vacuum-Waste-Heating/)
- [`030-800_Ice-Detection`](030-800_Ice-Detection/)
- [`030-810_Ice-Detector`](030-810_Ice-Detector/)
- [`030-820_Super-Large-Droplet-Ice-Detector`](030-820_Super-Large-Droplet-Ice-Detector/)
- [`030-900_Bleedless-Energy-Integrated-Ice-Protection`](030-900_Bleedless-Energy-Integrated-Ice-Protection/) [G]
