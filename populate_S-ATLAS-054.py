#!/usr/bin/env python3
"""Populate the programme-agnostic S-ATLAS chapter 054 scaffold."""

import argparse
import sys
from pathlib import Path

CH = "054"
CH_TITLE = "Nacelles-Pylons-and-Propulsion-Integration-Structures"
RANGE_REL = (
    "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
    "000-099_S-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces"
)

SCOPE = (
    "Airframe-side propulsion integration structures: nacelle structures, pylons, "
    "mounts and support structures, dorsal and embedded propulsion integration, "
    "inlet and exhaust structural interfaces, load-transfer attachments, "
    "fire-thermal-acoustic protection structures, cowlings and fairings, "
    "aero-structural integration, and sustainable-installation provisions. "
    "Ownership rule: 054 owns the physical nacelle, pylon, fairing, mounting and "
    "propulsion-to-airframe structural integration; propulsion ranges 060-079 own "
    "the machines, powertrains and functional installation requirements; 053 and "
    "057 own the receiving primary structure."
)

DIAGRAM = """```mermaid
flowchart LR
  M["Machine and powertrain<br>060-079<br>(061 · 077-500 installation discipline)"]
  I["054<br>Integration structures:<br>nacelle · pylon · dorsal fairing<br>mounts · inlet/exhaust structure"]
  P["Receiving primary structure<br>053 centerbody/fuselage · 057 wing"]
  C["Type-class constraints<br>091 BWB/BLI"]
  M --&gt;|"functional requirements<br>and interface loads"| I
  I --&gt;|"attachment reactions<br>and load transfer"| P
  C -. "constrains, never duplicates" .-&gt; I
```"""

