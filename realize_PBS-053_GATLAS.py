#!/usr/bin/env python3
# =============================================================================
# realize_PBS-053_GATLAS.py — eWTW PBS chapter 053, G-ATLAS-coherent (v2.0.0)
# -----------------------------------------------------------------------------
# SUPERSEDES the x10-section draft (realize_PBS-053_chapter.py, v1). The v1
# section grammar (053-010..053-110) was NOT coherent with the G-ATLAS 053
# schema, which uses ATA-section x10 codes rendered as 3-digit fields
# (053-000, 053-100 .. 053-900) — the same grammar already used by the TPuBS
# chapter 021 nodes (021-000 / 021-200 / 021-300 / 021-510) and by the ICN
# battery-bay reference 053-900. Under the 1:1-by-number doctrine (PBS code =
# SSOT taxonomy code = AMM SNS code), the PBS conforms to G-ATLAS.
#
# Sections and subjects below are EXACTLY the G-ATLAS 053 register:
#   000 General | 100 Nose-and-Forward | 200 Center | 300 Aft |
#   400 Tailcone-and-APM | 500 Skin-Panels-and-Doublers |
#   600 Frames-Stringers-and-Longerons | 700 Floor-and-Pressure-Deck |
#   800 Pressure-Bulkheads-and-Major-Attach-Fittings |
#   900 Energy-Carrier-Structural-Integration
# plus ONE proposed taxonomy extension: 053-600-090 Keel-Beam-Structure
# (requires ruling; delete its entry below to drop it).
#
# Conventions:
#   * CSN grammar per AMPEL360-PBS-PN-CM-001: EWTW-53SU-III where S=section
#     hundreds+tens ('00','10'..'90') and U=subject tens ('01'..'09');
#     items x10, children +1..+9 (LH/RH variants or constituents). No-AAA.
#   * SSOT precedence: FOLDER NAME authoritative; YAML mirrors.
#   * YAML schemas reconstructed; align keys on diff vs realized exemplar.
#   * Standards families (splices, cutout doublers, clips, lugs) are chapter
#     051 Standard-Practices-Structures scope and are NOT realized here.
#   * Production joins are realized as zone-general splice hardware plus
#     assembly stations; there is no join subject in G-ATLAS 053.
#
# Behaviour: idempotent (skip-existing), --overwrite, --dry-run, --manifest,
# --migration-map. No zips. Legacy x10 folders are never touched or deleted.
#
# Usage (from repo root):
#   python3 realize_PBS-053_GATLAS.py --dry-run
#   python3 realize_PBS-053_GATLAS.py --manifest PBS-053-BREAKDOWN.md
#   python3 realize_PBS-053_GATLAS.py --migration-map
# =============================================================================

import argparse
import pathlib
import sys

MIC = "EWTW"
CHAPTER = "053"
DATE = "2026-07-06"
VERSION = "2.0.0-GATLAS"

PBS_PATH = (
    "01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/"
    "01-02-01-01_MODELS/01-02-01-01-01_eWTW/"
    "01-02-01-01-01-01_SBS_System-Breakdown-Structure/"
    "01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/"
    "eWTW-PBS-000_Aircraft-Product/"
    "eWTW-PBS-050_Airframe-Structure/"
    "eWTW-PBS-053-000_Fuselage-Wide-Tube"
)

SCHEMA_NOTE = (
    "AMPEL360-PBS-PN-CM-001 - schema reconstructed by generator; "
    "folder name is SSOT, this file mirrors it"
)

GEN_NOTE = f"Generated {DATE} - realize_PBS-053_GATLAS.py ({VERSION}) - No-AAA compliant"

# =============================================================================
# BREAKDOWN — G-ATLAS-coherent chapter SSOT.
# section: (code, Title-Hyphenated, [subjects])
# subject: (code, Title-Hyphenated, [items], [notes])
# item:    (num, NOMENCLATURE, [children])
# =============================================================================

