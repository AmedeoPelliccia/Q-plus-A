#!/usr/bin/env python3
"""Scaffold the S-ATLAS 070-079 electric and hybrid-electric range."""

import argparse
import sys
from pathlib import Path

RANGE = "070-079"
RANGE_TITLE = "Electric-and-Hybrid-Electric-Propulsion"
BAND_REL = (
    "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
    "000-099_S-ATLAS"
)
RANGE_SCOPE = (
    "Electric drivetrains and their architectures: motors, drives, distributed "
    "propulsion, battery-electric and hybrid-electric integration, and "
    "fuel-cell-electric powertrains (electrochemical source, electric drive). "
    "060-069 owns the combustion machine and turbogenerator set; this range "
    "owns the hybrid architecture, energy-management logic, drivetrain and "
    "propulsor integration."
)
RANGE_DIAGRAM = """```mermaid
flowchart LR
  subgraph SRC["Energy sources"]
    C074["074 Propulsion<br/>Energy Storage"]
    C075["075 Fuel-Cell-Electric<br/>Powertrains"]
    EXT["068 Turbogenerator sets<br/>(060-069)"]
  end
  SRC --> C076["076 Propulsion Power<br/>Distribution & Protection"]
  C076 --> C073["073 Power Electronics<br/>& Conversion"]
  C073 --> C072["072 Electric Machines"]
  C072 --> C077["077 Electric Propulsors &<br/>Distributed Integration"]
  C071["071 Architectures &<br/>Energy Management"] -. "supervises" .-> SRC
  C071 -. "supervises" .-> C076
  C078["078 Thermal Management"] --- SRC
  C078 --- C073
  C079["079 HV Safety &<br/>System Evidence"] --- C076
```"""

