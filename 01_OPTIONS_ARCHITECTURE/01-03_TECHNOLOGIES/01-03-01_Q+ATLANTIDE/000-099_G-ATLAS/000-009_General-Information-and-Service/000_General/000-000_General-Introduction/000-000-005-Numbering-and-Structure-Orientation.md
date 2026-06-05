---
document_id: G-ATLAS-000-000-005
title: "000-000-005 — Numbering and Structure Orientation"
node: 000-000
item: "005"
ata_ref: 00-00-05
owner: Q-DATAGOV
agnostic: true
status: baseline
---

# 000-000-005 — Numbering and Structure Orientation

> **Node:** `000-000` · **Item:** `005` · **ATA ref:** 00-00-05
> **Owner:** Q-DATAGOV · **Status:** baseline · **Agnostic:** yes

---

## 1. Four-Tier Hierarchy

G-ATLAS uses a four-tier hierarchy that mirrors ATA 100 / iSpec 2200:

```text
Band  ──►  Master Range  ──►  Chapter (folder)  ──►  Node (code section)  ──►  Item (subject file)
```

Each tier has a defined numbering format and a corresponding physical location in the repository.

---

## 2. Tier Definitions

### Tier 1 — Band

| Attribute | Value |
|---|---|
| Format | `000–099`, `100–199`, … |
| Example | `000-099_G-ATLAS` |
| Physical | Top-level folder under `01-03-01_Q+ATLANTIDE/` |
| ATA mirror | Major subject group |

### Tier 2 — Master Range

| Attribute | Value |
|---|---|
| Format | `00X–00(X+9)_<Title>` |
| Example | `000-009_General-Information-and-Service` |
| Physical | Sub-folder within the band folder |
| ATA mirror | Group of ATA chapters |
| Note | Previously called *code range* — that term is retired |

### Tier 3 — Chapter (physical folder)

| Attribute | Value |
|---|---|
| Format | `00X_<Title>` |
| Example | `000_General` ⇄ ATA 00 |
| Physical | Sub-folder within the master-range folder |
| ATA mirror | ATA chapter (single digit 0–9 within the master range) |

### Tier 4 — Node (Code Section)

| Attribute | Value |
|---|---|
| Format | `00X-Y00_<Title>` |
| Example | `000-000` ⇄ ATA 00-00 |
| Physical | Sub-folder within the chapter folder |
| ATA mirror | ATA chapter-section (`XX-YY0`) |
| Section scaling | ATA section `Y0` → G-ATLAS `Y00` (multiply by 10) |
| `-000` convention | The `00X-000` node is the chapter-general / overview node |
| `-900` convention | Delta node for topics with no ATA equivalent; tagged `[G]` |

### Tier 5 — Item (Subject File)

| Attribute | Value |
|---|---|
| Format | `<node>-<item>-<Title>.md` |
| Example | `000-000-001-Scope-and-Definitions.md` ⇄ ATA 00-00-01 |
| Physical | Markdown file inside the node folder |
| ATA mirror | ATA subject (`XX-YY-ZZ`) |
| Item `000` | Always the overview item for the node |
| Item `001` | Always scope and definitions |

---

## 3. Section Scaling Rule

ATA uses a two-digit section suffix (`Y0`). G-ATLAS uses a three-digit suffix (`Y00`) to allow future expansion of item codes beyond 99 without ambiguity:

| ATA section | G-ATLAS node suffix | Example |
|---|---|---|
| `00-00` | `-000` | `000-000` ⇄ ATA 00-00 |
| `02-10` | `-100` | `002-100` ⇄ ATA 02-10 |
| `05-50` | `-500` | `005-500` ⇄ ATA 05-50 |
| — (delta) | `-900` | `000-900` — no ATA equivalent |

---

## 4. Naming Conventions

| Element | Rule |
|---|---|
| Band folder | `<range>_<Acronym>` | `000-099_G-ATLAS` |
| Master-range folder | `<range>_<Title-words-hyphenated>` | `000-009_General-Information-and-Service` |
| Chapter folder | `<chapter-number>_<Title-words-hyphenated>` | `000_General` |
| Node folder | `<node-id>_<Title-words-hyphenated>` | `000-000_General-Introduction` |
| Item file | `<node>-<item>-<Title-words-hyphenated>.md` | `000-000-001-Scope-and-Definitions.md` |

Title words use **Title-Case-With-Hyphens** (each significant word capitalised; spaces replaced by hyphens).

---

## 5. Worked Example — Full Path

```text
01_OPTIONS_ARCHITECTURE/
└── 01-03_TECHNOLOGIES/
    └── 01-03-01_Q+ATLANTIDE/
        └── 000-099_G-ATLAS/                               ← band
            └── 000-009_General-Information-and-Service/   ← master range
                └── 000_General/                           ← chapter (ATA 00)
                    └── 000-000_General-Introduction/      ← node (ATA 00-00)
                        └── 000-000-005-Numbering-and-Structure-Orientation.md  ← item (ATA 00-00-05)
```

---

```yaml
Last.MarkedDown:
  node: 000-000
  item: "005"
  ata_ref: 00-00-05
  file: 000-000-005-Numbering-and-Structure-Orientation.md
  owner: Q-DATAGOV
  status: baseline
  .YieldedAlgorithmicMachineLearning: true
```