BREAKDOWN = [
    ("000", "General", [
        ("010", "Fuselage-General", [
            ("000", "STRUCTURE-FUSELAGE-GENERAL", []),
            ("010", "MARKING-AND-PLACARD-PROVISION-SET", []),
            ("020", "BONDING-AND-GROUNDING-PROVISION-SET", []),
        ], []),
        ("020", "Fuselage-Protective-Films-and-Tapes", [
            ("000", "SET-PROTECTIVE-FILMS-AND-TAPES", []),
            ("010", "FILM-EROSION-PROTECTION-SET", []),
            ("020", "TAPE-AERO-SEAL-SET", []),
            ("030", "FILM-ANTI-CHAFE-SET", []),
        ], []),
        ("030", "Fuselage-External-Access-Doors-and-Panels-General", [
            ("000", "SET-EXTERNAL-ACCESS-GENERAL", []),
            ("010", "LATCH-PANEL-STANDARD", []),
            ("020", "HINGE-PANEL-STANDARD", []),
            ("030", "SEAL-PANEL-STANDARD", []),
        ], ["Panel INSTANCES live in the zone access-panel subjects "
            "(100-060, 200-060, 300-040, 400-050)."]),
        ("040", "Fuselage-Drains", [
            ("000", "SET-FUSELAGE-DRAINS", []),
            ("010", "MAST-DRAIN", []),
            ("020", "VALVE-DRAIN-SET", []),
            ("030", "PATH-DRAIN-BILGE-SET", []),
        ], []),
    ]),
    ("100", "Nose-and-Forward-Fuselage-Structure", [
        ("010", "Forward-Fuselage-Zone-General", [
            ("000", "STRUCTURE-FORWARD-FUSELAGE-ZONE", []),
            ("010", "SPLICE-RING-FWD-TO-CENTER-JOIN", [
                ("011", "SPLICE-RING-SEGMENT-UPPER"),
                ("012", "SPLICE-RING-SEGMENT-LOWER"),
            ]),
            ("020", "FITTING-JOIN-INDEXING", []),
            ("030", "SHIM-SET-CONTROLLED-JOIN", []),
        ], ["Zone-general owns the AFT production join splice hardware; the "
            "join operation itself is an assembly station (station.yaml)."]),
        ("020", "Nose-Landing-Gear-Bay-and-Door-Supports", [
            ("000", "STRUCTURE-NLG-BAY-AND-DOOR-SUPPORTS", []),
            ("010", "WALL-NLG-BAY-SIDE", [
                ("011", "WALL-NLG-BAY-SIDE-LH"),
                ("012", "WALL-NLG-BAY-SIDE-RH"),
            ]),
            ("020", "BULKHEAD-NLG-BAY-AFT", []),
            ("030", "BEAM-NLG-DOOR-HINGE-SUPPORT", []),
            ("040", "FRAME-NLG-BAY-ROOF-SUPPORT", []),
        ], ["NLG trunnion/drag fittings: 053-800-030. NLG bay pressure deck: "
            "053-700-020. Landing gear itself: ATA 032."]),
        ("030", "Forward-Avionics-Compartment-Structure", [
            ("000", "STRUCTURE-FWD-AVIONICS-COMPARTMENT", []),
            ("010", "FLOOR-GRID-COMPARTMENT", [
                ("011", "BEAM-LATERAL-SET"),
                ("012", "INTERCOSTAL-SET"),
            ]),
            ("020", "RAIL-EQUIPMENT-RACK-SUPPORT", []),
            ("030", "PANEL-COMPARTMENT-PARTITION", []),
            ("040", "SUPPORT-VENTILATION-DUCT-PROVISION", []),
        ], ["E-E bay ventilation function is ATA 021 (REF ICN-EWTW-021000010)."]),
        ("040", "Radome-and-Diverters-Attach-Structure", [
            ("000", "STRUCTURE-RADOME-AND-NOSE-CONE-ATTACH", []),
            ("010", "STRUCTURE-RADOME-ATTACH", [
                ("011", "FRAME-RADOME-ATTACH-RING"),
                ("012", "FITTING-RADOME-ATTACH-BACKUP"),
            ]),
            ("020", "FITTING-RADOME-HINGE", [
                ("021", "FITTING-RADOME-HINGE-LH"),
                ("022", "FITTING-RADOME-HINGE-RH"),
            ]),
            ("030", "FITTING-RADOME-LATCH", []),
            ("040", "STRIP-LIGHTNING-DIVERTER", []),
            ("050", "SEAL-RADOME-PERIMETER", []),
            ("060", "BRACKET-WEATHER-RADAR-ANTENNA-MOUNT", []),
        ], ["MIGRATION: realized in-repo at legacy eWTW-PBS-053-010-010 with "
            "CSN 530101. New identity is CSN 531004; item numbers and "
            "nomenclatures map 1:1 (EWTW-530101-xxx -> EWTW-531004-xxx)."]),
        ("050", "Forward-Fuselage-Direct-Vision-Window", [
            ("000", "STRUCTURE-DV-WINDOW-SURROUND", []),
            ("010", "FRAME-DV-WINDOW", [
                ("011", "FRAME-DV-WINDOW-LH"),
                ("012", "FRAME-DV-WINDOW-RH"),
            ]),
            ("020", "SILL-AND-HEADER-DV", []),
            ("030", "DOUBLER-DV-SURROUND", []),
        ], ["Transparencies and mechanisms: ATA 056. Windshield formers/posts: "
            "053-600-070."]),
        ("060", "Forward-Fuselage-External-Access-Panels", [
            ("000", "SET-ACCESS-PANELS-FWD", []),
            ("010", "PANEL-ACCESS-EQUIPMENT-BAY", []),
            ("020", "PANEL-ACCESS-SERVICE-SET", []),
            ("030", "SURROUND-PANEL-CUTOUT-SET", []),
        ], []),
    ]),
    ("200", "Center-Fuselage-Structure", [
        ("010", "Center-Fuselage-Zone-General", [
            ("000", "STRUCTURE-CENTER-FUSELAGE-ZONE", []),
            ("010", "SPLICE-RING-CENTER-TO-AFT-JOIN", [
                ("011", "SPLICE-RING-SEGMENT-UPPER"),
                ("012", "SPLICE-RING-SEGMENT-LOWER"),
            ]),
            ("020", "FITTING-JOIN-INDEXING", []),
            ("030", "SHIM-SET-CONTROLLED-JOIN", []),
        ], ["Wing-attach reinforced frames: 053-600-020. Wing-side attach "
            "lugs: ATA 057 (ruling pending on fuselage-side lug ownership)."]),
        ("020", "Wing-to-Fuselage-Fairing", [
            ("000", "STRUCTURE-WING-TO-FUSELAGE-FAIRING", []),
            ("010", "PANEL-FAIRING-FWD", [
                ("011", "PANEL-FAIRING-FWD-LH"),
                ("012", "PANEL-FAIRING-FWD-RH"),
            ]),
            ("020", "PANEL-FAIRING-CENTER", [
                ("021", "PANEL-FAIRING-CENTER-LH"),
                ("022", "PANEL-FAIRING-CENTER-RH"),
            ]),
            ("030", "PANEL-FAIRING-AFT", [
                ("031", "PANEL-FAIRING-AFT-LH"),
                ("032", "PANEL-FAIRING-AFT-RH"),
            ]),
            ("040", "FRAME-FAIRING-SUBSTRUCTURE-SET", []),
            ("050", "RAIL-PACK-MOUNT", [
                ("051", "RAIL-PACK-MOUNT-LH"),
                ("052", "RAIL-PACK-MOUNT-RH"),
            ]),
            ("060", "SEAL-FAIRING-PERIPHERAL", []),
        ], ["Hosts the unpressurized pack bay (PB in ICN-EWTW-021000010); "
            "E-PACK units are ATA 021-510."]),
        ("030", "Main-Landing-Gear-Wheelwell-and-Sealing", [
            ("000", "STRUCTURE-MLG-WHEELWELL", []),
            ("010", "WALL-WHEELWELL-SIDE", [
                ("011", "WALL-WHEELWELL-SIDE-LH"),
                ("012", "WALL-WHEELWELL-SIDE-RH"),
            ]),
            ("020", "BULKHEAD-WHEELWELL-FWD", []),
            ("030", "BULKHEAD-WHEELWELL-AFT", []),
            ("040", "SEAL-WHEELWELL-PERIMETER", []),
            ("050", "BEAM-MLG-DOOR-HINGE-SUPPORT", []),
        ], ["MLG wheelwell pressure deck: 053-700-030. MLG trunnion fittings: "
            "ATA 057 if wing-mounted gear (eWTW gear config ruling pending)."]),
        ("040", "Antenna-Provisions-and-Reinforcements", [
            ("000", "SET-ANTENNA-PROVISIONS", []),
            ("010", "DOUBLER-ANTENNA-CROWN-SET", []),
            ("020", "PROVISION-ANTENNA-MOUNT-SET", []),
            ("030", "PLATE-BACKING-ANTENNA-SET", []),
        ], []),
        ("050", "Middle-Avionics-Compartment-Structure", [
            ("000", "STRUCTURE-MID-AVIONICS-COMPARTMENT", []),
            ("010", "FLOOR-GRID-COMPARTMENT", []),
            ("020", "RAIL-EQUIPMENT-RACK-SUPPORT", []),
            ("030", "PANEL-COMPARTMENT-PARTITION", []),
        ], []),
        ("060", "Center-Fuselage-External-Access-and-Service-Doors", [
            ("000", "SET-ACCESS-AND-SERVICE-DOORS-CENTER", []),
            ("010", "PANEL-ACCESS-BELLY-SET", []),
            ("020", "SURROUND-SERVICE-DOOR-SMALL-SET", []),
            ("030", "PANEL-ACCESS-FAIRING-SET", []),
        ], ["Main pax/cargo door surrounds: 053-600-080; their fittings and "
            "sills: 053-800-040/-050/-080. Door leaves: 052."]),
    ]),
    ("300", "Aft-Fuselage-Structure", [
        ("010", "Rear-Fuselage-Zone-General", [
            ("000", "STRUCTURE-REAR-FUSELAGE-ZONE", []),
            ("010", "SPLICE-RING-AFT-TO-TAILCONE-JOIN", [
                ("011", "SPLICE-RING-SEGMENT-UPPER"),
                ("012", "SPLICE-RING-SEGMENT-LOWER"),
            ]),
            ("020", "FITTING-JOIN-INDEXING", []),
            ("030", "SUPPORT-SYSTEMS-RUN-SET", []),
            ("040", "SURROUND-OUTFLOW-VALVE", []),
        ], ["Outflow valve function: ATA 021-300; structural surround only."]),
        ("020", "Rear-Fuselage-Adjustable-Rods", [
            ("000", "SET-ADJUSTABLE-RODS-REAR", []),
            ("010", "ROD-ADJUSTABLE", [
                ("011", "ROD-ADJUSTABLE-LH"),
                ("012", "ROD-ADJUSTABLE-RH"),
            ]),
            ("020", "FITTING-ROD-END-SET", []),
            ("030", "BRACKET-ROD-SUPPORT-SET", []),
        ], []),
        ("030", "Tail-Bumper", [
            ("000", "STRUCTURE-TAIL-BUMPER", []),
            ("010", "SHOE-TAIL-BUMPER", []),
            ("020", "ABSORBER-TAIL-BUMPER", []),
            ("030", "FITTING-BUMPER-ATTACH", []),
        ], []),
        ("040", "Rear-Fuselage-External-Access-Panels", [
            ("000", "SET-ACCESS-PANELS-REAR", []),
            ("010", "PANEL-ACCESS-EMPENNAGE-SERVICE-SET", []),
            ("020", "PANEL-ACCESS-BULK-SET", []),
        ], []),
    ]),
    ("400", "Tailcone-and-Auxiliary-Power-Module-Structure", [
        ("010", "Tailcone-Zone-General", [
            ("000", "STRUCTURE-TAILCONE-ZONE", []),
            ("010", "BULKHEAD-TAILCONE-CLOSURE", []),
            ("020", "PROVISION-TAIL-NAV-LIGHT-MOUNT", []),
        ], ["Tailcone frames/longerons: 053-600-060; tailcone skins: "
            "053-500-060."]),
        ("020", "Auxiliary-Power-Module-Mounts-and-Support-Struts", [
            ("000", "STRUCTURE-APM-MOUNTS", []),
            ("010", "MOUNT-APM-ISOLATOR", [
                ("011", "MOUNT-APM-ISOLATOR-FWD"),
                ("012", "MOUNT-APM-ISOLATOR-AFT"),
            ]),
            ("020", "STRUT-APM-SUPPORT-SET", []),
            ("030", "RAIL-APM-INSTALLATION", []),
        ], ["APM unit itself: ATA 049 family (electric auxiliary module)."]),
        ("030", "Auxiliary-Power-Module-Firewall-and-Thermal-Provisions", [
            ("000", "STRUCTURE-APM-FIREWALL", []),
            ("010", "BULKHEAD-APM-CONTAINMENT-FIREWALL", []),
            ("020", "SHIELD-THERMAL-SET", []),
            ("030", "SEAL-FIREWALL-PENETRATION-SET", []),
        ], []),
        ("040", "Rudder-Root-Aft-Fairing", [
            ("000", "STRUCTURE-RUDDER-ROOT-FAIRING", []),
            ("010", "PANEL-FAIRING-RUDDER-ROOT", [
                ("011", "PANEL-FAIRING-RUDDER-ROOT-LH"),
                ("012", "PANEL-FAIRING-RUDDER-ROOT-RH"),
            ]),
            ("020", "SEAL-FAIRING-SET", []),
        ], ["Dorsal-fin root fairing home (053 vs 055): ruling pending."]),
        ("050", "Tailcone-External-Access-Panels", [
            ("000", "SET-ACCESS-PANELS-TAILCONE", []),
            ("010", "PANEL-ACCESS-APM-SET", []),
            ("020", "SURROUND-PANEL-CUTOUT-SET", []),
        ], []),
    ]),
    ("500", "Fuselage-Skin-Panels-and-Doublers", [
        ("010", "Forward-Fuselage-Skin", [
            ("000", "SET-SKIN-FORWARD", []),
            ("010", "PANEL-SKIN-CROWN-FWD", []),
            ("020", "PANEL-SKIN-SIDE-FWD", [
                ("021", "PANEL-SKIN-SIDE-FWD-LH"),
                ("022", "PANEL-SKIN-SIDE-FWD-RH"),
            ]),
            ("030", "PANEL-SKIN-BELLY-FWD", []),
            ("040", "DOUBLER-CUTOUT-SET-FWD", []),
        ], []),
        ("020", "Center-Fuselage-I-Skin", [
            ("000", "SET-SKIN-CENTER-I", []),
            ("010", "PANEL-SKIN-CROWN-CI", []),
            ("020", "PANEL-SKIN-SIDE-CI", [
                ("021", "PANEL-SKIN-SIDE-CI-LH"),
                ("022", "PANEL-SKIN-SIDE-CI-RH"),
            ]),
            ("030", "PANEL-SKIN-BELLY-CI", []),
            ("040", "PANEL-WINDOW-BELT-CI", [
                ("041", "PANEL-WINDOW-BELT-CI-LH"),
                ("042", "PANEL-WINDOW-BELT-CI-RH"),
            ]),
            ("050", "DOUBLER-CUTOUT-SET-CI", []),
        ], []),
        ("030", "Center-Fuselage-II-Skin", [
            ("000", "SET-SKIN-CENTER-II", []),
            ("010", "PANEL-SKIN-CROWN-CII", []),
            ("020", "PANEL-SKIN-SIDE-CII", [
                ("021", "PANEL-SKIN-SIDE-CII-LH"),
                ("022", "PANEL-SKIN-SIDE-CII-RH"),
            ]),
            ("030", "PANEL-SKIN-BELLY-CII", []),
            ("040", "PANEL-WINDOW-BELT-CII", [
                ("041", "PANEL-WINDOW-BELT-CII-LH"),
                ("042", "PANEL-WINDOW-BELT-CII-RH"),
            ]),
            ("050", "DOUBLER-CUTOUT-SET-CII", []),
        ], []),
        ("040", "Center-Fuselage-III-Skin", [
            ("000", "SET-SKIN-CENTER-III", []),
            ("010", "PANEL-SKIN-CROWN-CIII", []),
            ("020", "PANEL-SKIN-SIDE-CIII", [
                ("021", "PANEL-SKIN-SIDE-CIII-LH"),
                ("022", "PANEL-SKIN-SIDE-CIII-RH"),
            ]),
            ("030", "PANEL-SKIN-BELLY-CIII", []),
            ("040", "PANEL-WINDOW-BELT-CIII", [
                ("041", "PANEL-WINDOW-BELT-CIII-LH"),
                ("042", "PANEL-WINDOW-BELT-CIII-RH"),
            ]),
            ("050", "DOUBLER-CUTOUT-SET-CIII", []),
        ], []),
        ("050", "Rear-Fuselage-Skin", [
            ("000", "SET-SKIN-REAR", []),
            ("010", "PANEL-SKIN-CROWN-REAR", []),
            ("020", "PANEL-SKIN-SIDE-REAR", [
                ("021", "PANEL-SKIN-SIDE-REAR-LH"),
                ("022", "PANEL-SKIN-SIDE-REAR-RH"),
            ]),
            ("030", "PANEL-SKIN-BELLY-REAR", []),
            ("040", "DOUBLER-CUTOUT-SET-REAR", []),
        ], []),
        ("060", "Tailcone-Skin", [
            ("000", "SET-SKIN-TAILCONE", []),
            ("010", "PANEL-SKIN-TAILCONE-UPPER", []),
            ("020", "PANEL-SKIN-TAILCONE-LOWER", []),
            ("030", "DOUBLER-CUTOUT-SET-TAILCONE", []),
        ], []),
    ]),
    ("600", "Frames-Stringers-and-Longerons", [
        ("010", "Forward-Fuselage-Frames-Stringers-and-Structures", [
            ("000", "SET-FRAME-STRINGER-FWD", []),
            ("010", "FRAME-TYPICAL-FWD-SET", []),
            ("020", "STRINGER-SET-FWD", []),
            ("030", "CLIP-AND-TIE-SET-FWD", []),
        ], []),
        ("020", "Center-Fuselage-I-Frames-Stringers-and-Structures", [
            ("000", "SET-FRAME-STRINGER-CENTER-I", []),
            ("010", "FRAME-TYPICAL-CI-SET", []),
            ("020", "FRAME-WING-ATTACH-REINFORCED", [
                ("021", "FRAME-WING-ATTACH-REINFORCED-FWD"),
                ("022", "FRAME-WING-ATTACH-REINFORCED-AFT"),
            ]),
            ("030", "STRINGER-SET-CI", []),
            ("040", "CLIP-AND-TIE-SET-CI", []),
        ], []),
        ("030", "Center-Fuselage-II-Frames-Stringers-and-Structures", [
            ("000", "SET-FRAME-STRINGER-CENTER-II", []),
            ("010", "FRAME-TYPICAL-CII-SET", []),
            ("020", "STRINGER-SET-CII", []),
            ("030", "CLIP-AND-TIE-SET-CII", []),
        ], []),
        ("040", "Center-Fuselage-III-Frames-Stringers-and-Structures", [
            ("000", "SET-FRAME-STRINGER-CENTER-III", []),
            ("010", "FRAME-TYPICAL-CIII-SET", []),
            ("020", "STRINGER-SET-CIII", []),
            ("030", "CLIP-AND-TIE-SET-CIII", []),
        ], []),
        ("050", "Rear-Fuselage-Frames-Stringers-and-Structures", [
            ("000", "SET-FRAME-STRINGER-REAR", []),
            ("010", "FRAME-TYPICAL-REAR-SET", []),
            ("020", "FRAME-EMPENNAGE-REINFORCED-SET", []),
            ("030", "STRINGER-SET-REAR", []),
            ("040", "CLIP-AND-TIE-SET-REAR", []),
        ], ["Stabilizer/fin attach FITTINGS: 053-800-070."]),
        ("060", "Tailcone-Frames-Stringers-and-Structures", [
            ("000", "SET-FRAME-STRINGER-TAILCONE", []),
            ("010", "FRAME-TAILCONE-SET", []),
            ("020", "LONGERON-TAILCONE-SET", []),
            ("030", "CLIP-SET-TAILCONE", []),
        ], []),
        ("070", "Window-Formers-and-Surrounding-Structure", [
            ("000", "SET-WINDOW-FORMERS", []),
            ("010", "FORMER-CABIN-WINDOW-TYPICAL-SET", []),
            ("020", "FRAME-WINDSHIELD-MAIN-ARCH", [
                ("021", "ARCH-WINDSHIELD-UPPER"),
                ("022", "POST-WINDSHIELD-CENTER"),
            ]),
            ("030", "POST-WINDSHIELD-SIDE", [
                ("031", "POST-WINDSHIELD-SIDE-LH"),
                ("032", "POST-WINDSHIELD-SIDE-RH"),
            ]),
            ("040", "SILL-AND-CANT-RAIL-WINDSHIELD", []),
        ], ["Transparencies: ATA 056."]),
        ("080", "Door-Surrounding-Structure", [
            ("000", "SET-DOOR-SURROUND-STRUCTURE", []),
            ("010", "SURROUND-PAX-DOOR-FWD", [
                ("011", "EDGE-FRAME-PAX-DOOR-FWD-SET"),
                ("012", "HEADER-PAX-DOOR-FWD"),
            ]),
            ("020", "SURROUND-PAX-DOOR-AFT", [
                ("021", "EDGE-FRAME-PAX-DOOR-AFT-SET"),
                ("022", "HEADER-PAX-DOOR-AFT"),
            ]),
            ("030", "SURROUND-SERVICE-DOOR-SET", []),
            ("040", "SURROUND-CARGO-DOOR-SET", []),
        ], ["Door frame fittings/plates: 053-800-040/-050. Sills: 053-800-080. "
            "Door leaves: 052."]),
        ("090", "Keel-Beam-Structure", [
            ("000", "STRUCTURE-KEEL-BEAM", []),
            ("010", "SEGMENT-KEEL-FWD", []),
            ("020", "SEGMENT-KEEL-CENTER", []),
            ("030", "SEGMENT-KEEL-AFT", []),
            ("040", "SPLICE-KEEL-SET", []),
            ("050", "FITTING-KEEL-END", [
                ("051", "FITTING-KEEL-END-FWD"),
                ("052", "FITTING-KEEL-END-AFT"),
            ]),
        ], ["PROPOSED G-ATLAS EXTENSION - not in the current 053-600 register; "
            "requires taxonomy ruling. Delete this subject entry to drop it."]),
    ]),
    ("700", "Floor-and-Pressure-Deck-Structure", [
        ("010", "Fuselage-Floor-Structure-General", [
            ("000", "SET-FLOOR-STRUCTURE-GENERAL", []),
            ("010", "FITTING-FLOOR-ATTACH-STANDARD", []),
            ("020", "GRID-FLOOR-TYPICAL-ARRANGEMENT", []),
        ], []),
        ("020", "Forward-Fuselage-Floor-Structure", [
            ("000", "STRUCTURE-FLOOR-FWD", []),
            ("010", "BEAM-FLOOR-TRANSVERSE-FWD-SET", []),
            ("020", "INTERCOSTAL-FLOOR-FWD-SET", []),
            ("030", "DECK-PRESSURE-NLG-BAY", []),
            ("040", "SEAL-PRESSURE-DECK-NLG-PERIMETER", []),
        ], ["Owns the NLG bay pressure deck (Class B delta 1: pressure decks "
            "move from bulkheads to floors). NLG bay walls: 053-100-020."]),
        ("030", "Center-Fuselage-Floor-Structure", [
            ("000", "STRUCTURE-FLOOR-CENTER", []),
            ("010", "BEAM-FLOOR-TRANSVERSE-CENTER-SET", []),
            ("020", "INTERCOSTAL-FLOOR-CENTER-SET", []),
            ("030", "DECK-PRESSURE-MLG-WHEELWELL", [
                ("031", "DECK-PRESSURE-MLG-WHEELWELL-LH"),
                ("032", "DECK-PRESSURE-MLG-WHEELWELL-RH"),
            ]),
            ("040", "DECK-PRESSURE-OVER-WINGBOX", []),
            ("050", "SEAL-PRESSURE-DECK-CENTER-SET", []),
        ], ["Owns the MLG wheelwell and over-wingbox pressure decks (Class B "
            "delta 1). Wheelwell walls and sealing: 053-200-030."]),
        ("040", "Rear-Fuselage-Floor-Structure", [
            ("000", "STRUCTURE-FLOOR-REAR", []),
            ("010", "BEAM-FLOOR-TRANSVERSE-REAR-SET", []),
            ("020", "INTERCOSTAL-FLOOR-REAR-SET", []),
            ("030", "SUPPORT-FLOOR-BULK-CARGO", []),
        ], []),
        ("050", "Floor-Panels", [
            ("000", "SET-FLOOR-PANELS", []),
            ("010", "PANEL-FLOOR-PASSENGER-STANDARD", []),
            ("020", "PANEL-FLOOR-GALLEY-WET-AREA", []),
            ("030", "PANEL-FLOOR-CARGO", []),
            ("040", "PANEL-FLOOR-ACCESS-QUICK-RELEASE", []),
        ], []),
        ("060", "Seat-Tracks", [
            ("000", "SET-SEAT-TRACKS", []),
            ("010", "TRACK-SEAT-PASSENGER", [
                ("011", "TRACK-SEAT-PASSENGER-LH"),
                ("012", "TRACK-SEAT-PASSENGER-RH"),
            ]),
            ("020", "TRACK-SEAT-ATTENDANT", []),
            ("030", "FITTING-SEAT-TRACK-END-SET", []),
        ], ["Seats themselves: ATA 025."]),
    ]),
    ("800", "Pressure-Bulkheads-and-Major-Attach-Fittings", [
        ("010", "Forward-Pressure-Bulkhead", [
            ("000", "STRUCTURE-FWD-PRESSURE-BULKHEAD", []),
            ("010", "WEB-BULKHEAD-FWD", []),
            ("020", "STIFFENER-RADIAL-FWD-SET", []),
            ("030", "RING-PERIPHERAL-ATTACH-FWD", []),
            ("040", "FITTING-PENETRATION-SEALED-FWD-SET", []),
        ], ["MIGRATION: legacy eWTW-PBS-053-010-030 (CSN 530103) maps here "
            "(CSN 538001)."]),
        ("020", "Rear-Pressure-Bulkhead", [
            ("000", "STRUCTURE-REAR-PRESSURE-BULKHEAD", []),
            ("010", "DOME-BULKHEAD-REAR", []),
            ("020", "STIFFENER-MERIDIAN-REAR-SET", []),
            ("030", "RING-PERIPHERAL-ATTACH-REAR", []),
            ("040", "FITTING-PENETRATION-SEALED-REAR-SET", []),
        ], []),
        ("030", "Forward-Fuselage-Landing-Gear-Fittings", [
            ("000", "SET-NLG-FITTINGS", []),
            ("010", "FITTING-NLG-TRUNNION", [
                ("011", "FITTING-NLG-TRUNNION-LH"),
                ("012", "FITTING-NLG-TRUNNION-RH"),
            ]),
            ("020", "FITTING-NLG-DRAG-STRUT", []),
            ("030", "FITTING-NLG-LOCK-STAY", []),
        ], ["NLG bay structure: 053-100-020. Landing gear itself: ATA 032."]),
        ("040", "Passenger-and-Service-Door-Frame-Fittings-and-Plates", [
            ("000", "SET-PAX-AND-SERVICE-DOOR-FITTINGS", []),
            ("010", "FITTING-PAX-DOOR-HINGE-SET", []),
            ("020", "FITTING-PAX-DOOR-STOP-SET", []),
            ("030", "PLATE-LATCH-PAX-DOOR-SET", []),
            ("040", "FITTING-SERVICE-DOOR-SET", []),
        ], ["Door surround structure: 053-600-080. Door leaves: 052."]),
        ("050", "Cargo-and-Baggage-Door-Frame-Fittings-and-Plates", [
            ("000", "SET-CARGO-DOOR-FITTINGS", []),
            ("010", "FITTING-CARGO-DOOR-HINGE-SET", []),
            ("020", "FITTING-CARGO-DOOR-STOP-SET", []),
            ("030", "PLATE-LATCH-CARGO-DOOR-SET", []),
        ], []),
        ("060", "Fuselage-Plug-Frame-Fittings", [
            ("000", "SET-PLUG-FRAME-FITTINGS", []),
            ("010", "FITTING-PLUG-FRAME-FWD-SET", []),
            ("020", "FITTING-PLUG-FRAME-AFT-SET", []),
        ], []),
        ("070", "Rear-Fuselage-to-Stabilizer-Attach-Fittings", [
            ("000", "SET-STABILIZER-ATTACH-FITTINGS", []),
            ("010", "FITTING-THS-PIVOT", [
                ("011", "FITTING-THS-PIVOT-LH"),
                ("012", "FITTING-THS-PIVOT-RH"),
            ]),
            ("020", "FITTING-THS-ACTUATOR-SUPPORT", []),
            ("030", "FITTING-FIN-FRONT-SPAR-ATTACH", []),
            ("040", "FITTING-FIN-REAR-SPAR-ATTACH", []),
        ], ["Empennage-side structure: ATA 055. Reinforced frames: "
            "053-600-050."]),
        ("080", "Door-Sills", [
            ("000", "SET-DOOR-SILLS", []),
            ("010", "SILL-PAX-DOOR", [
                ("011", "SILL-PAX-DOOR-FWD"),
                ("012", "SILL-PAX-DOOR-AFT"),
            ]),
            ("020", "SILL-SERVICE-DOOR", []),
            ("030", "SILL-CARGO-DOOR", []),
        ], []),
    ]),
    ("900", "Energy-Carrier-Structural-Integration", [
        ("010", "Energy-Carrier-Bay-Structure", [
            ("000", "STRUCTURE-ENERGY-CARRIER-BAY", []),
            ("010", "BEAM-BAY-LONGITUDINAL", [
                ("011", "BEAM-BAY-LONGITUDINAL-LH"),
                ("012", "BEAM-BAY-LONGITUDINAL-RH"),
            ]),
            ("020", "FRAME-BAY-REINFORCED-SET", []),
            ("030", "PANEL-BAY-LINER-SET", []),
            ("040", "SEAL-BAY-PERIMETER", []),
        ], ["Battery bay per ICN-EWTW-021000010 (053-900 references confirmed "
            "correct). Energy carrier units: ATA 024 family."]),
        ("020", "Energy-Carrier-Crash-Protection-and-Containment-Interface", [
            ("000", "SET-CRASH-PROTECTION-INTERFACE", []),
            ("010", "STRUCTURE-CRASH-ABSORPTION-LOWER", []),
            ("020", "BARRIER-CONTAINMENT-INTERFACE", []),
            ("030", "FITTING-CONTAINMENT-ATTACH-SET", []),
        ], []),
        ("030", "Energy-Carrier-Mount-and-Attach-Fittings", [
            ("000", "SET-ENERGY-CARRIER-MOUNTS", []),
            ("010", "FITTING-CARRIER-MOUNT-PRIMARY", [
                ("011", "FITTING-CARRIER-MOUNT-PRIMARY-FWD"),
                ("012", "FITTING-CARRIER-MOUNT-PRIMARY-AFT"),
            ]),
            ("020", "FITTING-CARRIER-MOUNT-LATERAL-SET", []),
            ("030", "RAIL-CARRIER-INSTALLATION", []),
        ], []),
        ("040", "Electric-Energy-Maintenance-Compartment-Structure", [
            ("000", "STRUCTURE-EEM-COMPARTMENT", []),
            ("010", "FLOOR-GRID-EEM-COMPARTMENT", []),
            ("020", "RAIL-EQUIPMENT-RACK-SUPPORT-EEM", []),
            ("030", "PANEL-COMPARTMENT-PARTITION-EEM", []),
        ], []),
        ("050", "Vacated-Auxiliary-Fuel-Tank-Compartment-Footprint", [
            ("000", "SET-VACATED-AUX-FUEL-FOOTPRINT", []),
            ("010", "PROVISION-FOOTPRINT-PRESERVED-ATTACH-SET", []),
            ("020", "PANEL-FOOTPRINT-CLOSURE-SET", []),
            ("030", "PLACARD-FOOTPRINT-INERT-SET", []),
        ], ["Green-native: aux fuel tank deleted; footprint preserved inert."]),
    ]),
]

