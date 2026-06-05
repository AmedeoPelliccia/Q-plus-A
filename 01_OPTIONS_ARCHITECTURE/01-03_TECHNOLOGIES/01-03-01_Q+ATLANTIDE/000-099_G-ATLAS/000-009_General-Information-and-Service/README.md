# 000–009 — General Information and Service

**G-ATLAS Master Range Index / Technology Breakdown Tree**

> **Canonical path**
> `01_OPTIONS_ARCHITECTURE/01-03_TECHNOLOGIES/01-03-01_Q+ATLANTIDE/000-099_G-ATLAS/000-009_General-Information-and-Service/`
>
> **Band:** `000–099` — **G-ATLAS** (Green Aircraft Top-Level Architecture Schema)
> **Master Range:** `000–009` — General Information and Service *(first of ten master ranges in the band)*
> **Standards mirror:** ATA 100 / iSpec 2200, chapters **00–09**
> **Status:** programme- and product-**agnostic** standard

> **Terminology note:** at this level `000–009` is a **master range**; its **nodes are the code sections** (`00X-Y00`), not the chapters. The term *code range* is retired here.

---

## 1. Agnosticism Principle *(the governing rule of this standard)*

G-ATLAS names **functions, limits, zones, and intervals** in architecture-neutral terms. It never assumes a specific energy carrier or airframe geometry. A **programme** then **binds** each generic slot to its real technology through an impact study.

```text
G-ATLAS (standard)              Programme (instantiation)
"energy-carrier storage   ─────► eWTW  : traction-battery packs + power electronics
 airworthiness limits"          hBWB  : cryogenic LH₂ tank + fuel-cell stack
                                other : NH₃, SAF, hybrid, … (per architecture)
```

The standard **must fit all of them unchanged**. Where ATA has no equivalent (energy storage, novel geometry, replenishment, DPP), G-ATLAS adds an **agnostic delta node** at `00X-900` — see §6.

**No-AAA Rule applies.** `AAA` is not a valid node, section, item, or designation.

---

## 2. Numbering Rule (ATA / iSpec 2200 mirror)

| Tier | Format | ATA mirror | Example |
|---|---|---|---|
| Master Range | `000–009` | General group | `000-009_General-Information-and-Service` |
| Chapter (implicit, encoded in node prefix) | `00X` | ATA chapter `0X` | `002` ⇄ ATA 02 |
| **Node = Code Section** | `00X-Y00` | ATA chapter-section `0X-Y0` | `002-100` ⇄ **ATA 02-10** |
| Item / Subject (markdown file) | `<node>-<item>-<Title>.md` | ATA subject `0X-Y0-ZZ` | `002-100-001-…md` ⇄ ATA 02-10-01 |

**Section scaling:** ATA section `Y0` → 3-digit code `Y00` (`×10`).
`02-00 → 002-000` · `02-10 → 002-100` · `02-20 → 002-200` · … · `05-50 → 005-500` · green-delta → `00X-900`.

A node's **`-000`** code section is its chapter-general / overview node (ATA `0X-00`).

---

## 3. Master Range → Node Tree

