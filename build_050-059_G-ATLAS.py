#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_050-059_G-ATLAS.py
Scaffold del master range SSOT  050-059_Primary-Structures-and-Programme-Interfaces
(lato 01-03_TECHNOLOGIES / Q+ATLANTIDE / 000-099_G-ATLAS), green-native,
con focus su 053 (Fuselage) espanso nelle sue sezioni ATA ×10 (053-000..053-900),
esattamente come 021 nel range 020-029.

USO
    python3 build_050-059_G-ATLAS.py                 # dalla root del repo Q-plus-A
    python3 build_050-059_G-ATLAS.py /percorso/repo
"""
import os
import sys

OVERWRITE = True

ROOT_REL = (
    "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
    "000-099_G-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces"
)
OWNER = "Q-STRUCTURES"

# code -> (title, ata, green_summary)
CHAPTERS = [
    ("050", "Cargo-and-Accessory-Compartments", "ATA 50",
     "STD compartment structure. Green delta 050-900: energy-carrier-adjacent compartment provisions; cargo-fire <-> battery thermal-runaway interface (-> 026-900)."),
    ("051", "Standard-Practices-Structures", "ATA 51",
     "STD. Green delta 051-900: recyclable / bio-composite material practices, green repair allowables, design-for-disassembly and end-of-life recovery."),
    ("052", "Doors", "ATA 52",
     "STD. Green delta 052-900: energy-carrier bay access panels and service doors."),
    ("053", "Fuselage", "ATA 53",
     "STD primary structure + green delta 053-900 energy-carrier structural integration (under-floor bay, crash protection, attach fittings). EXPANDED into sections."),
    ("054", "Nacelles-and-Pylons", "ATA 54",
     "Green-significant: electric-propulsion module mounting replaces the turbine nacelle - no hot exhaust, different vibration/thermal, power-electronics support. Green delta 054-900 electric-propulsion structural mounting."),
    ("055", "Stabilizers", "ATA 55",
     "STD. Thin green delta 055-900."),
    ("056", "Windows", "ATA 56",
     "STD. Thin green delta 056-900."),
    ("057", "Wings", "ATA 57",
     "Green-significant: eWTW vacates the wet-wing fuel-tank function (carrier is fuselage-housed). Green delta 057-900: vacated wet-wing provisions (eWTW) / wing energy-carrier bay (wing-battery variants)."),
    ("058", "Advanced-and-Green-Structural-Systems", "G-ATLAS",
     "Green-native chapter: structural health monitoring, recyclable/bio composites, adaptive/morphing structures. STD-G dominant."),
    ("059", "Programme-Structural-Interfaces", "G-ATLAS",
     "Structural mounting/integration interfaces to programmes; STD with green where energy-carrier / propulsion structural interfaces occur."),
]

# 053 sections: (SS0, title, layer, note)
SECTIONS_053 = [
    ("000", "General", "STD",
     "Fuselage chapter general: configuration, zoning, fuselage-station references and green-native summary."),
    ("100", "Nose-and-Forward-Fuselage-Structure", "STD",
     "Nose / forward barrel: flight-deck structure, forward pressure boundary, radome attach, nose-gear bay. Energy-neutral."),
    ("200", "Center-Fuselage-Structure", "DIAMOND",
     "Center barrel: wing-to-body join and carry-through. Overlay for under-floor energy-carrier bay integration and its crash cases."),
    ("300", "Aft-Fuselage-Structure", "STD",
     "Aft barrel: aft pressure boundary and empennage attach interface."),
    ("400", "Tailcone-and-Auxiliary-Power-Module-Structure", "STD",
     "Tailcone and auxiliary-power-module mounting structure (engine/APU -> aux-power module, NORM-TERM-001)."),
    ("500", "Fuselage-Skin-Panels-and-Doublers", "STD",
     "Skin, lap/butt joints and doublers."),
    ("600", "Frames-Stringers-and-Longerons", "STD",
     "Circumferential frames, longitudinal stringers and longerons."),
    ("700", "Floor-and-Pressure-Deck-Structure", "DIAMOND",
     "Passenger and cargo floor grid. Overlay carrying energy-carrier bay loads and crash cases."),
    ("800", "Pressure-Bulkheads-and-Major-Attach-Fittings", "DIAMOND",
     "Forward/aft pressure bulkheads, keel beam, wing/gear/empennage/pylon fittings. Overlay for energy-carrier mount fittings."),
    ("900", "Energy-Carrier-Structural-Integration", "STD-G",
     "Green delta: dedicated under-floor energy-carrier bay structure, crash protection, thermal/fire containment interface (-> 026-900); carrier owned by 028. No conventional analogue."),
]

GLYPH = {"STD": "STD", "DIAMOND": "\u25c7", "STD-G": "STD-G"}


def write(path, text):
    if (not OVERWRITE) and os.path.exists(path):
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    root = os.path.join(base, ROOT_REL)
    os.makedirs(root, exist_ok=True)

    # ---- chapters ----
    chap_rows = ""
    for code, title, ata, green in CHAPTERS:
        cdir = os.path.join(root, "%s_%s" % (code, title))
        os.makedirs(cdir, exist_ok=True)
        chap_rows += "| [`%s`](./%s_%s/) | %s | %s |\n" % (
            code, code, title, title.replace("-", " "), ata)
        if code != "053":
            write(os.path.join(cdir, "README.md"),
                  "---\nchapter: \"%s\"\ntitle: %s\nata: \"%s\"\nband: 000-099_G-ATLAS\n"
                  "master_range: 050-059\nside: SSOT\nowner: %s\ngreen_overlay: Q-GREENTECH\n"
                  "doctrine: green-native\nstatus: scaffold\nversion: \"1.0\"\n---\n\n"
                  "# %s - %s\n\n**%s** | Green-native treatment:\n\n%s\n\n"
                  "> Green deltas live in the `%s-900` lane. Terminology per "
                  "G-ATLAS-NORM-TERM-001 (fuel -> energy carrier; engine/APU -> "
                  "propulsion / auxiliary-power module).\n"
                  % (code, title.replace("-", " "), ata, OWNER,
                     code, title.replace("-", " "), ata, green, code))
            write(os.path.join(cdir, ".gitkeep"), "")

    # ---- 053 expanded ----
    c053 = os.path.join(root, "053_Fuselage")
    sec_rows = ""
    sec_links = ""
    for ss0, title, lay, note in SECTIONS_053:
        sid = "053-%s" % ss0
        sdir = os.path.join(c053, "%s_%s" % (sid, title))
        os.makedirs(sdir, exist_ok=True)
        sec_rows += "| `%s` | %s | %s |\n" % (sid, title.replace("-", " "), GLYPH[lay])
        sec_links += "- [`%s`](./%s_%s/) - %s | %s\n" % (
            sid, sid, title, title.replace("-", " "), GLYPH[lay])
        write(os.path.join(sdir, "README.md"),
              "---\nsection: \"%s\"\ntitle: %s\nchapter: \"053\"\nlayer: \"%s\"\n"
              "band: 000-099_G-ATLAS\nside: SSOT\nowner: %s\ndoctrine: green-native\n"
              "status: scaffold\nversion: \"1.0\"\n---\n\n# %s - %s\n\n%s\n\n"
              "> Layer **%s**. Subjects populate the final triplet (`%s-UU0`).\n"
              % (sid, title.replace("-", " "), GLYPH[lay], OWNER,
                 sid, title.replace("-", " "), note, GLYPH[lay], sid))
        write(os.path.join(sdir, ".gitkeep"), "")

    write(os.path.join(c053, "README.md"),
          "---\nchapter: \"053\"\ntitle: Fuselage\nata: \"53\"\nband: 000-099_G-ATLAS\n"
          "master_range: 050-059\nside: SSOT\nowner: %s\ngreen_overlay: Q-GREENTECH\n"
          "doctrine: green-native\nstatus: scaffold\nversion: \"1.0\"\n---\n\n"
          "# 053 - Fuselage\n\n**ATA 53.** STD primary structure; green concentrates "
          "in the `053-900` lane (energy-carrier structural integration) with ◇ "
          "overlays where the center barrel, floor and bulkheads/fittings take "
          "energy-carrier mass and crash cases.\n\n## Sections\n\n"
          "| Section | Title | Layer |\n|---|---|:--:|\n%s\n%s\n"
          "> STD carries · ◇ green overlay · STD-G green delta. The dedicated "
          "under-floor bay `053-900` has no conventional analogue; it houses `028` "
          "and interfaces `026-900`.\n"
          % (OWNER, sec_rows, sec_links))

    # ---- master range README ----
    write(os.path.join(root, "README.md"),
          "---\nmaster_range: \"050-059_Primary-Structures-and-Programme-Interfaces\"\n"
          "ata_span: \"ATA 50-59\"\nband: 000-099_G-ATLAS\nside: SSOT\nowner: %s\n"
          "green_overlay: Q-GREENTECH\ndoctrine: green-native\nstatus: scaffold\n"
          "version: \"1.0\"\n---\n\n"
          "# 050-059 - Primary Structures and Programme Interfaces\n\n"
          "Structures master range (ATA 50-59), green-native. Primary structure is "
          "**STD-dominant** (it carries loads, not energy); green **concentrates** at "
          "`053-900` (carrier bay), `054-900` (electric-propulsion mount), `057-900` "
          "(vacated wet-wing) and the native chapter `058`.\n\n## Chapters\n\n"
          "| Chapter | Title | ATA |\n|---|---|---|\n%s\n"
          "> Focus chapter `053` is expanded into sections `053-000..053-900`. "
          "See `050-059_G-ATLAS-Green-Native-Breakdown.md` for the full normalization.\n"
          % (OWNER, chap_rows))

    print("OK: master range 050-059 scaffolded - %d chapters; 053 expanded into %d sections."
          % (len(CHAPTERS), len(SECTIONS_053)))
    print("Root: %s" % os.path.normpath(root))


if __name__ == "__main__":
    main()