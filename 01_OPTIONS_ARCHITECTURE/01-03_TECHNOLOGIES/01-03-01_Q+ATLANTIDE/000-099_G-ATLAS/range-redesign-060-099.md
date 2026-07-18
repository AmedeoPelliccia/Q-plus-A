# ATLAS Band — Range Redesign 060–099 (Sustainable-Aviation-Only)

**Ruling document** · Owner: architecture authority (AM.PEL) · Date: 2026-07-18
**Scope:** code ranges 060–099 of the aircraft band (Q+ATLANTIDE, 000-099).
**Status:** RATIFIED — merged into the band register.
**Migration cost:** register-level only. No chapter under 060–099 has been realized; no content moves.

---

## 1. Doctrine

The aircraft band documents propulsion **for sustainable aviation only**. Fossil-only propulsion configurations have no home in this band **by scope declaration, not by omission**: where a programme impact study requires a conventional baseline for comparison, it references established external documentation (ATA-structured legacy publications), never a band chapter. Combustion itself is not excluded — combustion of sustainable energy carriers is a pillar of the transition and is documented as such.

## 2. Range register — old → new

| Range | Former name | New controlled name | Primary scope |
|---|---|---|---|
| `060–069` | Traditional-Propulsion | **Sustainable-Fuel-Combustion-Propulsion** | Turbomachinery and combustion systems for sustainable energy carriers: SAF-compatible turbofans/turboprops, hydrogen-burning turbines, turbogenerator machines for hybrid architectures, low-NOx and contrail-aware combustion, fuel-flexibility provisions |
| `070–079` | Eco-Tech-and-Hybrid-Electric-Propulsion | **Electric-and-Hybrid-Electric-Propulsion** | Electric drivetrains and their architectures: motors, drives, distributed propulsion, battery-electric and hybrid-electric integration, fuel-cell-electric powertrains (electrochemical source, electric drive) |
| `080–089` | Alternative-and-Quantum-Propulsion | **Alternative-and-Quantum-Propulsion** *(unchanged)* | Frontier and disruptive propulsion concepts beyond the combustion/electric classes, including quantum-enabled propulsion research architectures |
| `090–099` | Type-Specific-Programmes-and-Expansion | **Type-Specific-Architectures-and-Expansion** | Aircraft-type-specific architecture classes (configurations, not programmes) and controlled expansion space |

## 3. Boundary lines (declared now, inherited by future chapters)

* **Hybrid split:** the hybrid **architecture** (energy management, drivetrain, propulsor integration) lives in `070`; the turbogenerator **machine** is `060` technology referenced by `070` — one machine taxonomy, many architecture consumers.
* **Hydrogen split:** hydrogen **combustion** (turbines burning H₂) is `060`; hydrogen **electrochemical conversion** (fuel-cell powertrains) is `070`; hydrogen **storage and distribution** remains with the fuel-system chapters (`028`-class) — conversion class decides the range, not the molecule.
* **Fuels as carriers:** SAF and hydrogen appear in `060` as *combustion integration* topics; energy-carrier production and off-aircraft infrastructure belong to the energy band (`400–499 EPTA`), referenced, never duplicated.
* **Non-CO₂ effects:** contrail-aware combustion and emissions characterization live in `060` as technology subjects; environmental *assessment methodology* stays with lifecycle/impact layers.
* **`090` agnosticism:** "type-specific" means configuration classes (e.g., blended-wing-body class provisions, regional-class provisions). Programme names never appear — the range title change from "Programmes" to "Architectures" is itself a compliance fix to the standing programme-agnostic ruling.

## 4. Naming consequence (for the band-name decision, separately ruled)

With this redesign, the band's content is sustainable-aviation-only **regardless of the band's name**: the internal contradiction that disqualified sustainability-claiming names ("zero-impact band containing Traditional Propulsion") is dissolved. The band-name ruling (ATLAS · Z-ATLAS · S-ATLAS) remains open and independent; whichever name is chosen, its subtitle can now state the orientation truthfully.

## 5. Execution

1. Ratify this register (merge = ratification). ✔ *This merge.*
2. Fold the range renames into the band-rename Copilot prompt (single `git mv` + register pass, executed verification per house standard) once the band name is ruled — one PR, one traffic disruption, one LinkedIn link edit.
3. Update `controlled-vocabulary.yaml`, root README band table and chapter-range references in the same PR.
