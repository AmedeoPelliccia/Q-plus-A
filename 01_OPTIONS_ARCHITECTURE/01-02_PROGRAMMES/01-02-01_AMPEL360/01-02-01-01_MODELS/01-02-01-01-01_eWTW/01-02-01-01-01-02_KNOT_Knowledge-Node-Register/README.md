---
status: draft
standard_scope: governance
---

# eWTW — KNOT Register

**Model:** AMPEL360 · [eWTW][MODEL]
**Location:** `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-02_KNOT_Knowledge-Node-Register/`
**Convention:** [`AMPEL360-KNOT-CM-004`][CM-004] Issue 1 — *PROPOSED*
**Version:** 0.4.0 · **Date:** 2026-11-12

This register holds what the eWTW must decide or satisfy — its **KNOTs** — and how each is to be resolved: its **Knowledge Units**, the **KNUs**. A KNOT states the problem. Its KNUs are the research, analyses, tests and other work that produce the knowledge to resolve it. A ruling records the decision with its rationale, and the options not retained stay in the record.

The records are YAML files, one per KNOT, each holding its KNUs. They are filed by scope, so that the register can grow without becoming one flat list: a KNOT that applies to a single S-ATLAS chapter sits in that chapter's folder, a KNOT whose home is still to be ruled sits in the folder of the chapter that raised it, and a KNOT that spans several chapters sits in `000_General/`, named after S-ATLAS chapter `000` *General* (rule 11 of [CM-004][CM-004]). The folder is a filing place, not part of the identity: a record moves when its scope is ruled, and its identifier does not change. This page is a view of the records. The [model README §5][MODEL-5] summarises the same KNOTs and shows how the decisions depend on one another.

---

## How a KNOT is resolved

```mermaid
flowchart LR
    K["KNOT<br/>problem statement"] --> U["KNUs<br/>research · analyses · tests · work items"]
    U --> E["Evidence<br/>EBS · TPMS · ReqBS"]
    E --> R{"Ruling by<br/>the authority"}
    R -->|"narrows the options"| K
    R -->|"rules"| B["Effects on the model<br/>PBS · requirements · baselines"]
    R -.->|"below the declared maturity"| W["Waiver<br/>QPLUS-LC-DECISION-MATURITY-001"]
```

No decision anchor has declared its criteria or its maturity thresholds yet: `criteria` and `maturity_required` are empty in every record, so no option can be scored (rule 5 of [CM-004][CM-004]). The verification script enforces that gate. Each anchor has a KNU that declares them first — a dedicated one for the configuration decisions (`KNU-EWTW-PRP-001-01` also serves `SRC`), the analysis KNU for the ownership rulings. A ruling may narrow the options without closing the KNOT, as ruling R1 of `KNOT-EWTW-NRG-001` did.

---

## Register

| KNOT | Title | Kind | Filed under | Resolution | KNUs | Proposed owner |
|---|---|---|---|---|:-:|---|
| `KNOT-EWTW-ESS-001` | Essential power | `decision-anchor` | `000` | OPEN | 3 | `STK_SAF` |
| `KNOT-EWTW-LCM-001` | Lifecycle notation and registry pin | `lifecycle-constraint` | `000` | OPEN | 2 | `STK_CM` |
| `KNOT-EWTW-NRG-001` | Energy carrier | `decision-anchor` | `000` | OPEN | 7 | `STK_SE` |
| `KNOT-EWTW-PRP-001` | Propulsion chain | `decision-anchor` | `000` | OPEN | 5 | `STK_SE` |
| `KNOT-EWTW-SRC-001` | Electrical sources | `decision-anchor` | `000` | OPEN | 3 | `STK_SE` |
| `KNOT-EWTW-STO-001` | Role of energy storage | `decision-anchor` | `000` | OPEN | 4 | `STK_SE` |
| `KNOT-EWTW-DFN-001` | Dorsal-fin root fairing | `decision-anchor` | `053` | OPEN | 1 | `STK_SE` |
| `KNOT-EWTW-KEL-001` | Keel-beam taxonomy home | `decision-anchor` | `053` | OPEN | 2 | `STK_CM` |
| `KNOT-EWTW-LUG-001` | Wing-attach lugs | `decision-anchor` | `053` | OPEN | 1 | `STK_SE` |
| `KNOT-EWTW-MLG-001` | MLG configuration | `decision-anchor` | `053` | OPEN | 2 | `STK_SE` |
| `KNOT-EWTW-TSI-001` | Tail-strike indicator | `decision-anchor` | `053` | OPEN | 1 | `STK_SE` |

