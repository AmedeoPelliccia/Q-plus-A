#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
realize_PBS-053-010-000.py
Nodo PBS  eWTW-PBS-053-010-000_Forward-Fuselage-Section  ->  breakdown in SUBJECT.

Grammatica ×10 (livello subject = tripletta finale):
    053-010-000      sezione (questo nodo) = generale di sezione
    053-010-010      subject 01
    053-010-020      subject 02  ...

USO
    python3 realize_PBS-053-010-000.py                 # dalla root del repo Q-plus-A
    python3 realize_PBS-053-010-000.py /percorso/repo
"""
import os
import re
import sys
import shutil

OVERWRITE = True
CLEANUP_OLD = True

NODE_REL = (
    "01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/"
    "01-02-01-01_MODELS/01-02-01-01-01_eWTW/"
    "01-02-01-01-01-01_SBS_System-Breakdown-Structure/"
    "01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/"
    "eWTW-PBS-000_Aircraft-Product/"
    "eWTW-PBS-050_Airframe-Structure/"
    "eWTW-PBS-053-000_Fuselage-Wide-Tube/"
    "eWTW-PBS-053-010-000_Forward-Fuselage-Section"
)
SEC = "eWTW-PBS-053-010"          # prefisso sezione per i subject
NODE_ID = "eWTW-PBS-053-010-000"  # nome del dir nodo (sezione)

# (subject UU0, title, layer, owner, scope note)  ->  codice  053-010-UU0
SUBJECTS = [
    ("010", "Radome-and-Nose-Cone-Attach-Structure", "STD", "Q-STRUCTURES",
     "Nose radome shell mounting and attach frame/bulkhead; weather-radar antenna owned by 034, radome de-ice by 030."),
    ("020", "Flight-Deck-Enclosure-and-Windshield-Post-Structure", "STD", "Q-STRUCTURES",
     "Windshield posts, cockpit crown/roof and windshield frame structure; glazing owned by 056, windshield heat by 030."),
    ("030", "Forward-Pressure-Bulkhead", "STD", "Q-STRUCTURES",
     "Nose forward pressure dome (physical instance); common bulkhead design basis catalogued in 053-080."),
    ("040", "Nose-Landing-Gear-Bay-Structure", "STD", "Q-STRUCTURES",
     "NLG wheel well, trunnion and drag-strut support fittings; landing-gear system owned by 032."),
    ("050", "Forward-Equipment-Bay-Structure", "STD", "Q-STRUCTURES",
     "E/E (avionics) bay structure below flight deck; equipment owned by 025, electrical/avionics by 024/040, bay cooling by 021."),
    ("060", "Nose-Section-Skin-Frames-and-Stringers", "STD", "Q-STRUCTURES",
     "Nose-zone skin panels, frames and stringers; element design basis in 053-050 / 053-060."),
    ("070", "Forward-to-Center-Production-Join", "STD", "Q-STRUCTURES",
     "Section 41-to-43/44 production splice frame and fastener system."),
]

GLYPH = {"STD": "STD", "DIAMOND": "\u25c7", "STD-G": "STD-G"}  # ◇ overlay


def write(path, text):
    if (not OVERWRITE) and os.path.exists(path):
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def cleanup_stub_and_old(node):
    if not os.path.isdir(node):
        return
    # rimuove lo stub di sezione lasciato dallo script di capitolo
    for leftover in ("pbs-item.yaml", ".gitkeep"):
        p = os.path.join(node, leftover)
        if os.path.exists(p):
            os.remove(p)
    # rimuove eventuali subject dir malformati (non 053-010-UU0)
    if CLEANUP_OLD:
        good = re.compile(re.escape(SEC) + r"-\d{3}_")
        for entry in os.listdir(node):
            full = os.path.join(node, entry)
            if os.path.isdir(full) and entry.startswith("eWTW-PBS-") and not good.match(entry):
                shutil.rmtree(full)


def code(uu):
    return "%s-%s" % (SEC, uu)


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    node = os.path.join(base, NODE_REL)
    os.makedirs(node, exist_ok=True)
    cleanup_stub_and_old(node)

    rows = ""
    links = ""
    reg = ("pbs_item_register:\n  node: %s\n  level: section\n  g_atlas: \"053\"\n"
           "  section: \"053-010\"\n  grammar: \"0CC-SS0-UU0 (subjects on final triplet)\"\n"
           "  model: eWTW\n  side: SSOT\n  subjects:\n" % NODE_ID)
    for uu, title, lay, owner, note in SUBJECTS:
        iid = code(uu)
        idir = os.path.join(node, "%s_%s" % (iid, title))
        os.makedirs(idir, exist_ok=True)
        write(os.path.join(idir, "pbs-item.yaml"),
              "pbs_item:\n  id: %s\n  title: %s\n  level: subject\n"
              "  layer: \"%s\"\n  owner: %s\n  parent: %s\n  model: eWTW\n"
              "  side: SSOT\n  scope: \"%s\"\n  status: scaffold\n  version: \"1.0\"\n"
              % (iid, title.replace("-", " "), GLYPH[lay], owner, NODE_ID,
                 note.replace('"', "'")))
        write(os.path.join(idir, ".gitkeep"), "")
        rows += "| `%s` | %s | %s | %s |\n" % (
            iid, title.replace("-", " "), GLYPH[lay], owner)
        links += "- [`%s`](./%s_%s/) - %s | %s\n" % (
            iid, iid, title, title.replace("-", " "), GLYPH[lay])
        reg += ("    - {id: %s, title: %s, layer: \"%s\", owner: %s}\n"
                % (iid, title.replace("-", " "), GLYPH[lay], owner))

    write(os.path.join(node, "pbs-item-register.yaml"), reg)

    write(os.path.join(node, "pbs-node.yaml"),
          "pbs_node:\n  id: %s\n  title: Forward Fuselage Section\n"
          "  type: section\n  level: section\n  g_atlas: \"053\"\n"
          "  section: \"053-010\"\n  zone: \"Nose / Section 41\"\n"
          "  grammar: \"0CC-SS0-UU0 (subjects on final triplet; -000 = section general)\"\n"
          "  parent: eWTW-PBS-053-000\n  model: eWTW\n  side: SSOT\n"
          "  member: \"-01_PBS\"\n  owner: Q-STRUCTURES\n  layer: \"STD\"\n"
          "  subjects: %d\n  status: realized\n  version: \"1.0\"\n"
          % (NODE_ID, len(SUBJECTS)))

    readme = """---
