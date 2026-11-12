# Generated 2026-11-12 - relations_project.py (0.1.0)
"""Check a model's architecture relations and project them onto its KNOT register.

Usage: python3 tools/relations_project.py <relations> <register> <s-atlas>

<relations> holds taxonomy-relations.yaml (QPLUS-REL-001) and programme-relations.yaml (AMPEL360-REL-CM-005).
Exit 0 when no rule fails, 1 otherwise; the projections are printed only when no rule fails.
"""
import pathlib
import re
import sys

import yaml

TAXONOMY_RELATIONS = ("requires", "enables", "interfaces-with", "draws-on", "references-standard")
SYMMETRIC = ("interfaces-with",)
STATES = ("PROPOSED", "RATIFIED", "WITHDRAWN")
KEY = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
RULING = re.compile(r"(KNOT-[A-Z0-9]+-[A-Z]{3}-\d{3})#(R\d+)")


def has_text(value):
    return isinstance(value, str) and bool(value.strip())


def load(relations, register):
    relations, register = pathlib.Path(relations), pathlib.Path(register)
    read = lambda p: yaml.safe_load(p.read_text(encoding="utf-8"))
    knots = {p.stem: read(p)["knot"] for p in sorted(register.rglob("KNOT-*.yaml"))}
    return read(relations / "taxonomy-relations.yaml"), read(relations / "programme-relations.yaml"), knots


def titles(tax_root):
    return {d.name.split("_")[0]: d.name.split("_", 1)[1].replace("-", " ")
            for d in pathlib.Path(tax_root).rglob("*_*") if d.is_dir()}


def ruling_state(ref, knots):
    """State of a ruling, read from its owning KNOT record; None when the ruling does not exist."""
    m = RULING.fullmatch(ref or "")
    if not m or m[1] not in knots:
        return None
    return next((r.get("state") for r in knots[m[1]]["rulings"] if r.get("id") == m[2]), None)


def validate(tax, prog, knots, TAX):
    bad, keys = [], set()

    def record(item, where):
        key = item.get("key") if isinstance(item, dict) else None
        if not isinstance(key, str) or not KEY.fullmatch(key) or key in keys:
            bad.append(f"{where}: missing or duplicate key {key}")
            return None
        keys.add(key)
        return key

    def sourced(item, key):
        if item.get("state") not in STATES:
            bad.append(f"{key}: state {item.get('state')}")
        if item.get("state") == "RATIFIED" and not (has_text(item.get("source")) and has_text(item.get("source_checked"))):
            bad.append(f"{key}: ratified without a checked source")
        if not has_text(item.get("authority")):
            bad.append(f"{key}: no authority")

    roles = {}
    for a in tax.get("alternatives", []):
        key = record(a, "alternatives")
        if not key:
            continue
        members = a.get("members")
        if not has_text(a.get("for")) or a["for"] in roles:
            bad.append(f"{key}: missing or repeated role")
        elif not isinstance(members, list) or len(members) < 2 or members != sorted(set(members)):
            bad.append(f"{key}: members must be two or more, sorted and unique")
        else:
            roles[a["for"]] = set(members)
        bad += [f"{key}: {m} is not an S-ATLAS address" for m in (members or []) + ([a["home"]] if a.get("home") else []) if m not in TAX]
        for u in a.get("unaddressed", []):
            if not has_text(u.get("name")) or u.get("nearest") not in TAX:
                bad.append(f"{key}: invalid unaddressed candidate {u.get('name')}")
        sourced(a, key)

    for r in tax.get("relations", []):
        key = record(r, "relations")
        if not key:
            continue
        rel, subject, obj = r.get("relation"), r.get("subject"), r.get("object")
        if rel not in TAXONOMY_RELATIONS:
            bad.append(f"{key}: relation {rel} is not a taxonomy relation")
        if subject not in TAX:
            bad.append(f"{key}: {subject} is not an S-ATLAS address")
        if rel == "references-standard":
            if not (isinstance(obj, dict) and has_text(obj.get("document")) and has_text(obj.get("clause"))):
                bad.append(f"{key}: a standard needs a document and a clause")
        elif obj not in TAX:
            bad.append(f"{key}: {obj} is not an S-ATLAS address")
        elif rel in SYMMETRIC and not subject < obj:
            bad.append(f"{key}: a symmetric relation is stored once, endpoints in order")
        if r.get("for") is not None and r["for"] not in roles:
            bad.append(f"{key}: role {r['for']} has no alternatives set")
        sourced(r, key)

    for d in prog.get("decided-by", []):
        if d.get("for") not in roles or d.get("knot") not in knots or not has_text(d.get("model")):
            bad.append(f"decided-by: {d.get('for')} -> {d.get('knot')}")
    for e in prog.get("exclusions", []) + prog.get("assignments", []):
        key = record(e, "programme")
        if not key:
            continue
        if ruling_state(e.get("ruling"), knots) is None:
            bad.append(f"{key}: ruling {e.get('ruling')} is not in the register")
        if e.get("relation") == "excluded-from":
            if e.get("subject") not in TAX or not has_text(e.get("model")) or e.get("for") not in (None, *roles):
                bad.append(f"{key}: invalid exclusion")
        elif e.get("relation") != "assigned-to":
            bad.append(f"{key}: relation {e.get('relation')}")
    for c in prog.get("combinations", []):
        key = record(c, "combinations")
        if not key:
            continue
        members = c.get("members")
        if c.get("for") not in roles or not isinstance(members, list) or len(members) < 2 or members != sorted(set(members)) \
                or not set(members) <= roles[c["for"]] or not has_text(c.get("model")):
            bad.append(f"{key}: members must be two or more sorted members of the alternatives of its role")
        sourced(c, key)
    return bad


