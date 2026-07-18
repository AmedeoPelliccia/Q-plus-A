#!/usr/bin/env python3
"""Scaffold the S-ATLAS 060-069 sustainable combustion propulsion range."""

import argparse
import sys
from pathlib import Path

RANGE = "060-069"
RANGE_TITLE = "Sustainable-Energy-Carrier-Combustion-Propulsion"
BAND_REL = (
    "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
    "000-099_S-ATLAS"
)

RANGE_SCOPE = (
    "Turbomachinery, combustion devices and associated propulsion systems "
    "designed for sustainable energy carriers, including SAF-capable systems, "
    "hydrogen-combustion turbines, fuel-flexible combustors and turbogenerators "
    "used by hybrid-electric architectures."
)

RANGE_DIAGRAM = """```mermaid
flowchart TD
  subgraph CORE["Machine core"]
    C062["062 Turbomachinery"]
    C063["063 Combustion Systems"]
    C064["064 Carrier Delivery"]
    C065["065 Air & Thermal"]
  end
  C060["060 General & Doctrine"] --> CORE
  C061["061 Installation & Nacelle"] --- CORE
  C066["066 Control & Monitoring"] --- CORE
  C067["067 Exhaust, Emissions,<br/>Contrail Management"] --- CORE
  C068["068 Turbogenerators &<br/>Power Offtakes"] --- CORE
  C069["069 Lubrication, Ignition,<br/>Starting, Accessories"] --- CORE
  C068 -. "machine here;<br/>architecture in 070" .-> X070["070-079"]
```"""

