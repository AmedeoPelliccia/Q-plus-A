#!/usr/bin/env python3
# =============================================================================
# migrate_PBS-053-010.py  (1.0.1)   -   F0 resolution, Copilot-free
# Merges the evolved residue branch eWTW-PBS-053-010-000_Forward-Fuselage-
# Section into its canonical twin eWTW-PBS-053-100-040 (content from residue,
# identity from twin), retires the residue, and repoints external references.
# Modes: --plan (default) / --apply. Idempotent after apply (residue absent ->
# merge and retire phases no-op; repoint replacements find nothing).
# =============================================================================
import argparse, re, shutil, sys, datetime
from pathlib import Path
try:
    import yaml
except ImportError:
    print("pyyaml required"); sys.exit(2)

TODAY = datetime.date.today().isoformat()
PROV  = f"# Amended {TODAY} - migrate_PBS-053-010.py (1.0.1)"
RES_SEC = "eWTW-PBS-053-010-000_Forward-Fuselage-Section"
TWIN    = "eWTW-PBS-053-100-040_Radome-and-Diverters-Attach-Structure"
OLD_CSN, NEW_CSN = "530101", "531004"
OLD_ID,  NEW_ID  = "eWTW-PBS-053-010-010", "eWTW-PBS-053-100-040"

# hinge nomenclature carried from the residue (ratified A1.8 handedness truth)
RENAME_TWIN = {  # twin folder suffix -> residue-truth suffix
  "EWTW-531004-021_FITTING-RADOME-HINGE-LH": "EWTW-531004-021_FITTING-RADOME-HINGE-UPPER",
  "EWTW-531004-022_FITTING-RADOME-HINGE-RH": "EWTW-531004-022_FITTING-RADOME-HINGE-LOWER",
}
NOM = {"021": "FITTING-RADOME-HINGE-UPPER", "022": "FITTING-RADOME-HINGE-LOWER"}