S = {
    "000": ("General", [
        "Chapter-level doctrine: what integration structure is, the 054/061/077 "
        "ownership rule, zoning of installations (underwing, aft, dorsal, "
        "embedded) and cross-references.",
        "Mount split: installation requirements and failure cases are 061-100 "
        "(077-500 for electric); mount and support structure is 054-200; "
        "wing-side attach provisions are 057-720, body-side 053-800.",
    ], [
        ("010", "Installation-Zoning-and-Configuration-Classes",
         "Underwing, aft-fuselage, dorsal, semi-embedded and blended installation classes as structural zones."),
        ("020", "Ownership-and-Interface-Doctrine",
         "The 054/061/077 rule and the mount, firewall and aerodynamics splits, stated once."),
        ("030", "Access-and-Openability-Doctrine",
         "Structural doctrine of opening systems: doors, latches and hinge structure classes."),
    ]),
    "100": ("Nacelle-Structures", [
        "Nacelle structure as airframe structure: barrels, frames, skins, "
        "acoustic-structure integration and nacelle-mounted fitting provisions.",
        "Cowl and fairing surfaces are 054-700; the powerplant build-up "
        "discipline inside is 061-500.",
    ], [
        ("110", "Nacelle-Barrel-and-Frame-Structure", "Primary nacelle barrels, frames and longitudinal members."),
        ("120", "Nacelle-Skins-and-Acoustic-Structure", "Skin panels including acoustic-lining structural integration."),
        ("130", "Nacelle-Fitting-and-Equipment-Provisions", "Structural provisions for nacelle-mounted equipment and services."),
        ("140", "Nacelle-Drain-and-Vent-Structural-Paths", "Structural paths for the drain and vent provisions defined in 061-400."),
    ]),
    "200": ("Pylons-Mounts-and-Support-Structures", [
        "Pylon boxes, mount structures and support members transferring "
        "propulsion loads to the receiving structure.",
        "Requirements, stiffness targets and failure cases: 061-100 / 077-500; "
        "this section owns the structure that satisfies them.",
    ], [
        ("210", "Pylon-Primary-Box-Structure", "Pylon spars, ribs, skins and closure structure."),
        ("220", "Mount-Structures-and-Fittings", "Forward and aft mount structures, links and their fittings."),
        ("230", "Support-Struts-and-Auxiliary-Members", "Secondary support members and reaction structures."),
        ("240", "Pylon-to-Airframe-Interface-Structure", "Interface structure toward 057-720 and 053-800 attach provisions."),
        ("250", "Pylon-Systems-Corridor-Provisions", "Structural corridors for carrier lines, harnesses and services crossing the pylon (systems own their lines)."),
    ]),
    "300": ("Dorsal-and-Embedded-Propulsion-Integration", [
        "Integrated installations without a conventional discrete pylon: dorsal "
        "humps, semi-embedded and blended propulsion integration structures — "
        "support and load-transfer members, dorsal fairings, centerbody "
        "aerodynamic blending structure and boundary-layer-ingesting inlet "
        "structural surrounds.",
        "BLI class constraints are 091; propulsor units and their aero "
        "integration are 077; the receiving centerbody primary structure is "
        "053/057 per zoning — this section owns the integration structure "
        "between them.",
    ], [
        ("310", "Dorsal-Support-and-Load-Transfer-Structure", "Support frames and load-transfer members of dorsal-mounted propulsors."),
        ("320", "Dorsal-Fairings-and-Blending-Structure", "External fairing and blending structures over integrated installations."),
        ("330", "Embedded-Inlet-Structural-Surrounds", "Structural surrounds of embedded and boundary-layer-ingesting inlets; the functional inlet is the propulsion range."),
        ("340", "Embedded-Exhaust-Structural-Surrounds", "Structural surrounds and shielding of embedded exhaust paths."),
        ("350", "Inter-Propulsor-and-Multi-Unit-Integration-Structure", "Shared structure between adjacent integrated propulsors, including burst and containment interfaces (026, 062-500)."),
    ]),
    "400": ("Inlet-and-Exhaust-Structural-Interfaces", [
        "Structural interfaces of inlets and exhausts for conventional "
        "installations: lips, ducts as structure, exhaust surrounds and "
        "heat-affected structure.",
        "Functional inlet/exhaust performance and hardware belong to the "
        "propulsion ranges (065, 067); the structural interface is owned here.",
    ], [
        ("410", "Inlet-Lip-and-Duct-Structure", "Inlet lip and duct structural elements including anti-ice structural interfaces (030, 065-500)."),
        ("420", "Exhaust-Surround-and-Shield-Structure", "Exhaust-adjacent structure, shields and heat-affected reinforcement."),
        ("430", "Thrust-Reverser-Structural-Interfaces", "Structural interfaces to reverser provisions (067-800 owns the function class)."),
        ("440", "Auxiliary-Intake-and-Vent-Structural-Openings", "Secondary intakes, vents and their structural openings."),
    ]),
    "500": ("Attachments-and-Load-Transfer-Interfaces", [
        "The attachment architecture of the chapter: fuse and shear concepts, "
        "load-limiting and failure-ordering structure, and the declared "
        "interfaces to receiving-structure fittings.",
        "Joint practices: 051-4xx/5xx; receiving fittings: 053-800, 057-720.",
    ], [
        ("510", "Primary-Load-Path-Architecture", "Declared load paths from propulsor to receiving structure per installation class."),
        ("520", "Fuse-Shear-and-Load-Limiting-Structure", "Structural elements ordering failure and limiting load transfer."),
        ("530", "Interface-Control-to-Receiving-Structure", "Interface definition toward 053/057 fittings; one interface, two owners, no duplication."),
        ("540", "Separation-and-Departure-Considerations", "Structural considerations for controlled separation cases."),
    ]),
    "600": ("Fire-Thermal-and-Acoustic-Protection-Structures", [
        "Protection structure of the installation: firewall panels and seals as "
        "structure, thermal barriers, acoustic treatment structure.",
        "This section owns the physical implementation of fire barriers, thermal "
        "shields, acoustic liners, insulation supports and structural segregation "
        "provisions. It does not own hazard detection, extinguishing, environmental "
        "qualification or source-noise functions (026, 061-300, 067-600 and the "
        "environmental chapters own those).",
    ], [
        ("610", "Firewall-Panels-and-Seals-Structure", "Firewall structural panels, penetrations and seal landings."),
        ("620", "Thermal-Barrier-and-Insulation-Structure", "Thermal barrier structures and their attachments."),
        ("630", "Acoustic-Treatment-Structural-Integration", "Acoustic panel structure beyond the nacelle lining (054-120)."),
        ("640", "Drainage-and-Leak-Management-Structural-Provisions", "Structural provisions serving 061-400 leak-management zones."),
    ]),
    "700": ("Cowlings-Fairings-and-Access-Provisions", [
        "External openable and fixed surfaces: cowl doors, latching structure, "
        "fixed fairings and access provisions.",
        "Access requirements and maintainability doctrine: 061-700; the "
        "structural provisions are owned here.",
    ], [
        ("710", "Cowl-Doors-and-Latching-Structure", "Openable cowl structures, hinges and latch load paths."),
        ("720", "Fixed-Fairings-and-Panels", "Fixed aerodynamic fairing structures of the installation."),
        ("730", "Access-Doors-and-Quick-Access-Provisions", "Access openings and their reinforcement per 061-700 needs."),
        ("740", "Surface-Protection-and-Erosion-Films", "Protection film systems of installation surfaces (sibling of 057-010)."),
    ]),
    "800": ("Aerodynamic-and-Aeroelastic-Integration", [
        "Aero-structural integration of the installation: shaping structure for "
        "interference control, aeroelastic behavior of pylon-nacelle systems, "
        "flutter and whirl considerations as structural properties.",
        "Powerplant-side integration effects (distortion on the machine): "
        "061-800; vehicle aero class constraints: 091.",
    ], [
        ("810", "Interference-and-Junction-Shaping-Structure", "Junction fairing structure controlling aerodynamic interference."),
        ("820", "Pylon-Nacelle-Aeroelastic-Characteristics", "Aeroelastic and whirl-mode structural characteristics of the installation."),
        ("830", "Vibration-and-Dynamic-Environment-Structure", "Structural response doctrine to the propulsion dynamic environment (isolation requirements: 061-600)."),
    ]),
    "900": ("Sustainable-Propulsion-Installation-Provisions", [
        "Green-native installation structures: provisions specific to hydrogen, "
        "electric and distributed-propulsion installations, and circularity of "
        "installation structures.",
        "Carrier systems: 028; powertrains: 070-079; this section owns the "
        "structural provisions their installations demand.",
    ], [
        ("910", "Hydrogen-Installation-Structural-Provisions", "Structural provisions of hydrogen-fed installations: line corridors, venting paths, zone boundaries (028, 061-400, three-layer model)."),
        ("920", "Electric-and-Hybrid-Installation-Structural-Provisions", "Structures for heavy electric machines, power-electronics bays and HV corridor provisions (070-079, 079 safety zones)."),
        ("930", "Distributed-and-Multi-Propulsor-Installation-Structures", "Repeating installation structure classes for distributed arrays (077-300; wing-side 057-950)."),
        ("940", "Cryogenic-and-Superconducting-Line-Corridors", "Structural corridors and supports for cryogenic and superconducting runs (078-600, 085 graduation)."),
        ("950", "Installation-Circularity-and-Disassembly-Provisions", "Design-for-disassembly and material identification of installation structures (051-340)."),
    ]),
}

