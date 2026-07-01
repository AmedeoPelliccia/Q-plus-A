#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
realize_assembly-station_053-010-010.py
Trasforma il subject PBS  eWTW-PBS-053-010-010_Radome-and-Nose-Cone-Attach-Structure
in una STAZIONE DI ASSEMBLAGGIO secondo AMPEL360-PBS-PN-CM-001, e ci costruisce
dentro l'albero part-number (top assembly -> sub-assembly -> dettaglio).

Grammatica PN:  EWTW-<CSN>-<VAR>[-<VAR>...]
    EWTW    model identity code (MIC)
    CSN     530101  = ATA-equivalent di 053-010-010 (root conservata)
    VAR     gruppo find x10; 000 = l'assieme stesso; odd/even = LH/RH

La stazione tiene UN solo top assembly (EWTW-530101-000) + station.yaml
(handshake  realizes: 053-010-010  <->  top_assembly: EWTW-530101-000).
Sopra la stazione: codici G-ATLAS. Sotto: part number.

USO
    python3 realize_assembly-station_053-010-010.py                 # dalla root del repo Q-plus-A
    python3 realize_assembly-station_053-010-010.py /percorso/repo
"""
import os
import re
import sys
import shutil

OVERWRITE = True
CLEANUP_OLD = True

# --- identita' stazione / handshake -----------------------------------------
STATION_ID = "eWTW-PBS-053-010-010"          # id tassonomico (G-ATLAS, subject)
TAXONOMY_ID = "053-010-010"                  # tripletta G-ATLAS
MIC = "EWTW"                                 # model identity code
CSN = "530101"                               # 6-digit compact system number
ROOT = "%s-%s" % (MIC, CSN)                  # EWTW-530101 (root conservata)
OWNER = "Q-STRUCTURES"

NODE_REL = (
    "01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/"
    "01-02-01-01_MODELS/01-02-01-01-01_eWTW/"
    "01-02-01-01-01-01_SBS_System-Breakdown-Structure/"
    "01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/"
    "eWTW-PBS-000_Aircraft-Product/"
    "eWTW-PBS-050_Airframe-Structure/"
    "eWTW-PBS-053-000_Fuselage-Wide-Tube/"
    "eWTW-PBS-053-010-000_Forward-Fuselage-Section/"
    "eWTW-PBS-053-010-010_Radome-and-Nose-Cone-Attach-Structure"
)

GLYPH = {"STD": "STD", "DIAMOND": "\u25c7", "STD-G": "STD-G"}  # overlay verde

# --- albero part-number -----------------------------------------------------
# (find-chain, nomenclature canonica noun-first, parent find-chain, qty, uom,
#  layer, make_or_buy, catalog_pn, interfaces, scope)
#   find "000"          = top assembly (l'assieme stesso)
#   find "010"/"020"..  = componenti x10
#   find "011"/"012"..  = dettaglio (nidificato x10)
#   odd/even in gruppo  = handed LH/RH
PARTS = [
    ("000", "STRUCTURE, RADOME AND NOSE CONE ATTACH", None, 1, "EA",
     "STD", "make", "",
     ["034 | weather-radar antenna | ICD-053-010-010-034",
      "053-010-030 | forward pressure bulkhead | ICD-053-010-010-053-010-030",
      "024 | bonding / lightning protection | ICD-053-010-010-024",
      "030 | radome / nose de-ice | ICD-053-010-010-030"],
     "Top assembly / station general: nose radome shell mount and attach structure."),

    ("010", "STRUCTURE, RADOME ATTACH", "000", 1, "EA",
     "STD", "make", "",
     ["053-010-030 | forward pressure bulkhead | ICD-053-010-010-053-010-030"],
     "Radome attach frame ring plus backup fittings (sub-assembly)."),
    ("011", "FRAME, RADOME ATTACH RING", "010", 1, "EA",
     "STD", "make", "",
     [],
     "Circumferential attach ring the radome bolts to."),
    ("012", "FITTING, RADOME ATTACH BACKUP", "010", 8, "EA",
     "STD", "make", "",
     [],
     "Backup fittings distributing radome loads into the ring."),

    ("020", "FITTING, RADOME HINGE", "000", 2, "EA",
     "STD", "buy", "",
     [],
     "Handed hinge pair (radome opens for antenna access)."),
    ("021", "FITTING, RADOME HINGE LH", "020", 1, "EA",
     "STD", "buy", "",
     [],
     "Left-hand hinge (odd find = LH)."),
    ("022", "FITTING, RADOME HINGE RH", "020", 1, "EA",
     "STD", "buy", "",
     [],
     "Right-hand hinge (even find = RH)."),

    ("030", "FITTING, RADOME LATCH", "000", 2, "EA",
     "STD", "buy", "",
     [],
     "Quick-release latch fittings securing the radome closed."),

    ("040", "STRIP, LIGHTNING DIVERTER", "000", 6, "EA",
     "STD", "buy", "",
     ["024 | bonding / lightning protection | ICD-053-010-010-024"],
     "Diverter strips on the radome/nose; bonding owned by 024 (interface)."),

    ("050", "SEAL, RADOME PERIMETER", "000", 1, "EA",
     "STD", "buy", "",
     [],
     "Perimeter seal between radome and nose skin."),

    ("060", "BRACKET, WEATHER RADAR ANTENNA MOUNT", "000", 1, "EA",
     "STD", "make", "",
     ["034 | weather-radar antenna | ICD-053-010-010-034"],
     "Antenna mount interface bracket; antenna itself owned by 034."),
]


def write(path, text):
    if (not OVERWRITE) and os.path.exists(path):
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def pn_of(find_chain):
    """EWTW-530101-<find> (root conservata)."""
    return "%s-%s" % (ROOT, find_chain)


def slug_of(nomenclature):
    """`STRUCTURE, RADOME ATTACH` -> `STRUCTURE-RADOME-ATTACH` (noun-first, no comma)."""
    s = nomenclature.upper().replace(",", "")
    s = re.sub(r"\s+", "-", s.strip())
    return s


def folder_of(find_chain, nomenclature):
    return "%s_%s" % (pn_of(find_chain), slug_of(nomenclature))


def cleanup_station(node):
    """Rimuove lo stub subject e vecchi folder P/N malformati."""
    if not os.path.isdir(node):
        return
    for leftover in (".gitkeep",):
        p = os.path.join(node, leftover)
        if os.path.exists(p):
            os.remove(p)
    if CLEANUP_OLD:
        good = re.compile(re.escape(ROOT) + r"-")
        for entry in os.listdir(node):
            full = os.path.join(node, entry)
            if os.path.isdir(full) and entry.startswith(MIC + "-") and not good.match(entry):
                shutil.rmtree(full)


def dir_path_for(node, find_chain, by_find):
    """Percorso fisico nidificato: risale i parent fino al top assembly."""
    chain = []
    cur = find_chain
    while cur is not None:
        _, nomen, parent, _, _, _, _, _, _, _ = by_find[cur]
        chain.append(folder_of(cur, nomen))
        cur = parent
    chain.reverse()
    return os.path.join(node, *chain)


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    node = os.path.join(base, NODE_REL)
    os.makedirs(node, exist_ok=True)
    cleanup_station(node)

    by_find = {p[0]: p for p in PARTS}

    # --- part.yaml per ogni nodo dell'albero --------------------------------
    reg_rows = ""
    tree_lines = ""
    for (find, nomen, parent, qty, uom, layer, mob, catalog, ifaces, scope) in PARTS:
        pn = pn_of(find)
        idir = dir_path_for(node, find, by_find)
        os.makedirs(idir, exist_ok=True)

        parent_pn = "" if parent is None else pn_of(parent)
        realizes = TAXONOMY_ID if parent is None else ""

        iface_yaml = ""
        if ifaces:
            iface_yaml = "  interfaces:\n"
            for it in ifaces:
                node_ref, item, icd = [x.strip() for x in it.split("|")]
                iface_yaml += ("    - {node: \"%s\", item: \"%s\", icd: %s}\n"
                               % (node_ref, item, icd))
        else:
            iface_yaml = "  interfaces: []\n"

        realizes_yaml = ("  realizes: %s\n" % realizes) if realizes else ""

        part_yaml = (
            "part:\n"
            "  pn: %s\n"
            "  find: \"%s\"\n"
            "  nomenclature: \"%s\"\n"
            "  parent_pn: %s\n"
            "  qty: %d\n"
            "  uom: %s\n"
            "  layer: \"%s\"\n"
            "  make_or_buy: %s\n"
            "  effectivity: EFF-BASE\n"
            "  catalog_pn: %s\n"
            "%s"
            "%s"
            "  root: %s\n"
            "  model: eWTW\n"
            "  side: SSOT\n"
            "  owner: %s\n"
            "  scope: \"%s\"\n"
            "  status: realized\n"
            "  version: \"1.0\"\n"
            % (pn, find, nomen,
               parent_pn if parent_pn else '""',
               qty, uom, GLYPH.get(layer, layer), mob,
               catalog if catalog else '""',
               iface_yaml, realizes_yaml, ROOT, OWNER,
               scope.replace('"', "'"))
        )
        write(os.path.join(idir, "part.yaml"), part_yaml)

        depth = 0                     # profondita' = lunghezza catena parent
        cur = parent
        while cur is not None:
            cur = by_find[cur][2]
            depth += 1
        indent = "  " * depth
        tree_lines += "%s%s  %s  (x%d %s, %s)\n" % (
            indent, pn, nomen, qty, uom, mob)
        reg_rows += ("    - {pn: %s, find: \"%s\", nomenclature: \"%s\", "
                     "parent_pn: %s, qty: %d, layer: \"%s\", make_or_buy: %s}\n"
                     % (pn, find, nomen,
                        parent_pn if parent_pn else '""',
                        qty, GLYPH.get(layer, layer), mob))

    # --- station.yaml (handshake) -------------------------------------------
    station_yaml = (
        "station:\n"
        "  id: %s\n"
        "  realizes: %s\n"
        "  top_assembly: %s\n"
        "  mic: %s\n"
        "  csn: \"%s\"\n"
        "  root: %s\n"
        "  owner: %s\n"
        "  model: eWTW\n"
        "  side: SSOT\n"
        "  layer: \"deepest SSOT layer (configuration items)\"\n"
        "  convention: AMPEL360-PBS-PN-CM-001\n"
        "  parallels: AMPEL360-AMM-INFOCODE-CM-001\n"
        "  grammar: \"EWTW-<CSN>-<VAR>[-<VAR>...] (x10 find; 000 = assembly; odd/even = LH/RH)\"\n"
        "  interfaces:\n"
        "    - {node: \"034\", item: \"weather-radar antenna\", icd: ICD-053-010-010-034}\n"
        "    - {node: \"053-010-030\", item: \"forward pressure bulkhead\", icd: ICD-053-010-010-053-010-030}\n"
        "    - {node: \"024\", item: \"bonding / lightning protection\", icd: ICD-053-010-010-024}\n"
        "    - {node: \"030\", item: \"radome / nose de-ice\", icd: ICD-053-010-010-030}\n"
        "  parts: %d\n"
        "  status: realized\n"
        "  version: \"1.0\"\n"
        % (STATION_ID, TAXONOMY_ID, pn_of("000"), MIC, CSN, ROOT, OWNER, len(PARTS))
    )
    write(os.path.join(node, "station.yaml"), station_yaml)

    # --- part-register.yaml -------------------------------------------------
    reg = (
        "part_register:\n"
        "  station: %s\n"
        "  realizes: %s\n"
        "  root: %s\n"
        "  top_assembly: %s\n"
        "  model: eWTW\n"
        "  side: SSOT\n"
        "  grammar: \"EWTW-<CSN>-<VAR> (x10 find; root conserved)\"\n"
        "  parts:\n%s"
        % (STATION_ID, TAXONOMY_ID, ROOT, pn_of("000"), reg_rows)
    )
    write(os.path.join(node, "part-register.yaml"), reg)

    # --- README.md ----------------------------------------------------------
    readme = """---
