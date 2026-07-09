"""Pytest tests for validate_ledger.py — self-contained fixtures in tmp_path.

No-AAA compliant.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import validate_ledger  # noqa: E402

GOOD_HASH = "a" * 64

SEED_POOLS = """\
pools:
  - id: "POOL-GENESIS-ARCHITECTURE"
    title: "Retroactive founding architecture work"
    amount: 0
    reserved: true
    status: "PROPOSED"
    reviewerPoolId: "POOL-REVIEW-GENESIS"
  - id: "POOL-REVIEW-GENESIS"
    title: "Independent review of genesis work packages"
    amount: 0
    reserved: true
    status: "PROPOSED"
    reviewerPoolId: null
"""

SEED_EMISSIONS = "emissions: []\n"

BAD_POOLS = """\
pools:
  - id: "POOL-OPEN"
    title: "Open pool with a small budget"
    amount: 5
    reserved: true
    status: "OPEN"
    reviewerPoolId: null
"""

BAD_EMISSIONS = """\
emissions:
  - id: "EM-0001"
    memberId: "AmedeoPelliccia"
    poolId: "POOL-OPEN"
    workPackage: "WP: #1"
    amount: 10
    event: "ACCEPTED"
    evidenceHash: "not-a-sha256"
    date: "2026-07-09"
"""

REGISTER = "memberId\nAmedeoPelliccia\n"


def write_node(tmp_path, pools, emissions, register=REGISTER):
    node = tmp_path / "node"
    ledger = node / "TT-LEDGER"
    ledger.mkdir(parents=True)
    (ledger / "pools.yaml").write_text(pools, encoding="utf-8")
    (ledger / "emissions.yaml").write_text(emissions, encoding="utf-8")
    if register is not None:
        org = tmp_path / "01_OPTIONS_ARCHITECTURE" / "01-01_ORGANIZATIONS"
        org.mkdir(parents=True)
        (org / "TEAM-REGISTER.csv").write_text(register, encoding="utf-8")
    return node


def test_seed_ledger_validates(tmp_path, capsys):
    node = write_node(tmp_path, SEED_POOLS, SEED_EMISSIONS)
    rc = validate_ledger.main(["--root", str(node), "--strict"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "RESULT: OK" in out


def test_bad_hash_and_over_budget_pool_fail(tmp_path, capsys):
    node = write_node(tmp_path, BAD_POOLS, BAD_EMISSIONS)
    rc = validate_ledger.main(["--root", str(node), "--strict"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "evidenceHash" in out
    assert "exceeds pool amount" in out


def test_unknown_member_fails_when_register_present(tmp_path):
    emissions = BAD_EMISSIONS.replace("not-a-sha256", GOOD_HASH).replace(
        "AmedeoPelliccia", "GhostContributor")
    node = write_node(tmp_path, BAD_POOLS.replace("amount: 5", "amount: 100"),
                      emissions)
    rc = validate_ledger.main(["--root", str(node), "--strict"])
    assert rc == 1


def test_non_open_pool_warns_without_strict(tmp_path, capsys):
    pools = BAD_POOLS.replace('status: "OPEN"', 'status: "PROPOSED"').replace(
        "amount: 5", "amount: 100")
    emissions = BAD_EMISSIONS.replace("not-a-sha256", GOOD_HASH)
    node = write_node(tmp_path, pools, emissions)
    rc = validate_ledger.main(["--root", str(node)])
    out = capsys.readouterr().out
    assert rc == 0
    assert "WARNING" in out
    rc_strict = validate_ledger.main(["--root", str(node), "--strict"])
    assert rc_strict == 1
