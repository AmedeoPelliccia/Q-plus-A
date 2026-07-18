#!/usr/bin/env python3
"""Populate the S-ATLAS 052 Doors chapter."""

import argparse
import sys
from pathlib import Path

CH = "052"
CH_TITLE = "Doors"
RANGE_REL = (
    "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
    "000-099_S-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces"
)

SCOPE = (
    "Door assemblies and associated mechanisms as programme-agnostic classes: "
    "passenger and crew doors, emergency exits and escape hatches, cargo doors, "
    "service and access doors, integral boarding stairs, common actuation-latching-"
    "locking technology, door-state sensing and alerting interfaces, seals and "
    "pressure-boundary provisions, and advanced sustainable door architectures. "
    "052 owns the door leaf, door-integral frame, hinges, guides, actuators, "
    "latches, locks, seals, door-side sensing and local mechanisms; the receiving "
    "airframe chapter (053 fuselage, 057 wing, or the relevant structural chapter) "
    "owns the opening, surrounding frames, sill beams, pressure-shell reinforcement "
    "and the airframe-side load path. 052 covers controlled closure assemblies for "
    "personnel passage, payload access, servicing access or emergency egress; small "
    "removable inspection panels, system-specific covers, nacelle cowlings and "
    "fairing access panels remain with their parent structure or system. Instance "
    "quantities, locations and arrangements are downstream matters."
)

DIAGRAM = """```mermaid
flowchart LR
  subgraph CLASSES["Door classes"]
    P["052-100 Passenger<br>and Crew"]
    E["052-200 Emergency Exits<br>and Hatches"]
    G["052-300 Cargo"]
    V["052-400 Service<br>and Access"]
    A["052-500 Integral Stairs"]
  end
  M["052-600 Mechanisms,<br>Latching and Locking"] --- CLASSES
  W["052-700 Door-State Sensing,<br>Monitoring and Alerting"] --- CLASSES
  Z["052-800 Seals and<br>Pressure Boundary"] --- CLASSES
  N["052-900 Advanced and<br>Sustainable Architectures"] -. "applies across" .-> CLASSES
  R["Receiving primary structure<br>053 fuselage · 057 wing"]
  CLASSES -->|"interface loads and<br>attachment reactions"| R
  W -. "warning logic and presentation" .-> X031["031-500"]
  Z -. "cabin-pressure function" .-> X021["021-300/320"]
  CLASSES -. "gear doors excluded" .-> X032["032"]
  CLASSES -. "evacuation equipment excluded" .-> X025["025-600"]
```"""

