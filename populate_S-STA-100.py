#!/usr/bin/env python3
# =============================================================================
# populate_S-STA-100.py
# Q+ATLANTIDE / S-STA / 100-109 / 100_General-and-Band-Doctrine
# Band doctrine chapter: transcribes ruling S-STA-BAND-RULING v0.4 into
# addresses. Principled exception to section register-gating: doctrine
# sections derive from the ratified ruling, which is their register.
# Sections only (subjects remain register-gated). Idempotent; truthful
# --dry-run; --bootstrap; guarded --overwrite.
# =============================================================================
import argparse, sys
from pathlib import Path

CH = "100"; CH_TITLE = "General-and-Band-Doctrine"
RANGE_REL = ("01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
             "100-199_S-STA/100-109_General-Space-Systems-Engineering-"
             "Assurance-and-Human-Support")

SCOPE = ("The doctrine chapter of the S-STA band: band scope and the "
         "revisitability doctrine, the layer model and agnosticism rule "
         "including the expendable scope declaration, the range register "
         "and navigation, the lifecycle-and-intervention model, the "
         "maturity and graduation discipline, cross-band boundaries, "
         "sources and registers governance, cross-cutting threads, and the "
         "controlled vocabulary. Doctrine sections derive from ruling "
         "S-STA-BAND-RULING v0.4 — their register is the ruling; "
         "technology sections across the band remain register-gated. This doctrine chapter is sections-only by design: its sections are the atomic doctrine units; discipline chapters 101-109 carry dual grain.")

DIAGRAM = """```mermaid
flowchart LR
  D["100<br/>General and Band Doctrine"]
  subgraph R["Ten ranges 100-199"]
    T["100-109 transversal"]
    F["110-189 functional"]
    C["190-199 classes"]
  end
  D -->|"doctrine, vocabulary,<br/>boundaries, threads"| R
  D -.->|"layer model:<br/>declarations live downstream"| DS["Impact studies · PBS · DMC"]
  REG["S-STA standards register<br/>(ISO · SC13/CCSDS · ECSS)"] -.->|"gates technology sections"| F
```"""