```text
000-009_General-Information-and-Service/                              (MASTER RANGE)
├── README.md                                                         ← this index
│
│   ── 000  ⇄ ATA 00  General / Introduction ──────────────────────
├── 000-000_General-Introduction/
├── 000-100_Applicability-and-Effectivity/
├── 000-200_Identification-and-Designation/
├── 000-300_Vocabulary-Units-and-Reference-Frames/
├── 000-900_Sustainability-Lifecycle-and-DPP-Framing/                 [G]
│
│   ── 001  ⇄ ATA 01  Maintenance Policy (programme-governed) ──────
├── 001-000_Maintenance-Policy-General/
├── 001-100_Maintenance-Concept-and-Philosophy/
├── 001-200_Maintenance-Programme-Structure-MSG-3/
├── 001-300_Reliability-and-Condition-Monitoring-Policy/
├── 001-900_Green-Maintenance-and-Circularity-Policy/                 [G]
│
│   ── 002  ⇄ ATA 02  Operations (programme-governed) ──────────────
├── 002-000_Operations-Information-General/
├── 002-100_Operating-Limitations-General/
├── 002-200_Crew-Roles-and-Responsibilities/
├── 002-300_Operational-Envelope-and-Mission-Profiles/
├── 002-900_Energy-and-Emissions-Operating-Considerations/           [G]
│
│   ── 003  ⇄ ATA 03  Support (programme-governed) ─────────────────
├── 003-000_Support-General/
├── 003-100_Ground-Support-Equipment-Interfaces-General/
├── 003-200_Maintenance-and-Support-Facilities/
├── 003-300_Safety-Zones-and-Hazard-Management-General/
├── 003-900_Energy-Replenishment-Ground-Infrastructure/              [G]
│
│   ── 004  ⇄ ATA 04  Airworthiness Limitations ───────────────────
├── 004-000_Airworthiness-Limitations-General-ALS/
├── 004-100_Structural-Airworthiness-Limitations/
├── 004-200_Systems-Airworthiness-Limitations/
├── 004-300_Certification-Maintenance-Requirements-CMR/
├── 004-900_Energy-Carrier-and-Storage-Airworthiness-Limitations/    [G]
│
│   ── 005  ⇄ ATA 05  Time Limits / Maintenance Checks ─────────────
├── 005-000_Time-Limits-General/
├── 005-100_Time-Limits-and-Life-Limited-Parts/
├── 005-200_Scheduled-Maintenance-Checks/
├── 005-500_Unscheduled-and-Conditional-Inspections/
├── 005-900_Energy-Storage-Inspection-and-Health-Intervals/          [G]
│
│   ── 006  ⇄ ATA 06  Dimensions and Areas ─────────────────────────
├── 006-000_Dimensions-and-Areas-General/
├── 006-100_Principal-Dimensions/
├── 006-200_Stations-Zones-and-Major-Areas/
├── 006-300_Access-Doors-and-Panels/
├── 006-900_Configuration-Geometry-and-Energy-Carrier-Zoning-Delta/  [G]
│
│   ── 007  ⇄ ATA 07  Lifting and Shoring ──────────────────────────
├── 007-000_Lifting-and-Shoring-General/
├── 007-100_Jacking-Points-and-Procedures/
├── 007-200_Shoring-Points-and-Procedures/
├── 007-900_Configuration-Specific-Lifting-Load-Paths-Delta/         [G]
│
│   ── 008  ⇄ ATA 08  Levelling and Weighing ───────────────────────
├── 008-000_Levelling-and-Weighing-General/
├── 008-100_Weighing-and-Balancing/
├── 008-200_Levelling/
├── 008-300_Weight-and-Balance-Reference-Data/
├── 008-900_Energy-Carrier-Mass-and-CG-Effects-Delta/                [G]
│
│   ── 009  ⇄ ATA 09  Towing and Taxiing ──────────────────────────
├── 009-000_Towing-and-Taxiing-General/
├── 009-100_Towing-Procedures-and-Limits/
├── 009-200_Taxiing-Procedures-and-Limits/
└── 009-900_Electrified-and-Energy-Carrier-Ground-Movement-Delta/    [G]
```

> **Structure note:** section-nodes sit **directly** under the master range (flat), as instructed (`master range → nodes`). The chapter (`00X`) is encoded in each node ID; `00X-000` carries the chapter-general content.

---

## 4. Node Register *(definitive)*

