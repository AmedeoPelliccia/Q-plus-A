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
 "000": ("General-Information",
   "Chapter role and derivation, and the agnosticism rule instanced: "
   "this chapter owns requirement classes, grammars and SE discipline; "
   "actual requirements are downstream artifacts. Sections cite their "
   "standards-register anchors undated; a declared absence is preferred "
   "to a false anchor.",
   ""),
 "100": ("Systems-Engineering-Management-and-Planning",
   "SE management as a discipline: the systems-engineering management "
   "plan as an artifact class, process tailoring doctrine, SE roles and "
   "responsibilities classes, and the relationship of SE planning to "
   "programme structure (103 owns the programme; this section owns how "
   "engineering is managed within it).",
   "ISO 18676"),
 "200": ("Requirements-Engineering-and-Management",
   "The requirements discipline: elicitation from mission concepts "
   "(101), requirement classes and quality criteria, allocation and "
   "flow-down doctrine, traceability grammar, and change interfaces "
   "toward configuration management (103). The requirements breakdown "
   "structure belongs to the 103 breakdown family; its content "
   "discipline lives here.",
   "ISO 16404"),
 "300": ("Functional-and-Technical-Specifications",
   "Specification artifact classes: functional specifications, "
   "technical specifications, their structure and content rules, and "
   "their relation to requirement sets and to downstream declaration "
   "schemas.",
   "ISO 21351"),
 "400": ("System-Architecture-Definition-and-Trade-Study-Discipline",
   "The SE side of architecture: functional and physical architecture "
   "definition process, trade-study methodology and decision-record "
   "classes. Mission-architecture content is 101; configuration "
   "constraints are 190-199; this section owns the method.",
   "Register-derived; trade-study sources pending"),
 "500": ("Engineering-Analysis-Models-and-Simulation-Management",
   "Model-management discipline: analysis-model classes, exchange of "
   "mathematical models, simulation requirement classes, fidelity and "
   "validation declaration. Domain models are built and used in their "
   "domains (structural 110, GNC 142, thermal 135); this section owns "
   "how models are declared, exchanged and managed.",
   "ISO 14954 — dynamic/static model exchange; ISO 16781 — control-system simulation; broader engineering-analysis governance register-derived"),
 "600": ("Technology-Readiness-Assessment-and-SE-Integration",
   "100-500 owns the shared maturity, evidence-state and graduation "
   "doctrine; this section owns TRL assessment planning, evidence "
   "integration, technology-insertion decisions and readiness claims "
   "within systems engineering.",
   "ISO 16290"),
 "700": ("Requirement-Verifiability-and-Verification-Planning-Interface",
   "The requirement-side of verification: verifiability as a "
   "requirement quality, verification-method assignment per requirement "
   "class, and the verification cross-reference matrix as the interface "
   "artifact — one interface, two owners: this section defines the "
   "requirement side; the verification programme, execution and "
   "qualification are 105.",
   "ISO 23135 — verification programme owned by 105"),
 "800": ("Model-Based-Systems-Engineering-and-Digital-Continuity",
   "MBSE discipline in the space SE process: model-based specification "
   "and architecture classes, digital continuity of SE artifacts, and "
   "the interface toward digital-twin technology — the technology "
   "domain is the digital band (300-399); the SE-discipline application "
   "is owned here.",
   "Register-derived; MBSE sources pending"),
 "900": ("SE-Products-Evidence-and-Review-Readiness",
   "SE products as evidence classes: SE management plans, requirement "
   "sets and traceability records, specification trees, trade and "
   "decision records, analysis reports — with review readiness toward "
   "programme reviews (103) and the maturity expectations of 100-500. "
   "Documentation precedence is band governance (100-700, 103) and is "
   "consumed, never redefined.",
   "ISO 18676; ISO 21349"),
}

def sec_readme(code, title, body, std):
    L = [f"# {CH}-{code} — {title.replace('-',' ')}", "",
         f"**Chapter:** {CH}_{CH_TITLE} · **Section:** {code}", "",
         body, ""]
    if std:
        L += [f"**Anchoring standards (undated):** {std}", ""]
    L += ["*Subjects are register-gated and follow per-range ratification.*", ""]
    return "\n".join(L)

def ch_readme():
    L=[];A=L.append
    A(f"# {CH}_{CH_TITLE}");A("")
    A(f"**Band:** 100-199_S-STA · **Range:** 100-109 · **Status:** Register-derived chapter — sections cite their anchoring standards from the S-STA standards register; merge constitutes ratification of this chapter section register under S-STA-BAND-RULING v0.4 §6. Source governance: sections cite standards-register anchors where they exist; the absence of a direct anchor does not invalidate a section when its architectural need is established by the ruling, boundary analysis or multiple source classes.");A("")
    A("## Scope");A("");A(SCOPE);A("")
    A("## Concept flow");A("");A(DIAGRAM);A("")
    A("## Section register");A("")
    A("| Section | Title | Anchors |");A("|---|---|---|")
    for code,(t,_,std) in S.items():
        A(f"| {CH}-{code} | [{t.replace('-',' ')}]({CH}-{code}_{t}/) | {std if std else '—'} |")
    A("")
    A("## Boundary summary");A("")
    A("Mission concepts and ConOps: 101 — consumed here as the source of "
      "requirements derivation and architecture definition. Requirement "
      "instances: downstream programme artefacts; the taxonomy holds "
      "classes and grammars, never programme requirements — the same "
      "rule covers specification instances (102-300 owns document "
      "classes), architecture instances (102-400 owns the method), and "
      "executable models (102-500 owns model classes, assumptions, "
      "validation-state metadata and exchange governance). Maturity: "
      "shared doctrine 100-500; TRL assessment and SE integration "
      "102-600. Verification split: verifiability, method allocation and "
      "the traceability interface 102-700; programme governance, "
      "execution, qualification, acceptance and evidence 105. MBSE "
      "split: model semantics, viewpoints and digital continuity "
      "102-800; configuration status, baselines and records 103. "
      "Reviews: product readiness and evidence sufficiency 102-900; "
      "process, authorities, gates and records 103. Assurance and "
      "dependability: 104. Interface control: interface requirements "
      "originate through 102; ICD structures and controlled execution "
      "106. Classes 190-199 constrain architecture definition and shall "
      "not duplicate the SE discipline.")
    A("")
    return "\n".join(L)+"\n"

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
    plan=[(cdir/"README.md",ch_readme(),True)]
    for code,(t,body,std) in S.items():
        plan.append((cdir/f"{CH}-{code}_{t}"/"README.md",sec_readme(code,t,body,std),True))
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