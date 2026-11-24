# AMPEL360-AMM-INFOCODE-CM-001 — Information-Code Breakdown and Effectivity Variants

**Issue 1** · Owner: `Q-DATAGOV` (proposed) · Authority: AM.PEL · Status: **PROPOSED**
**Approval act:** not yet recorded. On approval, this line names the act: commit or merge, date, authority.

Drafted by Claude on 2026-11-20, at the request of the authority. [CM-001][CM-001] §9 has cited this convention since its Issue 2, thirteen station records name it as their parallel, and no text of it was in the repository. Its only worked example was withdrawn on 2026-11-18 with the publications of chapter `021` ([record][WDR-021]). A clause marked **[carried]** restates what those documents and that example said. A clause marked **[added]** is proposed by the drafter, to bring the convention in line with rules that came after the example. No second reader has checked this text.

---

## 1. Purpose and scope

This convention governs three things in the information architecture of a TPuBS:

- how a subject node breaks down by information code;
- how each information code is linked to the product that it describes;
- how a modification of the product becomes, or does not become, a further data module with its own effectivity.

It begins where a data module carries content bound to a product: classes `P1` and `P2` of the Lifecycle Model. Before that, §8 applies.

It does not govern the requirement list of a node, the publication modules, the grammar of the data module code, or the content classes and their gates. §2 names the rule that does.

## 2. Where it stands among the rules

| Rule | What it fixes | What this convention adds |
|---|---|---|
| [`QPLUS-LC-PUBCLASS-001`][LCM], Lifecycle Model §2.4 | The content class of every publication artefact, and its gate | Nothing. §8 says what a subject node holds at class `P0` |
| [`QPLUS-LC-DECOUPLE-001`][LCM], §2.1 | A change upstream gives an iteration downstream, or a recorded no-action disposition | Where that record is kept for a data module: the modification stack, §6 |
| [`QPLUS-LC-SSOT-PIN-001`][LCM], §2.2 | Every revision of a deliverable pins the revisions of its sources | Where the pin is kept for a data module: §5 |
| [CM-001][CM-001] §9 | The SNS follows the PBS-local code; publications never redefine the product; the link to the source is one-way, in `ssot-ref.yaml` | The place and the content of `ssot-ref.yaml`: §5 |
| [TPuBS README][TPUBS] §3 | A requirement list (DMRL) in every node; the fork rule in one sentence | The anatomy under the requirement list, §4, and the fork rule in full, §7 |

Where this text and one of those rules differ, that rule holds and this text is corrected.

## 3. Terms

| Term | Meaning |
|---|---|
| **Subject node** | A node `0CC-SS0-UU0` of the information architecture. On the publication side it is what the assembly station of CM-001 is on the product side: station records carry `parallels: AMPEL360-AMM-INFOCODE-CM-001` |
| **Information code** | The S1000D code of a kind of information: `040` description, `200` servicing, `520` removal, `720` installation, and so on |
| **Solution** | One data module that answers one information code for one range of effectivity |
| **Variant** | The S1000D `infoCodeVariant` — `A`, `B`, … — that tells the solutions of one information code apart |
| **Modification stack** | The baseline of the product and, in order, the modifications that bear on the subject |
| **Fork** | The creation of a further solution of an information code |

## 4. Anatomy of a subject node

```text
<0CC-SS0-UU0>_<Title>/
├── DMRL-<0CC-SS0-UU0>.yaml            the requirements of the node (TPuBS README §3)
├── subject-infocode-breakdown.yaml    the information codes of the subject and their variants
├── <ic>_<Name>/                       one folder for each information code
│   ├── ssot-ref.yaml                  the product source, one way (§5)
│   ├── config-management.yaml         the modification stack and the solutions it gives (§6)
│   └── <ic><v>_EFF-<id>/              one folder for each solution
│       └── DMC-…-<ic><v>-….xml        its data module, with its applicability
└── ICN/                               the illustrations of the subject
```

