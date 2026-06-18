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


PMC = "PMC-EWTW-AMM"
PUB_TREE = "AMM"  # publication-tree entry the AMM subjects feed
OWNER = "Q-AIR"
ISSUE_DATE = ("2026", "06", "13")  # deterministic issue date for stub DMs

# info code -> (S1000D info name, S1000D 4.2 flat schema basename)
INFO_NAMES = {
    "040": ("Description", "descript"),
    "034": ("Operating principles", "descript"),
    "200": ("Servicing", "proced"),
    "300": ("Scheduled maintenance", "proced"),
    "520": ("Remove procedures", "proced"),
    "720": ("Install procedures", "proced"),
}


def sns_from_subject(subj):
    """Provisional SNS derived from the G-ATLAS triplet 021-SSS-UUU.

    Mirrors the existing AMM convention, e.g. 021-510-010 -> systemCode 21,
    subSystemCode 5, subSubSystemCode 1, assyCode 01 (DMC-EWTW-A-21-51-01-...).
    """
    chap, section3, subjsuf = subj.split("-")
    return {
        "systemCode": chap[1:],          # "021" -> "21"
        "subSystemCode": section3[0],    # "510" -> "5"
        "subSubSystemCode": section3[1],  # "510" -> "1"
        "assyCode": subjsuf[:2],         # "010" -> "01"
    }


def dmc_handle(sns, code):
    """Full provisional DMC string for the given SNS and info code."""
    return ("DMC-EWTW-A-%s-%s%s-%s-00A-%sA-A"
            % (sns["systemCode"], sns["subSystemCode"],
               sns["subSubSystemCode"], sns["assyCode"], code))


def dm_xml(sns, code, tech_name):
    """Minimal valid S1000D 4.2 data-module stub for a given info code."""
    info_name, schema = INFO_NAMES.get(code, ("Description", "descript"))
    yr, mo, dy = ISSUE_DATE
    if schema == "proced":
        content = (
            '    <procedure>\n'
            '      <preliminaryRqmts/>\n'
            '      <mainProcedure>\n'
            '        <proceduralStep><para>%s — %s. Stub step pending authoring.</para></proceduralStep>\n'
            '      </mainProcedure>\n'
            '      <closeRqmts/>\n'
            '    </procedure>\n'
            % (tech_name, info_name))
    else:
        content = (
            '    <description>\n'
            '      <levelledPara>\n'
            '        <title>General</title>\n'
            '        <para>%s — %s. Stub data module pending authoring.</para>\n'
            '      </levelledPara>\n'
            '    </description>\n'
            % (tech_name, info_name))
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<dmodule xmlns:xlink="http://www.w3.org/1999/xlink"\n'
        '         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'
        '         xsi:noNamespaceSchemaLocation="http://www.s1000d.org/'
        'S1000D_4-2/xml_schema_flat/%s.xsd">\n'
        '  <identAndStatusSection>\n'
        '    <dmAddress>\n'
        '      <dmIdent>\n'
        '        <dmCode modelIdentCode="EWTW" systemDiffCode="A" systemCode="%s" subSystemCode="%s"\n'
        '                subSubSystemCode="%s" assyCode="%s" disassyCode="00" disassyCodeVariant="A"\n'
        '                infoCode="%s" infoCodeVariant="A" itemLocationCode="A"/>\n'
        '        <language languageIsoCode="en" countryIsoCode="GB"/>\n'
        '        <issueInfo issueNumber="001" inWork="00"/>\n'
        '      </dmIdent>\n'
        '      <dmAddressItems>\n'
        '        <issueDate year="%s" month="%s" day="%s"/>\n'
        '        <dmTitle>\n'
        '          <techName>%s</techName>\n'
        '          <infoName>%s</infoName>\n'
        '        </dmTitle>\n'
        '      </dmAddressItems>\n'
        '    </dmAddress>\n'
        '    <dmStatus issueType="new">\n'
        '      <security securityClassification="01"/>\n'
        '      <responsiblePartnerCompany><enterpriseName>QplusA .INC</enterpriseName></responsiblePartnerCompany>\n'
        '      <originator><enterpriseName>QplusA .INC</enterpriseName></originator>\n'
        '      <applic><displayText><simplePara>eWTW</simplePara></displayText></applic>\n'
        '      <brexDmRef>\n'
        '        <dmRef><dmRefIdent><dmCode modelIdentCode="EWTW" systemDiffCode="A" systemCode="00"\n'
        '          subSystemCode="0" subSubSystemCode="0" assyCode="00" disassyCode="00"\n'
        '          disassyCodeVariant="A" infoCode="022" infoCodeVariant="A" itemLocationCode="D"/></dmRefIdent></dmRef>\n'
        '      </brexDmRef>\n'
        '      <qualityAssurance><unverified/></qualityAssurance>\n'
        '    </dmStatus>\n'
        '  </identAndStatusSection>\n'
        '  <content>\n'
        '%s'
        '  </content>\n'
        '</dmodule>\n'
        % (schema, sns["systemCode"], sns["subSystemCode"], sns["subSubSystemCode"],
           sns["assyCode"], code, yr, mo, dy, tech_name, info_name, content)
    )


