#!/usr/bin/env python3
# =============================================================================
# complete_PBS-053-000.py  (1.1.0)
# Depth Pass 1 - section eWTW-PBS-053-000 (General): adds missing PN nodes per
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
PROV  = f"# Amended {TODAY} - complete_PBS-053-000.py (1.1.0)"
GEN   = f"# Generated {TODAY} - complete_PBS-053-000.py (1.1.0)"

# ---------------------------------------------------------------- target spec
# (station csn, station folder, [(item, parent_item|None, nomenclature, role, qty, uom, mb)])
SPEC = {
 "530001": ("eWTW-PBS-053-000-010_Fuselage-General", [
   ("000", None,  "STRUCTURE, FUSELAGE GENERAL",                    "assembly", 1,"EA","make"),
   ("010", "000", "MARKING-AND-PLACARD-PROVISION-SET",              "set",      1,"SET","buy"),
   ("011", "010", "STENCIL SET, SERVICE AND RESCUE MARKINGS",       "leaf",     1,"EA","buy"),
   ("012", "010", "PLATE, DATA AND REGISTRATION",                   "leaf",     2,"EA","buy"),
   ("013", "010", "MARKER, ZONAL STATION REFERENCE",                "leaf",    24,"EA","buy"),
   ("020", "000", "BONDING-AND-GROUNDING-PROVISION-SET",            "set",      1,"SET","buy"),
   ("021", "020", "JUMPER, BONDING STANDARD",                       "leaf",    40,"EA","buy"),
   ("022", "020", "STUD, GROUNDING RECEPTACLE",                     "leaf",    12,"EA","buy"),
   ("023", "020", "STRAP, STATIC DISCHARGER PROVISION",             "leaf",     8,"EA","buy"),
   ("030", "000", "FINISH-AND-COATING-PROVISION-SET",               "set",      1,"SET","buy"),
   ("031", "030", "COATING SYSTEM, EXTERIOR BASE",                  "leaf",     1,"AR","buy"),
   ("032", "030", "COATING, EROSION PROTECTION LOCAL",              "leaf",     1,"AR","buy"),
   ("040", "000", "DATUM-AND-ALIGNMENT-PROVISION-SET",              "set",      1,"SET","make"),
   ("041", "040", "TARGET, OPTICAL ALIGNMENT",                      "leaf",     6,"EA","buy"),
   ("042", "040", "PLATE, REFERENCE DATUM",                         "leaf",     4,"EA","make"),
 ]),
 "530002": ("eWTW-PBS-053-000-020_Fuselage-Protective-Films-and-Tapes", [
   ("000", None,  "PROTECTIVE FILMS AND TAPES, FUSELAGE",           "assembly", 1,"EA","make"),
   ("010", "000", "FILM, EROSION PROTECTION",                       "leaf",     1,"AR","buy"),
   ("020", "000", "TAPE, AERODYNAMIC SEALING",                      "leaf",     1,"AR","buy"),
   ("030", "000", "TAPE, ANTI-CHAFE",                               "leaf",     1,"AR","buy"),
   ("040", "000", "FILM, WALKWAY ANTI-SKID",                        "leaf",     1,"AR","buy"),
   ("050", "000", "TAPE, MOISTURE BARRIER",                         "leaf",     1,"AR","buy"),
   ("060", "000", "FILM, DIELECTRIC ISOLATION",                     "leaf",     1,"AR","buy"),
   ("070", "000", "TAPE, EDGE AND SEAM PROTECTION",                 "leaf",     1,"AR","buy"),
 ]),
 "530003": ("eWTW-PBS-053-000-030_Fuselage-External-Access-Doors-and-Panels-General", [
   ("000", None,  "EXTERNAL ACCESS DOORS AND PANELS, GENERAL",      "assembly", 1,"EA","make"),
   ("010", "000", "LATCH-STANDARD-PROVISION-SET",                   "set",      1,"SET","buy"),
   ("011", "010", "LATCH, FLUSH QUARTER-TURN STANDARD",             "leaf",     1,"AR","buy"),
   ("012", "010", "RECEPTACLE, LATCH STANDARD",                     "leaf",     1,"AR","buy"),
   ("020", "000", "HINGE-STANDARD-PROVISION-SET",                   "set",      1,"SET","buy"),
   ("021", "020", "HINGE, CONTINUOUS STANDARD",                     "leaf",     1,"AR","buy"),
   ("022", "020", "HINGE, REMOVABLE-PIN STANDARD",                  "leaf",     1,"AR","buy"),
   ("030", "000", "SEAL-STANDARD-PROVISION-SET",                    "set",      1,"SET","buy"),
   ("031", "030", "SEAL, HOLLOW-BULB STANDARD",                     "leaf",     1,"AR","buy"),
   ("032", "030", "SEAL, WIPER-BLADE STANDARD",                     "leaf",     1,"AR","buy"),
   ("040", "000", "PANEL-STANDARD-PROVISION-SET",                   "set",      1,"SET","make"),
   ("041", "040", "PANEL, ROUND STANDARD",                          "leaf",     1,"AR","make"),
   ("042", "040", "PANEL, RECTANGULAR STANDARD",                    "leaf",     1,"AR","make"),
   ("050", "000", "MARKING, ACCESS IDENTIFICATION SET",             "leaf",     1,"EA","buy"),
   ("060", "000", "RETAINER, PANEL STANDARD",                       "leaf",     1,"AR","buy"),
   ("070", "000", "STOP AND SUPPORT, PANEL STANDARD",               "leaf",     1,"AR","buy"),
 ]),
 "530004": ("eWTW-PBS-053-000-040_Fuselage-Drains", [
   ("000", None,  "DRAINS, FUSELAGE",                               "assembly", 1,"EA","make"),
   ("010", "000", "MAST-DRAIN-PROVISION-SET",                       "set",      1,"SET","make"),
   ("011", "010", "MAST, DRAIN AFT",                                "leaf",     2,"EA","make"),
   ("012", "010", "SEAL, MAST BASE",                                "leaf",     2,"EA","buy"),
   ("020", "000", "VALVE-DRAIN-PROVISION-SET",                      "set",      1,"SET","buy"),
   ("021", "020", "VALVE, DRAIN FLAPPER",                           "leaf",    10,"EA","buy"),
   ("022", "020", "GROMMET, DRAIN PATH",                            "leaf",    24,"EA","buy"),
   ("030", "000", "BILGE-DRAIN-PATH-PROVISION-SET",                 "set",      1,"SET","make"),
   ("031", "030", "CHANNEL, BILGE DRAIN",                           "leaf",     8,"EA","make"),
   ("032", "030", "DAM, MOISTURE CONTROL",                          "leaf",    12,"EA","make"),
   ("040", "000", "PLUG-AND-CAP-PROVISION-SET",                     "set",      1,"SET","buy"),
   ("041", "040", "PLUG, DRAIN SERVICE",                            "leaf",     6,"EA","buy"),
   ("050", "000", "OUTLET, DRAIN OVERBOARD",                        "leaf",     8,"EA","make"),
   ("060", "000", "GUARD AND SCREEN, DRAIN",                        "leaf",     8,"EA","buy"),
 ]),
}

