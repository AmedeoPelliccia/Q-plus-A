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
| KNOT | `knot_id`, `title`, `kind`, `taxonomy`, `raised_at`, `question`, `context`, `effectivity`, `obligation_source`, `lifecycle_phase`, `due`, `owner`, `status`, `resolution`, `created_date`, `depends_on`, `closed_with`, `unblocks`, `affects`, `options`, `criteria`, `maturity_required` (every decision anchor), `assumptions`, `couplings`, `rulings`, `reopen_if`, `knus` |
| KNU | `knu_id`, `title`, `knu_class`, `description`, `research_brief`, `serves`, `outputs`, `exit`, `owner`, `lifecycle_phase`, `progress`, `created_date`, `start_date`, `end_date`, `evidence_refs`, `condition` (optional) |
| Option | `id`, `text`, `state`, `pbs_footprint` and `by` where applicable |
| Criterion | `id`, `text`, `class`, `source`, `weight`, `threshold`, `state` |
| Ruling | `id`, `date`, `authority`, `statement`, `effect`, `rationale`, `rationale_recorded`, `evidence`, `waiver`, `state`, `record`, `effectivity`, `effects`, `embodied_in` |

**Vocabularies**

| Field | Values |
|---|---|
| `status` (the record) | `DRAFT` · `REVIEW` · `APPROVED` · `SUPERSEDED` · `OBSOLETE` |
| `resolution` (KNOT) | `OPEN` · `RULED` · `DEFERRED` |
| `progress` (KNU) | `NOT_STARTED` · `IN_PROGRESS` · `PENDING_REVIEW` · `DONE` · `CANCELLED` |
| `knu_class` | `WORK_ITEM` · `CONTROLLED_ARTEFACT` · `REQUIREMENT_SET` · `ANALYSIS_PACKAGE` · `VERIFICATION_OBJECT` · `EVIDENCE_RECORD` · `OTHER` |
| option `state` | `open` · `retained` · `rejected` · `excluded` |
| ruling `state` | `PROVISIONAL` · `COMPLETE` |
| criterion `class` | `mandatory` · `tradable` |
| criterion `state` | `PROPOSED` · `APPROVED` |

An option is `retained` or `rejected` by scoring it against the declared criteria; it is `excluded` when a ruling removes it from the scope without scoring. A `mandatory` criterion is not traded: an option that fails it is rejected. A `tradable` criterion carries the `weight` and the `threshold` that the authority sets. A criterion is declared when the authority has made it `APPROVED`. While any criterion of a decision anchor is `PROPOSED`, rule 5 applies as if none were declared. `raised_at` is the S-ATLAS chapter of the node that recorded the KNOT, or null.

`progress` takes the place of the AEROSPACEMODEL `compliance_status`: Q+ATLANTIDE records carry no conformity claims. The AEROSPACEMODEL classes map as follows: `ARTEFACT` and `PROCEDURE` → `CONTROLLED_ARTEFACT`; `RECORD` and `REPORT` → `EVIDENCE_RECORD`; `VALIDATION_OBJECT` → `VERIFICATION_OBJECT`.

**References** are typed, as in [`AMPEL360-SBS-ID-CM-002`][CM-002]: `{view, ref}`, where `view` is an SBS view (`PBS`, `FBS`, `WBS`, `CBS`, `RBS`, `LBS`, `EBS`, `IBS`, `ReqBS`, `TPMS`, `TPuBS`) or `model`, `baseline`, `finding`, `registry`, `taxonomy`. A null `ref` marks an output still to be created: no identifier is invented ahead of its view. `taxonomy` holds S-ATLAS addresses, quoted — chapters such as `'024'` or finer nodes such as `'021-510'`. S-ATLAS is the reference taxonomy, not ATA chapter numbers.

## 6. Rules