1. **[carried]** A subject node is a folder, not a file. It contains the information-code breakdown.
2. **[carried]** Each information code of the subject has one folder, named by the code and a title: `040_Description`.
3. **[carried]** Each solution has one folder, named by the code, the variant and an effectivity identifier: `040B_EFF-POST-MOD-<id>`. The folder name binds the variant to the effectivity.
4. **[carried]** A solution folder holds one data module. The variant in its data module code is the variant of the folder.
5. **[carried]** `subject-infocode-breakdown.yaml` lists each information code with its name, the number of its solutions and their variants. **[added]** It agrees with the folders, and never says more than they hold.
6. **[added]** The requirement list of the node names every data module of the node, with its requirement. A data module that no requirement names does not belong in the node.

## 5. The product source

1. **[carried]** Each information-code folder holds one `ssot-ref.yaml`. It names the product item that the data modules of that code describe — PBS id, title, path and kind — and says that the link is one-way.
2. **[carried]** The link runs from the product to the publication. Nothing is read from a publication into the PBS, and a publication is never the authority for a statement on the product.
3. **[carried]** The SNS in the data module code follows the PBS-local code of the item that `ssot-ref.yaml` names (CM-001 §9).
4. **[added]** The link resolves: the item exists on disk at the path given. A link to an item that does not exist is a defect of the node. The withdrawn example named `eWTW-PBS-60-20`, which no PBS holds.
5. **[added]** Each solution records its pinned source set under `QPLUS-LC-SSOT-PIN-001`: the released revisions of the product artefacts that its content was verified against. It is written with the solution, in `config-management.yaml` (§6).

## 6. The modification stack

`config-management.yaml` holds two lists.

| List | Entry | Fields |
|---|---|---|
| `modification_stack` | The baseline, first | `baseline` |
| | Each modification, in order | `mod`, `description`, `affects_this_info_code`, and `content_delta` where it does |
| `resulting_solutions` | Each solution | `variant`, `effectivity`, `msn_range`, and **[added]** `pinned_source_set` |

1. **[carried]** Every modification of the product that bears on the subject stands in the stack of every information code of the subject, with `affects_this_info_code` answered `true` or `false`.
2. **[carried]** Where the answer is `true`, `content_delta` says what changes in the data module: its text, its steps or an illustration.
3. **[added]** Where the answer is `false`, the entry is the recorded no-action disposition that `QPLUS-LC-DECOUPLE-001` asks for.
4. **[added]** A modification carries the identifier that the configuration of the product gives it. A stack does not invent a modification, a baseline or a serial number. The withdrawn example did: `MOD-EWTW-021-001`, *embodied MSN 0050*, on a model with no design baseline.

## 7. The fork rule

1. **[carried]** A further solution of an information code exists only where a modification changes the content of the data module: its text, its steps or an illustration.
2. **[carried]** A change of effectivity alone gives no solution. It updates the stack, and the applicability of the solution that exists.
3. **[carried]** An information code that no modification affects has one solution: variant `A`, effectivity `EFF-ALL`.
4. **[carried]** Variants are given in the order of the stack. `A` is the solution of the baseline.
5. **[carried]** Each data module carries the applicability of its range, so that a publication filtered to one aircraft resolves to exactly one solution for each information code. **[added]** The ranges of the solutions of one information code therefore neither overlap nor leave a gap.

## 8. Before the product exists

**[added]** At class `P0` a subject node holds its requirement list, whose requirements say that they are planned, and at most shells with no prescriptive content. It holds no `ssot-ref.yaml`, no modification stack, no effectivity by serial number and no fork: there is no product item to link, no configuration to pin and no aircraft to apply to.

The anatomy of §4 is built with the first data module of class `P1` or `P2`. The publications of chapters `021` and `003-900` were built before, and were withdrawn ([021][WDR-021], [003-900][WDR-003]).

## 9. Verification

**[added]** Run from a subject node. Each line prints nothing when the node is in order.

```bash
# each information-code folder holds its two records
for d in [0-9][0-9][0-9]_*/; do for f in ssot-ref.yaml config-management.yaml; do [ -f "$d$f" ] || echo "missing $d$f"; done; done

# each solution folder holds one data module, and the variant of its code is the variant of the folder
for s in [0-9][0-9][0-9]_*/[0-9][0-9][0-9][A-Z]_EFF-*/; do
  v=$(basename "$s" | cut -c1-4); n=$(ls "$s" | grep -c "^DMC-.*-$v-.*\.xml$")
  [ "$n" = 1 ] && [ "$(ls "$s" | wc -l)" = 1 ] || echo "check $s"
done

# the product source is on disk (path from the repository root)
grep -h "pbs_path:" [0-9][0-9][0-9]_*/ssot-ref.yaml | sed 's/.*pbs_path: *//; s/"//g' | sort -u |
  while read -r p; do [ -d "$(git rev-parse --show-toplevel)/$p" ] || echo "no such item: $p"; done
```

