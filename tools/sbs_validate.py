#!/usr/bin/env python3
# Generated 2026-09-14 - sbs_validate.py (0.1.2)
# Single acceptance validator for SBS rework PRs. Exit 1 on ANY failing check.
# Distinguishes typed references (PBS id, part number, taxonomy address, file) and
# active occurrences from historical citations inside convention/act documents.
import argparse, glob, os, re, subprocess, sys
from pathlib import Path
import yaml

PROTECTED = ("01-01_PBS_Product-Breakdown", "01-02-01-01-02_BWB", "01-03_TECHNOLOGIES")
PROTECTED_EXT = (".step", ".glb", ".png", ".stp")
HISTORICAL = ("CM-00", "AMENDMENT", "CLARIFICATION", "ASSESSMENT", "/history/", "CHANGELOG")
RX_PBS = re.compile(r"eWTW-PBS-\d{3}(?:-\d{3}){0,2}\b")
RX_PN = re.compile(r"\bEWTW-\d{6}-\d{3}\b")
RX_TAX = re.compile(r"(?<![\w-])0\d{2}-\d00-\d00(?![\w-])")   # subject-grain S-ATLAS address, not a PBS-local tail
RX_FILEKEY = re.compile(r"^\s*(?:-\s*)?(?:file|path|dossier|evidence|source|exported|gate)\s*:\s*['\"]?([^'\"\s#]+\.(?:md|yaml|yml|txt|py|step|glb|png|inp|frd))['\"]?", re.M)

