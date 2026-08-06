#!/usr/bin/env python3
# =============================================================================
# populate_S-STA-104.py
# Q+ATLANTIDE / S-STA / 100-109 / 104_Product-Assurance-Safety-Dependability-
# and-Quality. First dual-grain S-STA chapter: register-derived SECTIONS and
# SUBJECTS (authority instruction), per-subject anchors where they exist,
# declared absence where they do not. Merge constitutes ratification of this
# chapter register (ruling v0.4 §6). Idempotent; truthful --dry-run;
# --bootstrap; guarded --overwrite.
# =============================================================================
import argparse, sys
from pathlib import Path

CH = "104"; CH_TITLE = "Product-Assurance-Safety-Dependability-and-Quality"
RANGE_REL = ("01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
             "100-199_S-STA/100-109_General-Space-Systems-Engineering-"
             "Assurance-and-Human-Support")

SCOPE = ("Product assurance, safety, dependability and quality as "
         "discipline doctrine at section and subject grain: the assurance "
         "framework, system safety, dependability and reliability, "
         "software product assurance, parts-materials-and-processes "
         "assurance, non-conformance and problem resolution, product "
         "characteristics and critical items, assurance for serviceable "
         "and reusable systems, and assurance products with review "
         "readiness. This chapter owns assurance doctrine and artifact "
         "classes; actual assurance plans, records and dispositions are "
         "downstream. Requirements discipline is 102; programme "
         "governance, configuration, reviews and programme risk are 103; "
         "verification execution and qualification are 105; parts and "
         "EMC engineering are 146; FDIR technology is 147; range safety "
         "and flight-safety-system infrastructure are 189.")

DIAGRAM = """```mermaid
flowchart LR
  FR["104-100 Product-assurance<br/>framework"] --> SF["104-200 System<br/>safety"]
  FR --> DP["104-300 Dependability<br/>and reliability"]
  FR --> SW["104-400 Software<br/>product assurance"]
  FR --> PM["104-500 Parts, materials,<br/>processes assurance"]
  NC["104-600 Non-conformance and<br/>problem resolution"] --- FR
  KC["104-700 Product characteristics<br/>and critical items"] --- FR
  RS["104-800 Assurance for serviceable<br/>and reusable systems"] --- DP
  FR --> EV["104-900 Assurance products,<br/>evidence, review readiness"]
  SF -. "range safety and FSS<br/>infrastructure" .-> X189["189"]
  DP -. "FDIR technology" .-> X147["147"]
  SW -. "flight software · AI" .-> X144["144 · 149"]
  PM -. "parts and EMC engineering" .-> X146["146"]
  EV -. "reviews and gates" .-> X103["103-500"]
  FR -. "verification and<br/>qualification" .-> X105["105"]
```"""