No node carries the anatomy today, so the checks have nothing to read.

## 10. The form, without a product

The records of one information code that a modification affects. Every value is a placeholder.

```yaml
# <ic>_<Name>/ssot-ref.yaml
subject: "<0CC-SS0-UU0>"
info_code: "<ic>"
ssot:
  pbs_item: "<PBS id of the item described>"
  pbs_item_title: "<its title>"
  pbs_path: "<its path from the repository root>"
  pbs_kind: "<system | station | part>"
  direction: "one-way"
```

```yaml
# <ic>_<Name>/config-management.yaml
subject: "<0CC-SS0-UU0>"
info_code: "<ic>"
convention: "AMPEL360-AMM-INFOCODE-CM-001"
modification_stack:
  - baseline: "<baseline, as the product configuration names it>"
  - mod: "<modification, as the product configuration names it>"
    description: "<what the modification is>"
    affects_this_info_code: true
    content_delta:
      - "<what changes in the text, the steps or an illustration>"
resulting_solutions:
  - variant: "<ic>A"
    effectivity: "EFF-PRE-<mod>"
    msn_range: "<range before the modification>"
    pinned_source_set: ["<released revision of each source>"]
  - variant: "<ic>B"
    effectivity: "EFF-POST-<mod>"
    msn_range: "<range from the modification on>"
    pinned_source_set: ["<released revision of each source>"]
```

## 11. Open points for the authority

1. **The flat folder.** The TPuBS README and `contributing.md` show the data modules of a node in one `DM/` folder. The example of this convention kept them in information-code folders. This text governs the second form and does not say when a node may keep the first.
2. **The pin.** §5.5 and §6 put the pinned source set with each solution, in `config-management.yaml`. The example carried none.
3. **The name.** The identifier says `AMM`. The data modules of a node are common to several publications, which are views (TPuBS README, doctrine). Whether the convention covers every information code of a node, or those of maintenance only, is not written.
4. **More than one modification.** The example had one, and named its two ranges `EFF-PRE-MOD-…` and `EFF-POST-MOD-…`. How an effectivity identifier is formed when two modifications cut the range in three is not written.
5. **The loop position.** The growth method says that the position of an artefact in its loop *shall be recorded in the SSOT impact/config layer (`AMPEL360-AMM-INFOCODE-CM-001` pattern or programme equivalent)* ([C-GROWTH][CGROWTH] §3.1). No field of the example carried it.

## Sources

| Source | What was taken |
|---|---|
| [CM-001][CM-001] Issue 2, §9, and the `parallels:` field of its station record | §5.2, §5.3 and the first term of §3 |
| [TPuBS README][TPUBS] v3.0, §3 | The requirement list in every node; the fork rule in one sentence |
| The example on subject `021-510-010`, at commit `53848df1`: `021_TPuBS-Node-Tree.md`, `subject-infocode-breakdown.yaml`, and the `ssot-ref.yaml` and `config-management.yaml` of its four information codes | The anatomy of §4, the fields of §5 and §6, and §7. Only its form is taken: its product data had no source |
| [Lifecycle Model][LCM] 0.7.1, §2.1, §2.2 and §2.4; [C-GROWTH][CGROWTH] §3.1 | §2, §5.5, §6.3 and §8 |

## Change record

| Issue | Content |
|---|---|
| 1 | First text, drafted on 2026-11-20 from the sources above, at the request of the authority. Five open points, §11 |

[CM-001]: ../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/AMPEL360-PBS-PN-CM-001_Assembly-Station-and-Part-Number-Breakdown.md
[TPUBS]: README.md
[LCM]: ../../../../../../../02_LIFECYCLE_MODEL/README.md
[CGROWTH]: ../../../../../../../02_LIFECYCLE_MODEL/C-GROWTH-METHOD-SPEC.md
[WDR-021]: TPuBS-EWTW-021_withdrawal_2026-11-18.md
[WDR-003]: TPuBS-EWTW-003-900_withdrawal_2026-11-20.md