1. Every KNOT names at least one obligation source.
2. Every KNU belongs to one parent KNOT through its identifier, and names at least one output and an exit criterion.
3. A KNU in progress carries an evidence reference or a target end date.
4. A KNOT is ruled by its authority on the evidence of its KNUs. A ruling states date, authority, statement, effect, rationale and evidence. A ruling that lacks rationale or evidence is `PROVISIONAL`: it directs the work, but it is not an auditable basis, and no KNOT is `RULED` and no option scored while one of its rulings is provisional. Options not retained stay in the record, with the reason (`QPLUS-LC-MEMORY-001`).
5. A decision anchor declares its criteria and the maturity it requires before any option is scored (`QPLUS-LC-DECISION-MATURITY-001`): while `criteria` or `maturity_required` is empty, no option becomes `retained` or `rejected` and the KNOT is not `RULED`. An exclusion from scope is not a scoring, but its ruling still owes rationale and evidence (rule 4). A ruling below that maturity carries the waiver of the accountable decision authority — deficit, rationale, invalidating condition, risk record, effectivity and duration. An assumption documents a deficit; it never waives one. A threshold that implements a regulatory requirement is never waived.
6. A ruling may narrow the option set without closing the KNOT; the KNOT stays `OPEN`.
7. A recorded ruling is never rewritten. Missing rationale and evidence may be completed once, by the authority, with the date in `rationale_recorded`; the ruling then becomes `COMPLETE`. Reopen conditions are not ruling fields: they are recorded in the KNOT's `reopen_if`. Append embodiment references under rule 16 when the baseline is ratified. A later ruling supersedes an earlier one and both stay in the record.
8. A ruled KNOT reopens when one of its `reopen_if` conditions is met.
9. The research agenda is a view — the KNUs neither `DONE` nor `CANCELLED`, across all records. It is generated from the records, not kept by hand.
10. No record carries a conformity claim.
11. Records are filed by scope. A KNOT whose `taxonomy` names one S-ATLAS chapter is filed in that chapter's folder, `<CCC>_<Title>/`. A KNOT with an empty `taxonomy` and a `raised_at` chapter is filed under that chapter until it is ruled. Every other KNOT — one that spans several chapters, or belongs to none — is filed in `000_General/`, the folder of S-ATLAS chapter `000` *General*. The folder is a filing place, not identity: a record moves when its scope changes, and its identifier stays.
12. The register verification script, `tools/knot_check.py`, checks rules 1–5, 10, 11 and 18 and the required field shapes and references for rules 14–17; `tools/knot_check_test.py` tests it. A passing check is required for merging a record.
13. A KNOT states its `context` in plain words, and a KNU that needs outside research states its questions in `research_brief`. With the model context of the register, written once, they form a self-contained research prompt. They state only what the model has declared and name no option as preferred.

14. The KNOT declares its effectivity. Each ruling records the effectivity of its own act, including the input baseline where one exists.
15. Each option records the product elements it would affect and their S-ATLAS addresses where known. Its trade study uses consistent part, interface, modularity, maintenance and applicable commonality criteria.
16. A complete ruling records its authorised effects by SBS view. The first ratified baseline that incorporates the effects in each applicable scope is recorded in `embodied_in` when the release act is available.
17. An `affects` reference with `relation: gates` identifies an existing PBS node and the allocation awaiting the decision. The register generates the view of these allocations from active, unresolved records.
18. Each product element in the footprints has a `key`, and one owning KNOT: the only KNOT whose options `create` it. Another KNOT that acts on the same element uses `update`, `populate`, `retire` or `remap`, names the owner in `owner`, and files the element under the owner's S-ATLAS address. Alternative options of one KNOT may create the same element. A turbogenerator in the propulsion or main generation chain is filed under S-ATLAS `068`; `049` applies only to an auxiliary unit detached from the propulsion architecture (architecture authority, 2026-11-12).

## 7. Lifecycle and memory

Configuration decisions are `LC-B` deliverables (registry §3): a KNOT is worked during `LC-A`, under recorded assumptions. KNUs that develop articles run as scoped maturation cycles (`QPLUS-LC-MATCYCLE-001`), and their exit decisions are recorded in the KNU. Ratified baselines say what the aircraft is in each age (`QPLUS-LC-AGE-001`); the KNOT records say why, and the options not retained keep the memory of what it did not become.

