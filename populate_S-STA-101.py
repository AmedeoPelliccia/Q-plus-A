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
 "000": ("General-Information",
   "Chapter role, derivation and the discipline-versus-execution line "
   "instanced: mission-architecture and operational-concept doctrine is "
   "owned here; operational execution, procedures and their "
   "documentation are 170-179. Sections derive from the standards "
   "register and the ratified ruling; each declares its anchors "
   "undated. Reconciled register v0.2.",
   ""),
 "100": ("Mission-Architecture-Classes-and-Segments",
   "The elements and classes of a mission architecture: space, launch, "
   "ground and user segments; orbital regimes (LEO, MEO, GEO, cislunar, "
   "interplanetary) and mission types (observation, communications, "
   "science, logistics, servicing, demonstration); crewed and uncrewed "
   "as an architecture dimension (human-systems implications 109, "
   "assurance 104, autonomy technology 144 and 149); and the trade "
   "space across single-spacecraft, constellation, serviced-platform "
   "and multi-vehicle architectures. Architecture selection references "
   "the lifecycle-and-intervention model (100-400): recurrence and "
   "intervention potential are architecture drivers, not afterthoughts. "
   "Mission classes cut across system and vehicle classes (190-199) "
   "and never duplicate them.",
   "Register-derived; direct architecture source pending"),
 "200": ("Concept-of-Operations-Doctrine",
   "Concept-of-operations doctrine: structure and content classes of a "
   "ConOps, operational scenario classes, nominal and contingency "
   "concept coverage, and the relationship to requirements — 102 "
   "consumes what this section defines.",
   "ISO 14711"),
 "300": ("Mission-Phases-and-Multi-Cycle-Timeline-Model",
   "The band's phase model: pre-launch integration, launch and ascent, "
   "early operations and commissioning, nominal operations, extended "
   "operations, servicing and intervention windows, and end-of-life. "
   "Multi-cycle missions are first-class: for reusable elements the "
   "model repeats — recovery, refurbishment and return-to-flight are "
   "phases, not exceptions; for serviced assets, intervention windows "
   "partition nominal operations. Physically inapplicable phases "
   "resolve through effectivity as not applicable (100-200 rule). "
   "Phase gates and reviews are programme matter (103); disposal "
   "doctrine is 108 with execution at 178.",
   "ISO 14300-1; ISO 21349"),
 "400": ("Mission-Profiles-and-Design-Reference-Missions",
   "Design reference missions and profiles as concept artifacts: "
   "mission timelines, orbit and trajectory envelopes, energy and "
   "delta-v budgets at concept level, and profile classes that "
   "downstream layers instantiate.",
   ""),
 "500": ("Operability-and-Operations-Driven-Design",
   "Operability as a design discipline: operability requirement "
   "classes, operations-driven design criteria, autonomy-level "
   "selection doctrine (technology in 144 and 149), and the "
   "operability assessment as an evidence class. The revisitability "
   "doctrine operationalized: intervention windows and servicing "
   "opportunities are concept-phase decisions.",
   "ISO 14950 — uncrewed-spacecraft baseline"),
 "600": ("Commissioning-and-Early-Operations-Doctrine",
   "Doctrine of initialization and commissioning: the initialization-"
   "plan class, the commissioning-report class, entry criteria into "
   "nominal operations, and commissioning of serviced or reconfigured "
   "assets after intervention — recommissioning is commissioning; the "
   "same doctrine applies per cycle. Execution is 171.",
   "ISO 10784-1/-2/-3"),
 "700": ("Serviced-and-Revisitable-Mission-Architectures",
   "The band's signature section: mission architectures built around "
   "on-orbit servicing, refuelling, upgrade and retrieval; servicer-"
   "and-client role doctrine; intervention-window planning. "
   "Serviceability is a mission-architecture decision before it is a "
   "vehicle property. Rendezvous, docking and servicing execution are "
   "172-174; docking and separation structures are 117.",
   "ISO 24330 — RPO/OOS anchor"),
 "800": ("Multi-Element-Fleet-and-Campaign-Concepts",
   "Architectures of many elements: constellations, fleets, staged "
   "campaigns and shared-infrastructure concepts; fleet-level phasing "
   "and replenishment-and-replacement doctrine. Constellation classes "
   "are 192; fleet operations automation is 179.",
   ""),
 "900": ("Mission-Concept-Products-Evidence-and-Review-Readiness",
   "Concept-phase products and their review readiness: ConOps "
   "documents, DRM sets, operability assessments, commissioning plans "
   "and reports as evidence classes, with the concept-maturity "
   "expectations of 100-500. Documentation-precedence doctrine is band "
   "governance — 100-700 and 103 own it; this section consumes it and "
   "never redefines it. Reviews as programme events are 103.",
   "ISO 14711; ISO 16290; ISO 21349; ISO 23135"),
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
    A("Concepts, classifications, architectural timelines and concept "
      "products here; operational execution 170-179 (commissioning 171, "
      "RPO/OOS 172-174, fleet 179). Requirements and systems engineering: "
      "102. Programme structure, configuration, documentation and "
      "reviews: 103. Assurance and dependability: 104. Human systems: "
      "109. End of life: lifecycle concept 101-300, debris and disposal "
      "doctrine 108, execution 178. System and vehicle classes: 190-199 "
      "— mission classes cross-cut and never reproduce their physical "
      "configuration taxonomies. Maturity: applied through 100-500; ISO "
      "16290 supports technology-readiness evidence and does not govern "
      "documentation precedence (band governance: 100-700 and 103).")
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