EXPECTED = {"sections": 10, "subjects": 59, "items": 263, "children": 74, "pns": 337}

# Class A migration map (deprecated x10 -> G-ATLAS x100), per coherence audit.
MIGRATION_MAP = [
    ("053-010 Forward-Fuselage-Section",
     "053-100 Nose-and-Forward-Fuselage-Structure"),
    ("053-020 Center-Fuselage-Section",
     "053-200 Center-Fuselage-Structure"),
    ("053-030 Aft-Fuselage-Section",
     "053-300 Aft-Fuselage-Structure"),
    ("053-040 Tailcone-and-APM-Bay",
     "053-400 Tailcone-and-APM-Structure"),
    ("053-050 Skin-Panels-and-Doublers",
     "053-500 Fuselage-Skin-Panels-and-Doublers"),
    ("053-060 Frames-Stringers-and-Longerons",
     "053-600 Frames-Stringers-and-Longerons"),
    ("053-070 Floor-Structure-Passenger-and-Cargo",
     "053-700 Floor-and-Pressure-Deck-Structure"),
    ("053-080 Pressure-Bulkheads",
     "053-800 Pressure-Bulkheads-and-Major-Attach-Fittings"),
    ("053-090 Keel-Beam-and-Major-Attach-Fittings",
     "DISSOLVED (keel -> 053-600-090 proposed; fittings -> 053-800; "
     "standards -> 051)"),
    ("053-100 Aerodynamic-Fairings",
     "DISSOLVED (belly/WBF -> 053-200-020; rudder-root -> 053-400-040)"),
    ("053-110 Energy-Carrier-Bay-Structural-Provisions",
     "053-900 Energy-Carrier-Structural-Integration"),
]

