---
pbs_node: eWTW-PBS-053-000
title: Fuselage Wide-Tube
g_atlas: "053"
ata_origin: "53"
config: WTW (Wide Tube Wing)
grammar: "0CC-SSS-UU0 (S-ATLAS x100 sections; subjects x10; -000 = general)"
model: eWTW
side: SSOT
member: "-01_PBS"
owner: Q-STRUCTURES
green_overlay: Q-GREENTECH
doctrine: green-native
status: realized
version: "3.0"
---

# eWTW-PBS-053-000 - Fuselage Wide-Tube

Product node for the primary fuselage structure of the eWTW (WTW - Wide Tube Wing
configuration). Mirrors S-ATLAS `053` (ATA 53) 1:1 - PBS code = SSOT taxonomy
code = AMM SNS code. SSOT-side; the AMM / SRM (PUB) consume it one-way via
`ssot-ref.yaml`.

## Numbering

`0CC-SSS-UU0` per the S-ATLAS 053 register: sections are ATA-section x10 codes
rendered as 3-digit hundreds fields (`053-000`, `053-100` .. `053-900`);
subjects populate the final triplet x10 (`053-SSS-UU0`). The former x10 section
grammar (`053-010` .. `053-110`) is SUPERSEDED - see `PBS-053-BREAKDOWN.md`
and `realize_PBS-053_GATLAS.py --migration-map`.

## Index

