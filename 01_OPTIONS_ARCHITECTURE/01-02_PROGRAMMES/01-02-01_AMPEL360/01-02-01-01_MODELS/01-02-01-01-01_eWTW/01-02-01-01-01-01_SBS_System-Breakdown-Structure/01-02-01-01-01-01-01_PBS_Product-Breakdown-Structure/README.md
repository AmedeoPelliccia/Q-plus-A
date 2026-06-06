---
status: draft
standard_scope: governance
---

# eWTW — Product Breakdown Structure (PBS)

**Product:** AMPEL360 · eWTW — regional electric Wide Tube and Wing
**Location:** `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_MODELS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/`

---

## Numbering convention

The PBS uses a **semantic product identifier** (`eWTW-PBS-NN[-NN[-NN]]`), not the folder ordinal chain. The folder ordinal positions the PBS in the repo; the PBS-ID identifies the product element and is the citable handle. This is the "semantic ID, ordinals for sort only" rule applied at product level.

The PBS decomposes the **physical/functional product** (what the aircraft *is made of*). It **references** the Q+ATLANTIDE/ATLAS taxonomy for what each element *is* — it does not re-define systems. Cross-reference, never cross-containment.

---

## PBS Tree

```text
eWTW-PBS-00  Aircraft Product (top assembly)
│
├── eWTW-PBS-10  AIRFRAME STRUCTURE
│   ├── eWTW-PBS-10-10  Fuselage — wide tube
│   │   ├── eWTW-PBS-10-10-10  Forward section (flight deck, nose)
│   │   ├── eWTW-PBS-10-10-20  Centre section (wing-box integration)
│   │   ├── eWTW-PBS-10-10-30  Aft section (empennage attach, tailcone)
│   │   └── eWTW-PBS-10-10-40  Pressure bulkheads and frames
│   ├── eWTW-PBS-10-20  Wing
│   │   ├── eWTW-PBS-10-20-10  Wing-box (spars, ribs, skins)
│   │   ├── eWTW-PBS-10-20-20  Leading-edge assemblies
│   │   ├── eWTW-PBS-10-20-30  Trailing-edge and high-lift devices
│   │   ├── eWTW-PBS-10-20-40  Control surfaces (ailerons, spoilers)
│   │   └── eWTW-PBS-10-20-50  Wingtip devices
│   ├── eWTW-PBS-10-30  Empennage
│   │   ├── eWTW-PBS-10-30-10  Horizontal stabilizer and elevator
│   │   └── eWTW-PBS-10-30-20  Vertical stabilizer and rudder
│   ├── eWTW-PBS-10-40  Nacelles and pylons (motor mounting structure)
│   ├── eWTW-PBS-10-50  Doors, hatches and windows
│   └── eWTW-PBS-10-60  Landing-gear structure (bays, attach fittings)
│
├── eWTW-PBS-20  ELECTRIC PROPULSION SYSTEM
│   ├── eWTW-PBS-20-10  Electric motor units
│   │   ├── eWTW-PBS-20-10-10  Motor (stator/rotor assembly)
│   │   ├── eWTW-PBS-20-10-20  Motor cooling jacket
│   │   └── eWTW-PBS-20-10-30  Bearings and shaft
│   ├── eWTW-PBS-20-20  Propulsor
│   │   ├── eWTW-PBS-20-20-10  Propeller / ducted-fan rotor
│   │   ├── eWTW-PBS-20-20-20  Pitch-control mechanism
│   │   └── eWTW-PBS-20-20-30  Spinner and duct
│   ├── eWTW-PBS-20-30  Motor power electronics
│   │   ├── eWTW-PBS-20-30-10  Inverters / motor controllers
│   │   ├── eWTW-PBS-20-30-20  Gate drivers and protection
│   │   └── eWTW-PBS-20-30-30  Control interface to FADEC-equivalent
│   ├── eWTW-PBS-20-40  Propulsion thermal management
│   │   ├── eWTW-PBS-20-40-10  Coolant loops and pumps
│   │   ├── eWTW-PBS-20-40-20  Heat exchangers / ram-air
│   │   └── eWTW-PBS-20-40-30  Coolant reservoir and conditioning
│   └── eWTW-PBS-20-50  Nacelle systems (mounts, vibration isolation, firewall)
│
├── eWTW-PBS-30  ENERGY STORAGE AND OPTIONAL HYBRID GENERATION
│   ├── eWTW-PBS-30-10  Battery system
│   │   ├── eWTW-PBS-30-10-10  Battery packs / modules
│   │   ├── eWTW-PBS-30-10-20  Battery management system (BMS)
│   │   ├── eWTW-PBS-30-10-30  Battery thermal management
│   │   ├── eWTW-PBS-30-10-40  Containment, venting and fire isolation
│   │   └── eWTW-PBS-30-10-50  Pack structure and installation
│   ├── eWTW-PBS-30-20  Hybrid energy module (range extender)
│   │   ├── eWTW-PBS-30-20-10  Turbogenerator / fuel-cell stack
│   │   ├── eWTW-PBS-30-20-20  Fuel / reactant storage and supply
│   │   └── eWTW-PBS-30-20-30  Generator power electronics
│   └── eWTW-PBS-30-30  Energy management controller (source arbitration)
│
├── eWTW-PBS-40  ELECTRICAL POWER DISTRIBUTION
│   ├── eWTW-PBS-40-10  High-voltage (HV) distribution
│   │   ├── eWTW-PBS-40-10-10  HV busbars and harnesses
│   │   ├── eWTW-PBS-40-10-20  HV contactors and switchgear
│   │   └── eWTW-PBS-40-10-30  HV protection and isolation monitoring
│   ├── eWTW-PBS-40-20  Power conversion (DC-DC, DC-AC for non-propulsive)
│   ├── eWTW-PBS-40-30  Low-voltage (LV) distribution and avionics power
│   └── eWTW-PBS-40-40  Grounding, bonding and lightning protection
│
├── eWTW-PBS-50  AVIONICS AND FLIGHT SYSTEMS
│   ├── eWTW-PBS-50-10  Integrated modular avionics (IMA) cabinets
│   ├── eWTW-PBS-50-20  Flight control system
│   │   ├── eWTW-PBS-50-20-10  Flight control computers
│   │   ├── eWTW-PBS-50-20-20  Actuation (electromechanical / EHA)
│   │   └── eWTW-PBS-50-20-30  Sensors (air data, inertial)
│   ├── eWTW-PBS-50-30  Navigation systems
│   ├── eWTW-PBS-50-40  Communication systems
│   ├── eWTW-PBS-50-50  Displays and crew interface
│   └── eWTW-PBS-50-60  Energy / propulsion health monitoring and indication
│
├── eWTW-PBS-60  MECHANICAL AND UTILITY SYSTEMS
│   ├── eWTW-PBS-60-10  Actuation power (electric-first; residual hydraulics if any)
│   ├── eWTW-PBS-60-20  Environmental control system (ECS) — electric
│   ├── eWTW-PBS-60-30  Ice and rain protection (electrothermal)
│   ├── eWTW-PBS-60-40  Fire protection and detection
│   ├── eWTW-PBS-60-50  Landing-gear actuation, brakes and steering
│   └── eWTW-PBS-60-60  Fuel/reactant system mechanics (for hybrid module)
│
├── eWTW-PBS-70  CABIN AND PAYLOAD
│   ├── eWTW-PBS-70-10  Cabin interior (linings, stowage, lighting)
│   ├── eWTW-PBS-70-20  Passenger seating
│   ├── eWTW-PBS-70-30  Galley and lavatory
│   ├── eWTW-PBS-70-40  Cargo and baggage systems
│   └── eWTW-PBS-70-50  Cabin safety equipment
│
├── eWTW-PBS-80  GROUND AND SERVICING INTERFACES
│   ├── eWTW-PBS-80-10  Ground charging interface (HV charge port)
│   ├── eWTW-PBS-80-20  Ground power and data interfaces
│   └── eWTW-PBS-80-30  Servicing and replenishment points
│
└── eWTW-PBS-90  PRODUCT SOFTWARE AND DIGITAL CONFIGURATION ITEMS
    ├── eWTW-PBS-90-10  Embedded software configuration items (CSCI)
    ├── eWTW-PBS-90-20  Loadable software parts and data
    └── eWTW-PBS-90-30  Product digital twin / DPP product record
```

