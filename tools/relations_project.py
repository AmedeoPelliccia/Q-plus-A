# Generated 2026-11-13 - relations_project.py (0.2.0)
"""Check a model's architecture relations and project them onto its KNOT register.

Usage: python3 tools/relations_project.py <relations> <register> <s-atlas> [--check | --write]

<relations> holds taxonomy-relations.yaml (QPLUS-REL-001), programme-relations.yaml (AMPEL360-REL-CM-005) and the
README.md whose generated section is this tool's output. --check fails when that section differs from the output;
--write replaces it. Exit 0 when no rule fails, 1 otherwise; the projections are printed only when no rule fails.
"""
import datetime
import pathlib
import re
import sys

import yaml

TAXONOMY_RELATIONS = ("requires", "enables", "interfaces-with", "draws-on", "references-standard")
SYMMETRIC = ("interfaces-with",)
STATES = ("PROPOSED", "RATIFIED", "WITHDRAWN")
LIVE = ("open", "retained")                      # option states that still stand (CM-004)
SUBJECT_NAMESPACES = ("energy-carrier", "function")
KEY = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
RULING = re.compile(r"(KNOT-[A-Z0-9]+-[A-Z]{3}-\d{3})#(R\d+)")
DAY = re.compile(r"\d{4}-\d{2}-\d{2}")
CONTROL = re.compile(r"[\x00-\x1f\x7f-\x9f‪-‮⁦-⁩]")
BEGIN, END = "<!-- projections:begin -->", "<!-- projections:end -->"


def has_text(value):
    return isinstance(value, str) and bool(value.strip())


def is_list_of(value, kind):
    return isinstance(value, list) and all(isinstance(v, kind) for v in value)


def safe(text):
    """Text with control and direction-override characters made visible, so that a record cannot rewrite the report."""
    return CONTROL.sub(lambda m: f"\\x{ord(m[0]):02x}", text)


def checked_date(value):
    """True when the value is a calendar date: a YAML date, or text in the form YYYY-MM-DD."""
    if isinstance(value, datetime.date):
        return True
    if not (isinstance(value, str) and DAY.fullmatch(value)):
        return False
    try:
        datetime.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def read_yaml(path):
    """Return (document, failure): the parsed file, or the reason it cannot be read."""
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")), None
    except (OSError, UnicodeDecodeError, yaml.YAMLError) as error:
        return None, f"{path.name}: cannot be read as YAML ({type(error).__name__})"


def load(relations, register):
    """Read the two relation files and the register. Return (taxonomy, programme, KNOTs, failures)."""
    relations, register, knots = pathlib.Path(relations), pathlib.Path(register), {}
    tax, failure_t = read_yaml(relations / "taxonomy-relations.yaml")
    prog, failure_p = read_yaml(relations / "programme-relations.yaml")
    bad = [f for f in (failure_t, failure_p) if f]
    paths = sorted(register.rglob("KNOT-*.yaml"))
    if not paths:
        bad.append("no KNOT record found under the register path")
    for path in paths:
        doc, failure = read_yaml(path)
        knot = doc.get("knot") if isinstance(doc, dict) else None
        if failure:
            bad.append(failure)
        elif not isinstance(knot, dict) or knot.get("knot_id") != path.stem:
            bad.append(f"{path.name}: no `knot` record whose knot_id is the file name")
        elif path.stem in knots:
            bad.append(f"{path.stem}: recorded in more than one file")
        else:
            knots[path.stem] = knot
    return tax, prog, knots, bad


def titles(tax_root):
    return {d.name.split("_")[0]: d.name.split("_", 1)[1].replace("-", " ")
            for d in pathlib.Path(tax_root).rglob("*_*") if d.is_dir()}


def models(root):
    """Model identities of a programme: the names of the folders under its models node."""
    return {d.name.split("_", 1)[1] for d in pathlib.Path(root).glob("*_*") if d.is_dir()}


def shape(doc, name, sections):
    """Failures of form in a relations file: a mapping whose sections are lists of records."""
    if not isinstance(doc, dict):
        return [f"{name}: not a YAML mapping"]
    return [f"{name}: {s} must be a list of records" for s in sections if not is_list_of(doc.get(s, []), dict)]


