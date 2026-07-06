---
node: 02_PUBLICATION-MODULES
model: eWTW
mic: EWTW
side: PUB
csdb: S1000D Issue 4.2
owner: Q-DATAGOV
status: baseline
---

# 02_PUBLICATION-MODULES — Publication Definition Layer

One folder per **PMC** (Publication Module Code). A PMC folder holds the
**editorial structure of the publication and references to Data Modules** —
never a material copy of the information tree. The canonical content lives in
`../01_INFORMATION-ARCHITECTURE/` (common DM pool); each publication is a
**controlled composition of that pool**.

```text
PM references DMs by DMC; it never holds DM content (linked, not stored).
```

## What a PMC folder contains

* publication identity and configuration (`publication-baseline.yaml`, `pm.xml`);
* editorial structure / PM sequence (`PM-<PMC>-<chapter>_*.yaml`);
* selection rules (`PMC-<code>.yaml` — which G-ATLAS scope and info codes to pull);
* applicability (`applicability.yaml`);
* DM reference index (`dm-reference-index.yaml`);
* release baseline, front matter, delivery configuration.

A PM can be generated automatically from the DMRL rows that satisfy its
selection rules, e.g. for the AMM ATA 021 module:

```text
publicationTargets contains PMC-EWTW-AMM  AND  G-ATLAS chapter = 021
```

## Not every node needs every manual

The DM ↔ publication matrix is many-to-many and lives in DMRL metadata
(`publicationTargets`), not in the filesystem. No per-manual folders exist
under information nodes, and no G-ATLAS copies exist under PMCs.

## G-ATLAS is the allocation backbone, not a mandatory TOC

AMM, SDS, FIM and IPC largely follow the ATA/G-ATLAS breakdown. MPD, MMEL,
SB, CMM and DPP publications follow their own editorial axes (task/interval,
dispatch item, effectivity/modification, component/part number,
asset/lifecycle). The G-ATLAS link is preserved through the DM references:

```text
G-ATLAS = semantic allocation backbone
Publication Module = purpose-specific projection
```
