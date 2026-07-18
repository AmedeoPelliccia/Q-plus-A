#!/usr/bin/env python3
"""Populate the S-ATLAS 057 Wings chapter."""

import argparse
import sys
from pathlib import Path

CH = "057"
CH_TITLE = "Wings"
RANGE_REL = (
    "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
    "000-099_S-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces"
)

SCOPE = (
    "Wing primary and secondary structure: root and center integration, main box, "
    "outer wing and transitions, tips and tip devices, leading- and trailing-edge "
    "structures including high-lift device structures, attachments and fittings, "
    "systems installation provisions, and the novel sustainable wing-technology "
    "block. Surface structure lives here; surface actuation and control functions "
    "are 027; the energy-carrier system is 028; practices are 051; type classes "
    "(092) constrain, this chapter owns the technology."
)

DIAGRAM = """```mermaid
flowchart LR
  subgraph SPAN["Spanwise structure"]
    R["057-100 Root &amp;<br>Center Integration"] --&gt; B["057-200<br>Wing Main Box"] --&gt; O["057-300 Outer Wing<br>&amp; Transitions"] --&gt; T["057-400 Tips &amp;<br>Tip Devices"]
  end
  LE["057-500 Leading Edge &amp;<br>LE Device Structures"] --- SPAN
  TE["057-600 Trailing Edge &amp;<br>TE Device Structures"] --- SPAN
  F["057-700 Attachments,<br>Joints &amp; Fittings"] --- SPAN
  P["057-800 Systems<br>Installation Provisions"] --- SPAN
  N["057-900 Novel Wing Architectures<br>&amp; Sustainable Technologies"] -. "applies across" .-&gt; SPAN
  F -. "pylon/propulsor attach" .-&gt; X077["054 · 061 · 077"]
  P -. "carrier volume boundary" .-&gt; X028["028"]
```"""

