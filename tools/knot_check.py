# Generated 2026-11-13 - knot_check.py (0.1.3)
"""Check a KNOT register against AMPEL360-KNOT-CM-004 and print its generated views.

Usage: python3 tools/knot_check.py <register> <s-atlas> [<pbs>]

The PBS defaults to the model's SBS folder beside the register. Exit 0 when no rule fails,
1 otherwise; the views are printed only when no rule fails.
"""
import pathlib
import re
import sys

import yaml

VOCAB = {
    "kind": "obligation control-intent decision-anchor lifecycle-constraint",
    "status": "DRAFT REVIEW APPROVED SUPERSEDED OBSOLETE",
    "resolution": "OPEN RULED DEFERRED",
    "knu_class": "WORK_ITEM CONTROLLED_ARTEFACT REQUIREMENT_SET ANALYSIS_PACKAGE VERIFICATION_OBJECT EVIDENCE_RECORD OTHER",
    "progress": "NOT_STARTED IN_PROGRESS PENDING_REVIEW DONE CANCELLED",
}
REQ = ("knot_id title kind taxonomy raised_at question obligation_source lifecycle_phase due owner status resolution "
       "created_date context effectivity depends_on closed_with unblocks affects options criteria assumptions "
       "couplings rulings reopen_if knus").split()
RUL = ("id date authority statement effect rationale rationale_recorded evidence waiver state record "
       "effectivity effects embodied_in").split()
ACTIONS = ("create", "update", "populate", "retire", "remap")
SBS_VIEWS = ("PBS", "FBS", "WBS", "CBS", "RBS", "LBS", "EBS", "IBS", "ReqBS", "TPMS", "TPuBS")
KEY = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")


def has_text(value):
    return isinstance(value, str) and bool(value.strip())


def valid_effectivity(scopes):
    if not isinstance(scopes, list) or not scopes:
        return False
    for scope in scopes:
        if not isinstance(scope, dict) or not has_text(scope.get("model")):
            return False
        variants = scope.get("variants")
        if not isinstance(variants, list) or not all(has_text(v) for v in variants):
            return False
        if len(variants) != len(set(variants)) or "from_baseline" not in scope:
            return False
        if scope["from_baseline"] is not None and not has_text(scope["from_baseline"]):
            return False
    return True


def effectivity_label(scopes):
    return " · ".join(f"{s['model']} / {', '.join(s['variants']) or 'model scope'} / "
                      f"{s['from_baseline'] or 'initial definition'}" for s in scopes)


def valid_effect(item):
    return (isinstance(item, dict) and item.get("view") in SBS_VIEWS and item.get("action") in ACTIONS
            and has_text(item.get("description")) and "ref" in item
            and (has_text(item["ref"]) or (item["action"] == "create" and item["ref"] is None)))


def valid_baseline_ref(item):
    return isinstance(item, dict) and item.get("view") == "baseline" and has_text(item.get("ref"))


def cell(value):
    return value.replace("|", r"\|").replace("\n", " ")