def register_shape(knots):
    """Failures of form in the fields of the register that the projection reads."""
    bad = []
    for kid, k in knots.items():
        ok = all(is_list_of(k.get(f), str) for f in ("depends_on", "closed_with", "taxonomy")) \
            and all(is_list_of(k.get(f), dict) for f in ("options", "rulings", "effectivity"))
        if ok:
            ok = set(k["depends_on"] + k["closed_with"]) <= set(knots)
            for option in k["options"]:
                footprint = option.get("pbs_footprint") or []
                ok = ok and has_text(option.get("id")) and has_text(option.get("state")) and is_list_of(footprint, dict) \
                    and all(has_text(item.get(f)) for item in footprint for f in ("action", "key", "taxonomy"))
        if not ok:
            bad.append(f"{kid}: not a record the projection can read; check it with tools/knot_check.py")
    return bad


def ruling_state(ref, knots):
    """State of a ruling, read from its owning KNOT record; None when the ruling does not exist."""
    m = RULING.fullmatch(ref) if isinstance(ref, str) else None
    if not m or m[1] not in knots:
        return None
    return next((r.get("state") for r in knots[m[1]]["rulings"] if r.get("id") == m[2]), None)


def validate(tax, prog, knots, TAX, known_models):
    bad, keys = [], set()
    address = lambda value: isinstance(value, str) and value in TAX
    model = lambda value: isinstance(value, str) and value in known_models

    def record(item, where):
        key = item.get("key")
        if not isinstance(key, str) or not KEY.fullmatch(key) or key in keys:
            bad.append(f"{where}: missing or duplicate key {key}")
            return None
        keys.add(key)
        return key

    def sourced(item, key):
        if item.get("state") not in STATES:
            bad.append(f"{key}: state {item.get('state')}")
        if item.get("source_checked") is not None and not checked_date(item["source_checked"]):
            bad.append(f"{key}: source_checked is not a date in the form YYYY-MM-DD")
        elif item.get("state") == "RATIFIED" and not (has_text(item.get("source")) and item.get("source_checked")):
            bad.append(f"{key}: ratified without a checked source")
        if not has_text(item.get("authority")):
            bad.append(f"{key}: no authority")

    roles = {}                                   # role -> members of its one set that is not withdrawn
    for a in tax.get("alternatives", []):
        key = record(a, "alternatives")
        if not key:
            continue
        members, role, live = a.get("members"), a.get("for"), a.get("state") != "WITHDRAWN"
        formed = is_list_of(members, str) and len(members) >= 2 and members == sorted(set(members))
        if not has_text(role):
            bad.append(f"{key}: no role")
        elif live and role in roles:
            bad.append(f"{key}: role {role} already has an alternatives set that is not withdrawn")
        elif live and formed:
            roles[role] = set(members)
        if not formed:
            bad.append(f"{key}: members must be two or more addresses, sorted and unique")
        named = (members if isinstance(members, list) else []) + ([a["home"]] if a.get("home") is not None else [])
        bad += [f"{key}: {m} is not an S-ATLAS address" for m in named if not address(m)]
        unaddressed = a.get("unaddressed", [])
        if not is_list_of(unaddressed, dict) or not all(has_text(u.get("name")) and address(u.get("nearest")) for u in unaddressed):
            bad.append(f"{key}: an unaddressed candidate needs a name and a nearest S-ATLAS address")
        sourced(a, key)
    role_or_any = lambda value: value is None or (isinstance(value, str) and value in roles)

    for r in tax.get("relations", []):
        key = record(r, "relations")
        if not key:
            continue
        rel, subject, obj = r.get("relation"), r.get("subject"), r.get("object")
        if rel not in TAXONOMY_RELATIONS:
            bad.append(f"{key}: relation {rel} is not a taxonomy relation")
        if not address(subject):
            bad.append(f"{key}: {subject} is not an S-ATLAS address")
        if rel == "references-standard":
            if not (isinstance(obj, dict) and has_text(obj.get("document")) and has_text(obj.get("clause"))):
                bad.append(f"{key}: a standard needs a document and a clause")
        elif not address(obj):
            bad.append(f"{key}: {obj} is not an S-ATLAS address")
        elif rel in SYMMETRIC and address(subject) and not subject < obj:
            bad.append(f"{key}: a symmetric relation is stored once, endpoints in order")
        if not role_or_any(r.get("for")):
            bad.append(f"{key}: role {r.get('for')} has no alternatives set")
        sourced(r, key)

    decided = set()
    for d in prog.get("decided-by", []):
        key = record(d, "decided-by")
        if not key:
            continue
        role, knot, live = d.get("for"), d.get("knot"), d.get("state") != "WITHDRAWN"
        if not (isinstance(role, str) and role in roles):
            bad.append(f"{key}: role {role} has no alternatives set")
        if not model(d.get("model")):
            bad.append(f"{key}: {d.get('model')} is not a model of the programme")
        if not (isinstance(knot, str) and knot in knots):
            bad.append(f"{key}: {knot} is not in the register")
        elif model(d.get("model")) and not any(scope.get("model") == d["model"] for scope in knots[knot]["effectivity"]):
            bad.append(f"{key}: the effectivity of {knot} does not include {d['model']}")
        if live and isinstance(role, str) and model(d.get("model")):
            if (role, d["model"]) in decided:
                bad.append(f"{key}: {role} for {d['model']} already has a deciding KNOT")
            decided.add((role, d["model"]))
        sourced(d, key)

    for e in prog.get("exclusions", []) + prog.get("assignments", []):
        key = record(e, "programme")
        if not key:
            continue
        if ruling_state(e.get("ruling"), knots) is None:
            bad.append(f"{key}: ruling {e.get('ruling')} is not in the register")
        subject, obj = e.get("subject"), e.get("object")
        if e.get("relation") == "excluded-from":
            if not address(subject) or not model(e.get("model")) or not role_or_any(e.get("for")):
                bad.append(f"{key}: an exclusion needs an S-ATLAS address, a model of the programme and a role or null")
        elif e.get("relation") == "assigned-to":
            if not (address(subject) or (isinstance(subject, dict) and subject.get("ns") in SUBJECT_NAMESPACES
                                         and has_text(subject.get("id")))):
                bad.append(f"{key}: the subject is an S-ATLAS address, or a reference in "
                           f"{' or '.join(SUBJECT_NAMESPACES)}")
            if not (isinstance(obj, dict) and obj.get("ns") == "model" and model(obj.get("id"))):
                bad.append(f"{key}: the object is a model of the programme")
        else:
            bad.append(f"{key}: relation {e.get('relation')}")

    for c in prog.get("combinations", []):
        key = record(c, "combinations")
        if not key:
            continue
        members, role = c.get("members"), c.get("for")
        formed = is_list_of(members, str) and len(members) >= 2 and members == sorted(set(members))
        if c.get("state") != "WITHDRAWN" and not (formed and isinstance(role, str) and role in roles
                                                  and set(members) <= roles[role]):
            bad.append(f"{key}: members must be two or more sorted members of the alternatives of its role")
        if not model(c.get("model")):
            bad.append(f"{key}: {c.get('model')} is not a model of the programme")
        sourced(c, key)
    return bad


