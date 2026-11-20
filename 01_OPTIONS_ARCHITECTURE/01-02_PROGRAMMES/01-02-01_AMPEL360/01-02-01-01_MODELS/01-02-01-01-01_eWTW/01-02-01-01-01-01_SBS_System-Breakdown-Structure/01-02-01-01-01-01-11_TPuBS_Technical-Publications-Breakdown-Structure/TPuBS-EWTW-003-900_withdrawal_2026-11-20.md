# Withdrawal record — the publications of chapter 003-900

| | |
|---|---|
| Subject | The tree of section `003-900` *Energy-Replenishment Ground Infrastructure* in the information architecture of the TPuBS, and its rows of the consolidated registers |
| Finding | `F24` of the [model findings register](../../README.md#9-findings) |
| Asked by | The architecture authority, 2026-11-20 |
| Produced by | Claude, 2026-11-20. The same hand reviewed and withdrew: no second reader has checked this record |
| Takes effect | With the merge of the pull request that carries it |
| Restores from | Commit `53848df1` — see [How to restore](#how-to-restore) |

The [record of 2026-11-18](TPuBS-EWTW-021_withdrawal_2026-11-18.md) withdrew the publications of chapter `021` and kept this tree, which the request of that day did not name. It said that the tree had the same defects. On 2026-11-20 the authority asked:

> «puoi eliminare pure le pubblicazioni del 003-900»

The rules are those of the first record: `QPLUS-LC-PUBCLASS-001`, CM-001 §9, the doctrine of the TPuBS, and the declared scope with ruling R2 of `KNOT-EWTW-NRG-001`. This record gives the counts, and what this tree had of its own.

---

## What was on `main`

At `fe6e4685`, from the first commit of the repository, `53848df1` of 2026-08-22. No later commit changed these files.

| What | Count |
|---|---|
| Files under `01_INFORMATION-ARCHITECTURE/S-ATLAS_000-099/003-900_Energy-Replenishment-Ground-Infrastructure/` | 37 |
| Subject nodes — one with data modules, eight placeholders | 9 |
| Data modules, dated 9 June 2026 — two descriptive, two of fault isolation, one procedure | 5 |
| Illustrations — a page that links an image kept outside the repository, and two placeholders | 3 |
| Requirement lists (DMRL), and the requirements they held | 10 and 5 |
| Rows of the consolidated requirement list, and entries of the data management list | 5 of 5, and 5 of 5 |

## What was found

| # | Finding | Count | Against |
|---|---|---|---|
| | **Premature** | | |
| 1 | No artefact declared a content class | 0 of 37 | `QPLUS-LC-PUBCLASS-001` |
| 2 | Data modules carried steps — to connect a charging connector, and to isolate faults of it — for a charging inlet that no item of the PBS holds, in a model at `LC-A` | 3 of 5 | `P0` carries no procedural step |
| | **Incoherent** | | |
| 3 | Every requirement read `AUTHORED`, over data modules marked unverified, at issue 001, in work 00, while the registers of the subject said `in_work: true`. The chapter and the subject said `baseline` | 5 | A status states its class truthfully |
| 4 | The nine subject nodes stood at addresses that the taxonomy does not define: S-ATLAS has section `003-900` and no subject under it | 9 of 9 | The doctrine of the TPuBS |
| 5 | No subject was linked to the product: no `ssot-ref.yaml` in the tree | 0 | CM-001 §9 |
| 6 | The SNS was marked provisional, pending `_CSDB-CONTROL/SNS-mapping.yaml`; the data modules named the business-rules data module `DMC-EWTW-A-00-00-00-00A-022A-D`; the chapter sent the reader to `node-subject-register.yaml` for the full set. None of the three is in the repository | 3 missing | — |
| 7 | The data module of code `730`, required as *Test and check* and used by the subject as the procedure to disconnect, held the text of the fault isolation module of code `420`, word for word | 1 | — |
| 8 | The subject placed itself under `PMC-EWTW-ECHM_…/000-099_S-ATLAS/`, the layout that the TPuBS README v3.0 superseded, and described the eWTW as an *Electric wing-to-wing configuration* | 1 | TPuBS README v3.0; model README |
| | **Wrong** | | |
| 9 | The chapter bound the energy replenishment of the eWTW to charging alone — *Electrical-charge carrier*, a charging inlet of the megawatt class — and set every other carrier aside as not applicable. Ruling R2 excluded the option that stores its energy in batteries alone. Every option that stands carries conventional fuel, and a propulsion battery is in option C only | The whole tree | Ruling R2 of `KNOT-EWTW-NRG-001`, 2026-11-14 |

The tree is older than the ruling. It described the eWTW that the ruling excluded.

## What is withdrawn

- the tree `003-900_Energy-Replenishment-Ground-Infrastructure/` of the information architecture, whole: 37 files;
- the five rows that were left in `DMRL-EWTW.yaml`, `DMRL-EWTW.csv`, `DMRL-EWTW.md` and `DML-EWTW.xml`. The four registers now hold no row: no node of the information architecture holds a requirement.

## What is kept, and why

| Kept | Why |
|---|---|
| `PMC-EWTW-ECHM`, the publication module of the energy-carrier handling manual, with its impact analysis | A skeleton and a plan: it lists the taxonomy nodes in the scope of the manual and binds no carrier. Its entry for `003-900` now says that the folder is withdrawn |
| The other folders of the information architecture: `010-900`, `011-900`, `012-900`, `020-029`, `020-900`, `070-079`, and the bands `EPTA` and `AMTA` | Each holds a `.gitkeep` and nothing else |
| Section `003-900` of the taxonomy | It names the ground infrastructure of energy replenishment without naming a carrier |

## What the tree held that is written nowhere else

The projection of section `003-900` into nine subjects. The taxonomy defines none of them. The function of each is carrier-neutral; the title is how the tree bound it to charging.

| Subject | Function, carrier-neutral | As the tree bound it |
|---|---|---|
| `003-900-010` | Replenishment connection interface | Ground charging connection interface |
| `003-900-020` | Replenishment energy source | Ground charging source and supply |
| `003-900-030` | Replenishment control and sequencing | Charging process control and sequencing |
| `003-900-040` | Replenishment safety and isolation | Charging safety, isolation, grounding and bonding |
| `003-900-050` | Replenishment communication | Charging communication protocol |
| `003-900-060` | Replenishment thermal conditioning | Battery thermal pre-conditioning during charging |
| `003-900-070` | Replenishment metering | Charge metering and energy-transfer verification |
| `003-900-080` | Infrastructure compatibility | Charging-infrastructure compatibility and interface standards |
| `003-900-090` | Abnormal replenishment and disconnect | Abnormal charging and emergency disconnect |

The tree mapped them to three entries of the manual: energy-carrier replenishment (`010`, `020`, `030`, `050`, `060`, `070`), hazards, placards and isolation (`040`, `090`), and ground-infrastructure interface (`010`, `020`, `080`).

## For the author

Not changed here.

1. **The replenishment of the eWTW is first a fuelling.** A projection of `003-900` for the options that stand names the fuel, and charging for option C if its battery is charged on the ground. It can be planned at class `P0` once the taxonomy or the product gives the subjects.
2. **One folder of the information architecture carries an old name.** It is `070-079_Eco-Tech-and-Hybrid-Electric-Propulsion`; the taxonomy names the range `070-079_Electric-and-Hybrid-Electric-Propulsion`. The impact analysis of `PMC-EWTW-ECHM` points to the name of the taxonomy, and that path resolves to nothing.

## How to restore

The tree as it was, defects included:

```bash
A="01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-11_TPuBS_Technical-Publications-Breakdown-Structure"
git checkout 53848df1 -- "$A/01_INFORMATION-ARCHITECTURE/S-ATLAS_000-099/003-900_Energy-Replenishment-Ground-Infrastructure"
```

## How to verify

From the repository root, with `A` as above:

```bash
git ls-tree -r --name-only 53848df1 -- "$A/01_INFORMATION-ARCHITECTURE/S-ATLAS_000-099/003-900_Energy-Replenishment-Ground-Infrastructure" | wc -l   # 37
git grep -h 'status: "AUTHORED"' 53848df1 -- "$A/01_INFORMATION-ARCHITECTURE/S-ATLAS_000-099/003-900_Energy-Replenishment-Ground-Infrastructure" | wc -l   # 5 — finding 3
find "$A/01_INFORMATION-ARCHITECTURE" -name 'DMRL-*.yaml' | wc -l                                  # 0 after the withdrawal
git grep -n -E 'ICN-EWTW-003|DMC-EWTW-A-03|DMREQ-003' -- . ':!*withdrawal_2026-11-20.md'           # nothing
```