---

## ATLAS cross-reference (PBS segment → Q+ATLANTIDE/ATLAS code range)

The PBS organizes the physical product; ATLAS defines the systems. Each PBS segment references its governing ATLAS code range; it does not contain those definitions.

| PBS segment | References ATLAS code range |
|---|---|
| `eWTW-PBS-10` Airframe Structure | `050-059` Primary Structures and Programme Interfaces |
| `eWTW-PBS-20` Electric Propulsion | `070-079` Eco-Tech and Hybrid-Electric Propulsion |
| `eWTW-PBS-30` Energy Storage / Hybrid | `070-079` (hybrid) + EPTA `420-429` Energy Storage (cross-band) |
| `eWTW-PBS-40` Electrical Power Distribution | `020-029` Core Aircraft Systems |
| `eWTW-PBS-50` Avionics and Flight Systems | `040-049` Avionics, Information Systems and APU |
| `eWTW-PBS-60` Mechanical and Utility Systems | `030-039` Protection and Mechanical Systems |
| `eWTW-PBS-70` Cabin and Payload | `020-029` (interiors/systems) + `010-019` service interfaces |
| `eWTW-PBS-80` Ground and Servicing Interfaces | `010-019` Ground Handling and Servicing |
| `eWTW-PBS-90` Product Software / Digital | `040-049` (avionics SW) + Standards `CSDB/DMC`, `DPP` |

