#!/usr/bin/env python3
"""Scaffold the S-ATLAS 080-089 alternative and quantum propulsion range."""

import argparse
import sys
from pathlib import Path

RANGE = "080-089"
RANGE_TITLE = "Alternative-and-Quantum-Propulsion"
BAND_REL = (
    "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
    "000-099_S-ATLAS"
)
RANGE_SCOPE = (
    "Frontier propulsion beyond the combustion/electric classes. The register "
    "distinguishes maturity classes — physically established alternative "
    "propulsion; exploratory concepts; quantum-enabled analysis, sensing or "
    "control; speculative quantum-propulsion hypotheses — and every future "
    "chapter in this range carries a declared maturity or evidence status."
)
MATURITY = {
    "M1": "Physically established alternative propulsion",
    "M2": "Exploratory concepts — demonstrated physics, aircraft application open",
    "M3": "Quantum-enabled analysis, sensing or control (quantum as enabler)",
    "M4": "Speculative quantum-propulsion hypotheses — epistemic register only",
}
RANGE_DIAGRAM = """```mermaid
flowchart LR
  subgraph M2["M2 — exploratory concepts"]
    C081["081 Pressure-Gain &<br/>Detonation Combustion"]
    C082["082 High-Speed<br/>Airbreathing"]
    C083["083 Electroaerodynamic<br/>& Ionic"]
    C084["084 Beamed & Remote<br/>Energy"]
    C085["085 Superconducting &<br/>Cryo-Electric"]
  end
  subgraph M3["M3 — quantum as enabler"]
    C086["086 Quantum-Enabled<br/>Analysis & Design"]
    C087["087 Quantum Sensing<br/>& Control"]
  end
  C088["088 Quantum-Propulsion<br/>Hypotheses (M4)"]
  C089["089 Horizon Scanning &<br/>Hypothesis Register"]
  C080["080 Doctrine, Maturity<br/>& Graduation"] -. governs .-> M2
  C080 -. governs .-> M3
  C080 -. governs .-> C088
  C081 -- "graduation" --> G060["060-069"]
  C082 -- "graduation" --> G060
  C085 -- "graduation" --> G070["070-079 (072/078)"]
  C089 --> M2
```"""

