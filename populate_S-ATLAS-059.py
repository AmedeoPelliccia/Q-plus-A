#!/usr/bin/env python3
"""Populate S-ATLAS 059, the programme-structural interfaces chapter."""

import argparse
import sys
from pathlib import Path

CH = "059"
CH_TITLE = "Programme-Structural-Interfaces"
RANGE_REL = (
    "01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/"
    "000-099_S-ATLAS/050-059_Primary-Structures-and-Programme-Interfaces"
)

SCOPE = (
    "The interface doctrine of the structures range toward downstream mapping "
    "layers: the layer model, applicability and effectivity grammar, interface-"
    "definition schema classes, assembly and station convention classes, "
    "crosswalk doctrine, the structural evidence interface, change propagation, "
    "interface governance and machine-readable automation. Rule of the chapter: "
    "schemas and doctrine live here; instances live downstream. This chapter "
    "declares no applicability and names no programme — it defines how "
    "programmes declare applicability onto chapters 050-058, in their impact "
    "studies, product breakdown structures and data-module mappings."
)

DIAGRAM = """```mermaid
flowchart LR
  T["Taxonomy layer<br>050-058 chapters<br>(technology, agnostic)"]
  C["Type-class layer<br>090-099<br>(configuration constraints)"]
  D["Downstream layer<br>impact studies · PBS · DMC<br>(instances, effectivity)"]
  S["059<br>Interface doctrine<br>and schema classes"]
  T --&gt; D
  C -. "constrains" .-&gt; D
  S -. "defines how the mapping<br>is declared" .-&gt; D
  S -. "governs crosswalks<br>and change propagation" .-&gt; T
```"""