Cross-band references (e.g. PBS-30 → EPTA `420-429`) are reference edges only and are registered through the programme impact study, not duplicated into ATLAS.

---

## Effectivity

Every PBS element carries a controlled effectivity tag so the breakdown is queryable and configuration-controlled:

```yaml
effectivity:
  product: eWTW
  configuration: <baseline | block-N>
  msn_range: <e.g. MSN-001..050>
  status: <active | reserved | superseded>
```

The PBS is the **product** decomposition. The matching **work** decomposition (WBS), **cost** (CBS), and **risk** (RBS) live in the sibling folders under the same SBS and reference these PBS-IDs as their anchor.

---

## Repository nesting rule

The physical repository tree follows the PBS hierarchy. Parent PBS folders contain their child PBS folders; physical folder names append a nomenclature slug to the semantic PBS-ID (`<PBS-ID>_<Nomenclature>`), large product blocks are nested under `eWTW-PBS-00_Aircraft-Product/`, and publication artefacts stay inside the owning element's `PUB/` container.

```text
eWTW-PBS-00_Aircraft-Product/
├── eWTW-PBS-10_Airframe-Structure/
│   ├── eWTW-PBS-10-10_Fuselage-Wide-Tube/
│   │   ├── eWTW-PBS-10-10-10_Forward-Fuselage-Section/
│   │   │   ├── SSOT/
│   │   │   ├── PUB/
│   │   │   │   ├── README.md
│   │   │   │   ├── APPLIC/
│   │   │   │   ├── BREX/
│   │   │   │   ├── DM/
│   │   │   │   ├── DMRL/
│   │   │   │   ├── ICN/
│   │   │   │   └── PM/
│   │   │   ├── eWTW-PBS-10-10-10-10_Nose-Structure-and-Radome-Backup/
│   │   │   ├── eWTW-PBS-10-10-10-20_Forward-Pressure-Bulkhead/
│   │   │   ├── eWTW-PBS-10-10-10-30_Flight-Deck-Structure/
│   │   │   ├── eWTW-PBS-10-10-10-40_Side-Window-Structural-Surrounds/
│   │   │   ├── eWTW-PBS-10-10-10-50_Nose-Landing-Gear-Bay-and-Attach/
│   │   │   ├── eWTW-PBS-10-10-10-60_Forward-Equipment-Bay-Structure/
│   │   │   ├── eWTW-PBS-10-10-10-70_Forward-Barrel-Skin-Stringer-Frame/
│   │   │   └── eWTW-PBS-10-10-10-80_Forward-Door-Hatch-Surrounds/
│   │   ├── eWTW-PBS-10-10-20_Centre-Section/
│   │   ├── eWTW-PBS-10-10-30_Aft-Section/
│   │   └── eWTW-PBS-10-10-40_Pressure-Bulkheads-and-Frames/
│   ├── eWTW-PBS-10-20_Wing/
│   ├── eWTW-PBS-10-30_Empennage/
│   ├── eWTW-PBS-10-40_Nacelles-and-Pylons-Motor-Mounting-Structure/
│   ├── eWTW-PBS-10-50_Doors-Hatches-and-Windows/
│   └── eWTW-PBS-10-60_Landing-Gear-Structure-Bays-Attach-Fittings/
├── eWTW-PBS-20_Electric-Propulsion-System/
├── eWTW-PBS-30_Energy-Storage-and-Optional-Hybrid-Generation/
├── eWTW-PBS-40_Electrical-Power-Distribution/
├── eWTW-PBS-50_Avionics-and-Flight-Systems/
├── eWTW-PBS-60_Mechanical-and-Utility-Systems/
├── eWTW-PBS-70_Cabin-and-Payload/
├── eWTW-PBS-80_Ground-and-Servicing-Interfaces/
└── eWTW-PBS-90_Product-Software-and-Digital-Configuration-Items/
```

