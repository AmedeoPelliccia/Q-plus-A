#!/usr/bin/env python3
# =============================================================================
# complete_PBS-053-200.py  (1.3.1) - controlled migration pass
# Depth Pass 1 - section eWTW-PBS-053-200 (Center Fuselage): adds missing PN nodes per
# the ratified spec below, and corrects existing files in place:
#   - part.yaml      : enrich to Issue-2 schema (role/qty/uom/make_buy) - never
#                      touching pn/csn/item/parentAssembly/nomenclature values
#   - station.yaml   : Issue-2 fields (type, parts recount, interfaces[] stub,
#                      realizesNote if absent, convention bump)
#   - README.md      : derived BOM block between markers (created if absent)
#   - part-register.yaml (station) and pbs-item-register.yaml (section):
#                      rebuilt from disk (derived registers)
# Modes: --plan (default, no writes) / --apply.  Idempotent: second --apply is
# a no-op (volatile provenance dates excluded from comparison).
# Invariants: existing pn/csn/parentAssembly byte-identical; node count only grows.
# =============================================================================
import argparse, re, sys, datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml required: pip install pyyaml --break-system-packages"); sys.exit(2)

TODAY = datetime.date.today().isoformat()
PROV  = f"# Amended {TODAY} - complete_PBS-053-200.py (1.3.1)"
GEN   = f"# Generated {TODAY} - complete_PBS-053-200.py (1.3.1)"

