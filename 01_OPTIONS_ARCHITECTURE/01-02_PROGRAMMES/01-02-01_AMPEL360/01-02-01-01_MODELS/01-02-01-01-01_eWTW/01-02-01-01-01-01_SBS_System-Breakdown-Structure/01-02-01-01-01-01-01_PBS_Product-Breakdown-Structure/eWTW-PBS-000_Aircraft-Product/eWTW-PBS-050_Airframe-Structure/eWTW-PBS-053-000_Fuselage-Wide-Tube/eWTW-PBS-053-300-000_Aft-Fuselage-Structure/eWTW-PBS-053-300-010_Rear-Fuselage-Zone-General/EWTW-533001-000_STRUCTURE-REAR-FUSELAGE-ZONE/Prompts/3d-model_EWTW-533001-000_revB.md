---
title: "3D Model Request — EWTW-533001-000 · STRUCTURE, REAR FUSELAGE ZONE"
model: "AMPEL360 eWTW — Electric Wide Tube and Wing"
product-identity: "EWTW-533001-000"
nomenclature: "STRUCTURE-REAR-FUSELAGE-ZONE"
revision: "B"
maturity: "CONCEPT"
governing-convention: "AMPEL360-PBS-PN-CM-001 (Issue 2)"
convention-ref: "<relative-path-to>/AMPEL360-PBS-PN-CM-001"
prompt-role: "Generative CAD input"
usage: "Feed verbatim to a CAD-modeler agent; generated artifacts land according to §0."
---

# 3D Model Request

## EWTW-533001-000 — STRUCTURE, REAR FUSELAGE ZONE

**Programme:** AMPEL360 eWTW  
**Aircraft concept:** Electric Wide Tube and Wing  
**Revision:** B  
**Maturity:** 
---

## Role and Scope

**Role:** Mechanical / aerostructures CAD modeler.

**Maturity:** `CONCEPT`.

All dimensions in this brief are declared **envelope assumptions** as defined in §7.  
Model them parametrically and exactly where this brief defines them.

### In scope

The model represents the:

- aft-to-tailcone join package;
- indexing provisions;
- systems-run structural supports;
- outflow-valve structural surround;
- NDT access provisions.

### Out of scope

Do **not** model:

- fuselage frames;
- stringers;
- skins;
- rear pressure bulkhead;
- the outflow valve itself;
- systems runs.

### Governing convention

Apply:

`AMPEL360-PBS-PN-CM-001 (Issue 2)`

Apply its operative rules, including:

- body names = PN;
- set nodes = sub-assemblies;
- rollups count leaves;
- no compliance self-claims;
- one provenance line.

Do **not** restate the governing convention in the response.

---

# 0 · Delivery Contract

Read this section first.

You cannot attach binary files in this channel.

Deliver instead:

1. **One self-contained parametric generator script**

   Filename must be exactly:

   `ewtw_533001_concept.py`

   The filename is part of provenance truth. Renaming or paraphrasing it is non-conforming.

   Preferred toolchain:

   - Python ≥ 3.8
   - CadQuery ≥ 2.1

   A different toolchain is permitted only if justified in one line.

2. **Running the script shall write the following files into `--out DIR`:**

   ### Neutral CAD

   `EWTW-533001-000_concept.step`

   Requirements:

   - STEP AP242 requested;
   - AP214 fallback permitted;
   - fallback must surface as `WARN`;
   - fallback must never be silent;
   - fallback alone must not generate `FAIL`;
   - units: mm;
   - assembly tree mirrors the PN hierarchy;
   - ghost envelope excluded.

   ### Lightweight Preview

   `EWTW-533001-000_concept.glb`

   Requirements:

   - glTF binary;
   - colour-coded;
   - ghost context envelope included;
   - ghost colour: white;
   - ghost opacity: 12%.

   ### Verification Evidence

   `EWTW-533001-000_concept_verification.txt`

   Content shall follow §6.