| Node | ATA XX-YY | Controlled Node Title | Owner | [G] |
|---|---|---|---|:---:|
| `000-000` | 00-00 † | General / Introduction | Q-DATAGOV | |
| `000-100` | 00-10 † | Applicability & Effectivity | Q-DATAGOV | |
| `000-200` | 00-20 † | Identification & Designation | Q-DATAGOV | |
| `000-300` | 00-30 † | Vocabulary, Units & Reference Frames | Q-DATAGOV | |
| `000-900` | — ‡ | Sustainability, Lifecycle & DPP Framing | Q-GREENTECH | ● |
| `001-000` | 01-00 † | Maintenance Policy — General | Q-DATAGOV | |
| `001-100` | 01-10 † | Maintenance Concept & Philosophy | Q-DATAGOV | |
| `001-200` | 01-20 † | Maintenance Programme Structure (MSG-3) | Q-DATAGOV | |
| `001-300` | 01-30 † | Reliability & Condition-Monitoring Policy | Q-DATAGOV | |
| `001-900` | — ‡ | Green Maintenance & Circularity Policy | Q-GREENTECH | ● |
| `002-000` | 02-00 † | Operations Information — General | Q-AIR | |
| `002-100` | 02-10 † | Operating Limitations — General | Q-AIR | |
| `002-200` | 02-20 † | Crew Roles & Responsibilities | Q-AIR | |
| `002-300` | 02-30 † | Operational Envelope & Mission Profiles | Q-AIR | |
| `002-900` | — ‡ | Energy & Emissions Operating Considerations | Q-GREENTECH | ● |
| `003-000` | 03-00 † | Support — General | Q-GROUND | |
| `003-100` | 03-10 † | GSE Interfaces — General | Q-GROUND | |
| `003-200` | 03-20 † | Maintenance & Support Facilities | Q-GROUND | |
| `003-300` | 03-30 † | Safety Zones & Hazard Management — General | Q-GROUND | |
| `003-900` | — ‡ | Energy-Replenishment Ground Infrastructure | Q-GREENTECH | ● |
| `004-000` | 04-00 | Airworthiness Limitations — General (ALS) | Q-DATAGOV | |
| `004-100` | 04-10 | Structural Airworthiness Limitations | Q-DATAGOV | |
| `004-200` | 04-20 | Systems Airworthiness Limitations | Q-DATAGOV | |
| `004-300` | 04-30 | Certification Maintenance Requirements (CMR) | Q-DATAGOV | |
| `004-900` | — ‡ | Energy-Carrier & Storage Airworthiness Limitations | Q-GREENTECH | ● |
| `005-000` | 05-00 | Time Limits — General | Q-DATAGOV | |
| `005-100` | 05-10 | Time Limits & Life-Limited Parts | Q-DATAGOV | |
| `005-200` | 05-20 | Scheduled Maintenance Checks | Q-DATAGOV | |
| `005-500` | 05-50 | Unscheduled & Conditional Inspections | Q-DATAGOV | |
| `005-900` | — ‡ | Energy-Storage Inspection & Health Intervals | Q-GREENTECH | ● |
| `006-000` | 06-00 | Dimensions & Areas — General | Q-STRUCTURES | |
| `006-100` | 06-10 | Principal Dimensions | Q-STRUCTURES | |
| `006-200` | 06-20 | Stations, Zones & Major Areas | Q-STRUCTURES | |
| `006-300` | 06-30 | Access Doors & Panels | Q-STRUCTURES | |
| `006-900` | — ‡ | Configuration Geometry & Energy-Carrier Zoning Delta | Q-GREENTECH | ● |
| `007-000` | 07-00 | Lifting & Shoring — General | Q-STRUCTURES | |
| `007-100` | 07-10 | Jacking Points & Procedures | Q-STRUCTURES | |
| `007-200` | 07-20 | Shoring Points & Procedures | Q-STRUCTURES | |
| `007-900` | — ‡ | Configuration-Specific Lifting Load Paths Delta | Q-GREENTECH | ● |
| `008-000` | 08-00 | Levelling & Weighing — General | Q-STRUCTURES | |
| `008-100` | 08-10 | Weighing & Balancing | Q-STRUCTURES | |
| `008-200` | 08-20 | Levelling | Q-STRUCTURES | |
| `008-300` | 08-30 | Weight & Balance Reference Data | Q-STRUCTURES | |
| `008-900` | — ‡ | Energy-Carrier Mass & CG Effects Delta | Q-GREENTECH | ● |
| `009-000` | 09-00 | Towing & Taxiing — General | Q-GROUND | |
| `009-100` | 09-10 | Towing Procedures & Limits | Q-GROUND | |
| `009-200` | 09-20 | Taxiing Procedures & Limits | Q-GROUND | |
| `009-900` | — ‡ | Electrified & Energy-Carrier Ground-Movement Delta | Q-GREENTECH | ● |

> † **Chapters 00–03**: ATA 100 reserves these for the operator and does not standardize their sections; the `0X-Y0` codes here are **G-ATLAS-defined** within that band.
> ‡ **`00X-900`**: agnostic **green-architecture delta** — no ATA equivalent; bound per programme (§6).
> All `-900` nodes carry the **Q-GREENTECH** overlay in addition to the chapter owner.

---

## 5. Item / Subject Level & Naming

Items are the **markdown files inside a node**, following `<node>-<item>-<Controlled-Title>.md` (ATA subject `XX-YY-ZZ`).
Convention: `000` = Overview · `001` = Scope and Definitions · then topic-specific.

**Worked example — node `002-100` (⇄ ATA 02-10, Operating Limitations — General):**

```text
002-100_Operating-Limitations-General/
├── README.md
├── 002-100-000-Operating-Limitations-Overview.md
├── 002-100-001-Scope-and-Definitions.md
├── 002-100-002-General-Operating-Limitations.md
├── 002-100-003-Environmental-and-Weather-Limitations.md
└── 002-100-004-Traceability-and-Evidence-Links.md
```

The same item pattern applies to every node above.

---

## 6. Green-Architecture Delta — Agnostic Slots & Programme Specialization

Each `00X-900` node is a **neutral function slot**. The standard ships it once; programmes bind it. This table is the proof of agnosticism — the **left two columns are the standard**, the rest are instantiations.