### Rulings recorded

| KNOT | Ruling | Date | Statement | State |
|---|---|---|---|---|
| `KNOT-EWTW-NRG-001` | R1 | 2026-11-07 | Scope narrowed: all-electric, or hybrid-electric with conventional fuel; liquid hydrogen allocated to the [BWB-Q100][BWB]. Option D, cryogenic hydrogen, excluded; the KNOT stays open | `PROVISIONAL` — neither rationale nor evidence is recorded; `KNU-EWTW-NRG-001-07` |

The same ruling removes fuel cells from `KNOT-EWTW-SRC-001`. A provisional ruling directs the work, but it is not an auditable basis: both exclusions stand on the authority's statement alone until R1 is completed, and no KNOT can be ruled on it (rule 4).

---

## By S-ATLAS chapter

Each record lists, in its `taxonomy` field, the [S-ATLAS][S-ATLAS] chapters it applies to: for a configuration decision, the chapters of the model README §3 rows it unblocks — and `053` for the energy-carrier bay. The identifiers carry no classification ([CM-004][CM-004] §4). Generated from the records:

| Chapter | S-ATLAS title | KNOTs |
|---|---|---|
| `012` | Servicing | `ESS` · `SRC` |
| `021` | Air Conditioning Environmental Control | `NRG` · `PRP` · `STO` |
| `022` | Auto Flight | `ESS` · `PRP` |
| `023` | Communications | `ESS` |
| `024` | Electrical Power | `ESS` · `NRG` · `PRP` · `SRC` · `STO` |
| `026` | Fire Protection | `ESS` · `NRG` · `STO` |
| `027` | Flight Control | `PRP` |
| `028` | Energy Carrier Storage and Distribution | `NRG` |
| `031` | Indicating and Recording Systems | `ESS` |
| `034` | Navigation | `ESS` |
| `042` | Integrated Modular Avionics | `ESS` |
| `046` | Information Systems | `ESS` |
| `047` | Inerting and Protective Atmospheres | `ESS` · `NRG` · `STO` |
| `049` | Auxiliary Power Module | `ESS` · `SRC` |
| `053` | Fuselage | `NRG` |
| `061` | Powerplant Installation and Nacelle Integration | `PRP` |
| `062` | Combustion Machinery | `PRP` |
| `063` | Combustion Systems for Sustainable Carriers | `PRP` |
| `064` | Carrier Delivery Metering and Conditioning | `NRG` · `PRP` |
| `065` | Engine Air and Thermal Management | `PRP` |
| `066` | Control Monitoring and Indicating | `PRP` |
| `067` | Exhaust Emissions and Contrail Management | `PRP` |
| `068` | Turbogenerators and Power Offtakes | `NRG` · `PRP` · `SRC` · `STO` |
| `069` | Lubrication Ignition Starting and Accessories | `PRP` |
| `071` | Propulsion Architectures and Energy Management | `PRP` |
| `072` | Electric Machines for Propulsion | `PRP` |
| `073` | Power Electronics and Conversion | `PRP` |
| `074` | Propulsion Energy Storage Systems | `NRG` · `PRP` · `SRC` · `STO` |
| `076` | Propulsion Power Distribution and Protection | `ESS` · `PRP` · `SRC` |
| `077` | Electric Propulsors Installation and Distributed Integration | `PRP` |
| `078` | Thermal Management of Electric Propulsion | `NRG` · `PRP` · `STO` |
| `079` | High Voltage Safety and System Evidence | `ESS` · `NRG` · `PRP` · `SRC` · `STO` |

Home to be ruled, since each decides where its scope lives: `DFN` · `KEL` · `LUG` · `MLG` · `TSI`. Lifecycle, with no chapter: `LCM`.

---

## Research agenda

