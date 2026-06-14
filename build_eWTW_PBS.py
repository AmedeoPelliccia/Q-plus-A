#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_eWTW_PBS.py
Costruisce la PBS eWTW riformata (allineata G-ATLAS / ATA ×10) sotto
…/01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/.

Sostituisce lo schema decimale ad-hoc (00/10/.../90) con la numerazione 0CC / 0CC-SS0,
cosi' che PBS id == G-ATLAS subject id (PBS <-> SSOT <-> AMM 1:1).

USO
    python3 build_eWTW_PBS.py                 # dalla root del repo Q-plus-A
    python3 build_eWTW_PBS.py /percorso/repo  # base dir esplicita

Crea: directory product-root + group + chapter, ognuna con README.md + pbs-node.yaml.
OVERWRITE = False per saltare i file gia' presenti (preserva edit manuali).
"""
import os
import sys

OVERWRITE = True

ROOT_REL = (
    "01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/"
    "01-02-01-01_MODELS/01-02-01-01-01_eWTW/"
    "01-02-01-01-01-01_SBS_System-Breakdown-Structure/"
    "01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure"
)
PRODUCT_ROOT = ("000", "Aircraft-Product")

# group band-root -> (group title, [(chapter/section code, title)])
PBS = {
    "010": ("Ground-and-Servicing-Interfaces", [
        ("010-000", "Parking-Mooring-and-Return-to-Service"),
        ("011-000", "Placards-and-Markings"),
        ("012-000", "Servicing-Points")]),
    "020": ("Core-Systems", [
        ("021-000", "Air-Conditioning-and-Environmental-Control"),
        ("022-000", "Auto-Flight"),
        ("023-000", "Communications"),
        ("024-000", "Electrical-Power-Distribution"),
        ("025-000", "Equipment-and-Furnishings"),
        ("026-000", "Fire-Protection"),
        ("027-000", "Flight-Controls"),
        ("028-000", "Energy-Carrier-Storage"),
        ("029-000", "Actuation-and-Utility-Power")]),
    "030": ("Protection-and-Mechanical-Systems", [
        ("030-000", "Ice-and-Rain-Protection"),
        ("031-000", "Indicating-and-Recording"),
        ("032-000", "Landing-Gear"),
        ("033-000", "Lights"),
        ("034-000", "Navigation"),
        ("035-000", "Oxygen"),
        ("036-000", "Pneumatic-Vacated"),
        ("038-000", "Water-and-Waste")]),
    "040": ("Avionics-Information-and-Auxiliary-Power", [
        ("042-000", "Integrated-Modular-Avionics"),
        ("045-000", "Onboard-Maintenance-System"),
        ("046-000", "Information-Systems"),
        ("049-000", "Auxiliary-Power-Module")]),
    "050": ("Airframe-Structure", [
        ("051-000", "Standard-Practices-Structures"),
        ("052-000", "Doors"),
        ("053-000", "Fuselage-Wide-Tube"),
        ("054-000", "Nacelles-and-Pylons"),
        ("055-000", "Stabilizers-Empennage"),
        ("056-000", "Windows"),
        ("057-000", "Wing")]),
    "070": ("Electric-Propulsion", [
        ("071-000", "Propulsion-Module-Installation"),
        ("073-000", "Energy-Delivery-to-Propulsion"),
        ("074-000", "Propulsion-Power-Electronics"),
        ("076-000", "Propulsion-Control"),
        ("077-000", "Propulsion-Indicating"),
        ("078-000", "Thrust-Producer-Fan-and-Duct")]),
    "080": ("Alternative-and-Quantum-Propulsion", [
        ("080-000", "Reserved-Future")]),
    "090": ("Software-and-Digital-Configuration-Items", [
        ("090-100", "Computer-Software-Configuration-Items"),
        ("090-300", "Digital-Twin-Configuration"),
        ("090-500", "Digital-Product-Passport")]),
}


def write(path, text):
    if (not OVERWRITE) and os.path.exists(path):
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def node_yaml(nid, title, ntype, parent, gatlas):
    return ("pbs_node:\n  id: %s\n  title: %s\n  type: %s\n"
            "  g_atlas: \"%s\"\n  parent: %s\n  model: eWTW\n  side: SSOT\n"
            "  member: \"-01_PBS\"\n  status: scaffold\n  version: \"2.0\"\n"
            % (nid, title.replace("-", " "), ntype, gatlas, parent))


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    pbs_root = os.path.join(base, ROOT_REL)

    # product root
    rcode, rtitle = PRODUCT_ROOT
    root_id = "eWTW-PBS-%s" % rcode
    root_dir = os.path.join(pbs_root, "%s_%s" % (root_id, rtitle))
    os.makedirs(root_dir, exist_ok=True)

    group_rows = ""
    n_grp = n_chap = 0

    for band, (gtitle, chapters) in PBS.items():
        grp_id = "eWTW-PBS-%s" % band
        grp_dir = os.path.join(root_dir, "%s_%s" % (grp_id, gtitle))
        os.makedirs(grp_dir, exist_ok=True)
        n_grp += 1
        group_rows += "| `%s` | %s | %d |\n" % (grp_id, gtitle.replace("-", " "), len(chapters))

        chap_lines = ""
        for code, ctitle in chapters:
            chap_id = "eWTW-PBS-%s" % code
            chap_dir = os.path.join(grp_dir, "%s_%s" % (chap_id, ctitle))
            os.makedirs(chap_dir, exist_ok=True)
            n_chap += 1
            gatlas = code.split("-")[0]
            write(os.path.join(chap_dir, "pbs-node.yaml"),
                  node_yaml(chap_id, ctitle, "chapter", grp_id, gatlas))
            write(os.path.join(chap_dir, "README.md"),
                  "# %s — %s\n\nPBS chapter node (mirrors G-ATLAS `%s`). "
                  "Backed one-way by SSOT; consumed by PUB via `ssot-ref.yaml`.\n"
                  % (chap_id, ctitle.replace("-", " "), gatlas))
            write(os.path.join(chap_dir, ".gitkeep"), "")
            chap_lines += "- [`%s`](%s_%s) — %s\n" % (
                chap_id, chap_id, ctitle, ctitle.replace("-", " "))

        write(os.path.join(grp_dir, "pbs-node.yaml"),
              node_yaml(grp_id, gtitle, "group", root_id, band))
        write(os.path.join(grp_dir, "README.md"),
              "# %s — %s\n\nProduct group = G-ATLAS band `%s`. Chapters:\n\n%s"
              % (grp_id, gtitle.replace("-", " "), band, chap_lines))
        write(os.path.join(grp_dir, ".gitkeep"), "")

    # product-root README + node
    write(os.path.join(root_dir, "pbs-node.yaml"),
          node_yaml(root_id, rtitle, "product-root", "eWTW", "000"))
    write(os.path.join(root_dir, "README.md"),
          "---\npbs: eWTW\nscheme: G-ATLAS ×10 (v2.0)\nstatus: baseline\n---\n\n"
          "# %s — %s\n\nPBS riformata, allineata G-ATLAS/ATA ×10: "
          "`eWTW-PBS-<band>` group, `eWTW-PBS-<0CC>-<SS0>` chapter. "
          "PBS id == G-ATLAS subject id.\n\n## Groups\n\n"
          "| Group | Title | Chapters |\n|---|---|:--:|\n%s\n"
          % (root_id, rtitle.replace("-", " "), group_rows))

    print("OK: 1 product-root, %d group, %d chapter." % (n_grp, n_chap))
    print("Root: %s" % os.path.normpath(root_dir))


if __name__ == "__main__":
    main()