---

## Forward fuselage section branch

The forward fuselage branch (`eWTW-PBS-10-10-10`) is scaffolded in-repo down to detail-part level so the programme can attach element documentation, SSOT records, and publication artefacts without redefining system ownership.

```text
eWTW-PBS-00_Aircraft-Product/
└── eWTW-PBS-10_Airframe-Structure/
    └── eWTW-PBS-10-10_Fuselage-Wide-Tube/
        └── eWTW-PBS-10-10-10_Forward-Fuselage-Section/
            ├── PUB/
            ├── SSOT/
            ├── eWTW-PBS-10-10-10-10_Nose-Structure-and-Radome-Backup/
            │   ├── eWTW-PBS-10-10-10-10-10_Radome/
            │   ├── eWTW-PBS-10-10-10-10-20_Radome-Backup-Bulkhead/
            │   ├── eWTW-PBS-10-10-10-10-30_Nose-Cap-and-Forward-Fairing/
            │   └── eWTW-PBS-10-10-10-10-40_Lightning-Diverter-Provisions/
            ├── eWTW-PBS-10-10-10-20_Forward-Pressure-Bulkhead/
            │   ├── eWTW-PBS-10-10-10-20-10_Bulkhead-Web/
            │   ├── eWTW-PBS-10-10-10-20-20_Stiffeners-and-Ring-Frame/
            │   └── eWTW-PBS-10-10-10-20-30_Penetration-and-Seal-Provisions/
            ├── eWTW-PBS-10-10-10-30_Flight-Deck-Structure/
            │   ├── eWTW-PBS-10-10-10-30-10_Flight-Deck-Floor-Grid/
            │   ├── eWTW-PBS-10-10-10-30-20_Windshield-Surround-and-Posts/
            │   ├── eWTW-PBS-10-10-10-30-30_Canopy-and-Roof-Frames/
            │   ├── eWTW-PBS-10-10-10-30-40_Glareshield-Support-Structure/
            │   └── eWTW-PBS-10-10-10-30-50_Crew-Volume-Crashworthy-Members/
            ├── eWTW-PBS-10-10-10-40_Side-Window-Structural-Surrounds/
            │   ├── eWTW-PBS-10-10-10-40-10_Window-Cut-Out-Reinforcement/
            │   └── eWTW-PBS-10-10-10-40-20_Window-Frame-Fittings/
            ├── eWTW-PBS-10-10-10-50_Nose-Landing-Gear-Bay-and-Attach/
            │   ├── eWTW-PBS-10-10-10-50-10_NLG-Bay-Structure/
            │   ├── eWTW-PBS-10-10-10-50-20_NLG-Trunnion-Attach-Fittings/
            │   ├── eWTW-PBS-10-10-10-50-30_Drag-and-Side-Load-Fittings/
            │   └── eWTW-PBS-10-10-10-50-40_Bay-Doors-Hinge-Structure/
            ├── eWTW-PBS-10-10-10-60_Forward-Equipment-Bay-Structure/
            │   ├── eWTW-PBS-10-10-10-60-10_Equipment-Rack-Support-Structure/
            │   ├── eWTW-PBS-10-10-10-60-20_Shelf-and-Mounting-Provisions/
            │   ├── eWTW-PBS-10-10-10-60-30_EMI-HIRF-Shielding-Provisions/
            │   ├── eWTW-PBS-10-10-10-60-40_Cooling-Duct-and-Routing-Provisions/
            │   └── eWTW-PBS-10-10-10-60-50_Access-Panel-and-Door-Structure/
            ├── eWTW-PBS-10-10-10-70_Forward-Barrel-Skin-Stringer-Frame/
            │   ├── eWTW-PBS-10-10-10-70-10_Skin-Panels/
            │   ├── eWTW-PBS-10-10-10-70-20_Stringers/
            │   ├── eWTW-PBS-10-10-10-70-30_Frames/
            │   └── eWTW-PBS-10-10-10-70-40_Forward-Production-Join-Splice/
            └── eWTW-PBS-10-10-10-80_Forward-Door-Hatch-Surrounds/
                ├── eWTW-PBS-10-10-10-80-10_Door-Cut-Out-Reinforcement/
                └── eWTW-PBS-10-10-10-80-20_Hatch-Surround-Fittings/
```

