# Withdrawal record — the publications of chapter 021

| | |
|---|---|
| Subject | The tree of chapter `021` *Air Conditioning / Environmental Control* in the information architecture of the TPuBS, its module of the maintenance manual and its rows of the consolidated registers |
| Finding | `F24` of the [model findings register](../../README.md#9-findings) |
| Asked by | The architecture authority, 2026-11-18 |
| Produced by | Claude, 2026-11-18. The same hand reviewed and withdrew: no second reader has checked this record |
| Takes effect | With the merge of the pull request that carries it |
| Restores from | Commit `53848df1` — see [How to restore](#how-to-restore) |

The authority asked:

> «se la documentazione del S-ATLAS 021 in TpuBS o in qualsiasi altro nodo é incoerente, prematura o completamente sbagliata, pòtresti individuarla ed eliminarla? allo stesso tempo aggiornare i commenti che la referenziano»

The publications of chapter `021` were all three, and are withdrawn whole. The product node, the interface dossier, the functions and the taxonomy of the chapter are kept. One record of the KNOT register said a wrong thing about the taxonomy of the chapter and is corrected.

---

## What was on `main`

At `fe6e4685`, from the first commit of the repository, `53848df1` of 2026-08-22. No later commit changed these files.

| What | Count |
|---|---|
| Files under `01_INFORMATION-ARCHITECTURE/S-ATLAS_000-099/020-029_Core-Aircraft-Systems/021_Air-Conditioning-Environmental-Control/` | 789 |
| Sections `021-000` … `021-900`, and subject nodes under them | 23 and 50 |
| Data modules, dated 9 and 13 June 2026 — descriptive and procedural | 210 — 61 and 149 |
| Illustrations — drawn, and placeholders | 41 — 2 and 39 |
| Requirement lists (DMRL), and the requirements they held | 74 and 207 |
| Module of the maintenance manual, `PM-EWTW-AMM-021_AIR-CONDITIONING.yaml` | 1 |
| Rows of the consolidated requirement list, of 212, and entries of the data management list, of 215 | 207 and 210 |

## What it was measured against

| Rule | Where | What it says |
|---|---|---|
| `QPLUS-LC-PUBCLASS-001` | [Lifecycle Model](../../../../../../../02_LIFECYCLE_MODEL/README.md) 0.7.1, §2.4 and governance rule 24 | Every publication artefact declares one content class. Class `P0`, publication architecture, may proceed from `LC-A`: it plans publications, *carries no prescriptive content (no procedural step, limit, value, warning or caution), and is never the authority for a product statement*. Class `P2`, maintenance content, is released only against released product baselines. A status *states its class truthfully* |
| CM-001 Issue 2, §9 | [`AMPEL360-PBS-PN-CM-001`](../01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/AMPEL360-PBS-PN-CM-001_Assembly-Station-and-Part-Number-Breakdown.md) | The SNS of maintenance publications aligns with the PBS-local code. Publications describe, support or evidence the controlled product and never redefine it; they reference their source one way, through `ssot-ref.yaml` |
| The doctrine of the TPuBS | [README](README.md) v3.0 | *S-ATLAS determines where information semantically belongs* |
| The declared scope | [Model README](../../README.md), header and §2; ruling R1 of `KNOT-EWTW-NRG-001` | The model is at stage `LC-A`, every identifier `PLANNED`, with no design baseline. It carries no hydrogen; cryogenic tanks are out of scope |

The rule on content classes entered the Lifecycle Model on 2026-10-12, with version 0.7.0. The tree is older. It was not written against the rule, and was not brought in line with it afterwards.

## What was found

Counts are of files in the tree at `53848df1`, unless a row says otherwise.

| # | Finding | Count | Against |
|---|---|---|---|
| | **Premature** | | |
| 1 | No artefact declared a content class | 0 of 789 | `QPLUS-LC-PUBCLASS-001` |
| 2 | Procedural data modules carried procedural steps — servicing, scheduled maintenance, removal, installation — for a system that has no station under `eWTW-PBS-021-000`, in a model at `LC-A` | 149 | `P0` carries no procedural step; `P2` needs released baselines |
| 3 | Effectivity by serial number, and a modification `MOD-EWTW-021-001` *embodied MSN 0050* that split three information codes into data modules before and after it. No configuration of the aircraft exists to which a serial number or a modification can apply | 53 and 14 | Model README §4: the link runs from the product, with its configuration and effectivity, to the publication |
| | **Incoherent** | | |
| 4 | Every requirement read `AUTHORED`. Of the 61 descriptive data modules, 51 said *Stub data module pending authoring*; all 210 were marked unverified; all were at issue 001, in work 00, while the registers of 41 subjects said `in_work: true`; and the READMEs and metadata of the nodes said `scaffold` | 207 | A status states its class truthfully |
| 5 | Subject nodes at addresses that the taxonomy does not define. S-ATLAS defines subjects of chapter `021` under `021-510` and `021-900` only, nine in all | 41 of 50 | The doctrine of the TPuBS |
| 6 | The SNS of the data modules was derived from the taxonomy address. In 41 subjects it was marked provisional, pending a file `_CSDB-CONTROL/SNS-mapping.yaml` that is not in the repository. No PBS-local code exists below the chapter to align it with | 123 files name the file | CM-001 §9 |
| 7 | No subject was linked to the product. The nine subjects of `021-510` and `021-900` named as their source `eWTW-PBS-60-20`, under `eWTW-PBS-00_Aircraft-Product/eWTW-PBS-60_Mechanical-and-Utility-Systems`: no such node exists, and the chapter node is `eWTW-PBS-021-000`. The other 41 carried no source link | 46 files name the node | CM-001 §9 |
| 8 | Applicability files described the eWTW as an *Electric wing-to-wing configuration*. WTW is wide tube and wing | 41 | Model README |
| 9 | Data modules and applicability files named a business-rules data module, `DMC-EWTW-A-00-00-00-00A-022A-D`, that is not in the repository; the governance layer of the TPuBS holds none | 251 | — |
| 10 | The convention named as governing, `AMPEL360-AMM-INFOCODE-CM-001`, has no text in the repository | — | — |
| 11 | The two drawn illustrations carried the retired name *G-ATLAS* and a claim of their own on the No-AAA rule. The first sent the reader to sections `021-020`, `021-030` and `021-050`, which do not exist, and labelled the energy-carrier bay *BATT BAY*; PBS notes cited it as their authority (finding F01) | 2 | A publication is never the authority for a product statement |
| 12 | Requirement matrices of the subjects held *TBD* in every row | 171 rows | — |
| 13 | The originator of the data modules was *QplusA .INC*, that of the illustrations *GQAOA .INC* | 210 and 2 | — |
| | **Wrong** | | |
| 14 | *Cryogenic Cold Sink Utilization* stood as part of the environmental control system of the eWTW, with a description, a servicing task and procedures to remove and install it | 10 | Ruling R1 of `KNOT-EWTW-NRG-001`: liquid hydrogen is allocated to the BWB-Q100. Model README §2: cryogenic tanks are out of scope |
| 15 | Design data with no source on record: a two-stage centrifugal compressor on foil-gas bearings, a 540 V DC permanent-magnet motor, 45,000 rpm, a remote controller in the forward equipment bay; then a hermetic scroll compressor in a vapour-cycle loop at 9,000 rpm with an integrated silicon-carbide controller. The model declares electric packs and no cycle, and the voltage of the distribution is the work of `KNU-EWTW-SRC-001-03` | 8 files carry the voltage | `P0` carries no value |
| 16 | Procedures to remove and install subjects that are not items — the recovery of waste heat, the coupling with the thermal management system, the interface of the air supply — and servicing and scheduled maintenance of *ECS General and Zoning* and of *Distribution Ducting Architecture* | — | — |

The compressor data and the modification of finding 15 and finding 3 were written as the worked example of the information-code convention. They read as data of the eWTW.

## What is withdrawn

- the tree `021_Air-Conditioning-Environmental-Control/` of the information architecture, whole: 789 files;
- `PM-EWTW-AMM-021_AIR-CONDITIONING.yaml`, and its entry in `PMC-EWTW-AMM.yaml`, which now lists no module;
- the rows of chapter `021` in `DMRL-EWTW.yaml`, `DMRL-EWTW.csv`, `DMRL-EWTW.md` and `DML-EWTW.xml`. The four registers are aggregations of the requirement lists of the nodes; no generator is in the repository. The rows of the nodes that remain were kept as they were, and the count restated: five requirements, five data modules, all of `003-900-010`.

Nothing could be kept as class `P0`. A plan of the publications of the chapter needs subject addresses that the taxonomy or the product gives, and an SNS from the PBS-local codes of stations that do not exist yet.

## What is kept, and why

| Kept | Why |
|---|---|
| The doctrine of the TPuBS, its governance layer, its 19 publication modules and its two generated layers | Architecture of the publications. The [README](README.md) carries a note, at v3.0.1, that its examples on chapter `021` point to no file |
| Chapter `003-900` of the information architecture | Outside the chapter that the authority named. It has the same form: one subject with five data modules that read `AUTHORED`, three of them with procedural steps, for charging on the ground a battery that only option C carries since ruling R2. See [For the author](#for-the-author) |
| `eWTW-PBS-021-000`, the product node of the chapter | A chapter scaffold that states its mapping and nothing else. It is the home of the stations of the system when they are realized |
| `eWTW-IBS-533001-021`, the dossier of the outflow-valve surround | `PLANNED` in every section. It names the taxonomy chapter as its counterpart, and no publication |
| The functions `eWTW-FBS-70-10`, `-20` and `-40` | They name no solution of the chapter |
| The taxonomy of chapter `021` | The standard of every programme, and no documentation of the eWTW. A protected area. Two points on it are for its author, below |
| What the model declares: an electric system without bleed air, with electric packs in the wing-to-fuselage fairing | Declared by the authority (model README §2 and §3, row 9). It does not rest on the publications |

## What the tree held that is written nowhere else

1. **The worked example of `AMPEL360-AMM-INFOCODE-CM-001`.** CM-001 §9 cites the convention; its text is not in the repository. The tree applied it to the nine subjects of `021-510` and `021-900`, in this form:

   ```text
   subject node
    └── <infocode>/                       information code (040, 200, 520, 720 …)
          ├── ssot-ref.yaml               one-way link to the PBS source
          ├── config-management.yaml      modification stack → resulting effectivity
          └── <ic><variant>_EFF-<id>/     one folder for each range of effectivity
                └── DMC-…-<ic><variant>-…xml   the data module, with its applicability
   ```

   Its fork rule is kept in §3 of the [README](README.md): a new variant of an information code exists only where a modification changes the content of the data module; a change of effectivity alone updates the stack.
2. **The reason why chapter `021` has no section `021-100`.** The chapter README of the tree gave it: *the conventional bleed/compression section is footprinted out (no engine bleed in the green architecture)*. The taxonomy does not state it.
3. **Two drawn illustrations**, issue 01 of 2026-07-06: `ICN-EWTW-021000010-001-01`, general arrangement and cabin zoning, and `ICN-EWTW-021200010-001-01`, distribution ducting. An issue 02 of the first was the closing condition of finding F01; none is due now.

## References updated

| Where | What |
|---|---|
| [TPuBS README](README.md), v3.0.1 | A note on the withdrawal; §4 no longer lists the withdrawn module |
| [Model README](../../README.md), 0.3.29 | §1 counts; §2 and §4; finding F01 restated and F24 entered |
| PBS — an area that only the authority changes; these edits are ratified with the merge | The notes that named the illustration `ICN-EWTW-021000010`: stations `053-100-030`, `053-200-020` and `053-900-010`, the chapter `053` README and its breakdown. The row of F01 in the PBS README, 0.2.3 |
| Root `README.md` and `contributing.md` | The engineering focus on the publications of chapter `021`, which also named a rendition stamper that is not in the repository; and two examples that gave the TPuBS node `021-200-010` as the address of a simulation. The address is now the product node `eWTW-PBS-021-000` |
| [EBS index](../01-02-01-01-01-01-07_EBS_Evidence-Breakdown-Structure/EVIDENCE-INDEX.yaml) | A row for this record |

## Corrected in passing

The [concept of operations of the environmental control system](../../01-02-01-01-01-02_KNOT_Knowledge-Node-Register/000_General/evidence/CONOPS-EWTW-ECS-001/README.md), issues 0.1.0 and 0.1.1, said that S-ATLAS `021` names no node for compressing outside air to cabin pressure. It does: subject `021-900-070`, *Bleedless Air-Supply Interface (e-Compressor / Process Air)*. Issue 0.1.2 binds the function to `021-900` and restates the open input. The error was of this reviewer, who wrote both issues.

## For the author

Not changed here; each is the author's to decide.

1. **The taxonomy has no section for compressing outside air.** It names the electric compressor of the air supply as an *interface* of the energy-system thermal integration (`021-900-070`), and another electric compressor inside the cooling unit (`021-510-010`). In an aircraft without bleed air the compressors are machines of the system, with their own maintenance.
2. **The taxonomy gives the cooling two forms.** It says that the air-cycle pack is superseded by an electrically driven compressor with a vapour cycle or a cryogenic cold sink, and it names no air-cycle machine. The model declares electric packs and not their cycle: if an air cycle fed by electric compressors is a candidate, the taxonomy has no home for it.
3. **Chapter `003-900` of the TPuBS** has the defects of findings 1, 2 and 4.
4. **The convention `AMPEL360-AMM-INFOCODE-CM-001` needs a text.** Its only worked example is withdrawn with this tree.
5. **Finding F01 keeps two labels**, both in the chapter `053` README of the PBS: the row *Energy carrier (battery)* of its cross-references and its footnote on `028`.

When the publications of the chapter are planned again, the rule asks for class `P0` declared on every artefact, requirement lists whose status says planned, subjects that the taxonomy defines or that are proposed to it, and an SNS from the PBS-local codes of the stations.

## Since this record

Acted on at the request of the authority of 2026-11-20. The text above is as written on 2026-11-18.

| Point for the author | What was done |
|---|---|
| 1. No section for compressing outside air | Section `021-100` *Air Compression (Electric)* added to the taxonomy, with five subjects. `021-900-070` stays as the interface of the compressors with the energy system |
| 2. The cooling has two forms | Not acted on: it was not asked |
| 3. Chapter `003-900` of the TPuBS | Withdrawn: [record of 2026-11-20](TPuBS-EWTW-003-900_withdrawal_2026-11-20.md) |
| 4. The convention needs a text | Drafted for ratification: [`AMPEL360-AMM-INFOCODE-CM-001`](AMPEL360-AMM-INFOCODE-CM-001_Information-Code-Breakdown-and-Effectivity-Variants.md), Issue 1 |
| 5. Two labels of finding F01 | Neutralised in the chapter `053` README of the PBS |

## How to restore

The tree as it was, defects included:

```bash
A="01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure"
git checkout 53848df1 -- "$A/01_INFORMATION-ARCHITECTURE/S-ATLAS_000-099/020-029_Core-Aircraft-Systems/021_Air-Conditioning-Environmental-Control"
```

One file, for instance the first illustration, without restoring the tree:

```bash
git show "53848df1:$A/01_INFORMATION-ARCHITECTURE/S-ATLAS_000-099/020-029_Core-Aircraft-Systems/021_Air-Conditioning-Environmental-Control/021-000_General/021-000-010_ECS-General-and-Zoning/ICN/ICN-EWTW-021000010-001-01.svg" > ICN-EWTW-021000010-001-01.svg
```

## How to verify

From the repository root, with `A` as above:

```bash
git ls-tree -r --name-only 53848df1 -- "$A/01_INFORMATION-ARCHITECTURE/S-ATLAS_000-099/020-029_Core-Aircraft-Systems/021_Air-Conditioning-Environmental-Control" | wc -l   # 789
git grep -l proceduralStep 53848df1 -- "$A/01_INFORMATION-ARCHITECTURE/S-ATLAS_000-099/020-029_Core-Aircraft-Systems/021_Air-Conditioning-Environmental-Control" | wc -l       # 149 — finding 2
git grep -h 'status: "AUTHORED"' 53848df1 -- "$A/01_INFORMATION-ARCHITECTURE/S-ATLAS_000-099/020-029_Core-Aircraft-Systems/021_Air-Conditioning-Environmental-Control" | wc -l   # 207 — finding 4
find "$A/01_INFORMATION-ARCHITECTURE" -type d -name '021*' | wc -l                                  # 0 after the withdrawal
git grep -n -E 'ICN-EWTW-021|DMC-EWTW-A-21|DMREQ-021|PM-EWTW-AMM-021' -- . ':!*withdrawal_2026-11-18.md' ':!*/README.md'   # nothing
```

The last command leaves out this record and the READMEs, which name what was withdrawn.
