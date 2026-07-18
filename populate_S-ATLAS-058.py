#!/usr/bin/env python3
"""Populate the S-ATLAS 058 advanced and green structural systems chapter."""

import argparse
import sys
from pathlib import Path

CH = "058"
CH_TITLE = "Advanced-and-Green-Structural-Systems"
RANGE_REL = (
    "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
    "000-099_S-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces"
)

SCOPE = (
    "Cross-component structural technologies and airframe-level structural "
    "doctrines: multifunctional structures, structural energy storage, integrated "
    "antenna and sensor structures, the airframe-level structural-health architecture, "
    "thermal and environmental multifunction structures, bio-based and recycled "
    "structural applications, circular airframe architecture, certification pathfinding "
    "for novel structural technologies, and the structural technology watch. "
    "Reason-to-exist rule: 058 owns technologies whose unit of application spans "
    "components or whose governance is airframe-level; component-side implementations "
    "live in the sibling -900 blocks (052-900, 054-900, 055-900, 056-900, 057-900, "
    "053-900, 050-900); materials science lives in the materials band; practices live "
    "in 051. A technology with a single-component home has no address here. Frontier "
    "concepts carry a declared evidence status (080-200 discipline) and graduate to "
    "component blocks upon establishment."
)

DIAGRAM = """```mermaid
flowchart LR
  subgraph SIB["Component -900 blocks"]
    A57["057-900 Wings"]
    A54["054-900 Propulsion<br>Installation"]
    A52["052-900 Doors"]
    A55["055-900 Empennage"]
    A56["056-900 Windows"]
    A53["053-900 Fuselage /<br>Energy Integration"]
  end
  C["058<br>Cross-component technologies<br>and airframe-level doctrines"]
  C -->|"indexes and governs"| SIB
  C -->|"graduation of<br>established concepts"| SIB
  AMTA["500-599 Materials band<br>(materials science)"] -. "technology source" .-> C
  P051["051 Practices"] -. "execution standards" .-> C
  F["Functional chapters<br>021 · 023/034 · 042/045 · 074/024"] -. "functions consumed<br>by multifunction structures" .-> C
```"""

