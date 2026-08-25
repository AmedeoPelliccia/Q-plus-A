#!/usr/bin/env python3
# =============================================================================
# complete_PBS-053-100.py  (1.3.1) - controlled migration pass
# Depth Pass 1 - section eWTW-PBS-053-100 (Nose and Forward): adds missing PN nodes per
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
PROV  = f"# Amended {TODAY} - complete_PBS-053-100.py (1.3.1)"
GEN   = f"# Generated {TODAY} - complete_PBS-053-100.py (1.3.1)"

# ---------------------------------------------------------------- target spec
# (station csn, station folder, [(item, parent_item|None, nomenclature, role, qty, uom, mb)])
SPEC = {
 "531001": ("eWTW-PBS-053-100-010_Forward-Fuselage-Zone-General", [
   ("000", None,  "STRUCTURE-FORWARD-FUSELAGE-ZONE",        "assembly",   1,"EA","make"),
   ("010", "000", "SPLICE-RING-FWD-TO-CENTER-JOIN",         "set",        1,"SET","make"),
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
 "531002": ("eWTW-PBS-053-100-020_Nose-Landing-Gear-Bay-and-Door-Supports", [
   ("000", None,  "STRUCTURE-NLG-BAY-AND-DOOR-SUPPORTS",    "assembly",   1,"EA","make"),
   ("010", "000", "WALL-NLG-BAY-SIDE",                      "set",        1,"SET","make"),
   ("011", "010", "WALL-NLG-BAY-SIDE-LH",                   "constituent",1,"EA","make"),
   ("012", "010", "WALL-NLG-BAY-SIDE-RH",                   "constituent",1,"EA","make"),
   ("020", "000", "BULKHEAD-NLG-BAY-AFT",                   "set",        1,"SET","make"),
   ("021", "020", "WEB-BULKHEAD-AFT-REINFORCED",            "leaf",       1,"EA","make"),
   ("030", "000", "BEAM-NLG-DOOR-HINGE-SUPPORT",            "set",        1,"SET","make"),
   ("031", "030", "FITTING-DOOR-HINGE",                     "leaf",       4,"EA","make"),
   ("032", "030", "FITTING-DOOR-ACTUATOR-SUPPORT",          "leaf",       2,"EA","make"),
   ("040", "000", "FRAME-NLG-BAY-ROOF-SUPPORT",             "set",        1,"SET","make"),
   ("041", "040", "STRUT-BAY-ROOF-CROSS",                   "leaf",       3,"EA","make"),
   ("060", "000", "SEAL-AND-DRAIN-BAY-SET",                 "set",        1,"SET","make"),
   ("061", "060", "SEAL-LAND-NLG-DOOR-PERIMETER",           "leaf",       1,"EA","make"),
   ("062", "060", "DRAIN-BAY-PATH",                         "leaf",       4,"EA","make"),
 ]),
 "531003": ("eWTW-PBS-053-100-030_Forward-Avionics-Compartment-Structure", [
   ("000", None,  "STRUCTURE-FWD-AVIONICS-COMPARTMENT",     "assembly",   1,"EA","make"),
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
 "531004": ("eWTW-PBS-053-100-040_Radome-and-Diverters-Attach-Structure", []),
 "531005": ("eWTW-PBS-053-100-050_Forward-Fuselage-Direct-Vision-Window", [
   ("000", None,  "STRUCTURE-DV-WINDOW-SURROUND",           "assembly",   1,"EA","make"),
   ("010", "000", "FRAME-DV-WINDOW",                        "set",        1,"SET","make"),
   ("011", "010", "FRAME-DV-WINDOW-LH",                     "constituent",1,"EA","make"),
   ("012", "010", "FRAME-DV-WINDOW-RH",                     "constituent",1,"EA","make"),
   ("020", "000", "SILL-AND-HEADER-DV",                     "set",        1,"SET","make"),
   ("021", "020", "SILL-DV-LOWER",                          "leaf",       2,"EA","make"),
   ("022", "020", "HEADER-DV-UPPER",                        "leaf",       2,"EA","make"),
   ("030", "000", "DOUBLER-DV-SURROUND",                    "set",        1,"SET","make"),
   ("031", "030", "DOUBLER-CORNER-DV",                      "leaf",       8,"EA","make"),
   ("040", "000", "PROVISION-DRAIN-AND-SEAL-DV-SET",        "set",        1,"SET","make"),
   ("041", "040", "CHANNEL-DRAIN-DV",                       "leaf",       2,"EA","make"),
   ("042", "040", "SEAL-LAND-DV",                           "leaf",       1,"AR","make"),
 ]),
 "531006": ("eWTW-PBS-053-100-060_Forward-Fuselage-External-Access-Panels", [
   ("000", None,  "SET-ACCESS-PANELS-FWD",                  "assembly",   1,"EA","make"),
   ("010", "000", "PANEL-ACCESS-EQUIPMENT-BAY",             "set",        1,"SET","make"),
   ("011", "010", "PANEL-EE-BAY-MAIN",                      "leaf",       1,"EA","make"),
   ("020", "000", "PANEL-ACCESS-SERVICE-SET",               "installation",1,"SET","make",
     [("EWTW-530003-041",6,"EA"),("EWTW-530003-042",4,"EA")]),
   ("030", "000", "SURROUND-PANEL-CUTOUT-SET",              "set",        1,"SET","make"),
   ("031", "030", "FRAME-CUTOUT-REINFORCED",                "leaf",      10,"EA","make"),
   ("040", "000", "STANDARD-PANEL-HARDWARE-INSTALLATION",   "installation",1,"SET","make",
     [("EWTW-530003-011",24,"EA"),("EWTW-530003-021",12,"EA"),("EWTW-530003-031",1,"AR")]),
 ]),
}

REALIZES = {"531001":"053-100-100","531002":"053-100-200","531003":"053-100-300",
            "531004":"053-100-400","531005":"053-100-500","531006":"053-100-600"}
BOUNDARY = {
 "531001": "Zone-general structure of the forward fuselage: the forward-to-center production join (splice ring, indexing, controlled shimming) and zone-level NDT provisions. Zone skins/frames design basis remains with the element catalogs (053-500/-600).",
 "531002": "NLG bay primary structure and door/gear structural supports only: ATA 53 owns the structure that receives seals and mechanisms; the gear system, retraction, door mechanisms and functional door seals remain ATA 032.",
 "531003": "Forward avionics (E/E) compartment structure: floor grid, rack support rails, partitions, duct and tray structural brackets, structure-side grounding provisions. Busbars, trays, equipment and racks content remain ATA 024/025/040; compartment cooling remains ATA 021.",
 "531004": "Radome and diverter attach structure - the ratified exemplar, migration-controlled: this pass validates and never modifies identity or nomenclature.",
 "531005": "Direct-vision window surround structure: frames, sill/header, doublers, drain channels and seal lands (interface geometry). Glazing remains ATA 056; window heating remains ATA 030.",
 "531006": "Forward external access panels: zone-unique panel instances and cutout surrounds are local PNs; standard panels and hardware are catalog identities from 053-000-030, carried as references with quantities - one identity, no second folder (CM-001 Issue 2 section 6).",
}

MIGRATION_LOCKED = {"531004"}   # exemplar station: owned by the migration act - validate only

def load_strict(p):
    try: return yaml.safe_load(p.read_text()) or {}
    except Exception as e: raise RuntimeError(f"YAML-INVALID {p}: {e}")

LOCKED_EXPECTED_PNS = {"531004": {f"EWTW-531004-{i}" for i in
    ("000","010","011","012","020","021","022","030","040","050","060")}}

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
    s = re.sub(r"^_Generated \d{4}-\d{2}-\d{2} - complete_PBS-053-100\.py \([^)]+\)_\n?", "", s, flags=re.M)
    return re.sub(r"\n{2,}", "\n", s).strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="repo root or section parent")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    root = Path(a.root)
    hits = list(root.rglob("eWTW-PBS-053-100-000_Nose-and-Forward-Fuselage-Structure"))
    if not hits:
        print("section folder eWTW-PBS-053-100-000_Nose-and-Forward-Fuselage-Structure not found under", root); sys.exit(1)
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
        if sy.exists():
            sd = (yaml.safe_load(sy.read_text()) or {}).get("station", {})
            if "interfaces" in sd and not isinstance(sd["interfaces"], list):
                fatal.append(f"INTERFACES-NOT-LIST {sta_folder}")
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
                    if not any("complete_PBS-053-100.py" in l and l.startswith("# Amended") for l in header_lines):
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
        parts_on_disk = len(list(sta.rglob("part.yaml"))) + (st["added"] if False else 0)
        if sy.exists():
            doc = load(sy); s = doc.get("station", doc) or {}
            s.setdefault("type","assembly-station")
            s.setdefault("parallels","AMPEL360-AMM-INFOCODE-CM-001")
            s["realizes"] = REALIZES[csn]
            s.setdefault("realizesNote","current S-ATLAS address; PBS-local code conserved per CM-001 A1.1")
            s["convention"] = "AMPEL360-PBS-PN-CM-001 (Issue 2)"
            s["parts"] = len(list(sta.rglob("part.yaml"))) + (0 if not W else 0)
            s.setdefault("interfaces", [])
            if csn == "531002" and not any("ICD-EWTW-531002-538003" in str(i) for i in s["interfaces"]):
                s["interfaces"].append({"icd": "ICD-EWTW-531002-538003", "space": "pbs-local",
                    "counterpart": "eWTW-PBS-053-800-030", "counterpartCsn": "538003",
                    "taxonomyRef": "053-800-300",
                    "item": "NLG trunnion and drag-strut fittings - bay structure receives, 053-800-030 owns",
                    "carriedBy": ["EWTW-531002-011","EWTW-531002-012","EWTW-531002-021"]})
            s["version"] = "1.2"
            hdr = [l for l in sy.read_text().splitlines() if l.startswith(("# Generated","# Amended"))]
            if not any("complete_PBS-053-100.py" in l for l in hdr):
                hdr.append(PROV)
            out = "\n".join(hdr) + "\n" + yaml.safe_dump({"station": s}, sort_keys=False)
            if norm(out) != norm(sy.read_text()):
                st["sta_fix"] += 1
                if W: sy.write_text(out)
        # ---- README derived BOM block
        rd = sta / "README.md"
        lines = [f"| `{pn_of[it]}` | {nom_rt[it]} | {role} | {qty} | {uom} | {mb} | PLANNED |"
                 for it,_,nom,role,qty,uom,mb,*_r in rows]
        block = ("<!-- BOM:BEGIN (derived - regenerated by complete_PBS-053-100.py; do not edit) -->\n"
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
        reg = {"register": {"station": f"eWTW-PBS-053-100-{sta_folder.split('_')[0][-3:]}",
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
    blk = ("<!-- SECTION:BEGIN (derived - regenerated by complete_PBS-053-100.py; do not edit) -->\n"
           "## Section realization (derived view)\n\n"
           "| PBS station | Top-level items | PN nodes |\n|---|---:|---:|\n"
           + "\n".join(lines2)
           + f"\n| **Total** | **{sum(tl.values())}** | **{sum(pn_tot.values())}** |\n"
           + f"\n> Plus {len({x[0] for rows in [v[1] for v in SPEC.values()] for r in rows if len(r)>7 for x in r[7]})} distinct catalog-PN identities referenced from `EWTW-530003`, representing {sum(x[1] for rows in [v[1] for v in SPEC.values()] for r in rows if len(r)>7 for x in r[7] if x[2]=='EA')} installation occurrences (EA) plus {sum(1 for rows in [v[1] for v in SPEC.values()] for r in rows if len(r)>7 for x in r[7] if x[2]=='AR')} as-required allocation (CM-001 C1.2).\n"
           + "<!-- SECTION:END -->")
    t0 = sec_rd.read_text() if sec_rd.exists() else "# eWTW-PBS-053-100-000 - Nose and Forward Fuselage Structure\n"
    t1 = re.sub(r"<!-- SECTION:BEGIN.*?SECTION:END -->", blk, t0, flags=re.S) if "<!-- SECTION:BEGIN" in t0 else t0.rstrip() + "\n\n" + blk + "\n"
    if norm(t1) != norm(t0):
        st["readme"] += 1
        if W: sec_rd.write_text(t1)

    # ---- section register (derived)
    sreg = sec / "pbs-item-register.yaml"
    out = GEN + "\n" + yaml.safe_dump({"register": {"section": "eWTW-PBS-053-100",
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
    for cand in root.rglob("053-100_Nose-and-Forward-Fuselage-Structure"):
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
    contam = sum(1 for f in sec.rglob("*.yaml") if "eWTW-PBS-053-000-" in f.read_text())
    print(f"battery: yaml-invalid={bad}  pn-collisions={coll}  set-qty-discipline={'OK' if roll else 'FAIL'}  "
          f"unmanaged-pn={len(unmanaged_all)}  reference-dangling={len(ref_missing)}  register-contamination={contam}  part.yaml on disk={len(list(sec.rglob('part.yaml')))}")
    return 0

if __name__ == "__main__": sys.exit(main())