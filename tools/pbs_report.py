# Generated 2026-11-06 - pbs_report.py (0.1.0)
# Read-only report on the eWTW PBS on disk: station and part-node counts, station-record fields,
# CSN derivation, part roles, catalog identity and short-code collisions. Facts and counts only.
# Exit 0 whenever the report is produced; non-zero only for a usage error or a missing target.
import argparse, json, os, re, subprocess, sys
from pathlib import Path, PurePath

try:
    import yaml
except ImportError:
    sys.exit("pbs_report: PyYAML is required (pip install pyyaml)")

VERSION = "0.1.0"
REPO = Path(__file__).resolve().parents[1]
DEFAULT_PBS = ("01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/"
               "01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure")
STATION_FIELDS = sorted(("id", "localCode", "realizes", "realizesNote", "top_assembly", "root", "mic", "csn", "type",
                         "convention", "parallels", "owner", "status", "interfaces", "parts"))   # CM-001 Issue 2 section 5
RX_NODE = re.compile(r"eWTW-PBS-[0-9]{3}(?:-[0-9]{3})*")
CHAPTER = "eWTW-PBS-053-000"
RX_SECTION = re.compile(r"eWTW-PBS-053-[0-9]00-000")
RX_LOCAL = re.compile(r"(0[0-9]{2})-([0-9]00)-(0[1-9]0)")          # assumed CSN domain: chapter 0CC, section S00, subject 0U0
SUBJECTS = 9                                                       # subject codes 010 ... 090
CATALOG = {"present_non_empty": "present, non-empty", "present_empty": "present, empty", "absent": "absent"}
MISSING, FAILED = object(), object()


def node_id(name):
    head, sep, _ = name.partition("_")
    return head if sep and RX_NODE.fullmatch(head) else None


def git(cwd, *args):
    try:
        r = subprocess.run(("git", *args), cwd=cwd, capture_output=True, encoding="utf-8", errors="replace",
                           env=dict(os.environ, GIT_OPTIONAL_LOCKS="0"))      # no opportunistic index refresh
    except OSError:
        return None
    return r.stdout if r.returncode == 0 else None


def norm(v):
    if isinstance(v, dict): return {label(k): norm(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)): return [norm(x) for x in v]
    if isinstance(v, (set, frozenset)): return sorted(json.dumps(norm(x), sort_keys=True) for x in v)
    if isinstance(v, bytes): return v.hex()
    if v is None or isinstance(v, (bool, int, float, str)): return v
    return str(v)


def label(v):
    if v is MISSING: return "(absent)"
    if isinstance(v, str): return v if v else "(empty string)"
    if v is None: return "(null)"
    return f"({type(v).__name__}) " + json.dumps(norm(v), sort_keys=True, ensure_ascii=True, separators=(",", ":"))


def counts(values):
    c = {}
    for v in values: c[v] = c.get(v, 0) + 1
    return {k: c[k] for k in sorted(c)}


def sget(doc, key):                       # station field under station:, else at the document root
    root = doc if isinstance(doc, dict) else {}
    block = root.get("station") if isinstance(root.get("station"), dict) else {}
    return block[key] if key in block else root.get(key, MISSING)


def pget(doc, key):                       # part field under part: when it exists, else at the document root
    root = doc if isinstance(doc, dict) else {}
    src = root["part"] if "part" in root else root
    return src.get(key, MISSING) if isinstance(src, dict) else MISSING


