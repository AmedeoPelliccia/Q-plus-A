#!/usr/bin/env python3
# =============================================================================
# populate_S-STA-103.py
# Q+ATLANTIDE / S-STA / 100-109 / 103_Programme-Configuration-and-
# Information-Management. Register-derived sections; anchors cited undated;
# merge constitutes ratification of this chapter section register (ruling
# v0.4 §6). Sections only; subjects register-gated. Idempotent; truthful
# --dry-run; --bootstrap; guarded --overwrite.
# =============================================================================
import argparse, sys
from pathlib import Path

CH = "103"; CH_TITLE = "Programme-Configuration-and-Information-Management"
RANGE_REL = ("01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
             "100-199_S-STA/100-109_General-Space-Systems-Engineering-"
             "Assurance-and-Human-Support")

SCOPE = ("Programme, configuration and information management as "
         "discipline doctrine: programme structuring and the management "
         "framework, breakdown structures and the downstream-mapping "
         "anchor, configuration management, information and documentation "
         "management, reviews and gates, programme risk management, work "
         "definition and statements of work, lessons learned and "
         "knowledge management, and management products with records. "
         "This chapter owns management-discipline doctrine and artifact "
         "classes; actual programme structures, baselines, registers and "
         "records are downstream artifacts and are never instantiated in "
         "the taxonomy. Mission concepts are 101; systems engineering is "
         "102; assurance, dependability, non-conformance and problem "
         "solving are 104; verification execution is 105.")

DIAGRAM = """```mermaid
flowchart LR
  FR["103-100 Programme structuring<br/>and management framework"] --> BD["103-200 Breakdown structures,<br/>downstream-mapping anchor"] --> CM["103-300 Configuration<br/>management"] --> IM["103-400 Information and<br/>documentation management"]
  RV["103-500 Reviews<br/>and gates"] --- FR
  RK["103-600 Programme<br/>risk management"] --- FR
  SW["103-700 Work definition<br/>and statements of work"] --- FR
  LL["103-800 Lessons learned and<br/>knowledge management"] --- IM
  CM --> EV["103-900 Management products,<br/>evidence and records"]
  BD -. "maps onto the taxonomy;<br/>declarations live downstream" .-> DS["Impact studies · PBS · DMC"]
  CM -. "requirement change" .-> X102["102-200"]
  CM -. "as-verified configuration" .-> X105["105"]
  RV -. "readiness and evidence<br/>sufficiency" .-> X1029["101-900 · 102-900"]
  RK -. "safety and dependability<br/>analyses" .-> X104["104"]
  IM -. "precedence doctrine<br/>co-anchor" .-> X100["100-700"]
```"""