# Chapter code -> (title, maturity, [(section code, title), ...])
CH = {
    "080": ("General-Doctrine-Maturity-and-Graduation", "M1-M4 framework", [
        ("000", "General-Information"), ("100", "Range-Scope-and-Doctrine"),
        ("200", "Maturity-Class-Framework"), ("300", "Evidence-Requirements-per-Class"),
        ("400", "Graduation-Criteria-and-Process"), ("500", "Claims-Discipline-and-Epistemic-Guardrails"),
        ("600", "Safety-and-Certification-Pathfinding"), ("700", "Interfaces-to-Established-Ranges"),
        ("800", "Review-and-Reclassification-Cycle"), ("900", "Glossary-and-Controlled-Vocabulary")]),
    "081": ("Pressure-Gain-and-Detonation-Combustion", "M2 → graduates to 060", [
        ("000", "General-Information"), ("100", "Rotating-Detonation-Concepts"),
        ("200", "Pulse-Detonation-Concepts"), ("300", "Pressure-Gain-Cycle-Analysis"),
        ("400", "Sustainable-Carrier-Detonation-Behavior"), ("500", "Injection-and-Mixing-at-Detonation-Timescales"),
        ("600", "Thermal-and-Structural-Challenges"), ("700", "Instrumentation-and-Diagnostics"),
        ("800", "Integration-Pathways-to-Turbomachinery"), ("900", "Evidence-Status-and-Graduation-Tracking")]),
    "082": ("High-Speed-Airbreathing-Propulsion", "M2 → graduates to 060", [
        ("000", "General-Information"), ("100", "Ramjet-Concepts-for-Sustainable-Carriers"),
        ("200", "Scramjet-Concepts"), ("300", "Combined-Cycle-Architectures"),
        ("400", "Hydrogen-High-Speed-Combustion"), ("500", "Thermal-Management-at-High-Speed"),
        ("600", "Materials-and-Structures-Interfaces"), ("700", "Vehicle-Integration-Considerations"),
        ("800", "Test-Infrastructure-and-Evidence"), ("900", "Evidence-Status-and-Graduation-Tracking")]),
    "083": ("Electroaerodynamic-and-Ionic-Propulsion", "M2", [
        ("000", "General-Information"), ("100", "EAD-Physics-and-Thrust-Generation"),
        ("200", "Electrode-and-Emitter-Architectures"), ("300", "High-Voltage-Generation-Interfaces"),
        ("400", "Atmospheric-and-Environmental-Effects"), ("500", "Scaling-Laws-and-Limits"),
        ("600", "Ozone-and-Emissions-Considerations"), ("700", "Control-and-Modulation"),
        ("800", "Demonstrations-and-Flight-Evidence"), ("900", "Evidence-Status-and-Graduation-Tracking")]),
    "084": ("Beamed-and-Remote-Energy-Propulsion", "M2", [
        ("000", "General-Information"), ("100", "Laser-Power-Beaming-Concepts"),
        ("200", "Microwave-Power-Beaming-Concepts"), ("300", "Onboard-Reception-and-Conversion"),
        ("400", "Beam-Safety-and-Airspace-Considerations"), ("500", "Ground-Infrastructure-Interfaces"),
        ("600", "Pointing-Tracking-and-Link-Management"), ("700", "Atmospheric-Propagation-Effects"),
        ("800", "Demonstrations-and-Evidence"), ("900", "Evidence-Status-and-Graduation-Tracking")]),
    "085": ("Superconducting-and-Cryo-Electric-Propulsion", "M2 → graduates to 072/078", [
        ("000", "General-Information"), ("100", "Superconducting-Machine-Concepts"),
        ("200", "Cryogenic-Power-Transmission"), ("300", "Cryocooler-and-Thermal-Architecture"),
        ("400", "Quench-Detection-and-Protection"), ("500", "HTS-Materials-and-Conductors"),
        ("600", "Weight-and-Efficiency-Scaling"), ("700", "Integration-with-Hydrogen-Systems"),
        ("800", "Demonstrators-and-Evidence"), ("900", "Evidence-Status-and-Graduation-Tracking")]),
    "086": ("Quantum-Enabled-Propulsion-Analysis-and-Design", "M3", [
        ("000", "General-Information"), ("100", "Quantum-Chemistry-for-Combustion-and-Carriers"),
        ("200", "Quantum-Approaches-to-Flow-Simulation"), ("300", "Materials-Discovery-Support"),
        ("400", "Optimization-of-Propulsion-Architectures"), ("500", "Hybrid-Classical-Quantum-Workflows"),
        ("600", "Verification-and-Trust-of-Quantum-Results"), ("700", "Toolchain-and-Access-Models"),
        ("800", "Case-Studies-and-Benchmarks"), ("900", "Evidence-Status-and-Utility-Assessment")]),
    "087": ("Quantum-Sensing-and-Control-for-Propulsion", "M3", [
        ("000", "General-Information"), ("100", "Quantum-Inertial-and-Timing-for-Propulsion-Control"),
        ("200", "Quantum-Magnetometry-Applications"), ("300", "Quantum-Enhanced-Combustion-Diagnostics"),
        ("400", "Cryogenic-Co-Location-Synergies"), ("500", "Integration-with-Control-Systems"),
        ("600", "Environmental-Robustness"), ("700", "Certification-Considerations-for-Quantum-Sensors"),
        ("800", "Demonstrations-and-Evidence"), ("900", "Evidence-Status-and-Utility-Assessment")]),
    "088": ("Quantum-Propulsion-Hypotheses", "M4 — epistemic register only", [
        ("000", "General-Information"), ("100", "Hypothesis-Classes-and-Taxonomy"),
        ("200", "Physical-Consistency-Requirements"), ("300", "Falsifiability-and-Test-Criteria"),
        ("400", "Known-Claims-Review-Discipline"), ("500", "Energy-and-Momentum-Accounting-Requirements"),
        ("600", "Prohibited-Claims-and-Guardrails"), ("700", "Literature-and-Watch-Register"),
        ("800", "Evaluation-Protocol"), ("900", "Status-Register")]),
    "089": ("Horizon-Scanning-and-Hypothesis-Register", "Intake — classifies into M1-M4", [
        ("000", "General-Information"), ("100", "Intake-and-Screening-Process"),
        ("200", "Classification-into-Maturity-Classes"), ("300", "Registered-Concepts-Catalog"),
        ("400", "Nuclear-Propulsion-Considerations"), ("500", "Magnetohydrodynamic-and-Plasma-Concepts"),
        ("600", "Bio-Inspired-and-Unconventional-Concepts"), ("700", "Cross-Band-Technology-Watch"),
        ("800", "Periodic-Review-and-Reporting"), ("900", "Register-Evidence-and-Index")]),
}

