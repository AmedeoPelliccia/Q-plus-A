# AMPEL360-KNOT-CM-004 — Knowledge Nodes and Knowledge Units

**Issue 1** · Owner: `STK_CM` (proposed) · Authority: AM.PEL · Status: **PROPOSED**
**Approval act:** not yet recorded. On approval, this line names the act: commit or merge, date, authority.

---

## 1. Purpose and scope

This convention governs how the eWTW model records what it must decide or satisfy, and the work that produces the knowledge to do it. It applies to the eWTW [KNOT register](README.md) and, by adoption, to sibling models: the MRTT-Q300 manages its uncertainty with the same method.

## 2. Definitions

**KNOT** — a governing traceability node representing an obligation, a control intent, a decision anchor or an authoritative lifecycle constraint. A KNOT states the problem; it does not solve it. The expansion of the acronym is not fixed; *Knowledge Node Ontological Trace* (or *Track*) is under consideration.

**KNU** — Knowledge Unit: a traceable implementation unit linked to a KNOT. It is the action that produces knowledge toward the KNOT's resolution — research, analysis, test or any other activity — together with what that action delivers. Its class names the delivery: a work item, a controlled artefact, a requirement set, an analysis package, a verification object, an evidence record, or another executable lifecycle unit.

Both definitions come from [AEROSPACEMODEL] (`00_META/glossary/terms.md`, `00_META/schemas/`), restated by the authority on 2026-11-08.

## 3. Kinds of KNOT

| Kind | Meaning |
|---|---|
| `decision-anchor` | A choice the model must make: a configuration decision, or an ownership or taxonomy ruling |
| `obligation` | Something the model must satisfy, from a regulation, a requirement or a governance rule |
| `control-intent` | A constraint the authority imposes on design or process |
| `lifecycle-constraint` | An authoritative constraint from the lifecycle registry |

## 4. Identifiers

```text
KNOT-<MIC>-<TOPIC>-<NNN>           KNOT-EWTW-NRG-001
KNU-<MIC>-<TOPIC>-<NNN>-<NN>       KNU-EWTW-NRG-001-03
```

A KNU identifier is the identifier of its parent KNOT, prefixed `KNU`, with a two-digit sequence. A KNU has one parent and may serve other KNOTs (`serves`). Identifiers are never reused; a cancelled KNU keeps its number.

Identifiers carry no classification. The S-ATLAS addresses a KNOT applies to are in its `taxonomy` field: the identity stays sovereign and the classification is a reference, as for PBS codes ([`AMPEL360-PBS-PN-CM-001`][CM-001] §3.1, [`AMPEL360-SBS-ID-CM-002`][CM-002]). Classifications change; identifiers do not. A KNOT whose purpose is to decide where a scope lives leaves the field empty until it is ruled.

In AEROSPACEMODEL both identifiers carry an `LC01`–`LC14` code. The Q+ATLANTIDE lifecycle registry excludes that axis, so here the phase is a field (`lifecycle_phase`, LC letters) and not part of the identifier.

## 5. Records

One YAML file per KNOT, named by its identifier, holds the KNOT and its KNUs. Records are filed in folders by scope (rule 11). Field names follow the AEROSPACEMODEL schemas where they apply.

| Record | Fields |
|---|---|
| KNOT | `knot_id`, `title`, `kind`, `taxonomy`, `raised_at`, `question`, `context`, `obligation_source`, `lifecycle_phase`, `due`, `owner`, `status`, `resolution`, `created_date`, `depends_on`, `closed_with`, `unblocks`, `affects`, `options`, `criteria`, `maturity_required` (every decision anchor), `assumptions`, `couplings`, `rulings`, `reopen_if`, `knus` |
| KNU | `knu_id`, `title`, `knu_class`, `description`, `research_brief`, `serves`, `outputs`, `exit`, `owner`, `lifecycle_phase`, `progress`, `created_date`, `start_date`, `end_date`, `evidence_refs`, `condition` (optional) |
| Ruling | `id`, `date`, `authority`, `statement`, `effect`, `rationale`, `rationale_recorded`, `evidence`, `waiver`, `state`, `record` |

**Vocabularies**

| Field | Values |
|---|---|
| `status` (the record) | `DRAFT` · `REVIEW` · `APPROVED` · `SUPERSEDED` · `OBSOLETE` |
| `resolution` (KNOT) | `OPEN` · `RULED` · `DEFERRED` |
| `progress` (KNU) | `NOT_STARTED` · `IN_PROGRESS` · `PENDING_REVIEW` · `DONE` · `CANCELLED` |
| `knu_class` | `WORK_ITEM` · `CONTROLLED_ARTEFACT` · `REQUIREMENT_SET` · `ANALYSIS_PACKAGE` · `VERIFICATION_OBJECT` · `EVIDENCE_RECORD` · `OTHER` |
| option `state` | `open` · `retained` · `rejected` · `excluded` |
| ruling `state` | `PROVISIONAL` · `COMPLETE` |

An option is `retained` or `rejected` by scoring it against the declared criteria; it is `excluded` when a ruling removes it from the scope without scoring. `raised_at` is the S-ATLAS chapter of the node that recorded the KNOT, or null.

