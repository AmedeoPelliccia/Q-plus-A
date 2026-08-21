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
**part-number tree**. This is the handshake between the S-ATLAS functional
taxonomy (above) and the as-designed product configuration (below).

## 1. Assembly station

A PBS subject node is the **assembly station**: the single point where identity
switches from *taxonomy code* to *part number*. The station holds exactly one
**top assembly** plus a `station.yaml` recording the handshake
(`realizes: <taxonomy-id>` ↔ `top_assembly: <PN>`). Above the station: S-ATLAS
codes. Below: part numbers. Per Amendment A1, every record carrying `realizes`
also carries a `realizesNote` stating identity vs reference: `localCode` feeds
CSN and the PN tree; `realizes` follows taxonomy evolution. Per Amendment A2,
the station is the **Taxonomy–Product Identity Boundary (TPIB)**: the only
point where the two identity spaces touch.

## 2. Part-number grammar

```text
EWTW-<CSN>-<VAR>[-<VAR>…]
```

- `EWTW` — model identity code (MIC); changes per MODEL.
- `CSN` — 6-digit compact system number = ATA-equivalent of the station's
  S-ATLAS code (`053-010-010` → `530101`). This is the conserved **root**.
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

---

## Amendment A2 — the Taxonomy–Product Identity Boundary (TPIB)

**Status:** doctrinal clause of the convention (extends §1) · merge
constitutes ratification.

### A2.1 — Definition

> **Taxonomy–Product Identity Boundary (TPIB).** A normative architectural
> boundary, located at the PBS Subject Node (the assembly station), at which
> the governing identity regime transitions from taxonomic identification to
> configuration-controlled product identification.

Invariants:

```text
for every node above the station:   Identity = Taxonomic        (S-ATLAS address space)
for every node below the station:   Identity = Product          (PN · Revision · Effectivity)
at the station:                     Identity = Binding(Taxonomy, Configuration)
```

The binding is recorded in `station.yaml` (`realizes` ↔ `top_assembly`) and is
the **only** point where the two identity spaces touch.

### A2.2 — Decoupling theorems

```text
PN change                does NOT imply   taxonomy change
Taxonomic decomposition  does NOT imply   PN decomposition
```

Two identity spaces, one formally defined interface. Each side evolves under
its own governance: the taxonomy by ruling and register; the product tree by
configuration management.

### A2.3 — Maintenance obligation (what makes the boundary normative)

The binding is a **maintained joint**, not a one-time act: `realizes` must
resolve to an existing node of the current taxonomy (A1.6,
machine-verifiable), and a self-referential binding is non-conforming. The
taxonomic side of the binding is versioned — `localCode` is the identity
frozen at binding time; `realizes` is the reference that tracks taxonomy
evolution. A boundary whose currency cannot be checked by machine is
documentation; this one is doctrine.

### A2.4 — The CSN as crossing trace

The CSN is the imprint of the taxonomic identity carried into product space at
the moment of crossing (`053-000-030 → 530003`): human-readable,
AMM-SNS-aligned (1:1 by number, ratified), and immune to later taxonomy
evolution (A1.2). It is the fossil record of the handover.

### A2.5 — Prior-art positioning (calibrated claim)

Existing standards distinguish structural, functional, occurrence and part
identities, and some explicitly model the realization of breakdown elements by
parts: **S3000L** (hardware element as usage-in-context, realized by one or
more parts — the closest precedent — while declining to mandate where the
boundary sits), **IEC 81346 / IEC 62027** (reference designation of the
occurrence ≠ part identity, as coexisting schemes), **the FIN/PN practice**
(functional position → installed part, a concrete implementation without a
general theory), **STEP AP239/AP242** (the information-model building blocks).
None establishes a unique normative boundary at which the governing identity
regime transitions from taxonomy-based identification to part-number-based
product identity. **The PBS Subject Node is proposed as that boundary.** No
broader novelty is claimed.
