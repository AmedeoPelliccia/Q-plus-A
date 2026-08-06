#!/usr/bin/env python3
# =============================================================================
# populate_S-STA-102.py
# Q+ATLANTIDE / S-STA / 100-109 / 102_Systems-Engineering-and-Requirements-
# Management. Register-derived sections; anchors cited undated from the
# S-STA standards register; merge constitutes ratification of this chapter
# section register (ruling v0.4 §6). Sections only; subjects register-gated.
# Idempotent; truthful --dry-run; --bootstrap; guarded --overwrite.
# =============================================================================
import argparse, sys
from pathlib import Path

CH = "102"; CH_TITLE = "Systems-Engineering-and-Requirements-Management"
RANGE_REL = ("01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
             "100-199_S-STA/100-109_General-Space-Systems-Engineering-"
             "Assurance-and-Human-Support")

SCOPE = ("Systems-engineering discipline and requirements management for "
         "the band: SE management and planning, requirements engineering, "
         "functional and technical specification classes, architecture "
         "definition and trade discipline, analysis-model and simulation "
         "management, technology assessment and maturity in SE, the "
         "verification-planning interface, model-based systems engineering, "
         "and SE products with review readiness. This chapter owns "
         "requirement classes, grammars and the SE discipline — actual "
         "requirements are downstream artifacts and are never instantiated "
         "in the taxonomy. Mission concepts are 101 (102 consumes what "
         "101-200 defines); programme structure, configuration, "
         "documentation and reviews are 103; verification execution and "
         "qualification are 105; interface control is 106; system and "
         "vehicle classes are 190-199.")

DIAGRAM = """```mermaid
flowchart LR
  X101["101-200<br/>Concept of operations"] --> RQ["102-200 Requirements<br/>engineering"] --> SP["102-300 Functional and<br/>technical specifications"] --> AR["102-400 System architecture<br/>and trade studies"]
  SE["102-100 SE management<br/>and planning"] --- RQ
  MD["102-500 Engineering-analysis<br/>models and simulation"] --- AR
  TR["102-600 Technology-readiness<br/>assessment and SE integration"] --- AR
  MB["102-800 MBSE and<br/>digital continuity"] --- SE
  MB --- AR
  RQ --> VP["102-700 Requirement verifiability,<br/>verification-planning interface"] --> EV["102-900 SE products,<br/>evidence, review readiness"]
  AR --> EV
  VP -. "programme, execution,<br/>qualification" .-> X105["105"]
  SE -. "programme, configuration,<br/>information, reviews" .-> X103["103"]
  MB -. "baselines and<br/>controlled records" .-> X103
  AR -. "interface-control<br/>implementation" .-> X106["106"]
  AR -. "class constraints" .-> X190["190-199"]
  TR -. "shared maturity and<br/>graduation doctrine" .-> X100["100-500"]
```"""