def build(target):
    target = Path(target)
    top = git(target, "rev-parse", "--show-toplevel")
    top = top.strip() if top else None
    head = git(target, "rev-parse", "HEAD")
    status = git(top, "status", "--porcelain") if top else None
    repo = Path(os.path.realpath(REPO))
    root = os.path.realpath(top) if top else str(repo) if target == repo or repo in target.parents else str(target.parent)

    def rel(p):
        try: r = os.path.relpath(p, root)
        except ValueError: r = os.path.join(os.path.basename(target), os.path.relpath(p, target))
        return PurePath(r).as_posix()

    nodes, stations, parts, skipped, flat = {}, [], [], [], []
    def onerror(e):
        skipped.append((rel(e.filename) if e.filename else "?", "directory not listed: " + (e.strerror or type(e).__name__)))
    for d, dirs, files in os.walk(target, onerror=onerror):
        dirs.sort()
        p = Path(d)
        nid = node_id(p.name)
        if nid: nodes.setdefault(nid, []).append(p)
        if "station.yaml" in files: stations.append(p)
        if "part.yaml" in files: parts.append(p)
    key = lambda p: rel(p)
    stations.sort(key=key); parts.sort(key=key)

    def load(f):
        try:
            with open(f, "rb") as fh: doc = yaml.safe_load(fh.read())
        except OSError as e:
            skipped.append((rel(f), "not read: " + (e.strerror or type(e).__name__))); return FAILED
        except yaml.MarkedYAMLError as e:
            why = "; ".join(x for x in (e.context, e.problem) if x) or type(e).__name__
            if e.problem_mark is not None: why += f" (line {e.problem_mark.line + 1}, column {e.problem_mark.column + 1})"
            skipped.append((rel(f), "not parsed: " + why)); return FAILED
        except yaml.YAMLError as e:
            skipped.append((rel(f), "not parsed: " + (str(e).splitlines() or [type(e).__name__])[0])); return FAILED
        except Exception as e:
            skipped.append((rel(f), "not parsed: " + type(e).__name__)); return FAILED
        if not isinstance(doc, dict): flat.append(rel(f))
        return doc
    sdoc = {s: load(s / "station.yaml") for s in stations}
    pdoc = {p: load(p / "part.yaml") for p in parts}
    records = [(s, sdoc[s]) for s in stations if sdoc[s] is not FAILED]
    within = lambda p, a: p == a or a in p.parents

    # 2 - chapter 053 sections
    chapters = sorted(nodes.get(CHAPTER, []), key=key)
    sections = sorted((p for nid, ps in nodes.items() if RX_SECTION.fullmatch(nid) for p in ps if p.parent in chapters),
                      key=lambda p: (node_id(p.name), rel(p)))
    def section_row(sts, pts):
        return {"stations": len(sts), "part_nodes": len(pts),
                "records_by_convention": counts("(station record not parsed)" if sdoc[s] is FAILED
                                                else label(sget(sdoc[s], "convention")) for s in sts)}
    rows, in_sts, in_pts = [], set(), set()
    for sec in sections:
        sts = [s for s in stations if within(s, sec)]; pts = [p for p in parts if within(p, sec)]
        in_sts.update(sts); in_pts.update(pts)
        rows.append({"section": node_id(sec.name), "path": rel(sec), **section_row(sts, pts)})
    total = {"sections": len(sections), **section_row(sorted(in_sts, key=key), sorted(in_pts, key=key))}

    # 3 - station fields
    fields = {}
    for f in STATION_FIELDS:
        under = sum(1 for _, d in records if isinstance(d, dict) and isinstance(d.get("station"), dict) and f in d["station"])
        at_root = sum(1 for _, d in records if isinstance(d, dict) and f in d)
        fields[f] = {"under_station": under, "at_root": at_root, "either": sum(1 for _, d in records if sget(d, f) is not MISSING)}

    # 4, 5 - identity and CSN
    id_diff, csn_diff, outside, codes = [], [], [], {}
    for s, d in records:
        sid, fid = sget(d, "id"), node_id(s.name)
        if not (isinstance(sid, str) and sid == fid):
            id_diff.append({"path": rel(s), "folder_node_id": fid or "(none)", "station_id": label(sid)})
        lc, csn = sget(d, "localCode"), sget(d, "csn")
        m = RX_LOCAL.fullmatch(lc) if isinstance(lc, str) else None
        if not m:
            outside.append({"path": rel(s), "localCode": label(lc)}); continue
        codes[s] = m[3]
        derived = m[1][1:3] + m[2][0:2] + m[3][0:2]
        if not (isinstance(csn, str) and csn == derived):
            csn_diff.append({"path": rel(s), "localCode": lc, "csn": label(csn), "derived_csn": derived})
    subjects = []
    for sec in sections:
        used = sorted({c for s, c in codes.items() if within(s, sec)})
        subjects.append({"section": node_id(sec.name), "used": len(used), "of": SUBJECTS, "codes": used})

    # 6, 7 - part roles and catalog identity
    def enclosing(p):
        for a in (p, *p.parents):
            if a in sdoc: return a
            if a == target: return None
    groups, cat = {}, {"present_non_empty": 0, "present_empty": 0, "absent": 0}
    for p in parts:
        d = pdoc[p]
        if d is FAILED: continue
        st = enclosing(p)
        g = ("(no enclosing station)" if st is None else "(station record not parsed)" if sdoc[st] is FAILED
             else label(sget(sdoc[st], "convention")))
        groups.setdefault(g, []).append(label(pget(d, "role")))
        v = pget(d, "catalog_pn")
        empty = v is None or (isinstance(v, (str, list, tuple, dict, set)) and len(v) == 0)
        cat["absent" if v is MISSING else "present_empty" if empty else "present_non_empty"] += 1

    # 8 - short-code collisions
    collisions = [{"x": x, "x_paths": sorted(rel(p) for p in nodes[x]), "x000_paths": sorted(rel(p) for p in nodes[x + "-000"])}
                  for x in sorted(nodes) if x + "-000" in nodes]

    return {
        "tool": "pbs_report", "version": VERSION, "target": rel(target),
        "repository": {"commit": head.strip() if head and head.strip() else "unknown",
                       "tree": "unknown" if status is None else "dirty" if status.strip() else "clean"},
        "chapter_053": {"chapter_paths": [rel(c) for c in chapters], "sections": rows, "total": total,
                        "whole_target": {"stations": len(stations), "part_nodes": len(parts)}},
        "station_fields": {"station_records": len(records), "fields": fields,
                           "lacking_realizes": [rel(s) for s, d in records if sget(d, "realizes") is MISSING]},
        "station_id_differs_from_folder": id_diff,
        "csn": {"localCode_pattern": RX_LOCAL.pattern, "derivation": "CCC[1:3] + SSS[0:2] + UUU[0:2]",
                "csn_differs_from_derived": csn_diff, "localCode_outside_pattern": outside,
                "subject_codes_by_section": subjects},
        "roles_by_convention": {"part_records": sum(len(v) for v in groups.values()),
                                "groups": {g: counts(groups[g]) for g in sorted(groups)}},
        "catalog_pn": cat,
        "short_code_collisions": collisions,
        "station_status": counts(label(sget(d, "status")) for _, d in records),
        "skipped": [{"path": p, "reason": r} for p, r in sorted(skipped)],
        "top_level_not_a_mapping": sorted(flat),
    }