station: {sid}
realizes: {tax}
top_assembly: {top}
root: {root}
mic: {mic}
csn: "{csn}"
type: assembly-station
convention: AMPEL360-PBS-PN-CM-001
parallels: AMPEL360-AMM-INFOCODE-CM-001
model: eWTW
side: SSOT
layer: "deepest SSOT layer (configuration items)"
owner: {owner}
doctrine: green-native
status: realized
version: "1.0"
---

# {sid} - Radome & Nose Cone Attach Structure (Assembly Station)

This subject is an **assembly station** (AMPEL360-PBS-PN-CM-001): the single
point where identity switches from *taxonomy code* to *part number*. Above the
station: G-ATLAS codes. Below: part numbers.

**Handshake** - `realizes: {tax}` (G-ATLAS)  <->  `top_assembly: {top}` (P/N),
recorded in [`station.yaml`](./station.yaml).

## Part-number grammar

```text
{mic}-{csn}-<VAR>[-<VAR>...]
```

- `{mic}` model identity code (MIC).
- `{csn}` compact system number = ATA-equivalent of `{tax}` - the conserved root
  `{root}`.
- `<VAR>` x10 find group: `000` the assembly itself; `010`, `020`... components;
  nest deeper by appending another x10 group. Odd/even within a group = handed
  (`021` LH, `022` RH).