_NAMES = {
    "070": ("General-and-Range-Doctrine", [
        "Range-Scope-and-Doctrine", "Electric-Propulsion-Classes-Overview",
        "Commonality-and-Modularity-Principles", "Safety-and-Certification-Framework",
        "Environmental-Performance-Doctrine", "Interfaces-to-Aircraft-Systems",
        "Standard-Practices-Electric-Propulsion", "Testing-and-Evidence-Framework",
        "Glossary-and-Controlled-Vocabulary"]),
    "071": ("Propulsion-Architectures-and-Energy-Management", [
        "Battery-Electric-Architectures", "Series-Hybrid-and-Turboelectric-Architectures",
        "Parallel-and-Mixed-Hybrid-Architectures", "Fuel-Cell-Hybrid-Architectures",
        "Energy-Management-Strategies", "Power-Allocation-and-Sizing",
        "Degraded-Modes-and-Reversion", "Supervisory-Control-and-Monitoring",
        "Architecture-Evidence"]),
    "072": ("Electric-Machines-for-Propulsion", [
        "Machine-Topologies", "Windings-and-Insulation-Systems", "Magnetics-and-Materials",
        "Bearings-and-Mechanical-Integration", "Machine-Cooling-Interfaces",
        "Machine-Control-Interfaces", "Generators-for-Hybrid-Sets",
        "Advanced-Machine-Concepts", "Machine-Evidence"]),
    "073": ("Power-Electronics-and-Conversion", [
        "Inverter-Architectures", "Converter-and-Rectifier-Systems",
        "Switching-Devices-and-Modules", "Gate-Drive-and-Control", "EMI-EMC-and-Filtering",
        "Power-Electronics-Cooling-Interfaces", "Fault-Behavior-and-Protection-Coordination",
        "Altitude-and-Environmental-Effects", "Power-Electronics-Evidence"]),
    "074": ("Propulsion-Energy-Storage-Systems", [
        "Pack-Architectures", "Battery-Management-Systems", "Thermal-Runaway-Containment",
        "Crashworthiness-and-Structural-Integration", "Charging-and-Ground-Energy-Interfaces",
        "State-Estimation-and-Health", "Storage-Thermal-Conditioning",
        "Alternative-Storage-Integration", "Storage-Evidence"]),
    "075": ("Fuel-Cell-Electric-Powertrains", [
        "Stack-Integration-Architectures", "Balance-of-Plant-Air-Systems",
        "Balance-of-Plant-Hydrogen-Handling", "Water-and-Humidity-Management",
        "Fuel-Cell-Thermal-Integration", "Power-Conditioning-Interface",
        "Start-Stop-and-Freeze-Management", "Stack-Health-and-Degradation",
        "Fuel-Cell-Powertrain-Evidence"]),
    "076": ("Propulsion-Power-Distribution-and-Protection", [
        "HV-Network-Architectures", "Cables-Connectors-and-Busbars",
        "Contactors-and-Switching", "Protection-and-Fault-Isolation",
        "Insulation-Coordination-and-Monitoring", "Grounding-Bonding-and-Returns",
        "Interface-to-Aircraft-Electrical-Network", "Arc-Fault-Management",
        "Distribution-Evidence"]),
    "077": ("Electric-Propulsors-Installation-and-Distributed-Integration", [
        "Ducted-Fan-Propulsor-Units", "Open-Propeller-Electric-Units",
        "Distributed-Propulsion-Arrays", "Boundary-Layer-Ingestion-Integration",
        "Propulsor-Structural-Installation", "Propulsor-Acoustic-Characteristics",
        "Propulsor-Control-and-Pitch-Systems", "Ice-Protection-Interfaces",
        "Propulsor-Evidence"]),
    "078": ("Thermal-Management-of-Electric-Propulsion", [
        "Thermal-Architecture-and-Budgets", "Liquid-Cooling-Systems",
        "Air-and-Two-Phase-Cooling", "Cold-Plates-and-Heat-Exchangers",
        "Waste-Heat-Recovery-and-Reuse", "Cryogenic-Thermal-Synergies",
        "Thermal-Control-and-Monitoring", "Extreme-Ambient-Operation",
        "Thermal-Evidence"]),
    "079": ("High-Voltage-Safety-and-System-Evidence", [
        "HV-Safety-Doctrine-and-Zones", "Interlocks-and-Safe-Isolation",
        "Maintenance-Safety-Provisions", "Lightning-and-HIRF-Aspects-of-HV-Systems",
        "Failure-Containment-and-Segregation", "Emergency-Provisions-and-First-Response",
        "System-Level-Verification-Approach", "Integrated-Test-and-Iron-Bird-Evidence",
        "Range-Evidence-Index"]),
}
CH = {
    chapter: (title, [("000", "General-Information")] +
              [(f"{i * 100:03d}", section) for i, section in enumerate(sections, 1)])
    for chapter, (title, sections) in _NAMES.items()
}
BOUNDARIES = (
    "Machine split: combustion machines and turbogenerator sets are 060-069 "
    "(068); this range owns architectures, energy management, drivetrains and "
    "propulsor integration; electric-machine technology including hybrid-set "
    "generators is 072, consumed by 068 set integration. Aircraft electrical "
    "network and general storage: 024 — the propulsion HV network interfaces "
    "it at declared points (076-700). Propulsion energy storage doctrine: 074 "
    "is propulsion-side energy handling (the electric analogue of 064); cell "
    "and stack technology is EPTA (420s, 460s); hydrogen storage and "
    "distribution is 028, entering fuel-cell powertrains at the declared "
    "interface (075-300); charging follows the split doctrine — function 074, "
    "ground operation 010-019. Thermal-runaway three-layer analogue: 074-300 "
    "contains the system condition; 026 owns the aircraft-level hazard; "
    "atmosphere response per 047. Ice protection: 030 owns the function; "
    "077-800 declares the interfaces. Noise: propulsor source noise is 077-600; "
    "combustion source noise is 067-600. Frontier machine concepts cross-reference "
    "080-089 maturity classes. Waste-heat reuse coordinates with 021; crew "
    "alerting presentation with the flight-deck indicating chapters; hosted "
    "supervisory functions via 042-400."
)


def validate_schema():
    expected = [f"{number:03d}" for number in range(70, 80)]
    if list(CH) != expected:
        raise ValueError(f"Expected chapters {expected}, got {list(CH)}")
    sections = [f"{number * 100:03d}" for number in range(10)]
    for chapter, (_, values) in CH.items():
        if [code for code, _ in values] != sections:
            raise ValueError(f"Chapter {chapter}: invalid section sequence")