3. **Exit status**

   The script shall exit non-zero if any acceptance criterion produces `FAIL`.

4. **Response contract**

   The response shall contain:

   - the complete script in one code block;
   - run instructions;
   - an abridged expected verification report;
   - a **RESIDUAL interpretation register**.

   The residual interpretation register shall enumerate every decision the modeler had to make that this brief did not resolve.

   Keep explanatory prose minimal.  
   The generated artifacts carry the answer.

---

# 1 · Coordinate Frame, Units and Envelope

## Coordinate system

- Units: **mm**
- `X`: aft positive
- `Y`: aircraft left positive
- `Z`: up positive
- Origin: production join plane `JP`, on aircraft centreline

## Ghost context envelope

The ghost envelope exists for **preview context only**.

It shall never:

- appear in STEP;
- contribute to product counts;
- contribute to interference checks;
- become a PBS product identity.

Geometry:

- right-circular conical frustum;
- diameter `3000 mm` at `X = −4500`;
- diameter `2200 mm` at `JP`, `X = 0`;
- wall thickness `5 mm`;
- no upsweep.

---

# 2 · Fidelity Ladder

For this task, `CONCEPT` maturity means:

## Model exactly

- topology defined in §4;
- angular schedules;
- positions;
- hole patterns;
- pin-tip chamfer `2 × 45°`;
- plug hex socket;
- flush seating.

## Idealize

- threads → smooth bores;
- press fits → nominal diameters.

## Omit

- fastener holes in the ring band;
- fastener holes in the land;
- fastener holes in the flanges;
- joggles;
- unspecified fillets.

The ring forward flange may geometrically embed up to approximately `3 mm` into the ghost context envelope.  
Do not correct this with an invented joggle.

---

# 3 · Binding Interpretations

The following clauses are **specification**, not defaults.

## D-1 · Ring Axial Section

`JP = X = 0`

```text
      x=-75      x=-15    x=+15      x=+75
       ├──── 60 ────┼── 30 ──┼──── 60 ────┤
       │ fwd flange │ land    │ aft flange │
       │            total axial = 150 mm   │
       │
       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
       continuous band · t = 5 mm · OD = 2200 mm
                         │ web │
                         │     │ radial height = 120 mm
                         ▼
                       ID = 1960 mm
```

Requirements:

- ring OD = `2200 mm`;
- ring OD coincides with fuselage OML at JP;
- continuous band thickness = `5 mm`;
- continuous band axial length = `150 mm`;
- forward flange = `60 mm`;
- central land = `30 mm`;
- aft flange = `60 mm`;
- radial web height = `120 mm`;
- web exists only over the central land.

## D-2 · Indexing Bosses

`-020` bosses are modeled as **discrete bodies** faying onto the aft-flange face at flange mid-radius.

This follows the one-body-per-PN rule.

Production manufacture may machine them integrally, but that condition shall **not** be modeled here.

## D-3 · Indexing Pins

Each indexing pin shall have:

- total length = `60 mm`;
- boss engagement = `25 mm`;
- aft protrusion = `35 mm`.

The receiving tailcone half is outside this model.

## D-4 · NDT Plug Seats

`-050` seats are located at:

`15° + 30° × k`

for `k = 0…11`.

This places 4 of the 12 seats exactly on splice-segment butt joints.

This is intentional.

Each adjacent splice-ring segment shall contain its corresponding half-seat.  
Cut both segments where applicable.

## D-5 · Surround Frame

`-042 FRAME-SURROUND-OUTFLOW-VALVE`

Section:

- `40 mm` in-plane;
- `30 mm` radial standoff.

## D-6 · Doubler Geometry

`-041 DOUBLER-OUTFLOW-VALVE-CUTOUT`

The doubler shall be generated from the **exact conical development** of the shell.

It shall not be modeled as a planar plate merely positioned tangent to the fuselage.

Outer corner radius:

`R60`

## D-7 · Rivet Pattern

Requirements:

- diameter = `6 mm`;
- one row;
- nominal spacing ≈ `30 mm`;
- spacing distributed evenly around the contour;
- contour offset = `60 mm` from cutout contour.

The row shall clear:

- the frame footprint;
- the doubler edge.

## D-8 · Bracket / Valve-Surround Conflict

If a bracket in the RH systems-run row conflicts geometrically with the outflow-valve surround:

- displace that bracket circumferentially;
- use only the displacement required to obtain clearance;
- preserve the total quantity of `12`;
- preserve two bracket rows;
- record the displacement in the verification report.

## D-9 · Butt Straps

Butt straps currently have no controlled PN.

Instance names shall therefore be:

`BUTT-STRAP-SEGMENT-JOIN#NN`

Geometry:

- quantity = `4`;
- axial width = `30 mm`;
- thickness = `3 mm`;
- circumferential arc width = `100 mm`;
- location = internal face.

Angular locations:

- `45°`;
- `135°`;
- `225°`;
- `315°`.

## D-10 · Multi-Instance Naming

Multi-instance bodies shall use:

`PN#NN`

Example:

`EWTW-533001-051#07`

The `#NN` instance suffix is **not part of the Part Number**.

Single-instance bodies shall use the bare PN.

---

# 4 · Product Structure and Geometry

Compact notation:

`-0xx` = `EWTW-533001-0xx`

| PN | Nomenclature | Qty | Geometry | Placement |
|---|---|---:|---|---|
| `-010` | SPLICE-RING-AFT-TO-TAILCONE-JOIN | set | Z-section per D-1 | centred on JP; coaxial |
| `-011` | SPLICE-RING-SEGMENT-UPPER | 1 | 90° arc | −45°…+45° from Z+ |
| `-012` | SPLICE-RING-SEGMENT-LOWER | 1 | 90° arc | 135°…225° |
| `-013` | SPLICE-RING-SEGMENT-SIDE-LH | 1 | 90° arc | 45°…135° |
| `-014` | SPLICE-RING-SEGMENT-SIDE-RH | 1 | 90° arc | 225°…315° |
| — | BUTT-STRAP-SEGMENT-JOIN | 4 | per D-9 | 45° / 135° / 225° / 315° |
| `-020` | FITTING-JOIN-INDEXING | 8 | Ø40 × 25 boss; Ø16 bore; per D-2 | 22.5° + k·45° |
| `-021` | PIN-INDEXING-JOIN | 8 | Ø16 × 60; tip 2 × 45°; per D-3 | axial; aft |
| `-030` | SUPPORT-SYSTEMS-RUN-SET | set | two rows | ±35° from Z−; inner shell |
| `-031` | BRACKET-SYSTEMS-RUN | 12 | L 120 × 80 × 60; t3; 2 × Ø8 per leg | 6 per row; pitch 700; X −4200…−700 |
| `-040` | SURROUND-OUTFLOW-VALVE | set | cutout provision | centre X = −1200; 30° from Z− toward Y− |
| `-041` | DOUBLER-OUTFLOW-VALVE-CUTOUT | 1 | 640 × 480; t2.5; cutout 480 × 320; R60 | bonded to inner shell |
| `-042` | FRAME-SURROUND-OUTFLOW-VALVE | 1 | per D-5; follows cutout contour | doubler inner face |
| `-050` | PROVISION-NDT-ACCESS-JOIN-SET | set | 12 seats; per D-4 | 15° + 30°·k from Z+ |
| `-051` | PLUG-INSPECTION-JOIN | 12 | Ø40 × 12 flush; hex socket AF6 | flush in aft flange |

---

# 5 · Parametric Definition and Loud Failure

All dimensions and configurable values shall live in a single:

`PARAMS`

dictionary near the top of the generator.

All geometry and mates shall derive from these parameters.

Support command-line overrides using:

```bash
--param KEY=VALUE
```

Coupled parameters shall fail **loudly** through assertions carrying a human-readable message.

Never silently repair an invalid input.

At minimum validate:

### Bracket-row closure

