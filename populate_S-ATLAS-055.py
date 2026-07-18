#!/usr/bin/env python3
# =============================================================================
# populate_S-ATLAS-055.py
# Q+ATLANTIDE / S-ATLAS / 050-059 / 055_Stabilizers
# Empennage structures as classes; trimmable-stabilizer and intake surrounds.
# Class-level subjects; declared boundaries; programme-agnostic. Idempotent;
# truthful --dry-run; --bootstrap for fresh trees; guarded --overwrite.
# =============================================================================
import argparse, sys
from pathlib import Path

CH = "055"; CH_TITLE = "Stabilizers"
RANGE_REL = ("01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
             "000-099_S-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces")

SCOPE = ("Empennage structures as programme-agnostic classes: horizontal "
         "stabilizer including trimmable-stabilizer structure, elevator "
         "structures, vertical stabilizer including dorsal fin, rudder "
         "structures, leading edges, tips and fairings, hinges, fittings "
         "and attachments, systems installation provisions, aeroelastic "
         "and balance characteristics, and advanced sustainable empennage "
         "architectures. Control-surface structure lives here; actuation, "
         "control laws and trim function are 027; the receiving fuselage "
         "structure is 053; instance geometry and tail arrangements are "
         "class and downstream matters.")

DIAGRAM = """```mermaid
flowchart LR
  subgraph EMP["Empennage structure"]
    H["055-100 Horizontal<br>Stabilizer"] --- E["055-200<br>Elevators"]
    V["055-300 Vertical<br>Stabilizer"] --- RU["055-400<br>Rudders"]
  end
  L["055-500 Leading Edges,<br>Tips and Fairings"] --- EMP
  F["055-600 Hinges, Fittings<br>and Attachments"] --- EMP
  P["055-700 Systems Installation<br>Provisions"] --- EMP
  A["055-800 Aeroelastic, Balance<br>and Dynamics"] --- EMP
  N["055-900 Advanced and Sustainable<br>Empennage Architectures"] -. "applies across" .-&gt; EMP
  F --&gt;|"attachment reactions<br>and load transfer"| R053["Receiving structure<br>053 (fittings 053-800;<br>tailcone zone 053-400)"]
  EMP -. "actuation, control and<br>trim function" .-&gt; X027["027"]
```"""