def elements(knots):
    """Product elements of the register: key -> (owning KNOT, S-ATLAS address), from the `create` footprints (CM-004 rule 18)."""
    out = {}
    for kid, k in knots.items():
        for option in k["options"]:
            for item in option.get("pbs_footprint") or []:
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
    alt = next(a for a in tax["alternatives"] if a["for"] == role)
    knot = next(d["knot"] for d in prog["decided-by"] if d["for"] == role and d["model"] == model)
    excluded = {e["subject"]: (e["ruling"], ruling_state(e["ruling"], knots)) for e in prog.get("exclusions", [])
                if e["relation"] == "excluded-from" and e["model"] == model and e.get("for") in (None, role)}
    owned = elements(knots)
    candidates = [((m,), None) for m in alt["members"]]
    candidates += [(tuple(c["members"]), c["key"]) for c in prog.get("combinations", [])
                   if c["for"] == role and c["model"] == model and c["state"] != "WITHDRAWN"]
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
                        and r.get("for") in (None, role) and r["state"] != "WITHDRAWN"
                        and r["subject"] in members})  # a relation holds at its recorded address only
        if not hit:
            owners |= {kid for _, kid in uses}
        rows.append({"members": members, "status": status, "elements": uses, "requires": needs})

    registered = {tuple(sorted({i["taxonomy"] for i in o["pbs_footprint"]})): o["id"]
                  for o in knots[knot]["options"] if o["state"] != "excluded" and o.get("pbs_footprint")}
    projected = {r["members"] for r in rows if r["status"].startswith("open")}
    derived, declared = owners - {knot}, set(knots[knot]["depends_on"])
    outside = {m[:3] for members in projected for m in members} - {t[:3] for t in knots[knot]["taxonomy"]}
    return {
        "role": role, "model": model, "knot": knot, "rows": rows, "unaddressed": alt.get("unaddressed", []),
        "outside": sorted(outside),
        "registered": registered, "only_projected": sorted(projected - set(registered)),
        "only_registered": sorted(set(registered) - projected),
        "derived": sorted(derived), "declared": sorted(declared),
        "consistent": reach(derived, knots) | {knot} == reach(declared, knots) | {knot},
    }


def render(p, TAX):
    short = lambda kid: f"`{kid[10:13]}`"
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
    if not p["registered"]:
        lines.append(f"Options: none registered with a footprint; the {sum(r['status'].startswith('open') for r in p['rows'])} open candidates are proposals.")
    elif not p["only_projected"] and not p["only_registered"]:
        lines.append("Options: the open candidates match registered options " + ", ".join(sorted(p["registered"].values())) + ".")
    else:
        lines.append(f"Options: mismatch — only projected {p['only_projected']}, only registered {p['only_registered']}.")
    if p["outside"]:
        lines.append("Scope: open candidates lie in chapters outside the KNOT's `taxonomy` field: "
                     + " · ".join(f"`{c}`" for c in p["outside"]) + ".")
    else:
        lines.append("Scope: every open candidate lies in a chapter of the KNOT's `taxonomy` field.")
    show = lambda ks: " · ".join(short(k) for k in ks) or "none"
    lines.append(f"Prerequisites: derived from element ownership {show(p['derived'])}; declared in the register "
                 f"{show(p['declared'])}; {'consistent' if p['consistent'] else 'INCONSISTENT'}.")
    return lines


def run(relations, register, tax_root):
    tax, prog, knots = load(relations, register)
    TAX = titles(tax_root)
    bad = validate(tax, prog, knots, TAX)
    head = (f"{len(tax.get('alternatives', []))} alternative sets, {len(tax.get('relations', []))} taxonomy relations, "
            f"{sum(len(prog.get(k, [])) for k in ('assignments', 'exclusions', 'combinations'))} programme relations; "
            f"rule failures: {bad or 'none'}")
    lines = [head]
    if not bad:
        unchecked = sorted(i["key"] for i in tax.get("alternatives", []) + tax.get("relations", []) if not i.get("source_checked"))
        lines.append(f"Sources not yet checked: {' · '.join(unchecked) or 'none'}")
        for d in prog["decided-by"]:
            lines += [""] + render(project(tax, prog, knots, d["for"], d["model"]), TAX)
    return bad, lines


def main(argv):
    if len(argv) != 4:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    bad, lines = run(*argv[1:])
    print("\n".join(lines))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