The KNUs neither done nor cancelled, generated from the records (rule 9). Every KNU is proposed; none has started.

| KNU | Title | Class | Also serves | Progress |
|---|---|---|---|---|
| `KNU-EWTW-ESS-001-01` | Essential loads and duration | `ANALYSIS_PACKAGE` | — | NOT_STARTED |
| `KNU-EWTW-ESS-001-02` | Essential source options | `ANALYSIS_PACKAGE` | — | NOT_STARTED |
| `KNU-EWTW-ESS-001-03` | Decision criteria and maturity thresholds | `REQUIREMENT_SET` | — | NOT_STARTED |
| `KNU-EWTW-LCM-001-01` | Baseline notation | `WORK_ITEM` | — | NOT_STARTED |
| `KNU-EWTW-LCM-001-02` | Registry re-pin | `WORK_ITEM` | — | NOT_STARTED |
| `KNU-EWTW-NRG-001-01` | Decision criteria and maturity thresholds | `REQUIREMENT_SET` | — | NOT_STARTED |
| `KNU-EWTW-NRG-001-02` | Design mission and reserve policy | `REQUIREMENT_SET` | `PRP` · `SRC` · `STO` | NOT_STARTED |
| `KNU-EWTW-NRG-001-03` | Mission energy and power budget | `ANALYSIS_PACKAGE` | `PRP` · `SRC` · `STO` | NOT_STARTED |
| `KNU-EWTW-NRG-001-04` | Battery technology state | `EVIDENCE_RECORD` | `STO` | NOT_STARTED |
| `KNU-EWTW-NRG-001-05` | Thermal machine on conventional fuel | `ANALYSIS_PACKAGE` | `PRP` · `SRC` | NOT_STARTED |
| `KNU-EWTW-NRG-001-06` | Trade study of the energy carrier | `ANALYSIS_PACKAGE` | — | NOT_STARTED |
| `KNU-EWTW-NRG-001-07` | Rationale and evidence of ruling R1 | `EVIDENCE_RECORD` | — | NOT_STARTED |
| `KNU-EWTW-PRP-001-01` | Decision criteria and maturity thresholds | `REQUIREMENT_SET` | `SRC` | NOT_STARTED |
| `KNU-EWTW-PRP-001-02` | Propulsor architecture | `ANALYSIS_PACKAGE` | — | NOT_STARTED |
| `KNU-EWTW-PRP-001-03` | Efficiency and heat chain | `ANALYSIS_PACKAGE` | `SRC` | NOT_STARTED |
| `KNU-EWTW-PRP-001-04` | Propulsion failure cases | `ANALYSIS_PACKAGE` | — | NOT_STARTED |
| `KNU-EWTW-PRP-001-05` | PBS group for a thermal machine | `CONTROLLED_ARTEFACT` | — | NOT_STARTED |
| `KNU-EWTW-SRC-001-01` | Electrical load analysis | `ANALYSIS_PACKAGE` | `STO` · `ESS` | NOT_STARTED |
| `KNU-EWTW-SRC-001-02` | Source sizing | `ANALYSIS_PACKAGE` | — | NOT_STARTED |
| `KNU-EWTW-SRC-001-03` | Distribution architecture | `ANALYSIS_PACKAGE` | `ESS` | NOT_STARTED |
| `KNU-EWTW-STO-001-01` | Storage role and size | `ANALYSIS_PACKAGE` | — | NOT_STARTED |
| `KNU-EWTW-STO-001-02` | Battery installation safety | `REQUIREMENT_SET` | — | NOT_STARTED |
| `KNU-EWTW-STO-001-03` | Propagation test plan | `VERIFICATION_OBJECT` | — | NOT_STARTED |
| `KNU-EWTW-STO-001-04` | Decision criteria and maturity thresholds | `REQUIREMENT_SET` | — | NOT_STARTED |
| `KNU-EWTW-DFN-001-01` | Fairing ownership | `ANALYSIS_PACKAGE` | — | NOT_STARTED |
| `KNU-EWTW-KEL-001-01` | Taxonomy home of the keel beam | `CONTROLLED_ARTEFACT` | — | NOT_STARTED |
| `KNU-EWTW-KEL-001-02` | Station binding | `WORK_ITEM` | — | NOT_STARTED |
| `KNU-EWTW-LUG-001-01` | Wing-attach interface split | `ANALYSIS_PACKAGE` | — | NOT_STARTED |
| `KNU-EWTW-MLG-001-01` | Trunnion location | `ANALYSIS_PACKAGE` | — | NOT_STARTED |
| `KNU-EWTW-MLG-001-02` | 053-200 engine note | `CONTROLLED_ARTEFACT` | — | NOT_STARTED |
| `KNU-EWTW-TSI-001-01` | Tail-strike provision and sensing | `ANALYSIS_PACKAGE` | — | NOT_STARTED |