def esc(s):                               # printable ASCII as is; backslash, control and non-ASCII characters escaped
    return "".join(c if " " <= c <= "~" and c != "\\" else json.dumps(c)[1:-1] for c in s)


def text(d):
    L = []
    w = L.append
    def cnt(c, ind):
        if not c: w(ind + "(none)")
        for k, n in c.items(): w(f"{ind}{n:>6}  {esc(k)}")
    def paths(items, ind):
        if not items: w(ind + "(none)")
        for p in items: w(ind + esc(p))
    w(f"pbs_report {d['version']}")
    w(f"target: {esc(d['target'])}")
    w("")
    w("1. Repository")
    w(f"  commit: {d['repository']['commit']}")
    w(f"  tree: {d['repository']['tree']}")
    w("")
    c = d["chapter_053"]
    w("2. Chapter 053 sections: stations, part nodes, station records by station.convention")
    w("  chapter " + CHAPTER + ":")
    paths(c["chapter_paths"], "    ")
    for r in c["sections"]:
        w(f"  section {r['section']}")
        w(f"    path: {esc(r['path'])}")
        w(f"    stations: {r['stations']}")
        w(f"    part nodes: {r['part_nodes']}")
        w("    station records by station.convention:")
        cnt(r["records_by_convention"], "    ")
    t = c["total"]
    w(f"  total, {t['sections']} sections")
    w(f"    stations: {t['stations']}")
    w(f"    part nodes: {t['part_nodes']}")
    w("    station records by station.convention:")
    cnt(t["records_by_convention"], "    ")
    w("  whole target")
    w(f"    stations: {c['whole_target']['stations']}")
    w(f"    part nodes: {c['whole_target']['part_nodes']}")
    w("")
    s = d["station_fields"]
    w("3. Station fields (CM-001 Issue 2 section 5): station records carrying each field")
    w(f"  station records: {s['station_records']}")
    w(f"  {'field':<14}{'under station:':>16}{'at root':>9}{'either':>8}")
    for f, n in s["fields"].items():
        w(f"  {f:<14}{n['under_station']:>16}{n['at_root']:>9}{n['either']:>8}")
    w(f"  stations lacking realizes: {len(s['lacking_realizes'])}")
    paths(s["lacking_realizes"], "    ")
    w("")
    w(f"4. Stations whose station.id differs from the folder node id: {len(d['station_id_differs_from_folder'])}")
    if not d["station_id_differs_from_folder"]: w("  (none)")
    for r in d["station_id_differs_from_folder"]:
        w(f"  {esc(r['path'])}")
        w(f"    folder node id: {r['folder_node_id']}  station.id: {esc(r['station_id'])}")
    w("")
    k = d["csn"]
    w("5. CSN")
    w(f"  assumed localCode pattern: {k['localCode_pattern']}")
    w(f"  derived CSN: {k['derivation']}")
    w(f"  stations whose station.csn differs from the derived CSN: {len(k['csn_differs_from_derived'])}")
    if not k["csn_differs_from_derived"]: w("    (none)")
    for r in k["csn_differs_from_derived"]:
        w(f"    {esc(r['path'])}")
        w(f"      localCode: {esc(r['localCode'])}  csn: {esc(r['csn'])}  derived: {r['derived_csn']}")
    w(f"  stations whose station.localCode is outside the pattern: {len(k['localCode_outside_pattern'])}")
    if not k["localCode_outside_pattern"]: w("    (none)")
    for r in k["localCode_outside_pattern"]:
        w(f"    {esc(r['path'])}")
        w(f"      localCode: {esc(r['localCode'])}")
    w("  subject codes 010-090 used per chapter 053 section (from station.localCode):")
    if not k["subject_codes_by_section"]: w("    (none)")
    for r in k["subject_codes_by_section"]:
        w(f"    {r['section']}  {r['used']}/{r['of']}  {' '.join(r['codes']) or '-'}")
    w("")
    g = d["roles_by_convention"]
    w("6. part.yaml role, by station.convention of the enclosing station")
    w(f"  part records: {g['part_records']}")
    if not g["groups"]: w("  (none)")
    for conv, roles in g["groups"].items():
        w(f"  {esc(conv)}")
        cnt(roles, "  ")
    w("")
    w("7. part.yaml catalog_pn (empty: null, empty string, empty list or empty mapping)")
    for name, n in d["catalog_pn"].items(): w(f"  {n:>6}  {CATALOG[name]}")
    w("")
    w(f"8. Short-code collisions, node id X where node X-000 also exists: {len(d['short_code_collisions'])}")
    if not d["short_code_collisions"]: w("  (none)")
    for r in d["short_code_collisions"]:
        w(f"  {r['x']}")
        for p in r["x_paths"]: w(f"    X:     {esc(p)}")
        for p in r["x000_paths"]: w(f"    X-000: {esc(p)}")
    w("")
    w("9. station.status")
    cnt(d["station_status"], "  ")
    w("")
    w(f"Skipped, not read or not parsed: {len(d['skipped'])}")
    if not d["skipped"]: w("  (none)")
    for r in d["skipped"]: w(f"  {esc(r['path'])}: {esc(r['reason'])}")
    w(f"Parsed, top level not a mapping (empty documents included): {len(d['top_level_not_a_mapping'])}")
    paths(d["top_level_not_a_mapping"], "  ")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Read-only report on the eWTW PBS. Facts and counts only.")
    ap.add_argument("--pbs", default=None, help="PBS directory (default: the eWTW PBS of this repository)")
    ap.add_argument("--json", action="store_true", help="print the report as JSON")
    a = ap.parse_args()
    target = Path(a.pbs) if a.pbs is not None else REPO / DEFAULT_PBS
    if a.pbs == "" or not target.is_dir():
        print("pbs_report: target directory not found (--pbs)", file=sys.stderr)
        return 2
    d = build(os.path.realpath(target))
    sys.stdout.write(json.dumps(d, indent=2, ensure_ascii=True) + "\n" if a.json else text(d))
    return 0


if __name__ == "__main__":
    sys.exit(main())