# Section code -> (title, scope bullets, [(subject code, title, summary)])
S = {
    "000": ("General", [
        "Chapter doctrine: door classes and zoning, plug and non-plug principles, "
        "common hardware, and the openability-and-rescue doctrine.",
        "Instance counts and station locations are programme matter; the chapter "
        "documents door technology as classes.",
    ], [
        ("010", "Door-Classes-Zoning-and-Doctrine", "Plug/non-plug doctrine, class taxonomy and zoning conventions."),
        ("020", "Common-Seals-and-Retainers", "Seal and retainer hardware classes shared across door types."),
        ("030", "Common-Locking-Pins-and-Ground-Security", "Key locks, strap-locks, pins and ground-security hardware classes."),
        ("040", "Openability-and-Rescue-Doctrine", "External opening, rescue access and marking doctrine (011 placards interface)."),
    ]),
    "100": ("Passenger-and-Crew-Doors", [
        "Passenger and crew door class: structure, guidance, mechanisms, residual-pressure provisions, assist and evacuation interfaces.",
        "Slide and raft equipment is 025-6xx; the door-side structural and girt interfaces are owned here.",
    ], [
        ("110", "Door-Skin-and-Structure", "Door skins, internal structure and fittings as a class."),
        ("120", "Hinge-Support-Arm-and-Guidance", "Support arms, hinges and guidance kinematics structure."),
        ("130", "Latching-Box-Mechanisms-and-Fittings", "Latch box mechanisms, shafts and their fittings."),
        ("140", "Vent-Flaps-and-Residual-Pressure-Provisions", "Vent-flap structure and residual-pressure protection provisions (function interlocks per 052-620)."),
        ("150", "Dampers-Deflectors-and-Assist", "Dampers, airstream deflectors and opening-assist elements."),
        ("160", "Emergency-Opening-and-Power-Assist", "Emergency opening systems as a class — stored-energy and powered assist; more-electric evolution per 052-910."),
        ("170", "Slide-Interface-Girt-Bar-and-Evacuation-Provisions", "Girt-bar, slide attachment and evacuation structural provisions (equipment: 025-650)."),
        ("180", "Flight-Deck-Security-Door", "Reinforced crew-compartment door class: structure, locking and access-control provisions."),
    ]),
    "200": ("Emergency-Exits-and-Escape-Hatches", [
        "Escape hatch and emergency exit classes: structure, latching, seals and environmental provisions.",
        "Egress-path class constraints for novel types are 091-600; the hatch technology is owned here.",
    ], [
        ("210", "Hatch-Skin-and-Structure", "Hatch structural class including overwing types."),
        ("220", "Hatch-Latching-and-Locks", "Hatch latch and lock mechanisms."),
        ("230", "Hatch-Seals", "Hatch sealing systems."),
        ("240", "Ice-Breakers-and-Environmental-Provisions", "Ice-breaker and environmental hardware; ice-protection function is 030."),
        ("250", "Egress-Path-Structural-Provisions", "Door/hatch-side structural provisions of egress paths."),
    ]),
    "300": ("Cargo-Doors", [
        "Cargo door class: structure, support, latching with indication provisions, actuation provisions and sealing.",
        "Compartments are 050-1xx; loading systems are 050-2xx; the door is owned here.",
    ], [
        ("310", "Cargo-Door-Structure", "Cargo door structural class."),
        ("320", "Cargo-Door-Hinge-and-Support", "Hinges, supports and hold-open provisions."),
        ("330", "Cargo-Latching-Locking-and-Indication-Provisions", "Latch/lock trains and lock-indication provisions (function per 052-7xx)."),
        ("340", "Cargo-Door-Actuation-Provisions", "Powered actuation provisions; more-electric class per 052-910."),
        ("350", "Cargo-Door-Seals-and-Environmental", "Cargo door sealing and drainage provisions."),
    ]),
    "400": ("Service-and-Access-Doors", [
        "Service, access and equipment-bay doors as classes, including energy servicing access.",
        "Servicing operations are 012; carrier systems are 028; the access doors are owned here.",
    ], [
        ("410", "Service-Door-Classes", "General service door classes and their hardware."),
        ("420", "Access-Panel-Doors-and-Quick-Release", "Quick-release access door classes (061-700 and 057-020 siblings)."),
        ("430", "Energy-Service-Access-Doors", "Access doors of energy-carrier reception points (028 interface; servicing 012-110)."),
        ("440", "Avionics-and-Equipment-Bay-Doors", "Equipment and avionics bay door classes."),
    ]),
    "500": ("Integral-Stairs-and-Boarding-Provisions", [
        "Integral boarding stairs and ground-autonomy boarding provisions.",
        "Regional and commuter class constraints (093) reference this technology for ground autonomy.",
    ], [
        ("510", "Airstair-Structure", "Integral stair structural class."),
        ("520", "Airstair-Mechanism-and-Actuation", "Stair deployment mechanisms and powered actuation provisions."),
        ("530", "Boarding-Interface-and-Ground-Autonomy-Provisions", "Boarding interfaces supporting autonomous turnaround (003, 010-019 operations)."),
    ]),
    "600": ("Door-Mechanisms-Latching-and-Locking", [
        "Common mechanism technology across door classes: latch and lock architectures, interlocks, actuation classes and rigging provisions.",
        "Cabin-pressure function is 021-3xx; the interlock provisions are owned here.",
    ], [
        ("610", "Latch-and-Lock-Architectures", "Latching and locking architecture classes and their failure ordering."),
        ("620", "Interlock-and-Safety-Logic-Provisions", "Residual-pressure and flight-lock interlock provisions (021-320 function)."),
        ("630", "Manual-and-Powered-Actuation-Classes", "Manual, assisted and powered actuation classes."),
        ("640", "Mechanism-Health-and-Rigging-Provisions", "Rigging, wear and health provisions of door mechanisms (045 data path)."),
    ]),
    "700": ("Door-State-Sensing-Monitoring-and-Alerting-Interfaces", [
        "Sensing and interface provisions of doors: position and lock sensing, warning interfaces and pressure interlocks.",
        "Warning presentation and central warning are 031-5xx; this section owns the door-side provisions.",
    ], [
        ("710", "Position-and-Lock-Sensing-Provisions", "Door and lock position sensing provisions as classes."),
        ("720", "Warning-Interface-Provisions", "Door-side interfaces to central warning (031-500 owns the function)."),
        ("730", "Cabin-Pressure-Interlock-Interfaces", "Interfaces to pressurization interlocks (021-320)."),
        ("740", "Data-and-Maintenance-Interfaces", "Door data toward onboard maintenance (045)."),
    ]),
    "800": ("Door-Seals-Pressure-Boundary-and-Environmental-Interfaces", [
        "Sealing systems and environmental interfaces of doors: pressure seals, drainage, acoustic-thermal sealing and heating interfaces.",
        "Heating function is 030 (passenger-door heating class); provisions are owned here.",
    ], [
        ("810", "Primary-Pressure-Seals", "Pressure seal systems and their landings."),
        ("820", "Environmental-Seals-and-Drainage", "Weather sealing and drainage provisions."),
        ("830", "Acoustic-and-Thermal-Sealing", "Acoustic and thermal sealing classes (025-8xx insulation interfaces)."),
        ("840", "Door-Heating-Interfaces", "Structural provisions of door heating (030 owns the function)."),
    ]),
    "900": ("Advanced-and-Sustainable-Door-Architectures", [
        "Green-native door block: more-electric actuation, lightweight structures, energy-carrier bay doors, novel egress technology, smart sensing and circularity.",
        "Type classes constrain (091-600 evacuation); maturity-gated concepts incubate in 080-089.",
    ], [
        ("910", "More-Electric-Door-Actuation", "Electric actuation replacing stored-gas and pneumatic assist classes (070-079 practices; 024 supply)."),
        ("920", "Lightweight-and-Thermoplastic-Door-Structures", "Thermoplastic and advanced-composite door structures (051-320, 051-230)."),
        ("930", "Energy-Carrier-Bay-Door-Systems", "Doors of energy-carrier bays: venting-compatible sealing, zone boundaries and access interlocks (050-530, 028, three-layer model)."),
        ("940", "Novel-Egress-Architectures-for-New-Types", "Egress door technology for unconventional configurations; 091-600 constrains, technology owned here."),
        ("950", "Smart-Door-Sensing-and-Health", "Embedded sensing and health monitoring of doors (042 hosting, 045 data)."),
        ("960", "Door-Circularity-and-Disassembly", "Design-for-disassembly and material identification (051-340)."),
    ]),
}