# Section code -> (title, scope bullets, [(subject code, title, summary)])
S = {
    "000": ("General", [
        "Chapter-level items that apply across the wing: surface protection, access, "
        "mass balance and zoning.",
        "Wing zoning and station conventions align with chapter 006 references.",
    ], [
        ("010", "Wing-Surface-Protection-and-Films",
         "Erosion and surface-protection film systems, their zones and renewal criteria."),
        ("020", "Wing-Access-Provisions",
         "Access panels and openings doctrine across wing zones; panel classes and sealing interfaces."),
        ("030", "Mass-Balance-and-Trim-Provisions",
         "Balance-weight provisions for surfaces requiring mass balancing (051-600 practice)."),
        ("040", "Wing-Zoning-Stations-and-Reference-Geometry",
         "Station and zone reference frames for all wing structure addressing."),
    ]),
    "100": ("Wing-Root-and-Center-Integration", [
        "Root region structure and its integration with the center body: skins, internal "
        "structure, spar terminations, sealing dams and the wing-to-body attachment interfaces.",
        "Fuselage-side attach structure is 053-800; the fairing aerodynamic surfaces "
        "interface 053; this section owns the wing side.",
    ], [
        ("110", "Root-Skins-and-Panels", "Root-region skin panels and their reinforcement patterns."),
        ("120", "Root-Internal-Structure", "Internal root structure carrying the span-loads transition into the center body."),
        ("130", "Root-Spar-Terminations", "Spar run-outs and termination fittings at the root."),
        ("140", "Root-Ribs-and-Sealing-Dams", "Root ribs including sealing-dam structures bounding internal volumes."),
        ("150", "Wing-to-Body-Attachment-and-Fairing-Interfaces", "Wing-side attach fittings and belly-fairing structural interfaces (053, 054)."),
    ]),
    "200": ("Wing-Main-Box", [
        "The primary torsion-and-bending box: stiffened skins, spars, ribs and stringers, "
        "with access and integral-volume provisions.",
        "Integral volumes are structural provisions; the energy-carrier system that may "
        "occupy them is 028 (057-820 declares the split).",
    ], [
        ("210", "Main-Box-Skins-and-Stiffened-Panels", "Upper and lower stiffened skin panels; buckling and damage-tolerance drivers."),
        ("220", "Main-Box-Spars", "Front and rear spars; shear webs, caps and local reinforcements."),
        ("230", "Main-Box-Ribs", "Rib classes: load, sealing, system-support; pitch doctrine."),
        ("240", "Stringers-and-Stiffeners", "Stringer systems and skin-stringer joining approaches (051-4xx practices)."),
        ("250", "Integral-Volume-Provisions", "Structural provisions of internal volumes: dry-wing default, wet-wing option as declared architecture."),
        ("260", "Main-Box-Access-Panels", "Box access openings, their reinforcement and sealing interfaces."),
    ]),
    "300": ("Outer-Wing-and-Transitions", [
        "Outboard wing structure and the transition regions, including landing-gear support "
        "fittings where the configuration mounts gear in the wing.",
        "Gear system and doors are 032; the fitting structure is owned here.",
    ], [
        ("310", "Outer-Wing-Skins", "Outboard skin panels and taper transitions."),
        ("320", "Outer-Wing-Spars-and-Ribs", "Outboard spar and rib continuation; kink and transition structure."),
        ("330", "Landing-Gear-Support-Fittings", "Wing-mounted gear attachment fittings and their backup structure (032 interface)."),
        ("340", "Span-Transition-and-Kink-Structure", "Geometry-transition structure between inner and outer wing."),
    ]),
    "400": ("Wing-Tips-and-Tip-Devices", [
        "Tip structure and tip devices: winglets and other tip aerodynamic devices, their "
        "internal structure, fairings and provisions for adaptive or folding tips.",
        "Folding-tip ground-compatibility constraints are class matter (09x-700); the "
        "mechanism-bearing structure is owned here.",
    ], [
        ("410", "Wing-Tip-Structure", "Tip closure structure, skins and internal members."),
        ("420", "Winglet-and-Tip-Device-Structure", "Tip-device skins, spars and ribs as a class; device-to-wing joint."),
        ("430", "Tip-Device-Leading-Edges-and-Protection", "Tip-device leading edges and their surface-protection films."),
        ("440", "Tip-Lighting-and-Antenna-Fairings", "Structural fairings for lights and antennas at the tip region (033, 023/034 interfaces)."),
        ("450", "Folding-and-Adaptive-Tip-Provisions", "Fold-joint and adaptive-tip structural provisions; latching structure classes."),
    ]),
    "500": ("Leading-Edge-and-LE-Device-Structures", [
        "Fixed leading edge and leading-edge device structures: slat-class surfaces, their "
        "tracks, racks and bearings, seals and systems integration provisions.",
        "Device actuation and control are 027; ice-protection function is 030; this section "
        "owns the structures and their guidance hardware.",
    ], [
        ("510", "Fixed-Leading-Edge-Structure", "Fixed LE skins, stringers, ribs and access panels."),
        ("520", "Slat-Structures", "Slat-class surface structure: skins, girders, spars, ribs — class-level, instance counts are programme matter."),
        ("530", "LE-Device-Tracks-Racks-and-Bearings", "Track, rack, roller and spherical-bearing structures guiding LE devices."),
        ("540", "LE-Seals-and-Interfaces", "Longitudinal, chordwise, lower and weather seal classes and their landings."),
        ("550", "LE-Systems-Integration-Provisions", "Structural provisions for ice-protection distribution (030) and LE harness routing."),
    ]),
    "600": ("Trailing-Edge-and-TE-Device-Structures", [
        "Fixed trailing edge and trailing-edge device structures: flap-class surfaces including "
        "multi-element arrangements, their tracks, carriages and mechanisms' structure, "
        "aileron and spoiler surface structures.",
        "Actuation, control laws and rigging are 027; hinge and actuator fittings are 057-730.",
    ], [
        ("610", "Fixed-Trailing-Edge-Structure-and-Seals", "Fixed TE structure, TE seals and fairlead provisions."),
        ("620", "Flap-Structures", "Flap-class surfaces including aft-flap elements of multi-slotted arrangements; skins and internal structure."),
        ("630", "Flap-Tracks-Carriages-and-Mechanism-Structure", "Track supports, main and aft tracks, carriages, bellcrank and rod structural elements."),
        ("640", "Aileron-and-Spoiler-Surface-Structures", "Aileron and spoiler surface structure as classes; balance provisions per 057-030."),
        ("650", "TE-Fairings-and-Track-Fairings", "Track and mechanism fairing structures and their attachments."),
    ]),
    "700": ("Attachments-Joints-and-Fittings", [
        "Cross-cutting attachment structure: major fittings, pylon and propulsor attach "
        "provisions, control-surface hinge and actuator fittings, strut and brace attachments, "
        "and the joint doctrine.",
        "Practices for fastening, bonding and welding are 051-4xx; this section owns the wing's fitting architecture.",
    ], [
        ("710", "Major-Attach-Fittings", "Primary attach fittings and their backup structure; sibling of 053-800."),
        ("720", "Pylon-and-Propulsor-Attach-Provisions", "Wing-side attach provisions consumed by 054 pylons, 061 installation and 077-500 propulsor installation."),
        ("730", "Control-Surface-Hinge-and-Actuator-Fittings", "Hinge lines, actuator fittings and their load introduction (027 interface)."),
        ("740", "Strut-and-Brace-Attachment-Provisions", "Attachment provisions for braced-wing configurations; 092 class constrains, structure owned here."),
        ("750", "Joints-Splices-and-Fastening-Architecture", "Spanwise and chordwise joint architecture; splice doctrine per 051-510."),
    ]),
    "800": ("Wing-Systems-Installation-Provisions", [
        "The structure side of systems installation: routing, bonding, carrier-volume boundaries, "
        "ice-protection integration, sensors and lights, ground points.",
        "Split doctrine applies throughout: the system owns function and hardware; this section owns the structural provision.",
    ], [
        ("810", "Harness-Routing-and-Bonding-Provisions", "Structural routing paths and bonding/grounding provisions (024 wing harness, 051-800)."),
        ("820", "Energy-Carrier-Volume-Boundary-Provisions", "Structural boundary of carrier volumes where a wet-wing architecture is declared: boundary integrity, access, sealing substrate — the carrier system itself is 028."),
        ("830", "Ice-Protection-Integration-Provisions", "Structural integration of ice-protection distribution and heated zones (030 owns the function)."),
        ("840", "Sensor-and-Light-Installation-Provisions", "Structural provisions for sensors, lights and their fairings (033, 034 interfaces)."),
        ("850", "Ground-Point-Jacking-and-Safety-Provisions", "Jack points, safety points and their local structure (007, 003 interfaces)."),
    ]),
    "900": ("Novel-Wing-Architectures-and-Sustainable-Technologies", [
        "The green-native block: wing technologies that define sustainable aviation structures, "
        "documented as technology classes with declared interfaces to the classic sections.",
        "Type classes (091-097) constrain configurations; maturity-gated concepts incubate in 080-089 and graduate here.",
    ], [
        ("910", "High-Aspect-Ratio-and-Braced-Wing-Structures", "Structural technology of high-aspect-ratio and strut/truss-braced wings; attach provisions per 057-740."),
        ("920", "Laminar-Flow-Surface-Structures", "Surface-quality-driven structure: joint and fastener flushness classes, waviness control, suction-provision structures."),
        ("930", "Morphing-and-Adaptive-Structures", "Shape-adaptive structural concepts and their load-path doctrine; actuation remains 027."),
        ("940", "Thermoplastic-and-Welded-Wing-Structures", "Welded thermoplastic primary-structure application; processes per 051-230, materials per 051-320."),
        ("950", "Distributed-Propulsion-Structural-Integration", "Spanwise multi-attach structural integration for distributed propulsors (077-300 arrays; 077-500 installation)."),
        ("960", "Structural-Health-Monitoring-Integration", "Embedded and applied SHM provisions; data paths via platform services (042, 045)."),
        ("970", "Circularity-Disassembly-and-Recycling-Provisions", "Design-for-disassembly joints, material identification and end-of-life provisions (051-340)."),
    ]),
}