S = {
 "000": ("General-Information",
   "How to read the band: chapter roles, the transversal range as the "
   "band's General layer (no per-range General chapter — a deliberate "
   "deviation from the aircraft band's 060-099 pattern, because this "
   "range serves all ten), and the relationship between doctrine "
   "chapters and register-gated technology chapters."),
 "100": ("Band-Scope-and-Revisitability-Doctrine",
   "RATIFIED (ruling v0.4 §1): Documentation intensity follows "
   "revisitability — documentation depth scales with recurrence, "
   "revisitability, configuration persistence and intervention "
   "potential. The band is oriented toward reusable, serviceable and "
   "lifecycle-managed space systems: reusable launch elements, "
   "persistent orbital assets, maintainable stations and habitats, "
   "refuellable and upgradeable spacecraft, recoverable vehicles and "
   "modular infrastructures designed for repeated intervention. "
   "Reusability and serviceability are coupled but distinct lifecycle "
   "properties: a reusable system is intended to perform more than one "
   "operational cycle or mission; a serviceable system permits "
   "inspection, maintenance, repair, replenishment, replacement, "
   "reconfiguration or upgrade; a system may possess either property "
   "without fully possessing the other. The band represents the "
   "persistent information, documentation and operational system, not "
   "only the vehicle."),
 "200": ("Layer-Model-Agnosticism-and-Expendable-Declaration",
   "The three layers: the taxonomy documents technology; type classes "
   "(190-199) constrain configurations; downstream layers declare "
   "instances, applicability and effectivity. The taxonomy names no "
   "programme. Expendable scope declaration (RATIFIED, hosted here per "
   "v0.4): expendable elements are not excluded — they remain subject "
   "to manufacturing, assembly, integration, test, handling, launch, "
   "mission-operation, configuration-control, anomaly and disposal "
   "documentation; lifecycle branches that are physically inapplicable "
   "resolve through effectivity as not applicable and are never "
   "artificially instantiated. The class doctrine at 190 carries the "
   "class-level expression of this rule."),
 "300": ("Range-Register-and-Navigation",
   "The ten ranges of the band and their reading order: 100-109 the "
   "transversal engineering-assurance-and-human-support layer; 110-189 "
   "the functional domains (structures-materials-mechanisms, "
   "propulsion, power-and-thermal, avionics-GNC-autonomy, "
   "communications-and-data, sensors-payloads-and-downstream, on-orbit "
   "operations-servicing-and-maintenance, ground-segment-launch-and-"
   "recovery); 190-199 the system and vehicle classes with the "
   "expansion register. Chapter registers are ratified (ruling §4); "
   "technology sections derive from the standards register per range."),
 "400": ("Lifecycle-and-Intervention-Model",
   "The four declared properties every chapter may reference: "
   "recurrence (how often the system or its class repeats an "
   "operational cycle), revisitability (whether and how the system can "
   "be reached for intervention), configuration persistence (how long "
   "a controlled configuration remains under management), and "
   "intervention potential (which of inspection, maintenance, repair, "
   "replenishment, replacement, reconfiguration, upgrade the design "
   "admits). Documentation structures scale with these properties; "
   "none is assumed, all are declared."),
 "500": ("Maturity-and-Graduation-Discipline",
   "The shared maturity-class discipline (080-200 pattern, promoted to "
   "architecture doctrine) instanced for the band: concepts carry a "
   "declared evidence status; ISO 16290 Technology Readiness Levels "
   "anchor the evidence scale; the M-to-TRL mapping is declared once, "
   "band-independent; graduation moves established concepts to their "
   "functional homes. Range 190-199 consumes this discipline for class "
   "intake (199) and class evidence."),
 "600": ("Cross-Band-Boundaries",
   "RATIFIED (ruling v0.4 §5). S-ATLAS: winged atmospheric flight is "
   "S-ATLAS (082, 096); spaceplane-class systems split by segment — "
   "atmospheric-flight structures and functions reference S-ATLAS, "
   "space-segment systems live here. EPTA: energy and propulsion "
   "technology domain is 400-499; S-STA owns space integration. QCSAA: "
   "quantum technology is 900-999; space application is S-STA. DTTA "
   "boundary — overlay, not duplicate: S-STA owns programme-agnostic "
   "space-system, vehicle, infrastructure and lifecycle architectures "
   "independently of civil, commercial or dual-use sponsorship; DTTA "
   "owns defence-specific mission effects, tactical architectures, "
   "protected payload functions, threat integration, operational "
   "doctrine, security constraints and controlled overlays; dual-use "
   "systems apply DTTA overlays to an S-STA technical baseline without "
   "duplicating the underlying taxonomy."),
 "700": ("Sources-Standards-and-Registers-Governance",
   "Sources inspire structure and never govern it; standards are "
   "referenced undated by number (the undated reference designates the "
   "current edition; currency is verified at citation); manuals and "
   "books are never named in taxonomy content and never reproduced; "
   "crosswalks map, they never govern. The machine-readable standards "
   "register (metadata only, no normative text) gates technology "
   "sections; ISO/TC20/SC14 is the seeded backbone, ISO/TC20/SC13 with "
   "CCSDS and the ECSS E/Q/M branches join on acquisition. The band "
   "SOURCES file records provenance per source with its usage class. "
   "Documentation-precedence doctrine is band governance anchored here "
   "and in 103 (ISO 10789): a declared hierarchy from synthesis "
   "documents through operational rules and procedures to source data, "
   "so every operational statement has one authoritative home and "
   "derived views declare their sources."),
 "800": ("Threads-and-Cross-Cutting-Indexes",
   "Threads map homes and never create them. Declared for the band: "
   "DEBRIS-AND-SUSTAINABILITY — home 108, indexed functions include "
   "design measures and shielding (110-119), passivation provisions "
   "(120-129), disposal and end-of-life operations (170-179), space-"
   "traffic-coordination infrastructure (180-189); and the HYDROGEN "
   "thread space extension — propellant fluids and sampling (124), "
   "cryogenic systems (136), with declared synergy toward the aircraft "
   "band's cryo-electric chapters."),
 "900": ("Glossary-and-Controlled-Vocabulary",
   "Controlled forms of the band. On-Orbit is the controlled form "
   "(never In-Orbit) per ruling v0.4. S-STA expands to Sustainable "
   "Space Technology Architecture and is not an ASD S-Series "
   "specification. Reusable, serviceable and expendable carry the "
   "definitions of 100-100 and 100-200. Mapping, applicability, "
   "effectivity, instance and delta carry the downstream-layer "
   "meanings; declarations live downstream, never in the taxonomy. "
   "Terminology entries grow here as chapters author their sections."),
}

def sec_readme(code, title, body):
    return (f"# {CH}-{code} — {title.replace('-',' ')}\n\n"
            f"**Chapter:** {CH}_{CH_TITLE} · **Section:** {code}\n\n"
            f"{body}\n\n"
            f"*Subjects are register-gated and follow per-range ratification.*\n")

def ch_readme():
    L=[];A=L.append
    A(f"# {CH}_{CH_TITLE}");A("")
    A(f"**Band:** 100-199_S-STA · **Range:** 100-109 · **Status:** Doctrine chapter — sections derive from ruling S-STA-BAND-RULING v0.4 (the ruling is their register); technology sections across the band remain register-gated. This doctrine chapter is sections-only by design: its sections are the atomic doctrine units; discipline chapters 101-109 carry dual grain.");A("")
    A("## Scope");A("");A(SCOPE);A("")
    A("## Band context");A("");A(DIAGRAM);A("")
    A("## Section register");A("")
    A("| Section | Title |");A("|---|---|")
    for code,(t,_) in S.items():
        A(f"| {CH}-{code} | [{t.replace('-',' ')}]({CH}-{code}_{t}/) |")
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
    for code,(t,body) in S.items():
        plan.append((cdir/f"{CH}-{code}_{t}"/"README.md",sec_readme(code,t,body),True))
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
    