Three KNUs touch protected areas and are author acts: `KNU-EWTW-PRP-001-05` and `KNU-EWTW-KEL-001-02` in the PBS, `KNU-EWTW-KEL-001-01` in the taxonomy. Two are conditional on their KNOT's ruling: `KNU-EWTW-PRP-001-05` and `KNU-EWTW-STO-001-03`.

---

## PBS nodes pending a ruling

This view is generated from the `gates` relations in the KNOT records. Each row identifies the existing PBS node, the decision's effectivity and the allocation awaiting that decision. The option's `pbs_footprint` describes the candidate structure. A complete ruling records the requirements and authorised changes by view, and `embodied_in` references the first ratified baseline for the affected scope. [CM-004 §8][CM-004]

| PBS node | KNOT | Resolution | Effectivity | Pending allocation |
|---|---|---|---|---|
| `eWTW-PBS-024-000` | `KNOT-EWTW-ESS-001` | OPEN | eWTW / model scope / initial definition | Essential feeds and segregation |
| `eWTW-PBS-024-000` | `KNOT-EWTW-SRC-001` | OPEN | eWTW / model scope / initial definition | Source-dependent conversion, protection and distribution |
| `eWTW-PBS-028-000` | `KNOT-EWTW-STO-001` | OPEN | eWTW / model scope / initial definition | Storage installation by allocated role |
| `eWTW-PBS-053-200-010` | `KNOT-EWTW-LUG-001` | OPEN | eWTW / model scope / initial definition | Wing-attach lug ownership and interface split |
| `eWTW-PBS-053-200-030` | `KNOT-EWTW-MLG-001` | OPEN | eWTW / model scope / initial definition | Main landing gear trunnion mounting |
| `eWTW-PBS-053-300-030` | `KNOT-EWTW-TSI-001` | OPEN | eWTW / model scope / initial definition | Tail-strike provision and sensing ownership |
| `eWTW-PBS-053-400-040` | `KNOT-EWTW-DFN-001` | OPEN | eWTW / model scope / initial definition | Dorsal-fin root fairing ownership |
| `eWTW-PBS-053-600-090` | `KNOT-EWTW-KEL-001` | OPEN | eWTW / model scope / initial definition | Keel-beam taxonomy binding |
| `eWTW-PBS-053-900-000` | `KNOT-EWTW-NRG-001` | OPEN | eWTW / model scope / initial definition | Energy-carrier bay contents and installation |
| `eWTW-PBS-071-000` | `KNOT-EWTW-PRP-001` | OPEN | eWTW / model scope / initial definition | Propulsion module and installation allocation |

---

## Research briefs

Every KNOT carries a `context`, and every KNU that needs outside research a `research_brief` with its questions. Together with [`model-context.yaml`](model-context.yaml) — the aircraft, the research rules and the deliverable, written once — they form a prompt that can be handed as it is to a deep-research agent. From the repository root, with `REG` set as in *How to verify*, this command prints the brief of one KNU:

```sh
python3 - "$REG" KNU-EWTW-NRG-001-04 <<'EOF'
import pathlib, sys, yaml
reg, kid = pathlib.Path(sys.argv[1]), sys.argv[2]
p = next(reg.rglob("KNOT-" + kid[4:16] + ".yaml")); k = yaml.safe_load(p.read_text(encoding="utf-8"))["knot"]
u = next(x for x in k["knus"] if x["knu_id"] == kid)
if not u["research_brief"]: sys.exit(kid + " has no research brief: it is not a research task")
out = dict(yaml.safe_load((reg / "model-context.yaml").read_text(encoding="utf-8")))
out["decision"] = {f: k[f] for f in ("knot_id", "title", "question", "context", "effectivity", "options", "assumptions")}
out["task"] = {f: u[f] for f in ("knu_id", "title", "knu_class", "description", "research_brief", "exit")}
print(yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=110))
EOF
```