- [Scope & Boundary](#scope--boundary)
- [Section Breakdown](#section-breakdown)
- [Legacy](#legacy)
- [Cross-References](#cross-references)
- [Green-Native Notes](#green-native-notes)
- [References](#references)

## Scope & Boundary

**Owns** - the load-carrying fuselage product: major barrel zones (nose/forward /
center / aft / tailcone-and-APM), skin panels and doublers,
frames-stringers-longerons, floor and pressure-deck structure, pressure
bulkheads and major attach fittings, and the **energy-carrier structural
integration**. Door, window, wing, empennage and gear *cutout and attach
structure* is owned here; the *assemblies* that fit those interfaces are owned
by their own chapters.

**Cedes** - door assemblies -> `052`; window assemblies -> `056`; wing ->
`057`; stabilizers/empennage -> `055`; landing-gear *system* -> `032`;
pylons/nacelles -> `054`; the energy carrier itself -> `028`; fire/thermal
containment function -> `026-900`; standards families (splices, cutout
doublers, clips/ties, lugs) and repair practices -> `051`.

## Section Breakdown

| Section | Title | Layer | Owner |
|---|---|:--:|---|
| `eWTW-PBS-053-000-000` | General | STD | Q-STRUCTURES |
| `eWTW-PBS-053-100-000` | Nose and Forward Fuselage Structure | STD | Q-STRUCTURES |
| `eWTW-PBS-053-200-000` | Center Fuselage Structure | ◇ | Q-STRUCTURES |
| `eWTW-PBS-053-300-000` | Aft Fuselage Structure | STD | Q-STRUCTURES |
| `eWTW-PBS-053-400-000` | Tailcone and Auxiliary Power Module Structure | STD | Q-STRUCTURES |
| `eWTW-PBS-053-500-000` | Fuselage Skin Panels and Doublers | STD | Q-STRUCTURES |
| `eWTW-PBS-053-600-000` | Frames Stringers and Longerons | STD | Q-STRUCTURES |
| `eWTW-PBS-053-700-000` | Floor and Pressure Deck Structure | ◇ | Q-STRUCTURES |
| `eWTW-PBS-053-800-000` | Pressure Bulkheads and Major Attach Fittings | STD | Q-STRUCTURES |
| `eWTW-PBS-053-900-000` | Energy Carrier Structural Integration | STD-G | Q-GREENTECH |

> Layer: **STD** carries (energy-neutral) . **◇** green overlay . **STD-G** green delta.
> Each section's `-000` is its general; subjects populate the final triplet (`053-SSS-UU0`).

- [`eWTW-PBS-053-000-000`](eWTW-PBS-053-000-000_General) - General | STD
- [`eWTW-PBS-053-100-000`](eWTW-PBS-053-100-000_Nose-and-Forward-Fuselage-Structure) - Nose and Forward Fuselage Structure | STD
- [`eWTW-PBS-053-200-000`](eWTW-PBS-053-200-000_Center-Fuselage-Structure) - Center Fuselage Structure | ◇
- [`eWTW-PBS-053-300-000`](eWTW-PBS-053-300-000_Aft-Fuselage-Structure) - Aft Fuselage Structure | STD
- [`eWTW-PBS-053-400-000`](eWTW-PBS-053-400-000_Tailcone-and-Auxiliary-Power-Module-Structure) - Tailcone and Auxiliary Power Module Structure | STD
- [`eWTW-PBS-053-500-000`](eWTW-PBS-053-500-000_Fuselage-Skin-Panels-and-Doublers) - Fuselage Skin Panels and Doublers | STD
- [`eWTW-PBS-053-600-000`](eWTW-PBS-053-600-000_Frames-Stringers-and-Longerons) - Frames Stringers and Longerons | STD
- [`eWTW-PBS-053-700-000`](eWTW-PBS-053-700-000_Floor-and-Pressure-Deck-Structure) - Floor and Pressure Deck Structure | ◇
- [`eWTW-PBS-053-800-000`](eWTW-PBS-053-800-000_Pressure-Bulkheads-and-Major-Attach-Fittings) - Pressure Bulkheads and Major Attach Fittings | STD
- [`eWTW-PBS-053-900-000`](eWTW-PBS-053-900-000_Energy-Carrier-Structural-Integration) - Energy Carrier Structural Integration | STD-G

## Legacy

[`eWTW-PBS-053-010-000`](eWTW-PBS-053-010-000_Forward-Fuselage-Section) is the
retained legacy hand-built x10 tree hosting the realized exemplar
`eWTW-PBS-053-010-010` (CSN `530101`). Its S-ATLAS identity is
`053-100-040_Radome-and-Diverters-Attach-Structure` (CSN `531004`); PN map
`EWTW-530101-xxx -> EWTW-531004-xxx`, items and nomenclatures 1:1. Retire it
after executing the exemplar migration (ruling 5).

## Cross-References

| This node references | Owned by | Why |
|---|---|---|
| Door assemblies | `052` Doors | cutout/surround structure stays here |
| Window assemblies | `056` Windows | window-belt structure stays here |
| Wing | `057` Wing | body-side attach fitting here, wing-side there |
| Stabilizers / empennage | `055` Stabilizers-Empennage | body-side attach here |
| Landing-gear system | `032` Landing Gear | gear bays/fittings structure here |
| Pylons / nacelles | `054` Nacelles-and-Pylons | pylon-to-body attach here |
| Energy carrier (battery) | `028` Energy-Carrier-Storage | bay *structure* here, carrier there |
| Fire / thermal containment | `026-900` Fire Protection | structural interface here |
| Standard practices | `051` Standard-Practices-Structures | standards families, fasteners, repairs |

## Green-Native Notes

The fuselage is mostly energy-neutral structure (STD), but the electric WTW adds
one defining section and two overlays:

- **`053-900-000` Energy-Carrier Structural Integration** - the battery-bay
  structure, crash-protection/containment interface (to `026-900`), carrier
  mount and attach fittings, the electric-energy maintenance compartment and
  the vacated auxiliary-fuel-tank footprint. Confirmed coherent with
  `ICN-EWTW-021000010` (053-900 references). No conventional analogue
  (a kerosene tank is a wing-box volume, not a fuselage structural bay). ->
  **STD-G**.
- **◇ overlays** - two conventional sections also carry energy-carrier mass
  and its crash cases: `053-200-000` Center Fuselage Structure (bay
  integration) and `053-700-000` Floor and Pressure Deck Structure (bay
  support + crash).

Terminology per **S-ATLAS-NORM-TERM-001**: engine/APU -> auxiliary-power module
(mounts/firewall in `053-400-000`).

## References

[^ata53]: ATA 100 / iSpec 2200 - Chapter 53 *Fuselage* (heritage scope reference).
[^gatlas]: S-ATLAS `050-059 / 053_Fuselage` register (section/subject SSOT this chapter mirrors 1:1).
[^carrier]: S-ATLAS `028` Energy-Carrier-Storage (battery packs and their limits).
[^fire]: S-ATLAS `026-900` Fire Protection (energy-carrier thermal/fire containment).
[^sp]: S-ATLAS `051` Standard-Practices-Structures (standards families, fasteners, repair allowables).
