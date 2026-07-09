#!/usr/bin/env python3
"""build_merkle_root.py — deterministic Merkle root over the emissions ledger.

Usage:
    python3 build_merkle_root.py [--root .] [--anchor]

Canonical serialization: emissions.yaml rows sorted by 'id', each serialized
with json.dumps(..., sort_keys=True) as utf-8; sha256 per row as leaves;
binary Merkle tree (duplicate last leaf on odd counts). Prints the root.
With --anchor, appends "date, merkle_root, sha256(emissions.yaml)" to
TT-LEDGER/derived/anchors.log.

No-AAA compliant.
"""

import argparse
import datetime
import hashlib
import json
import sys
from pathlib import Path

import yaml


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def canonical_leaves(emissions):
    rows = sorted(emissions or [], key=lambda row: str(row.get("id")))
    leaves = []
    for row in rows:
        blob = json.dumps(row, sort_keys=True, default=str).encode("utf-8")
        leaves.append(hashlib.sha256(blob).digest())
    return leaves


def merkle_root(leaves):
    if not leaves:
        return hashlib.sha256(b"").hexdigest()
    level = list(leaves)
    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])
        level = [
            hashlib.sha256(level[i] + level[i + 1]).digest()
            for i in range(0, len(level), 2)
        ]
    return level[0].hex()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", default=str(Path(__file__).resolve().parent.parent),
        help="Teknia-Token node root containing TT-LEDGER/")
    parser.add_argument(
        "--anchor", action="store_true",
        help="append date, merkle_root, sha256(emissions.yaml) to anchors.log")
    args = parser.parse_args(argv)

    root_dir = Path(args.root)
    emissions_path = root_dir / "TT-LEDGER" / "emissions.yaml"
    doc = load_yaml(emissions_path) or {}
    leaves = canonical_leaves(doc.get("emissions"))
    root = merkle_root(leaves)
    print(root)

    if args.anchor:
        file_hash = hashlib.sha256(emissions_path.read_bytes()).hexdigest()
        anchors_path = root_dir / "TT-LEDGER" / "derived" / "anchors.log"
        anchors_path.parent.mkdir(parents=True, exist_ok=True)
        today = datetime.date.today().isoformat()
        with open(anchors_path, "a", encoding="utf-8") as fh:
            fh.write("%s, %s, %s\n" % (today, root, file_hash))
        print("anchored to %s" % anchors_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
