# AMPEL360-REL-CM-005 — Architecture Relations

**Issue 1** · Owner: `STK_CM` (proposed) · Authority: AM.PEL · Status: **PROPOSED**
**Approval act:** not yet recorded. On approval, this line names the act: commit or merge, date, authority.

---

## 1. Purpose and scope

This convention governs typed relations between identified things in the AMPEL360 programme, and how they are projected onto a model's KNOT register. A relation is a recorded claim: *this technology requires that one*, *this carrier is assigned to that model*. Read through the programme's decisions, the relations give the candidates for a decision and a check of what that decision waits for.

A projection proposes. Options enter a KNOT through its owner, and decisions are rulings under [`AMPEL360-KNOT-CM-004`][CM-004].

The convention applies to the eWTW [architecture relations](README.md) node and, by adoption, to sibling models. Relations between taxonomy nodes are governed by [`QPLUS-REL-001`][REL-001], which belongs to the taxonomy owner. This convention reads them.

## 2. Levels

A relation is recorded once, at the level of the authority that can change it.

| Level | A relation states | Changed by | Recorded in |
|---|---|---|---|
| Taxonomy | What holds of a technology for any programme | Taxonomy owner | `taxonomy-relations.yaml`, under [`QPLUS-REL-001`][REL-001] |
| Programme | What AMPEL360 assigns, excludes or admits across its models | Programme authority | `programme-relations.yaml` (§4) |
| Model | How the model's decisions, requirements and elements depend on one another | Model owner | The KNOT register, the ReqBS and the FBS — read, not copied (§5) |
| Product | What holds of a configured element | Authors of the PBS, the IBS and the baselines | Station records, the ICD register, baseline records — read, not copied (§6) |

## 3. Records

A relation file is YAML. Each record has a `key` in lower-case kebab form, unique across the files of a node and never reused. An S-ATLAS address is a quoted string. A reference to another namespace is `{ns, id}`.

| Field | Meaning |
|---|---|
| `key` | Identity of the record |
| `relation` | The predicate, read from `subject` to `object` |
| `subject`, `object` | The two ends |
| `for` | The role within which the relation holds; `null` for any role |
| `conditions` | The technical conditions under which the claim holds |
| `source` | The document and clause, or the act, that supports the claim |
| `source_checked` | The date, as `YYYY-MM-DD`, on which the source was read against the claim; `null` until then |
| `authority`, `state` | Who can change the record, and `PROPOSED`, `RATIFIED` or `WITHDRAWN` |

A programme exclusion or assignment carries `ruling` in place of `source`, `source_checked`, `authority` and `state`. Its support, authority and state are those of the ruling it cites, written `KNOT-<MIC>-<TOPIC>-<NNN>#R<n>` and read from the register. A decision link (`decided-by`) is a record like the others, with its key, its authority and its state.

## 4. Programme relations

| Relation | From → to | Recorded under | Meaning |
|---|---|---|---|
| `assigned-to` | Technology, energy carrier or function → model | `assignments` | The programme gives it to that model |
| `excluded-from` | S-ATLAS address → model, for one role or for any | `exclusions` | The address, and everything under it, leaves the option sets of the model |
| Combination | Role and model → two or more members of the role's alternatives | `combinations` | The members may be used together in one architecture |
| `decided-by` | Role and model → KNOT | `decided-by` | The KNOT whose ruling chooses among the candidates for the role |
| `constrained-by` | Model, capability or option → programme requirement or policy | — | A requirement that screens candidates |
| `common-with` | Element ↔ element of two models, with the commonality objective | — | Elements meant to be common |
| `certification-basis` | Model and effectivity → requirements, amendments and special conditions | — | The agreed basis against which obligations are read |

The subject of an assignment is an S-ATLAS address, or `{ns, id}` with `ns` set to `energy-carrier` or `function`. Its object is `{ns: model, id}`. A model is named as its folder under the models node of the programme: `eWTW`, `BWB-Q100`.

The last three relations are defined and have no record yet. `tools/relations_project.py` does not read them.

## 5. Model relations

These relations already have an owning record. A view reads them there.