def elements(knots):
    """Live product elements: key -> (owning KNOT, S-ATLAS address), from the `create` items of options that still stand."""
    out = {}
    for kid, k in knots.items():
        for option in k["options"]:
            for item in (option.get("pbs_footprint") or []) if option["state"] in LIVE else []:
                if item["action"] == "create":
                    out[item["key"]] = (kid, item["taxonomy"])
    return out


def reach(start, knots):
    """KNOTs that must close with or before the given ones: closure over depends_on and closed_with."""
    seen, todo = set(), list(start)
    while todo:
        kid = todo.pop()
        if kid in seen:
            continue
        seen.add(kid)
        todo += knots[kid]["depends_on"] + knots[kid]["closed_with"]
    return seen


def covers(address, member):
    """True when the member is the address or lies under it in the taxonomy."""
    return member == address or member.startswith(address + "-")


def project(tax, prog, knots, role, model):
    active = lambda item: item.get("state") != "WITHDRAWN"
    alt = next(a for a in tax["alternatives"] if a["for"] == role and active(a))
    knot = next(d["knot"] for d in prog["decided-by"] if d["for"] == role and d["model"] == model and active(d))
    excluded = {e["subject"]: (e["ruling"], ruling_state(e["ruling"], knots)) for e in prog.get("exclusions", [])
                if e["relation"] == "excluded-from" and e["model"] == model and e.get("for") in (None, role)}
    owned = elements(knots)
    candidates = [((m,), None) for m in alt["members"]]
    candidates += [(tuple(c["members"]), c["key"]) for c in prog.get("combinations", [])
                   if c["for"] == role and c["model"] == model and active(c)]
    rows, owners = [], set()
    for members, combination in sorted(candidates):
        hit = sorted({s for s in excluded for m in members if covers(s, m)})  # an exclusion covers what lies under it
        if hit and combination:
            status = "review: the combination includes excluded " + ", ".join(hit)
        elif hit:
            status = "excluded by `{}` ({})".format(*excluded[hit[0]])
        else:
            status = "open, combination" if combination else "open"
        uses = sorted({(key, kid) for key, (kid, address) in owned.items() for m in members if covers(address, m)})
        needs = sorted({r["object"] for r in tax.get("relations", []) if r["relation"] == "requires"
                        and r.get("for") in (None, role) and active(r)
                        and r["subject"] in members})  # a relation holds at its recorded address only
        if not hit:
            owners |= {kid for _, kid in uses}
        rows.append({"members": members, "status": status, "elements": uses, "requires": needs})

    registered, dead = {}, {}                    # footprint addresses -> option, by whether the option still stands
    for option in knots[knot]["options"]:
        if option.get("pbs_footprint"):
            addresses = tuple(sorted({item["taxonomy"] for item in option["pbs_footprint"]}))
            if option["state"] in LIVE:
                registered[addresses] = option["id"]
            else:
                dead[addresses] = (option["id"], option["state"])
    projected = {r["members"] for r in rows if r["status"].startswith("open")}
    derived, declared = owners - {knot}, set(knots[knot]["depends_on"])
    outside = {m[:3] for members in projected for m in members} - {t[:3] for t in knots[knot]["taxonomy"]}
    return {
        "role": role, "model": model, "knot": knot, "rows": rows, "unaddressed": alt.get("unaddressed", []),
        "outside": sorted(outside), "registered": registered, "dead": dead,
        "only_projected": sorted(projected - set(registered)), "only_registered": sorted(set(registered) - projected),
        "derived": sorted(derived), "declared": sorted(declared),
        "consistent": reach(derived, knots) | {knot} == reach(declared, knots) | {knot},
    }