S = {
    "000": (
        "General-and-Chapter-Doctrine",
        [
            "The reason-to-exist rule of the chapter and the router to the component -900 blocks.",
            "Frontier structural concepts carry a declared evidence status and graduate to component blocks upon establishment — the 080 graduation discipline adapted to structures.",
        ],
        [
            ("010", "Reason-to-Exist-and-Ownership-Rule", "The cross-component rule stated normatively: unit of application decides the address."),
            ("020", "Router-to-Component-Advanced-Blocks", "The index mapping component-side advanced technologies to their -900 homes."),
            ("030", "Evidence-Status-and-Graduation-Discipline", "Declared evidence status per concept and the graduation path to component blocks."),
            ("040", "Terminology-of-Multifunctional-Structures", "Controlled vocabulary of structure-plus-function integration."),
        ],
    ),
    "100": (
        "Multifunctional-Structures-Discipline",
        [
            "The discipline of structures that carry load and perform a second function: classification, load-function interaction doctrine and failure-interaction principles.",
            "Specific multifunction families live in 058-200 through 058-500; this section owns the common discipline.",
        ],
        [
            ("110", "Multifunction-Classification-and-Doctrine", "Classes of structure-function integration and their interaction doctrine."),
            ("120", "Load-and-Function-Interaction-Principles", "How structural and functional failure modes interact; separation-of-concerns doctrine."),
            ("130", "Mass-and-Energy-Accounting-of-Multifunction", "Airframe-level accounting doctrine: when integration earns its mass."),
            ("140", "Verification-Doctrine-for-Dual-Role-Structures", "Verification principles where one article carries two certifiable roles."),
        ],
    ),
    "200": (
        "Structural-Energy-Storage",
        [
            "Load-bearing energy storage as an airframe application architecture: structural battery and supercapacitor laminates, their zoning and load-function doctrine.",
            "Cell and laminate technology: materials band and EPTA storage technology; propulsion storage systems: 074; non-propulsive electrical storage: 024-360; the load-bearing application architecture is owned here — four owners, one boundary set.",
        ],
        [
            ("210", "Structural-Battery-Application-Architecture", "Where and how load-bearing storage applies across the airframe; zoning doctrine."),
            ("220", "Load-and-Electrical-Function-Interaction", "Interaction doctrine of structural damage and electrical state (074-300 three-layer analogue applies)."),
            ("230", "Structural-Storage-Interfaces", "Interfaces toward propulsion (074) and aircraft (024) electrical systems."),
            ("240", "Structural-Storage-Evidence-Doctrine", "Evidence classes of dual-role storage structures; status declared per 058-030."),
        ],
    ),
    "300": (
        "Integrated-Antenna-and-Sensor-Structures",
        [
            "Conformal and load-bearing antenna and sensor structures across the airframe.",
            "The radiating and sensing systems are 023, 034 and their chapters; component installation provisions are the siblings' domain; the cross-component load-bearing integration technology is owned here.",
        ],
        [
            ("310", "Conformal-Load-Bearing-Antenna-Structures", "Structurally integrated antenna classes and their airframe application doctrine."),
            ("320", "Embedded-Sensor-Network-Structures", "Structures embedding distributed sensing beyond single-component provisions."),
            ("330", "Electromagnetic-and-Structural-Co-Design", "Co-design doctrine of electromagnetic and structural performance (051-820 protection practices)."),
            ("340", "Integrated-Aperture-Evidence-Doctrine", "Evidence doctrine of load-bearing radiating structures."),
        ],
    ),
    "400": (
        "Airframe-Structural-Health-Architecture",
        [
            "Structural health monitoring as an airframe-level architecture: network topology, data doctrine and certification-credit doctrine.",
            "Component-side SHM provisions live in the sibling blocks (057-960, 055-950-class, 052-950, 056-950); hosting is 042-400; data flows via 045; the airframe-level architecture and credit doctrine are owned here.",
        ],
        [
            ("410", "SHM-Network-Architecture", "Airframe-level sensing-network topology and coverage doctrine."),
            ("420", "SHM-Data-and-Decision-Doctrine", "From sensing to maintenance decision: data classes and their authority (045 records)."),
            ("430", "SHM-Certification-Credit-Doctrine", "When and how monitoring earns inspection-interval or design credit."),
            ("440", "SHM-Evidence-and-Qualification", "Qualification doctrine of airframe SHM as a system."),
        ],
    ),
    "500": (
        "Thermal-and-Environmental-Multifunction-Structures",
        [
            "Structures carrying thermal or environmental functions across components: heat-path-bearing structure, integrated insulation-structure and environmental-barrier structures.",
            "Thermal functions belong to 021 and 078; component provisions to the siblings; the cross-component structural technology is owned here.",
        ],
        [
            ("510", "Heat-Path-Bearing-Structures", "Structural classes intentionally carrying thermal transport (021/078 functions)."),
            ("520", "Integrated-Insulation-Structures", "Structure-integrated insulation classes beyond compartment blankets (050-6xx provisions)."),
            ("530", "Environmental-Barrier-Structures", "Cross-component environmental-barrier structural classes."),
            ("540", "Thermal-Structural-Interaction-Doctrine", "Interaction doctrine of thermal duty and structural life."),
        ],
    ),
    "600": (
        "Bio-Based-and-Recycled-Structural-Applications",
        [
            "Airframe application architecture of bio-based and recycled structural materials: where such materials apply, under which structural roles and with which evidence.",
            "Materials science and development: materials band; materials practices and circularity standards: 051-3xx; the application architecture is owned here.",
        ],
        [
            ("610", "Bio-Based-Material-Application-Classes", "Structural roles admissible for bio-based materials and their doctrine."),
            ("620", "Recycled-Fiber-and-Reclaimed-Material-Applications", "Application classes of recycled and reclaimed structural materials."),
            ("630", "Qualification-Doctrine-for-Variable-Feedstock", "Evidence doctrine where feedstock variability is inherent."),
            ("640", "Application-Traceability-and-Passport-Content", "Structural content of material passports (045 DPP channel; 051-340 practices)."),
        ],
    ),
    "700": (
        "Circular-Airframe-Architecture",
        [
            "Circularity at airframe level: design-for-disassembly architecture, end-of-life flows and the structural content of the product passport.",
            "Component disassembly provisions live in the sibling -9x0 subjects; practices in 051-340; the airframe-level architecture is owned here.",
        ],
        [
            ("710", "Airframe-Disassembly-Architecture", "Aircraft-level joint and module architecture for end-of-life separation."),
            ("720", "Material-Identification-and-Flow-Architecture", "Airframe-wide identification and recovery-flow doctrine."),
            ("730", "Reuse-Remanufacture-and-Recycle-Doctrine", "Hierarchy doctrine of structural end-of-life paths."),
            ("740", "Circularity-Evidence-and-Passport-Integration", "Evidence and passport integration of circular architecture (045 channel)."),
        ],
    ),
    "800": (
        "Certification-Pathfinding-for-Novel-Structural-Technologies",
        [
            "Pathfinding doctrine — not a certification basis — for structural technologies without established compliance paths: bonded primary structure, dual-role structures, monitored-structure credit.",
            "Type-level certification doctrine for novel configurations is 090-700; range safety framework is the range doctrine chapters; this section owns the structural-technology pathfinding.",
        ],
        [
            ("810", "Pathfinding-Doctrine-and-Scope", "What pathfinding is and is not; relationship to authorities and standards."),
            ("820", "Bonded-and-Jointless-Primary-Structure-Paths", "Compliance-path doctrine for bonded primary structure classes."),
            ("830", "Dual-Role-Structure-Compliance-Paths", "Paths where one article certifies under two functions (058-140 verification doctrine)."),
            ("840", "Monitored-Structure-Credit-Paths", "Compliance-path doctrine for SHM-credited structures (058-430)."),
            ("850", "Novel-Process-Structure-Paths", "Paths for structures from novel processes (051-230 practices; materials band technology)."),
        ],
    ),
    "900": (
        "Structural-Technology-Watch-and-Graduation",
        [
            "The structural frontier register: intake, evidence-status tracking and graduation of structural concepts to their component homes.",
            "Mirrors the 089 pattern: the watch never creates homes — it maps concepts to future addresses and graduates them when established.",
        ],
        [
            ("910", "Intake-and-Screening-of-Structural-Concepts", "How structural concepts enter the watch and are classified."),
            ("920", "Registered-Structural-Concepts", "The living register of watched concepts with declared evidence status."),
            ("930", "Graduation-to-Component-Blocks", "Criteria and process moving established concepts to sibling -900 homes."),
            ("940", "Cross-Band-Structural-Watch", "Watch on the materials band and external structural research (references, never duplication)."),
        ],
    ),
}

