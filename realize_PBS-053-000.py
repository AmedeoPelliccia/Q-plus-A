#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
realize_PBS-053-000.py  (v2 — numerazione corretta)
Nodo PBS  eWTW-PBS-053-000_Fuselage-Wide-Tube.

Grammatica ×10 gerarchica:
    053-000          capitolo (questo nodo)
    053-000-000      capitolo generale
    053-SS0-000      sezione (tripletta centrale ×10), -000 = generale di sezione
    053-SS0-UU0      unita' (tripletta finale ×10), per breakdown piu' profondo

USO
    python3 realize_PBS-053-000.py                 # dalla root del repo Q-plus-A
    python3 realize_PBS-053-000.py /percorso/repo
"""
import os
import re
import sys
import shutil

OVERWRITE = True
CLEANUP_OLD = True  # rimuove i vecchi dir errati  053-000-0XX  (XX != 00)

NODE_REL = (
    "01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/"
    "01-02-01-01_MODELS/01-02-01-01-01_eWTW/"
    "01-02-01-01-01-01_SBS_System-Breakdown-Structure/"
    "01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/"
    "eWTW-PBS-000_Aircraft-Product/"
    "eWTW-PBS-050_Airframe-Structure/"
    "eWTW-PBS-053-000_Fuselage-Wide-Tube"
)
CHAP = "eWTW-PBS-053"           # prefisso capitolo per gli item del breakdown
NODE_ID = "eWTW-PBS-053-000"    # nome del dir nodo (capitolo)

# (sezione SS0, title, layer, owner, scope note)  ->  codice  053-SS0-000
SECTIONS = [
    ("000", "General", "STD", "Q-STRUCTURES",
     "Fuselage chapter general: WTW configuration, zoning, fuselage-station references and breakdown overview."),
    ("010", "Forward-Fuselage-Section", "STD", "Q-STRUCTURES",
     "Nose / Section 41: flight-deck structure, forward pressure-bulkhead interface, radome attach, nose-gear bay structure."),
    ("020", "Center-Fuselage-Section", "DIAMOND", "Q-STRUCTURES",
     "Section 43/44: wing-to-body join and center carry-through; integrates under-floor energy-carrier bay loads."),
    ("030", "Aft-Fuselage-Section", "STD", "Q-STRUCTURES",
     "Section 46/47: aft pressure-bulkhead interface and empennage attach interface."),
    ("040", "Tailcone-and-Auxiliary-Power-Module-Bay", "STD", "Q-STRUCTURES",
     "Section 48 tailcone; auxiliary-power-module mounting structure (engine/APU -> aux-power module, NORM-TERM-001)."),
    ("050", "Skin-Panels-and-Doublers", "STD", "Q-STRUCTURES",
     "Fuselage skin, lap/butt joints and doublers; standard practices per 051."),
    ("060", "Frames-Stringers-and-Longerons", "STD", "Q-STRUCTURES",
     "Circumferential frames, longitudinal stringers and longerons."),
    ("070", "Floor-Structure-Passenger-and-Cargo", "DIAMOND", "Q-STRUCTURES",
     "Passenger and cargo floor beams and grid; now also carries energy-carrier bay loads and associated crash cases."),
    ("080", "Pressure-Bulkheads", "STD", "Q-STRUCTURES",
     "Forward and aft pressure bulkheads."),
    ("090", "Keel-Beam-and-Major-Attach-Fittings", "DIAMOND", "Q-STRUCTURES",
     "Keel beam; wing / gear / empennage / pylon attach fittings plus energy-carrier mount fittings."),
    ("100", "Aerodynamic-Fairings", "STD", "Q-STRUCTURES",
     "Belly fairing and wing-body fairing."),
    ("110", "Energy-Carrier-Bay-Structural-Provisions", "STD-G", "Q-GREENTECH",
     "Dedicated under-floor energy-carrier (battery) bay: structural enclosure, crash protection, thermal/fire containment interface to 026-900; carrier owned by 028."),
]

GLYPH = {"STD": "STD", "DIAMOND": "\u25c7", "STD-G": "STD-G"}  # \u25c7 overlay


def write(path, text):
    if (not OVERWRITE) and os.path.exists(path):
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def cleanup_old(node):
    if not (CLEANUP_OLD and os.path.isdir(node)):
        return
    pat = re.compile(re.escape(NODE_ID) + r"-(\d{3})_")  # eWTW-PBS-053-000-XXX_
    for entry in os.listdir(node):
        m = pat.match(entry)
        if m and m.group(1) != "000":
            p = os.path.join(node, entry)
            if os.path.isdir(p):
                shutil.rmtree(p)


def code(mid):
    return "%s-%s-000" % (CHAP, mid)


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    node = os.path.join(base, NODE_REL)
    os.makedirs(node, exist_ok=True)
    cleanup_old(node)

    rows = ""
    links = ""
    reg = ("pbs_item_register:\n  node: %s\n  g_atlas: \"053\"\n"
           "  grammar: \"0CC-SS0-UU0 (x10 hierarchical)\"\n"
           "  model: eWTW\n  side: SSOT\n  sections:\n" % NODE_ID)
    for mid, title, lay, owner, note in SECTIONS:
        iid = code(mid)
        idir = os.path.join(node, "%s_%s" % (iid, title))
        os.makedirs(idir, exist_ok=True)
        write(os.path.join(idir, "pbs-item.yaml"),
              "pbs_item:\n  id: %s\n  title: %s\n  level: section\n"
              "  layer: \"%s\"\n  owner: %s\n  parent: %s\n  model: eWTW\n"
              "  side: SSOT\n  scope: \"%s\"\n  status: scaffold\n  version: \"1.0\"\n"
              % (iid, title.replace("-", " "), GLYPH[lay], owner, NODE_ID,
                 note.replace('"', "'")))
        write(os.path.join(idir, ".gitkeep"), "")
        rows += "| `%s` | %s | %s | %s |\n" % (
            iid, title.replace("-", " "), GLYPH[lay], owner)
        links += "- [`%s`](%s_%s) - %s | %s\n" % (
            iid, iid, title, title.replace("-", " "), GLYPH[lay])
        reg += ("    - {id: %s, title: %s, layer: \"%s\", owner: %s}\n"
                % (iid, title.replace("-", " "), GLYPH[lay], owner))

    write(os.path.join(node, "pbs-item-register.yaml"), reg)

    write(os.path.join(node, "pbs-node.yaml"),
          "pbs_node:\n  id: %s\n  title: Fuselage Wide-Tube\n"
          "  type: chapter\n  g_atlas: \"053\"\n  ata_origin: \"53\"\n"
          "  config: WTW (Wide Tube Wing)\n"
          "  grammar: \"0CC-SS0-UU0 (x10 hierarchical; -000 = general at each level)\"\n"
          "  parent: eWTW-PBS-050\n  model: eWTW\n  side: SSOT\n"
          "  member: \"-01_PBS\"\n  owner: Q-STRUCTURES\n  green_overlay: Q-GREENTECH\n"
          "  sections: %d\n  status: realized\n  version: \"2.0\"\n"
          % (NODE_ID, len(SECTIONS)))

    readme = """---