EXEMPLAR_MAP = ("EWTW-530101-xxx", "EWTW-531004-xxx",
                "eWTW-PBS-053-010-010 (CSN 530101) -> "
                "eWTW-PBS-053-100-040_Radome-and-Diverters-Attach-Structure "
                "(CSN 531004); item numbers and nomenclatures map 1:1")


def csn(section, subject):
    """EWTW-53SU-III: S = section hundreds+tens, U = subject tens."""
    return CHAPTER[1:] + section[:2] + subject[:2]


def title_text(hyphenated):
    return hyphenated.replace("-", " ")


class Writer:
    def __init__(self, root, dry_run=False, overwrite=False):
        self.root = root
        self.dry_run = dry_run
        self.overwrite = overwrite
        self.created = 0
        self.skipped = 0

    def write(self, relpath, content):
        path = self.root / relpath
        if path.exists() and not self.overwrite:
            self.skipped += 1
            return
        self.created += 1
        if self.dry_run:
            print(f"  [dry-run] {relpath}")
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def header(kind):
    return (f"# {kind}\n# {SCHEMA_NOTE}\n# {GEN_NOTE}\n")


def role_of(item_num, has_children, is_top):
    if is_top:
        return "top-assembly"
    if has_children:
        return "assembly"
    return "item"