| Delta Node | Agnostic Function (the standard) | **eWTW** (electric WTW) | **hBWB** (hydrogen BWB) | Other green architecture |
|---|---|---|---|---|
| `000-900` | Sustainability, lifecycle (LC01–LC14) & Digital Product Passport framing | identical | identical | identical |
| `001-900` | Green-maintenance & circularity policy | cell 2nd-life, pack recovery | tank/fuel-cell overhaul, embrittlement mgmt | per technology |
| `002-900` | Energy & emissions operating considerations | grid-carbon & charge scheduling | well-to-wake H₂ pathway | NH₃ / SAF / hybrid |
| `003-900` | Energy-replenishment ground infrastructure | high-power charging interface | LH₂ refuelling interface | per carrier |
| `004-900` | Energy-carrier & storage airworthiness limits | battery + power-electronics limits | cryo-tank + fuel-cell stack limits | per carrier |
| `005-900` | Energy-storage inspection & health intervals | battery State-of-Health thresholds | cryo-tank + stack inspection intervals | per carrier |
| `006-900` | Configuration geometry & energy-carrier zoning | wide tube-and-wing zones; HV keep-out | blended-wing-body zones; cryo keep-out | per geometry/carrier |
| `007-900` | Configuration-specific lifting load paths | tube-and-wing jack/shoring paths | BWB load paths & constraints | per geometry |
| `008-900` | Energy-carrier mass & CG effects | battery mass distribution | LH₂ low-density mass + boil-off CG | per carrier |
| `009-900` | Electrified / energy-carrier ground-movement | e-taxi + HV/thermal-runaway safety | e-taxi + H₂ leak/vent safety | per carrier |

---

## 7. Reference Programme Instantiations

| Programme | Energy carrier | Geometry | Binds deltas as |
|---|---|---|---|
| **eWTW** | Battery-electric | Wide tube-and-wing | battery / power-electronics + conventional zoning |
| **hBWB** | Hydrogen (cryo LH₂ + fuel cell) | Blended-wing-body | cryo-tank / fuel-cell + BWB zoning |
| **(other green-suitable)** | NH₃, SAF, hybrid, … | any | per architecture |

The `000-009` standard is **identical** for all three; only the bindings differ.

---

## 8. Programme Impact & DMC Mapping

`000-009` is the **standard (SSOT)**. A programme consumes it via an impact study mapping applicable nodes/items into its **CSDB (PUB)**.

```text
G-ATLAS node/item            ──(impact study)──►   Programme DMC
00X-Y00/<node>-<item>                              DMC-<PROGRAMME>-<node>-<item>
```

- Canonical short form: `DMC-<PROGRAMME>-<node>-<item>`
- **eWTW** example: `DMC-EWTW-004-900-002`  ·  **hBWB** example: `DMC-HBWB-004-900-002`
- S1000D Issue 4.2 SNS aligns the node prefix `00X` to chapter `0X`; full DMC adds MIC, system/sub-system, disassembly code, info code, applicability.
- **Impact flagging:** each applicable node receives a flag file under the canonical **five-state flag-file impact classification** (state labels are programme-governed; this index defines the slot, not the value).

---

## 9. Governance, Ownership & Inheritance

| Concern | Assignment |
|---|---|
| Band | `000–099` G-ATLAS |
| Master range | `000–009` General Information and Service |
| DEGF | Inherits **DEGF v1.0** eleven mandatory inheritance traits from the band |
| Lifecycle | Governed across **LC01–LC14**; ALS (`004-x`) and Time Limits (`005-x`) are gate-critical |
| Owners | `000/001/004/005` → Q-DATAGOV · `002` → Q-AIR · `003/009` → Q-GROUND · `006/007/008` → Q-STRUCTURES · all `-900` → **Q-GREENTECH** overlay |
| Doctrines | **No-AAA**, **SICO.CA**, **SSOT+PUB** (this standard is SSOT; programme CSDB is PUB) |

---

## 10. Conventions

| Element | Format | Example |
|---|---|---|
| Master range | `000-009_<Title>` | `000-009_General-Information-and-Service` |
| Node (code section) | `00X-Y00_<Title>` | `002-100_Operating-Limitations-General` |
| Item (markdown file) | `<node>-<item>-<Title>.md` | `002-100-001-Scope-and-Definitions.md` |
| Section scaling | ATA `Y0` → `Y00` (`×10`) | `02-10 → 002-100` |
| Green delta | `00X-900`, tagged `[G]` | `004-900` |
| Retired term | ~~code range~~ → **master range** (this level) | — |

---

## 11. Provenance

```yaml
Last.MarkedDown:
  architecture: Q+ATLANTIDE1000
  band: 000-099_G-ATLAS
  band_meaning: Green Aircraft Top-Level Architecture Schema
  master_range: 000-009_General-Information-and-Service
  standards_mirror: ATA 100 / iSpec 2200 chapters 00-09
  node_model: node = code section (00X-Y00) ⇄ ATA chapter-section (0X-Y0)
  section_scaling: "ATA Y0 -> Y00 (x10); green delta -> 00X-900"
  agnostic: true
  reference_programmes: [eWTW, hBWB]
  green_binding: per-programme via impact study (SSOT->PUB)
  nodes_total: 48
  status: agnostic master-range index baseline
  .YieldedAlgorithmicMachineLearning: true
```