## Forward fuselage detail-part index

| PBS ID | Detail part | Primary driver / note |
|---|---|---|
| `eWTW-PBS-10-10-10-10-10` | Radome | RF-transparent nose fairing; bird strike, lightning Zone 1A, weather-radar RF window |
| `eWTW-PBS-10-10-10-10-20` | Radome backup bulkhead | Structural closure behind radome; bird-strike load path |
| `eWTW-PBS-10-10-10-10-30` | Nose cap and forward fairing | Aerodynamic nose; erosion and lightning |
| `eWTW-PBS-10-10-10-10-40` | Lightning diverter provisions | Bonding/diverter mounts; provisions only, system owned by `eWTW-PBS-40-40` |
| `eWTW-PBS-10-10-10-20-10` | Bulkhead web | Pressure boundary; pressurization fatigue and damage tolerance |
| `eWTW-PBS-10-10-10-20-20` | Stiffeners and ring frame | Bulkhead stiffening; pressure stability |
| `eWTW-PBS-10-10-10-20-30` | Penetration and seal provisions | Feed-through points; sealed routing for harnesses and ducts |
| `eWTW-PBS-10-10-10-30-10` | Flight-deck floor grid | Crew floor; crashworthiness and equipment loads |
| `eWTW-PBS-10-10-10-30-20` | Windshield surround and posts | Windshield reaction structure; bird strike and field of view |
| `eWTW-PBS-10-10-10-30-30` | Canopy and roof frames | Flight-deck roof; pressure and escape provisions |
| `eWTW-PBS-10-10-10-30-40` | Glareshield support structure | Instrument-panel support; crew interface install provision for `eWTW-PBS-50-50` |
| `eWTW-PBS-10-10-10-30-50` | Crew-volume crashworthy members | Survivable-volume structure; crashworthiness |
| `eWTW-PBS-10-10-10-40-10` | Window cut-out reinforcement | Local reinforcement; fatigue around cut-outs |
| `eWTW-PBS-10-10-10-40-20` | Window frame fittings | Transparency attach; pressure-seal interface |
| `eWTW-PBS-10-10-10-50-10` | NLG bay structure | Gear cavity; reacts landing gear loads |
| `eWTW-PBS-10-10-10-50-20` | NLG trunnion attach fittings | Primary gear attach; interface to `eWTW-PBS-60-50` |
| `eWTW-PBS-10-10-10-50-30` | Drag and side-load fittings | Gear load reaction; landing and taxi loads |
| `eWTW-PBS-10-10-10-50-40` | Bay doors hinge structure | Gear-door support; door system provision |
| `eWTW-PBS-10-10-10-60-10` | Equipment rack support structure | E/E rack structure; avionics install provision for `eWTW-PBS-50` |
| `eWTW-PBS-10-10-10-60-20` | Shelf and mounting provisions | Equipment shelves; install provision |
| `eWTW-PBS-10-10-10-60-30` | EMI/HIRF shielding provisions | Shielding structure elevated for electric architecture |
| `eWTW-PBS-10-10-10-60-40` | Cooling duct and routing provisions | Thermal-path provision; cooling system owned by `eWTW-PBS-60-20` |
| `eWTW-PBS-10-10-10-60-50` | Access panel and door structure | Maintenance access; maintainability |
| `eWTW-PBS-10-10-10-70-10` | Skin panels | Fuselage shell; pressure and bending |
| `eWTW-PBS-10-10-10-70-20` | Stringers | Longitudinal stiffening; bending and buckling |
| `eWTW-PBS-10-10-10-70-30` | Frames | Circumferential stiffening; shape and pressure |
| `eWTW-PBS-10-10-10-70-40` | Forward production join splice | Mate to centre section; shared interface with `eWTW-PBS-10-10-20` |
| `eWTW-PBS-10-10-10-80-10` | Door cut-out reinforcement | Local reinforcement; fatigue around door cut-outs |
| `eWTW-PBS-10-10-10-80-20` | Hatch surround fittings | Hatch attach; seal interface |