def part_yaml(pn, nom, csn_code, item, role, parent, ptype):
    return (header("Part record") +
            "part:\n"
            f"  pn: \"{pn}\"\n"
            f"  nomenclature: \"{nom}\"\n"
            f"  csn: \"{csn_code}\"\n"
            f"  item: \"{item}\"\n"
            f"  type: \"{ptype}\"\n"
            f"  role: \"{role}\"\n"
            f"  parentAssembly: \"{parent}\"\n"
            "  applicability:\n"
            "    model: \"eWTW\"\n"
            "    effectivity:\n"
            "      - \"ALL\"\n"
            "  status: \"PLANNED\"\n")


def iter_parts(subject_id, csn_code, items):
    """Yield (relative_folder_path, pn, nom, item_num, role, parent, ptype)."""
    top_num, top_nom = items[0][0], items[0][1]
    top_pn = f"{MIC}-{csn_code}-{top_num}"
    top_folder = f"{top_pn}_{top_nom}"
    yield (top_folder, top_pn, top_nom, top_num, "top-assembly",
           subject_id, "assembly")
    for num, nom, children in items[1:]:
        pn = f"{MIC}-{csn_code}-{num}"
        folder = f"{top_folder}/{pn}_{nom}"
        role = "assembly" if children else "item"
        ptype = "assembly" if children else "part"
        yield (folder, pn, nom, num, role, top_pn, ptype)
        for cnum, cnom in children:
            cpn = f"{MIC}-{csn_code}-{cnum}"
            cfolder = f"{folder}/{cpn}_{cnom}"
            crole = ("variant" if cnom.endswith(("-LH", "-RH"))
                     else "constituent")
            yield (cfolder, cpn, cnom, cnum, crole, pn, "part")