BOUNDARIES = (
    "Graduation doctrine: conversion class decides the range for established technology; "
    "maturity decides for the frontier. Concepts incubate here under a declared class and "
    "graduate to their conversion-class range upon physical establishment and an open "
    "certification path — detonation and high-speed combustion to 060-069; superconducting "
    "and cryo-electric to 072/078. Quantum technology itself (computing, sensors, networks) "
    "is owned by 900-999 QCSAA; this range documents its propulsion application (M3) only. "
    "Solar-electric aircraft are not homed here: the drivetrain is 070-079 and harvesting "
    "technology is EPTA — an energy source feeding an electric drive is electric propulsion. "
    "EAD high-voltage practice follows 076-class discipline. Beamed-energy ground "
    "infrastructure is referenced, never duplicated (S-ATLAS boundary condition). M4 claims "
    "discipline: no functional or performance claims may be derived from theoretical or "
    "morphological results; falsifiability criteria and energy-momentum accounting are "
    "mandatory for any registered hypothesis. Every chapter README carries its maturity "
    "class and evidence status; reclassification follows the 080-800 review cycle."
)


def validate_schema():
    expected = [f"{number:03d}" for number in range(80, 90)]
    if list(CH) != expected:
        raise ValueError(f"Expected chapters {expected}, got {list(CH)}")
    sections = [f"{number * 100:03d}" for number in range(10)]
    for chapter, (_, _, values) in CH.items():
        if [code for code, _ in values] != sections:
            raise ValueError(f"Chapter {chapter}: invalid section sequence")


def range_readme():
    lines = [f"# {RANGE}_{RANGE_TITLE}", "", f"**Band:** 000-099_S-ATLAS · **Range:** {RANGE}",
             "", "## Scope (ratified)", "", RANGE_SCOPE, "", "## Maturity-class framework", "",
             "| Class | Meaning |", "|---|---|"]
    lines.extend(f"| {key} | {value} |" for key, value in MATURITY.items())
    lines += ["", "## Chapter map", "", RANGE_DIAGRAM, "", "## Chapter register", "",
              "| Chapter | Title | Maturity | Folder |", "|---|---|---|---|"]
    lines.extend(f"| {code} | {title.replace('-', ' ')} | {maturity} | <a>{code}</a> |"
                 for code, (title, maturity, _) in CH.items())
    lines += ["", "## Boundary summary", "", BOUNDARIES, "",
              "*Section registers are PROPOSED; ratification by merge. Subjects are "
              "scaffolded as General-Information plus reserved slots and are authored "
              "per work package.*", ""]
    return "\n".join(lines)


def chapter_readme(chapter, title, maturity, sections):
    lines = [f"# {chapter}_{title}", "",
             f"**Range:** {RANGE}_{RANGE_TITLE} · **Chapter:** {chapter}", "",
             f"**Maturity class:** {maturity} · **Evidence status:** scaffolded — "
             "no authored evidence; status updated per work package.", "",
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
    for chapter, (title, maturity, sections) in CH.items():
        chapter_dir = range_dir / f"{chapter}_{title}"
        plan.append((chapter_dir / "README.md", chapter_readme(chapter, title, maturity, sections), True))
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
            path.write_text(content, encoding="utf-8")
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