# ---------------------------------------------------------------- target spec
# (station csn, station folder, [(item, parent_item|None, nomenclature, role, qty, uom, mb)])
SPEC = {
 "532001": ("eWTW-PBS-053-200-010_Center-Fuselage-Zone-General", [
   ("000", None,  "STRUCTURE-CENTER-FUSELAGE-ZONE",         "assembly",   1,"EA","make"),
   ("010", "000", "SPLICE-RING-CENTER-TO-AFT-JOIN",         "set",        1,"SET","make"),
   ("011", "010", "SPLICE-RING-SEGMENT-UPPER",              "constituent",1,"EA","make"),
   ("012", "010", "SPLICE-RING-SEGMENT-LOWER",              "constituent",1,"EA","make"),
   ("013", "010", "SPLICE-RING-SEGMENT-SIDE-LH",            "constituent",1,"EA","make"),
   ("014", "010", "SPLICE-RING-SEGMENT-SIDE-RH",            "constituent",1,"EA","make"),
   ("020", "000", "FITTING-JOIN-INDEXING",                  "set",        1,"SET","make"),
   ("021", "020", "PIN-INDEXING-JOIN",                      "leaf",       8,"EA","buy"),
   ("030", "000", "SHIM-SET-CONTROLLED-JOIN",               "set",        1,"SET","buy"),
   ("031", "030", "SHIM-PEELABLE-CONTROLLED",               "leaf",       1,"AR","buy"),
   ("040", "000", "PROVISION-NDT-ACCESS-JOIN-SET",          "set",        1,"SET","make"),
   ("041", "040", "PLUG-INSPECTION-JOIN",                   "leaf",      12,"EA","buy"),
 ]),
 "532002": ("eWTW-PBS-053-200-020_Wing-to-Fuselage-Fairing", [
   ("000", None,  "STRUCTURE-WING-TO-FUSELAGE-FAIRING",     "assembly",   1,"EA","make"),
   ("010", "000", "PANEL-FAIRING-FWD",                      "set",        1,"SET","make"),
   ("011", "010", "PANEL-FAIRING-FWD-LH",                   "constituent",1,"EA","make"),
   ("012", "010", "PANEL-FAIRING-FWD-RH",                   "constituent",1,"EA","make"),
   ("020", "000", "PANEL-FAIRING-CENTER",                   "set",        1,"SET","make"),
   ("021", "020", "PANEL-FAIRING-CENTER-LH",                "constituent",1,"EA","make"),
   ("022", "020", "PANEL-FAIRING-CENTER-RH",                "constituent",1,"EA","make"),
   ("030", "000", "PANEL-FAIRING-AFT",                      "set",        1,"SET","make"),
   ("031", "030", "PANEL-FAIRING-AFT-LH",                   "constituent",1,"EA","make"),
   ("032", "030", "PANEL-FAIRING-AFT-RH",                   "constituent",1,"EA","make"),
   ("040", "000", "FRAME-FAIRING-SUBSTRUCTURE-SET",         "set",        1,"SET","make"),
   ("041", "040", "FRAME-FAIRING-STANDARD",                 "leaf",       8,"EA","make"),
   ("050", "000", "RAIL-PACK-MOUNT",                        "set",        1,"SET","make"),
   ("051", "050", "RAIL-PACK-MOUNT-LH",                     "constituent",1,"EA","make"),
   ("052", "050", "RAIL-PACK-MOUNT-RH",                     "constituent",1,"EA","make"),
   ("053", "050", "FITTING-RAIL-ATTACH",                    "leaf",       8,"EA","make"),
   ("060", "000", "SEAL-FAIRING-PERIPHERAL",                "leaf",       1,"AR","buy"),
   ("070", "000", "DRAIN-AND-VENT-FAIRING-SET",             "set",        1,"SET","make"),
   ("071", "070", "GRILLE-VENT-FAIRING",                    "leaf",       4,"EA","buy"),
   ("072", "070", "PATH-DRAIN-FAIRING",                     "leaf",       6,"EA","make"),
 ]),
 "532003": ("eWTW-PBS-053-200-030_Main-Landing-Gear-Wheelwell-and-Sealing", [
   ("000", None,  "STRUCTURE-MLG-WHEELWELL",                "assembly",   1,"EA","make"),
   ("010", "000", "WALL-WHEELWELL-SIDE",                    "set",        1,"SET","make"),
   ("011", "010", "WALL-WHEELWELL-SIDE-LH",                 "constituent",1,"EA","make"),
   ("012", "010", "WALL-WHEELWELL-SIDE-RH",                 "constituent",1,"EA","make"),
   ("020", "000", "BULKHEAD-WHEELWELL-FWD",                 "set",        1,"SET","make"),
   ("021", "020", "WEB-BULKHEAD-FWD-REINFORCED",            "leaf",       1,"EA","make"),
   ("030", "000", "BULKHEAD-WHEELWELL-AFT",                 "set",        1,"SET","make"),
   ("031", "030", "WEB-BULKHEAD-AFT-REINFORCED",            "leaf",       1,"EA","make"),
   ("040", "000", "SEAL-WHEELWELL-PERIMETER",               "leaf",       1,"AR","make"),
   ("050", "000", "BEAM-MLG-DOOR-HINGE-SUPPORT",            "set",        1,"SET","make"),
   ("051", "050", "FITTING-DOOR-HINGE",                     "leaf",       4,"EA","make"),
   ("052", "050", "FITTING-DOOR-ACTUATOR-SUPPORT",          "leaf",       2,"EA","make"),
   ("060", "000", "DRAIN-WHEELWELL-SET",                    "set",        1,"SET","make"),
   ("061", "060", "PATH-DRAIN-WHEELWELL",                   "leaf",       4,"EA","make"),
 ]),
 "532004": ("eWTW-PBS-053-200-040_Antenna-Provisions-and-Reinforcements", [
   ("000", None,  "SET-ANTENNA-PROVISIONS",                 "assembly",   1,"EA","make"),
   ("010", "000", "DOUBLER-ANTENNA-CROWN-SET",              "set",        1,"SET","make"),
   ("011", "010", "DOUBLER-CROWN-LARGE",                    "leaf",       3,"EA","make"),
   ("012", "010", "DOUBLER-CROWN-SMALL",                    "leaf",       5,"EA","make"),
   ("020", "000", "PROVISION-ANTENNA-MOUNT-SET",            "set",        1,"SET","make"),
   ("021", "020", "BOSS-ANTENNA-MOUNT",                     "leaf",       8,"EA","make"),
   ("030", "000", "PLATE-BACKING-ANTENNA-SET",              "set",        1,"SET","make"),
   ("031", "030", "PLATE-BACKING-STANDARD",                 "leaf",       8,"EA","make"),
   ("040", "000", "BONDING-ANTENNA-PROVISION-SET",          "set",        1,"SET","make"),
   ("041", "040", "BOSS-BONDING-ANTENNA",                   "leaf",       8,"EA","make"),
 ]),
 "532005": ("eWTW-PBS-053-200-050_Middle-Avionics-Compartment-Structure", [
   ("000", None,  "STRUCTURE-MID-AVIONICS-COMPARTMENT",     "assembly",   1,"EA","make"),
   ("010", "000", "FLOOR-GRID-COMPARTMENT",                 "set",        1,"SET","make"),
   ("011", "010", "BEAM-LATERAL-SET",                       "leaf",       1,"SET","make"),
   ("012", "010", "INTERCOSTAL-SET",                        "leaf",       1,"SET","make"),
   ("020", "000", "RAIL-EQUIPMENT-RACK-SUPPORT",            "set",        1,"SET","make"),
   ("021", "020", "RAIL-RACK-STANDARD",                     "leaf",       6,"EA","make"),
   ("030", "000", "PANEL-COMPARTMENT-PARTITION",            "set",        1,"SET","make"),
   ("031", "030", "PANEL-PARTITION-ACCESS-REMOVABLE",       "leaf",       1,"EA","make"),
   ("040", "000", "SUPPORT-VENTILATION-DUCT-PROVISION",     "set",        1,"SET","make"),
   ("041", "040", "BRACKET-DUCT-SUPPORT",                   "leaf",       8,"EA","make"),
   ("050", "000", "PROVISION-GROUNDING-EE-SET",             "set",        1,"SET","make"),
   ("051", "050", "BOSS-GROUNDING-EQUIPMENT-PROVISION",     "leaf",       6,"EA","make"),
   ("060", "000", "CABLE-TRAY-STRUCTURAL-SUPPORT-SET",      "set",        1,"SET","make"),
   ("061", "060", "BRACKET-CABLE-TRAY-SUPPORT",             "leaf",      10,"EA","make"),
 ]),
 "532006": ("eWTW-PBS-053-200-060_Center-Fuselage-External-Access-and-Service-Doors", [
   ("000", None,  "SET-ACCESS-AND-SERVICE-DOORS-CENTER",    "assembly",   1,"EA","make"),
   ("010", "000", "PANEL-ACCESS-BELLY-SET",                 "set",        1,"SET","make"),
   ("011", "010", "PANEL-BELLY-MAIN",                       "leaf",       2,"EA","make"),
   ("012", "010", "PANEL-BELLY-SECONDARY",                  "leaf",       2,"EA","make"),
   ("020", "000", "SURROUND-SERVICE-DOOR-SMALL-SET",        "set",        1,"SET","make"),
   ("021", "020", "FRAME-SURROUND-SERVICE-DOOR",            "leaf",       4,"EA","make"),
   ("022", "020", "SILL-SERVICE-DOOR-SMALL",                "leaf",       4,"EA","make"),
   ("030", "000", "PANEL-ACCESS-FAIRING-SET",               "set",        1,"SET","make"),
   ("031", "030", "PANEL-ACCESS-FAIRING",                   "leaf",       6,"EA","make"),
   ("040", "000", "STANDARD-PANEL-HARDWARE-INSTALLATION",   "installation",1,"SET","make",
     [("EWTW-530003-011",16,"EA"),("EWTW-530003-021",8,"EA"),("EWTW-530003-031",1,"AR")]),
   ("050", "000", "STANDARD-PANEL-INSTALLATION",            "installation",1,"SET","make",
     [("EWTW-530003-041",4,"EA"),("EWTW-530003-042",6,"EA")]),
 ]),
}

