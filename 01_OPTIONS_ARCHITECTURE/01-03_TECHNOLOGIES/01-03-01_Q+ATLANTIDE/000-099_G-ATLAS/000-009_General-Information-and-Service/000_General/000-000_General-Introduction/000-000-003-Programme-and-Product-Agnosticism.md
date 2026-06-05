---
document_id: G-ATLAS-000-000-003
title: "000-000-003 — Programme and Product Agnosticism"
node: 000-000
item: "003"
ata_ref: 00-00-03
owner: Q-DATAGOV
agnostic: true
status: baseline
---

# 000-000-003 — Programme and Product Agnosticism

> **Node:** `000-000` · **Item:** `003` · **ATA ref:** 00-00-03
> **Owner:** Q-DATAGOV · **Status:** baseline · **Agnostic:** yes

---

## 1. The Neutral-Standard Principle

G-ATLAS is **agnostic by design**. No node, item, or definition in the standard assumes a specific energy carrier, airframe geometry, propulsion architecture, or programme identity. Every slot is defined in terms of **function, limit, zone, or interval** — not in terms of a specific technology realising it.

This principle is constitutional. It is not a preference that a programme may override.

---

## 2. What Agnosticism Means in Practice

### 2.1 Function Slots, Not Technology Slots

A G-ATLAS node defines *what* a function is and *what* must be documented about it. It does not define *how* the function is realised. Examples:

| G-ATLAS slot (agnostic) | eWTW binding | hBWB binding |
|---|---|---|
| `000-900` — Sustainability, lifecycle & DPP framing | Battery-electric DPP; LC-letter lifecycle accounting | Hydrogen DPP; well-to-wake H₂ lifecycle |
| `004-900` — Energy-carrier & storage airworthiness limits | Battery + power-electronics limits (CS-23/25 + SC) | Cryo-tank + fuel-cell stack limits (novel SC) |
| `008-900` — Energy-carrier mass & CG effects | Battery mass distribution; pack layout CG model | LH₂ low-density mass + boil-off CG shift |

### 2.2 Programme Binding via Impact Study

A programme **binds** each G-ATLAS slot to its real technology through an **impact study**. The impact study is stored in the programme's `01-02-XX-04_IMPACT-STUDIES/` folder. It maps:

```text
G-ATLAS node/item  ──(impact study)──►  Programme DMC
                                        Programme-specific engineering value
                                        Applicable certification basis
```

The G-ATLAS SSOT does not change when a binding is made. Only the programme's PUB (CSDB) changes.

### 2.3 Delta Nodes for Novel Functions

Where ATA has no equivalent function slot, G-ATLAS defines an **agnostic delta node** (`00X-900`). These nodes are explicitly labelled `[G]` (green-architecture delta). They are part of the standard; programmes bind them exactly as they bind any other node.

---

## 3. What Breaks Agnosticism

An item is **not agnostic** if it:

- Names a specific energy carrier (battery, hydrogen, …) as an assumption rather than an example.
- Names a specific airframe geometry as a constraint.
- Contains a programme identifier (eWTW, hBWB, …) in the normative body of the item.
- References a specific certification special condition that is not universally applicable.

Agnosticism violations are **defects** in the SSOT and must be raised as change requests under the document-control process (`000-000-007`).

---

## 4. Reference Programme Instantiations

These are listed for illustration only. They are not part of the standard.

| Programme | Energy carrier | Geometry | Example binding |
|---|---|---|---|
| **eWTW** | Battery-electric | Wide tube-and-wing | Battery mass + HV zoning |
| **hBWB** | Hydrogen (cryo LH₂ + fuel cell) | Blended-wing-body | Cryo-tank CG + LH₂ airworthiness limits |
| *(other)* | NH₃, SAF, hybrid, … | any | Per architecture; determined by impact study |

The standard is identical for all three. Only the bindings differ.

---

```yaml
Last.MarkedDown:
  node: 000-000
  item: "003"
  ata_ref: 00-00-03
  file: 000-000-003-Programme-and-Product-Agnosticism.md
  owner: Q-DATAGOV
  status: baseline
  .YieldedAlgorithmicMachineLearning: true
```