def render(p, TAX):
    short = lambda kid: f"`{kid[10:13]}`"
    code = lambda members: " + ".join(f"`{m}`" for m in members)
    name = lambda members: " + ".join(f"`{m}` {TAX[m]}" for m in members)
    lines = [f"### {p['role']} — {p['model']} — `{p['knot']}`", "",
             "| Candidate | Status | Product elements and owning KNOT | Requires |", "|---|---|---|---|"]
    for r in p["rows"]:
        uses = " · ".join(f"`{key}` ({short(kid)})" for key, kid in r["elements"]) or "none recorded"
        needs = " · ".join(f"`{n}`" for n in r["requires"]) or "—"
        lines.append(f"| {name(r['members'])} | {r['status']} | {uses} | {needs} |")
    lines.append("")
    for u in p["unaddressed"]:
        lines.append(f"No S-ATLAS address: {u['name']} — nearest `{u['nearest']}` {TAX[u['nearest']]}.")
    if not p["registered"] and not p["dead"]:
        lines.append(f"Options: none registered with a footprint; the {sum(r['status'].startswith('open') for r in p['rows'])} open candidates are proposals.")
    elif not p["only_projected"] and not p["only_registered"]:
        lines.append("Options: the open candidates match registered options " + ", ".join(sorted(p["registered"].values())) + ".")
    else:
        fate = lambda members: " (option {} is {})".format(*p["dead"][members]) if members in p["dead"] else ""
        parts = []
        if p["only_projected"]:
            parts.append("open candidates with no standing option: " + " · ".join(code(m) + fate(m) for m in p["only_projected"]))
        if p["only_registered"]:
            parts.append("standing options with no open candidate: "
                         + " · ".join(f"{p['registered'][m]} {code(m)}" for m in p["only_registered"]))
        lines.append("Options: mismatch — " + "; ".join(parts) + ".")
    if p["outside"]:
        lines.append("Scope: open candidates lie in chapters outside the KNOT's `taxonomy` field: "
                     + " · ".join(f"`{c}`" for c in p["outside"]) + ".")
    else:
        lines.append("Scope: every open candidate lies in a chapter of the KNOT's `taxonomy` field.")
    show = lambda ks: " · ".join(short(k) for k in ks) or "none"
    lines.append(f"Prerequisites: derived from element ownership {show(p['derived'])}; declared in the register "
                 f"{show(p['declared'])}; {'consistent' if p['consistent'] else 'INCONSISTENT'}.")
    return lines


