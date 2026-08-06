#!/usr/bin/env python3
# =============================================================================
# populate_S-STA-101.py
# Q+ATLANTIDE / S-STA / 100-109 / 101_Mission-Architecture-and-Operational-
# Concepts. Register-derived sections: each cites its anchoring standards
# (undated) from the S-STA standards register; merge constitutes the
# per-range ratification the ruling's §6 requires. Sections only; subjects
# remain register-gated. Idempotent; truthful --dry-run; --bootstrap.
# =============================================================================
import argparse, sys
from pathlib import Path

CH = "101"; CH_TITLE = "Mission-Architecture-and-Operational-Concepts"
RANGE_REL = ("01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
             "100-199_S-STA/100-109_General-Space-Systems-Engineering-"
             "Assurance-and-Human-Support")

SCOPE = ("Mission-level architecture and operational concepts as discipline "
         "doctrine: mission classes and typologies, concept-of-operations "
         "doctrine, mission phases and lifecycle model, design reference "
         "missions and profiles, operability doctrine, serviced and "
         "revisitable mission architectures, crewed and uncrewed concepts, "
         "multi-element and campaign architectures, and concept-phase "
         "evidence. This chapter owns concepts and doctrine; operational "
         "execution is 170-179 (commissioning doctrine here, commissioning "
         "operations 171); programme structure and reviews are 103; "
         "system and vehicle classes are 190-199 — mission classes cut "
         "across them and never duplicate them.")

DIAGRAM = """```mermaid
flowchart LR
  MC["101-100 Mission architecture<br/>classes and segments"] --> CO["101-200<br/>Concept of operations"] --> PH["101-300 Mission phases and<br/>multi-cycle timeline"] --> PR["101-400 Profiles and<br/>design reference missions"]
  OP["101-500 Operability and<br/>operations-driven design"] --- CO
  CM["101-600 Commissioning and<br/>early-operations doctrine"] --- PH
  SV["101-700 Serviced and<br/>revisitable architectures"] --- PH
  ME["101-800 Multi-element, fleet<br/>and campaign concepts"] --- PR
  PR --> EV["101-900 Concept products,<br/>evidence, review readiness"]
  PH -. "operational execution" .-> X170["170-179"]
  CM -. "commissioning execution" .-> X171["171"]
  PH -. "phase gates and reviews" .-> X103["103"]
  MC -. "class constraints" .-> X190["190-199"]
  SV -. "RPO/OOS execution" .-> X172["172-174"]
  EV -. "maturity application" .-> X100["100-500"]
```"""

