# 031 — Indicating and Recording Systems

**Chapter:** `031` ⇄ ATA **31**
**Master range:** `030-039_Protection-and-Mechanical-Systems` · **Band:** `000-099_G-ATLAS`
**Owner:** Q-AIR · **Data owner (`031-900`):** Q-DATAGOV · **Green overlay:** Q-GREENTECH (node `031-900`; ◇ surfaces `031-300`, `031-500`, `031-600`) · **Status:** agnostic standard (SSOT)

Panels, instruments, recorders, central computers, warning, and displays are energy-neutral electronics that carry whole (like Communications `023`). The green content is additive: the indicating/recording must now show and log the energy state (SoC/SoH), HV bus status, and thermal state, and carry new CAS messages for energy/HV/thermal faults — captured by the green delta `031-900`. The ◇ sections (recorders, warning, display) are the surfaces through which the delta appears; the hardware itself is unchanged. See the master-range [`README.md`](../README.md) for the full node register, doctrine, and heritage footprint.

## Section-nodes

- [`031-000_General`](031-000_General/)
- [`031-100_Instrument-and-Control-Panels`](031-100_Instrument-and-Control-Panels/)
- [`031-110_Main-Panel`](031-110_Main-Panel/)
- [`031-120_Glareshield-Panel`](031-120_Glareshield-Panel/)
- [`031-130_Lighting-Panel`](031-130_Lighting-Panel/)
- [`031-140_Pedestal-Panel`](031-140_Pedestal-Panel/)
- [`031-150_Overhead-Panel`](031-150_Overhead-Panel/)
- [`031-160_Circuit-Breaker-Panel`](031-160_Circuit-Breaker-Panel/)
- [`031-170_Multifunction-Panel`](031-170_Multifunction-Panel/)
- [`031-200_Independent-Instruments`](031-200_Independent-Instruments/)
- [`031-210_Clock`](031-210_Clock/)
- [`031-220_Chronometer`](031-220_Chronometer/)
- [`031-300_Recorders`](031-300_Recorders/) ◇
- [`031-310_Digital-Voice-Data-Recorder`](031-310_Digital-Voice-Data-Recorder/)
- [`031-320_Quick-Access-Recorder`](031-320_Quick-Access-Recorder/)
- [`031-400_Central-Computers`](031-400_Central-Computers/)
- [`031-410_Modular-Avionics-Unit`](031-410_Modular-Avionics-Unit/)
- [`031-420_ASCB-Bus`](031-420_ASCB-Bus/)
- [`031-430_General-Purpose-A429-Bus`](031-430_General-Purpose-A429-Bus/)
- [`031-500_Central-Warning`](031-500_Central-Warning/) ◇
- [`031-510_Aural-Warning`](031-510_Aural-Warning/)
- [`031-520_Master-Warning-Caution`](031-520_Master-Warning-Caution/)
- [`031-530_Visual-Warning-Function-CAS`](031-530_Visual-Warning-Function-CAS/)
- [`031-600_Central-Display`](031-600_Central-Display/) ◇
- [`031-610_Displays`](031-610_Displays/)
- [`031-620_Cursor-Control`](031-620_Cursor-Control/)
- [`031-900_Energy-System-Indicating-and-Recording`](031-900_Energy-System-Indicating-and-Recording/) [G]