def sh(*a, cwd=None):
    return subprocess.run(a, capture_output=True, text=True, cwd=cwd).stdout.strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sbs", default=os.environ.get("SBS"), help="SBS directory (or env SBS)")
    ap.add_argument("--tax", default=os.environ.get("TAX"), help="taxonomy root 000-099_S-ATLAS (or env TAX)")
    ap.add_argument("--base", default=None, help="reference commit; default merge-base with origin/main")
    ap.add_argument("--repo", default=".")
    a = ap.parse_args()
    if not a.sbs or not Path(a.sbs).is_dir(): sys.exit("usage: --sbs <dir> (or export SBS) - directory not found")
    repo = Path(a.repo).resolve(); sbs = Path(a.sbs).resolve()
    tax = Path(a.tax).resolve() if a.tax and Path(a.tax).is_dir() else None
    rows, fails = [], 0
    def check(name, expected, actual, ok):
        nonlocal fails
        rows.append((name, expected, actual, "PASS" if ok else "FAIL")); fails += 0 if ok else 1
    def info(name, value): rows.append((name, "-", value, "INFO"))

    # A - git scope: committed diff + working tree + untracked, against protected areas
    base = a.base or sh("git", "merge-base", "origin/main", "HEAD", cwd=repo) or "HEAD"
    changed = set(sh("git", "diff", "--name-only", base, cwd=repo).splitlines())            # committed + working tree vs base
    changed |= set(sh("git", "ls-files", "--others", "--exclude-standard", cwd=repo).splitlines())  # untracked
    changed.discard("")
    prot = sorted(f for f in changed if any(p in f for p in PROTECTED) or f.lower().endswith(PROTECTED_EXT))
    check("protected areas untouched (PBS, BWB-Q100, taxonomy, binaries)", 0, len(prot), not prot)
    for f in prot[:8]: info("  protected file touched", f)
    stage_dirs = sorted(f for f in changed if re.search(r"/(?:LCS-[A-N]|LC-[A-N])/", "/" + f))
    check("no lifecycle-stage directories created in this PR", 0, len(stage_dirs), not stage_dirs)
    info("reference commit", base[:12])

    # B - YAML validity across the SBS
    bad = []
    for f in glob.glob(str(sbs / "**" / "*.y*ml"), recursive=True):
        try: yaml.safe_load(open(f, encoding="utf-8"))
        except Exception as e: bad.append((os.path.relpath(f, sbs), str(e).splitlines()[0][:70]))
    check("YAML files parse", 0, len(bad), not bad)
    for f, e in bad[:6]: info("  invalid", f"{f}: {e}")

    # C - placeholders and ghost codes: active files fail, historical citations are counted only
    def scan(rx):
        act, hist = [], []
        for f in glob.glob(str(sbs / "**" / "*"), recursive=True):
            if not os.path.isfile(f) or not f.endswith((".md", ".yaml", ".yml", ".txt")): continue
            rel = os.path.relpath(f, sbs)
            try: txt = open(f, encoding="utf-8", errors="ignore").read()
            except Exception: continue
            n = len(rx.findall(txt))
            if n: (hist if any(h in rel for h in HISTORICAL) else act).append((rel, n))
        return act, hist
    act, hist = scan(re.compile(r"10-10-10-10"))
    check("placeholder ids 10-10-10-10 (active files)", 0, sum(n for _, n in act), not act)
    info("placeholder ids in historical documents", sum(n for _, n in hist))
    act, hist = scan(re.compile(r"eWTW-PBS-10\b"))
    check("ghost code eWTW-PBS-10 (active files)", 0, sum(n for _, n in act), not act)
    for f, n in act[:6]: info("  ghost code in", f"{f} x{n}")
    info("ghost code in historical documents", sum(n for _, n in hist))

    # D - typed references in YAML and MD under the SBS
    pbs_ids, pns, taxes, files, tbd = set(), set(), set(), [], 0
    for f in glob.glob(str(sbs / "**" / "*"), recursive=True):
        if not os.path.isfile(f) or not f.endswith((".md", ".yaml", ".yml")): continue
        if "01-01_PBS_Product-Breakdown" in f: continue                     # the PBS is the referent, not a referrer
        try: txt = open(f, encoding="utf-8", errors="ignore").read()
        except Exception: continue
        pbs_ids |= set(RX_PBS.findall(txt)); pns |= set(RX_PN.findall(txt)); taxes |= set(RX_TAX.findall(txt))
        tbd += len(re.findall(r":\s*TBD\b", txt))
        for m in RX_FILEKEY.findall(txt): files.append((Path(f).parent, m))
    def dir_exists(root, prefix):
        return any(os.path.isdir(p) for p in glob.glob(str(root / "**" / f"{prefix}_*"), recursive=True))
    # chapter/section short forms (eWTW-PBS-053, eWTW-PBS-053-100) alias the -000 node of that grain (CM-002 3, ruling)
    def resolve_pbs(i):
        if dir_exists(sbs, i): return "direct"
        if i.count("-") in (2, 3) and dir_exists(sbs, i + "-000"): return "alias"
        return None
    res = {i: resolve_pbs(i) for i in pbs_ids}
    d_pbs = sorted(i for i, r in res.items() if r is None)
    check("PBS ids resolve to a PBS node directory (short forms alias the -000 node)", 0, len(d_pbs), not d_pbs)
    info("PBS ids resolved via chapter/section alias", sum(1 for r in res.values() if r == "alias"))
    for i in d_pbs[:6]: info("  dangling PBS id", i + ("  (short form: section ids end with -000)" if i.count("-") == 3 else ""))
    d_pn = []
    for pn in sorted(pns):
        hits = [p for p in glob.glob(str(sbs / "**" / f"{pn}_*"), recursive=True) if os.path.isdir(p)]
        if not hits: d_pn.append((pn, "no node")); continue
        py = Path(hits[0]) / "part.yaml"
        if not py.is_file(): d_pn.append((pn, "no part.yaml")); continue
        try: declared = str((yaml.safe_load(open(py, encoding="utf-8")) or {}).get("part", {}).get("pn", ""))
        except Exception: declared = "?"
        if declared != pn: d_pn.append((pn, f"part.yaml pn={declared!r}"))
    check("part numbers resolve to a node whose part.yaml agrees", 0, len(d_pn), not d_pn)
    for pn, why in d_pn[:6]: info("  part number", f"{pn}: {why}")
    if tax:
        d_tax = sorted(t for t in taxes if not dir_exists(tax, t))
        check("taxonomy addresses resolve under S-ATLAS", 0, len(d_tax), not d_tax)
        for t in d_tax[:6]: info("  dangling taxonomy address", t)
    else:
        info("taxonomy addresses found (not validated: --tax not given)", len(taxes))
    def node_root(d):                      # nearest ancestor that is a product node (PN folder)
        for anc in [d, *d.parents]:
            if re.fullmatch(r"EWTW-\d{6}-\d{3}_.*", anc.name): return anc
        return None
    def ref_ok(base_, m):
        nr = node_root(base_)
        return any(x for x in ((base_ / m), (sbs / m), (repo / m), (nr / m) if nr else None) if x and x.exists())
    d_files = sorted({m for base_, m in files if not ref_ok(base_, m)})
    check("declared file references exist", 0, len(d_files), not d_files)
    for m in d_files[:6]: info("  missing file", m)
    info("TBD references (unassigned, counted separately)", tbd)

    # E - self-claims
    sc = [os.path.relpath(f, sbs) for f in glob.glob(str(sbs / "**" / "*.y*ml"), recursive=True)
          if "compliant" in open(f, encoding="utf-8", errors="ignore").read()]
    check("no conformity self-claims in YAML", 0, len(sc), not sc)

    w = max(len(r[0]) for r in rows)
    print(f"sbs_validate 0.1.2 | SBS={sbs.relative_to(repo) if str(sbs).startswith(str(repo)) else sbs}")
    for name, exp, act_, res in rows:
        print(f"[{res:4}] {name:<{w}}  expected {exp!s:<4} actual {act_}")
    print(f"\n{'RESULT: PASS' if not fails else f'RESULT: FAIL ({fails} failing check(s))'}")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