REALIZES = {"532001":"053-200-100","532002":"053-200-200","532003":"053-200-300",
            "532004":"053-200-400","532005":"053-200-500","532006":"053-200-600"}
BOUNDARY = {
 "532001": "Zone-general structure of the center fuselage: the center-to-aft production join (four splice-ring segments, indexing, controlled shimming) and zone NDT provisions. Wing-to-body attach majors are not fuselage items on this class: the joint is expressed at the wing chapter interface, never as duplicate PNs.",
 "532002": "Wing-to-fuselage fairing structure: panels (LH/RH), substructure frames, pack-mount rails and peripheral aerodynamic seal (owned here as structure). Energy-carrier pack content and HV remain 053-900 / ATA 024; fairing venting and drainage owned here.",
 "532003": "MLG wheelwell structure and sealing lands. The gear system, retraction, doors mechanisms and functional door seals remain ATA 032; MLG trunnion support is wing structure (ATA 057); the keel interface is expressed toward eWTW-PBS-053-600-090 (taxonomy home 053-600-900 pending ratification).",
 "532004": "Antenna structural provisions: crown doublers, mount bosses, backing plates, bonding provisions. Antennas, radios and their functions remain ATA 023/034.",
 "532005": "Middle avionics compartment structure: floor grid, rack rails, partitions, duct and tray structural brackets, structure-side grounding. Equipment remains ATA 024/025/040; cooling remains ATA 021.",
 "532006": "Center external access and service-door surrounds: zone-unique belly and fairing panels are local PNs; standard panels and hardware are catalog identities from 053-000-030, carried as references with quantities (CM-001 C1.2).",
}

MIGRATION_LOCKED = set()        # no migration acts in this section

