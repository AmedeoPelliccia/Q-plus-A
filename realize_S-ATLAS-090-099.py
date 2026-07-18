#!/usr/bin/env python3
"""Scaffold the S-ATLAS 090-099 type architecture range."""

import argparse
import sys
from pathlib import Path

RANGE = "090-099"
RANGE_TITLE = "Type-Specific-Architectures-and-Expansion"
BAND_REL = (
    "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
    "000-099_S-ATLAS"
)
RANGE_SCOPE = (
    "Type-specific architecture chapters define cross-domain configuration "
    "provisions and integration constraints. They reference functional "
    "chapters in other ranges and shall not duplicate system, structure or "
    "propulsion taxonomies. Types are configuration classes, never "
    "programmes; programme applicability is mapped downstream."
)
RANGE_DIAGRAM = """```mermaid
flowchart LR
  subgraph TYPES["Type classes (provisions &amp; constraints only)"]
    C091["091 Blended &amp; Hybrid<br/>Wing Body"]
    C092["092 Advanced<br/>Tube-and-Wing"]
    C093["093 Regional &amp;<br/>Commuter"]
    C094["094 Rotorcraft &amp;<br/>Powered Lift"]
    C095["095 Unmanned &amp;<br/>Optionally Piloted Cargo"]
    C096["096 High-Speed &amp;<br/>Supersonic Transport"]
    C097["097 Stratospheric<br/>Platform / HAPS"]
  end
  C090["090 Doctrine &amp;<br/>Non-Duplication Rule"] -. governs .-> TYPES
  C098["098 Family Commonality<br/>&amp; Derivatives"] --- TYPES
  C099["099 Expansion Register<br/>&amp; Class Intake"] --> TYPES
  TYPES -->|"references, never duplicates"| FUNC["Functional ranges<br/>020-089 · 050s structures"]
```"""

TYPE_SECTIONS = [
    ("000", "General-Information"),
    ("100", "Class-Definition-and-Variants"),
    ("200", "Configuration-Geometry-and-Layout-Provisions"),
    ("300", "Structural-Integration-Constraints"),
    ("400", "Propulsion-Integration-Constraints"),
    ("500", "Systems-Integration-Constraints"),
    ("600", "Cabin-Payload-and-Evacuation-Provisions"),
    ("700", "Ground-Operations-and-Airport-Compatibility"),
    ("800", "Certification-Basis-Considerations"),
    ("900", "Class-Evidence-and-Reference-Configurations"),
]

CH = {
    "090": ("General-and-Type-Architecture-Doctrine", "Doctrine", [
        ("000", "General-Information"),
        ("100", "Range-Scope-and-Non-Duplication-Doctrine"),
        ("200", "Type-Chapter-Structure-and-Uniform-Template"),
        ("300", "Provisions-and-Constraints-Grammar"),
        ("400", "Relationship-to-Functional-Ranges"),
        ("500", "Relationship-to-Downstream-Mapping-Layers"),
        ("600", "Cross-Class-Comparison-Framework"),
        ("700", "Safety-and-Certification-Doctrine-for-Novel-Types"),
        ("800", "Evidence-Framework"),
        ("900", "Glossary-and-Controlled-Vocabulary"),
    ]),
    "091": ("Blended-and-Hybrid-Wing-Body-Class", "Type class", TYPE_SECTIONS),
    "092": ("Advanced-Tube-and-Wing-Class", "Type class", TYPE_SECTIONS),
    "093": ("Regional-and-Commuter-Class", "Type class", TYPE_SECTIONS),
    "094": ("Rotorcraft-and-Powered-Lift-Class", "Type class", TYPE_SECTIONS),
    "095": ("Unmanned-and-Optionally-Piloted-Cargo-Class", "Type class", TYPE_SECTIONS),
    "096": ("High-Speed-and-Supersonic-Transport-Class", "Type class", TYPE_SECTIONS),
    "097": ("Stratospheric-Platform-and-HAPS-Class", "Type class", TYPE_SECTIONS),
    "098": ("Family-Commonality-and-Derivative-Provisions", "Cross-class", [
        ("000", "General-Information"),
        ("100", "Commonality-Doctrine"),
        ("200", "Derivative-Design-Provisions"),
        ("300", "Shared-Systems-Strategies"),
        ("400", "Stretch-and-Shrink-Provisions"),
        ("500", "Cross-Class-Family-Considerations"),
        ("600", "Modular-Cabin-and-Role-Change-Provisions"),
        ("700", "Certification-of-Derivatives"),
        ("800", "Family-Evidence"),
        ("900", "Family-Reference-Patterns"),
    ]),
    "099": ("Expansion-Register-and-Class-Intake", "Intake", [
        ("000", "General-Information"),
        ("100", "Intake-and-Screening-Process"),
        ("200", "Class-Eligibility-Criteria"),
        ("300", "Registered-Candidate-Classes"),
        ("400", "Reserved-Class-Slots"),
        ("500", "Cross-Band-Watch"),
        ("600", "Naming-and-Numbering-Rules"),
        ("700", "Ratification-Process"),
        ("800", "Periodic-Review"),
        ("900", "Register-Index"),
    ]),
}

