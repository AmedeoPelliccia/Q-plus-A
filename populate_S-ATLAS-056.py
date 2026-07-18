#!/usr/bin/env python3
"""Populate the programme-agnostic S-ATLAS 056 Windows chapter."""

import argparse
import sys
from pathlib import Path

CH = "056"
CH_TITLE = "Windows"
RANGE_REL = (
    "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
    "000-099_S-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces"
)

SCOPE = (
    "Transparency assemblies as programme-agnostic classes: flight-compartment "
    "windows including openable direct-vision classes, passenger-cabin windows, "
    "door and hatch windows, sensor and special apertures, retention and sealing "
    "systems, transparency materials and optical properties, environmental "
    "protection and heating interfaces, monitoring and inspection, and advanced "
    "sustainable window architectures. 056 owns the transparency assembly — "
    "panes, interlayers, assembly-integral frame, retainers and seals; the "
    "receiving structure owns the opening, posts, surround reinforcement and "
    "load path (053 fuselage; 052 where the carrier is a door or hatch leaf). "
    "Instance counts and arrangements are downstream matters."
)

DIAGRAM = """```mermaid
flowchart LR
  subgraph CLASSES["Transparency classes"]
    W["056-100 Flight-Compartment<br>Windows"]
    P["056-200 Passenger-Cabin<br>Windows"]
    D["056-300 Door and<br>Hatch Windows"]
    A["056-400 Sensor and<br>Special Apertures"]
  end
  R["056-500 Retention, Seals<br>and Pressure Boundary"] --- CLASSES
  M["056-600 Materials and<br>Optical Properties"] --- CLASSES
  E["056-700 Environmental Protection<br>and Heating Interfaces"] --- CLASSES
  H["056-800 Monitoring, Inspection<br>and Health"] --- CLASSES
  N["056-900 Advanced and Sustainable<br>Window Architectures"] -. "applies across" .-&gt; CLASSES
  CLASSES --&gt;|"interface loads and<br>attachment reactions"| RS["Receiving structure<br>053 fuselage · 052 door/hatch leaf"]
  E -. "heating, wiping and<br>ice function" .-&gt; X030["030-4xx"]
  N -. "virtual-window and dimming<br>control functions" .-&gt; X044["044"]
```"""

