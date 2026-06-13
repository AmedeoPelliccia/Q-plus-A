#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_021_subjects.py
Genera i subject node di G-ATLAS 021 (Air Conditioning & Environmental Control)
per il modello eWTW dentro PMC-EWTW-AMM, secondo la convenzione
AMPEL360-AMM-INFOCODE-CM-001 (subject = directory che contiene il breakdown info-code).

USO
    # dalla root del repo Q-plus-A:
    python3 build_021_subjects.py
    # oppure indicando una base dir:
    python3 build_021_subjects.py /percorso/al/repo

Crea: directory di sezione + subject, un README.md per sezione + capitolo,
e un subject-infocode-breakdown.yaml (stub) per ogni subject.
Imposta OVERWRITE = False per NON sovrascrivere file gia' presenti (preserva edit manuali).
"""
import os
import sys

OVERWRITE = False  # False = salta i file gia' esistenti (preserva modifiche manuali)

ROOT_REL = (
    "01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/"
    "01-02-01-01_MODELS/01-02-01-01-01_eWTW/"
    "01-02-01-01-01-01_SBS_System-Breakdown-Structure/"
    "01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure/"
    "PMC-EWTW-AMM_Aircraft-Maintenance-Manual/G-ATLAS_000-099/"
    "020-029_Core-Aircraft-Systems/021_Air-Conditioning-Environmental-Control"
)
CONVENTION = "AMPEL360-AMM-INFOCODE-CM-001"
DEV = "021-510-010"  # subject con CM package completo (artefatto separato)

# sezione id -> (titolo, layer)
SECTIONS = {
    "021-000": ("General", "STD"),
    "021-200": ("Distribution", "STD"),
    "021-210": ("Cockpit-Distribution", "STD"),
    "021-220": ("Passenger-Cabin-Distribution", "STD"),
    "021-230": ("Gasper", "STD"),
    "021-240": ("Recirculation", "STD"),
    "021-250": ("Ram-Air-Ventilation", "STD"),
    "021-260": ("Avionics-Compartment-Ventilation", "STD"),
    "021-270": ("Cargo-Compartment-Ventilation", "STD"),
    "021-280": ("Miscellaneous-Equipment-and-Chiller-Ventilation", "STD"),
    "021-290": ("Low-Pressure-Ground-Supply", "STD"),
    "021-300": ("Pressurization-Control", "STD"),
    "021-310": ("Pressurization-Control-and-Indication", "STD"),
    "021-320": ("Cabin-Pressure-Relief", "STD"),
    "021-330": ("Cargo-Compartment-Pressure-Equalization", "STD"),
    "021-400": ("Heating", "STD"),
    "021-410": ("Floor-Panel-Heating", "STD"),
    "021-500": ("Environmental-Cooling-Electric-Integrated", "ELEC"),
    "021-510": ("Environmental-Cooling-Unit-Electric", "ELEC"),
    "021-600": ("Temperature-Control", "ELEC"),
    "021-610": ("Cockpit-Zone-Temperature-Control", "ELEC"),
    "021-620": ("Passenger-Cabin-Zone-Temperature-Control", "ELEC"),
    "021-900": ("Energy-System-Thermal-Integration", "STD-G"),
}

# sezione -> [(suffisso, titolo, layer)]
SUBJECTS = {
    "021-000": [("010", "ECS-General-and-Zoning", "STD")],
    "021-200": [("010", "Distribution-Ducting-Architecture", "STD"),
                ("030", "Distribution-Control-and-Balancing", "STD")],
    "021-210": [("010", "Flight-Deck-Supply-Ducting", "STD"),
                ("030", "Flight-Deck-Outlets-and-Diffusers", "STD")],
    "021-220": [("010", "Cabin-Supply-Riser-Ducts", "STD"),
                ("030", "Cabin-Outlets-and-Diffusers", "STD"),
                ("050", "Overhead-Distribution-Manifold", "STD")],
    "021-230": [("010", "Gasper-Fan", "STD"),
                ("030", "Gasper-Outlets-and-Ducting", "STD")],
    "021-240": [("010", "Recirculation-Fan", "STD"),
                ("030", "Recirculation-Filter-HEPA", "STD"),
                ("050", "Recirculation-Ducting-and-Check-Valves", "STD")],
    "021-250": [("010", "Ram-Air-Inlet-and-Scoop", "STD"),
                ("030", "Ram-Air-Valve-and-Actuator", "STD"),
                ("050", "Ram-Air-Ducting", "STD")],
    "021-260": [("010", "Avionics-Cooling-Fan", "STD"),
                ("030", "Avionics-Cooling-Ducting-and-Exhaust", "STD"),
                ("050", "Avionics-Cooling-Control-and-Override", "STD")],
    "021-270": [("010", "Cargo-Ventilation-Fan", "STD"),
                ("030", "Cargo-Ventilation-Ducting", "STD")],
    "021-280": [("010", "Equipment-Cooling-Ventilation", "STD"),
                ("030", "Galley-Chiller-Ventilation", "STD")],
    "021-290": [("010", "LP-Ground-Air-Connection", "STD"),
                ("030", "Ground-Supply-Check-Valve", "STD")],
    "021-300": [("010", "Pressurization-General-and-Schedule", "STD")],
    "021-310": [("010", "Outflow-Valve-and-Actuator", "STD"),
                ("030", "Cabin-Pressure-Controller", "STD"),
                ("050", "Pressurization-Indication-and-Sensors", "STD")],
    "021-320": [("010", "Positive-Pressure-Relief-Valve", "STD"),
                ("030", "Negative-Pressure-Relief-Valve", "STD")],
    "021-330": [("010", "Cargo-Pressure-Equalization-Valves", "STD")],
    "021-400": [("010", "Heating-General", "STD")],
    "021-410": [("010", "Floor-Heating-Panels", "STD"),
                ("030", "Floor-Heating-Controller-and-Sensors", "STD")],
    "021-500": [("010", "Integrated-Cooling-General-and-Architecture", "ELEC")],
    "021-510": [("010", "Electrically-Driven-Cooling-Compressor", "ELEC"),
                ("030", "Heat-Exchanger-Network", "ELEC"),
                ("050", "Working-Fluid-Refrigerant-Loop", "ELEC"),
                ("070", "Water-Extraction-and-Humidity-Control", "STD"),
                ("090", "Cooling-Control-Sensors-and-Protection", "ELEC")],
    "021-600": [("010", "Temperature-Control-General-and-Zoning", "ELEC")],
    "021-610": [("010", "Flight-Deck-Electric-Reheat-Trim", "ELEC"),
                ("030", "Flight-Deck-Zone-Sensors-and-Controller", "STD")],
    "021-620": [("010", "Cabin-Zone-Electric-Reheat-Trim", "ELEC"),
                ("030", "Cabin-Zone-Sensors-and-Controller", "STD")],
    "021-900": [("010", "Energy-Source-Waste-Heat-Recovery", "STD-G"),
                ("030", "Cryogenic-Cold-Sink-Utilization", "STD-G"),
                ("050", "ECS-Thermal-Management-System-Coupling", "STD-G"),
                ("070", "Bleedless-Air-Supply-Interface", "STD-G")],
}


def infocode_menu(title, layer):
    """Menu info-code AMM tipico, scelto per tipo di subject."""
    t = title.lower()
    if layer == "STD-G":
        return ["040", "034", "200"]
    if any(k in t for k in ["fan", "valve", "compressor", "panel", "unit",
                            "filter", "scoop", "manifold", "outlet",
                            "diffuser", "connection"]):
        return ["040", "200", "300", "520", "720"]
    if any(k in t for k in ["control", "controller", "sensor", "indication",
                            "reheat", "trim"]):
        return ["040", "034", "200", "300"]
    return ["040", "200", "300"]  # ducting / general / interface


def write(path, text):
    if (not OVERWRITE) and os.path.exists(path):
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return True


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    root = os.path.join(base, ROOT_REL)
    n_sub = 0

    for sid, (stitle, slayer) in SECTIONS.items():
        sec_dir = os.path.join(root, "%s_%s" % (sid, stitle))
        os.makedirs(sec_dir, exist_ok=True)
        subs = SUBJECTS.get(sid, [])

        sub_lines = "".join(
            "- [`%s-%s`](%s-%s_%s) - %s | %s\n"
            % (sid, suf, sid, suf, t, t.replace("-", " "), lay)
            for suf, t, lay in subs
        ) or "- (nessun subject definito)\n"

        write(os.path.join(sec_dir, "README.md"),
              "---\nnode: %s\ntitle: %s\nlayer: \"%s\"\nmodel: eWTW\n"
              "pmc: PMC-EWTW-AMM\nstatus: scaffold\n---\n\n# %s - %s\n\n"
              "Subject node (ogni directory contiene il breakdown info-code "
              "secondo %s):\n\n%s"
              % (sid, stitle.replace("-", " "), slayer, sid,
                 stitle.replace("-", " "), CONVENTION, sub_lines))

        for suf, t, lay in subs:
            subj = "%s-%s" % (sid, suf)
            subj_dir = os.path.join(sec_dir, "%s_%s" % (subj, t))
            os.makedirs(subj_dir, exist_ok=True)
            codes = infocode_menu(t, lay)
            codestr = "[" + ", ".join('{code: "%s"}' % c for c in codes) + "]"
            status = ('"developed - full CM package available (%s demo)"' % CONVENTION
                      if subj == DEV else "stub")
            write(os.path.join(subj_dir, "subject-infocode-breakdown.yaml"),
                  "subject_infocode_breakdown:\n  subject: %s\n  title: %s\n"
                  "  section: %s\n  layer: \"%s\"\n  model: eWTW\n"
                  "  pmc: PMC-EWTW-AMM\n  convention: %s\n"
                  "  amm_infocodes: %s\n  status: %s\n  version: \"1.0\"\n"
                  % (subj, t.replace("-", " "), sid, lay, CONVENTION, codestr, status))
            n_sub += 1

    # README di capitolo
    rows = ""
    for sid, (stitle, slayer) in SECTIONS.items():
        rows += "| `%s` | %s | %s | %d |\n" % (
            sid, stitle.replace("-", " "), slayer, len(SUBJECTS.get(sid, [])))
    write(os.path.join(root, "README.md"),
          "---\nchapter: \"021\"\ntitle: Air Conditioning & Environmental Control\n"
          "model: eWTW\npmc: PMC-EWTW-AMM\nband: G-ATLAS_000-099\n"
          "doctrine: green-native\nstatus: scaffold\nversion: \"1.0\"\n---\n\n"
          "# 021 - Air Conditioning & Environmental Control - Subject Nodes (eWTW / AMM)\n\n"
          "%d subject node su %d sezioni. Subject = directory con breakdown "
          "info-code secondo **%s** (stub finche' non realizzato).\n\n"
          "## Section register\n\n| Section | Title | Layer | Subjects |\n"
          "|---|---|:--:|:--:|\n%s\n"
          "> Layer: **STD** carries - **ELEC** sostituzione elettrica "
          "(cooling 021-500/510; trim->reheat elettrico 021-600/610/620) - "
          "**STD-G** green delta.\n"
          % (n_sub, len(SECTIONS), CONVENTION, rows))

    print("OK: %d subject node creati su %d sezioni." % (n_sub, len(SECTIONS)))
    print("Root: %s" % os.path.normpath(root))


if __name__ == "__main__":
    main()