```text
row_span = (n − 1) × pitch
```

### Ring axial geometry

```text
ring_axial_total > 2 × flange_width
```

### Pin / butt-joint separation

```text
minimum angular separation ≥ 1°
```

---

# 6 · Acceptance and Verification

Every check shall print:

```text
expected | actual
```

using one of:

```text
[PASS]
[FAIL]
[WARN]
[INFO]
```

The verification report shall terminate with a summary line.

The process shall exit with code `1` if and only if one or more checks produce `FAIL`.

## A · Part Counts

Expected:

```text
-011 × 1
-012 × 1
-013 × 1
-014 × 1
butt straps × 4
-020 × 8
-021 × 8
-031 × 12
-041 × 1
-042 × 1
-051 × 12
```

Total leaf bodies:

`50`

No undeclared controlled PN shall exist.

## B · Assembly Tree

Root:

`EWTW-533001-000`

Required sub-assemblies:

```text
EWTW-533001-010
EWTW-533001-020
EWTW-533001-030
EWTW-533001-040
EWTW-533001-050
```

## C · Instance Naming

All instance names shall be unique.

## D · Bracket Pitch Closure

Expected error:

`0.0 mm`

## E · Pin-to-Butt Separation

Minimum permitted separation:

`≥ 1°`

## F · Interference

Expected:

`0`

assembly-body pairs having common volume:

`> 1 mm³`

Exclusions:

- ghost context;
- intentional faying contact.

## G · STEP Verification

Verify that the STEP file:

- exists;
- is non-empty;
- contains every controlled PN string;
- contains no ghost-context node.

## H · GLB Verification

Verify:

- GLB magic = `glTF`;
- ghost context node exists.

## I · STEP Schema

Expected:

`AP242`

If unavailable and writer falls back to another schema:

`WARN`

not:

`FAIL`

---

# 7 · Configuration Flexibility

Every numerical dimension in this brief is a **CONCEPT envelope assumption**.

These dimensions are expected to be superseded by ratified AMPEL360 eWTW structural data.

The following topology, however, represents current design intent and shall survive parameter changes:

```text
4-segment splice ring
8 indexing pins
12 systems-run brackets
2 bracket rows
1 lower-RH outflow-valve structural cutout
12 NDT plugs
```

Overriding a topology count through `--param` is permitted.

If an override changes a declared topology quantity, the verification report shall produce `FAIL` against the declared topology.

That is intentional behaviour.

---

# 8 · Hygiene and Provenance

Do not include:

- engraved text;
- manufacturer names;
- manufacturer logos;
- references to existing aircraft types.

Do not make compliance self-claims in comments.

Conformity shall be demonstrated through §6 verification.

Generated artifacts shall carry one provenance statement containing:

```text
date · ewtw_533001_concept.py · version
```

## Preview Colours

Preview colours are visualization metadata only.

| Product family | Colour |
|---|---|
| splice ring | bronze |
| pins / plugs | steel-grey |
| systems-run brackets | amber |
| doubler / surround frame | teal |
| ghost context | white · 12% opacity |

---

# Residual Interpretation Register

The responding modeler shall append a numbered register containing every ambiguity or design decision that could not be resolved directly from this brief.

Format:

```text
R-1 · <issue>
Decision: <interpretation made>
Reason: <why the brief did not determine it>
Impact: <geometry / topology / export / verification>
```

A residual interpretation shall **not** silently become specification.

If subsequently ratified, promote it into a `D-n` clause in the next revision of this prompt.

---

# Change Record

| Rev | Change |
|---|---|
| A | Original verbal brief. Delivery medium, acceptance criteria and 14 interpretation points remained open and were surfaced post-hoc as responder register I-1…I-14. |
| B | Ratifies I-1…I-14 as binding interpretations consolidated into D-1…D-10 and §2 fidelity rules; adds §0 delivery contract, §5 loud-failure requirements and §6 acceptance values; references CM-001 rather than duplicating its contents. |