S = {
 "000": ('General-Information',
   'Chapter role and derivation, and the agnosticism rule instanced: this chapter owns requirement classes, grammars and SE discipline; actual requirements are downstream artifacts. Sections cite their standards-register anchors undated; a declared absence is preferred to a false anchor.',
   '',
   [('010', 'Derivation-and-Agnosticism-Rule', 'Classes and grammars here; actual requirements downstream.'), ('020', 'Relationship-Map', 'How 102 relates to 101, 103, 105, 106 without duplication.')]),
 "100": ('Systems-Engineering-Management-and-Planning',
   'SE management as a discipline: the systems-engineering management plan as an artifact class, process tailoring doctrine, SE roles and responsibilities classes, and the relationship of SE planning to programme structure (103 owns the programme; this section owns how engineering is managed within it).',
   'ISO 18676',
   [('110', 'SE-Management-Plan-Class', 'The SEMP artifact class (ISO 18676).'), ('120', 'Process-Tailoring-Doctrine', 'Tailoring of SE processes by project class.'), ('130', 'SE-Roles-and-Responsibilities', 'Role classes within the engineering organization (11893 interface at 103).')]),
 "200": ('Requirements-Engineering-and-Management',
   'The requirements discipline: elicitation from mission concepts (101), requirement classes and quality criteria, allocation and flow-down doctrine, traceability grammar, and change interfaces toward configuration management (103). The requirements breakdown structure belongs to the 103 breakdown family; its content discipline lives here.',
   'ISO 16404',
   [('210', 'Requirement-Classes-and-Quality', 'Requirement classes and quality criteria (ISO 16404).'), ('220', 'Allocation-and-Flow-Down', 'Allocation and flow-down doctrine.'), ('230', 'Traceability-Grammar', 'Traceability relations and their grammar.'), ('240', 'Requirement-Change-Interface', 'Change interface toward configuration management (103-300).')]),
 "300": ('Functional-and-Technical-Specifications',
   'Specification artifact classes: functional specifications, technical specifications, their structure and content rules, and their relation to requirement sets and to downstream declaration schemas.',
   'ISO 21351',
   [('310', 'Functional-Specification-Class', 'Functional specification structure and semantics (ISO 21351).'), ('320', 'Technical-Specification-Class', 'Technical specification structure and semantics.'), ('330', 'Specification-Tree-Relationships', 'Relations among specifications and to downstream schemas.')]),
 "400": ('System-Architecture-Definition-and-Trade-Study-Discipline',
   'The SE side of architecture: functional and physical architecture definition process, trade-study methodology and decision-record classes. Mission-architecture content is 101; configuration constraints are 190-199; this section owns the method.',
   'Register-derived; trade-study sources pending',
   [('410', 'Functional-and-Physical-Architecture-Method', 'Architecture definition method and views.'), ('420', 'Trade-Study-Method', 'Trade methodology classes.'), ('430', 'Decision-Record-Classes', 'Decision-record artifact classes.')]),
 "500": ('Engineering-Analysis-Models-and-Simulation-Management',
   'Model-management discipline: analysis-model classes, exchange of mathematical models, simulation requirement classes, fidelity and validation declaration. Domain models are built and used in their domains (structural 110, GNC 142, thermal 135); this section owns how models are declared, exchanged and managed.',
   'ISO 14954 — dynamic/static model exchange; ISO 16781 — control-system simulation; broader engineering-analysis governance register-derived',
   [('510', 'Model-Classes-and-Assumptions', 'Analysis-model classes and declared assumptions.'), ('520', 'Model-Exchange-Governance', 'Exchange governance (ISO 14954 — dynamic/static model exchange).'), ('530', 'Simulation-Requirement-Classes', 'Simulation requirement classes (ISO 16781 — control-system simulation).'), ('540', 'Validation-State-Metadata', 'Fidelity and validation-state declaration of models.')]),
 "600": ('Technology-Readiness-Assessment-and-SE-Integration',
   '100-500 owns the shared maturity, evidence-state and graduation doctrine; this section owns TRL assessment planning, evidence integration, technology-insertion decisions and readiness claims within systems engineering.',
   'ISO 16290',
   [('610', 'TRL-Assessment-Planning', 'Assessment planning within SE (ISO 16290).'), ('620', 'Evidence-Integration', 'Integrating maturity evidence into engineering decisions.'), ('630', 'Technology-Insertion-Decisions', 'Insertion and readiness-claim doctrine; shared doctrine 100-500.')]),
 "700": ('Requirement-Verifiability-and-Verification-Planning-Interface',
   'The requirement-side of verification: verifiability as a requirement quality, verification-method assignment per requirement class, and the verification cross-reference matrix as the interface artifact — one interface, two owners: this section defines the requirement side; the verification programme, execution and qualification are 105.',
   'ISO 23135 — verification programme owned by 105',
   [('710', 'Verifiability-as-Requirement-Quality', 'Verifiability criteria per requirement class.'), ('720', 'Verification-Method-Assignment', 'Method assignment doctrine per class.'), ('730', 'Cross-Reference-Matrix-Interface', 'The VCRM as interface artifact — requirement side here, programme 105.')]),
 "800": ('Model-Based-Systems-Engineering-and-Digital-Continuity',
   'MBSE discipline in the space SE process: model-based specification and architecture classes, digital continuity of SE artifacts, and the interface toward digital-twin technology — the technology domain is the digital band (300-399); the SE-discipline application is owned here.',
   'Register-derived; MBSE sources pending',
   [('810', 'MBSE-Semantics-and-Viewpoints', 'Model semantics and viewpoint classes.'), ('820', 'Cross-Model-Traceability', 'Traceability across models and artifacts.'), ('830', 'Digital-Continuity-Interfaces', 'Continuity toward digital-twin technology (300-399) and records (103).')]),
 "900": ('SE-Products-Evidence-and-Review-Readiness',
   'SE products as evidence classes: SE management plans, requirement sets and traceability records, specification trees, trade and decision records, analysis reports — with review readiness toward programme reviews (103) and the maturity expectations of 100-500. Documentation precedence is band governance (100-700, 103) and is consumed, never redefined.',
   'ISO 18676; ISO 21349',
   [('910', 'SE-Product-Classes', 'SEMP, requirement sets, specification trees, trade and analysis records.'), ('920', 'Evidence-Sufficiency', 'Sufficiency doctrine of SE evidence.'), ('930', 'Review-Readiness', 'Readiness toward reviews; process and gates 103-500.')]),
}