S = {
 "000": ("General", [
   "Chapter-level items across the empennage: surface protection, access, "
   "mass balance and zoning.",
   "Surface instances and tail arrangements (conventional, T-tail, "
   "V-tail) are class and downstream matters; the technology classes are "
   "owned here."],
  [("010","Surface-Protection-and-Films","Erosion and protection film systems of empennage surfaces (sibling of 057-010)."),
   ("020","Access-Provisions","Access panel doctrine per surface class."),
   ("030","Mass-Balance-and-Trim-Provisions","Balance-weight provisions of control surfaces (051-600 practice)."),
   ("040","Empennage-Zoning-and-Reference-Geometry","Station and zone references for empennage addressing.")]),
 "100": ("Horizontal-Stabilizer-Structure", [
   "Horizontal stabilizer box structure including the trimmable-"
   "stabilizer structural class: pivot structure, screwjack attach and "
   "the sliding-fairing kinematic interfaces.",
   "Trim actuation and control are 027; the pivot and attach structure "
   "and the moving-fairing structure are owned here."],
  [("110","Stabilizer-Skins-and-Stiffened-Panels","Upper and lower stiffened panels of the stabilizer box."),
   ("120","Stabilizer-Spars","Front and rear spars and their terminations."),
   ("130","Stabilizer-Ribs-and-Stringers","Rib and stringer systems of the box."),
   ("140","Center-Section-Pivot-and-Screwjack-Attach-Structure","Trimmable-stabilizer pivot fittings and actuator attach structure (function 027-400)."),
   ("150","Sliding-Fairings-and-Trim-Kinematic-Interfaces","Sliding fairing and plate structures accommodating stabilizer travel."),
   ("160","Integral-Volume-Provisions","Structural provisions of internal volumes where a trim-storage architecture is declared; the carrier system is 028 (057-250 sibling).")]),
 "200": ("Elevator-Structures", [
   "Elevator surface structural class: structure, fittings, interfaces "
   "to the stabilizer and fairings.",
   "Actuation and control: 027; hinge and actuator fittings interface "
   "them structurally here."],
  [("210","Elevator-Skin-and-Structure","Elevator skins, spars and ribs as a class."),
   ("220","Elevator-Hinge-and-Actuator-Fittings","Hinge-line and actuator load-introduction fittings (027 loads)."),
   ("230","Stabilizer-to-Elevator-Interfaces-and-Seals","Gap architecture, seals and interface structure between stabilizer and elevator."),
   ("240","Elevator-Fairings-and-Tips","Root and tip fairing structures of the elevator."),
   ("250","Elevator-Balance-Provisions","Surface balance provisions per 055-030 doctrine.")]),
 "300": ("Vertical-Stabilizer-Structure", [
   "Vertical stabilizer box, root attachment, dorsal fin and sealing "
   "structures.",
   "Root fittings transfer into 053-800; the tailcone and auxiliary-"
   "power zone boundary is 053-400."],
  [("310","Fin-Skins-and-Panels","Fin skin panels and stiffening."),
   ("320","Fin-Spars-Ribs-and-Stringers","Fin internal structure classes."),
   ("330","Fin-Root-Attachment-and-Fittings","Root attach fittings and their backup structure (053-800 receiving side)."),
   ("340","Dorsal-Fin-and-Fillet-Structures","Dorsal fin and fillet structural classes."),
   ("350","Root-and-Aerodynamic-Seals","Root seals and aerodynamic sealing of the fin junction.")]),
 "400": ("Rudder-Structures", [
   "Rudder surface structural class including multi-panel arrangements.",
   "Actuation and control: 027."],
  [("410","Rudder-Skin-and-Structure","Rudder skins, spars and ribs as a class."),
   ("420","Rudder-Hinge-and-Actuator-Fittings","Hinge-line and actuator fittings (027 loads)."),
   ("430","Multi-Panel-Rudder-Provisions","Structural provisions of segmented and multi-panel rudder classes."),
   ("440","Rudder-Fairings-and-Tips","Rudder fairing and tip structures."),
   ("450","Rudder-Balance-Provisions","Surface balance provisions per 055-030 doctrine.")]),
 "500": ("Leading-Edges-Tips-and-Fairings", [
   "Fixed leading edges of the empennage, intake provisions in fin "
   "leading edges, tip structures and fairing classes.",
   "Auxiliary-power intake function is 049-300; ice protection function "
   "is 030; the structural surrounds and provisions are owned here."],
  [("510","Fixed-Leading-Edge-Structures","Fixed LE structural classes of stabilizer and fin."),
   ("520","LE-Intake-and-Scoop-Structural-Surrounds","Structural surrounds of leading-edge intakes and scoops serving auxiliary power (049-300 function)."),
   ("530","Tip-Structures-and-Fairings","Tip fairing structures across empennage surfaces."),
   ("540","Ice-Protection-Integration-Provisions","Structural integration of empennage ice protection (030 owns the function).")]),
 "600": ("Hinges-Fittings-and-Attachments", [
   "The attachment architecture of the empennage: hinge lines, actuator "
   "reaction fittings, trimmable-stabilizer attach structure and the "
   "attachment to the receiving fuselage.",
   "Joint practices: 051-4xx/5xx."],
  [("610","Hinge-Line-Architectures","Hinge-line classes and failure ordering of surface suspensions."),
   ("620","Actuator-and-Reaction-Fittings","Actuator load-introduction and reaction fitting classes (027 interface)."),
   ("630","Trim-Pivot-and-Attach-Structure","Pivot and screwjack attach structure of trimmable stabilizers (055-140 detail class)."),
   ("640","Attachment-to-Receiving-Structure","Interface toward 053-800 fittings; opening and reinforcement stay with 053."),
   ("650","Joints-Splices-and-Fastening","Empennage joint architecture per 051-510 practices.")]),
 "700": ("Empennage-Systems-Installation-Provisions", [
   "Structure-side provisions for systems installed on the empennage.",
   "Split doctrine applies: systems own function and hardware; this "
   "section owns the structural provision."],
  [("710","Harness-Routing-and-Bonding-Provisions","Routing and bonding provisions (024, 051-800)."),
   ("720","Static-Discharger-Provisions","Discharger mounting provisions (023-600 owns the system)."),
   ("730","Lights-and-Antenna-Provisions","Provisions for lights (033) and antennas (023, 034) on the empennage."),
   ("740","Sensor-Installation-Provisions","Provisions for sensors installed on empennage surfaces.")]),
 "800": ("Aeroelastic-Balance-and-Dynamic-Characteristics", [
   "Aeroelastic and dynamic structural characteristics of the empennage "
   "as declared properties: flutter doctrine, balance doctrine, buffet "
   "and dynamic environment.",
   "Control-law interactions are 027; class-level configuration effects "
   "are 09x."],
  [("810","Flutter-and-Aeroelastic-Doctrine","Declared aeroelastic characteristics and their evidence basis."),
   ("820","Surface-Balance-Doctrine","Balance philosophy per surface class (051-600 execution)."),
   ("830","Dynamic-Environment-and-Buffet","Buffet and dynamic-load structural doctrine.")]),
 "900": ("Advanced-and-Sustainable-Empennage-Architectures", [
   "Green-native empennage block: all-movable and reduced-tail "
   "structures, adaptive surfaces, welded thermoplastic boxes, "
   "aft-propulsion interaction provisions, load-alleviation provisions "
   "and circularity.",
   "Type classes constrain arrangements (09x); functions stay with 027; "
   "the door-side rule generalizes: this chapter owns the empennage-side "
   "implementation, never the generic technology."],
  [("910","All-Movable-and-Reduced-Tail-Structures","Structural classes of all-movable surfaces and reduced-tail architectures; stability function is 027, class constraints 09x."),
   ("920","Morphing-and-Adaptive-Empennage-Structures","Shape-adaptive empennage structural concepts; actuation remains 027."),
   ("930","Thermoplastic-and-Welded-Empennage-Structures","Welded thermoplastic torsion-box application (051-230, 051-320)."),
   ("940","Aft-Propulsion-Interaction-Provisions","Empennage-side provisions where aft or dorsal propulsion interacts; integration structure is 054-300."),
   ("950","Load-Alleviation-Structural-Provisions","Structural provisions of active load alleviation; function is 027."),
   ("960","Empennage-Circularity-and-Disassembly","Design-for-disassembly and material identification (051-340).")]),
}