SEEDS = {
 "532003": [
  {"icd":"ICD-EWTW-532003-032","space":"taxonomy","counterpart":"032",
   "item":"MLG system, retraction, doors mechanisms and functional door seals",
   "carriedBy":["EWTW-532003-051","EWTW-532003-052"]},
  {"icd":"ICD-EWTW-532003-057","space":"taxonomy","counterpart":"057",
   "item":"MLG trunnion support at wing rear spar - wheelwell receives, wing owns",
   "carriedBy":["EWTW-532003-011","EWTW-532003-012"]},
  {"icd":"ICD-EWTW-532003-536009","space":"pbs-local","counterpart":"eWTW-PBS-053-600-090",
   "counterpartCsn":"536009",
   "item":"keel-beam interface (taxonomy home 053-600-900 pending ratification)",
   "carriedBy":["EWTW-532003-021","EWTW-532003-031"]},
 ],
}

SCRIPT_NAME = "complete_PBS-053-200.py"
_src = Path(__file__).read_text(encoding="utf-8", errors="ignore")
assert SCRIPT_NAME.replace(".", "\\.") in _src, "SELF-CHECK: norm() pattern does not name this script"
assert 'else "# eWTW-PBS-053-200-000' in _src, "SELF-CHECK: section README fallback belongs to another section"
for _foreign in ("053-000-000_General","053-100-000_Nose","053-200-000_Center","053-300-000_Aft"):
    if not _foreign.startswith("053-200-000"):
        assert _foreign not in _src.split("SCRIPT_NAME =")[0], f"SELF-CHECK: foreign section folder in engine constants: {_foreign}"

def load_strict(p):
    try: return yaml.safe_load(p.read_text()) or {}
    except Exception as e: raise RuntimeError(f"YAML-INVALID {p}: {e}")

LOCKED_EXPECTED_PNS = {}

def slug(nom):  # nomenclature -> FOLDER-SLUG
    s = re.sub(r"[^A-Za-z0-9]+", "-", nom.upper()).strip("-")
    return re.sub(r"-{2,}", "-", s)

def load(p):
    try: return yaml.safe_load(p.read_text()) or {}
    except Exception: return {}

def dump_part(d, header):
    body = yaml.safe_dump({"part": d}, sort_keys=False, allow_unicode=True)
    return header + "\n" + body