REALIZES = {"530001":"053-000-100","530002":"053-000-200",
            "530003":"053-000-300","530004":"053-000-400"}
BOUNDARY = {
 "530001": "Only fuselage structural provisions are owned here. Placard and marking content is ATA 011; electrical bonding conductors and system functionality remain with their owning chapters; standard structural families and repair practices remain ATA 051.",
 "530002": "This subject owns installed fuselage protective film and tape product sets. Generic standard-practice materials, process specifications and repair practices remain ATA 051.",
 "530003": "General panel hardware and provisions are defined here; physical panel instances remain in the zonal access-panel subjects (053-100-060, 053-200-060, 053-300-040, 053-400-050). Door leaves and mechanisms remain ATA 052. Zone stations reference these standards via catalog_pn - never a second folder.",
 "530004": "This subject owns fuselage-installed general drain hardware, outlets and structural drain paths. System-specific source plumbing and fluid functions remain with the originating system chapter.",
}

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
    return re.sub(r"\n{2,}", "\n", s).strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="repo root or section parent")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    root = Path(a.root)
    hits = list(root.rglob("eWTW-PBS-053-000-000_General"))
    if not hits:
        print("section folder eWTW-PBS-053-000-000_General not found under", root); sys.exit(1)
    sec = hits[0]
    W = a.apply
    st = dict(added=0, part_fix=0, sta_fix=0, readme=0, reg=0, skipped=0)
    section_rows = []

    for csn, (sta_folder, rows) in SPEC.items():
        sta = sec / sta_folder
        if not sta.is_dir():
            print(f"!! station folder missing: {sta_folder} - skipped"); continue
        pn_of = {it: f"EWTW-{csn}-{it}" for it,_,_,_,_,_,_ in rows}
        nom_rt = {it: nom for it,_,nom,_,_,_,_ in rows}
        dir_of = {}
        # resolve folder path for each item (nested under its parent chain)
        for it, par, nom, role, qty, uom, mb in rows:
            parent_dir = sta if par is None else dir_of[par]
            # find existing folder for this PN regardless of slug
            existing = [d for d in parent_dir.iterdir() if d.is_dir() and d.name.startswith(pn_of[it]+"_")] if parent_dir.exists() else []
            d = existing[0] if existing else parent_dir / f"{pn_of[it]}_{slug(nom)}"
            dir_of[it] = d
            py = d / "part.yaml"
            target = {
                "pn": pn_of[it], "nomenclature": nom, "csn": csn, "item": it,
                "type": "part", "role": role, "qty": qty, "uom": uom,
                "make_buy": mb,
                "parentAssembly": (pn_of[par] if par else None),
                "applicability": {"model": "eWTW", "effectivity": ["ALL"]},
                "status": "PLANNED",
                "convention": "AMPEL360-PBS-PN-CM-001 (Issue 2)",
            }
            if par is None: target.pop("parentAssembly")
            if py.exists():
                cur = load(py).get("part", {})
                # invariants: never change identity values
                for k in ("pn","csn","item"):
                    if str(cur.get(k, target[k])) != str(target[k]):
                        print(f"!! identity mismatch {py}: {k} disk={cur.get(k)} spec={target[k]} - left untouched")
                        st["skipped"] += 1; break
                else:
                    merged = dict(cur)
                    nom_rt[it] = cur.get("nomenclature", nom_rt[it])
                    for k in ("role","qty","uom","make_buy","convention"):
                        merged[k] = target[k]
                    merged.setdefault("applicability", target["applicability"])
                    merged.setdefault("status", "PLANNED")
                    if par and not merged.get("parentAssembly"):
                        merged["parentAssembly"] = pn_of[par]
                    prev = py.read_text().splitlines()
                    header_lines = [l for l in prev if l.startswith(("# Generated","# Amended"))]
                    if not any("complete_PBS-053-000.py" in l and l.startswith("# Amended") for l in header_lines):
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
            s.setdefault("realizesNote","current S-ATLAS address; PBS-local code conserved per CM-001 A1.1")
            s["convention"] = "AMPEL360-PBS-PN-CM-001 (Issue 2)"
            s["parts"] = len(list(sta.rglob("part.yaml"))) + (0 if not W else 0)
            s.setdefault("interfaces", [])
            s["version"] = "1.2"
            hdr = [l for l in sy.read_text().splitlines() if l.startswith(("# Generated","# Amended"))]
            if not any("complete_PBS-053-000.py" in l for l in hdr):
                hdr.append(PROV)
            out = "\n".join(hdr) + "\n" + yaml.safe_dump({"station": s}, sort_keys=False)
            if norm(out) != norm(sy.read_text()):
                st["sta_fix"] += 1
                if W: sy.write_text(out)
        # ---- README derived BOM block
        rd = sta / "README.md"
        lines = [f"| `{pn_of[it]}` | {nom_rt[it]} | {role} | {qty} | {uom} | {mb} | PLANNED |"
                 for it,_,nom,role,qty,uom,mb in rows]
        block = ("<!-- BOM:BEGIN (derived - regenerated by complete_PBS-053-000.py; do not edit) -->\n"
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
        reg = {"register": {"station": f"eWTW-PBS-053-000-{sta_folder.split('_')[0][-3:]}",
                            "csn": csn, "derived": True,
                            "parts": [{"pn": pn_of[it], "nomenclature": nom_rt[it], "role": role,
                                       "qty": qty, "uom": uom, "make_buy": mb, "status": "PLANNED"}
                                      for it,_,nom,role,qty,uom,mb in rows]}}
        out = GEN + "\n" + yaml.safe_dump(reg, sort_keys=False, allow_unicode=True)
        if not pr.exists() or norm(out) != norm(pr.read_text()):
            st["reg"] += 1
            if W: pr.write_text(out)
        section_rows.append({"station": sta_folder.split("_")[0], "csn": csn,
                             "parts": len(rows), "status": "PLANNED"})

    # ---- section register (derived)
    sreg = sec / "pbs-item-register.yaml"
    out = GEN + "\n" + yaml.safe_dump({"register": {"section": "eWTW-PBS-053-000",
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
    for cand in root.rglob("053-000_General"):
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
    roll = all(r[4] == 1 for rows in [v[1] for v in SPEC.values()] for r in rows if r[3]=="set")
    print(f"battery: yaml-invalid={bad}  pn-collisions={coll}  set-qty-discipline={'OK' if roll else 'FAIL'}  "
          f"part.yaml on disk={len(list(sec.rglob('part.yaml')))}")
    return 0

if __name__ == "__main__": sys.exit(main())