BOUNDARIES = (
    "Non-duplication rule (ratified): type chapters define cross-domain "
    "configuration provisions and integration constraints; they reference "
    "functional chapters and shall not duplicate system, structure or "
    "propulsion taxonomies. Section grammar is constrained to provisions, "
    "constraints and considerations. Urban air mobility and city vehicles: "
    "700-799 ACV; defence unmanned systems: 200-299 DTTA; space platforms: "
    "100-199 STA. Stratospheric solar platforms: the type class and its "
    "integration constraints live here; the electric drivetrain is 070-079 "
    "and harvesting technology is EPTA. Supersonic: high-speed propulsion "
    "technology matures in 082 and graduates to 060; the class here owns "
    "vehicle-level integration constraints only. Structural content: 050s "
    "chapters own it, type classes constrain it. Freighter and role change: "
    "a family provision (098-600), not a type class. Programme applicability "
    "and instance configurations: downstream mapping layers only."
)


def validate_schema():
    expected_chapters = [f"{chapter:03d}" for chapter in range(90, 100)]
    if list(CH) != expected_chapters:
        raise ValueError(f"Expected chapters {expected_chapters}, got {list(CH)}")
    expected_sections = [f"{index * 100:03d}" for index in range(10)]
    for chapter, (_, _, sections) in CH.items():
        codes = [code for code, _ in sections]
        if codes != expected_sections:
            raise ValueError(
                f"Chapter {chapter}: expected sections {expected_sections}, got {codes}"
            )


def range_readme():
    lines = [
        f"# {RANGE}_{RANGE_TITLE}", "",
        "**Band:** 000-099_S-ATLAS · **Range:** " + RANGE, "",
        "## Scope (ratified)", "", RANGE_SCOPE, "",
        "## Chapter map", "", RANGE_DIAGRAM, "",
        "## Chapter register", "",
        "| Chapter | Title | Kind | Folder |", "|---|---|---|---|",
    ]
    lines.extend(
        f"| {chapter} | {title.replace('-', ' ')} | {kind} | "
        f"[{chapter}]({chapter}_{title}/) |"
        for chapter, (title, kind, _) in CH.items()
    )
    lines += [
        "", "## Boundary summary", "", BOUNDARIES, "",
        "*Section registers are PROPOSED; ratification by merge. Subjects are "
        "scaffolded as General-Information plus reserved slots and are authored "
        "per work package.*", "",
    ]
    return "\n".join(lines)


def chapter_readme(chapter, title, maturity, sections):
    lines = [
        f"# {chapter}_{title}", "",
        f"**Range:** {RANGE}_{RANGE_TITLE} · **Chapter:** {chapter}", "",
        f"**Register note:** {maturity} · **Rule:** references functional "
        "chapters; never duplicates them.", "",
        "## Section register (PROPOSED)", "",
        "| Section | Title | Folder |", "|---|---|---|",
    ]
    lines.extend(
        f"| {section} | {section_title.replace('-', ' ')} | "
        f"[{chapter}-{section}]({chapter}-{section}_{section_title}/) |"
        for section, section_title in sections
    )
    lines += [
        "", "*Status: scaffolded. Section content and subject titles are authored "
        "per work package; registers ratified by merge.*", "",
    ]
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
            f"# {code} — Reserved\n\nReserved subject slot — title and "
            "content assigned at authoring per work package.\n"
        )
    return (
        f"# {code} — General Information\n\n**Section:** {chapter}-{section} · "
        "**Subject:** 000\n\nGeneral information for this section — "
        "authored per work package.\n"
    )


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--no-subjects", action="store_true")
    parser.add_argument(
        "--bootstrap",
        action="store_true",
        help="allow creating the tree when the Q+ATLANTIDE anchor is absent",
    )
    args = parser.parse_args(argv)
    validate_schema()
    root = Path(args.root).resolve()
    anchor = root / BAND_REL.rsplit("/", 1)[0]
    if not anchor.is_dir() and not args.bootstrap:
        parser.error(
            f"Q+ATLANTIDE root not found under {root}; use --root or --bootstrap"
        )
    range_dir = root / BAND_REL / f"{RANGE}_{RANGE_TITLE}"
    plan = [(range_dir / "README.md", range_readme(), True)]
    for chapter, (title, maturity, sections) in CH.items():
        chapter_dir = range_dir / f"{chapter}_{title}"
        plan.append((
            chapter_dir / "README.md",
            chapter_readme(chapter, title, maturity, sections),
            True,
        ))
        for section, section_title in sections:
            section_dir = chapter_dir / f"{chapter}-{section}_{section_title}"
            plan.append((
                section_dir / "README.md",
                section_readme(chapter, section, section_title),
                False,
            ))
            if not args.no_subjects:
                plan.append((
                    section_dir / f"{chapter}-{section}-000_General-Information/README.md",
                    subject_stub(chapter, section, "000", False),
                    False,
                ))
                for number in range(1, 10):
                    plan.append((
                        section_dir / f"{chapter}-{section}-00{number}_Reserved/README.md",
                        subject_stub(chapter, section, f"00{number}", True),
                        False,
                    ))
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
