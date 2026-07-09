"""Pytest tests for build_balances.py — --check semantics and determinism."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import build_balances  # noqa: E402

H = "b" * 64
EMISSIONS = f"""\
emissions:
  - {{id: "EM-0001", memberId: "Alice", poolId: "POOL-A", workPackage: "WP: #1",
     amount: 7, event: "ACCEPTED", evidenceHash: "{H}", date: "2026-07-01"}}
  - {{id: "EM-0002", memberId: "Alice", poolId: "POOL-B", workPackage: "WP: #2",
     amount: 3, event: "ACCEPTED", evidenceHash: "{H}", date: "2026-07-09"}}
  - {{id: "EM-0003", memberId: "Bob", poolId: "POOL-A", workPackage: "WP: #3",
     amount: 5, event: "ACCEPTED", evidenceHash: "{H}", date: "2026-07-05"}}
"""


def make_node(tmp_path, emissions=EMISSIONS):
    node = tmp_path / "node"
    (node / "TT-LEDGER").mkdir(parents=True)
    (node / "TT-LEDGER" / "emissions.yaml").write_text(emissions, "utf-8")
    return node


def test_generate_then_check_ok_then_stale(tmp_path, capsys):
    node = make_node(tmp_path)
    assert build_balances.main(["--root", str(node)]) == 0
    assert build_balances.main(["--root", str(node), "--check"]) == 0
    y = node / "TT-LEDGER" / "derived" / "balances.yaml"
    y.write_text(y.read_text("utf-8") + "# tamper\n", "utf-8")
    assert build_balances.main(["--root", str(node), "--check"]) == 1
    assert "STALE" in capsys.readouterr().out


def test_check_fails_when_derived_missing(tmp_path, capsys):
    node = make_node(tmp_path)
    assert build_balances.main(["--root", str(node), "--check"]) == 1
    assert "MISSING" in capsys.readouterr().out


def test_totals_ordering_and_none_date_guard(tmp_path):
    bad = EMISSIONS + (
        '  - {id: "EM-0004", memberId: "Alice", poolId: "POOL-A",\n'
        '     workPackage: "WP: #4", amount: 2, event: "ACCEPTED",\n'
        f'     evidenceHash: "{H}"}}\n')  # no date: must not become "None"
    node = make_node(tmp_path, bad)
    assert build_balances.main(["--root", str(node)]) == 0
    text = (node / "TT-LEDGER" / "derived" / "balances.yaml").read_text("utf-8")
    import yaml as _y
    data = _y.safe_load(text.split("\n", 2)[2])
    alice, bob = data["balances"][0], data["balances"][1]
    assert alice["memberId"] == "Alice" and alice["total"] == 12
    assert alice["lastEmissionDate"] == "2026-07-09"   # not "None"
    assert bob["memberId"] == "Bob" and bob["total"] == 5