def norm(s):  # comparison ignoring provenance lines entirely
    s = re.sub(r"^# (Generated|Amended) .*$\n?", "", s, flags=re.M)
    s = re.sub(r"^_Generated \d{4}-\d{2}-\d{2} - complete_PBS-053-200\.py \([^)]+\)_\n?", "", s, flags=re.M)
    return re.sub(r"\n{2,}", "\n", s).strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="repo root or section parent")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    root = Path(a.root)
    hits = list(root.rglob("eWTW-PBS-053-200-000_Center-Fuselage-Structure"))
    if not hits:
        print("section folder eWTW-PBS-053-200-000_Center-Fuselage-Structure not found under", root); sys.exit(1)
    sec = hits[0]
    W = a.apply
    st = dict(added=0, part_fix=0, sta_fix=0, readme=0, reg=0, skipped=0)
    section_rows = []
    # ================= PASS A - global preflight (read-only) =================
    fatal, yaml_fatal, unmanaged_all = [], [], []
    for f in sec.rglob("*.yaml"):
        try: yaml.safe_load(f.read_text())
        except Exception as e: yaml_fatal.append(f"YAML-INVALID {f}: {e}")
    for csn, (sta_folder, rows) in SPEC.items():
        sta = sec / sta_folder
        if not sta.is_dir():
            fatal.append(f"MISSING-STATION {sta_folder}"); continue
        if csn in MIGRATION_LOCKED:
            exp = LOCKED_EXPECTED_PNS.get(csn, set())
            disk = {d.name.split("_")[0] for d in sta.rglob("EWTW-*") if d.is_dir()}
            for d in sorted(exp - disk): fatal.append(f"LOCKED-SIGNATURE-DRIFT {csn}: missing {d}")
            for d in sorted(disk - exp): fatal.append(f"LOCKED-SIGNATURE-DRIFT {csn}: unexpected {d}")
            sy = sta / "station.yaml"
            if not sy.exists():
                fatal.append(f"LOCKED-STATION-YAML-MISSING {sta_folder}")
            else:
                try: sd = (yaml.safe_load(sy.read_text()) or {}).get("station", {})
                except Exception as e: sd = {}; fatal.append(f"LOCKED-STATION-YAML-INVALID {sta_folder}: {e}")
                if sd:
                    lc = sta_folder.split("_")[0].replace("eWTW-PBS-","")
                    for k, exp in (("realizes", REALIZES[csn]), ("csn", csn),
                                   ("localCode", lc), ("id", sta_folder.split("_")[0])):
                        if str(sd.get(k, "")) != str(exp):
                            fatal.append(f"LOCKED-STATION-DRIFT {sta_folder}: {k} disk={sd.get(k)!r} expected={exp!r}")
                    if "interfaces" in sd and not isinstance(sd["interfaces"], list):
                        fatal.append(f"INTERFACES-NOT-LIST {sta_folder}")
            continue
        spec_pns = {f"EWTW-{csn}-{r[0]}" for r in rows}
        disk_pns = {d.name.split("_")[0] for d in sta.rglob("EWTW-*") if d.is_dir()}
        for u in sorted(disk_pns - spec_pns):
            unmanaged_all.append((csn, u)); fatal.append(f"UNMANAGED-PN {csn}: {u}")
        # expected-path map + drift/duplicate + identity (read-only)
        vdir = {}
        for it, par, nom, role, qty, uom, mb, *refs in rows:
            pnv = f"EWTW-{csn}-{it}"
            parent = sta if par is None else vdir[par]
            hits = [d for d in sta.rglob(f"{pnv}_*") if d.is_dir()]
            if len(hits) > 1:
                fatal.append(f"PN-DUPLICATE {pnv}: " + " | ".join(str(h) for h in hits))
                vdir[it] = hits[0]; continue
            if len(hits) == 1:
                if hits[0].parent.resolve() != Path(parent).resolve():
                    fatal.append(f"PN-PATH-DRIFT {pnv}: disk={hits[0].parent} expected={parent}")
                vdir[it] = hits[0]
                py = hits[0] / "part.yaml"
                if py.exists():
                    try: cur = (yaml.safe_load(py.read_text()) or {}).get("part", {})
                    except Exception: cur = None
                    if cur is not None:
                        expmap = {"pn": pnv, "csn": csn, "item": it}
                        if par is not None: expmap["parentAssembly"] = f"EWTW-{csn}-{par}"
                        for k, v in expmap.items():
                            if str(cur.get(k, v)) != str(v):
                                fatal.append(f"IDENTITY-MISMATCH {py}: {k} disk={cur.get(k)!r} spec={v!r}")
            else:
                vdir[it] = Path(parent) / f"{pnv}_{slug(nom)}"
            for r0, _q, _u in (refs[0] if refs else []):
                if not list(root.rglob(f"{r0}_*")):
                    fatal.append(f"REFERENCE-DANGLING {csn}: {r0}")
        sy = sta / "station.yaml"
        if not sy.exists():
            fatal.append(f"STATION-YAML-MISSING {sta_folder}")
        else:
            try: sd = (yaml.safe_load(sy.read_text()) or {}).get("station", {})
            except Exception as e: sd = {}; fatal.append(f"STATION-YAML-INVALID {sta_folder}: {e}")
            if sd:
                lc = sta_folder.split("_")[0].replace("eWTW-PBS-", "")
                for k, expv in (("id", sta_folder.split("_")[0]), ("localCode", lc), ("csn", csn)):
                    if str(sd.get(k, "")) != str(expv):
                        fatal.append(f"STATION-IDENTITY-MISMATCH {sta_folder}: {k} disk={sd.get(k)!r} expected={expv!r}")
                if "interfaces" in sd and not isinstance(sd["interfaces"], list):
                    fatal.append(f"INTERFACES-NOT-LIST {sta_folder}")
    tax_root = next((c for c in root.rglob("000-099_S-ATLAS") if c.is_dir()), None)
    for csn_s, seeds in SEEDS.items():
        for e in seeds:
            if e.get("space") == "pbs-local":
                cp = e.get("counterpart", "")
                hits = [d for d in root.rglob(f"{cp}_*") if d.is_dir()]
                if not hits:
                    fatal.append(f"PBS-COUNTERPART-DANGLING {csn_s}: {cp}"); continue
                sy2 = hits[0] / "station.yaml"
                if e.get("counterpartCsn"):
                    if not sy2.exists():
                        fatal.append(f"COUNTERPART-STATION-YAML-MISSING {csn_s}: {cp}")
                    else:
                        try:
                            dcs = str((yaml.safe_load(sy2.read_text()) or {}).get("station", {}).get("csn", ""))
                        except Exception as ex:
                            fatal.append(f"COUNTERPART-STATION-YAML-INVALID {csn_s}: {cp}: {ex}")
                        else:
                            if dcs != str(e["counterpartCsn"]):
                                fatal.append(f"COUNTERPART-CSN-MISMATCH {csn_s}: {cp} disk={dcs!r} seed={e['counterpartCsn']!r}")
            tr = e.get("taxonomyRef")
            if tr:
                if tax_root is None:
                    fatal.append(f"TAXONOMY-ROOT-MISSING {csn_s}: cannot validate {tr}")
                elif not list(tax_root.rglob(f"{tr}_*")):
                    fatal.append(f"SEED-TAXONOMYREF-DANGLING {csn_s}: {tr}")
    for m in yaml_fatal + fatal: print("PREFLIGHT:", m)
    if yaml_fatal:
        print(f"ABORT(4): {len(yaml_fatal)} invalid YAML - no migration plan can be safely evaluated"); return 4
    if fatal:
        print(f"ABORT(3): {len(fatal)} preflight fatal(s) - no migration plan can be safely evaluated"); return 3
    print("preflight: yaml-fatal=0  fatal=0  (PASS)")
    # ================= PASS B - mutate =================

    for csn, (sta_folder, rows) in SPEC.items():
        sta = sec / sta_folder
        if csn in MIGRATION_LOCKED:
            if not (sta / "station.yaml").exists():
                print(f"!! locked station missing on disk: {sta_folder}")
            section_rows.append({"station": sta_folder.split("_")[0], "csn": csn,
                                 "parts": len(list(sta.rglob("part.yaml"))),
                                 "status": "migration-controlled"})
            continue
        if not sta.is_dir():
            print(f"!! station folder missing: {sta_folder} - skipped"); continue
        pn_of = {it: f"EWTW-{csn}-{it}" for it,*_ in rows}
        nom_rt = {r[0]: r[2] for r in rows}
        dir_of = {}
        # resolve folder path for each item (nested under its parent chain)
        for it, par, nom, role, qty, uom, mb, *refs in rows:
            parent_dir = sta if par is None else dir_of[par]
            # find existing folder for this PN regardless of slug
            existing = [d for d in parent_dir.iterdir() if d.is_dir() and d.name.startswith(pn_of[it]+"_")] if parent_dir.exists() else []
            d = existing[0] if existing else parent_dir / f"{pn_of[it]}_{slug(nom)}"
            dir_of[it] = d
            py = d / "part.yaml"
            target = {
                "pn": pn_of[it], "nomenclature": nom, "csn": csn, "item": it,
                "type": ("assembly" if role in ("assembly","set","installation") else "part"),
                "role": role, "qty": qty, "uom": uom,
                "make_buy": mb,
                "parentAssembly": (pn_of[par] if par else None),
                "applicability": {"model": "eWTW", "effectivity": ["ALL"]},
                "status": "PLANNED",
                "convention": "AMPEL360-PBS-PN-CM-001 (Issue 2)",
            }
            if refs: target["references"] = [{"pn": r0, "qty": r1, "uom": r2} for r0,r1,r2 in refs[0]]
            if par is None: target.pop("parentAssembly")
            if py.exists():
                cur = load_strict(py).get("part", {})
                # invariants: never change identity values
                for k in ("pn","csn","item","parentAssembly"):
                    if k not in target: continue
                    if str(cur.get(k, target[k])) != str(target[k]):
                        print(f"!! identity mismatch {py}: {k} disk={cur.get(k)} spec={target[k]} - left untouched")
                        st["skipped"] += 1; break
                else:
                    merged = dict(cur)
                    nom_rt[it] = cur.get("nomenclature", nom_rt[it])
                    for k in ("type","role","qty","uom","make_buy","convention"):
                        merged[k] = target[k]
                    if refs: merged["references"] = target["references"]
                    merged.setdefault("applicability", target["applicability"])
                    merged.setdefault("status", "PLANNED")
                    if par and not merged.get("parentAssembly"):
                        merged["parentAssembly"] = pn_of[par]
                    prev = py.read_text().splitlines()
                    header_lines = [l for l in prev if l.startswith(("# Generated","# Amended"))]
                    if not any("complete_PBS-053-200.py" in l and l.startswith("# Amended") for l in header_lines):
                        header_lines.append(PROV)
                    header = "\n".join(header_lines) if header_lines else PROV
                    out = dump_part(merged, header)
                    if norm(out) != norm(py.read_text()):
                        st["part_fix"] += 1
                        if W: py.write_text(out)
            else:
                st["added"] += 1
                if W:
                    d.mkdir(parents=True, exist_ok=True)
                    py.write_text(dump_part(target, GEN))
        # ---- station.yaml correction
        sy = sta / "station.yaml"
        if sy.exists():
            doc = load(sy); s = doc.get("station", doc) or {}
            s.setdefault("type","assembly-station")
            s.setdefault("parallels","AMPEL360-AMM-INFOCODE-CM-001")
            s["realizes"] = REALIZES[csn]
            s.setdefault("realizesNote","current S-ATLAS address; PBS-local code conserved per CM-001 A1.1")
            s["convention"] = "AMPEL360-PBS-PN-CM-001 (Issue 2)"
            s["parts"] = len(rows)
            s.setdefault("interfaces", [])
            for e in SEEDS.get(csn, []):
                have = {str(i.get("icd")) for i in s["interfaces"] if isinstance(i, dict)}
                if e["icd"] not in have: s["interfaces"].append(e)
            s["version"] = "1.2"
            hdr = [l for l in sy.read_text().splitlines() if l.startswith(("# Generated","# Amended"))]
            if not any("complete_PBS-053-200.py" in l for l in hdr):
                hdr.append(PROV)
            out = "\n".join(hdr) + "\n" + yaml.safe_dump({"station": s}, sort_keys=False)
            if norm(out) != norm(sy.read_text()):
                st["sta_fix"] += 1
                if W: sy.write_text(out)
        # ---- README derived BOM block
        rd = sta / "README.md"
        lines = [f"| `{pn_of[it]}` | {nom_rt[it]} | {role} | {qty} | {uom} | {mb} | PLANNED |"
                 for it,_,nom,role,qty,uom,mb,*_r in rows]
        block = ("<!-- BOM:BEGIN (derived - regenerated by complete_PBS-053-200.py; do not edit) -->\n"
                 f"## Bill of material (derived view)\n\n_{GEN[2:]}_\n\n"
                 "| PN | Nomenclature | Role | Qty | UoM | Make/Buy | Status |\n|---|---|---|---:|---|---|---|\n"
                 + "\n".join(lines)
                 + f"\n\n**Ownership boundary** - {BOUNDARY[csn]}\n"
                 + "\n> Lifecycle note: station `status` describes existence of the PBS realization; part `PLANNED` describes maturity. The two are intentionally not collapsed.\n"
                 + "<!-- BOM:END -->")
        txt = rd.read_text() if rd.exists() else f"# {sta_folder}\n"
        if "<!-- BOM:BEGIN" in txt:
            new = re.sub(r"<!-- BOM:BEGIN.*?BOM:END -->", block, txt, flags=re.S)
        else:
            new = txt.rstrip() + "\n\n" + block + "\n"
        if norm(new) != norm(txt):
            st["readme"] += 1
            if W: rd.write_text(new)
        # ---- station part-register.yaml (derived)
        pr = sta / "part-register.yaml"
        reg = {"register": {"station": f"eWTW-PBS-053-200-{sta_folder.split('_')[0][-3:]}",
                            "csn": csn, "derived": True,
                            "parts": [{"pn": pn_of[it], "nomenclature": nom_rt[it], "role": role,
                                       "qty": qty, "uom": uom, "make_buy": mb, "status": "PLANNED",
                                        **({"references": [{"pn": a, "qty": b, "uom": c} for a,b,c in _r[0]]} if _r else {})}
                                      for it,_,nom,role,qty,uom,mb,*_r in rows]}}
        out = GEN + "\n" + yaml.safe_dump(reg, sort_keys=False, allow_unicode=True)
        if not pr.exists() or norm(out) != norm(pr.read_text()):
            st["reg"] += 1
            if W: pr.write_text(out)
        section_rows.append({"station": sta_folder.split("_")[0], "csn": csn,
                             "parts": len(rows), "status": "PLANNED"})

    # ---- section README derived block
    sec_rd = sec / "README.md"
    tl = {}; pn_tot = {}
    for csn, (sta_folder, rows) in SPEC.items():
        sta = sec / sta_folder
        if csn in MIGRATION_LOCKED or not rows:
            top = next((d for d in sta.iterdir() if d.is_dir() and d.name.startswith("EWTW-")), None)
            tl[csn] = (1 + sum(1 for d in top.iterdir() if d.is_dir() and d.name.startswith("EWTW-"))) if top else 0
            pn_tot[csn] = len(list(sta.rglob("part.yaml")))
        else:
            tl[csn] = sum(1 for r in rows if r[1] in (None, "000"))
            pn_tot[csn] = len(rows)
    lines2 = [f"| `{SPEC[c][0].split('_')[0]}` | {tl[c]} | {pn_tot[c]}{' (migration-locked)' if c in MIGRATION_LOCKED else ''} |"
              for c in sorted(SPEC)]
    blk = ("<!-- SECTION:BEGIN (derived - regenerated by complete_PBS-053-200.py; do not edit) -->\n"
           "## Section realization (derived view)\n\n"
           "| PBS station | Top-level items | PN nodes |\n|---|---:|---:|\n"
           + "\n".join(lines2)
           + f"\n| **Total** | **{sum(tl.values())}** | **{sum(pn_tot.values())}** |\n"
           + f"\n> Plus {len({x[0] for rows in [v[1] for v in SPEC.values()] for r in rows if len(r)>7 for x in r[7]})} distinct catalog-PN identities referenced from `EWTW-530003`, representing {sum(x[1] for rows in [v[1] for v in SPEC.values()] for r in rows if len(r)>7 for x in r[7] if x[2]=='EA')} installation occurrences (EA) plus {sum(1 for rows in [v[1] for v in SPEC.values()] for r in rows if len(r)>7 for x in r[7] if x[2]=='AR')} as-required allocation (CM-001 C1.2).\n"
           + "<!-- SECTION:END -->")
    t0 = sec_rd.read_text() if sec_rd.exists() else "# eWTW-PBS-053-200-000 - Center Fuselage Structure\n"
    t1 = re.sub(r"<!-- SECTION:BEGIN.*?SECTION:END -->", blk, t0, flags=re.S) if "<!-- SECTION:BEGIN" in t0 else t0.rstrip() + "\n\n" + blk + "\n"
    if norm(t1) != norm(t0):
        st["readme"] += 1
        if W: sec_rd.write_text(t1)

    # ---- section register (derived)
    sreg = sec / "pbs-item-register.yaml"
    out = GEN + "\n" + yaml.safe_dump({"register": {"section": "eWTW-PBS-053-200",
        "derived": True, "stations": section_rows}}, sort_keys=False)
    if not sreg.exists() or norm(out) != norm(sreg.read_text()):
        st["reg"] += 1
        if W: sreg.write_text(out)

    mode = "APPLIED" if W else "PLAN"
    print(f"[{mode}] nodes added={st['added']}  part.yaml corrected={st['part_fix']}  "
          f"station.yaml corrected={st['sta_fix']}  READMEs={st['readme']}  registers={st['reg']}  identity-skips={st['skipped']}")
    # ---- battery
    # realizes verification (expected map + taxonomy existence when reachable)
    tax = None
    for cand in root.rglob("053-200_Center-Fuselage-Structure"):
        if "000-099_S-ATLAS" in str(cand): tax = cand; break
    for csn,(sta_folder,_) in SPEC.items():
        sy = sec / sta_folder / "station.yaml"
        if sy.exists():
            r = (load(sy).get("station") or {}).get("realizes","")
            if r != REALIZES[csn]:
                print(f"REALIZES-DRIFT {sta_folder}: disk={r!r} expected={REALIZES[csn]!r}")
            elif tax and not any(tax.glob(f"{r}_*")):
                print(f"REALIZES-DANGLING {sta_folder}: {r} not in taxonomy")
    # PN-collision: same PN folder appearing in more than one directory
    seen = {}
    coll = 0
    for d in sec.rglob("EWTW-*"):
        if d.is_dir():
            k = d.name.split("_")[0]
            if k in seen and seen[k] != d.parent:
                coll += 1; print(f"PN-COLLISION {k}: {seen[k]} vs {d.parent}")
            seen.setdefault(k, d.parent)
    bad = 0
    for f in sec.rglob("*.yaml"):
        try: yaml.safe_load(f.read_text())
        except Exception as e: bad += 1; print("YAML-INVALID", f, e)
    roll = all(r[4] == 1 for rows in [v[1] for v in SPEC.values()] for r in rows if r[3] in ("set","installation"))
    refs_all = [x[0] for rows in [v[1] for v in SPEC.values()] for r in rows if len(r) > 7 for x in r[7]]
    ref_missing = [c for c in refs_all if not list(root.rglob(f"{c}_*"))]
    if ref_missing: print("REFERENCE-DANGLING:", *ref_missing)
    contam = sum(1 for f in list(sec.rglob("part-register.yaml"))+list(sec.rglob("pbs-item-register.yaml")) if re.search(r"eWTW-PBS-053-(?!200-)\d00-\d", f.read_text()))
    print(f"battery: yaml-invalid={bad}  pn-collisions={coll}  set-qty-discipline={'OK' if roll else 'FAIL'}  "
          f"unmanaged-pn={len(unmanaged_all)}  reference-dangling={len(ref_missing)}  register-contamination={contam}  part.yaml on disk={len(list(sec.rglob('part.yaml')))}")
    return 0

if __name__ == "__main__": sys.exit(main())