def subject_readme(sec_code, sub_code, sub_title, csn_code, items, notes):
    sid = f"eWTW-PBS-{CHAPTER}-{sec_code}-{sub_code}"
    lines = [f"# {sid} - {title_text(sub_title)}", ""]
    lines.append(
        f"CSN `{csn_code}` - grammar `{MIC}-{csn_code}-III` per "
        "AMPEL360-PBS-PN-CM-001 (items x10; +1..+9 children as LH/RH "
        "variants or constituents). Folder names are SSOT; YAML mirrors. "
        f"Mirrors G-ATLAS `{CHAPTER}-{sec_code}-{sub_code}`.")
    lines += ["", "## Items", ""]
    for num, nom, children in items:
        lines.append(f"- `{MIC}-{csn_code}-{num}` {nom}")
        for cnum, cnom in children:
            lines.append(f"  - `{MIC}-{csn_code}-{cnum}` {cnom}")
    if notes:
        lines += ["", "## Notes", ""]
        for n in notes:
            lines.append(f"- {n}")
    lines += ["", GEN_NOTE, ""]
    return "\n".join(lines)


def realize(writer):
    all_pns = []
    for sec_code, sec_title, subjects in BREAKDOWN:
        sec_id = f"eWTW-PBS-{CHAPTER}-{sec_code}-000"
        sec_dir = f"{sec_id}_{sec_title}"
        # section pbs-node.yaml
        writer.write(f"{sec_dir}/pbs-node.yaml",
                     header("PBS node record (section)") +
                     "node:\n"
                     f"  id: \"{sec_id}\"\n"
                     f"  title: \"{title_text(sec_title)}\"\n"
                     "  level: \"section\"\n"
                     f"  gAtlas: \"{CHAPTER}-{sec_code}\"\n"
                     f"  csnPrefix: \"{CHAPTER[1:]}{sec_code[:2]}\"\n"
                     f"  parent: \"eWTW-PBS-{CHAPTER}-000\"\n"
                     "  status: \"PLANNED\"\n")
        # section pbs-item-register.yaml
        reg = [header("PBS item register (section) - subjects, generated"),
               "subjects:\n"]
        for sub_code, sub_title, items, notes in subjects:
            reg.append(f"  - id: \"eWTW-PBS-{CHAPTER}-{sec_code}-{sub_code}\"\n"
                       f"    csn: \"{csn(sec_code, sub_code)}\"\n"
                       f"    title: \"{title_text(sub_title)}\"\n"
                       f"    gAtlas: \"{CHAPTER}-{sec_code}-{sub_code}\"\n"
                       "    realized: true\n")
        writer.write(f"{sec_dir}/pbs-item-register.yaml", "".join(reg))
        # section README.md
        rl = [f"# {sec_id} - {title_text(sec_title)}", "",
              f"Section node mirroring G-ATLAS `{CHAPTER}-{sec_code}_"
              f"{sec_title}` 1:1 (PBS code = SSOT taxonomy code = AMM SNS "
              "code). Folder names are SSOT; YAML mirrors.", "",
              "## Subjects", ""]
        for sub_code, sub_title, items, notes in subjects:
            rl.append(f"- `{CHAPTER}-{sec_code}-{sub_code}` - "
                      f"{title_text(sub_title)} ({len(items)} items)")
        rl += ["", GEN_NOTE, ""]
        writer.write(f"{sec_dir}/README.md", "\n".join(rl))

        for sub_code, sub_title, items, notes in subjects:
            sub_id = f"eWTW-PBS-{CHAPTER}-{sec_code}-{sub_code}"
            sub_dir = f"{sec_dir}/{sub_id}_{sub_title}"
            csn_code = csn(sec_code, sub_code)
            scope = (f"{title_text(sub_title)} - G-ATLAS "
                     f"{CHAPTER}-{sec_code}-{sub_code} subject scope; "
                     "folder name is SSOT.")
            writer.write(f"{sub_dir}/pbs-item.yaml",
                         "pbs_item:\n"
                         f"  id: {sub_id}\n"
                         f"  title: {title_text(sub_title)}\n"
                         "  level: subject\n"
                         "  layer: \"STD\"\n"
                         "  owner: Q-STRUCTURES\n"
                         f"  parent: {sec_id}\n"
                         "  model: eWTW\n"
                         "  side: SSOT\n"
                         f"  scope: \"{scope}\"\n"
                         "  status: scaffold\n"
                         "  version: \"1.0\"\n")
            writer.write(f"{sub_dir}/station.yaml",
                         header("Assembly station record") +
                         "assemblyStation:\n"
                         f"  id: \"AS-{MIC}-{csn_code}\"\n"
                         f"  csn: \"{csn_code}\"\n"
                         f"  scope: \"Assembly and integration station - "
                         f"{title_text(sub_title)}\"\n"
                         "  status: \"PLANNED\"\n")
            preg = [header("Part register (subject) - ordered, generated"),
                    "parts:\n"]
            for folder, pn, nom, num, role, parent, ptype in iter_parts(
                    sub_id, csn_code, items):
                all_pns.append(pn)
                preg.append(f"  - pn: \"{pn}\"\n"
                            f"    nomenclature: \"{nom}\"\n"
                            f"    role: \"{role}\"\n"
                            f"    parentAssembly: \"{parent}\"\n")
                writer.write(f"{sub_dir}/{folder}/part.yaml",
                             part_yaml(pn, nom, csn_code, num, role,
                                       parent, ptype))
            writer.write(f"{sub_dir}/part-register.yaml", "".join(preg))
            writer.write(f"{sub_dir}/README.md",
                         subject_readme(sec_code, sub_code, sub_title,
                                        csn_code, items, notes))

    # chapter root registers (x100 grammar)
    chap_id = f"eWTW-PBS-{CHAPTER}-000"
    writer.write("pbs-node.yaml",
                 header("PBS node record (chapter)") +
                 "node:\n"
                 f"  id: \"{chap_id}\"\n"
                 "  title: \"Fuselage Wide-Tube\"\n"
                 "  level: \"chapter\"\n"
                 f"  gAtlas: \"{CHAPTER}\"\n"
                 "  ataOrigin: \"53\"\n"
                 "  config: \"WTW (Wide Tube Wing)\"\n"
                 "  grammar: \"0CC-SSS-UU0 (G-ATLAS x100 sections; "
                 "subjects x10; -000 = general)\"\n"
                 "  parent: \"eWTW-PBS-050\"\n"
                 f"  sections: {len(BREAKDOWN)}\n"
                 "  status: \"PLANNED\"\n")
    creg = [header("PBS item register (chapter) - sections, generated"),
            "sections:\n"]
    for sec_code, sec_title, subjects in BREAKDOWN:
        creg.append(f"  - id: \"eWTW-PBS-{CHAPTER}-{sec_code}-000\"\n"
                    f"    title: \"{title_text(sec_title)}\"\n"
                    f"    gAtlas: \"{CHAPTER}-{sec_code}\"\n"
                    f"    subjects: {len(subjects)}\n")
    writer.write("pbs-item-register.yaml", "".join(creg))
    return all_pns