## 8. Effectivity and product definition

**Effectivity.** Each entry is `{model, variants, from_baseline}`. Use the controlled model identifier and the applicable variant IDs. An empty variant list denotes the named model scope covered by the record. Use `from_baseline: null` for a scope in initial definition. When the decision acts on a released configuration, pin the applicable input baseline. A ruling's effectivity is the scope of that act at the time of the decision. Cross-model dependencies remain in `couplings` until the applicable authority determines scope for each model.

**Candidate product structure.** In `pbs_footprint`, record `{action, taxonomy, element, key}` for each identified physical change, with `owner` and `note` where they apply. `taxonomy` is a quoted S-ATLAS address and `element` describes the candidate part or installation. Use `[]` while the footprint is still to be determined. The trade can use common product elements and neutral provisions in the PBS and compare the option-specific elements through their footprints. Reconcile overlapping footprints so a shared element is allocated and counted once. Count parts and interfaces on a common basis. Evaluate replacement boundaries, access, and commonality against the documented configuration and effectivity of the other model. Apply mandatory requirements and maturity criteria before scoring the remaining options.

**Authorised changes.** Each `effects` item is `{view, action, ref, description}`. The actions for effects and footprints are `create`, `update`, `populate`, `retire` and `remap`. Allocate the selected requirements in ReqBS and trace the resulting product and interface changes in PBS and IBS. An effect references the affected object in its view. A `create` can carry `ref: null` pending allocation by that view. Record the implemented object's reference in the implementation evidence and link it back to the KNOT and ruling ID. PBS implementation is an author act, including when an authorised author applies a completion engine. A `PROVISIONAL` ruling carries empty `effects` and `embodied_in` lists.

**Embodiment.** Each `embodied_in` entry is a typed baseline reference `{view: baseline, ref}`. Add it for the first ratified baseline that verifies the resulting configuration in its applicable scope. Use a separate entry for each scope whose first embodiment occurs in a different baseline. Preserve earlier references when adding one. The release act and its evidence remain governed by [QPLUS-LC-RATIFY-001 and QPLUS-LC-AGE-001][LCM].

**Pending PBS allocation.** A gate is a typed `affects` entry `{view: PBS, ref, relation: gates, note}`. Use the existing canonical PBS identifier and state the pending allocation in `note`. The view includes active KNOTs with `OPEN` or `DEFERRED` resolution. The note identifies the portion of the node to which the gate applies.

## Change record

| Issue | Content |
|---|---|
| 1 | Definitions from AEROSPACEMODEL as restated on 2026-11-08; kinds; identifier grammar without `LC01`–`LC14` and without classification, S-ATLAS addresses in the `taxonomy` field; record fields and vocabularies; provisional rulings; scoring gate; filing by scope; research briefs, effectivity, product footprints, ruling effects and embodiment, and PBS gates. Rules 1–18. The fields `effectivity`, `effects` and `embodied_in` were added to the recorded ruling R1 of `KNOT-EWTW-NRG-001` with empty values when they were introduced: a schema migration of a provisional ruling while this issue is proposed, not a rewriting under rule 7 |
| 1, revision of 2026-11-13 | The criterion record with its two classes and its two states; a criterion that is only proposed does not open the gate of rule 5 |

[AEROSPACEMODEL]: https://github.com/AmedeoPelliccia/AEROSPACEMODEL
[CM-001]: ../01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/AMPEL360-PBS-PN-CM-001_Assembly-Station-and-Part-Number-Breakdown.md
[CM-002]: ../01-02-01-01-01-01_SBS_System-Breakdown-Structure/AMPEL360-SBS-ID-CM-002_Cross-Structure-Identification.md
[LCM]: ../../../../../../02_LIFECYCLE_MODEL/README.md