24 of the 31 KNUs have a brief. The other seven are work items, author acts and the authority's own rationale for R1, which no outside research can supply. The briefs state only what the model has declared; they are proposed text, to be sharpened before a research run.

---

## How to verify

From the repository root:

```bash
TAX="01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_S-ATLAS"
REG="01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-02_KNOT_Knowledge-Node-Register"
python3 - "$REG" "$TAX" <<'EOF'
import pathlib, re, sys, yaml

register = pathlib.Path(sys.argv[1])
pbs = (register.parent / "01-02-01-01-01-01_SBS_System-Breakdown-Structure"
       / "01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure")
pbs_ids = {d.name.split("_", 1)[0] for d in pbs.rglob("eWTW-PBS-*_*") if d.is_dir()}
F = {p.stem: p.parent.name.split("_")[0] for p in sorted(pathlib.Path(sys.argv[1]).rglob("KNOT-*.yaml"))}
K = {p.stem: yaml.safe_load(p.read_text(encoding="utf-8"))["knot"] for p in sorted(pathlib.Path(sys.argv[1]).rglob("KNOT-*.yaml"))}
TAX = {d.name.split("_")[0]: d.name.split("_", 1)[1].replace("-", " ") for d in pathlib.Path(sys.argv[2]).rglob("*_*") if d.is_dir()}
V = {"kind": "obligation control-intent decision-anchor lifecycle-constraint", "status": "DRAFT REVIEW APPROVED SUPERSEDED OBSOLETE",
     "resolution": "OPEN RULED DEFERRED", "knu_class": "WORK_ITEM CONTROLLED_ARTEFACT REQUIREMENT_SET ANALYSIS_PACKAGE "
     "VERIFICATION_OBJECT EVIDENCE_RECORD OTHER", "progress": "NOT_STARTED IN_PROGRESS PENDING_REVIEW DONE CANCELLED"}
REQ = ("knot_id title kind taxonomy raised_at question obligation_source lifecycle_phase due owner status resolution created_date "
       "context effectivity depends_on closed_with unblocks affects options criteria assumptions couplings rulings reopen_if knus").split()
RUL = ("id date authority statement effect rationale rationale_recorded evidence waiver state record "
       "effectivity effects embodied_in").split()
actions = ("create", "update", "populate", "retire", "remap")
sbs_views = ("PBS", "FBS", "WBS", "CBS", "RBS", "LBS", "EBS", "IBS", "ReqBS", "TPMS", "TPuBS")
bad, seen, by, prov, pbs_gates = [], set(), {}, [], []

def has_text(value):
    return isinstance(value, str) and bool(value.strip())

def valid_effectivity(scopes):
    if not isinstance(scopes, list) or not scopes:
        return False
    for scope in scopes:
        if not isinstance(scope, dict) or not has_text(scope.get("model")):
            return False
        variants = scope.get("variants")
        if not isinstance(variants, list) or not all(has_text(variant) for variant in variants):
            return False
        if len(variants) != len(set(variants)) or "from_baseline" not in scope:
            return False
        baseline = scope["from_baseline"]
        if baseline is not None and not has_text(baseline):
            return False
    return True

def effectivity_label(scopes):
    return " · ".join(
        f"{scope['model']} / {', '.join(scope['variants']) or 'model scope'} / "
        f"{scope['from_baseline'] or 'initial definition'}"
        for scope in scopes
    )

def valid_footprint(item):
    return (isinstance(item, dict) and item.get("action") in actions
            and has_text(item.get("taxonomy")) and item["taxonomy"] in TAX
            and has_text(item.get("element")))

def valid_effect(item):
    return (isinstance(item, dict) and item.get("view") in sbs_views
            and item.get("action") in actions and has_text(item.get("description"))
            and "ref" in item
            and (has_text(item["ref"]) or (item["action"] == "create" and item["ref"] is None)))

def valid_baseline_ref(item):
    return isinstance(item, dict) and item.get("view") == "baseline" and has_text(item.get("ref"))

def markdown_cell(value):
    return value.replace("|", r"\|").replace("\n", " ")

for kid, k in K.items():
    anchor = k.get("kind") == "decision-anchor"
    miss = [f for f in REQ + ["maturity_required"] * anchor if f not in k]
    if miss:
        bad.append(f"{kid} missing {miss}"); continue
    bad += [f"{kid} context"] * (not k["context"])
    bad += [kid] * (kid != k["knot_id"] or not re.fullmatch(r"KNOT-EWTW-[A-Z]{3}-\d{3}", kid) or not k["obligation_source"])
    bad += [f"{kid} {f}" for f in ("kind", "status", "resolution") if k[f] not in V[f].split()]
    bad += [f"{kid} -> {r}" for f in ("depends_on", "closed_with", "unblocks") for r in k[f] if r not in K]
    bad += [f"{kid} taxonomy {a}" for a in k["taxonomy"] + [k["raised_at"]] * bool(k["raised_at"]) if a not in TAX]
    home = k["taxonomy"][0] if len(k["taxonomy"]) == 1 else k["raised_at"] or "000"          # rule 11
    bad += [f"{kid} filed under {F[kid]}, expected {home}"] * (F[kid] != home)
    scope_valid = valid_effectivity(k["effectivity"])
    if not scope_valid:
        bad.append(f"{kid} invalid effectivity")
    for option in k["options"]:
        footprint = option.get("pbs_footprint")
        if not isinstance(footprint, list) or not all(valid_footprint(item) for item in footprint):
            bad.append(f"{kid} option {option.get('id')} invalid pbs_footprint")
    for target in k["affects"]:
        relation = target.get("relation", "affects")
        if relation == "affects":
            continue
        ref, note = target.get("ref"), target.get("note")
        if (relation != "gates" or target.get("view") != "PBS"
                or not has_text(ref) or ref not in pbs_ids or not has_text(note)):
            bad.append(f"{kid} invalid PBS gate {ref}")
            continue
        if scope_valid and k["status"] in ("DRAFT", "REVIEW", "APPROVED") and k["resolution"] in ("OPEN", "DEFERRED"):
            pbs_gates.append((ref, kid, k["resolution"], effectivity_label(k["effectivity"]), note))
    if k["resolution"] == "RULED" and not k["rulings"]:
        bad.append(f"{kid} ruled without a ruling")
    for r in k["rulings"]:
        bad += [f"{kid} {r.get('id')} fields"] * any(f not in r for f in RUL)
        full = bool(r.get("rationale") and r.get("evidence"))
        bad += [f"{kid} {r.get('id')} state"] * (r.get("state") != ("COMPLETE" if full else "PROVISIONAL"))
        prov += [f"`{kid[10:13]}` {r.get('id')}"] * (not full)
        ruling = f"{kid} {r.get('id')}"
        if not valid_effectivity(r.get("effectivity")):
            bad.append(f"{ruling} invalid effectivity")
        effects, baselines = r.get("effects"), r.get("embodied_in")
        if not isinstance(effects, list) or not all(valid_effect(item) for item in effects):
            bad.append(f"{ruling} invalid effects")
        if not isinstance(baselines, list) or not all(valid_baseline_ref(item) for item in baselines):
            bad.append(f"{ruling} invalid embodied_in")
        if r.get("state") == "PROVISIONAL" and (effects or baselines):
            bad.append(f"{ruling} provisional ruling with authorised effects or embodiment")
    scored = k["resolution"] == "RULED" or any(o["state"] in ("retained", "rejected") for o in k["options"])
    if scored:                                                                                 # rules 4 and 5
        bad += [f"{kid} ruled on a provisional ruling"] * any(r.get("state") != "COMPLETE" for r in k["rulings"])
        waived = any(r.get("waiver") for r in k["rulings"])
        bad += [f"{kid} scored without criteria or maturity"] * (anchor and not (k["criteria"] and (k["maturity_required"] or waived)))
    for a in k["taxonomy"]:
        by.setdefault(a, []).append(kid[10:13])
    for u in k["knus"]:
        i = u["knu_id"]
        bad += [i] * (not re.fullmatch(f"KNU-{kid[5:]}-\\d\\d", i) or i in seen or not u["outputs"] or not u["exit"]
                      or u["knu_class"] not in V["knu_class"].split() or u["progress"] not in V["progress"].split()
                      or (u["progress"] == "IN_PROGRESS" and not (u["evidence_refs"] or u["end_date"])))
        bad += [f"{i} serves {r}" for r in u["serves"] if r not in K] + [f"{i} research_brief"] * ("research_brief" not in u)
        seen.add(i)
if re.search(r"\b(compliant|conforms?)\b", str(K).lower()): bad.append("conformity claim")
print(f"{len(K)} KNOTs, {len(seen)} KNUs, {len(by)} S-ATLAS chapters; rule failures: {bad or 'none'}")
print(f"Provisional rulings: {' · '.join(prov) or 'none'}")
if bad:
    sys.exit(1)
for kid, k in K.items():
    print(f"| `{kid}` | {k['title']} | `{k['kind']}` | `{F[kid]}` | {k['resolution']} | {len(k['knus'])} | `{k['owner']}` |")
for a in sorted(by):
    print(f"| `{a}` | {TAX[a]} | {' · '.join(f'`{t}`' for t in by[a])} |")
for label, kinds in (("Home to be ruled", ("decision-anchor",)), ("Lifecycle", ("lifecycle-constraint",))):
    ks = [kid[10:13] for kid, k in K.items() if not k["taxonomy"] and k["kind"] in kinds]
    print(f"{label}: {' · '.join(f'`{t}`' for t in ks)}")
for k in K.values():
    for u in k["knus"]:
        if u["progress"] not in ("DONE", "CANCELLED"):
            also = " · ".join(f"`{x[10:13]}`" for x in u["serves"]) or "—"
            print(f"| `{u['knu_id']}` | {u['title']} | `{u['knu_class']}` | {also} | {u['progress']} |")
for ref, kid, resolution, scope, note in sorted(pbs_gates):
    print(f"| `{ref}` | `{kid}` | {resolution} | {markdown_cell(scope)} | {markdown_cell(note)} |")
EOF
```