BOUNDARIES = (
    "Reason-to-exist rule: 058 owns cross-component structural technologies and "
    "airframe-level doctrines; component-side implementations live in the sibling "
    "-900 blocks; a single-component technology has no address here. Materials science: "
    "the materials band (500-599); materials and process practices: 051. Structural "
    "energy storage four-way split: cell and laminate technology in the materials and "
    "energy bands; propulsion storage systems 074; non-propulsive electrical storage "
    "024-360; load-bearing application architecture 058-200. SHM: component provisions "
    "in sibling blocks; airframe architecture and credit doctrine 058-400; hosting "
    "042-400; data and DPP channel 045. Antenna and sensing systems: 023, 034 and "
    "their chapters. Thermal functions: 021 and 078. Type-level certification doctrine "
    "for novel configurations: 090-700; structural-technology pathfinding: 058-800. "
    "Evidence-status and graduation discipline: 080-200 pattern adopted; graduation "
    "targets are the component -900 blocks. Type classes 090-099 constrain and shall "
    "not duplicate this chapter."
)


def sec_readme(code, title, bullets, subjects):
    lines = [
        f"# {CH}-{code} — {title.replace('-', ' ')}",
        "",
        f"**Chapter:** {CH}_{CH_TITLE} · **Section:** {code}",
        "",
    ]
    lines.extend(f"- {bullet}" for bullet in bullets)
    lines.extend(["", "## Subjects", "", "| Subject | Title |", "|---|---|"])
    lines.extend(
        f"| {CH}-{subject} | [{subject_title.replace('-', ' ')}]({CH}-{subject}_{subject_title}/) |"
        for subject, subject_title, _ in subjects
    )
    return "\n".join(lines) + "\n"


def subj_readme(section, subject, title, summary):
    return (
        f"# {CH}-{subject} — {title.replace('-', ' ')}\n\n"
        f"**Section:** {CH}-{section} · **Subject:** {subject}\n\n"
        f"- {summary}\n"
    )


def ch_readme():
    lines = [
        f"# {CH}_{CH_TITLE}",
        "",
        "**Range:** 050-059_Primary-Structures-and-Programme-Interfaces · "
        f"**Chapter:** {CH}",
        "",
        "## Scope",
        "",
        SCOPE,
        "",
        "## Integration chain",
        "",
        DIAGRAM,
        "",
        "## Section register",
        "",
        "| Section | Title | Subjects |",
        "|---|---|---|",
    ]
    lines.extend(
        f"| {CH}-{code} | [{title.replace('-', ' ')}]({CH}-{code}_{title}/) | "
        f"{len(subjects)} |"
        for code, (title, _, subjects) in S.items()
    )
    lines.extend(["", "## Boundary summary", "", BOUNDARIES, ""])
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--bootstrap", action="store_true")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    anchor = root / "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE"
    if not anchor.is_dir() and not args.bootstrap:
        parser.error(
            f"Q+ATLANTIDE root not found under {root}; run from repo root, "
            "use --root, or pass --bootstrap."
        )

    chapter_dir = root / RANGE_REL / f"{CH}_{CH_TITLE}"
    plan = [(chapter_dir / "README.md", ch_readme(), True)]
    for section, (title, bullets, subjects) in S.items():
        section_dir = chapter_dir / f"{CH}-{section}_{title}"
        plan.append((section_dir / "README.md", sec_readme(section, title, bullets, subjects), True))
        for subject, subject_title, summary in subjects:
            plan.append((
                section_dir / f"{CH}-{subject}_{subject_title}" / "README.md",
                subj_readme(section, subject, subject_title, summary),
                False,
            ))

    written = skipped = 0
    for path, content, always in plan:
        exists = path.exists()
        should_write = not exists or always or args.overwrite
        if args.dry_run:
            written += should_write
            skipped += not should_write
        elif should_write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            written += 1
        else:
            skipped += 1

    mode = "dry-run" if args.dry_run else CH
    print(f"[{mode}] written={written} skipped={skipped} planned={len(plan)} at {chapter_dir}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        sys.exit(0)