# Chapter code -> (title, [(section code, title), ...])
CH = {
    "060": ("General-and-Range-Doctrine", [
        ("000", "General-Information"),
        ("100", "Range-Scope-and-Doctrine"),
        ("200", "Sustainable-Energy-Carriers-Overview"),
        ("300", "Commonality-and-Product-Line-Principles"),
        ("400", "Safety-and-Certification-Framework"),
        ("500", "Environmental-Performance-and-Non-CO2-Doctrine"),
        ("600", "Interfaces-to-Aircraft-Systems"),
        ("700", "Standard-Practices-Powerplant"),
        ("800", "Testing-and-Evidence-Framework"),
        ("900", "Glossary-and-Controlled-Vocabulary"),
    ]),
    "061": ("Powerplant-Installation-and-Nacelle-Integration", [
        ("000", "General-Information"),
        ("100", "Engine-Mounting-and-Structural-Interfaces"),
        ("200", "Nacelle-and-Cowling-Integration"),
        ("300", "Firewalls-and-Zone-Segregation"),
        ("400", "Drains-Vents-and-Leak-Management"),
        ("500", "Powerplant-Build-Up-and-Interchangeability"),
        ("600", "Vibration-Isolation-and-Dynamic-Interfaces"),
        ("700", "Access-and-Maintainability-Provisions"),
        ("800", "Installation-Aerodynamics-and-Integration-Effects"),
        ("900", "Ground-Handling-and-Transport-Interfaces"),
    ]),
    "062": ("Combustion-Machinery", [
        ("000", "General-Information"), ("100", "Compression-Systems"),
        ("200", "Turbine-Systems"), ("300", "Shafts-Bearings-and-Rotordynamics"),
        ("400", "Sealing-Systems"), ("500", "Rotor-Integrity-and-Containment"),
        ("600", "Materials-and-Coatings-for-Carrier-Compatibility"),
        ("700", "Clearance-Control-and-Tip-Management"),
        ("800", "Reciprocating-and-Rotary-Combustion-Machines"),
        ("900", "Turbomachinery-Health-Characteristics"),
    ]),
    "063": ("Combustion-Systems-for-Sustainable-Carriers", [
        ("000", "General-Information"),
        ("100", "Fuel-Flexible-Combustor-Architectures"),
        ("200", "Hydrogen-Combustion-Systems"),
        ("300", "SAF-Combustion-and-Compatibility"),
        ("400", "Injection-Mixing-and-Flame-Stabilization"),
        ("500", "Emissions-Formation-and-Control"),
        ("600", "Combustion-Dynamics-and-Instability-Management"),
        ("700", "Ignition-and-Relight-Envelope"),
        ("800", "Liner-Cooling-and-Thermal-Management"),
        ("900", "Combustion-Diagnostics-and-Evidence"),
    ]),
    "064": ("Carrier-Delivery-Metering-and-Conditioning", [
        ("000", "General-Information"),
        ("100", "Aircraft-Interface-and-Reception"),
        ("200", "Engine-Side-Distribution-and-Manifolds"),
        ("300", "Metering-and-Flow-Control"),
        ("400", "Thermal-Conditioning-and-Heat-Exchange"),
        ("500", "Pumping-and-Pressurization"),
        ("600", "Purge-Inerting-and-Safe-States"),
        ("700", "Carrier-Quality-and-Contamination-Management"),
        ("800", "Dual-Carrier-and-Transition-Operation"),
        ("900", "Delivery-System-Protection-and-Relief"),
    ]),
    "065": ("Engine-Air-and-Thermal-Management", [
        ("000", "General-Information"), ("100", "Secondary-Air-Systems"),
        ("200", "Turbine-Cooling-Air"), ("300", "Thermal-Management-Architecture"),
        ("400", "Bleed-and-Bleedless-Offtake-Provisions"),
        ("500", "Anti-Ice-Air-Provisions"), ("600", "Ventilation-and-Nacelle-Cooling"),
        ("700", "Heat-Exchangers-and-Recuperation"),
        ("800", "Active-Thermal-Control"), ("900", "Thermal-Evidence-and-Characterization"),
    ]),
    "066": ("Control-Monitoring-and-Indicating", [
        ("000", "General-Information"), ("100", "Control-System-Architecture"),
        ("200", "Carrier-Aware-Control-Laws"), ("300", "Sensors-and-Instrumentation"),
        ("400", "Actuation-and-Effectors"), ("500", "Protection-Functions-and-Limits"),
        ("600", "Indicating-and-Crew-Interface-Data"),
        ("700", "Health-Monitoring-and-Diagnostics"),
        ("800", "Software-and-Certification-Aspects"), ("900", "Control-System-Evidence"),
    ]),
    "067": ("Exhaust-Emissions-and-Contrail-Management", [
        ("000", "General-Information"), ("100", "Exhaust-System-and-Nozzles"),
        ("200", "Gaseous-Emissions-Characterization"), ("300", "Particulate-and-nvPM"),
        ("400", "Contrail-Formation-and-Mitigation"),
        ("500", "Water-Vapour-and-Plume-Behavior"), ("600", "Propulsion-Noise-at-Source"),
        ("700", "Emissions-Measurement-and-Instrumentation"),
        ("800", "Thrust-Reverser-Provisions"), ("900", "Environmental-Evidence-and-Reporting"),
    ]),
    "068": ("Turbogenerators-and-Power-Offtakes", [
        ("000", "General-Information"), ("100", "Turbogenerator-Architectures"),
        ("200", "Generator-Integration-and-Cooling"), ("300", "Mechanical-Offtakes-and-Gearboxes"),
        ("400", "Accessory-Drives"), ("500", "Power-Quality-at-Machine-Interface"),
        ("600", "Transient-Behavior-and-Load-Response"),
        ("700", "Turbogenerator-Control-Interface"),
        ("800", "Hybrid-Duty-Cycles-and-Endurance"), ("900", "Offtake-Evidence-and-Characterization"),
    ]),
    "069": ("Lubrication-Ignition-Starting-and-Accessories", [
        ("000", "General-Information"), ("100", "Lubrication-Systems"),
        ("200", "Oil-Thermal-Management"), ("300", "Ignition-Systems"),
        ("400", "Starting-Systems"), ("500", "Accessory-Systems-and-Mounting"),
        ("600", "Seals-Buffering-and-Vent-Systems"),
        ("700", "Chip-Detection-and-Debris-Monitoring"),
        ("800", "Servicing-Points-and-Ground-Interfaces"),
        ("900", "Auxiliary-Systems-Evidence"),
    ]),
}