`progress` takes the place of the AEROSPACEMODEL `compliance_status`: Q+ATLANTIDE records carry no conformity claims. The AEROSPACEMODEL classes map as follows: `ARTEFACT` and `PROCEDURE` → `CONTROLLED_ARTEFACT`; `RECORD` and `REPORT` → `EVIDENCE_RECORD`; `VALIDATION_OBJECT` → `VERIFICATION_OBJECT`.

**References** are typed, as in [`AMPEL360-SBS-ID-CM-002`][CM-002]: `{view, ref}`, where `view` is an SBS view (`PBS`, `FBS`, `WBS`, `CBS`, `RBS`, `LBS`, `EBS`, `IBS`, `ReqBS`, `TPMS`, `TPuBS`) or `model`, `baseline`, `finding`, `registry`, `taxonomy`. A null `ref` marks an output still to be created: no identifier is invented ahead of its view. `taxonomy` holds S-ATLAS addresses, quoted — chapters such as `'024'` or finer nodes such as `'021-510'`. S-ATLAS is the reference taxonomy, not ATA chapter numbers.

## 6. Rules

1. Every KNOT names at least one obligation source.
2. Every KNU belongs to one parent KNOT through its identifier, and names at least one output and an exit criterion.
3. A KNU in progress carries an evidence reference or a target end date.
4. A KNOT is ruled by its authority on the evidence of its KNUs. A ruling states date, authority, statement, effect, rationale and evidence. A ruling that lacks rationale or evidence is `PROVISIONAL`: it directs the work, but it is not an auditable basis, and no KNOT is `RULED` and no option scored while one of its rulings is provisional. Options not retained stay in the record, with the reason (`QPLUS-LC-MEMORY-001`).
5. A decision anchor declares its criteria and the maturity it requires before any option is scored (`QPLUS-LC-DECISION-MATURITY-001`): while `criteria` or `maturity_required` is empty, no option becomes `retained` or `rejected` and the KNOT is not `RULED`. An exclusion from scope is not a scoring, but its ruling still owes rationale and evidence (rule 4). A ruling below that maturity carries the waiver of the accountable decision authority — deficit, rationale, invalidating condition, risk record, effectivity and duration. An assumption documents a deficit; it never waives one. A threshold that implements a regulatory requirement is never waived.
6. A ruling may narrow the option set without closing the KNOT; the KNOT stays `OPEN`.
7. A recorded ruling is never rewritten. Missing rationale and evidence may be completed once, by the authority, with the date in `rationale_recorded`; the ruling then becomes `COMPLETE`. Reopen conditions are not ruling fields: they are recorded in the KNOT's `reopen_if`. A later ruling supersedes an earlier one; both stay in the record.
8. A ruled KNOT reopens when one of its `reopen_if` conditions is met.
9. The research agenda is a view — the KNUs neither `DONE` nor `CANCELLED`, across all records. It is generated from the records, not kept by hand.
10. No record carries a conformity claim.
11. Records are filed by scope. A KNOT whose `taxonomy` names one S-ATLAS chapter is filed in that chapter's folder, `<CCC>_<Title>/`. A KNOT with an empty `taxonomy` and a `raised_at` chapter is filed under that chapter until it is ruled. Every other KNOT — one that spans several chapters, or belongs to none — is filed in `000_General/`, the folder of S-ATLAS chapter `000` *General*. The folder is a filing place, not identity: a record moves when its scope changes, and its identifier stays.
12. The verification script of the register enforces rules 1–5, 10 and 11 and the required fields; a record that fails it is not merged.
13. A KNOT states its `context` in plain words, and a KNU that needs outside research states its questions in `research_brief`. With the model context of the register, written once, they form a self-contained research prompt. They state only what the model has declared and name no option as preferred.

## 7. Lifecycle and memory

Configuration decisions are `LC-B` deliverables (registry §3): a KNOT is worked during `LC-A`, under recorded assumptions. KNUs that develop articles run as scoped maturation cycles (`QPLUS-LC-MATCYCLE-001`), and their exit decisions are recorded in the KNU. Ratified baselines say what the aircraft is in each age (`QPLUS-LC-AGE-001`); the KNOT records say why, and the options not retained keep the memory of what it did not become.

## Change record

| Issue | Content |
|---|---|
| 1 | Definitions from AEROSPACEMODEL as restated on 2026-11-08; kinds; identifier grammar without `LC01`–`LC14` and without classification, S-ATLAS addresses in the `taxonomy` field; record fields and vocabularies; provisional rulings; scoring gate; filing by scope; research briefs; rules 1–13 |

[AEROSPACEMODEL]: https://github.com/AmedeoPelliccia/AEROSPACEMODEL
[CM-001]: ../01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/AMPEL360-PBS-PN-CM-001_Assembly-Station-and-Part-Number-Breakdown.md
[CM-002]: ../01-02-01-01-01-01_SBS_System-Breakdown-Structure/AMPEL360-SBS-ID-CM-002_Cross-Structure-Identification.md