BOUNDARIES = (
    "Surface structure here; surface actuation, control laws and rigging: 027. "
    "Carrier volumes: 057-250/-820 own the structural provision and boundary; the "
    "energy-carrier system is 028; sealing practices 051-220. Ice protection: 030 "
    "owns the function, 057-550/-830 the structural integration. Landing gear: 032 "
    "owns the system, 057-330 the fittings. Pylons and propulsors: 054 pylon "
    "structure, 061 installation, 077 propulsor units — 057-720/-950 own the "
    "wing-side provisions. Fuselage side: 053. Practices: 051. Jacking operations: "
    "007. Type classes 091-097 constrain; 080-089 incubates and graduates."
)


def sec_readme(code, title, bullets, subjects):
    lines = [f"# {CH}-{code} — {title.replace('-', ' ')}", "",
             f"**Chapter:** {CH}_{CH_TITLE} · **Section:** {code}", ""]
    lines.extend(f"- {bullet}" for bullet in bullets)
    lines.extend(["", "## Subjects", "", "| Subject | Title |", "|---|---|"])
    lines.extend(
        f"| {CH}-{subject} | [{title.replace('-', ' ')}]({CH}-{subject}_{title}/) |"
        for subject, title, _ in subjects
    )
    return "\n".join(lines) + "\n"


def subj_readme(section, subject, title, summary):
    return (
        f"# {CH}-{subject} — {title.replace('-', ' ')}\n\n"
        f"**Section:** {CH}-{section} · **Subject:** {subject}\n\n"
        f"- {summary}\n"
    )


def ch_readme():
    lines = [f"# {CH}_{CH_TITLE}", "",
             "**Range:** 050-059_Primary-Structures-and-Programme-Interfaces · "
             f"**Chapter:** {CH}", "", "## Scope", "", SCOPE, "",
             "## Structure map", "", DIAGRAM, "", "## Section register", "",
             "| Section | Title | Subjects |", "|---|---|---|"]
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
        plan.append((section_dir / "README.md",
                     sec_readme(section, title, bullets, subjects), True))
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
