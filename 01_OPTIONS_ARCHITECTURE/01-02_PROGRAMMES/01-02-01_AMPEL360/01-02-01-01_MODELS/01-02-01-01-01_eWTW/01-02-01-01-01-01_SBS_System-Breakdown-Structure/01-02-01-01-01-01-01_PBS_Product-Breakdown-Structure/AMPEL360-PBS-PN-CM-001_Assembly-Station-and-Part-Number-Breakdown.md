# AMPEL360-PBS-PN-CM-001 — Assembly Station & Part-Number Breakdown Convention

**Issue 2** · Owner: Q-STRUCTURES · Authority: AM.PEL · Status: **PROPOSED — merge constitutes ratification.**
Supersedes Issue 1 and absorbs Amendments **A1** (clauses .1–.7, .9) and **A2** (TPIB). Clause A1.8 (handedness truth) is ratified herein, the authority having adopted it in the governing exemplar.

---

## 1. Purpose and scope

This convention governs the transition from architecture taxonomy to configuration-controlled product definition in the AMPEL360 PBS: the assembly station, the part-number grammar, node anatomy, interface identifiers, status truth and the executable verification that keeps all of it honest. It applies to every PBS branch of the eWTW model and, by adoption, to sibling models.

## 2. The assembly station and the identity boundary (TPIB)

> **A PBS subject node is the assembly station: the single point where identity switches from taxonomy-linked PBS code to part number.**

The station is the **Taxonomy–Product Identity Boundary**:

```text
above the station:   Identity = PBS-local code (taxonomy linked by mapping)
below the station:   Identity = Product (PN · Revision · Effectivity)
at the station:      Identity = Binding(Taxonomy, Configuration)
```

**Decoupling theorems.** A part-number change never implies a taxonomy change; taxonomic decomposition never implies part-number decomposition. Two identity spaces, one formally defined interface, each evolving under its own governance.

**Maintenance obligation.** The binding is a maintained joint, not a one-time act: `realizes:` must resolve to an existing node of the current taxonomy, is re-verified by machine (§10), and a self-referential binding is non-conforming. *A boundary whose currency cannot be checked by machine is documentation; this one is doctrine.*

A station holds **exactly one** top assembly and one `station.yaml` recording the handshake `realizes ↔ top_assembly`. Above it, no node sees the physical assembly; below it, everything is physical.

## 3. Identity and mapping

**3.1 — Sovereign local codes.** PBS codes are programme-local, conserved identifiers — never taxonomy addresses. No PBS artifact may claim its codes *are* S-ATLAS: the prose formula is "Realizes S-ATLAS `<address>`", never "is S-ATLAS `<code>`". The taxonomy link is carried only by:

```yaml
taxonomyRef:                     # node frontmatter / pbs-node.yaml
  chapter: "053"
  section: "053-100"             # current taxonomy address
  localCode: "053-010"           # conserved PBS-local code
  note: "PBS-local addressing per CM-001; taxonomy linked by mapping, never mirrored"
```

and, at station grain, by `realizes:` with its explanatory `realizesNote`.

**3.2 — CSN derivation.** The compact system number derives from the **PBS-local code** and is immune to taxonomy evolution:

```text
053-010-010  →  CSN 530101  →  root EWTW-530101
```

**3.3 — The crossing trace.** The CSN is the imprint of the local identity carried into product space at the moment of crossing — human-readable, AMM-SNS-aligned (1:1 by number), the fossil record of the handover.

## 4. Part-number grammar

```text
EWTW-<CSN>-<VAR>[-<VAR>...]
```

`EWTW` model identity code (MIC) · `<CSN>` per §3.2 · `<VAR>` ×10 find group: `000` is the assembly itself (and "general" at every level); `010`, `020` … components; nest deeper by appending another ×10 group; `+1..+9` within a group are variants or constituents.

