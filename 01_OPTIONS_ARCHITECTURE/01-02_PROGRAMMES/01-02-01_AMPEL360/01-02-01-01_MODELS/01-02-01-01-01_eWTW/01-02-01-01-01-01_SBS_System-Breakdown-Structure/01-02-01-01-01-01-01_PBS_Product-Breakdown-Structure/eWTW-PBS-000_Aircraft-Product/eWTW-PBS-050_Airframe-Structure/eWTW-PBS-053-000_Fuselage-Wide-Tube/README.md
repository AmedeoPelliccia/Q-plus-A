---
pbs_node: eWTW-PBS-053-000
title: Fuselage Wide-Tube
g_atlas: "053"
ata_origin: "53"
config: WTW (Wide Tube Wing)
grammar: "0CC-SS0-UU0 (x10 hierarchical; -000 = general at each level)"
model: eWTW
side: SSOT
member: "-01_PBS"
owner: Q-STRUCTURES
green_overlay: Q-GREENTECH
doctrine: green-native
status: realized
version: "2.0"
---

# eWTW-PBS-053-000 - Fuselage Wide-Tube

Product node for the primary fuselage structure of the eWTW (WTW - Wide Tube Wing
configuration). Mirrors G-ATLAS `053` (ATA 53). SSOT-side; the AMM / SRM (PUB)
consume it one-way via `ssot-ref.yaml`.

## Numbering

`0CC-SS0-UU0`, x10 at each level, `-000` = general:
`053-000` chapter . `053-000-000` chapter general . `053-SS0-000` section
(general of section) . `053-SS0-UU0` unit.

## Index

