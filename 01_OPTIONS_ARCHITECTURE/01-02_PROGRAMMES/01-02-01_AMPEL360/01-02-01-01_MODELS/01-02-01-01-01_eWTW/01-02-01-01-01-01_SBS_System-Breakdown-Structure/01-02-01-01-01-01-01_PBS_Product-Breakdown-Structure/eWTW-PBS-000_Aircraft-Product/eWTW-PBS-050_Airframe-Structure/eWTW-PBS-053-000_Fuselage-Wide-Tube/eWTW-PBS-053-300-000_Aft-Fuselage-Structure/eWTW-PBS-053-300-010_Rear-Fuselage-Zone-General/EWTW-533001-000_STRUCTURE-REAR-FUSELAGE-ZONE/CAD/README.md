---
status: draft
standard_scope: governance
---

# EWTW-533001-000 — CAD

**Part:** `EWTW-533001-000` STRUCTURE-REAR-FUSELAGE-ZONE · concept
**Generator:** [`source/EWTW-533001-000_concept.py`](source/EWTW-533001-000_concept.py), `v0.2.2-concept`, built on CadQuery

The geometry of this part is generated, not drawn. One Python script builds the assembly and writes four files into the part folder. The four belong to one run: the run record carries the size and the SHA-256 of the other three.

## What lives where

Paths are given from the part folder, `EWTW-533001-000_STRUCTURE-REAR-FUSELAGE-ZONE/`.

| Path | Content | Written by |
|---|---|---|
| `CAD/source/EWTW-533001-000_concept.py` | The generator | Author |
| `CAD/exchange/EWTW-533001-000_concept.step` | STEP AP242 in millimetres; bodies named by part number | Generator |
| `CAD/Preview/EWTW-533001-000_concept.glb` | glTF preview, with the context envelope | Generator |
| `evidence/EWTW-533001-000_concept_verification.txt` | Verification report of the run | Generator |
| `Prompts/Run-record.yaml` | Run record: generator version, environment, size and SHA-256 of each output | Generator |
| `evidence/EWTW-533001-000_concept_freecad-roundtrip.txt` | Round trip of the STEP file through FreeCAD | `tools/freecad_roundtrip.py` |
| `MEDIA/` | Views of the model opened in FreeCAD | Author |

`evidence/`, `Prompts/` and `MEDIA/` are beside `CAD/`, not inside it.

The generator spells two of these in lower case: `CAD/preview/` and `prompts/run-record.yaml`. The repository has `CAD/Preview/` and `Prompts/Run-record.yaml`. Which spelling is the rule is open, with the rest of the CAD convention, in `KNOT-EWTW-CAD-001`.

## Running the generator

The script needs Python with CadQuery. By default it writes into the part folder, and it stops if its own folder is not `CAD/source/`.

The paths of this repository are longer than Windows accepts by default. On Windows the generator is run in a short copy of the part folder, from any working folder:

```
mkdir EWTW-533001-000\CAD\source EWTW-533001-000\CAD\Preview EWTW-533001-000\Prompts
copy EWTW-533001-000_concept.py EWTW-533001-000\CAD\source\
cd EWTW-533001-000\CAD\source
python EWTW-533001-000_concept.py
```

The run prints the verification report. Its four outputs are then committed together, each at its path in the table, unchanged. A file from another run, or one saved again by an editor, no longer matches the hash in the run record.

`--layout flat --out <folder>` writes the four files into one folder instead. `--help` lists what a run can declare: the prompt file and its revision, and the model named as author.

## Checking a committed set

- The sizes and hashes in `Prompts/Run-record.yaml` equal those of the committed files.
- `tools/freecad_roundtrip.py` on the STEP file reports 50 bodies under their part numbers and no failure.
