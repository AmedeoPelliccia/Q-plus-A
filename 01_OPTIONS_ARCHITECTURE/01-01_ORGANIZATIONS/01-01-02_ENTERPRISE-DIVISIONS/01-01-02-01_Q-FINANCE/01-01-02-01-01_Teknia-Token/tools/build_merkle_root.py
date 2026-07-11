#!/usr/bin/env python3
"""build_merkle_root.py — deterministic Merkle root over the emissions ledger.

Canonical serialization: emissions rows sorted by 'id'; each row encoded as
json.dumps(..., sort_keys=True) UTF-8 with a STRICT encoder (str, int, bool,
None, list, dict; dates as ISO strings; any other type fails loudly);
sha256 per row as leaves; binary Merkle tree duplicating the last leaf on
odd counts. Empty ledger -> EMPTY_ROOT sentinel (sha256 of empty bytes).

Anchoring (--anchor): appends one line to <node>/TT-LEDGER/anchors.log —
an APPEND-ONLY EVIDENCE FILE, deliberately outside derived/ (derived files
are regenerable; anchor history is not):

    <utc-iso-timestamp>, <merkle_root>, <sha256(emissions.yaml)>, <ledgerRef>

ledgerRef defaults to the short git commit of --root (fallback "-") and is
the reference carried on-chain by TekniaLedgerAnchor.anchor(). Re-anchoring
an unchanged state is a no-op (duplicate guard).

Contract (aligned with the node suite): --root is the TT node directory
containing TT-LEDGER/ (default: cwd; in CI pass --root "$TT_NODE");
main(argv) RETURNS an int; sys.exit lives only in the __main__ guard.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml

EMPTY_ROOT = hashlib.sha256(b"").hexdigest()  # sentinel: root of empty ledger
LOG_HEADER = ("# TT ledger anchors — append-only evidence log; "
              "never edit or regenerate\n"
              "# utc_timestamp, merkle_root, emissions_sha256, ledger_ref\n")


def _canonical(value, ctx: str):
    """Strict canonical form: fail loudly on unexpected types."""
    if value is None or isinstance(value, (str, int, bool)):
        return value
    if isinstance(value, (_dt.date, _dt.datetime)):
        return value.isoformat()
    if isinstance(value, list):
        return [_canonical(v, ctx) for v in value]
    if isinstance(value, dict):
        return {str(k): _canonical(v, ctx) for k, v in value.items()}
    raise TypeError(f"{ctx}: unsupported type {type(value).__name__} "
                    f"in canonical serialization")


def canonical_leaves(emissions: list) -> list[bytes]:
    rows = sorted(emissions or [], key=lambda row: str(row.get("id")))
    leaves = []
    for row in rows:
        ctx = f"emission {row.get('id')}"
        blob = json.dumps(_canonical(row, ctx), sort_keys=True,
                          separators=(",", ":")).encode("utf-8")
        leaves.append(hashlib.sha256(blob).digest())
    return leaves


def merkle_root(leaves: list[bytes]) -> str:
    if not leaves:
        return EMPTY_ROOT
    level = list(leaves)
    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])
        level = [hashlib.sha256(level[i] + level[i + 1]).digest()
                 for i in range(0, len(level), 2)]
    return level[0].hex()


def _git_ref(root: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=5)
        ref = out.stdout.strip()
        return ref if out.returncode == 0 and ref else "-"
    except (OSError, subprocess.SubprocessError):
        return "-"


def _last_anchor(log_path: Path) -> tuple[str, str] | None:
    if not log_path.is_file():
        return None
    last = None
    for line in log_path.read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            last = line
    if not last:
        return None
    parts = [p.strip() for p in last.split(",")]
    return (parts[1], parts[2]) if len(parts) >= 3 else None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".",
                    help="TT node directory containing TT-LEDGER/ "
                         "(default: cwd)")
    ap.add_argument("--anchor", action="store_true",
                    help="append timestamp, root, file hash and ledger ref "
                         "to TT-LEDGER/anchors.log")
    ap.add_argument("--ref", default=None,
                    help="ledger reference for the anchor line "
                         "(default: short git commit of --root, else '-')")
    args = ap.parse_args(argv)

    root_dir = Path(args.root)
    emissions_path = root_dir / "TT-LEDGER" / "emissions.yaml"
    if not emissions_path.is_file():
        print(f"ERROR: {emissions_path} not found", file=sys.stderr)
        return 1

    try:
        doc = yaml.safe_load(emissions_path.read_text(encoding="utf-8")) or {}
        leaves = canonical_leaves(doc.get("emissions"))
    except (yaml.YAMLError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    root = merkle_root(leaves)
    print(root)

    if args.anchor:
        file_hash = hashlib.sha256(emissions_path.read_bytes()).hexdigest()
        log_path = root_dir / "TT-LEDGER" / "anchors.log"
        if _last_anchor(log_path) == (root, file_hash):
            print(f"state already anchored in {log_path} — no append")
            return 0
        ref = args.ref if args.ref else _git_ref(root_dir)
        stamp = _dt.datetime.now(_dt.timezone.utc) \
            .replace(microsecond=0).isoformat()
        log_path.parent.mkdir(parents=True, exist_ok=True)
        new_file = not log_path.is_file()
        with open(log_path, "a", encoding="utf-8") as fh:
            if new_file:
                fh.write(LOG_HEADER)
            fh.write(f"{stamp}, {root}, {file_hash}, {ref}\n")
        print(f"anchored to {log_path} (ref {ref})")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