- [Scope & Boundary](#scope--boundary)
- [Section Breakdown](#section-breakdown)
- [Cross-References](#cross-references)
- [Green-Native Notes](#green-native-notes)
- [References](#references)

## Scope & Boundary

**Owns** - the load-carrying fuselage product: major barrel sections (forward /
center / aft / tailcone), skin, frames-stringers-longerons, passenger and cargo
floor, pressure bulkheads, keel beam and major attach fittings, aerodynamic
fairings, and the **energy-carrier bay structural provisions**. Door, window,
wing, empennage, gear and pylon *cutout and attach structure* is owned here; the
*assemblies* that fit those interfaces are owned by their own chapters.

**Cedes** - door assemblies -> `052`; window assemblies -> `056`; wing ->
`057`; stabilizers/empennage -> `055`; landing-gear *system* -> `032`;
pylons/nacelles -> `054`; the energy carrier itself -> `028`; fire/thermal
containment function -> `026-900`; fasteners/repair practices -> `051`.

## Section Breakdown

| Section | Title | Layer | Owner |
|---|---|:--:|---|
| `eWTW-PBS-053-000-000` | General | STD | Q-STRUCTURES |
| `eWTW-PBS-053-010-000` | Forward Fuselage Section | STD | Q-STRUCTURES |
| `eWTW-PBS-053-020-000` | Center Fuselage Section | ◇ | Q-STRUCTURES |
| `eWTW-PBS-053-030-000` | Aft Fuselage Section | STD | Q-STRUCTURES |
| `eWTW-PBS-053-040-000` | Tailcone and Auxiliary Power Module Bay | STD | Q-STRUCTURES |
| `eWTW-PBS-053-050-000` | Skin Panels and Doublers | STD | Q-STRUCTURES |
| `eWTW-PBS-053-060-000` | Frames Stringers and Longerons | STD | Q-STRUCTURES |
| `eWTW-PBS-053-070-000` | Floor Structure Passenger and Cargo | ◇ | Q-STRUCTURES |
| `eWTW-PBS-053-080-000` | Pressure Bulkheads | STD | Q-STRUCTURES |
| `eWTW-PBS-053-090-000` | Keel Beam and Major Attach Fittings | ◇ | Q-STRUCTURES |
| `eWTW-PBS-053-100-000` | Aerodynamic Fairings | STD | Q-STRUCTURES |
| `eWTW-PBS-053-110-000` | Energy Carrier Bay Structural Provisions | STD-G | Q-GREENTECH |

> Layer: **STD** carries (energy-neutral) . **◇** green overlay . **STD-G** green delta.
> Each section's `-000` is its general; deeper units populate the final triplet (`053-SS0-UU0`).

- [`eWTW-PBS-053-000-000`](eWTW-PBS-053-000-000_General) - General | STD
- [`eWTW-PBS-053-010-000`](eWTW-PBS-053-010-000_Forward-Fuselage-Section) - Forward Fuselage Section | STD
- [`eWTW-PBS-053-020-000`](eWTW-PBS-053-020-000_Center-Fuselage-Section) - Center Fuselage Section | ◇
- [`eWTW-PBS-053-030-000`](eWTW-PBS-053-030-000_Aft-Fuselage-Section) - Aft Fuselage Section | STD
- [`eWTW-PBS-053-040-000`](eWTW-PBS-053-040-000_Tailcone-and-Auxiliary-Power-Module-Bay) - Tailcone and Auxiliary Power Module Bay | STD
- [`eWTW-PBS-053-050-000`](eWTW-PBS-053-050-000_Skin-Panels-and-Doublers) - Skin Panels and Doublers | STD
- [`eWTW-PBS-053-060-000`](eWTW-PBS-053-060-000_Frames-Stringers-and-Longerons) - Frames Stringers and Longerons | STD
- [`eWTW-PBS-053-070-000`](eWTW-PBS-053-070-000_Floor-Structure-Passenger-and-Cargo) - Floor Structure Passenger and Cargo | ◇
- [`eWTW-PBS-053-080-000`](eWTW-PBS-053-080-000_Pressure-Bulkheads) - Pressure Bulkheads | STD
- [`eWTW-PBS-053-090-000`](eWTW-PBS-053-090-000_Keel-Beam-and-Major-Attach-Fittings) - Keel Beam and Major Attach Fittings | ◇
- [`eWTW-PBS-053-100-000`](eWTW-PBS-053-100-000_Aerodynamic-Fairings) - Aerodynamic Fairings | STD
- [`eWTW-PBS-053-110-000`](eWTW-PBS-053-110-000_Energy-Carrier-Bay-Structural-Provisions) - Energy Carrier Bay Structural Provisions | STD-G

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
| Standard practices | `051` Standard-Practices-Structures | fasteners, repairs |

## Green-Native Notes

The fuselage is mostly energy-neutral structure (STD), but the electric WTW adds
one defining section and three overlays:

- **`053-110-000` Energy-Carrier Bay Structural Provisions** - a dedicated
  under-floor enclosure for the battery packs: structural cassette, crash-load
  protection, and the thermal/fire **containment interface** to `026-900`. No
  conventional analogue (a kerosene tank is a wing-box volume, not a fuselage
  structural bay). -> **STD-G**.
- **◇ overlays** - three conventional sections now also carry energy-carrier
  mass and its crash cases: `053-020-000` Center Fuselage Section (bay
  integration), `053-070-000` Floor Structure (bay support + crash), and
  `053-090-000` Keel Beam & Major Attach Fittings (energy-carrier mount
  fittings). -> **◇**.

Terminology per **G-ATLAS-NORM-TERM-001**: engine/APU -> auxiliary-power module
(bay in `053-040-000`).

## References

[^ata53]: ATA 100 / iSpec 2200 - Chapter 53 *Fuselage* (heritage scope reference).
[^carrier]: G-ATLAS `028` Energy-Carrier-Storage (battery packs and their limits).
[^fire]: G-ATLAS `026-900` Fire Protection (energy-carrier thermal/fire containment).
[^sp]: G-ATLAS `051` Standard-Practices-Structures (fasteners, repair allowables).