pbs_node: {nid}
title: Fuselage Wide-Tube
g_atlas: "053"
ata_origin: "53"
config: WTW (Wide Tube Wing)
grammar: "0CC-SS0-UU0 (x10 hierarchical; -000 = general at each level)"
model: eWTW
side: SSOT
member: "-01_PBS"
owner: Q-STRUCTURES
green_overlay: Q-GREENTECH
doctrine: green-native
status: realized
version: "2.0"
---

# {nid} - Fuselage Wide-Tube

Product node for the primary fuselage structure of the eWTW (WTW - Wide Tube Wing
configuration). Mirrors G-ATLAS `053` (ATA 53). SSOT-side; the AMM / SRM (PUB)
consume it one-way via `ssot-ref.yaml`.

## Numbering

`0CC-SS0-UU0`, x10 at each level, `-000` = general:
`053-000` chapter . `053-000-000` chapter general . `053-SS0-000` section
(general of section) . `053-SS0-UU0` unit.

## Index

- [Scope & Boundary](#scope--boundary)
- [Section Breakdown](#section-breakdown)
- [Cross-References](#cross-references)
- [Green-Native Notes](#green-native-notes)
- [References](#references)

## Scope & Boundary

**Owns** - the load-carrying fuselage product: major barrel sections (forward /
center / aft / tailcone), skin, frames-stringers-longerons, passenger and cargo
floor, pressure bulkheads, keel beam and major attach fittings, aerodynamic
fairings, and the **energy-carrier bay structural provisions**. Door, window,
wing, empennage, gear and pylon *cutout and attach structure* is owned here; the
*assemblies* that fit those interfaces are owned by their own chapters.

**Cedes** - door assemblies -> `052`; window assemblies -> `056`; wing ->
`057`; stabilizers/empennage -> `055`; landing-gear *system* -> `032`;
pylons/nacelles -> `054`; the energy carrier itself -> `028`; fire/thermal
containment function -> `026-900`; fasteners/repair practices -> `051`.

## Section Breakdown

| Section | Title | Layer | Owner |
|---|---|:--:|---|
{rows}
> Layer: **STD** carries (energy-neutral) . **\u25c7** green overlay . **STD-G** green delta.
> Each section's `-000` is its general; deeper units populate the final triplet (`053-SS0-UU0`).

{links}
## Cross-References

| This node references | Owned by | Why |
|---|---|---|
| Door assemblies | `052` Doors | cutout/surround structure stays here |
| Window assemblies | `056` Windows | window-belt structure stays here |
| Wing | `057` Wing | body-side attach fitting here, wing-side there |
| Stabilizers / empennage | `055` Stabilizers-Empennage | body-side attach here |
| Landing-gear system | `032` Landing Gear | gear bays/fittings structure here |
| Pylons / nacelles | `054` Nacelles-and-Pylons | pylon-to-body attach here |
| Energy carrier (battery) | `028` Energy-Carrier-Storage | bay *structure* here, carrier there |
| Fire / thermal containment | `026-900` Fire Protection | structural interface here |
| Standard practices | `051` Standard-Practices-Structures | fasteners, repairs |

## Green-Native Notes

The fuselage is mostly energy-neutral structure (STD), but the electric WTW adds
one defining section and three overlays:

- **`053-110-000` Energy-Carrier Bay Structural Provisions** - a dedicated
  under-floor enclosure for the battery packs: structural cassette, crash-load
  protection, and the thermal/fire **containment interface** to `026-900`. No
  conventional analogue (a kerosene tank is a wing-box volume, not a fuselage
  structural bay). -> **STD-G**.
- **\u25c7 overlays** - three conventional sections now also carry energy-carrier
  mass and its crash cases: `053-020-000` Center Fuselage Section (bay
  integration), `053-070-000` Floor Structure (bay support + crash), and
  `053-090-000` Keel Beam & Major Attach Fittings (energy-carrier mount
  fittings). -> **\u25c7**.

Terminology per **G-ATLAS-NORM-TERM-001**: engine/APU -> auxiliary-power module
(bay in `053-040-000`).

## References

[^ata53]: ATA 100 / iSpec 2200 - Chapter 53 *Fuselage* (heritage scope reference).
[^carrier]: G-ATLAS `028` Energy-Carrier-Storage (battery packs and their limits).
[^fire]: G-ATLAS `026-900` Fire Protection (energy-carrier thermal/fire containment).
[^sp]: G-ATLAS `051` Standard-Practices-Structures (fasteners, repair allowables).
""".format(nid=NODE_ID, rows=rows, links=links)

    write(os.path.join(node, "README.md"), readme)

    print("OK: %s realizzato (v2) - %d sezioni (incl. generale)." % (NODE_ID, len(SECTIONS)))
    print("Path: %s" % os.path.normpath(node))


if __name__ == "__main__":
    main()