| Relation | From → to | Read from |
|---|---|---|
| `option-of` | Option → KNOT | `options` of the KNOT (CM-004 §5) |
| `depends-on`, `closed-with` | KNOT → KNOT | `depends_on`, `closed_with` |
| `serves` | KNU → KNOT | `serves` of the KNU |
| `affects`, `gates` | KNOT → object of an SBS view | `affects` of the KNOT |
| `owns` | KNOT → product element | The `create` item of a `pbs_footprint`; other items name that KNOT in `owner` (CM-004 rule 18) |
| `allocated-to` | Requirement or function → element | `allocatedTo:` in the ReqBS ([CM-002][CM-002] §3); the FBS allocation matrix |
| `satisfies` | Element → requirement | `satisfies:` in the ReqBS — `null` until closed by evidence |
| `derives-from` | Requirement → source requirement | No record yet |
| `verifies` | Verification case → requirement | No record yet; the ReqBS states the method only |

`allocated-to` has this one meaning. The programme act that gives a technology or a carrier to a model is `assigned-to`.

## 6. Product relations

| Relation | From → to | Read from |
|---|---|---|
| `realizes` | PBS station → S-ATLAS address | `realizes:` of the station record ([CM-001][CM-001] §3.1) |
| `interfaces-with` | Element ↔ element | The [ICD register][ICD-REG]. The ICD holds the direction of each flow |
| `embodied-in` | Ruling → baseline | `embodied_in` of the ruling (CM-004 §8) |
| `supersedes` | Baseline or ruling → its predecessor | `supersedes:` of the baseline record; the ruling history |
| `substitutes` | Replacement → replaced item | No record yet. Needs its own evidence of fit, interfaces, performance and effectivity |
| `certified-for` | Configuration → type or variant | No record yet. Exists only as a reference to an approval issued by the competent authority |
| `data-derived-from` | Artefact or evidence → the versioned input it was produced from | No record yet |

A taxonomy alternative can lead to an option. It never stands for a substitution, which is a product relation with its own evidence.

## 7. Rules

1. A relation has one owner. It is recorded at one level and read from there. A view never restates it.
2. A relation is a claim, not a decision. Nothing enters a KNOT, the PBS or a baseline because a projection shows it.
3. A relation holds at the address it is recorded for. The nodes above and below do not inherit it, and relations are not chained: `A requires B` and `B requires C` do not give `A requires C`. An exclusion is the one exception: it covers its address and everything under it, so that an excluded scope is not re-entered through a sub-node.
4. Alternatives are a set per role ([QPLUS-REL-001][REL-001] §3), never pairs. Each member can fill the role alone. Using two members together needs a programme combination, and its members belong to the set.
5. A symmetric relation is stored once, with the lower address as `subject`.
6. `requires` names what a candidate brings with it, and the projection lists it beside the candidate. `enables` marks an opportunity and never creates a prerequisite. The prerequisites of a decision come from the ownership of product elements (CM-004 rule 18) and are checked against `depends_on`.
7. A record becomes `RATIFIED` by the authority of its level, with a `source` that is public or in this repository and a `source_checked` date. A ratified record is not edited: it is withdrawn and a record with a new key replaces it. Withdrawn records stay in the file. A withdrawn alternatives set leaves its role free for the set that replaces it, and its members are no longer candidates.
8. An exclusion or an assignment cites a ruling in the register, and its state is the state of that ruling. A `PROVISIONAL` ruling gives a provisional exclusion.
9. A combination that includes an excluded member is reported for review. It is neither dropped nor kept silently.
10. A candidate with no S-ATLAS address is listed as `unaddressed` with its nearest node. This convention gives it no address: the taxonomy owner decides.
11. No record states conformity. `satisfies`, `verifies` and `certified-for` are read from records that carry their own evidence and, for `certified-for`, the approval.
12. A role has one deciding KNOT per model, and the effectivity of that KNOT includes the model.

## 8. Projection

For a role and a model, [`tools/relations_project.py`][TOOL]:

1. Takes as candidates the members of the role's alternatives and the combinations admitted for the role and the model.
2. Marks a candidate `excluded` when an exclusion for the model covers it, with the ruling and its state. A combination with an excluded member goes to review (rule 9). The others are `open`.
3. Joins each candidate to the product elements of the register filed at the candidate's address or at a node above it, with the KNOT that owns each element. An element counts while an option that creates it is `open` or `retained`.
4. Lists the `requires` relations recorded at the candidate's address for the role.
5. Compares the open candidates with the options of the deciding KNOT that still stand — `open` or `retained` — by the addresses of their footprints. A candidate whose option was rejected or excluded is named with that option.
6. Lists the chapters of open candidates that the `taxonomy` field of the KNOT does not include.
7. Derives the prerequisites — the KNOTs that own the elements of the candidates not excluded — and compares them with `depends_on`. Both sides are closed over `depends_on` and `closed_with` before the comparison.

A difference found in steps 5, 6 or 7 is reported to the KNOT owner. The tool changes no record.

Two limits apply in this issue. The join of step 3 is as precise as the address of the footprint: an element filed at a chapter matches every candidate in that chapter. Step 5 compares addresses, not the content of the options.

## 9. Verification

From the repository root:

```bash
TAX="01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_S-ATLAS"
MODEL="01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW"
python3 tools/relations_project.py "$MODEL/01-02-01-01-01-03_REL_Architecture-Relations" "$MODEL/01-02-01-01-01-02_KNOT_Knowledge-Node-Register" "$TAX" --check
python3 tools/relations_project_test.py
```

The tool checks keys, relation names, S-ATLAS addresses, the form of alternatives sets and combinations (rule 4), the order of symmetric relations (rule 5), states, dates and the source of a ratified record (rule 7), the rulings cited by exclusions and assignments (rule 8), the ends of an assignment, the models named by programme records, and the deciding KNOT of each role (rule 12). An input that cannot be read, a KNOT recorded in more than one file and a file whose name differs from its `knot_id` are failures. Control characters found in a record are printed in escaped form. The tool exits with status 1 on a failure and then prints no projection.

The node README holds the output between two markers. `--check` fails when that section differs from the output, and `--write` replaces it. The tool reads the working tree: the run that counts is the one on a commit, in review or on a clean checkout. Rules 1 and 2, the public availability of a source and the no-edit part of rule 7, and rule 11 are checked by review.

## Change record

| Issue | Content |
|---|---|
| 1 | From draft 0.1.0 of 2026-11-12, pinned to `565b5bb`: the four levels, the relation sets and the projection of the `SRC` options. Changes to the draft: alternatives are sets per role and not pairs, so that nothing is inferred by chaining; the taxonomy relations move to `QPLUS-REL-001`; `allocated-to` keeps its model meaning and the programme act becomes `assigned-to`; `source_checked` added; rules on inheritance, on `enables`, on ratification and on combinations with an excluded member; the closure order, which restated `depends_on`, is replaced by prerequisites derived from element ownership and compared with `depends_on`; scope check against the `taxonomy` field of the KNOT; the script and its tests are in `tools/` |
| 1, review of 2026-11-13 | Decision links are keyed records with authority and state; rule 12; the form of the ends of an assignment; `source_checked` is a date; a withdrawn set leaves its role free (rule 7); only options that still stand count in steps 3 and 5; the generated section of the README is written and checked by the tool |

[CM-001]: ../01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/AMPEL360-PBS-PN-CM-001_Assembly-Station-and-Part-Number-Breakdown.md
[CM-002]: ../01-02-01-01-01-01_SBS_System-Breakdown-Structure/AMPEL360-SBS-ID-CM-002_Cross-Structure-Identification.md
[CM-004]: ../01-02-01-01-01-02_KNOT_Knowledge-Node-Register/AMPEL360-KNOT-CM-004_Knowledge-Nodes-and-Units.md
[REL-001]: QPLUS-REL-001_Taxonomy-Relations.md
[ICD-REG]: ../01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-08_IBS_Interface-and-Installation-Breakdown-Structure/ICD-REGISTER.yaml
[TOOL]: ../../../../../../tools/relations_project.py
