#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
populate_053_subjects.py
Popola le 10 sezioni SSOT di 053 (Fuselage) con i subject ridistribuiti prendendo
ispirazione dall'Embraer 170/175/190/195 & Lineage 1000 ATA Breakdown (cap. 53).

Ogni subject e' una directory 053-SS0-UU0_Title con subject.yaml (che registra
l'origine Embraer = crosswalk). Aggiorna il README di ogni sezione e del capitolo,
ed emette 053-Embraer-Crosswalk.yaml + 053-Section-Subject-Distribution.md.

USO
    python3 populate_053_subjects.py                 # dalla root del repo Q-plus-A
    python3 populate_053_subjects.py /percorso/repo
"""
import os
import sys

OVERWRITE = True

CHAP_REL = (
    "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
    "000-099_G-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces/053_Fuselage"
)
OWNER = "Q-STRUCTURES"
GLYPH = {"STD": "STD", "DIAMOND": "\u25c7", "STD-G": "STD-G", "VACATED": "\u2205"}

# section code -> (section folder title, [ (uu, title, layer, embraer, crossref/note) ])
SECTIONS = {
    "053-000": ("General", [
        ("010", "Fuselage-General", "STD", ["53-00-00"], ""),
        ("020", "Fuselage-Protective-Films-and-Tapes", "STD", ["53-00-20", "53-00-40"],
         "green: recyclable/bio protective films -> 051-900"),
        ("030", "Fuselage-External-Access-Doors-and-Panels-General", "STD", ["53-03-00"],
         "zone panels distributed to 100/200/300/400"),
        ("040", "Fuselage-Drains", "STD", ["53-05-00", "53-05-65", "53-05-67", "53-05-69", "53-05-71", "53-05-73"], ""),
    ]),
    "053-100": ("Nose-and-Forward-Fuselage-Structure", [
        ("010", "Forward-Fuselage-Zone-General", "STD", ["53-10-00"], ""),
        ("020", "Nose-Landing-Gear-Bay-and-Door-Supports", "STD", ["53-10-18", "53-10-31", "53-02-00"], "system -> 032"),
        ("030", "Forward-Avionics-Compartment-Structure", "STD", ["53-10-75", "53-10-27", "53-10-29", "53-10-30", "53-10-81"], "equipment -> 025/024/040"),
        ("040", "Radome-and-Diverters-Attach-Structure", "STD", ["53-14-00", "53-14-21"], "antenna -> 034"),
        ("050", "Forward-Fuselage-Direct-Vision-Window", "STD", ["53-10-77"], "glazing -> 056"),
        ("060", "Forward-Fuselage-External-Access-Panels", "STD", ["53-03-55"], ""),
    ]),
    "053-200": ("Center-Fuselage-Structure", [
        ("010", "Center-Fuselage-Zone-General", "STD", ["53-20-00", "53-21-00", "53-22-00", "53-23-00"], ""),
        ("020", "Wing-to-Fuselage-Fairing", "STD", ["53-04-00", "53-04-02", "53-04-20", "53-04-30", "53-04-40", "53-04-50", "53-04-51", "53-04-52", "53-04-60"], ""),
        ("030", "Main-Landing-Gear-Wheelwell-and-Sealing", "STD", ["53-04-34", "53-04-35"], "system -> 032"),
        ("040", "Antenna-Provisions-and-Reinforcements", "STD", ["53-22-16", "53-22-17", "53-22-18", "53-22-20", "53-22-22", "53-22-25", "53-22-28"], "antennas -> 023"),
        ("050", "Middle-Avionics-Compartment-Structure", "STD", ["53-22-27"], "equipment -> 025/024/040"),
        ("060", "Center-Fuselage-External-Access-and-Service-Doors", "STD", ["53-03-56", "53-03-57", "53-03-59", "53-03-60", "53-03-61", "53-03-62"], "oxygen -> 035, water/waste -> 038"),
    ]),
    "053-300": ("Aft-Fuselage-Structure", [
        ("010", "Rear-Fuselage-Zone-General", "STD", ["53-30-00"], ""),
        ("020", "Rear-Fuselage-Adjustable-Rods", "STD", ["53-30-21"], ""),
        ("030", "Tail-Bumper", "STD", ["53-30-81"], ""),
        ("040", "Rear-Fuselage-External-Access-Panels", "STD", ["53-03-63"], ""),
    ]),
    "053-400": ("Tailcone-and-Auxiliary-Power-Module-Structure", [
        ("010", "Tailcone-Zone-General", "STD", ["53-31-00"], ""),
        ("020", "Auxiliary-Power-Module-Mounts-and-Support-Struts", "DIAMOND", ["53-31-27", "53-31-29", "53-31-31", "53-31-33", "53-31-35"], "green: electric aux-power mount (APU->aux-power module); propulsion 070"),
        ("030", "Auxiliary-Power-Module-Firewall-and-Thermal-Provisions", "DIAMOND", ["53-31-21", "53-31-23", "53-31-10"], "green: electric aux-power thermal/fire (-> 026-900); oil-cooler duct may vacate"),
        ("040", "Rudder-Root-Aft-Fairing", "STD", ["53-31-25"], "control surface -> 055"),
        ("050", "Tailcone-External-Access-Panels", "STD", ["53-03-64"], ""),
    ]),
    "053-500": ("Fuselage-Skin-Panels-and-Doublers", [
        ("010", "Forward-Fuselage-Skin", "STD", ["53-10-01"], ""),
        ("020", "Center-Fuselage-I-Skin", "STD", ["53-21-01"], ""),
        ("030", "Center-Fuselage-II-Skin", "STD", ["53-22-01"], ""),
        ("040", "Center-Fuselage-III-Skin", "STD", ["53-23-01"], ""),
        ("050", "Rear-Fuselage-Skin", "STD", ["53-30-01"], ""),
        ("060", "Tailcone-Skin", "STD", ["53-31-01"], ""),
    ]),
    "053-600": ("Frames-Stringers-and-Longerons", [
        ("010", "Forward-Fuselage-Frames-Stringers-and-Structures", "STD", ["53-10-02", "53-10-03", "53-10-04"], ""),
        ("020", "Center-Fuselage-I-Frames-Stringers-and-Structures", "STD", ["53-21-02", "53-21-03", "53-21-04"], ""),
        ("030", "Center-Fuselage-II-Frames-Stringers-and-Structures", "STD", ["53-22-02", "53-22-03", "53-22-04"], ""),
        ("040", "Center-Fuselage-III-Frames-Stringers-and-Structures", "STD", ["53-23-02", "53-23-03", "53-23-04"], ""),
        ("050", "Rear-Fuselage-Frames-Stringers-and-Structures", "STD", ["53-30-02", "53-30-03", "53-30-04"], ""),
        ("060", "Tailcone-Frames-Stringers-and-Structures", "STD", ["53-31-02", "53-31-03", "53-31-04"], ""),
        ("070", "Window-Formers-and-Surrounding-Structure", "STD", ["53-10-09", "53-10-12", "53-21-09", "53-21-12", "53-22-09", "53-22-12", "53-23-09", "53-23-12"], "cross-ref 056"),
        ("080", "Door-Surrounding-Structure", "STD", ["53-10-11", "53-21-11", "53-23-11", "53-30-11"], "cross-ref 052"),
    ]),
    "053-700": ("Floor-and-Pressure-Deck-Structure", [
        ("010", "Fuselage-Floor-Structure-General", "STD", ["53-00-10"], ""),
        ("020", "Forward-Fuselage-Floor-Structure", "STD", ["53-10-10"], ""),
        ("030", "Center-Fuselage-Floor-Structure", "STD", ["53-21-10", "53-22-10", "53-23-10"], ""),
        ("040", "Rear-Fuselage-Floor-Structure", "STD", ["53-30-10"], ""),
        ("050", "Floor-Panels", "STD", ["53-01-00", "53-01-35", "53-01-37", "53-01-39", "53-01-41", "53-01-43", "53-01-44", "53-01-45", "53-01-46"], ""),
        ("060", "Seat-Tracks", "STD", ["53-06-00", "53-06-01"], "seats -> 025"),
    ]),
    "053-800": ("Pressure-Bulkheads-and-Major-Attach-Fittings", [
        ("010", "Forward-Pressure-Bulkhead", "STD", ["53-10-06"], ""),
        ("020", "Rear-Pressure-Bulkhead", "STD", ["53-30-06"], ""),
        ("030", "Forward-Fuselage-Landing-Gear-Fittings", "STD", ["53-10-08"], "system -> 032"),
        ("040", "Passenger-and-Service-Door-Frame-Fittings-and-Plates", "STD", ["53-10-21", "53-10-22", "53-10-25", "53-10-26", "53-23-21", "53-23-22", "53-23-25", "53-23-26"], "cross-ref 052"),
        ("050", "Cargo-and-Baggage-Door-Frame-Fittings-and-Plates", "STD", ["53-21-29", "53-21-30", "53-23-29", "53-23-30", "53-23-31", "53-23-32"], "cross-ref 052"),
        ("060", "Fuselage-Plug-Frame-Fittings", "STD", ["53-10-35", "53-23-35"], ""),
        ("070", "Rear-Fuselage-to-Stabilizer-Attach-Fittings", "STD", ["53-30-83", "53-30-84", "53-30-85"], "cross-ref 055"),
        ("080", "Door-Sills", "STD", ["53-10-79", "53-23-79"], "cross-ref 052"),
    ]),
    "053-900": ("Energy-Carrier-Structural-Integration", [
        ("010", "Energy-Carrier-Bay-Structure", "STD-G", [], "green-native, no Embraer analogue; houses 028"),
        ("020", "Energy-Carrier-Crash-Protection-and-Containment-Interface", "STD-G", [], "-> 026-900 fire/thermal containment"),
        ("030", "Energy-Carrier-Mount-and-Attach-Fittings", "STD-G", [], "carrier -> 028"),
        ("040", "Electric-Energy-Maintenance-Compartment-Structure", "STD-G", ["53-01-47"], "Embraer ELECTRIC/FUEL maint compartment -> green (fuel->energy)"),
        ("050", "Vacated-Auxiliary-Fuel-Tank-Compartment-Footprint", "VACATED", ["53-23-39"], "Embraer aux-fuel-tank compartment door -> VACATED for eWTW; migration footprint"),
    ]),
}


def write(path, text):
    if (not OVERWRITE) and os.path.exists(path):
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    chap = os.path.join(base, CHAP_REL)
    os.makedirs(chap, exist_ok=True)

    n_sub = 0
    cross_rows = []      # (embraer, gatlas, title)
    dist_blocks = []     # markdown per section

    for scode, (stitle, subjects) in SECTIONS.items():
        sdir = os.path.join(chap, "%s_%s" % (scode, stitle))
        os.makedirs(sdir, exist_ok=True)

        rows = ""
        links = ""
        for uu, title, lay, emb, note in subjects:
            sid = "%s-%s" % (scode, uu)
            idir = os.path.join(sdir, "%s_%s" % (sid, title))
            os.makedirs(idir, exist_ok=True)
            emb_yaml = "".join("\n    - \"%s\"" % e for e in emb) or " []"
            emb_field = ("  embraer_origin:%s\n" % emb_yaml) if emb else "  embraer_origin: []\n"
            write(os.path.join(idir, "subject.yaml"),
                  "subject:\n  id: %s\n  title: %s\n  level: subject\n"
                  "  layer: \"%s\"\n  chapter: \"053\"\n  section: \"%s\"\n"
                  "  owner: %s\n  model: SSOT-agnostic\n  side: SSOT\n"
                  "%s"
                  "  crossref_note: \"%s\"\n  status: scaffold\n  version: \"1.0\"\n"
                  % (sid, title.replace("-", " "), GLYPH[lay], scode, OWNER,
                     emb_field, note))
            write(os.path.join(idir, ".gitkeep"), "")
            n_sub += 1
            embs = ", ".join(emb) if emb else "(green-native)"
            rows += "| `%s` | %s | %s | %s |\n" % (sid, title.replace("-", " "), GLYPH[lay], embs)
            links += "- [`%s`](./%s_%s/) - %s | %s\n" % (sid, sid, title, title.replace("-", " "), GLYPH[lay])
            for e in (emb or ["(none)"]):
                cross_rows.append((e, sid, title.replace("-", " ")))

        # section README
        write(os.path.join(sdir, "README.md"),
              "---\nsection: \"%s\"\ntitle: %s\nchapter: \"053\"\nband: 000-099_G-ATLAS\n"
              "side: SSOT\nowner: %s\ndoctrine: green-native\nsource_inspiration: "
              "\"Embraer 170/175/190/195 & Lineage 1000 ATA Breakdown, ch.53\"\n"
              "status: scaffold\nversion: \"1.0\"\n---\n\n# %s - %s\n\n"
              "Subjects (redistributed from Embraer ch.53; `-000` = section general, "
              "deeper units on the final triplet):\n\n"
              "| Subject | Title | Layer | Embraer origin |\n|---|---|:--:|---|\n%s\n%s\n"
              "> Layer: **STD** carries . **\u25c7** green overlay . **STD-G** green delta "
              ". **\u2205** vacated.\n"
              % (scode, stitle.replace("-", " "), OWNER, scode, stitle.replace("-", " "),
                 rows, links))

        dist_blocks.append("### `%s` %s\n\n| Subject | Title | Layer | Embraer origin |\n|---|---|:--:|---|\n%s"
                           % (scode, stitle.replace("-", " "), rows))

    # chapter README (refresh with section index + counts)
    sec_rows = ""
    for scode, (stitle, subjects) in SECTIONS.items():
        lay_set = sorted({GLYPH[s[2]] for s in subjects})
        sec_rows += "| [`%s`](./%s_%s/) | %s | %d | %s |\n" % (
            scode, scode, stitle, stitle.replace("-", " "), len(subjects), " ".join(lay_set))
    write(os.path.join(chap, "README.md"),
          "---\nchapter: \"053\"\ntitle: Fuselage\nata: \"53\"\nband: 000-099_G-ATLAS\n"
          "master_range: 050-059\nside: SSOT\nowner: %s\ngreen_overlay: Q-GREENTECH\n"
          "doctrine: green-native\nsource_inspiration: \"Embraer 170/175/190/195 & "
          "Lineage 1000 ATA Breakdown, ch.53\"\nsubjects_total: %d\nstatus: scaffold\n"
          "version: \"2.0\"\n---\n\n# 053 - Fuselage\n\n**ATA 53.** Sections populated "
          "with %d subjects redistributed from the Embraer ch.53 breakdown. Element "
          "sections (`500/600/700/800`) collect the repeating elements across zones; "
          "zone sections (`100/200/300/400`) collect zone-unique features; `900` is the "
          "green delta.\n\n## Sections\n\n| Section | Title | Subjects | Layers |\n"
          "|---|---|:--:|---|\n%s\n"
          "> See `053-Embraer-Crosswalk.yaml` and `053-Section-Subject-Distribution.md` "
          "for the full Embraer -> G-ATLAS mapping.\n"
          % (OWNER, n_sub, n_sub, sec_rows))

    # crosswalk yaml
    cw = ("embraer_to_gatlas_crosswalk:\n  chapter: \"53\"\n"
          "  source: \"Embraer 170/175/190/195 & Lineage 1000 ATA Breakdown\"\n"
          "  target_band: 000-099_G-ATLAS\n  mappings:\n")
    for emb, sid, title in cross_rows:
        if emb == "(none)":
            continue
        cw += "    - {embraer: \"%s\", gatlas: %s, title: \"%s\"}\n" % (emb, sid, title)
    write(os.path.join(chap, "053-Embraer-Crosswalk.yaml"), cw)

    # distribution markdown
    dist = ("# 053 Fuselage - Section/Subject Distribution (Embraer-inspired)\n\n"
            "Redistribution of the Embraer 170/175/190/195 & Lineage 1000 ATA ch.53 "
            "breakdown into the G-ATLAS `053` sections. Element sections gather repeating "
            "elements by zone; zone sections gather zone-unique features; `053-900` is the "
            "green delta.\n\n" + "\n\n".join(dist_blocks) +
            "\n\n> Layer: **STD** carries . **\u25c7** green overlay . **STD-G** green delta "
            ". **\u2205** vacated. Green concentrates at `053-400` (aux-power module) and "
            "`053-900` (energy carrier); Embraer `53-01-47` (electric/fuel maint) and "
            "`53-23-39` (aux-fuel-tank door) are the fuel->energy transition points.\n")
    write(os.path.join(chap, "053-Section-Subject-Distribution.md"), dist)

    print("OK: 053 popolato - %d subject su %d sezioni; crosswalk + distribution emessi."
          % (n_sub, len(SECTIONS)))
    print("Chapter: %s" % os.path.normpath(chap))


if __name__ == "__main__":
    main()