## Part-number tree

```text
{tree}```

> `-000` remains "the assembly itself / general" at every level. The root
> `{root}` is conserved down the entire tree; only the notation changed at the
> boundary (`{tax}` -> `{root}-...`).

## Interfaces

The station is where cross-taxonomy interfaces (system <-> structure) are
declared - see `interfaces[]` in [`station.yaml`](./station.yaml):

| Interface | Owned by | ICD |
|---|---|---|
| Weather-radar antenna | `034` Navigation | `ICD-053-010-010-034` |
| Forward pressure bulkhead | `053-010-030` | `ICD-053-010-010-053-010-030` |
| Bonding / lightning protection | `024` | `ICD-053-010-010-024` |
| Radome / nose de-ice | `030` Ice-and-Rain-Protection | `ICD-053-010-010-030` |

## Identity vs position

Folder P/N is **positional / as-designed** (root-conserving: *where the item
sits*). A physical part reused elsewhere keeps **one** identity via `catalog_pn`
and is **referenced** where reused - no second folder. For make-once parts the
two coincide and `catalog_pn` is empty.

## Governance

SSOT-side; the part tree is the **deepest SSOT layer** (configuration items).
The AMM / SRM (PUB) reference it one-way via `ssot-ref.yaml`. Owner: {owner}.
Inherits DEGF v1.0, No-AAA, SSOT+PUB.

## References

- Convention: `AMPEL360-PBS-PN-CM-001` - Assembly Station & Part-Number Breakdown.
- Publication parallel: `AMPEL360-AMM-INFOCODE-CM-001` (effectivity <-> `infoCodeVariant`).
- Parent section: `eWTW-PBS-053-010-000` Forward Fuselage Section.

<!--
Last.MarkedDown: {sid} realized as assembly station - root {root}, top assembly {top}, {n} P/N nodes; handshake {tax} <-> {top}
.YieldedAlgorithmicMachineLearning: true
-->
""".format(sid=STATION_ID, tax=TAXONOMY_ID, top=pn_of("000"), root=ROOT,
           mic=MIC, csn=CSN, owner=OWNER, tree=tree_lines, n=len(PARTS))
    write(os.path.join(node, "README.md"), readme)

    print("OK: %s realizzato come stazione di assemblaggio - %d nodi P/N."
          % (STATION_ID, len(PARTS)))
    print("Top assembly: %s" % pn_of("000"))
    print("Path: %s" % os.path.normpath(node))


if __name__ == "__main__":
    main()