def is_developed(subj_dir):
    """True if the subject already holds the AMM info-code-folder package
    (e.g. 040_Description/); such curated nodes are left untouched."""
    if not os.path.isdir(subj_dir):
        return False
    for name in os.listdir(subj_dir):
        if os.path.isdir(os.path.join(subj_dir, name)) and name[:3].isdigit() and "_" in name:
            return True
    return False


def emit_subject_package(subj_dir, subj, title, layer, codes):
    """Write the ECHM-style subject package (mirrors PMC-EWTW-ECHM
    003-900-010): metadata + registers + DM/ICN/evidence/pub folders."""
    sid = subj.rsplit("-", 1)[0]
    tech_name = title.replace("-", " ")
    sns = sns_from_subject(subj)
    digits = subj.replace("-", "")
    dm_dir = os.path.join(subj_dir, "DM")
    icn_dir = os.path.join(subj_dir, "ICN")
    ev_dir = os.path.join(subj_dir, "evidence")
    pub_dir = os.path.join(subj_dir, "pub")
    for d in (dm_dir, icn_dir, ev_dir, pub_dir):
        os.makedirs(d, exist_ok=True)

    dm_rows = []
    dm_files = []
    for code in codes:
        info_name, _ = INFO_NAMES.get(code, ("Description", "descript"))
        handle = dmc_handle(sns, code)
        fname = "%s_001-00_en-GB.xml" % handle
        write(os.path.join(dm_dir, fname), dm_xml(sns, code, tech_name))
        dm_files.append(handle)
        dm_rows.append((code, info_name, handle, fname))

    # ICN stub (one placeholder illustration)
    icn = "ICN-EWTW-%s-001-01" % digits
    write(os.path.join(icn_dir, "%s.svg" % icn),
          '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800">\n'
          '  <rect width="1200" height="800" fill="#f4f4f4" stroke="#999"/>\n'
          '  <text x="600" y="400" font-family="sans-serif" font-size="28" '
          'text-anchor="middle" fill="#555">%s — placeholder</text>\n</svg>\n'
          % tech_name)

    # subject-metadata.yaml
    dmset = "[" + ", ".join('"%s"' % c for c in codes) + "]"
    write(os.path.join(subj_dir, "subject-metadata.yaml"),
          "---\n# subject-metadata.yaml — %s %s\n"
          "# Authoritative subject definition for the eWTW projection.\n\n"
          'subject: "%s"\ntitle: "%s"\n'
          "description: >-\n  %s subject package for the eWTW AMM "
          "(%s · %s layer).\n\n"
          'parent_node: "%s"\npmc: "%s"\nmodel: "eWTW"\nmic: "EWTW"\n'
          'side: "PUB"\nowner: "%s"\n\n'
          "dm_set: %s\n\n"
          "sns:\n  system_code: \"%s\"\n  sub_system: \"%s\"\n"
          "  sub_sub_system: \"%s\"\n  assy: \"%s\"\n  status: \"PROVISIONAL\"\n"
          "  pending: \"_CSDB-CONTROL/SNS-mapping.yaml\"\n\n"
          "feeds_tree:\n  - \"%s\"\n\n"
          "convention: \"%s\"\ngovernance:\n  - \"LC-A..LC-N\"\n  - \"SSOT+PUB\"\n\n"
          'status: "scaffold"\nversion: "1.0"\n'
          % (subj, tech_name, subj, tech_name, tech_name, sid, layer,
             sid, PMC, OWNER, dmset, sns["systemCode"], sns["subSystemCode"],
             sns["subSubSystemCode"], sns["assyCode"], PUB_TREE, CONVENTION))

    # dm-register.yaml
    dm_yaml = ""
    for code, info_name, handle, fname in dm_rows:
        dm_yaml += (
            '  - short_handle: "DMC-EWTW-%s-%s"\n'
            '    full_dmc: "%s"\n'
            '    info_code: "%s"\n    type: "%s"\n    language: "en-GB"\n'
            '    issue: "001-00"\n    in_work: true\n    quality: "unverified"\n'
            '    file: "DM/%s"\n\n'
            % (subj, code, handle, code, info_name, fname))
    write(os.path.join(subj_dir, "dm-register.yaml"),
          "---\n# dm-register.yaml — %s %s\n"
          "# Data module allocation and ICN register.\n\n"
          'subject: "%s"\ntitle: "%s"\npmc: "%s"\n\n'
          "data_modules:\n%s"
          "illustrations:\n  - icn: \"%s\"\n    caption: \"%s — general arrangement\"\n"
          "    used_by: %s\n    file: \"ICN/%s.svg\"\n\n"
          'sns_status: "PROVISIONAL — pending _CSDB-CONTROL/SNS-mapping.yaml"\n'
          % (subj, tech_name, subj, tech_name, PMC, dm_yaml, icn, tech_name,
             dmset, icn))

    # applicability.yaml
    write(os.path.join(subj_dir, "applicability.yaml"),
          "---\n# applicability.yaml — %s %s\n"
          "# Carrier-binding and exclusion rules for the subject's data modules.\n\n"
          'subject: "%s"\ntitle: "%s"\npmc: "%s"\n\n'
          "applicability:\n  carrier: \"eWTW\"\n"
          "  carrier_description: \"Electric wing-to-wing configuration\"\n"
          "  binding: \"electric\"\n"
          "  brex: \"DMC-EWTW-A-00-00-00-00A-022A-D\"\n"
          "  security: \"01\"  # unclassified\n\n"
          "  applicable_models:\n    - model: \"eWTW\"\n"
          "      description: \"Electric wing-to-wing configuration\"\n\n"
          "all_dms_bind_to: \"eWTW\"\n"
          % (subj, tech_name, subj, tech_name, PMC))

    # evidence/
    req_rows = "".join(
        "| TBD-%s-%03d | TBD requirement for %s | `%s` | TBD | TBD |\n"
        % (subj[-3:], i + 1, info_name.lower(), code)
        for i, (code, info_name, _, _) in enumerate(dm_rows))
    write(os.path.join(ev_dir, "interface-requirements-matrix.md"),
          "# Interface Requirements Matrix — %s\n\n"
          "Requirement -> DM -> verification trace for the %s subject.\n\n"
          "| Req ID | Requirement | DM(s) | Verification method | Status |\n"
          "|---|---|---|---|---|\n%s\n"
          "> **Note:** Requirement IDs are provisional (TBD-nnn-nnn) pending "
          "formal allocation in the ReqBS register.\n"
          % (subj, tech_name, req_rows))
    write(os.path.join(ev_dir, "standards-cross-reference.md"),
          "# Standards Cross-Reference — %s\n\n"
          "Standards map for the %s subject. TBDs are flagged; no standards "
          "are invented.\n\n"
          "| Topic | Standard / Reference | Status | Notes |\n|---|---|---|---|\n"
          "| Maintenance information | S1000D Issue 4.2 | Reference | "
          "Data module authoring specification |\n"
          "| Subject standards | TBD | TBD | Pending allocation |\n\n"
          "> **Note:** Cross-references will be updated as applicable standards "
          "mature.\n"
          % (subj, tech_name))
    vs_rows = "".join(
        "  - dmc: \"%s\"\n    info_code: \"%s\"\n    type: \"%s\"\n"
        "    quality: \"unverified\"\n    issue: \"001-00\"\n    in_work: true\n"
        "    lc_gate: null\n    last_review: null\n    reviewer: null\n\n"
        % (handle, code, info_name)
        for code, info_name, handle, _ in dm_rows)
    write(os.path.join(ev_dir, "verification-status.yaml"),
          "---\n# verification-status.yaml — %s %s\n"
          "# Per-DM QA state and lifecycle gates.\n\n"
          'subject: "%s"\ntitle: "%s"\n\n'
          "data_modules:\n%s"
          'overall_status: "unverified"\n'
          % (subj, tech_name, subj, tech_name, vs_rows))

    # pub/ link index
    refs = "".join('  - "%s"\n' % h for h in dm_files)
    write(os.path.join(pub_dir, "%s.link" % PUB_TREE),
          "# %s.link — Publication-tree pointer\n"
          "# Subject %s feeds %s\n"
          "# This is a link index entry, not a copy of the PM.\n\n"
          'target_tree_entry: "%s"\nsubject: "%s"\ndms_referenced:\n%s'
          % (PUB_TREE, subj, PUB_TREE, PUB_TREE, subj, refs))

    # README.md (ECHM-style subject package overview)
    dmc_table = "".join(
        "| `DMC-EWTW-%s-%s` | `%s` | %s | %s |\n"
        % (subj, code, handle, code, info_name)
        for code, info_name, handle, _ in dm_rows)
    write(os.path.join(subj_dir, "README.md"),
          "---\nsubject: %s\ntitle: %s — Subject Package\n"
          "pmc: %s\nparent_node: %s\nmodel: eWTW\nmic: EWTW\nside: PUB\n"
          "owner: %s\nfeeds_tree: [%s]\ndm_set: %s\n"
          "sns_status: \"PROVISIONAL — pending _CSDB-CONTROL/SNS-mapping.yaml\"\n"
          "status: scaffold\nversion: \"1.0\"\n---\n\n"
          "# %s — %s · Subject Package\n\n"
          "TPuBS container for the **%s** subject of chapter `%s`, projected to "
          "the eWTW AMM. Structure mirrors the PMC-EWTW-ECHM subject package "
          "(`003-900-010`).\n\n"
          "## Directory tree\n\n```text\n%s_%s/\n"
          "├── README.md\n├── subject-metadata.yaml\n├── dm-register.yaml\n"
          "├── applicability.yaml\n├── DM/                # S1000D 4.2 data modules\n"
          "├── ICN/               # illustrations\n"
          "├── evidence/          # leaf-level traceability\n"
          "└── pub/               # publication-tree pointers\n```\n\n"
          "## DMC allocation\n\nSNS (`systemCode %s · subSystem %s · "
          "subSubSystem %s · assy %s`) is **derived** from the G-ATLAS triplet "
          "and **provisional** pending `_CSDB-CONTROL/SNS-mapping.yaml`.\n\n"
          "| Short handle | Full DMC (provisional) | Info | Type |\n"
          "|---|---|---|---|\n%s\n"
          "## References\n\n"
          "1. S1000D — *International Specification for Technical Publications*, "
          "Issue 4.2. https://s1000d.org/\n"
          "2. Convention `%s`.\n"
          % (subj, tech_name, PMC, sid, OWNER, PUB_TREE, dmset,
             subj, tech_name, tech_name, sid, subj, title,
             sns["systemCode"], sns["subSystemCode"], sns["subSubSystemCode"],
             sns["assyCode"], dmc_table, CONVENTION))


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
            n_sub += 1
            # Leave curated/developed AMM nodes (info-code-folder package) untouched.
            if is_developed(subj_dir):
                continue
            codes = infocode_menu(t, lay)
            emit_subject_package(subj_dir, subj, t, lay, codes)

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
