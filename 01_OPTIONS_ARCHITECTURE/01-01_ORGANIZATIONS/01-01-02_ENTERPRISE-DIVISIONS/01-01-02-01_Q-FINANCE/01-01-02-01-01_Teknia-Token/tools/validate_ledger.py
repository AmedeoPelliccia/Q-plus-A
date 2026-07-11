#!/usr/bin/env python3
"""validate_ledger.py — Teknia Token (TT) ledger validator.

Deterministic validation of the authored ledger SSOT:
    <node>/TT-LEDGER/pools.yaml
    <node>/TT-LEDGER/emissions.yaml

Contract:
  * --root points at the TT node directory (the one containing TT-LEDGER/).
    Default: current working directory. In CI, pass --root "$TT_NODE".
  * The team register is resolved by upward search from --root for
    01_OPTIONS_ARCHITECTURE/01-01_ORGANIZATIONS/TEAM-REGISTER.csv,
    or explicitly via --register.
  * main(argv) RETURNS an int (0 ok, 1 violations); sys.exit lives only
    in the __main__ guard. All findings are collected — no early exit.
  * --strict promotes WARNINGs to VIOLATIONs (non-OPEN pool emissions,
    missing team register).

Emission event vocabulary:
    EVENTS — TODO: bind to the GQAOA-QFIN-TT-KLT-001 four-event grammar
    at merge review.
"""

from __future__ import annotations

import argparse
import csv
import datetime as _dt
import re
import sys
from pathlib import Path

import yaml

EVENTS = ["QUOTED", "ASSIGNED", "ACCEPTED", "RELEASED"]
POOL_STATUS = ["PROPOSED", "OPEN", "CLOSED"]
HASH_RE = re.compile(r"^[0-9a-f]{64}$")
WP_RE = re.compile(r"#\d+")
DATE_FMT = "YYYY-MM-DD"

POOL_REQUIRED = ("id", "title", "amount", "status")
EMISSION_REQUIRED = ("id", "memberId", "poolId", "workPackage",
                     "amount", "event", "evidenceHash", "date")

REGISTER_REL = Path("01_OPTIONS_ARCHITECTURE") / "01-01_ORGANIZATIONS" \
    / "TEAM-REGISTER.csv"


class Findings:
    """Ordered collection of violations and warnings."""

    def __init__(self) -> None:
        self.violations: list[str] = []
        self.warnings: list[str] = []

    def violation(self, msg: str) -> None:
        self.violations.append(msg)

    def warning(self, msg: str) -> None:
        self.warnings.append(msg)


# ---------------------------------------------------------------- loading

def _load_yaml(path: Path, key: str, f: Findings):
    if not path.is_file():
        f.violation(f"{path.name}: file not found at {path}")
        return None
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        f.violation(f"{path.name}: YAML parse error: {exc}")
        return None
    if not isinstance(data, dict) or key not in data:
        f.violation(f"{path.name}: top-level key '{key}' missing")
        return None
    if data[key] is None:
        return []
    if not isinstance(data[key], list):
        f.violation(f"{path.name}: '{key}' must be a list")
        return None
    return data[key]


def _resolve_register(root: Path, explicit: str | None) -> Path | None:
    if explicit:
        p = Path(explicit)
        return p if p.is_file() else None
    for anchor in (root, *root.resolve().parents):
        candidate = anchor / REGISTER_REL
        if candidate.is_file():
            return candidate
    return None