S = {
 "000": ('General-Information',
   'Chapter role and derivation, and the governance line instanced: management-discipline doctrine and artifact classes are owned here; actual programme structures, baselines and records are downstream. Sections cite standards-register anchors undated; a declared absence is preferred to a false anchor.',
   '',
   [('010', 'Derivation-and-Governance-Line', 'Discipline and classes here; structures, baselines and records downstream.'), ('020', 'Vocabulary-Interface', 'Programme-management vocabulary anchor (ISO 10795 at 103-900).')]),
 "100": ('Programme-Structuring-and-Management-Framework',
   'The management framework of a space project as doctrine: programme structuring, project organization classes, management-framework definition and the phase-gate interface — the lifecycle phase model is 101-300; the gates that punctuate it are governed here.',
   'ISO 14300-1; ISO 23462; ISO 11893',
   [('110', 'Programme-Structuring-Classes', 'Project structuring classes (ISO 14300-1).'), ('120', 'Project-Organization-Classes', 'Organization classes (ISO 11893).'), ('130', 'Management-Framework-Definition', 'Framework definition doctrine (ISO 23462).'), ('140', 'Phase-Gate-Interface', 'Gates governing the 101-300 phase model.')]),
 "200": ('Breakdown-Structures-and-Downstream-Mapping-Anchor',
   "The breakdown-structure family as recognized discipline: specification and requirements, functional, product, work, cost, business and organizational breakdowns, with the open clause admitting further structures — including economic and contribution-accounting structures — that serve project success. The taxonomy is the reference architecture onto which breakdown structures map; it is not itself a programme breakdown. This section anchors the downstream-mapping doctrine of both bands' interface chapters.",
   'ISO 27026',
   [('210', 'Breakdown-Structure-Family', 'Specification, functional, product, work, cost, business, organizational (ISO 27026).'), ('220', 'Open-Clause-and-Additional-Structures', 'Further structures — including economic and contribution-accounting — under the open clause.'), ('230', 'Taxonomy-as-Reference-Architecture', 'The taxonomy is what breakdowns map onto; not itself a programme breakdown.'), ('240', 'Interface-to-Downstream-Mapping', "Anchor of both bands' interface-chapter doctrine.")]),
 "300": ('Configuration-Management',
   'Configuration management as discipline: configuration-item identification classes, baseline classes, change-control doctrine and configuration-status accounting. Requirement-change interfaces are 102-200; the as-verified configuration evidence is 105; baseline instances are downstream.',
   'ISO 21886',
   [('310', 'Configuration-Item-Identification', 'CI identification classes (ISO 21886).'), ('320', 'Baseline-Classes', 'Baseline classes; instances downstream.'), ('330', 'Change-Control-Doctrine', 'Change control; requirement change 102-200.'), ('340', 'Configuration-Status-Accounting', 'Status accounting; as-verified evidence 105.')]),
 "400": ('Information-and-Documentation-Management',
   'Information and documentation management as discipline: document and record classes, identification and retention doctrine, and the operationalization of the documentation-precedence doctrine — band governance stated at 100-700, co-anchored here. Operational documentation classes are 170; data standards and protocols are 156.',
   'ISO 10789',
   [('410', 'Document-and-Record-Classes', 'Document and record classes (ISO 10789).'), ('420', 'Identification-and-Retention', 'Identification and retention doctrine.'), ('430', 'Precedence-Operationalization', 'Operationalizing the 100-700 precedence doctrine.')]),
 "500": ('Reviews-and-Gates',
   "Review governance: review classes, authorities, entry and exit criteria classes, gate doctrine and review records. Product readiness and evidence sufficiency are the producing chapters' matter (101-900, 102-900); the process, authority and gates are owned here.",
   'ISO 21349',
   [('510', 'Review-Classes-and-Authorities', 'Review classes and authorities (ISO 21349).'), ('520', 'Entry-and-Exit-Criteria', 'Criteria classes; readiness with producing chapters.'), ('530', 'Gate-Doctrine-and-Records', 'Gate doctrine and review records.')]),
 "600": ('Programme-Risk-Management',
   'Programme risk as discipline: risk classes, assessment and treatment doctrine, risk-register artifact classes. Safety, dependability and their probabilistic analyses are 104; this section owns programme-level risk governance.',
   'ISO 17666',
   [('610', 'Risk-Classes', 'Programme risk classes (ISO 17666).'), ('620', 'Assessment-and-Treatment', 'Assessment and treatment doctrine.'), ('630', 'Risk-Register-Class', 'Risk-register artifact class; safety analyses 104.')]),
 "700": ('Work-Definition-and-Statements-of-Work',
   'Work definition as discipline: statement-of-work artifact classes, work-package definition doctrine and their relation to the work breakdown of 103-200. Actual statements of work are downstream.',
   'ISO 17255',
   [('710', 'Statement-of-Work-Class', 'SOW artifact classes (ISO 17255).'), ('720', 'Work-Package-Definition', 'Work-package definition doctrine.'), ('730', 'Relation-to-Work-Breakdown', 'Relation to the 103-200 work breakdown.')]),
 "800": ('Lessons-Learned-and-Knowledge-Management',
   'Experience capture as discipline: lessons-learned classes, knowledge retention and reuse doctrine, and the feed toward doctrine evolution across the band. Closed-loop problem solving and non-conformance control are 104.',
   'ISO 16192',
   [('810', 'Lessons-Learned-Classes', 'Lessons-learned classes (ISO 16192).'), ('820', 'Knowledge-Retention-and-Reuse', 'Retention and reuse doctrine.'), ('830', 'Doctrine-Evolution-Feed', 'Feeding lessons into band doctrine; problem solving 104-600.')]),
 "900": ('Management-Products-Evidence-and-Records',
   'Management products as evidence classes: management plans, breakdown-structure definitions, baselines-as-records, review and risk records, and the controlled vocabulary of programme management. Documentation precedence is consumed from 100-700 and 103-400, never redefined.',
   'ISO 10795; ISO 21349',
   [('910', 'Management-Plan-Classes', 'Management plan and product classes.'), ('920', 'Baselines-as-Records', 'Baselines and records as evidence classes.'), ('930', 'Vocabulary-and-Records', 'Controlled vocabulary and record governance (ISO 10795).')]),
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