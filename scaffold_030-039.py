#!/usr/bin/env python3
"""
G-ATLAS scaffold generator — code range 030-039 (Protection and Mechanical Systems).
Chapters: 032 Landing Gear · 033 Lights · 034 Navigation · 035 Oxygen ·
          036 Pneumatic (vacated) · 037 Vacuum (vestigial).

Deterministic · idempotent · zero LLM. Sources of truth:
  032-033_G-ATLAS-Green-Native-Breakdown.md (v1.0)
  034-037_G-ATLAS-Green-Native-Breakdown.md (v1.0)

Usage:
    python3 scaffold_030-039.py              # run from repo root
    python3 scaffold_030-039.py /path/to/repo
Re-running is safe: existing files are skipped, never overwritten (top-up only).

Layer glyphs: STD carries · ⚡ source substitution · ◇ green overlay ·
              STD-G green delta · ∅ vacated (function migrated out of the chapter).
Note: 034-600 (FMS computing) is marked ◇ in the source prose but its Layer
      column reads STD; the Layer column is taken verbatim here.
"""
import re
import sys
from pathlib import Path

BAND       = "000-099_G-ATLAS"
CODE_RANGE = "030-039_Protection-and-Mechanical-Systems"
REL_ROOT   = Path("01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE") / BAND / CODE_RANGE