def range_readme():
    lines = [f"# {RANGE}_{RANGE_TITLE}", "", f"**Band:** 000-099_S-ATLAS · **Range:** {RANGE}",
             "", "## Scope (ratified)", "", RANGE_SCOPE, "", "## Chapter map", "",
             RANGE_DIAGRAM, "", "## Chapter register", "", "| Chapter | Title | Folder |",
             "|---|---|---|"]
    lines.extend(f"| {code} | {title.replace('-', ' ')} | <a>{code}</a> |"
                 for code, (title, _) in CH.items())
    lines += ["", "## Boundary summary", "", BOUNDARIES, "",
              "*Section registers are PROPOSED; ratification by merge. Subjects are "
              "scaffolded as General-Information plus reserved slots and are authored "
              "per work package.*", ""]
    return "\n".join(lines)


def chapter_readme(chapter, title, sections):
    lines = [f"# {chapter}_{title}", "",
             f"**Range:** {RANGE}_{RANGE_TITLE} · **Chapter:** {chapter}", "",
             "## Section register (PROPOSED)", "", "| Section | Title | Folder |",
             "|---|---|---|"]
    lines.extend(f"| {section} | {title.replace('-', ' ')} | <a>{chapter}-{section}</a> |"
                 for section, title in sections)
    lines += ["", "*Status: scaffolded. Section content and subject titles are authored "
              "per work package; registers ratified by merge.*", ""]
    return "\n".join(lines)


def section_readme(chapter, section, title):
    return (f"# {chapter}-{section} — {title.replace('-', ' ')}\n\n"
            f"**Chapter:** {chapter} · **Section:** {section} · **Status:** scaffolded\n\n"
            "Scope, subjects and graphics are authored per work package. Subject "
            "000 carries general information; slots 001-009 are reserved.\n")


def subject_stub(chapter, section, number, reserved):
    code = f"{chapter}-{section}-{number}"
    if reserved:
        return f"# {code} — Reserved\n\nReserved subject slot — title and content assigned at authoring per work package.\n"
    return (f"# {code} — General Information\n\n**Section:** {chapter}-{section} · "
            "**Subject:** 000\n\nGeneral information for this section — authored per work package.\n")


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--no-subjects", action="store_true")
    parser.add_argument("--bootstrap", action="store_true",
                        help="allow creating the tree when the Q+ATLANTIDE anchor is absent")
    args = parser.parse_args(argv)
    validate_schema()
    root = Path(args.root).resolve()
    anchor = root / "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE"
    if not anchor.is_dir() and not args.bootstrap:
        parser.error(f"Q+ATLANTIDE root not found under {root}; use --root or --bootstrap")
    range_dir = root / BAND_REL / f"{RANGE}_{RANGE_TITLE}"
    plan = [(range_dir / "README.md", range_readme(), True)]
    for chapter, (title, sections) in CH.items():
        chapter_dir = range_dir / f"{chapter}_{title}"
        plan.append((chapter_dir / "README.md", chapter_readme(chapter, title, sections), True))
        for section, section_title in sections:
            section_dir = chapter_dir / f"{chapter}-{section}_{section_title}"
            plan.append((section_dir / "README.md", section_readme(chapter, section, section_title), False))
            if not args.no_subjects:
                plan.append((section_dir / f"{chapter}-{section}-000_General-Information/README.md",
                             subject_stub(chapter, section, "000", False), False))
                for number in range(1, 10):
                    plan.append((section_dir / f"{chapter}-{section}-00{number}_Reserved/README.md",
                                 subject_stub(chapter, section, f"00{number}", True), False))
    written = skipped = 0
    for path, content, always in plan:
        should_write = not path.exists() or always or args.overwrite
        if args.dry_run:
            written += should_write
            skipped += not should_write
        elif should_write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content + ("" if content.endswith("\n") else "\n"), encoding="utf-8")
            written += 1
        else:
            skipped += 1
    mode = "dry-run" if args.dry_run else RANGE
    print(f"[{mode}] written={written} skipped={skipped} planned={len(plan)} at {range_dir}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        sys.exit(0)