BOUNDARIES = (
 "Control surfaces: structure here; actuation, control laws and trim "
 "function 027 (trimmable-stabilizer drive 027-400; pivot and attach "
 "structure 055-140/630). Receiving structure: 053 owns the fuselage "
 "opening, reinforcement and fittings (053-800); the tailcone and "
 "auxiliary-power zone boundary is 053-400. Auxiliary-power intake: "
 "function 049-300, leading-edge structural surrounds 055-520. Ice "
 "protection: function 030, provisions 055-540. Static dischargers: "
 "system 023-600, provisions 055-720. Lights 033 and antennas 023/034: "
 "provisions 055-730. Aft and dorsal propulsion: integration structure "
 "054-300, empennage-side provisions 055-940. Trim-volume storage: "
 "provisions 055-160, carrier system 028. Structural practices: 051. "
 "Type classes 090-099 constrain tail arrangements and geometry and "
 "shall not duplicate this chapter.")

def sec_readme(code, title, bullets, subjects):
    L=[];A=L.append
    A(f"# {CH}-{code} — {title.replace('-',' ')}");A("")
    A(f"**Chapter:** {CH}_{CH_TITLE} · **Section:** {code}");A("")
    for b in bullets: A(f"- {b}")
    A("");A("## Subjects");A("")
    A("| Subject | Title |");A("|---|---|")
    for sc,st,_ in subjects:
        A(f"| {CH}-{sc} | <a>{st.replace('-',' ')}</a> |")
    A("")
    return "\n".join(L)+"\n"

def subj_readme(sec, sc, st, line):
    return (f"# {CH}-{sc} — {st.replace('-',' ')}\n\n"
            f"**Section:** {CH}-{sec} · **Subject:** {sc}\n\n- {line}\n")

def ch_readme():
    L=[];A=L.append
    A(f"# {CH}_{CH_TITLE}");A("")
    A(f"**Range:** 050-059_Primary-Structures-and-Programme-Interfaces · **Chapter:** {CH}");A("")
    A("## Scope");A("");A(SCOPE);A("")
    A("## Integration chain");A("");A(DIAGRAM);A("")
    A("## Section register");A("")
    A("| Section | Title | Subjects |");A("|---|---|---|")
    for code,(t,_,subs) in S.items():
        A(f"| {CH}-{code} | <a>{t.replace('-',' ')}</a> | {len(subs)} |")
    A("");A("## Boundary summary");A("");A(BOUNDARIES);A("")
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
    for code,(t,bl,subs) in S.items():
        sdir=cdir/f"{CH}-{code}_{t}"
        plan.append((sdir/"README.md",sec_readme(code,t,bl,subs),True))
        for sc,st,line in subs:
            plan.append((sdir/f"{CH}-{sc}_{st}"/"README.md",subj_readme(code,sc,st,line),False))
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