S = {
 "000": ('General-Information',
   'Chapter role, derivation and the discipline-versus-execution line instanced: mission-architecture and operational-concept doctrine is owned here; operational execution, procedures and their documentation are 170-179. Sections derive from the standards register and the ratified ruling; each declares its anchors undated. Reconciled register v0.2.',
   '',
   [('010', 'Derivation-and-Anchor-Rule', 'Dual-grain derivation; anchors undated; declared absence over false anchors.'), ('020', 'Discipline-versus-Execution-Line', 'Concepts and doctrine here; operational execution 170-179.')]),
 "100": ('Mission-Architecture-Classes-and-Segments',
   'The elements and classes of a mission architecture: space, launch, ground and user segments; orbital regimes (LEO, MEO, GEO, cislunar, interplanetary) and mission types (observation, communications, science, logistics, servicing, demonstration); crewed and uncrewed as an architecture dimension (human-systems implications 109, assurance 104, autonomy technology 144 and 149); and the trade space across single-spacecraft, constellation, serviced-platform and multi-vehicle architectures. Architecture selection references the lifecycle-and-intervention model (100-400): recurrence and intervention potential are architecture drivers, not afterthoughts. Mission classes cut across system and vehicle classes (190-199) and never duplicate them.',
   'Register-derived; direct architecture source pending',
   [('110', 'Segment-Model', 'Space, launch, ground and user segments as architecture elements.'), ('120', 'Regimes-and-Mission-Types', 'Orbital regimes and mission-type classes; never vehicle classes (190-199).'), ('130', 'Crewed-and-Uncrewed-Dimension', 'Human presence as an architecture decision (109, 104, 144, 149 interfaces).'), ('140', 'Architecture-Trade-Space', 'Single-spacecraft to serviced-platform and multi-vehicle trade space; 100-400 drivers.')]),
 "200": ('Concept-of-Operations-Doctrine',
   'Concept-of-operations doctrine: structure and content classes of a ConOps, operational scenario classes, nominal and contingency concept coverage, and the relationship to requirements — 102 consumes what this section defines.',
   'ISO 14711',
   [('210', 'ConOps-Structure-and-Content', 'The ConOps artifact class: required structure and content (ISO 14711).'), ('220', 'Operational-Scenario-Classes', 'Scenario classes covered by a concept of operations.'), ('230', 'Nominal-and-Contingency-Coverage', 'Coverage doctrine across nominal and contingency concepts.')]),
 "300": ('Mission-Phases-and-Multi-Cycle-Timeline-Model',
   "The band's phase model: pre-launch integration, launch and ascent, early operations and commissioning, nominal operations, extended operations, servicing and intervention windows, and end-of-life. Multi-cycle missions are first-class: for reusable elements the model repeats — recovery, refurbishment and return-to-flight are phases, not exceptions; for serviced assets, intervention windows partition nominal operations. Physically inapplicable phases resolve through effectivity as not applicable (100-200 rule). Phase gates and reviews are programme matter (103); disposal doctrine is 108 with execution at 178.",
   'ISO 14300-1; ISO 21349',
   [('310', 'Phase-Model', 'The band phase model from integration to end-of-life.'), ('320', 'Multi-Cycle-and-Return-to-Flight-Phases', 'Recovery, refurbishment and return-to-flight as first-class phases.'), ('330', 'Intervention-Windows', 'Servicing windows partitioning nominal operations.'), ('340', 'Phase-Effectivity-Resolution', 'Physically inapplicable phases resolve as not applicable (100-200 rule).')]),
 "400": ('Mission-Profiles-and-Design-Reference-Missions',
   'Design reference missions and profiles as concept artifacts: mission timelines, orbit and trajectory envelopes, energy and delta-v budgets at concept level, and profile classes that downstream layers instantiate.',
   '',
   [('410', 'Design-Reference-Mission-Classes', 'DRM classes instantiated downstream.'), ('420', 'Profile-Timelines-and-Envelopes', 'Timeline, orbit and trajectory envelope classes.'), ('430', 'Concept-Level-Budgets', 'Energy and delta-v budget classes at concept level.')]),
 "500": ('Operability-and-Operations-Driven-Design',
   'Operability as a design discipline: operability requirement classes, operations-driven design criteria, autonomy-level selection doctrine (technology in 144 and 149), and the operability assessment as an evidence class. The revisitability doctrine operationalized: intervention windows and servicing opportunities are concept-phase decisions.',
   'ISO 14950 — uncrewed-spacecraft baseline',
   [('510', 'Operability-Requirement-Classes', 'Operability requirement classes (ISO 14950 — uncrewed baseline).'), ('520', 'Operations-Driven-Design-Criteria', 'Design criteria derived from operations.'), ('530', 'Autonomy-Level-Selection', 'Autonomy-level selection doctrine; technology 144 and 149.')]),
 "600": ('Commissioning-and-Early-Operations-Doctrine',
   'Doctrine of initialization and commissioning: the initialization-plan class, the commissioning-report class, entry criteria into nominal operations, and commissioning of serviced or reconfigured assets after intervention — recommissioning is commissioning; the same doctrine applies per cycle. Execution is 171.',
   'ISO 10784-1/-2/-3',
   [('610', 'Initialization-Plan-Class', 'The initialization-plan artifact class (ISO 10784-2).'), ('620', 'Commissioning-Report-Class', 'The commissioning-report artifact class (ISO 10784-3).'), ('630', 'Recommissioning-After-Intervention', 'Recommissioning is commissioning; same doctrine per cycle.')]),
 "700": ('Serviced-and-Revisitable-Mission-Architectures',
   "The band's signature section: mission architectures built around on-orbit servicing, refuelling, upgrade and retrieval; servicer-and-client role doctrine; intervention-window planning. Serviceability is a mission-architecture decision before it is a vehicle property. Rendezvous, docking and servicing execution are 172-174; docking and separation structures are 117.",
   'ISO 24330 — RPO/OOS anchor',
   [('710', 'Servicer-and-Client-Roles', 'Role doctrine of servicer and client architectures (ISO 24330).'), ('720', 'Serviceable-Architecture-Patterns', 'Architecture patterns built for intervention; structures 117.'), ('730', 'Intervention-Window-Planning', 'Concept-level planning of intervention opportunities.')]),
 "800": ('Multi-Element-Fleet-and-Campaign-Concepts',
   'Architectures of many elements: constellations, fleets, staged campaigns and shared-infrastructure concepts; fleet-level phasing and replenishment-and-replacement doctrine. Constellation classes are 192; fleet operations automation is 179.',
   '',
   [('810', 'Constellation-and-Fleet-Concepts', 'Multi-element concept classes; configuration classes 192.'), ('820', 'Campaign-and-Staged-Architectures', 'Staged and campaign architecture classes.'), ('830', 'Replenishment-and-Replacement', 'Fleet replenishment-and-replacement doctrine; execution 179.')]),
 "900": ('Mission-Concept-Products-Evidence-and-Review-Readiness',
   'Concept-phase products and their review readiness: ConOps documents, DRM sets, operability assessments, commissioning plans and reports as evidence classes, with the concept-maturity expectations of 100-500. Documentation-precedence doctrine is band governance — 100-700 and 103 own it; this section consumes it and never redefines it. Reviews as programme events are 103.',
   'ISO 14711; ISO 16290; ISO 21349; ISO 23135',
   [('910', 'Concept-Product-Classes', 'ConOps, DRM sets, operability assessments, commissioning plans and reports.'), ('920', 'Evidence-and-Maturity-Expectations', 'Concept-maturity expectations per 100-500.'), ('930', 'Review-Readiness', 'Readiness toward programme reviews; process 103-500.')]),
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