The first line reads `11 KNOTs, 31 KNUs, 32 S-ATLAS chapters; rule failures: none` and the second `Provisional rulings: `NRG` R1`; the remaining output reproduces the four tables and the two lines under the chapter table. The script checks record fields, filing, scoring and ruling state, identifiers, vocabularies, references between KNOTs, S-ATLAS addresses, KNU outputs and exit criteria, and the absence of conformity claims. It also validates the new effectivity, option footprints and ruling fields, and resolves each `gates` reference to a canonical PBS node. It exits with status 1 on a rule failure.

---

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-08 | Register created: the 11 KNOTs of the model README 0.3.0 §5 as records, 29 KNUs proposed, ruling R1 of `KNOT-EWTW-NRG-001` recorded; S-ATLAS chapters per KNOT and the view by chapter |
| 0.2.0 | 2026-11-12 | Review of 0.1.0 applied. Records filed by scope: `053_Fuselage/` and `000_General/`. Scoring gate and required fields enforced by the script; `maturity_required` on every decision anchor; criteria KNUs added for `STO` and `ESS` (31 KNUs). R1 marked `PROVISIONAL`; `KNU-EWTW-NRG-001-07` now covers its evidence and writes the reopen condition to the KNOT |
| 0.3.0 | 2026-11-12 | `context` on every KNOT and `research_brief` on 24 KNUs, with `model-context.yaml`: together they are a prompt for a deep-research agent; command to print one brief |
| 0.4.0 | 2026-11-12 | Added effectivity, candidate PBS footprints, ruling effects across SBS views, baseline embodiment and a generated view of pending PBS allocations. |

[MODEL]: ../README.md
[MODEL-5]: ../README.md#5-open-knots
[CM-004]: AMPEL360-KNOT-CM-004_Knowledge-Nodes-and-Units.md
[BWB]: ../../01-02-01-01-02_BWB-Q100/README.md
[S-ATLAS]: ../../../../../01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_S-ATLAS/
