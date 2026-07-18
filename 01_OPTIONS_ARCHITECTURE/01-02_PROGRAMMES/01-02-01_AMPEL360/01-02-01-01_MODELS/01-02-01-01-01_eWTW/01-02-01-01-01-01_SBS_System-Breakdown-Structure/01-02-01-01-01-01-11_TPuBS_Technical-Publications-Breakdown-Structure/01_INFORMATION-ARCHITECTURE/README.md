---
node: 01_INFORMATION-ARCHITECTURE
model: eWTW
mic: EWTW
side: PUB
csdb: S1000D Issue 4.2
owner: Q-DATAGOV
status: baseline
---

# 01_INFORMATION-ARCHITECTURE — Canonical Information Layer (common DM pool)

The **single canonical instance** of the Q+ATLANTIDE taxonomy for the eWTW
technical information. This layer is the CSDB-side common Data Module pool:
every Data Module is authored **once**, under the S-ATLAS/SNS node where it
semantically belongs, and is then *referenced* — never copied — by the
Publication Modules in `../02_PUBLICATION-MODULES/`.

```text
eWTW product / model
        ↓
S-ATLAS / SNS  (this layer — semantic allocation backbone)
        ↓
information nodes (0CC-SS0-UU0 subject packages)
        ↓
node DMRLs (DMRL-<code>.yaml — declared information requirements)
        ↓
common Data Modules (DM/ folders, one DM per info code / effectivity solution)
        ↓
Publication Modules (02_PUBLICATION-MODULES — purpose-specific projections)
        ↓
AMM, FIM, SDS, IPC, FCOM, …
```

## Bands

| Band | Content |
|---|---|
| `S-ATLAS_000-099/` | Aircraft-level S-ATLAS breakdown (decade bands → chapters → sections → subjects). |
| `EPTA_400-499/` | Energy and Propulsion Technology band. |
| `AMTA_500-599/` | Advanced Materials band (energy storage materials). |

## DMRL per node

Every node carries a `DMRL-<code>.yaml`:

* **subject nodes** (`0CC-SS0-UU0`) declare their own information requirements
  (`nodeType: information-authoring-node`) or none (`nodeType: placeholder-node`);
* **section** (`0CC-SS0`) and **chapter** (`0CC`) nodes carry generated
  roll-ups (`nodeType: information-rollup-node`).

Each requirement declares `infoCode`, `schemaType`, `status` and
`publicationTargets`. Publication membership is **metadata**, never folder
structure:

```text
absence of a publicationTarget  =  the Data Module does not enter that publication
```

One S-ATLAS node → many DM requirements/InfoCodes → many Data Modules → many
Publication Modules. There is deliberately **no** "one node = one manual" and
**no** "one Data Module = one manual" relation.

The consolidated aggregation of all node DMRLs is generated into
`../04_CONSOLIDATED-REGISTERS/`.