# (code, title, layer)
NODES = {
    "032_Landing-Gear": [
        ("032-000", "General — Landing Gear", "STD"),
        ("032-100", "Main Landing Gear and Doors", "STD"),
        ("032-110", "Main landing gear (structure)", "STD"),
        ("032-120", "Main-landing-gear doors", "STD"),
        ("032-200", "Nose Landing Gear and Doors", "STD"),
        ("032-210", "Nose landing gear (structure)", "STD"),
        ("032-220", "Nose-landing-gear doors", "STD"),
        ("032-300", "Extension and Retraction", "⚡"),
        ("032-310", "Main-gear extension/retraction — electric (EMA)", "⚡"),
        ("032-320", "Nose-gear extension/retraction — electric (EMA)", "⚡"),
        ("032-330", "Gear extension/retraction control", "⚡"),
        ("032-340", "Emergency (free-fall) extension", "STD"),
        ("032-350", "Emergency electrical-release", "STD"),
        ("032-400", "Wheels and Brakes", "⚡"),
        ("032-410", "Main brake — electric / brake-by-wire", "⚡"),
        ("032-440", "Emergency/parking brake — electric", "⚡"),
        ("032-470", "Brake-temperature monitoring", "STD"),
        ("032-490", "Wheels, brakes and tyres", "STD"),
        ("032-500", "Steering", "⚡"),
        ("032-520", "Steering hydraulic system → electric", "⚡"),
        ("032-530", "Steering electric/electronic (green-native primary)", "STD"),
        ("032-600", "Position and Warning", "STD"),
        ("032-610", "Landing-gear indicating", "STD"),
        ("032-620", "Air/ground (weight-on-wheels)", "STD"),
        ("032-630", "Warning", "STD"),
        ("032-900", "Electric Landing-Gear Actuation, Braking and Taxi", "STD-G"),
        ("032-900-010", "Electric gear actuation architecture", "G-subject"),
        ("032-900-030", "Electric braking", "G-subject"),
        ("032-900-050", "Electric nose-wheel steering integration", "G-subject"),
        ("032-900-070", "Gear and brake health monitoring", "G-subject"),
        ("032-900-090", "Electric-taxi (green taxiing) drive — optional", "G-subject"),
    ],
    "033_Lights": [
        ("033-000", "General — Lights", "STD"),
        ("033-100", "Flight-Deck Lights", "STD"),
        ("033-110", "Flight-deck lights", "STD"),
        ("033-120", "Instrument and panel lights", "STD"),
        ("033-150", "Flood / storm lights", "STD"),
        ("033-200", "Passenger-Cabin Lights", "STD"),
        ("033-210", "Cabin lights", "STD"),
        ("033-220", "Airstair lights", "STD"),
        ("033-230", "Warning signs", "STD"),
        ("033-240", "Attendant-call indicators", "STD"),
        ("033-250", "Reading lights", "STD"),
        ("033-260", "Courtesy lights", "STD"),
        ("033-270", "Wardrobe / stowage lights", "STD"),
        ("033-280", "Lavatory lights", "STD"),
        ("033-290", "Galley lights", "STD"),
        ("033-300", "Cargo and Service-Compartment Lights", "STD"),
        ("033-310", "Cargo-compartment lights", "STD"),
        ("033-320", "Service-compartment lights", "STD"),
        ("033-330", "Baggage-compartment lights", "STD"),
        ("033-400", "External Lights", "STD"),
        ("033-410", "Landing lights", "STD"),
        ("033-420", "Taxi lights", "STD"),
        ("033-430", "Navigation lights", "STD"),
        ("033-440", "Inspection lights", "STD"),
        ("033-450", "Red beacon", "STD"),
        ("033-460", "Logotype lights", "STD"),
        ("033-470", "Strobe lights", "STD"),
        ("033-500", "Emergency Lighting", "STD"),
        ("033-510", "Flashlight", "STD"),
        ("033-900", "LED-Native Lighting and Energy Management", "STD-G"),
        ("033-900-010", "LED-native lighting and efficiency", "G-subject"),
        ("033-900-030", "Lighting electrical-load management", "G-subject"),
        ("033-900-050", "Energy-independent emergency-egress marking (photoluminescent)", "G-subject"),
    ],
    "034_Navigation": [
        ("034-000", "General — Navigation", "STD"),
        ("034-010", "Navigation antennas", "STD"),
        ("034-020", "Modular radio cabinet (MRC / MMRC / NIM)", "STD"),
        ("034-100", "Flight Environment Data", "STD"),
        ("034-110", "Integrated electronic standby system", "STD"),
        ("034-130", "Integrated pitot/static/AOA system", "STD"),
        ("034-150", "Air-data computing (ADC, TAT)", "STD"),
        ("034-200", "Attitude and Direction", "STD"),
        ("034-230", "Standby compass", "STD"),
        ("034-250", "Head-up guidance system", "STD"),
        ("034-260", "Inertial reference system (micro IRU)", "STD"),
        ("034-270", "Enhanced flight vision system", "STD"),
        ("034-300", "Landing and Taxiing Aids", "STD"),
        ("034-310", "Radar altimeter", "STD"),
        ("034-320", "VHF nav (VOR/LOC, marker, glide slope)", "STD"),
        ("034-400", "Independent Position Determining", "STD"),
        ("034-410", "EGPWS / windshear", "STD"),
        ("034-420", "Weather radar", "STD"),
        ("034-430", "TCAS", "STD"),
        ("034-440", "Lightning sensor", "STD"),
        ("034-500", "Dependent Position Determining", "STD"),
        ("034-510", "DME", "STD"),
        ("034-520", "Transponder", "STD"),
        ("034-530", "ADF", "STD"),
        ("034-560", "GPS", "STD"),
        ("034-600", "Flight Management Computing", "STD"),
        ("034-610", "Flight management system", "STD"),
        ("034-900", "Energy-Aware Navigation and Flight Management", "STD-G"),
        ("034-900-010", "Energy-aware FMS — range/reserve from energy state", "G-subject"),
        ("034-900-030", "Energy-optimal trajectory optimization (green routing)", "G-subject"),
        ("034-900-050", "Electric-taxi navigation/guidance", "G-subject"),
    ],
    "035_Oxygen": [
        ("035-000", "General — Oxygen", "STD"),
        ("035-100", "Crew Oxygen (cylinder, charging valve, mask)", "STD"),
        ("035-110", "Crew control / indicating", "STD"),
        ("035-120", "Oxygen-cylinder-bay ventilation", "STD"),
        ("035-200", "Passenger-Cabin Oxygen (chemical generator / gaseous)", "STD"),
        ("035-210", "Passenger control / indicating", "STD"),
        ("035-220", "Passenger gaseous-oxygen system", "STD"),
        ("035-300", "Portable Oxygen (cylinder, mask, PBE)", "STD"),
        ("035-900", "Oxygen-System Integration Safety (thin)", "STD-G"),
        ("035-900-010", "Zonal segregation from hydrogen / high-voltage zones", "G-subject"),
    ],
    "036_Pneumatic": [
        ("036-000", "General — Pneumatic", "STD"),
        ("036-100", "Air-Bleed Distribution", "∅"),
        ("036-110", "Engine pneumatic bleed system", "∅"),
        ("036-120", "APU pneumatic bleed system", "∅"),
        ("036-130", "Ground air supply (HP)", "∅"),
        ("036-140", "Bleed control (overpressure, HPSOV)", "∅"),
        ("036-150", "Water-tank pressurization → electric (migrates)", "⚡"),
        ("036-200", "Pneumatic Indicating (bleed-leak detection)", "∅"),
        ("036-300", "Ozone converters → on electric ECS air (migrates to 021)", "⚡"),
        ("036-900", "Bleedless Architecture and Function Migration", "STD-G"),
        ("036-900-010", "Bleedless doctrine — no engine/APU bleed offtake", "G-subject"),
        ("036-900-030", "Function-migration map", "G-subject"),
        ("036-900-050", "Residual dedicated pneumatic provision (electric, if any)", "G-subject"),
    ],
    "037_Vacuum": [
        ("037-000", "General — Vacuum (vestigial)", "STD"),
        ("037-100", "Vacuum source (engine-driven pump)", "∅"),
        ("037-200", "Vacuum distribution", "∅"),
        ("037-300", "Vacuum indicating", "∅"),
        ("037-900", "Electric Vacuum Provision (if required)", "STD-G"),
        ("037-900-010", "Electric vacuum source for any residual need", "G-subject"),
        ("037-900-030", "Vacuum-waste motive — cross-ref to water/waste 038", "G-subject"),
    ],
}

