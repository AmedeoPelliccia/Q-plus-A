# QPLUS-REL-001 — Taxonomy Relations

**Issue 1** · Owner: taxonomy owner · Authority: AM.PEL · Status: **PROPOSED**
**Held in:** the eWTW model, as a proposal. The taxonomy (`01-03_TECHNOLOGIES`) is a protected area: adopting this convention and moving its records there is an act of the taxonomy owner. The identifier is proposed with the text.

---

## 1. Purpose

This convention governs relations between Q+ATLANTIDE nodes that hold for any programme. They are the reusable part of an architecture study. A programme reads them, applies its own decisions and obtains its candidates ([`AMPEL360-REL-CM-005`][CM-005]).

## 2. Relations

| Relation | From → to | Meaning |
|---|---|---|
| `requires` | Node → node | The subject does not work without the object, under the conditions stated |
| `enables` | Node → node | The subject makes the object possible. An opportunity, never a prerequisite |
| `interfaces-with` | Node ↔ node | The two share a boundary: power, thermal, data or mechanical. Symmetric |
| `draws-on` | Node → node, often in another band | The subject uses a technology or a method classified at the object |
| `references-standard` | Node → `{document, clause}` | The clause is screened for applicability wherever the node is used |

## 3. Alternatives

An alternatives set names a role (`for`) and the nodes that can each fill it alone (`members`: two or more addresses, sorted). `home` is the node that describes the role itself, when one exists. There is one set per role.

Pairs of alternatives are not recorded. With pairs, `A` alternative to `B` and `B` alternative to `C` invite the inference that `A` and `C` are alternatives, and the role is lost on the way. A set states the role and its members in one record.

A candidate that has no node is listed under `unaddressed`, with its `nearest` node. It marks a gap for the taxonomy owner. It is not an address.

## 4. Rules

1. A taxonomy relation is programme-agnostic. Its subject, object, role and conditions name no programme, model or ruling.
2. A relation is recorded at the most specific address its source supports, and holds at that address only (CM-005 rule 3).
3. Fields and states are those of CM-005 §3. A record is ratified by the taxonomy owner, with a public source that has been read against the claim.
4. `references-standard` names the issuing body and the clause. The issue or amendment that applies is set by the certification basis of a model, not here.
5. A relation changes no node. Titles, scope and addresses stay governed by the taxonomy.

## 5. Filing on adoption

Proposed, for the taxonomy owner to decide: one relations file per S-ATLAS chapter, holding the relations whose subject lies in that chapter. An alternatives set is filed in the chapter of its `home`, or in `000_General` when it has none. A relation that crosses bands is filed with its subject.

## 6. Pilot records

[`taxonomy-relations.yaml`](taxonomy-relations.yaml) holds two alternatives sets and five relations for the eWTW pilot, all `PROPOSED`. Two have a source read against the claim on 2026-11-12; three have no source yet.

## Change record

| Issue | Content |
|---|---|
| 1 | Five relations and the alternatives set, separated from draft 0.1.0 of `AMPEL360-REL-CM-005`; `impacts`, from the first list of relation types, is not adopted at this level, because it does not say what follows for either end; the effect of a decision on an object is the model relation `affects` (CM-005 §5); `substitutes`, `certified-for` and `data-derived-from` are product relations (CM-005 §6) |

[CM-005]: AMPEL360-REL-CM-005_Architecture-Relations.md