BOUNDARIES = (
    "Ownership rule: 054 owns the physical nacelle, pylon, fairing, mounting "
    "and propulsion-to-airframe structural integration. Propulsion ranges "
    "060-079 own machines, powertrains, propulsion functions and functional "
    "installation requirements (061 combustion installation discipline, "
    "077-500 electric-propulsor installation). 053 and 057 own the receiving "
    "centerbody, fuselage or wing primary structure and the corresponding "
    "airframe-side attachment provisions. Mount split: requirements, loads "
    "and failure cases 061-100 / 077-500; physical mount and support "
    "structure 054-200. Firewall split: zone definition, hazards and "
    "protection requirements 061-300 and 026; implementing firewall and "
    "segregation structure 054-600. Inlet and exhaust split: aerodynamic and "
    "functional requirements belong to 061-800, the relevant propulsion-"
    "machine chapters and 067; anti-ice and thermal provisions reference 030 "
    "and 065; physical structural interfaces, lips, ducts, load paths and "
    "surrounding structure belong to 054-400. Aerodynamic split: machine and "
    "installation effects 061-800; aerostructural and aeroelastic "
    "integration 054-800; configuration-class constraints 091. Protection "
    "split: 054-600 owns physical barriers, shields, liners, insulation "
    "supports and structural segregation; detection, extinguishing, "
    "environmental-control and source-noise functions remain in their "
    "functional chapters. Structural practices: 051. Type classes 090-099 "
    "constrain and reference this chapter and shall not duplicate it."
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


def subj_readme(section, subject, title, description):
    return (
        f"# {CH}-{subject} — {title.replace('-', ' ')}\n\n"
        f"**Section:** {CH}-{section} · **Subject:** {subject}\n\n"
        f"- {description}\n"
    )


def ch_readme():
    lines = [f"# {CH}_{CH_TITLE}", "",
             f"**Range:** 050-059_Primary-Structures-and-Programme-Interfaces · **Chapter:** {CH}",
             "", "## Scope", "", SCOPE, "", "## Integration chain", "", DIAGRAM,
             "", "## Section register", "", "| Section | Title | Subjects |",
             "|---|---|---|"]
    lines.extend(
        f"| {CH}-{code} | [{title.replace('-', ' ')}]({CH}-{code}_{title}/) | {len(subjects)} |"
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
        parser.error(f"Q+ATLANTIDE root not found under {root}; run from repo root, use --root, or pass --bootstrap.")
    chapter_dir = root / RANGE_REL / f"{CH}_{CH_TITLE}"
    plan = [(chapter_dir / "README.md", ch_readme(), True)]
    for code, (title, bullets, subjects) in S.items():
        section_dir = chapter_dir / f"{CH}-{code}_{title}"
        plan.append((section_dir / "README.md", sec_readme(code, title, bullets, subjects), True))
        plan.extend(
            (section_dir / f"{CH}-{subject}_{subject_title}/README.md",
             subj_readme(code, subject, subject_title, description), False)
            for subject, subject_title, description in subjects
        )
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
    mode = "dry-run" if args.dry_run else CH
    print(f"[{mode}] written={written} skipped={skipped} planned={len(plan)} at {chapter_dir}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        sys.exit(0)