S = {
    "000": (
        "General-and-Layer-Doctrine",
        [
            "The layer model of the architecture: taxonomy documents technology; "
            "type classes constrain configurations; downstream layers declare "
            "instances, applicability and effectivity.",
            "The canonical rule this chapter exists to teach: programme "
            "applicability, effectivity and instance sizing are out of scope for "
            "the taxonomy — they are declared in the impact studies and PBS "
            "layers that map onto it.",
        ],
        [
            ("010", "Layer-Model-and-Ownership", "The three layers, their owners and their artifacts."),
            ("020", "What-May-and-May-Not-Live-in-the-Taxonomy", "The agnosticism rule operationalized: allowed doctrine sentences, forbidden instance content."),
            ("030", "Terminology-of-Interfaces-and-Mapping", "Controlled vocabulary: mapping, applicability, effectivity, instance, delta."),
        ],
    ),
    "100": (
        "Downstream-Mapping-Model",
        [
            "The mapping chain from taxonomy to delivered documentation: impact "
            "study selects, product breakdown structures instantiate, data-module "
            "codes deliver.",
            "Pointer level only: the chain's artifacts are downstream deliverables.",
        ],
        [
            ("110", "Impact-Study-Interface", "What an impact study consumes from the taxonomy and what it declares."),
            ("120", "Product-Breakdown-Interface", "How breakdown structures reference taxonomy addresses without duplicating them."),
            ("130", "Data-Module-Mapping-Interface", "How taxonomy subjects map to data-module requirements downstream (typical information sets as inputs)."),
            ("140", "Thread-Index-Consumption", "How cross-cutting thread indexes serve as downstream starting checklists."),
        ],
    ),
    "200": (
        "Effectivity-and-Declaration-Grammar",
        [
            "The grammar by which downstream layers declare applicability and "
            "effectivity onto structural chapters, referencing the technical-"
            "publication standard's applicability model.",
            "The standard's constructs are referenced, never re-specified.",
        ],
        [
            ("210", "Declaration-Points-and-Granularity", "At which taxonomy levels downstream declarations may attach."),
            ("220", "Effectivity-Model-References", "References to the publication standard's applicability constructs (standards references, not duplication)."),
            ("230", "Instance-Sizing-and-Delta-Declarations", "How instance counts and deltas are declared downstream — never upstream."),
            ("240", "Validation-Rules-for-Declarations", "Consistency rules a downstream declaration must satisfy against the taxonomy."),
        ],
    ),
    "300": (
        "Downstream-Interface-Definition-Schemas",
        [
            "The schema classes by which downstream layers define structural "
            "interface items against taxonomy addresses: record structure, "
            "required fields, address references and evidence hooks.",
            "Schemas are taxonomy artifacts; populated instances are downstream "
            "artifacts — misplaced instance files relocate to their layer.",
        ],
        [
            ("310", "Interface-Record-Schema-Class", "The controlled record structure of a downstream structural interface definition."),
            ("320", "Address-Reference-Rules", "How records reference taxonomy addresses: exact codes, no duplication of content."),
            ("330", "Evidence-and-Traceability-Fields", "Required traceability and evidence-hook fields of interface records."),
            ("340", "Schema-Versioning-and-Compatibility", "Versioning doctrine of schema classes and downstream compatibility."),
        ],
    ),
    "400": (
        "Assembly-and-Station-Convention-Classes",
        [
            "Convention classes for assembly stations, position identification "
            "and part-number mapping structure — the class level of conventions "
            "whose instances are downstream.",
            "Instance conventions and their registers are downstream artifacts.",
        ],
        [
            ("410", "Station-and-Position-Convention-Classes", "Controlled classes of station and position identification schemes."),
            ("420", "Part-Number-Mapping-Structure-Classes", "Structure classes for mapping breakdown items to taxonomy addresses."),
            ("430", "Assembly-Interface-Declaration-Classes", "Classes for declaring assembly-level structural interfaces downstream."),
        ],
    ),
    "500": (
        "Crosswalks-and-Legacy-Mapping-Doctrine",
        [
            "Doctrine of crosswalk artifacts mapping taxonomy chapters to "
            "external standards and legacy documentation structures.",
            "Crosswalks are derived, traceable artifacts: they map, they never "
            "govern; external structures are referenced for traceability, never "
            "imported as authority.",
        ],
        [
            ("510", "Crosswalk-Artifact-Classes", "Controlled classes of crosswalk artifacts and their required metadata."),
            ("520", "Legacy-Chapter-Mapping-Rules", "Rules for mapping to legacy chapter systems while preserving taxonomy authority."),
            ("530", "Crosswalk-Maintenance-and-Supersession", "How crosswalks track taxonomy and external evolution."),
        ],
    ),
    "600": (
        "Structural-Evidence-Interface",
        [
            "How taxonomy-level evidence subjects connect to downstream "
            "certification data sets and the product passport channel.",
            "Evidence content lives with its chapters; the interface doctrine "
            "lives here; the passport channel is the onboard-maintenance data path.",
        ],
        [
            ("610", "Evidence-Subject-Interface-Doctrine", "How chapter evidence subjects are consumed by downstream certification sets."),
            ("620", "Passport-Channel-Interface", "The structural content path toward digital product passports (045 channel)."),
            ("630", "Evidence-Traceability-Rules", "Traceability rules linking downstream evidence items to taxonomy addresses."),
        ],
    ),
    "700": (
        "Change-Propagation-and-Impact-Doctrine",
        [
            "How taxonomy changes propagate downstream: notification, impact "
            "assessment and re-declaration duties.",
            "Supersession is recorded, never silent; downstream layers own their "
            "re-validation.",
        ],
        [
            ("710", "Change-Classes-and-Notification", "Classes of taxonomy change and their downstream notification duties."),
            ("720", "Downstream-Impact-Assessment-Doctrine", "How downstream layers assess and record impact of taxonomy changes."),
            ("730", "Supersession-and-Re-Declaration-Rules", "Rules for superseding mappings and re-declaring against new addresses."),
        ],
    ),
    "800": (
        "Interface-Governance-and-Ratification",
        [
            "Governance of the interface: who ratifies schemas, crosswalks and "
            "mapping rules, and how ratification is recorded.",
            "Merge is ratification; authority layers are declared, not implied.",
        ],
        [
            ("810", "Authority-Layers-and-Roles", "Which authority ratifies which interface artifact class."),
            ("820", "Ratification-Recording", "How interface ratifications are recorded and referenced."),
            ("830", "Dispute-and-Boundary-Resolution-Process", "How mapping disputes between layers are resolved and recorded."),
        ],
    ),
    "900": (
        "Machine-Readable-Interfaces-and-Automation",
        [
            "The automation block: machine-readable interface artifacts, "
            "generated draft requirements from typical information sets, and "
            "validation tooling classes.",
            "Generators derive, never author; derived artifacts declare their "
            "sources; a generator that fails loudly beats one that infers.",
        ],
        [
            ("910", "Machine-Readable-Artifact-Classes", "Schema-conformant, parseable interface artifact classes."),
            ("920", "Draft-Requirements-Generation", "Generation of draft documentation requirements from typical-information-set tables (pointer to the authoring convention)."),
            ("930", "Validation-Tooling-Classes", "Tooling classes validating downstream declarations against the taxonomy."),
            ("940", "Automation-Evidence-and-Determinism", "Determinism and evidence doctrine of interface automation."),
        ],
    ),
}