def manifest_text():
    lines = ["# PBS-053 Chapter Breakdown - eWTW Fuselage Wide-Tube "
             "(G-ATLAS-coherent)", "",
             f"{GEN_NOTE} - grammar AMPEL360-PBS-PN-CM-001 (CSN "
             "`EWTW-53SU-III`; S = section hundreds+tens, U = subject tens; "
             "items x10; +1..+9 children).", "",
             "Sections and subjects are 1:1 with the G-ATLAS 053 register "
             "(PBS code = SSOT taxonomy code = AMM SNS code). SUPERSEDES the "
             "x10-section draft manifest (realize_PBS-053_chapter.py, v1). "
             "Standards families (splices, cutout doublers, clips, lugs) are "
             "chapter 051 scope and are not realized here; production joins "
             "are zone-general splice hardware plus assembly stations.", ""]
    for sec_code, sec_title, subjects in BREAKDOWN:
        lines.append(f"## {CHAPTER}-{sec_code}-000 {title_text(sec_title)}")
        lines.append("")
        for sub_code, sub_title, items, notes in subjects:
            csn_code = csn(sec_code, sub_code)
            lines.append(f"### {CHAPTER}-{sec_code}-{sub_code} "
                         f"{title_text(sub_title)} (csn {csn_code})")
            lines.append("")
            for num, nom, children in items:
                lines.append(f"- `{MIC}-{csn_code}-{num}` {nom}")
                for cnum, cnom in children:
                    lines.append(f"  - `{MIC}-{csn_code}-{cnum}` {cnom}")
            if notes:
                lines.append("")
                for n in notes:
                    lines.append(f"> {n}")
            lines.append("")
    lines += [GEN_NOTE, ""]
    return "\n".join(lines)


