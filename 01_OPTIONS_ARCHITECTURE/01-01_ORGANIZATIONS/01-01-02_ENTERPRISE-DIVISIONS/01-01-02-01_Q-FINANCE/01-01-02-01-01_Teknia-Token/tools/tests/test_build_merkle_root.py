"""Pytest tests for build_merkle_root.py — algorithm pin, invariance, anchoring."""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import build_merkle_root as bmr  # noqa: E402

H = "c" * 64
ROW = ('{{id: "EM-{n:04d}", memberId: "Alice", poolId: "POOL-A", '
       'workPackage: "WP: #{n}", amount: {amt}, event: "ACCEPTED", '
       'evidenceHash: "' + H + '", date: "2026-07-0{d}"}}')


def make_node(tmp_path, body):
    node = tmp_path / "node"
    (node / "TT-LEDGER").mkdir(parents=True)
    (node / "TT-LEDGER" / "emissions.yaml").write_text(
        "emissions:\n" + body, "utf-8")
    return node


def rows(*specs):
    return "".join("  - " + ROW.format(n=n, amt=a, d=d) + "\n"
                   for n, a, d in specs)


def expected_root(dicts):
    # independent mini-implementation: cross-checks the module's algorithm
    leaves = [hashlib.sha256(json.dumps(r, sort_keys=True,
              separators=(",", ":")).encode()).digest()
              for r in sorted(dicts, key=lambda r: r["id"])]
    level = leaves
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        level = [hashlib.sha256(level[i] + level[i + 1]).digest()
                 for i in range(0, len(level), 2)]
    return level[0].hex()


def test_root_matches_independent_implementation_odd_leaves(tmp_path, capsys):
    node = make_node(tmp_path, rows((1, 7, 1), (2, 3, 2), (3, 5, 3)))
    assert bmr.main(["--root", str(node)]) == 0
    got = capsys.readouterr().out.strip()
    dicts = [{"id": f"EM-{n:04d}", "memberId": "Alice", "poolId": "POOL-A",
              "workPackage": f"WP: #{n}", "amount": a, "event": "ACCEPTED",
              "evidenceHash": H, "date": f"2026-07-0{d}"}
             for n, a, d in ((1, 7, 1), (2, 3, 2), (3, 5, 3))]
    assert got == expected_root(dicts)


def test_yaml_formatting_and_order_invariance(tmp_path, capsys):
    node_a = make_node(tmp_path / "a", rows((1, 7, 1), (2, 3, 2)))
    # same semantic rows: reversed order, keys shuffled, date unquoted
    shuffled = (
        '  - {amount: 3, id: "EM-0002", poolId: "POOL-A", '
        'memberId: "Alice", event: "ACCEPTED", workPackage: "WP: #2", '
        f'evidenceHash: "{H}", date: 2026-07-02}}\n'
        '  - {date: "2026-07-01", amount: 7, id: "EM-0001", '
        'memberId: "Alice", poolId: "POOL-A", event: "ACCEPTED", '
        f'workPackage: "WP: #1", evidenceHash: "{H}"}}\n')
    node_b = make_node(tmp_path / "b", shuffled)
    bmr.main(["--root", str(node_a)])
    root_a = capsys.readouterr().out.strip()
    bmr.main(["--root", str(node_b)])
    root_b = capsys.readouterr().out.strip()
    assert root_a == root_b


def test_empty_ledger_sentinel(tmp_path, capsys):
    node = tmp_path / "node"
    (node / "TT-LEDGER").mkdir(parents=True)
    (node / "TT-LEDGER" / "emissions.yaml").write_text("emissions: []\n")
    assert bmr.main(["--root", str(node)]) == 0
    assert capsys.readouterr().out.strip() == bmr.EMPTY_ROOT


def test_anchor_append_duplicate_guard_and_ref(tmp_path, capsys):
    node = make_node(tmp_path, rows((1, 7, 1)))
    log = node / "TT-LEDGER" / "anchors.log"
    assert bmr.main(["--root", str(node), "--anchor", "--ref", "abc123"]) == 0
    capsys.readouterr()
    assert bmr.main(["--root", str(node), "--anchor", "--ref", "abc123"]) == 0
    assert "already anchored" in capsys.readouterr().out
    data_lines = [l for l in log.read_text().splitlines()
                  if l and not l.startswith("#")]
    assert len(data_lines) == 1 and data_lines[0].endswith(", abc123")
    # ledger changes -> new anchor line
    (node / "TT-LEDGER" / "emissions.yaml").write_text(
        "emissions:\n" + rows((1, 7, 1), (2, 3, 2)), "utf-8")
    assert bmr.main(["--root", str(node), "--anchor", "--ref", "def456"]) == 0
    data_lines = [l for l in log.read_text().splitlines()
                  if l and not l.startswith("#")]
    assert len(data_lines) == 2
    assert log.read_text().startswith("# TT ledger anchors")


def test_missing_emissions_rc1(tmp_path):
    assert bmr.main(["--root", str(tmp_path)]) == 1