BOUNDARIES = (
    "Rule of the chapter: schemas and doctrine here; instances downstream. "
    "This chapter names no programme and declares no applicability — it defines "
    "how downstream layers declare theirs. Taxonomy content: chapters 050-058 "
    "own their technology and evidence subjects. Type classes: 090-099 constrain "
    "configurations; their relationship to downstream layers is 090-500. "
    "Publication-standard applicability constructs: referenced as standards, "
    "never re-specified. Passport channel: 045. Practices: 051. Misplaced "
    "downstream instance files relocate to their layer — the taxonomy hosts "
    "their schema classes only (059-300)."
)


def sec_readme(code, title, bullets, subjects):
    lines = [f"# {CH}-{code} — {title.replace('-', ' ')}", ""]
    lines += [f"**Chapter:** {CH}_{CH_TITLE} · **Section:** {code}", ""]
    lines += [f"- {bullet}" for bullet in bullets]
    lines += ["", "## Subjects", "", "| Subject | Title |", "|---|---|"]
    lines += [
        f"| {CH}-{subject_code} | [{subject_title.replace('-', ' ')}]({CH}-{subject_code}_{subject_title}/) |"
        for subject_code, subject_title, _ in subjects
    ]
    return "\n".join(lines) + "\n"


def subj_readme(sec, subject_code, subject_title, summary):
    return (
        f"# {CH}-{subject_code} — {subject_title.replace('-', ' ')}\n\n"
        f"**Section:** {CH}-{sec} · **Subject:** {subject_code}\n\n"
        f"- {summary}\n"
    )


def ch_readme():
    lines = [
        f"# {CH}_{CH_TITLE}",
        "",
        f"**Range:** 050-059_Primary-Structures-and-Programme-Interfaces · **Chapter:** {CH}",
        "",
        "## Scope",
        "",
        SCOPE,
        "",
        "## Integration chain",
        "",
        DIAGRAM,
        "",
        "## Section register",
        "",
        "| Section | Title | Subjects |",
        "|---|---|---|",
    ]
    lines += [
        f"| {CH}-{code} | [{title.replace('-', ' ')}]({CH}-{code}_{title}/) | {len(subjects)} |"
        for code, (title, _, subjects) in S.items()
    ]
    lines += ["", "## Boundary summary", "", BOUNDARIES, ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--bootstrap", action="store_true")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    anchor = root / "01_OPTIONS_ARCHITECTURE" / "01-03_TECHNOLOGIES" / "01-03-01_Q+ATLANTIDE"
    if not anchor.is_dir() and not args.bootstrap:
        parser.error(
            f"Q+ATLANTIDE root not found under {root}; run from repo root, "
            "use --root, or pass --bootstrap."
        )

    chapter_dir = root / RANGE_REL / f"{CH}_{CH_TITLE}"
    plan = [(chapter_dir / "README.md", ch_readme(), True)]
    for code, (title, bullets, subjects) in S.items():
        section_dir = chapter_dir / f"{CH}-{code}_{title}"
        plan.append((section_dir / "README.md", sec_readme(code, title, bullets, subjects), True))
        for subject_code, subject_title, summary in subjects:
            plan.append(
                (
                    section_dir / f"{CH}-{subject_code}_{subject_title}" / "README.md",
                    subj_readme(code, subject_code, subject_title, summary),
                    False,
                )
            )

    written = skipped = 0
    for filepath, content, always in plan:
        exists = filepath.exists()
        should_write = not exists or always or args.overwrite
        if args.dry_run:
            written += should_write
            skipped += not should_write
        elif should_write:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.write_text(content, encoding="utf-8")
            written += 1
        else:
            skipped += 1

    mode = "dry-run" if args.dry_run else CH
    print(f"[{mode}] written={written} skipped={skipped} planned={len(plan)} at {chapter_dir}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        sys.exit(0)