### Forward fuselage notes

- **Provisions vs systems.** Structural provisions in this branch own only mounts, routing paths, shielding, and load paths. The corresponding systems remain owned by their governing PBS branches (for example `eWTW-PBS-40-40` and `eWTW-PBS-60-20`).
- **Shared interface.** `eWTW-PBS-10-10-10-70-40` is the controlled splice to the centre section (`eWTW-PBS-10-10-20`); any definition change on either side requires coordinated review across both product elements.
- **Effectivity inheritance.** The branch inherits `eWTW · baseline · MSN-001..050` by default, while detail parts can override `status` or block effectivity when needed.
- **Element documents.** The drilled path and detail-part folders each carry a local `README.md` so configuration, SSOT, and publication artefacts can be added without changing the PBS identifier scheme.

---

## Notes

- **Electric-first architecture.** PBS-60-10 is named "electric-first" because the eWTW removes the conventional central hydraulic system in favour of electromechanical actuation; residual hydraulics, if retained for specific actuators, are a configuration decision recorded in effectivity.
- **Hybrid module is optional by configuration.** PBS-30-20 (range extender) is present in hybrid blocks and `reserved`/absent in battery-only blocks; the energy management controller (PBS-30-30) arbitrates whichever sources the block carries.
- **HV charging is a product element.** Unlike conventional refuelling (a service interface), the HV charge port (PBS-80-10) is product hardware with its own airworthiness and safety case, hence its place in the PBS rather than only in operations.
