#!/usr/bin/env python3
"""validate_ledger.py — deterministic validation of the Teknia Token ledger SSOT.

Usage:
    python3 validate_ledger.py [--root .] [--strict]

Validates TT-LEDGER/pools.yaml and TT-LEDGER/emissions.yaml under --root
(default: the Teknia-Token node containing this tools/ directory).

Exit codes: 0 = valid, 1 = violations found.

No-AAA compliant.
"""

import argparse
import csv
import re
import sys
from datetime import date as _date
from pathlib import Path

import yaml

EVENTS = ["QUOTED", "ASSIGNED", "ACCEPTED", "RELEASED"]
EVIDENCE_RE = re.compile(r"^[0-9a-f]{64}$")
POOL_STATUSES = ["PROPOSED", "OPEN", "CLOSED"]

POOL_REQUIRED = ["id", "title", "amount", "reserved", "status", "reviewerPoolId"]
EMISSION_REQUIRED = [
    "id", "memberId", "poolId", "workPackage", "amount",
    "event", "evidenceHash", "date",
]

REGISTER_CANDIDATES = ["TEAM-REGISTER.csv", "TEAM-MEMBERS.csv"]
REGISTER_COLUMNS = ["memberId", "github_username", "member_id"]


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find_register(root):
    """Search upward from root for the organizations team register."""
    root = Path(root).resolve()
    for base in [root] + list(root.parents):
        org = base / "01_OPTIONS_ARCHITECTURE" / "01-01_ORGANIZATIONS"
        for name in REGISTER_CANDIDATES:
            candidate = org / name
            if candidate.is_file():
                return candidate
        for name in REGISTER_CANDIDATES:
            candidate = base / name
            if candidate.is_file():
                return candidate
    return None


def load_members(register_path):
    members = set()
    with open(register_path, "r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            for col in REGISTER_COLUMNS:
                value = (row.get(col) or "").strip()
                if value:
                    members.add(value)
    return members


def validate(pools_doc, emissions_doc, members, strict=False):
    """Return (violations, warnings) as lists of strings."""
    violations = []
    warnings = []

    pools = (pools_doc or {}).get("pools")
    if not isinstance(pools, list):
        return (["pools.yaml: missing or invalid 'pools' list"], warnings)
    emissions = (emissions_doc or {}).get("emissions")
    if not isinstance(emissions, list):
        return (["emissions.yaml: missing or invalid 'emissions' list"], warnings)

    pool_by_id = {}
    for idx, pool in enumerate(pools):
        label = "pools[%d]" % idx
        if not isinstance(pool, dict):
            violations.append("%s: not a mapping" % label)
            continue
        for key in POOL_REQUIRED:
            if key not in pool:
                violations.append("%s: missing key '%s'" % (label, key))
        pid = pool.get("id")
        if pid:
            if pid in pool_by_id:
                violations.append("%s: duplicate pool id '%s'" % (label, pid))
            else:
                pool_by_id[pid] = pool
        amount = pool.get("amount")
        if not isinstance(amount, int) or isinstance(amount, bool) or amount < 0:
            violations.append("%s: 'amount' must be a non-negative integer" % label)
        status = pool.get("status")
        if status not in POOL_STATUSES:
            violations.append(
                "%s: 'status' must be one of %s" % (label, POOL_STATUSES))

    for pid, pool in sorted(pool_by_id.items()):
        rid = pool.get("reviewerPoolId")
        if rid is not None and rid not in pool_by_id:
            violations.append(
                "pool '%s': reviewerPoolId '%s' does not exist" % (pid, rid))

    emitted = {}
    seen_ids = set()
    for idx, row in enumerate(emissions):
        label = "emissions[%d]" % idx
        if not isinstance(row, dict):
            violations.append("%s: not a mapping" % label)
            continue
        for key in EMISSION_REQUIRED:
            if key not in row:
                violations.append("%s: missing key '%s'" % (label, key))
        eid = row.get("id")
        if eid:
            label = "emission '%s'" % eid
            if eid in seen_ids:
                violations.append("%s: duplicate emission id" % label)
            seen_ids.add(eid)
        pid = row.get("poolId")
        if pid not in pool_by_id:
            violations.append("%s: poolId '%s' does not exist" % (label, pid))
        else:
            status = pool_by_id[pid].get("status")
            if status != "OPEN":
                message = ("%s: pool '%s' has status '%s' (emissions require "
                           "status OPEN)" % (label, pid, status))
                if strict:
                    violations.append(message)
                else:
                    warnings.append(message)
        amount = row.get("amount")
        if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
            violations.append("%s: 'amount' must be a positive integer" % label)
        elif pid in pool_by_id:
            emitted[pid] = emitted.get(pid, 0) + amount
        event = row.get("event")
        if event not in EVENTS:
            violations.append("%s: 'event' must be one of %s" % (label, EVENTS))
        evidence = row.get("evidenceHash")
        if not isinstance(evidence, str) or not EVIDENCE_RE.match(evidence):
            violations.append(
                "%s: 'evidenceHash' must match ^[0-9a-f]{64}$" % label)
        raw_date = row.get("date")
        if isinstance(raw_date, _date):
            pass
        else:
            try:
                _date.fromisoformat(str(raw_date))
            except (TypeError, ValueError):
                violations.append("%s: 'date' must be ISO YYYY-MM-DD" % label)
        member = row.get("memberId")
        if members is None:
            warnings.append(
                "%s: team register missing — cannot verify memberId '%s'"
                % (label, member))
        elif member not in members:
            violations.append(
                "%s: memberId '%s' not present in team register" % (label, member))

    for pid, total in sorted(emitted.items()):
        cap = pool_by_id[pid].get("amount")
        if isinstance(cap, int) and not isinstance(cap, bool) and total > cap:
            violations.append(
                "pool '%s': emitted total %d exceeds pool amount %d"
                % (pid, total, cap))

    return violations, warnings


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", default=str(Path(__file__).resolve().parent.parent),
        help="Teknia-Token node root containing TT-LEDGER/")
    parser.add_argument(
        "--strict", action="store_true",
        help="treat emissions against non-OPEN pools as violations")
    args = parser.parse_args(argv)

    root = Path(args.root)
    pools_path = root / "TT-LEDGER" / "pools.yaml"
    emissions_path = root / "TT-LEDGER" / "emissions.yaml"
    for path in (pools_path, emissions_path):
        if not path.is_file():
            print("ERROR: missing %s" % path)
            return 1

    pools_doc = load_yaml(pools_path)
    emissions_doc = load_yaml(emissions_path)

    register = find_register(root)
    members = load_members(register) if register else None
    if register is None:
        print("WARNING: team register not found (searched %s)"
              % ", ".join(REGISTER_CANDIDATES))

    violations, warnings = validate(
        pools_doc, emissions_doc, members, strict=args.strict)

    pools = (pools_doc or {}).get("pools") or []
    emissions = (emissions_doc or {}).get("emissions") or []
    print("TT ledger validation summary")
    print("----------------------------")
    print("%-12s %d" % ("pools:", len(pools) if isinstance(pools, list) else 0))
    print("%-12s %d" % ("emissions:",
                        len(emissions) if isinstance(emissions, list) else 0))
    print("%-12s %d" % ("warnings:", len(warnings)))
    print("%-12s %d" % ("violations:", len(violations)))
    for message in warnings:
        print("WARNING: %s" % message)
    for message in violations:
        print("VIOLATION: %s" % message)
    if violations:
        print("RESULT: FAIL")
        return 1
    print("RESULT: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
