---
convention: AMPEL360-PBS-PN-CM-001
title: Assembly Station & Part-Number Breakdown
parallels: AMPEL360-AMM-INFOCODE-CM-001
model: eWTW (generalizes across MODELS)
side: SSOT
layer: deepest SSOT layer (configuration items)
governance: [DEGF-v1.0, No-AAA, SSOT+PUB]
status: baseline
version: "1.0"
---

# AMPEL360-PBS-PN-CM-001 — Assembly Station & Part-Number Breakdown

Defines how a PBS **subject** node (`0CC-SS0-UU0`) transitions into the physical
**part-number tree**. This is the handshake between the G-ATLAS functional
taxonomy (above) and the as-designed product configuration (below).

## 1. Assembly station

A PBS subject node is the **assembly station**: the single point where identity
switches from *taxonomy code* to *part number*. The station holds exactly one
**top assembly** plus a `station.yaml` recording the handshake
(`realizes: <taxonomy-id>` ↔ `top_assembly: <PN>`). Above the station: G-ATLAS
codes. Below: part numbers.

## 2. Part-number grammar

```text
EWTW-<CSN>-<VAR>[-<VAR>…]
```

- `EWTW` — model identity code (MIC); changes per MODEL.
- `CSN` — 6-digit compact system number = ATA-equivalent of the station's
  G-ATLAS code (`053-010-010` → `530101`). This is the conserved **root**.
- `VAR` — find/variant group, ×10 (`000` = the assembly itself; `010`, `020`…
  its components; nest deeper by appending another ×10 group). The root
  `EWTW-<CSN>` is conserved down the entire tree.
- Handed / config variants — odd/even within a group (`021` LH, `022` RH).

The P/N tree is the ×10 grammar **continued below the station**: the only change
at the boundary is the notation (`053-010-010` → `EWTW-530101-…`).

## 3. Node folder

```text
<PN>_<NOMENCLATURE-SLUG>/
```

- `<PN>` — full part number (root + find chain).
- `<NOMENCLATURE-SLUG>` — controlled **noun-first** item name, uppercase, comma
  removed, spaces → hyphen (`STRUCTURE, RADOME ATTACH` → `STRUCTURE-RADOME-ATTACH`).
- Each node folder holds `part.yaml`. The canonical `STRUCTURE, RADOME ATTACH`
  (with comma) lives in `part.yaml`, not the folder name.

## 4. part.yaml

`pn` · `find` · `nomenclature` (canonical, noun-first) · `parent_pn` · `qty` ·
`uom` · `layer` (STD/◇/STD-G) · `make_or_buy` · `effectivity` · `catalog_pn`
(see §5) · `interfaces[]` · `realizes` (top assembly only — the station id) ·
`status` · `version`.

## 5. Part identity vs position — the one caveat

The folder P/N is **positional / as-designed** (root-conserving: it says *where
the item sits* in this assembly). A physical part **reused elsewhere** must keep
**one** identity: record it in `catalog_pn` (opaque, unique, from the model part
register) and **reference** it where reused — do **not** create a second folder.

> Folder P/N = where it sits. `catalog_pn` = what it is. For make-once parts the
> two coincide and `catalog_pn` is left empty.

## 6. Effectivity ↔ publication

A dash/variant (LH/RH, config, embodied mod) is the **product face** of the same
effectivity carried on the **publication face** by `infoCodeVariant` in
`AMPEL360-AMM-INFOCODE-CM-001`. A mod that forks a part (new dash) and forks a
data-module info-code variant are two records of **one** change. The part
register and the DM register reconcile on the mod id.

## 7. Interfaces

`interfaces[]` lists interfacing nodes — other part numbers **and** adjacent
taxonomy items (e.g. `034` antenna, `053-010-030` forward pressure bulkhead,
`024` bonding) — each with an ICD reference. The station is where cross-taxonomy
interfaces (system ↔ structure) are declared, because it is the first node that
sees the physical assembly.

## 8. Depth

Below the subject the tree nests by appending ×10 find groups until detail-part
level. No fixed depth; `-000` remains "the assembly itself / general" at every
level.

## 9. Governance

SSOT-side; the part tree is the **deepest SSOT layer** (configuration items). The
AMM/SRM (PUB) reference it via `ssot-ref.yaml`. Owner is the station's owner
(structures → Q-STRUCTURES). Inherits DEGF v1.0, No-AAA, SSOT+PUB.

## 10. Reference realization

The station `053-010-010` (Radome & Nose Cone Attach Structure, root
`EWTW-530101`) is realized to full depth by
[`realize_assembly-station_053-010-010.py`](../../../../../../../../../realize_assembly-station_053-010-010.py)
at the repository root.