def check(register, tax_root, pbs=None):
    """Return (failures, provisional rulings, generated table and summary lines)."""
    register, tax_root = pathlib.Path(register), pathlib.Path(tax_root)
    pbs = pathlib.Path(pbs) if pbs else (register.parent / "01-02-01-01-01-01_SBS_System-Breakdown-Structure"
                                          / "01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure")
    pbs_ids = {d.name.split("_", 1)[0] for d in pbs.rglob("eWTW-PBS-*_*") if d.is_dir()}
    paths = sorted(register.rglob("KNOT-*.yaml"))
    folder = {p.stem: p.parent.name.split("_")[0] for p in paths}
    K = {p.stem: yaml.safe_load(p.read_text(encoding="utf-8"))["knot"] for p in paths}
    TAX = {d.name.split("_")[0]: d.name.split("_", 1)[1].replace("-", " ") for d in tax_root.rglob("*_*") if d.is_dir()}
    bad, seen, by, prov, gates = [], set(), {}, [], []
    creates, uses = {}, []                                                       # rule 18
    stems = [p.stem for p in paths]
    bad += [f"{stem} recorded in more than one file" for stem in sorted(set(stems)) if stems.count(stem) > 1]

    for kid, k in K.items():
        anchor = k.get("kind") == "decision-anchor"
        miss = [f for f in REQ + ["maturity_required"] * anchor if f not in k]
        if miss:
            bad.append(f"{kid} missing {miss}")
            continue
        bad += [f"{kid} context"] * (not k["context"])
        bad += [kid] * (kid != k["knot_id"] or not re.fullmatch(r"KNOT-EWTW-[A-Z]{3}-\d{3}", kid) or not k["obligation_source"])
        bad += [f"{kid} {f}" for f in ("kind", "status", "resolution") if k[f] not in VOCAB[f].split()]
        bad += [f"{kid} -> {r}" for f in ("depends_on", "closed_with", "unblocks") for r in k[f] if r not in K]
        bad += [f"{kid} taxonomy {a}" for a in k["taxonomy"] + [k["raised_at"]] * bool(k["raised_at"]) if a not in TAX]
        home = k["taxonomy"][0] if len(k["taxonomy"]) == 1 else k["raised_at"] or "000"          # rule 11
        bad += [f"{kid} filed under {folder[kid]}, expected {home}"] * (folder[kid] != home)
        scope_valid = valid_effectivity(k["effectivity"])
        bad += [f"{kid} invalid effectivity"] * (not scope_valid)

        for option in k["options"]:
            footprint = option.get("pbs_footprint")
            if not isinstance(footprint, list):
                bad.append(f"{kid} option {option.get('id')} invalid pbs_footprint")
                continue
            for item in footprint:
                ok = (isinstance(item, dict) and item.get("action") in ACTIONS and has_text(item.get("taxonomy"))
                      and item["taxonomy"] in TAX and has_text(item.get("element"))
                      and isinstance(item.get("key"), str) and KEY.fullmatch(item["key"]))
                if not ok:
                    bad.append(f"{kid} option {option.get('id')} invalid pbs_footprint")
                elif item["action"] == "create":
                    if item.get("owner") not in (None, kid):
                        bad.append(f"{kid} option {option.get('id')} creates {item['key']} with another owner")
                    creates.setdefault(item["key"], {}).setdefault(kid, set()).add(item["taxonomy"])
                else:
                    uses.append((kid, option.get("id"), item))

        for target in k["affects"]:
            relation = target.get("relation", "affects")
            if relation == "affects":
                continue
            ref, note = target.get("ref"), target.get("note")
            if relation != "gates" or target.get("view") != "PBS" or not has_text(ref) or ref not in pbs_ids or not has_text(note):
                bad.append(f"{kid} invalid PBS gate {ref}")
            elif scope_valid and k["status"] in ("DRAFT", "REVIEW", "APPROVED") and k["resolution"] in ("OPEN", "DEFERRED"):
                gates.append((ref, kid, k["resolution"], effectivity_label(k["effectivity"]), note))

        bad += [f"{kid} ruled without a ruling"] * (k["resolution"] == "RULED" and not k["rulings"])
        for r in k["rulings"]:
            ruling = f"{kid} {r.get('id')}"
            bad += [f"{ruling} fields"] * any(f not in r for f in RUL)
            full = bool(r.get("rationale") and r.get("evidence"))
            bad += [f"{ruling} state"] * (r.get("state") != ("COMPLETE" if full else "PROVISIONAL"))
            prov += [f"`{kid[10:13]}` {r.get('id')}"] * (not full)
            bad += [f"{ruling} invalid effectivity"] * (not valid_effectivity(r.get("effectivity")))
            effects, baselines = r.get("effects"), r.get("embodied_in")
            if not isinstance(effects, list) or not all(valid_effect(i) for i in effects):
                bad.append(f"{ruling} invalid effects")
            if not isinstance(baselines, list) or not all(valid_baseline_ref(i) for i in baselines):
                bad.append(f"{ruling} invalid embodied_in")
            if r.get("state") == "PROVISIONAL" and (effects or baselines):
                bad.append(f"{ruling} provisional ruling with authorised effects or embodiment")

        for c in k["criteria"]:                                                                # a criterion record
            if not (isinstance(c, dict) and all(isinstance(c.get(f), str) and c[f].strip() for f in ("id", "text", "source"))
                    and c.get("class") in ("mandatory", "tradable") and c.get("state") in ("PROPOSED", "APPROVED")):
                bad.append(f"{kid} invalid criterion {c.get('id') if isinstance(c, dict) else c}")
        approved = bool(k["criteria"]) and all(isinstance(c, dict) and c.get("state") == "APPROVED" for c in k["criteria"])
        scored = k["resolution"] == "RULED" or any(o["state"] in ("retained", "rejected") for o in k["options"])
        if scored:                                                                             # rules 4 and 5
            bad += [f"{kid} ruled on a provisional ruling"] * any(r.get("state") != "COMPLETE" for r in k["rulings"])
            waived = any(r.get("waiver") for r in k["rulings"])
            bad += [f"{kid} scored without criteria or maturity"] * (anchor and not (approved and (k["maturity_required"] or waived)))

        for a in k["taxonomy"]:
            by.setdefault(a, []).append(kid[10:13])
        for u in k["knus"]:
            i = u["knu_id"]
            bad += [i] * (not re.fullmatch(f"KNU-{kid[5:]}-\\d\\d", i) or i in seen or not u["outputs"] or not u["exit"]
                          or u["knu_class"] not in VOCAB["knu_class"].split() or u["progress"] not in VOCAB["progress"].split()
                          or (u["progress"] == "IN_PROGRESS" and not (u["evidence_refs"] or u["end_date"])))
            bad += [f"{i} serves {r}" for r in u["serves"] if r not in K] + [f"{i} research_brief"] * ("research_brief" not in u)
            seen.add(i)

    for key, owners in sorted(creates.items()):                                               # rule 18
        if len(owners) > 1:
            bad.append(f"{key} created by {sorted(owners)}")
    for kid, oid, item in uses:
        key, owner = item["key"], item.get("owner")
        if key in creates:
            if owner not in creates[key] or owner == kid:
                bad.append(f"{kid} option {oid} uses {key} without its owner")
            elif item["taxonomy"] not in creates[key][owner]:
                bad.append(f"{kid} option {oid} files {key} under {item['taxonomy']}, owner uses {sorted(creates[key][owner])}")
        elif owner is not None:
            bad.append(f"{kid} option {oid} names owner {owner} for {key}, which no KNOT creates")

    if re.search(r"\b(compliant|conforms?)\b", str(K).lower()):
        bad.append("conformity claim")

    lines = [f"| `{kid}` | {k['title']} | `{k['kind']}` | `{folder[kid]}` | {k['resolution']} | {len(k['knus'])} | `{k['owner']}` |"
             for kid, k in K.items()]
    lines += [f"| `{a}` | {TAX[a]} | {' · '.join(f'`{t}`' for t in by[a])} |" for a in sorted(by)]
    for label, kind in (("Home to be ruled", "decision-anchor"), ("Lifecycle", "lifecycle-constraint"), ("Control", "control-intent")):
        ks = [kid[10:13] for kid, k in K.items() if not k["taxonomy"] and k["kind"] == kind]
        lines.append(f"{label}: {' · '.join(f'`{t}`' for t in ks)}")
    for k in K.values():
        for u in k["knus"]:
            if u["progress"] not in ("DONE", "CANCELLED"):
                also = " · ".join(f"`{x[10:13]}`" for x in u["serves"]) or "—"
                lines.append(f"| `{u['knu_id']}` | {u['title']} | `{u['knu_class']}` | {also} | {u['progress']} |")
    lines += [f"| `{ref}` | `{kid}` | {res} | {cell(scope)} | {cell(note)} |" for ref, kid, res, scope, note in sorted(gates)]
    summary = f"{len(K)} KNOTs, {len(seen)} KNUs, {len(by)} S-ATLAS chapters; rule failures: {bad or 'none'}"
    return bad, prov, [summary, f"Provisional rulings: {' · '.join(prov) or 'none'}"] + lines


def main(argv):
    if len(argv) not in (3, 4):
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    bad, _, lines = check(*argv[1:])
    print("\n".join(lines[:2] if bad else lines))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