def subj_readme(sec, sc, st, line):
    return (f"# {CH}-{sc} — {st.replace('-',' ')}\n\n"
            f"**Section:** {CH}-{sec} · **Subject:** {sc}\n\n- {line}\n\n"
            f"*Subject items are downstream matter; anchors cited undated.*\n")

def sec_readme(code, title, body, std, subs):
    L = [f"# {CH}-{code} — {title.replace('-',' ')}", "",
         f"**Chapter:** {CH}_{CH_TITLE} · **Section:** {code}", "", body, ""]
    if std: L += [f"**Anchoring standards (undated):** {std}", ""]
    L += ["## Subjects", "", "| Subject | Title |", "|---|---|"]
    for sc, st, _ in subs:
        L.append(f"| {CH}-{sc} | [{st.replace('-',' ')}]({CH}-{sc}_{st}/) |")
    L.append("")
    return "\n".join(L)

def ch_readme():
    L=[];A=L.append
    A(f"# {CH}_{CH_TITLE}");A("")
    A(f"**Band:** 100-199_S-STA · **Range:** 100-109 · **Status:** Register-derived chapter at dual grain — sections and subjects cite standards-register anchors; merge constitutes ratification of this chapter register under S-STA-BAND-RULING v0.4 §6. Source governance: a declared absence is preferred to a false anchor.");A("")
    A("## Scope");A("");A(SCOPE);A("")
    A("## Concept flow");A("");A(DIAGRAM);A("")
    A("## Section register");A("")
    A("| Section | Title | Subjects | Anchors |");A("|---|---|---|---|")
    for code,(t,_,std,subs) in S.items():
        A(f"| {CH}-{code} | [{t.replace('-',' ')}]({CH}-{code}_{t}/) | {len(subs)} | {std if std else '—'} |")
    A("")
    A("## Boundary summary");A("")
    A("")
    return "\n".join(L)+"\n"

def build_plan(cdir):
    plan=[(cdir/"README.md",ch_readme(),True)]
    for code,(t,body,std,subs) in S.items():
        sdir=cdir/f"{CH}-{code}_{t}"
        plan.append((sdir/"README.md",sec_readme(code,t,body,std,subs),True))
        for sc,st,line in subs:
            plan.append((sdir/f"{CH}-{sc}_{st}"/"README.md",subj_readme(code,sc,st,line),False))
    return plan

def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument("--root",default=".")
    p.add_argument("--dry-run",action="store_true")
    p.add_argument("--overwrite",action="store_true")
    p.add_argument("--bootstrap",action="store_true")
    a=p.parse_args(argv)
    root=Path(a.root).resolve()
    anchor=root/"01_OPTIONS_ARCHITECTURE"/"01-03_TECHNOLOGIES"/"01-03-01_Q+ATLANTIDE"
    if not anchor.is_dir() and not a.bootstrap:
        p.error(f"Q+ATLANTIDE root not found under {root}; run from repo root, use --root, or pass --bootstrap.")
    cdir=root/RANGE_REL/f"{CH}_{CH_TITLE}"
    plan=build_plan(cdir)
    written=skipped=0
    for fp,content,always in plan:
        exists=fp.exists(); should=(not exists) or always or a.overwrite
        if a.dry_run:
            written+=should; skipped+=(not should); continue
        if not should: skipped+=1; continue
        fp.parent.mkdir(parents=True,exist_ok=True)
        fp.write_text(content,encoding="utf-8"); written+=1
    mode="dry-run" if a.dry_run else CH
    print(f"[{mode}] written={written} skipped={skipped} planned={len(plan)} at {cdir}")
    return 0

if __name__=="__main__":
    try: sys.exit(main())
    except BrokenPipeError: sys.exit(0)