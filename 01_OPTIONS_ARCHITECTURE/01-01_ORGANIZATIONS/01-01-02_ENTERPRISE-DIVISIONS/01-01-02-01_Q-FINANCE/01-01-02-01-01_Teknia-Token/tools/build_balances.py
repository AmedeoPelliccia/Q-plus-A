#!/usr/bin/env python3
"""build_balances.py — derive per-member balances from the emissions SSOT.

Usage:
    python3 build_balances.py [--root .] [--check]

Writes TT-LEDGER/derived/balances.yaml and TT-LEDGER/derived/balances.md.
Both outputs are GENERATED — never hand-edit. Deterministic ordering
(memberId ascending). With --check, regenerates to memory and diffs against
the committed derived files; exits 1 if they are stale.

No-AAA compliant.
"""

import argparse
import sys
from pathlib import Path

import yaml

GENERATED_HEADER = "# GENERATED — never hand-edit\n"


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def compute_balances(emissions):
    balances = {}
    for row in emissions or []:
        member = str(row.get("memberId"))
        pool = str(row.get("poolId"))
        amount = row.get("amount") or 0
        raw_date = str(row.get("date"))
        entry = balances.setdefault(
            member, {"total": 0, "pools": {}, "lastEmissionDate": ""})
        entry["total"] += amount
        entry["pools"][pool] = entry["pools"].get(pool, 0) + amount
        if raw_date > entry["lastEmissionDate"]:
            entry["lastEmissionDate"] = raw_date
    return balances


def render_yaml(balances):
    members = []
    for member in sorted(balances):
        entry = balances[member]
        members.append({
            "memberId": member,
            "total": entry["total"],
            "pools": {pid: entry["pools"][pid] for pid in sorted(entry["pools"])},
            "lastEmissionDate": entry["lastEmissionDate"],
        })
    body = yaml.safe_dump(
        {"balances": members}, sort_keys=False, default_flow_style=False)
    return GENERATED_HEADER + "# Derived from TT-LEDGER/emissions.yaml\n" + body


def render_md(balances):
    lines = [
        "<!-- GENERATED — never hand-edit -->",
        "",
        "# Teknia Token balances (derived)",
        "",
        "| memberId | total TT | per-pool breakdown | last emission date |",
        "| --- | --- | --- | --- |",
    ]
    if not balances:
        lines.append("| _none_ | 0 | — | — |")
    for member in sorted(balances):
        entry = balances[member]
        breakdown = "; ".join(
            "%s: %d" % (pid, entry["pools"][pid])
            for pid in sorted(entry["pools"])) or "—"
        lines.append("| %s | %d | %s | %s |" % (
            member, entry["total"], breakdown,
            entry["lastEmissionDate"] or "—"))
    lines += ["", "No-AAA compliant.", ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", default=str(Path(__file__).resolve().parent.parent),
        help="Teknia-Token node root containing TT-LEDGER/")
    parser.add_argument(
        "--check", action="store_true",
        help="verify committed derived files are up to date; do not write")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="print outputs without writing")
    args = parser.parse_args(argv)

    root = Path(args.root)
    emissions_path = root / "TT-LEDGER" / "emissions.yaml"
    derived_dir = root / "TT-LEDGER" / "derived"
    yaml_path = derived_dir / "balances.yaml"
    md_path = derived_dir / "balances.md"

    doc = load_yaml(emissions_path) or {}
    balances = compute_balances(doc.get("emissions"))
    yaml_out = render_yaml(balances)
    md_out = render_md(balances)

    if args.check:
        stale = []
        for path, expected in ((yaml_path, yaml_out), (md_path, md_out)):
            actual = path.read_text(encoding="utf-8") if path.is_file() else None
            if actual != expected:
                stale.append(str(path))
        if stale:
            print("STALE derived files (regenerate with build_balances.py):")
            for path in stale:
                print("  %s" % path)
            return 1
        print("derived balances up to date")
        return 0

    if args.dry_run:
        print(yaml_out)
        print(md_out)
        return 0

    derived_dir.mkdir(parents=True, exist_ok=True)
    yaml_path.write_text(yaml_out, encoding="utf-8")
    md_path.write_text(md_out, encoding="utf-8")
    print("wrote %s" % yaml_path)
    print("wrote %s" % md_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