def generated_section(readme, expected, write):
    """Compare the generated section of the README with the output; with write, replace it. Return a failure or None."""
    try:
        text = readme.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return "README.md: cannot be read"
    if text.count(BEGIN) != 1 or text.count(END) != 1 or text.index(BEGIN) > text.index(END):
        return "README.md: the markers of the generated section are missing or repeated"
    before, rest = text.split(BEGIN)
    current, after = rest.split(END)
    if current.strip("\n") == expected:
        return None
    if not write:
        return "README.md: the generated section differs from the output; run again with --write"
    readme.write_text(f"{before}{BEGIN}\n{expected}\n{END}{after}", encoding="utf-8")
    return None


def run(relations, register, tax_root, mode=None, models_root=None):
    """Return (failures, output lines). mode is None, "check" or "write" for the generated section of the README."""
    relations = pathlib.Path(relations)
    tax, prog, knots, bad = load(relations, register)
    TAX, known = titles(tax_root), models(models_root or relations.resolve().parent.parent)
    if not TAX:
        bad.append("no S-ATLAS node found under the taxonomy path")
    if not known:
        bad.append("no model folder found beside the model of these relations")
    if not bad:
        bad += shape(tax, "taxonomy-relations.yaml", ("alternatives", "relations"))
        bad += shape(prog, "programme-relations.yaml", ("decided-by", "assignments", "exclusions", "combinations"))
        bad += register_shape(knots)
    if not bad:
        bad += validate(tax, prog, knots, TAX, known)
    count = lambda doc, names: sum(len(doc.get(n) or []) for n in names) if isinstance(doc, dict) else 0
    head = (f"{count(tax, ('alternatives',))} alternative sets, {count(tax, ('relations',))} taxonomy relations, "
            f"{count(prog, ('decided-by', 'assignments', 'exclusions', 'combinations'))} programme relations; rule failures: ")
    body = []
    if not bad:
        unchecked = sorted(i["key"] for i in tax.get("alternatives", []) + tax.get("relations", []) if not i.get("source_checked"))
        body = ["", f"Sources not yet checked: {' · '.join(unchecked) or 'none'}"]
        for d in prog.get("decided-by", []):
            if d["state"] != "WITHDRAWN":
                body += [""] + render(project(tax, prog, knots, d["for"], d["model"]), TAX)
        body = [safe(line) for line in body]
        if mode:
            failure = generated_section(relations / "README.md", "\n".join([head + "none"] + body), mode == "write")
            bad += [failure] if failure else []
    bad = [safe(b) for b in bad]
    return bad, [head + (str(bad) if bad else "none")] + ([] if bad else body)


def main(argv):
    paths, flags = [a for a in argv[1:] if not a.startswith("--")], [a for a in argv[1:] if a.startswith("--")]
    if len(paths) != 3 or len(flags) > 1 or not set(flags) <= {"--check", "--write"}:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    bad, lines = run(*paths, mode=flags[0][2:] if flags else None)
    print("\n".join(lines))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