BOUNDARIES = (
    "Door assembly versus receiving structure: 052 owns the door leaf, door-integral "
    "frame, hinges, guides, mechanisms, locks, seals and local sensing; 053, 057 or "
    "the relevant structural chapter owns the opening, surrounding primary structure, "
    "reinforcement and airframe-side load path. Landing-gear doors: 032. Nacelle "
    "cowlings and propulsion access panels: 054-700. Evacuation equipment: 025-6xx; "
    "door-side girt bars and deployment interfaces: 052-170. Warning split: door-state "
    "sensing and local interfaces 052-700; aircraft-level warning logic and presentation "
    "031-5xx. Pressure split: seals, pressure-boundary implementation and residual-"
    "pressure interlock provisions 052-800 and 052-620; cabin-pressure control and "
    "relief function 021-3xx. Heating split: function 030; door-integrated provisions "
    "052-840. Energy-carrier servicing: operations 012, systems 028, controlled-access "
    "doors 052-430, bay provisions 050-530. Cargo and loading functions: 050. Placards: "
    "011. Practices: 051. Type classes 090-099 constrain quantities, locations and "
    "egress geometry and shall not duplicate this chapter."
)


def sec_readme(code, title, bullets, subjects):
    lines = [f"# {CH}-{code} — {title.replace('-', ' ')}", "",
             f"**Chapter:** {CH}_{CH_TITLE} · **Section:** {code}", ""]
    lines.extend(f"- {bullet}" for bullet in bullets)
    lines.extend(["", "## Subjects", "", "| Subject | Title |", "|---|---|"])
    lines.extend(
        f"| {CH}-{subject} | [{subject_title.replace('-', ' ')}]"
        f"({CH}-{subject}_{subject_title}/) |"
        for subject, subject_title, _ in subjects
    )
    return "\n".join(lines) + "\n"


def subj_readme(section, subject, title, summary):
    return (f"# {CH}-{subject} — {title.replace('-', ' ')}\n\n"
            f"**Section:** {CH}-{section} · **Subject:** {subject}\n\n"
            f"- {summary}\n")


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
    return "\n".join(lines) + "\n"


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