def migration_map_text():
    lines = ["# PBS-053 Migration Map - deprecated x10 -> G-ATLAS x100", "",
             f"{GEN_NOTE}", "",
             "| Deprecated x10 (PBS v1 / in-repo) | G-ATLAS (v2) |",
             "|---|---|"]
    for old, new in MIGRATION_MAP:
        lines.append(f"| {old} | {new} |")
    lines += ["",
              f"Exemplar migration: {EXEMPLAR_MAP[2]}.",
              f"PN map `{EXEMPLAR_MAP[0]} -> {EXEMPLAR_MAP[1]}`.", ""]
    return "\n".join(lines)


def stats():
    sections = len(BREAKDOWN)
    subjects = items = children = 0
    pns = set()
    for sec_code, _t, subs in BREAKDOWN:
        for sub_code, _st, its, _n in subs:
            subjects += 1
            csn_code = csn(sec_code, sub_code)
            for num, _nom, ch in its:
                items += 1
                pns.add(f"{MIC}-{csn_code}-{num}")
                for cnum, _cn in ch:
                    children += 1
                    pns.add(f"{MIC}-{csn_code}-{cnum}")
    return {"sections": sections, "subjects": subjects, "items": items,
            "children": children, "pns": len(pns)}


def main():
    ap = argparse.ArgumentParser(
        description="Realize eWTW PBS chapter 053 (G-ATLAS-coherent, v2).")
    ap.add_argument("--dry-run", action="store_true",
                    help="print planned writes, touch nothing")
    ap.add_argument("--overwrite", action="store_true",
                    help="overwrite existing generated files")
    ap.add_argument("--manifest", metavar="FILE", nargs="?",
                    const="PBS-053-BREAKDOWN.md",
                    help="write the breakdown manifest at the chapter root")
    ap.add_argument("--migration-map", action="store_true",
                    help="print the x10 -> x100 migration map and exit")
    args = ap.parse_args()

    st = stats()
    if st != EXPECTED:
        sys.exit(f"BREAKDOWN integrity check failed: {st} != {EXPECTED}")

    if args.migration_map:
        print(migration_map_text())
        return

    repo = pathlib.Path(__file__).resolve().parent
    root = repo / PBS_PATH
    if not root.is_dir() and not args.dry_run:
        sys.exit(f"Chapter root not found: {root}")

    writer = Writer(root, dry_run=args.dry_run, overwrite=args.overwrite)
    pns = realize(writer)
    assert len(pns) == len(set(pns)) == EXPECTED["pns"], "PN collision"

    if args.manifest:
        writer.write(args.manifest, manifest_text())

    mode = "dry-run" if args.dry_run else "realize"
    print(f"[{mode}] chapter {CHAPTER} @ {root}")
    print(f"  sections={st['sections']} subjects={st['subjects']} "
          f"items={st['items']} children={st['children']} "
          f"unique_pns={st['pns']}")
    print(f"  files created={writer.created} skipped-existing={writer.skipped}")


if __name__ == "__main__":
    main()