**4.1 — Handedness truth (was A1.8).** Variant names describe **position or function as built**, never an inherited symmetry: odd/even encodes LH/RH **only for true mirrored pairs**; a same-side stack is UPPER/LOWER; other dispositions name what they are (FWD/AFT, INBD/OUTBD). Renaming a variant's nomenclature never changes its PN code.

**4.2 — Quantity discipline.** Find groups with enumerated children are **sets**: the group line reads `(set of N)`; unit quantities live on the leaves. Quantity rollups count leaves only — a group must never double-count its children. Leaf-only groups may carry `×N EA` directly.

**4.3 — Worked exemplar** (station `eWTW-PBS-053-010-010`, status realized):

```text
EWTW-530101-000  STRUCTURE, RADOME AND NOSE CONE ATTACH      (×1 EA, make)
  EWTW-530101-010  STRUCTURE, RADOME ATTACH                  (×1 EA, make)
    EWTW-530101-011  FRAME, RADOME ATTACH RING               (×1 EA, make)
    EWTW-530101-012  FITTING, RADOME ATTACH BACKUP           (×8 EA, make)
  EWTW-530101-020  FITTING, RADOME HINGE                     (set of 2, buy)
    EWTW-530101-021  FITTING, RADOME HINGE UPPER             (×1 EA, buy)
    EWTW-530101-022  FITTING, RADOME HINGE LOWER             (×1 EA, buy)
  EWTW-530101-030  FITTING, RADOME LATCH                     (×2 EA, buy)
  EWTW-530101-040  STRIP, LIGHTNING DIVERTER                 (×6 EA, buy)
  EWTW-530101-050  SEAL, RADOME PERIMETER                    (×1 EA, buy)
  EWTW-530101-060  BRACKET, WEATHER RADAR ANTENNA MOUNT      (×1 EA, make)
```

The root `EWTW-530101` is conserved down the entire tree; only the notation changed at the boundary.

## 5. Node anatomy and provenance

**Folder identity is SSOT**; YAML mirrors it. Every part node carries `part.yaml`; every station carries `station.yaml` on the **single station schema**:

```yaml
station:
  id: <PBS node id>              # never an invented serial
  localCode: "..."               # conserved
  realizes: "..."                # current taxonomy address, resolving, never self-referential
  realizesNote: "..."            # the identity-vs-reference explanation, verbatim clause
  top_assembly: EWTW-<CSN>-000
  root: EWTW-<CSN>
  mic: EWTW
  csn: "<CSN>"
  type: assembly-station
  convention: "AMPEL360-PBS-PN-CM-001 (Issue 2)"
  parallels: AMPEL360-AMM-INFOCODE-CM-001
  owner: <division>
  status: PLANNED | realized
  interfaces: [ ... ]            # §7 schema
  parts: <leaf+group count on disk>
```

**Provenance truth.** Generated files carry one provenance line — date · generator filename verbatim · version — and nothing else. Compliance self-claims are prohibited: conformity is demonstrated by §10, never asserted in comments. Paraphrasing a generator filename destroys provenance and is non-conforming.

## 6. Identity versus position

The folder P/N is **positional, as-designed** — where the item sits, root-conserving. A physical part reused elsewhere keeps **one** identity via `catalog_pn` and is referenced where reused; no second folder. For make-once parts the two coincide and `catalog_pn` is empty.

## 7. Interfaces and ICD grammar

The station is where cross-taxonomy interfaces (system ↔ structure) are declared — it is the first node that sees the physical assembly. Every `interfaces[]` entry declares its address space and its carrying parts:

```yaml
- icd: ICD-EWTW-530101-034
  space: taxonomy | pbs-local
  counterpart: "034"                 # chapter, or PBS station id
  counterpartCsn: "530103"           # when pbs-local
  taxonomyRef: "053-800"             # when the counterpart realizes a taxonomy element
  item: "..."
  carriedBy: [EWTW-530101-060]       # part numbers physically realizing the interface
```