def _load_members(register: Path, f: Findings) -> set[str] | None:
    try:
        with register.open(encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            if not reader.fieldnames:
                f.violation(f"TEAM-REGISTER: empty register at {register}")
                return None
            col = "memberId" if "memberId" in reader.fieldnames \
                else reader.fieldnames[0]
            return {row[col].strip() for row in reader if row.get(col)}
    except (OSError, csv.Error) as exc:
        f.violation(f"TEAM-REGISTER: cannot read {register}: {exc}")
        return None


# ---------------------------------------------------------------- checks

def _check_pools(pools: list, f: Findings) -> dict[str, dict]:
    by_id: dict[str, dict] = {}
    for i, pool in enumerate(pools):
        ctx = f"pools[{i}]"
        if not isinstance(pool, dict):
            f.violation(f"{ctx}: entry must be a mapping")
            continue
        missing = [k for k in POOL_REQUIRED if k not in pool]
        if missing:
            f.violation(f"{ctx}: missing required keys {missing}")
            continue
        pid = pool["id"]
        ctx = f"pool {pid}"
        if pid in by_id:
            f.violation(f"{ctx}: duplicate pool id")
            continue
        by_id[pid] = pool
        if not isinstance(pool["amount"], int) \
                or isinstance(pool["amount"], bool) or pool["amount"] < 0:
            f.violation(f"{ctx}: amount must be a non-negative integer")
        if pool["status"] not in POOL_STATUS:
            f.violation(f"{ctx}: status '{pool['status']}' not in "
                        f"{POOL_STATUS}")
    for pid, pool in by_id.items():
        rev = pool.get("reviewerPoolId")
        if rev is not None and rev not in by_id:
            f.violation(f"pool {pid}: reviewerPoolId '{rev}' does not exist")
    return by_id


def _check_emissions(emissions: list, pools: dict[str, dict],
                     members: set[str] | None, register_found: bool,
                     f: Findings) -> dict[str, int]:
    per_pool: dict[str, int] = {}
    seen: set[str] = set()
    for i, em in enumerate(emissions):
        ctx = f"emissions[{i}]"
        if not isinstance(em, dict):
            f.violation(f"{ctx}: entry must be a mapping")
            continue
        missing = [k for k in EMISSION_REQUIRED if k not in em]
        if missing:
            f.violation(f"{ctx}: missing required keys {missing}")
            continue
        eid = em["id"]
        ctx = f"emission {eid}"
        if eid in seen:
            f.violation(f"{ctx}: duplicate emission id")
            continue
        seen.add(eid)

        if not isinstance(em["amount"], int) \
                or isinstance(em["amount"], bool) or em["amount"] <= 0:
            f.violation(f"{ctx}: amount must be a positive integer")
        if not isinstance(em["evidenceHash"], str) \
                or not HASH_RE.fullmatch(em["evidenceHash"]):
            f.violation(f"{ctx}: evidenceHash must be a 64-hex sha256")
        if em["event"] not in EVENTS:
            f.violation(f"{ctx}: event '{em['event']}' not in {EVENTS}")
        if not isinstance(em["workPackage"], str) \
                or not WP_RE.search(em["workPackage"]):
            f.violation(f"{ctx}: workPackage must reference an issue "
                        f"('... #<n>')")
        try:
            _dt.date.fromisoformat(str(em["date"]))
        except ValueError:
            f.violation(f"{ctx}: date must be ISO {DATE_FMT}")

        pid = em["poolId"]
        pool = pools.get(pid)
        if pool is None:
            f.violation(f"{ctx}: poolId '{pid}' does not exist")
        else:
            if isinstance(em["amount"], int) \
                    and not isinstance(em["amount"], bool) and em["amount"] > 0:
                per_pool[pid] = per_pool.get(pid, 0) + em["amount"]
            if pool.get("status") != "OPEN":
                f.warning(f"{ctx}: emission against pool '{pid}' with "
                          f"status '{pool.get('status')}' (not OPEN)")

        member = em["memberId"]
        if members is not None:
            if member not in members:
                f.violation(f"{ctx}: memberId '{member}' not found in "
                            f"TEAM-REGISTER.csv")
        elif not register_found:
            pass  # register absence reported once, globally
    for pid, total in sorted(per_pool.items()):
        pool = pools.get(pid)
        if pool and isinstance(pool.get("amount"), int) \
                and total > pool["amount"]:
            f.violation(f"pool {pid}: emitted total {total} exceeds pool "
                        f"amount {pool['amount']}")
    return per_pool


# ---------------------------------------------------------------- main

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Validate the Teknia Token ledger SSOT.")
    ap.add_argument("--root", default=".",
                    help="TT node directory containing TT-LEDGER/ "
                         "(default: cwd)")
    ap.add_argument("--register", default=None,
                    help="Explicit path to TEAM-REGISTER.csv "
                         "(default: upward search from --root)")
    ap.add_argument("--strict", action="store_true",
                    help="Promote warnings to violations")
    args = ap.parse_args(argv)

    root = Path(args.root)
    ledger = root / "TT-LEDGER"
    f = Findings()

    pools_raw = _load_yaml(ledger / "pools.yaml", "pools", f)
    emissions_raw = _load_yaml(ledger / "emissions.yaml", "emissions", f)

    register = _resolve_register(root, args.register)
    members: set[str] | None = None
    if register is None:
        f.warning("TEAM-REGISTER.csv not found (searched upward from "
                  f"--root for {REGISTER_REL}); member check skipped")
    else:
        members = _load_members(register, f)

    pools: dict[str, dict] = {}
    per_pool: dict[str, int] = {}
    if pools_raw is not None:
        pools = _check_pools(pools_raw, f)
    if emissions_raw is not None:
        per_pool = _check_emissions(emissions_raw, pools, members,
                                    register is not None, f)

    if args.strict:
        f.violations.extend(f"[strict] {w}" for w in f.warnings)
        f.warnings = []

    # ---- report ----
    print("TT LEDGER VALIDATION")
    print(f"  root:      {root}")
    print(f"  register:  {register if register else 'NOT FOUND'}")
    print(f"  pools:     {len(pools)}")
    n_em = len(emissions_raw) if isinstance(emissions_raw, list) else 0
    print(f"  emissions: {n_em}")
    for pid in sorted(pools):
        amount = pools[pid].get("amount", 0)
        used = per_pool.get(pid, 0)
        print(f"    {pid}: {used}/{amount} TT "
              f"[{pools[pid].get('status')}]")
    for w in f.warnings:
        print(f"WARNING: {w}")
    for v in f.violations:
        print(f"VIOLATION: {v}")
    if f.violations:
        print(f"RESULT: FAIL ({len(f.violations)} violation"
              f"{'s' if len(f.violations) != 1 else ''})")
        return 1
    print("RESULT: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