# Section code -> (title, scope bullets, [(subject code, title, summary)])
S = {
    "000": ("General", [
        "Chapter doctrine: transparency classes and zoning, optical and structural roles, and the assembly-vs-opening rule.",
        "The rule generalizes 052: the transparency assembly is owned here; the opening, posts and reinforcement belong to the receiving or carrying chapter.",
    ], [
        ("010", "Transparency-Classes-and-Doctrine", "Class taxonomy, pressure-bearing roles and fail-safe pane doctrine."),
        ("020", "Optical-Requirements-Doctrine", "Optical quality classes, distortion and visibility doctrine."),
        ("030", "Bird-Strike-and-Impact-Doctrine", "Impact-resistance doctrine as a class property of forward-facing transparencies."),
        ("040", "Window-Zoning-and-Reference-Conventions", "Addressing and zoning of transparency installations."),
    ]),
    "100": ("Flight-Compartment-Windows", [
        "Windshield and cockpit window classes: fixed panels, openable direct-vision classes and their sealing and retention.",
        "Windshield posts and surround structure are 053; heating, wiping and rain-removal functions are 030-4xx.",
    ], [
        ("110", "Windshield-Panel-Assemblies", "Windshield pane build-ups, interlayers and assembly-integral framing."),
        ("120", "Direct-Vision-and-Openable-Window-Assemblies", "Openable cockpit window class: assembly, guidance and its dedicated sealing."),
        ("130", "Cockpit-Side-and-Fixed-Window-Assemblies", "Fixed side-window assemblies of the flight compartment."),
        ("140", "Flight-Compartment-Retention-and-Fail-Safe-Provisions", "Retention systems and fail-safe pane provisions of cockpit transparencies."),
        ("150", "Heated-Element-and-Sensor-Integration-Provisions", "Assembly-side provisions of heating films and sensors (030-420 function; 034 data users)."),
    ]),
    "200": ("Passenger-Cabin-Windows", [
        "Cabin window assembly class: outer and inner panes, seals, retainers and reveal interfaces.",
        "Cabin reveals, shades and furnishing surrounds are 025; the transparency assembly is owned here.",
    ], [
        ("210", "Cabin-Window-Pane-Assemblies", "Outer structural pane, inner pane and vented-interspace class."),
        ("220", "Cabin-Window-Retainers-and-Clips", "Retention hardware classes of cabin windows."),
        ("230", "Cabin-Window-Seals", "Sealing systems of cabin window assemblies."),
        ("240", "Reveal-and-Furnishing-Interface-Provisions", "Assembly-side interfaces toward cabin reveals and shades (025)."),
        ("250", "Enlarged-and-Special-Format-Cabin-Windows", "Large-format cabin transparency classes and their retention doctrine."),
    ]),
    "300": ("Door-and-Hatch-Windows", [
        "Window classes carried by door and hatch leaves: viewing ports, door windows and escape-hatch windows.",
        "The leaf is 052; the transparency assembly it carries is owned here — one interface, two owners, no duplication.",
    ], [
        ("310", "Passenger-Door-Window-Assemblies", "Door window class: panes, integral frame and seals toward the leaf."),
        ("320", "Escape-Hatch-Window-Assemblies", "Hatch window class carried by 052-200 leaves."),
        ("330", "Service-and-Cargo-Door-Viewing-Ports", "Viewing-port classes of service and cargo doors."),
        ("340", "Door-Window-Retention-and-Sealing", "Retention and sealing toward the carrying leaf structure."),
    ]),
    "400": ("Sensor-and-Special-Apertures", [
        "Transparent apertures serving sensors and special functions: vision-system windows, camera apertures and instrument ports.",
        "The sensing systems are 034 and their chapters; the transparency and its mounting are owned here.",
    ], [
        ("410", "Vision-System-Window-Assemblies", "Aperture windows of enhanced-vision sensors (034-270 system)."),
        ("420", "Camera-and-Monitoring-Apertures", "Camera aperture classes including external-monitoring installations (044-400 users)."),
        ("430", "Instrument-and-Special-Ports", "Special transparent port classes."),
        ("440", "Aperture-Environmental-Protection", "Contamination, heating and protection provisions of apertures (030 functions)."),
    ]),
    "500": ("Retention-Seals-and-Pressure-Boundary", [
        "Cross-class retention and sealing technology: the transparency as pressure boundary, its drainage and misting management.",
        "Cabin-pressure control is 021-3xx; the boundary implementation is owned here (052-800 sibling).",
    ], [
        ("510", "Retention-System-Architectures", "Bolted, clamped and bonded retention classes and their failure ordering."),
        ("520", "Pressure-Boundary-Sealing", "Primary sealing of transparencies as pressure boundary."),
        ("530", "Interspace-Venting-and-Misting-Management", "Vented interspace, desiccation and misting provisions."),
        ("540", "Drainage-and-Environmental-Sealing", "Drainage paths and environmental sealing of window installations."),
    ]),
    "600": ("Transparency-Materials-and-Optical-Properties", [
        "Transparency material classes and their optical and structural properties: glass, stretched acrylic, polycarbonate, interlayers and coatings.",
        "Generic materials practices are 051-3xx; transparency-specific behavior is owned here.",
    ], [
        ("610", "Glass-and-Glass-Laminate-Classes", "Glass and laminated-glass transparency classes."),
        ("620", "Acrylic-and-Polycarbonate-Classes", "Stretched-acrylic and polycarbonate classes and their aging behavior."),
        ("630", "Interlayers-and-Bonding-Systems", "Interlayer and bonding system classes of laminated transparencies."),
        ("640", "Coatings-Conductive-and-Hydrophobic", "Coating classes: conductive heating films, hydrophobic and protective coatings."),
        ("650", "Optical-Quality-and-Aging-Characteristics", "Optical classes, crazing and aging characteristics as declared properties."),
    ]),
    "700": ("Environmental-Protection-and-Heating-Interfaces", [
        "Assembly-side interfaces of environmental functions: anti-ice and demist heating, rain removal, solar and UV management.",
        "The functions are 030-4xx; the provisions and interfaces are owned here.",
    ], [
        ("710", "Heating-and-Demist-Interface-Provisions", "Assembly interfaces of windshield and window heating (030-420/440 functions)."),
        ("720", "Rain-Removal-Interface-Provisions", "Interfaces of wiper and rain-removal systems (030-410) including hydrophobic strategy."),
        ("730", "Solar-and-UV-Management", "Solar-load and UV management of transparencies; dimming technology per 056-910."),
        ("740", "Erosion-and-External-Protection", "External protection of transparencies against erosion and environment."),
    ]),
    "800": ("Monitoring-Inspection-and-Health", [
        "Inspection and health of transparencies: damage classes, heater monitoring interfaces and data paths.",
        "NDI standards are 051-140; maintenance data flows via 045.",
    ], [
        ("810", "Transparency-Damage-Classes-and-Inspection", "Crazing, delamination, arcing and impact damage classes and inspection doctrine."),
        ("820", "Heater-Element-Monitoring-Interfaces", "Monitoring interfaces of heating films (030 function, 045 data)."),
        ("830", "Health-Data-and-Records", "Transparency health records toward onboard maintenance (045)."),
    ]),
    "900": ("Advanced-and-Sustainable-Window-Architectures", [
        "Green-native window block: electrochromic dimming, windowless and virtual-window provisions, advanced lightweight transparencies and thermal-performance glazing.",
        "Display and dimming control functions are 044; class constraints on window arrangements are 09x; the window-side implementation is owned here.",
    ], [
        ("910", "Electrochromic-and-Dimmable-Window-Systems", "Dimmable transparency classes; control function 044, electrical supply 024, window-side implementation here."),
        ("920", "Windowless-and-Virtual-Window-Provisions", "Structural blanking, camera apertures (056-420) and interfaces of virtual-window cabins; display function 044-200, class constraints 09x."),
        ("930", "Advanced-Lightweight-Transparencies", "Lightweight and hybrid transparency classes reducing mass and thermal load."),
        ("940", "Thermal-Performance-Glazing", "Glazing classes reducing cabin thermal loads (021 load relief)."),
        ("950", "Smart-Sensing-Transparencies", "Transparencies with embedded sensing (042 hosting, 045 data)."),
        ("960", "Transparency-Circularity-and-Disassembly", "Material identification and end-of-life provisions of transparencies (051-340)."),
    ]),
}

