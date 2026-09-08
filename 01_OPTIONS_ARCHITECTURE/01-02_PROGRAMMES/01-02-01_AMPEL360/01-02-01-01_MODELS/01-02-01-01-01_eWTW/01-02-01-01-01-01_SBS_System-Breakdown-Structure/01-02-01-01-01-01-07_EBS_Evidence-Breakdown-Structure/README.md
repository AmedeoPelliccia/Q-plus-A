---
status: draft
standard_scope: governance
---

# eWTW — Evidence Breakdown Structure (EBS)

<!-- Generated 2026-09-06 - GitHub Copilot - SBS rework under CM-002 -->

## Charter

The EBS is a **derived index over `**/evidence/`**. Evidence lives with the node that produced it (CM-001 C1.5) and the EBS references it — it never relocates it. A verification report belongs to the part it verifies; a run-record belongs to the station whose work it records; a ratified act belongs to the structure it governs. The EBS adds no second home for any of these: it is the one place where all of them can be *found*, not where any of them *live*.

Per **`AMPEL360-SBS-ID-CM-002` §3 the EBS has no id space of its own** — its rows are path-addressed and carry a `subject:` field (a part number or an act id). There is nothing to number: an evidence row is fully identified by the path of the artefact it points at, and the subject binds it to the identity systems of the PBS (part numbers) or of the governance record (act ids). Derived means regenerated: the index is rebuilt from what is on disk, and a row with no artefact behind it is a defect of the index, not a record of intent.

**Evidence classes:** ratified acts and conventions · migration and completion records · verification reports · analysis and test records (future) · principal-structural-element register (future).

## Index

- [`EVIDENCE-INDEX.yaml`](EVIDENCE-INDEX.yaml) — the row schema and every evidence row discoverable today.