**ICD identifier grammar:** `ICD-<MIC>-<CSN>-<counterpart>` — a **6-digit** counterpart is a PBS station (by CSN); a **3-digit** counterpart is a taxonomy chapter. *The segment length is the space discriminator*: the identifier is machine-parseable with no further convention. Concatenated 9-digit codes and undiscriminated mixed spaces are non-conforming.

## 8. Status truth

`status: realized` only when **every** breakdown row exists on disk; otherwise `partially-realized` with a per-row Status column derived from `pbs-item-register.yaml` (the register is SSOT; tables are views). Hyperlinks appear only on REALIZED rows — links never 404.

## 9. Downstream and publications

The SNS of maintenance publications aligns 1:1 by number with the PBS-local code (`530101 → 53-10-01` class). Effectivity meets publications through `infoCodeVariant` per `AMPEL360-AMM-INFOCODE-CM-001`. Publications **describe, support or evidence** the controlled product — they never redefine it; the PUB side references SSOT one-way via `ssot-ref.yaml`.

## 10. Executable verification

Run at repo root; every check must print its expected value. Paste outputs in any ratifying PR.

```bash
PBS="<...>/01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure"
TAX="<...>/01-03-01_Q+ATLANTIDE/000-099_S-ATLAS"

# realizes resolves, and is never self-referential
for f in $(find "$PBS" -name station.yaml); do
  r=$(grep -E '^\s*realizes:' "$f" | grep -oE '[0-9]{3}-[0-9]{3}-[0-9]{3}')
  find "$TAX" -type d -name "${r}_*" | grep -q . || echo "DANGLING $r in $f"
  grep -oE 'localCode: "'$r'"' "$f" | grep -q . && echo "SELF-REFERENTIAL in $f"
done; echo realizes-scan-done

# ICD grammar: MIC + 6-digit CSN + (3|6)-digit counterpart
grep -rhoE 'ICD-[A-Z0-9]+-[0-9]{6}-[0-9]{3}([0-9]{3})?' "$PBS" | sort -u | head
grep -rhoE 'ICD-[0-9-]{15,}' "$PBS" | grep -vE 'ICD-[A-Z]' | wc -l        # expect 0 (legacy concatenations)

# provenance and claims
grep -rn "No-AAA compliant" "$PBS" | wc -l                                 # expect 0
grep -rn "compliant" --include="*.yaml" "$PBS" | wc -l                     # expect 0

# schema singularity and status truth
grep -rl '^assemblyStation:' "$PBS" | wc -l                                # expect 0
grep -rnE '\| PLANNED \|.*\]\(' --include="README.md" "$PBS" | wc -l       # expect 0
```

## Annex A — Prior art and calibrated claim

Existing standards distinguish structural, functional, occurrence and part identities, and some model the realization of breakdown elements by parts: S3000L (hardware element as usage-in-context, realized by parts — the closest precedent — while declining to fix where the boundary sits), IEC 81346 / IEC 62027 (occurrence ≠ part identity, coexisting schemes), the FIN/PN practice (a concrete implementation without a general theory), STEP AP239/AP242 (the information-model building blocks). None establishes a unique normative boundary at which the governing identity regime transitions from taxonomy-based identification to part-number-based product identity. **The PBS Subject Node is proposed as that boundary. No broader novelty is claimed.**

## Change record

| Issue | Content |
|---|---|
| 1 | Original convention: station definition, PN grammar, catalog_pn, interfaces, ×10 depth |
| 2 | Absorbs A1.1–.7 (mapping doctrine, CSN clause, status truth, §10 checks, interface spaces, provenance truth, single station schema), A1.8 ratified (handedness truth), A1.9 (ICD grammar), A2 (TPIB, decoupling theorems, maintenance obligation, crossing trace, prior-art claim); adds quantity discipline §4.2; exemplar re-instanced on the 11-part realized station |