BOUNDARIES = (
    "Carrier storage and aircraft-side distribution: 028 (this range starts at "
    "the aircraft interface — 064-100). Loss-of-containment three-layer model: "
    "028 system condition / 026 aircraft-level hazard / 047 atmosphere response. "
    "Venting: 028 function / 030-720 terminal mast. Hybrid split: the "
    "turbogenerator machine is 068; the hybrid architecture, energy management "
    "and drivetrain are 070-079. Fire protection: 026. Waste-heat and vehicle "
    "thermal coordination: REF 021 and 070-079. Crew alerting presentation: "
    "flight-deck indicating chapters. Hosting of control/monitoring functions "
    "on shared platforms: 042-400. Emissions: 063 owns in-combustor formation "
    "and combustion-side control; 067 owns exhaust-system effects, plume "
    "characterization, measurement, reporting and aircraft-level mitigation "
    "provisions. Ice protection: 065 owns anti-ice air generation and "
    "powerplant-side supply; 030 owns the aircraft ice-protection function and "
    "protected surfaces. Machine classes: functional chapters (063-067, 069) "
    "apply across combustion machine classes; machine-specific internals live "
    "in 062, with reciprocating and rotary machines at 062-800. Range-extender "
    "combustion engines: machine in 062, generator-set integration in 068, "
    "hybrid architecture in 070-079."
)


def validate_schema():
    expected = [f"{code:03d}" for code in range(60, 70)]
    if list(CH) != expected:
        raise ValueError(f"Expected chapters {expected}, got {list(CH)}")
    sections = [f"{index * 100:03d}" for index in range(10)]
    for chapter, (_, values) in CH.items():
        if [code for code, _ in values] != sections:
            raise ValueError(f"Chapter {chapter}: invalid section sequence")


def range_readme():
    lines = [
        f"# {RANGE}_{RANGE_TITLE}", "",
        f"**Band:** 000-099_S-ATLAS · **Range:** {RANGE}", "",
        "## Scope (ratified)", "", RANGE_SCOPE, "",
        "## Chapter map", "", RANGE_DIAGRAM, "",
        "## Chapter register", "",
        "| Chapter | Title | Folder |", "|---|---|---|",
    ]
    lines.extend(
        f"| {code} | {title.replace('-', ' ')} | <a>{code}</a> |"
        for code, (title, _) in CH.items()
    )
    lines.extend([
        "", "## Boundary summary", "", BOUNDARIES, "",
        "*Section registers are PROPOSED; ratification by merge. Subjects are "
        "scaffolded as General-Information plus reserved slots and are authored "
        "per work package.*", "",
    ])
    return "\n".join(lines)


def chapter_readme(chapter, title, sections):
    lines = [
        f"# {chapter}_{title}", "",
        f"**Range:** {RANGE}_{RANGE_TITLE} · **Chapter:** {chapter}", "",
        "## Section register (PROPOSED)", "",
        "| Section | Title | Folder |", "|---|---|---|",
    ]
    lines.extend(
        f"| {section} | {title.replace('-', ' ')} | <a>{chapter}-{section}</a> |"
        for section, title in sections
    )
    lines.extend([
        "", "*Status: scaffolded. Section content and subject titles are authored "
        "per work package; registers ratified by merge.*", "",
    ])
    return "\n".join(lines)


def section_readme(chapter, section, title):
    return (
        f"# {chapter}-{section} — {title.replace('-', ' ')}\n\n"
        f"**Chapter:** {chapter} · **Section:** {section} · **Status:** scaffolded\n\n"
        "Scope, subjects and graphics are authored per work package. Subject "
        "000 carries general information; slots 001-009 are reserved.\n"
    )


def subject_stub(chapter, section, number, reserved):
    code = f"{chapter}-{section}-{number}"
    if reserved:
        return (
            f"# {code} — Reserved\n\n"
            "Reserved subject slot — title and content assigned at authoring "
            "per work package.\n"
        )
    return (
        f"# {code} — General Information\n\n"
        f"**Section:** {chapter}-{section} · **Subject:** 000\n\n"
        "General information for this section — authored per work package.\n"
    )


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--no-subjects", action="store_true")
    parser.add_argument(
        "--bootstrap", action="store_true",
        help="allow creating the tree when the Q+ATLANTIDE anchor is absent",
    )
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
                plan.append((
                    section_dir / f"{chapter}-{section}-000_General-Information/README.md",
                    subject_stub(chapter, section, "000", False), False,
                ))
                for number in range(1, 10):
                    plan.append((
                        section_dir / f"{chapter}-{section}-00{number}_Reserved/README.md",
                        subject_stub(chapter, section, f"00{number}", True), False,
                    ))

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