pbs_node: {nid}
title: Forward Fuselage Section
type: section
g_atlas: "053"
section: "053-010"
zone: "Nose / Section 41"
grammar: "0CC-SS0-UU0 (subjects on final triplet; -000 = section general)"
model: eWTW
side: SSOT
member: "-01_PBS"
owner: Q-STRUCTURES
layer: "STD"
doctrine: green-native
status: realized
version: "1.0"
---

# {nid} - Forward Fuselage Section

Section node for the nose zone (Section 41) of the eWTW fuselage. Section general
of G-ATLAS `053-010`; parent chapter `053-000`. SSOT-side; the AMM / SRM (PUB)
consume it one-way via `ssot-ref.yaml`.

## Numbering

Subjects populate the final triplet (×10): `053-010-000` section general (this
node) . `053-010-010`, `053-010-020` ... subjects.

## Index

- [Scope & Boundary](#scope--boundary)
- [Subject Breakdown](#subject-breakdown)
- [Cross-References](#cross-references)
- [Green-Native Notes](#green-native-notes)
- [References](#references)

## Scope & Boundary

**Owns** - the nose-zone primary structure and its distinctive assemblies:
radome attach, flight-deck enclosure and windshield-post structure, forward
pressure bulkhead (physical instance), nose landing-gear bay, forward equipment
(E/E) bay, nose-zone skin/frames/stringers, and the forward-to-center production
join.

**Cedes** - weather-radar antenna -> `034`; windshield glazing -> `056`;
windshield/radome heating -> `030`; landing-gear *system* -> `032`; E/E-bay
*equipment* -> `025`, electrical/avionics -> `024`/`040`, bay cooling -> `021`;
pressure-bulkhead and skin/frame *design basis* -> `053-080` / `053-050` /
`053-060` (element catalogs).

## Subject Breakdown

| Subject | Title | Layer | Owner |
|---|---|:--:|---|
{rows}
> Layer: **STD** carries (energy-neutral) . **\u25c7** green overlay . **STD-G** green delta.
> The nose zone is entirely **STD**: the energy-carrier bay is under-floor in the
> center section (`053-110-000`), not here.

{links}
## Cross-References

| This node references | Owned by | Why |
|---|---|---|
| Weather-radar antenna | `034` Navigation | radome is a radar boundary |
| Windshield glazing | `056` Windows | transparencies are a windows item |
| Windshield / radome heating | `030` Ice-and-Rain-Protection | anti-ice is a protection function |
| Nose landing-gear system | `032` Landing Gear | bay structure here, system there |
| E/E-bay equipment | `025` / `024` / `040` | bay structure here, contents there |
| E/E-bay cooling | `021` Air-Conditioning-ECS | bay ventilation is an ECS function |
| Bulkhead / skin design basis | `053-080` / `053-050` / `053-060` | element catalogs |

## Green-Native Notes

The nose is **energy-neutral primary structure** - every subject is **STD**. This
is green-native doctrine working in the negative: nothing is forced green where
the structure carries no energy function.

The single green touchpoint is an *interface*, not structure: **`053-010-050`
Forward Equipment Bay** - if forward high-voltage power electronics or conversion
are installed there, the HV safe-state (`024-900`), arc/fire (`026-900`) and
thermal (`021`) interfaces apply to the *equipment*; the bay **structure** stays
STD.

## References

[^ata53]: ATA 100 / iSpec 2200 - Chapter 53 *Fuselage*, nose / Section 41 (heritage scope reference).
[^radar]: G-ATLAS `034` Navigation (weather-radar antenna behind the radome).
[^win]: G-ATLAS `056` Windows (windshield transparencies).
[^ice]: G-ATLAS `030` Ice-and-Rain-Protection (windshield / radome heating).
[^gear]: G-ATLAS `032` Landing Gear (nose-gear system in the bay owned here).

<!--
Last.MarkedDown: eWTW PBS 053-010-000 realized - forward fuselage (nose/Sec 41) subjects 053-010-010..070; all STD (energy-neutral zone); only green touchpoint is E/E-bay equipment interface, structure STD
.YieldedAlgorithmicMachineLearning: true
-->
""".format(nid=NODE_ID, rows=rows, links=links)

    write(os.path.join(node, "README.md"), readme)

    print("OK: %s realizzato - %d subject." % (NODE_ID, len(SUBJECTS)))
    print("Path: %s" % os.path.normpath(node))


if __name__ == "__main__":
    main()
> center section (`053-110-000`), not here.

{links}
## Cross-References

| This node references | Owned by | Why |
|---|---|---|
| Weather-radar antenna | `034` Navigation | radome is a radar boundary |
| Windshield glazing | `056` Windows | transparencies are a windows item |
| Windshield / radome heating | `030` Ice-and-Rain-Protection | anti-ice is a protection function |
| Nose landing-gear system | `032` Landing Gear | bay structure here, system there |
| E/E-bay equipment | `025` / `024` / `040` | bay structure here, contents there |
| E/E-bay cooling | `021` Air-Conditioning-ECS | bay ventilation is an ECS function |
| Bulkhead / skin design basis | `053-080` / `053-050` / `053-060` | element catalogs |

## Green-Native Notes

The nose is **energy-neutral primary structure** - every subject is **STD**. This
is green-native doctrine working in the negative: nothing is forced green where
the structure carries no energy function.

The single green touchpoint is an *interface*, not structure: **`053-010-050`
Forward Equipment Bay** - if forward high-voltage power electronics or conversion
are installed there, the HV safe-state (`024-900`), arc/fire (`026-900`) and
thermal (`021`) interfaces apply to the *equipment*; the bay **structure** stays
STD.

## References

[^ata53]: ATA 100 / iSpec 2200 - Chapter 53 *Fuselage*, nose / Section 41 (heritage scope reference).
[^radar]: G-ATLAS `034` Navigation (weather-radar antenna behind the radome).
[^win]: G-ATLAS `056` Windows (windshield transparencies).
[^ice]: G-ATLAS `030` Ice-and-Rain-Protection (windshield / radome heating).
[^gear]: G-ATLAS `032` Landing Gear (nose-gear system in the bay owned here).

<!--
Last.MarkedDown: eWTW PBS 053-010-000 realized - forward fuselage (nose/Sec 41) subjects 053-010-010..070; all STD (energy-neutral zone); only green touchpoint is E/E-bay equipment interface, structure STD
.YieldedAlgorithmicMachineLearning: true
-->
""".format(nid=NODE_ID, rows=rows, links=links)

    write(os.path.join(node, "README.md"), readme)

    print("OK: %s realizzato - %d subject." % (NODE_ID, len(SUBJECTS)))
    print("Path: %s" % os.path.normpath(node))


if __name__ == "__main__":
    main()