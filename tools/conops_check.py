# Generated 2026-11-14 - conops_check.py (0.1.0)
"""Check a concept of operations and print its tables: phases, functions, supplies, cases and open inputs.

    python3 tools/conops_check.py <conops folder> <KNOT register> <S-ATLAS folder> [--check | --write]

Reads conops.yaml in the folder, checks its form and its references and prints the tables. The README of the
folder holds the output between two markers: --check fails when it differs, --write replaces it. A concept of
operations says how a system is used: in which phases, doing what, supplied by what, and what it does when
something fails. It carries no figure: a number in the input is a failure. Every statement names its basis, and
the output counts them. The tool states no conformity with any rule. It exits with status 1 on a failure and
then prints only its first line.
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import relations_project as rp  # noqa: E402

BASES = ("declared", "assumption", "proposed", "open")   # by the model or a ruling; of an analysis on record; of this document; undecided
KINDS = ("degraded", "emergency", "ground")
SECTIONS = ("id", "version", "date", "title", "knot", "serves", "bindings", "functions", "supplies", "phases", "cases", "open_inputs")
STATEMENTS = ("functions", "supplies", "phases", "cases")
AUTHORITY = "authority"                                    # an open point that no KNOT holds
SBS = "01-02-01-01-01-01_SBS_System-Breakdown-Structure"
BEGIN, END = "<!-- conops:begin -->", "<!-- conops:end -->"
KEY = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")


def numbers(value):
    """Count the numbers in a document. A date and a version are text."""
    if isinstance(value, bool):
        return 0
    if isinstance(value, (int, float)):
        return 1
    if isinstance(value, dict):
        return sum(numbers(v) for v in value.values())
    return sum(numbers(v) for v in value) if isinstance(value, list) else 0


def node_ids(sbs, prefix):
    return {d.name.split("_", 1)[0] for d in pathlib.Path(sbs).rglob(f"{prefix}-*_*") if d.is_dir()}


def validate(c, TAX, knots, sbs):
    """Return the failures of a concept of operations against its form, the register, the taxonomy and the SBS."""
    bad = [f"missing section {s}" for s in SECTIONS if s not in c]
    if bad:
        return bad
    bad += [f"{f} is not text" for f in ("id", "version", "title") if not rp.has_text(c[f])]
    bad += ["date is not a calendar date"] * (not rp.checked_date(c["date"]))
    bad += [f"a concept of operations carries no figure; {numbers(c)} found"] * bool(numbers(c))
    knot = knots.get(c["knot"])
    if knot is None:
        bad.append(f"{c['knot']} is not a KNOT of the register")
    elif c["serves"] not in [u["knu_id"] for u in knot["knus"]]:
        bad.append(f"{c['serves']} is not a KNU of {c['knot']}")
    b = c["bindings"]
    if not (isinstance(b, dict) and all(rp.is_list_of(b.get(f), str) and b[f] for f in ("functions", "pbs", "taxonomy"))):
        return bad + ["bindings name functions, pbs and taxonomy, each a list of identifiers"]
    known = {"functions": node_ids(sbs, "eWTW-FBS"), "pbs": node_ids(sbs, "eWTW-PBS"), "taxonomy": set(TAX)}
    bad += [f"binding {i} is not on disk" for f in known for i in b[f] if i not in known[f]]

    keys = {}
    for section in STATEMENTS + ("open_inputs",):
        items = c[section]
        if not (isinstance(items, list) and items and all(isinstance(i, dict) and rp.has_text(i.get("key")) and KEY.fullmatch(i["key"])
                                                          and rp.has_text(i.get("text")) for i in items)):
            return bad + [f"{section}: each item has a key in lower case with hyphens and a text"]
        keys[section] = [i["key"] for i in items]
        bad += [f"{section}: key {k} repeated" for k in sorted(set(keys[section])) if keys[section].count(k) > 1]
    every = [k for s in keys.values() for k in s]
    bad += [f"key {k} used in more than one section" for k in sorted(set(every)) if every.count(k) > 1]

    for section in STATEMENTS:                                                  # every statement names its basis
        for i in c[section]:
            where, basis = f"{section} {i['key']}", i.get("basis")
            if basis not in BASES:
                bad.append(f"{where}: basis is one of {', '.join(BASES)}")
            elif basis in ("declared", "assumption") and not rp.has_text(i.get("source")):
                bad.append(f"{where}: a statement that is {basis} names its source")
            elif basis == "open" and i.get("decided_by") != AUTHORITY and i.get("decided_by") not in knots:
                bad.append(f"{where}: an open statement names the KNOT that decides it, or `{AUTHORITY}`")
            if section in ("functions", "supplies") and i.get("taxonomy") not in TAX:
                bad.append(f"{where}: taxonomy {i.get('taxonomy')} is not an S-ATLAS address")

    functions, supplies = set(keys["functions"]), set(keys["supplies"])
    for p in c["phases"]:
        where = f"phases {p['key']}"
        if not (rp.has_text(p.get("state")) and rp.is_list_of(p.get("functions"), str) and p["functions"] and rp.is_list_of(p.get("supply"), str) and p["supply"]):
            bad.append(f"{where}: a phase has a state, the functions that run and what supplies them")
            continue
        bad += [f"{where}: {x} is not a function" for x in p["functions"] if x not in functions]
        bad += [f"{where}: {x} is not a supply" for x in p["supply"] if x not in supplies]
    for k in c["cases"]:
        where = f"cases {k['key']}"
        if not (k.get("kind") in KINDS and rp.has_text(k.get("response")) and all(rp.is_list_of(k.get(f), str) for f in ("keeps", "sheds", "supply"))):
            bad.append(f"{where}: a case has a kind ({', '.join(KINDS)}), a response, what is kept, what is shed and what supplies what is kept")
            continue
        bad += [f"{where}: {x} is not a function" for x in k["keeps"] + k["sheds"] if x not in functions]
        bad += [f"{where}: {x} is not a supply" for x in k["supply"] if x not in supplies]
        bad += [f"{where}: {x} is both kept and shed" for x in sorted(set(k["keeps"]) & set(k["sheds"]))]
    used = {x for p in c["phases"] for x in (p.get("functions") or []) + (p.get("supply") or []) if isinstance(x, str)}
    used |= {x for k in c["cases"] for x in (k.get("keeps") or []) + (k.get("supply") or []) if isinstance(x, str)}
    bad += [f"function {x} runs in no phase and is kept in no case" for x in keys["functions"] if x not in used]
    bad += [f"supply {x} supplies no phase and no case" for x in keys["supplies"] if x not in used]
    targets = set(every) - set(keys["open_inputs"])
    for o in c["open_inputs"]:
        where = f"open_inputs {o['key']}"
        if not (rp.is_list_of(o.get("blocks"), str) and o["blocks"]) or (o.get("decided_by") != AUTHORITY and o.get("decided_by") not in knots):
            bad.append(f"{where}: an open input names what it blocks and the KNOT that decides it, or `{AUTHORITY}`")
            continue
        bad += [f"{where}: {x} is not a key of this document" for x in o["blocks"] if x not in targets]
    return bad


def count(c):
    return {b: sum(1 for s in STATEMENTS for i in c[s] if i["basis"] == b) for b in BASES}


def render(c, TAX):
    def code(items):
        return " · ".join(f"`{i}`" for i in items) or "—"

    def note(i):
        decided = i.get("decided_by")
        by = "" if not decided else ("Decided by the authority" if decided == AUTHORITY else f"Decided by `{decided}`")
        return ". ".join(x.rstrip(".") for x in (i.get("source"), by, i.get("note")) if x) or "—"

    lines = [f"Scope: {c['title']}. Bound to the functions {code(c['bindings']['functions'])}, the PBS nodes {code(c['bindings']['pbs'])} "
             f"and S-ATLAS {code(c['bindings']['taxonomy'])}. Serves `{c['serves']}`.", ""]
    lines += ["### Phases", "", "| Phase | What happens | State | Functions that run | Supplied by | Basis | Source or note |", "|---|---|---|---|---|---|---|"]
    lines += [f"| `{p['key']}` | {p['text']} | {p['state']} | {code(p['functions'])} | {code(p['supply'])} | {p['basis']} | {note(p)} |" for p in c["phases"]]
    for title, section in (("Functions", "functions"), ("Supplies", "supplies")):
        lines += ["", f"### {title}", "", "| Key | What it is | S-ATLAS | Basis | Source or note |", "|---|---|---|---|---|"]
        lines += [f"| `{i['key']}` | {i['text']} | `{i['taxonomy']}` {TAX[i['taxonomy']]} | {i['basis']} | {note(i)} |" for i in c[section]]
    lines += ["", "### Cases", "", "| Case | Kind | What happens | Response | Kept | Supplied by | Shed | Basis | Source or note |", "|---|---|---|---|---|---|---|---|---|"]
    lines += [f"| `{k['key']}` | {k['kind']} | {k['text']} | {k['response']} | {code(k['keeps'])} | {code(k['supply'])} | {code(k['sheds'])} | {k['basis']} | {note(k)} |"
              for k in c["cases"]]
    lines += ["", "### Open inputs", "", "| Input | What is missing | Blocks | Decided by |", "|---|---|---|---|"]
    lines += [f"| `{o['key']}` | {o['text']} | {code(o['blocks'])} | {'the authority' if o['decided_by'] == AUTHORITY else '`' + o['decided_by'] + '`'} |" for o in c["open_inputs"]]
    return lines


def run(folder, register, tax_root, mode=None, sbs=None):
    """Return (failures, output lines). mode is None, "check" or "write" for the generated section of the README."""
    folder, register = pathlib.Path(folder), pathlib.Path(register)
    doc, failure = rp.read_yaml(folder / "conops.yaml")
    bad, c, TAX = ([failure] if failure else []), None, rp.titles(tax_root)
    if not TAX:
        bad.append("no S-ATLAS node found under the taxonomy path")
    if not bad and not (isinstance(doc, dict) and isinstance(doc.get("conops"), dict)):
        bad.append("conops.yaml: the top-level key is `conops`")
    if not bad:
        c, knots = doc["conops"], {}
        for path in sorted(register.rglob("KNOT-*.yaml")):
            record, failure = rp.read_yaml(path)
            if failure or not (isinstance(record, dict) and isinstance(record.get("knot"), dict)):
                bad.append(failure or f"{path.name}: the top-level key is `knot`")
            else:
                knots[path.stem] = record["knot"]
        if not bad:
            bad += validate(c, TAX, knots, sbs or register.resolve().parent / SBS)
    head, body = "concept of operations; rule failures: ", []
    if not bad:
        n = count(c)
        head = (f"{c['id']} {c['version']} for {c['knot']}: {len(c['phases'])} phases, {len(c['functions'])} functions, {len(c['supplies'])} supplies, "
                f"{len(c['cases'])} cases, {len(c['open_inputs'])} open inputs; {sum(n.values())} statements — {n['declared']} declared, "
                f"{n['assumption']} from an analysis, {n['proposed']} proposed here, {n['open']} open; no figure; rule failures: ")
        body = [rp.safe(line) for line in [""] + render(c, TAX)]
        if mode:
            failure = rp.generated_section(folder / "README.md", "\n".join([rp.safe(head) + "none"] + body), mode == "write", BEGIN, END)
            bad += [failure] if failure else []
    bad = [rp.safe(b) for b in bad]
    return bad, [rp.safe(head) + (str(bad) if bad else "none")] + ([] if bad else body)


def main(argv):
    paths, flags = [x for x in argv[1:] if not x.startswith("--")], [x for x in argv[1:] if x.startswith("--")]
    if len(paths) != 3 or len(flags) > 1 or not set(flags) <= {"--check", "--write"}:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    bad, lines = run(*paths, mode=flags[0][2:] if flags else None)
    print("\n".join(lines))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