def slug(title: str) -> str:
    return re.sub(r"[^0-9A-Za-z]+", "-", title).strip("-")

def stub(code: str, title: str, layer: str, node: str) -> str:
    return (
        "---\n"
        f'code: "{code}"\n'
        f'title: "{title}"\n'
        f'layer: "{layer}"\n'
        f'node: "{node}"\n'
        f'code_range: "{CODE_RANGE}"\n'
        f'band: "{BAND}"\n'
        "status: stub\n"
        'version: "0.1"\n'
        "---\n\n"
        f"# {code} — {title}\n\n"
        f"> Stub — content to be authored. Layer: **{layer}**.\n\n"
        "\n"
    )

def main() -> None:
    base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    root = base / REL_ROOT
    created = skipped = 0

    root.mkdir(parents=True, exist_ok=True)
    range_readme = root / "README.md"
    if not range_readme.exists():
        nodes_line = ", ".join(n.replace("_", " ") for n in NODES)
        range_readme.write_text(
            f"# {CODE_RANGE}\n\nCode-range index · band {BAND}.\nNodes: {nodes_line}.\n",
            encoding="utf-8")
        created += 1

    for node, items in NODES.items():
        ndir = root / node
        ndir.mkdir(parents=True, exist_ok=True)
        nreadme = ndir / "README.md"
        if not nreadme.exists():
            nreadme.write_text(f"# {node}\n\nNode index · {CODE_RANGE}.\n", encoding="utf-8")
            created += 1
        for code, title, layer in items:
            f = ndir / f"{code}-{slug(title)}.md"
            if f.exists():
                skipped += 1
                continue
            f.write_text(stub(code, title, layer, node), encoding="utf-8")
            created += 1

    print(f"done · created {created} · skipped {skipped}")

if __name__ == "__main__":
    main()