STATION_V2 = """# Assembly station record
# AMPEL360-PBS-PN-CM-001 (Issue 2) - folder name is SSOT; this file mirrors it
# Generated 2026-07-06 - realize_PBS-053_GATLAS.py (2.0.0-GATLAS)
{prov}
station:
  id: eWTW-PBS-053-100-040
  localCode: "053-100-040"
  realizes: "053-100-400"
  realizesNote: "current S-ATLAS address (post hundreds migration); PBS-local code conserved per CM-001 A1.1 - identity vs reference: localCode feeds CSN and the PN tree; realizes follows taxonomy evolution"
  top_assembly: EWTW-531004-000
  root: EWTW-531004
  mic: EWTW
  csn: "531004"
  type: assembly-station
  convention: "AMPEL360-PBS-PN-CM-001 (Issue 2)"
  parallels: AMPEL360-AMM-INFOCODE-CM-001
  model: eWTW
  side: SSOT
  layer: "deepest SSOT layer (configuration items)"
  owner: Q-STRUCTURES
  doctrine: green-native
  grammar: "EWTW-<CSN>-<VAR>[-<VAR>...] (x10 find; 000 = assembly; variant names describe position - A1.8)"
  interfaces:
    - icd: ICD-EWTW-531004-034
      space: taxonomy
      counterpart: "034"
      item: "weather-radar antenna - mechanical mount, bonding, connector clearance"
      carriedBy: [EWTW-531004-060]
    - icd: ICD-EWTW-531004-538001
      space: pbs-local
      counterpart: eWTW-PBS-053-800-010
      counterpartCsn: "538001"
      taxonomyRef: "053-800-100"
      item: "forward pressure bulkhead - structural joint at radome bulkhead station"
      carriedBy: [EWTW-531004-011]
    - icd: ICD-EWTW-531004-024
      space: taxonomy
      counterpart: "024"
      item: "bonding and lightning protection - diverter strips to airframe return path"
      carriedBy: [EWTW-531004-040, EWTW-531004-011]
    - icd: ICD-EWTW-531004-030
      space: taxonomy
      counterpart: "030"
      item: "radome / nose de-ice provisions"
      carriedBy: []
  parts: 11
  status: realized
  version: "2.0"
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args(); W = a.apply
    root = Path(a.root)
    ch = next((p for p in root.rglob("eWTW-PBS-053-000_Fuselage-Wide-Tube") if p.is_dir()), None)
    if not ch: print("chapter dir not found"); sys.exit(1)
    res = ch / RES_SEC
    twin = next((p for p in ch.rglob(TWIN) if p.is_dir()), None)
    if not twin: print("canonical twin not found"); sys.exit(1)
    st = dict(merged=0, renamed=0, retired=0, repointed=0)

    # ---- Phase M: merge residue content into twin (content=residue, identity=twin)
    res_sta = res / "eWTW-PBS-053-010-010_Radome-and-Nose-Cone-Attach-Structure"
    if res_sta.is_dir():
        for rp in sorted(res_sta.rglob("part.yaml")):
            item = re.search(r"EWTW-530101-(\d+)_", str(rp.parent.name)).group(1)
            tp = next((q for q in twin.rglob(f"EWTW-{NEW_CSN}-{item}_*/part.yaml")), None)
            if not tp: print(f"!! twin missing item {item} - report only"); continue
            rd = (yaml.safe_load(rp.read_text()) or {}).get("part", {})
            td_txt = tp.read_text()
            td = (yaml.safe_load(td_txt) or {}).get("part", {})
            merged = dict(td)
            for k, v in rd.items():
                if k in ("pn","csn","parentAssembly"): continue      # identity = twin
                merged.setdefault(k, v)
            merged["nomenclature"] = NOM.get(item, rd.get("nomenclature", td.get("nomenclature")))
            def _san(v):
                if isinstance(v, str):
                    return v.replace(OLD_CSN, NEW_CSN).replace(OLD_ID, NEW_ID).replace("053-010-010","053-100-040")
                if isinstance(v, dict): return {k:_san(x) for k,x in v.items()}
                if isinstance(v, list): return [_san(x) for x in v]
                return v
            merged = {k:_san(v) for k,v in merged.items()}
            hdr = [l for l in td_txt.splitlines() if l.startswith(("# Generated","# Amended","# Part","# AMPEL"))]
            if not any("migrate_PBS-053-010.py" in l for l in hdr): hdr.append(PROV)
            out = "\n".join(hdr) + "\n" + yaml.safe_dump({"part": merged}, sort_keys=False, allow_unicode=True)
            if out != td_txt:
                st["merged"] += 1
                if W: tp.write_text(out)
    # twin hinge folder renames (A1.8 nomenclature carried over)
    for old, new in RENAME_TWIN.items():
        src = next((q for q in twin.rglob(old) if q.is_dir()), None)
        if src:
            st["renamed"] += 1
            if W: src.rename(src.parent / new)
    # twin station.yaml v2.0 (rich schema transposed, ICDs re-derived per A1.9)
    tw_sy = twin / "station.yaml"
    out = STATION_V2.format(prov=PROV)
    if not tw_sy.exists() or tw_sy.read_text() != out:
        st["merged"] += 1
        if W: tw_sy.write_text(out)

    # ---- Phase X: repoint external references (mechanical only)
    conv = next(root.rglob("AMPEL360-PBS-PN-CM-001_*.md"), None)
    targets = [ch / "PBS-053-BREAKDOWN.md", ch / "README.md",
               ch / "PBS-053-REALIZED-TREE.txt", twin / "README.md"]
    if conv: targets.append(conv)
    for f in targets:
        if not f.exists(): continue
        t0 = f.read_text(); t = t0
        t = t.replace(OLD_CSN, NEW_CSN).replace(OLD_ID, NEW_ID)
        t = t.replace("053-010-010", "053-100-040")
        # drop the residue section row/block lines mentioning the Forward section node
        t = "\n".join(l for l in t.splitlines()
                      if "053-010-000" not in l and "Forward-Fuselage-Section" not in l) + "\n"
        if t != t0:
            st["repointed"] += 1
            if W: f.write_text(t)

    # ---- Phase R: retire the residue branch
    if res.is_dir():
        n = sum(1 for _ in res.rglob("*") if _.is_file())
        st["retired"] = n
        print(f"RETIRE {res.relative_to(root)}  ({n} files)")
        if W: shutil.rmtree(res)

    mode = "APPLIED" if W else "PLAN"
    print(f"[{mode}] part.yaml merged/updated={st['merged']}  hinge renames={st['renamed']}  "
          f"external files repointed={st['repointed']}  residue files retired={st['retired']}")

    # ---- battery
    left = [str(p) for p in ch.rglob("*") if p.is_file()
            and re.search(r"530101|053-010-01\d", p.read_text(errors="ignore"))]
    icds = set()
    for p in ch.rglob("station.yaml"):
        icds |= set(re.findall(r"ICD-[A-Z0-9-]+", p.read_text()))
    bad_icd = [i for i in icds if not re.fullmatch(r"ICD-EWTW-\d{6}-(\d{3}|\d{6})", i)]
    n_parts = len(list(ch.rglob("part.yaml")))
    bulk = next((q for q in ch.rglob("eWTW-PBS-053-800-010_*") if q.is_dir()), None)
    hup = next((q for q in ch.rglob("EWTW-531004-021_FITTING-RADOME-HINGE-UPPER") if q.is_dir()), None)
    yb = 0
    for p in ch.rglob("*.yaml"):
        try: yaml.safe_load(p.read_text())
        except Exception: yb += 1
    print(f"battery: residual-old-refs={len(left)}  bad-icd-grammar={len(bad_icd)}  "
          f"chapter part.yaml={n_parts}  icd-counterpart-053-800-010={'OK' if bulk else 'MISSING'}  "
          f"hinge-UPPER-on-twin={'OK' if hup or not W else 'MISSING'}  yaml-invalid={yb}")
    if left[:4]: print("  residual refs in:", *[Path(x).name for x in left[:4]])
    return 0

if __name__ == "__main__": sys.exit(main())