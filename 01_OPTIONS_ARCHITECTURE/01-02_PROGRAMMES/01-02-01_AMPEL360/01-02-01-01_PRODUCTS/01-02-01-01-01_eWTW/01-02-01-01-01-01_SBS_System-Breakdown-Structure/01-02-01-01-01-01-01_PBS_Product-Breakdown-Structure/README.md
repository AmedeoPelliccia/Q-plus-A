---
status: draft
standard_scope: governance
---

# eWTW — Product Breakdown Structure (PBS)

**Product:** AMPEL360 · eWTW — regional electric Wide Tube and Wing
**Location:** `01_OPTIONS_ARCHITECTURE/01-02_PROGRAMMES/01-02-01_AMPEL360/01-02-01-01_PRODUCTS/01-02-01-01-01_eWTW/01-02-01-01-01-01_SBS_System-Breakdown-Structure/01-02-01-01-01-01-01_PBS_Product-Breakdown-Structure/`

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
| `eWTW-PBS-10` Airframe Structure | `050-059` Estructuras |
| `eWTW-PBS-20` Electric Propulsion | `070-079` Propulsión Eco-Tech e Híbrido-Eléctrica |
| `eWTW-PBS-30` Energy Storage / Hybrid | `070-079` (hybrid) + EPTA `420-429` Almacenamiento de Energía (cross-band) |
| `eWTW-PBS-40` Electrical Power Distribution | `020-029` Sistemas Core de Aeronave |
| `eWTW-PBS-50` Avionics and Flight Systems | `040-049` Aviónica, Información & APU |
| `eWTW-PBS-60` Mechanical and Utility Systems | `030-039` Protección & Sistemas Mecánicos |
| `eWTW-PBS-70` Cabin and Payload | `020-029` (interiors/systems) + `010-019` service interfaces |
| `eWTW-PBS-80` Ground and Servicing Interfaces | `010-019` Manejo en Tierra & Servicio |
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

## Notes

- **Electric-first architecture.** PBS-60-10 is named "electric-first" because the eWTW removes the conventional central hydraulic system in favour of electromechanical actuation; residual hydraulics, if retained for specific actuators, are a configuration decision recorded in effectivity.
- **Hybrid module is optional by configuration.** PBS-30-20 (range extender) is present in hybrid blocks and `reserved`/absent in battery-only blocks; the energy management controller (PBS-30-30) arbitrates whichever sources the block carries.
- **HV charging is a product element.** Unlike conventional refuelling (a service interface), the HV charge port (PBS-80-10) is product hardware with its own airworthiness and safety case, hence its place in the PBS rather than only in operations.