BOUNDARIES = (
    "Assembly versus receiving structure: 056 owns panes, interlayers, assembly-integral frames, retainers and seals; "
    "053 owns fuselage openings, windshield posts and surround reinforcement; 052 owns the door or hatch leaf carrying a "
    "window assembly. Heating, demist, wiping and rain-removal functions: 030-4xx; assembly-side provisions 056-150/7xx. "
    "Cabin-pressure function: 021-3xx; boundary implementation 056-5xx. Cabin reveals, shades and furnishings: 025. "
    "Vision and sensing systems: 034 and their chapters; apertures 056-400. Display and dimming control functions: 044; "
    "window-side implementation 056-910/920. Materials practices: 051-3xx generic, transparency-specific behavior "
    "056-600; NDI standards 051-140. Lights and lenses: 033. Placards: 011. Type classes 090-099 constrain window "
    "arrangements and shall not duplicate this chapter."
)


def sec_readme(code, title, bullets, subjects):
    lines = [f"# {CH}-{code} — {title.replace('-', ' ')}", "",
             f"**Chapter:** {CH}_{CH_TITLE} · **Section:** {code}", ""]
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
    lines = [f"# {CH}_{CH_TITLE}", "",
             "**Range:** 050-059_Primary-Structures-and-Programme-Interfaces · "
             f"**Chapter:** {CH}", "", "## Scope", "", SCOPE, "",
             "## Integration chain", "", DIAGRAM, "", "## Section register", "",
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
