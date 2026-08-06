#!/usr/bin/env python3
# =============================================================================
# reconcile_S-STA-dorsale.py
# Migration companion for the S-STA 100-104 populate scripts. Any previously
# pushed state is reconciled to the current generators: the expected tree is
# built in a temporary sim from the populate scripts sitting NEXT TO this
# file; the repository tree is diffed against it; stale generated folders
# get a git-rm plan. SAFE BY DESIGN: --plan (default) only prints; --apply
# executes; any stale folder containing files other than README.md is
# FLAGGED and never removed (possible hand-authored content).
# Usage, at repo root, with populate_S-STA-10*.py alongside:
#   python3 reconcile_S-STA-dorsale.py --repo . --plan
#   python3 reconcile_S-STA-dorsale.py --repo . --apply
# Then re-run the five populate scripts and commit once.
# =============================================================================
import argparse, subprocess, sys, tempfile
from pathlib import Path

CHAPTERS = ["100","101","102","103","104"]
BAND_REL = ("01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
            "100-199_S-STA/100-109_General-Space-Systems-Engineering-"
            "Assurance-and-Human-Support")

def expected_tree(scripts_dir: Path) -> dict:
    """chapter -> set of relative dir paths (sections and subjects)."""
    exp = {}
    with tempfile.TemporaryDirectory() as td:
        for ch in CHAPTERS:
            sp = scripts_dir / f"populate_S-STA-{ch}.py"
            if not sp.is_file():
                print(f"[warn] missing {sp.name}; chapter {ch} skipped")
                continue
            subprocess.run([sys.executable, str(sp), "--root", td,
                            "--bootstrap"], check=True,
                           stdout=subprocess.DEVNULL)
        base = Path(td) / BAND_REL
        for ch in CHAPTERS:
            cdirs = list(base.glob(f"{ch}_*"))
            if not cdirs: continue
            cdir = cdirs[0]
            exp[ch] = (cdir.name,
                       {str(p.relative_to(cdir)) for p in cdir.rglob("*")
                        if p.is_dir()})
    return exp

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--plan", action="store_true")
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    scripts_dir = Path(__file__).resolve().parent
    band = repo / BAND_REL
    if not band.is_dir():
        sys.exit(f"[error] band path not found under {repo}")
    exp = expected_tree(scripts_dir)
    plan, flags = [], []
    for ch, (cname, edirs) in exp.items():
        rdirs = list(band.glob(f"{ch}_*"))
        for rdir in rdirs:
            if rdir.name != cname:
                plan.append(("mv-chapter", str(rdir.relative_to(repo)), cname))
                continue
            actual = {str(p.relative_to(rdir)) for p in rdir.rglob("*")
                      if p.is_dir()}
            for stale in sorted(actual - edirs):
                # keep parents whose children are expected
                if any(e.startswith(stale + "/") or e == stale for e in edirs):
                    continue
                sp = rdir / stale
                extra = [f.name for f in sp.rglob("*")
                         if f.is_file() and f.name != "README.md"]
                if extra:
                    flags.append((str(sp.relative_to(repo)), extra))
                else:
                    plan.append(("rm", str(sp.relative_to(repo)), None))
    # collapse nested rm paths (keep top-most only)
    rms = sorted([p for op, p, _ in plan if op == "rm"])
    top = [p for p in rms if not any(p.startswith(q + "/") for q in rms if q != p)]
    print(f"# Reconciliation plan — {len(top)} stale folder(s), "
          f"{len(flags)} flagged, {sum(1 for o,_,_ in plan if o=='mv-chapter')} chapter rename(s)")
    for op, p, new in plan:
        if op == "mv-chapter":
            print(f"git mv '{p}' '{Path(p).parent / new}'")
    for p in top:
        print(f"git rm -r '{p}'")
    for p, extra in flags:
        print(f"# FLAGGED (hand-authored files, NOT touched): {p} -> {extra}")
    if a.apply and (top or any(o=='mv-chapter' for o,_,_ in plan)):
        for op, p, new in plan:
            if op == "mv-chapter":
                subprocess.run(["git", "mv", p, str(Path(p).parent / new)],
                               cwd=repo, check=True)
        import shutil
        for p in top:
            subprocess.run(["git", "rm", "-r", "-q", "--ignore-unmatch", p],
                           cwd=repo, check=True)
            full = repo / p
            if full.exists():          # untracked stale dir: safe fs removal
                shutil.rmtree(full)
        print("# applied. Now re-run the five populate scripts and commit once.")
    elif not a.apply:
        print("# plan only — nothing touched. Re-run with --apply to execute.")
    return 0

if __name__ == "__main__":
    sys.exit(main())