S = {
 "000": ("General-Information",
   "Chapter role and derivation at dual grain: sections and subjects "
   "derive from the standards register; per-subject anchors are cited "
   "where they exist and absence is declared where they do not. "
   "Assurance doctrine and artifact classes are owned here; plans, "
   "records and dispositions are downstream.",
   "",
   [("010","Chapter-Doctrine-and-Derivation","Dual-grain derivation rule and the instance line: classes here, records downstream."),
    ("020","Assurance-Vocabulary-and-Classes","Controlled assurance vocabulary; programme-management vocabulary interface (ISO 10795 at 103-900)."),
    ("030","Relationship-to-Programme-and-Engineering","How assurance relates to 102 requirements and 103 governance without duplicating either.")]),
 "100": ("Product-Assurance-Framework",
   "The assurance framework: PA programme and planning classes, quality "
   "assurance requirements, capability-based assurance and "
   "class-tailored assurance for commercial systems.",
   "ISO 14300-2; ISO 27025",
   [("110","PA-Programme-and-Planning-Classes","Product-assurance programme structure and planning artifact classes (ISO 14300-2)."),
    ("120","Quality-Assurance-Requirements","Quality-assurance requirement classes for space projects (ISO 27025)."),
    ("130","Capability-Based-SDQA","Capability-based safety, dependability and quality assurance management (ISO 18667)."),
    ("140","Class-Tailored-and-Commercial-Assurance","Assurance tailoring by system class, including commercial-satellite profiles (ISO 20188).")]),
 "200": ("System-Safety",
   "System safety as discipline: safety programme classes, hazard "
   "analysis, probabilistic risk assessment and the interfaces of "
   "safety in operations. Launch-site operational safety and "
   "flight-safety-system infrastructure are 189; programme risk is "
   "103-600.",
   "ISO 14620-1",
   [("210","System-Safety-Programme-Classes","Safety programme and safety-case artifact classes (ISO 14620-1)."),
    ("220","Hazard-Analysis-Classes","Hazard identification and analysis method classes across lifecycle phases."),
    ("230","Probabilistic-Risk-Assessment","PRA discipline and its evidence classes (ISO 11231)."),
    ("240","Safety-in-Operations-Interfaces","Doctrine interfaces toward launch-site safety and flight-safety systems (ISO 14620-2, ISO 14620-3; infrastructure 189).")]),
 "300": ("Dependability-and-Reliability",
   "Dependability assurance: reliability, availability and "
   "maintainability doctrine and analysis classes. Maintainability "
   "connects to the band's lifecycle-and-intervention model (100-400); "
   "FDIR technology is 147.",
   "ISO 23460",
   [("310","Dependability-Assurance-Requirements","Dependability assurance requirement classes (ISO 23460)."),
    ("320","Reliability-Analysis-Classes","Reliability prediction and analysis method classes."),
    ("330","Availability-and-Maintainability-Doctrine","Availability and maintainability as declared properties serving serviceable systems (100-400)."),
    ("340","FDIR-Assurance-Interface","Assurance view of fault management; the technology is 147.")]),
 "400": ("Software-Product-Assurance",
   "Software product assurance: SPA requirements, criticality classes "
   "and the assurance of autonomy and learning-enabled functions. "
   "Flight software engineering is 144; AI-and-autonomous-systems "
   "technology and its governance discipline are 149.",
   "ISO 22893",
   [("410","SPA-Requirements-and-Planning","Software product assurance requirement and planning classes (ISO 22893)."),
    ("420","Software-Criticality-Classes","Criticality classification doctrine and its assurance consequences."),
    ("430","Assurance-of-Autonomy-and-Learning-Enabled-Functions","Assurance classes for autonomous and learning-enabled functions; frozen-model discipline per 149.")]),
 "500": ("Parts-Materials-and-Processes-Assurance",
   "Assurance of parts, materials and processes: EEE parts assurance, "
   "materials and processes assurance, off-the-shelf utilization and "
   "provenance control. Parts and radiation-effects engineering are "
   "146; materials test methods are 114.",
   "ISO 14621-1",
   [("510","EEE-Parts-Assurance","EEE parts management and control assurance classes (ISO 14621-1; engineering 146)."),
    ("520","Materials-and-Processes-Assurance","Materials and processes assurance including flammability and compatibility doctrine (ISO 14624 series; methods 114, propellant fluids 124)."),
    ("530","Off-the-Shelf-and-COTS-Utilization","Off-the-shelf item utilization doctrine (ISO 21350; COTS radiation evaluation with 146)."),
    ("540","Counterfeit-and-Provenance-Control","Provenance and counterfeit-avoidance classes — register-derived; sources pending.")]),
 "600": ("Non-Conformance-and-Problem-Resolution",
   "The closed loop of failure: non-conformance control, failure "
   "reporting analysis and corrective action, closed-loop problem "
   "solving, and alerts. Lessons learned as knowledge discipline is "
   "103-800.",
   "ISO 23461",
   [("610","Non-Conformance-Control","Non-conformance control system classes (ISO 23461)."),
    ("620","FRACA","Failure reporting, analysis and corrective action classes (ISO 5461)."),
    ("630","Closed-Loop-Problem-Solving","Closed-loop problem-solving management classes (ISO 18238)."),
    ("640","Alerts-and-Escape-Management","Alert and escape handling classes — register-derived; sources pending.")]),
 "700": ("Product-Characteristics-and-Critical-Items",
   "Management of product characteristics and critical items as "
   "assurance discipline; traceability of characteristics interfaces "
   "configuration management (103-300).",
   "ISO 19826",
   [("710","Key-and-Critical-Characteristics","Key-characteristic identification and management classes (ISO 19826)."),
    ("720","Critical-Items-Control-Classes","Critical-item lists and control doctrine."),
    ("730","Characteristics-Traceability","Traceability of characteristics through configuration records (103-300).")]),
 "800": ("Assurance-for-Serviceable-and-Reusable-Systems",
   "The band's signature assurance section: assurance across multiple "
   "cycles and interventions — reuse and refurbishment assurance, "
   "on-orbit intervention assurance, life extension and "
   "recertification, and assurance data across cycles. No dedicated "
   "SC14 standard yet exists for this discipline: the sections "
   "document ahead of the standards, with sources declared pending.",
   "Register-derived; serviceability-assurance sources pending",
   [("810","Reuse-and-Refurbishment-Assurance","Return-to-flight assurance classes for reusable elements (propulsion reusability 128; recovery infrastructure 186)."),
    ("820","On-Orbit-Intervention-Assurance","Assurance of serviced assets before, during and after intervention (operations 174)."),
    ("830","Life-Extension-and-Recertification-Doctrine","Recertification and life-extension assurance classes per cycle."),
    ("840","Assurance-Data-Across-Cycles","Cycle-indexed assurance records doctrine (information management 103-400).")]),
 "900": ("Assurance-Products-Evidence-and-Review-Readiness",
   "Assurance products as evidence classes: plans, records, safety "
   "cases, dependability analyses and their review readiness. Review "
   "process and gates are 103-500; documentation precedence is band "
   "governance, consumed here.",
   "ISO 27025; ISO 21349",
   [("910","Assurance-Plans-and-Records-Classes","Plan and record classes across the assurance disciplines."),
    ("920","Assurance-Evidence-in-Reviews","Evidence sufficiency doctrine toward programme reviews (103-500)."),
    ("930","Assurance-Metrics-and-Indicators","Assurance metric classes — register-derived; sources pending.")]),
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
    A("## Assurance map");A("");A(DIAGRAM);A("")
    A("## Section register");A("")
    A("| Section | Title | Subjects | Anchors |");A("|---|---|---|---|")
    for code,(t,_,std,subs) in S.items():
        A(f"| {CH}-{code} | [{t.replace('-',' ')}]({CH}-{code}_{t}/) | {len(subs)} | {std if std else '—'} |")
    A("")
    A("## Boundary summary");A("")
    A("Assurance doctrine and classes here; plans, records and "
      "dispositions downstream. Requirements discipline 102; programme "
      "governance, configuration, reviews and programme risk 103 — "
      "programme risk 103-600 versus safety and probabilistic analyses "
      "104-200. Verification execution and qualification 105. Parts and "
      "EMC engineering 146; assurance of parts 104-500. Flight software "
      "144 and AI technology 149; their assurance 104-400. FDIR "
      "technology 147; its assurance view 104-340. Range safety and "
      "flight-safety-system infrastructure 189; safety doctrine here. "
      "Materials methods 114 and propellant fluids 124; their assurance "
      "doctrine 104-520. Lessons learned 103-800; the failure loop "
      "104-600. Serviceability assurance 104-800 with operations 170-179 "
      "and recovery 186. Classes 190-199 constrain and shall not "
      "duplicate assurance discipline.")
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