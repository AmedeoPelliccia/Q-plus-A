# 040-049 — Avionics Information Systems and APU

Green Aircraft Top-Level Architecture Schema (G-ATLAS) code range for the AMPEL360 next-generation models **eWTW** (electric Wide-Tube-and-Wing) and **hBWB** (hydrogen Blended-Wing-Body).

Headline transpositions: the auxiliary power unit becomes the **Auxiliary Power Module** (049 — fuel-cell on hBWB, battery/converter on eWTW; no turbomachinery); nitrogen generation becomes **Inerting and Protective Atmospheres** (047 — hydrogen bays and, pending ruling, the energy-carrier bay); central maintenance becomes **Onboard Maintenance Systems** (045 — prognostics and Digital Product Passport governance); 042/046 carry explicit partitioning and security-domain governance.

## Chapter register

| Chapter | Title | Applicability | Sections |
|---|---|---|---|
| `042` | Integrated Modular Avionics | eWTW+hBWB | 6 |
| `044` | Cabin Systems | eWTW+hBWB | 6 |
| `045` | Onboard Maintenance Systems | eWTW+hBWB | 6 |
| `046` | Information Systems | eWTW+hBWB | 7 |
| `047` | Inerting and Protective Atmospheres | hBWB baseline; eWTW pending ruling | 6 |
| `049` | Auxiliary Power Module | eWTW+hBWB | 9 |

## Reserved chapter slots

- `040` Reserved — RESERVED: future assignment (range-general provisions).
- `041` Water Ballast — RESERVED: not applicable on eWTW/hBWB.
- `043` Reserved — RESERVED: reserved per classic grammar.
- `048` Reserved — RESERVED: reserved per classic grammar.

Generated 2026-07-09 · realize_G-ATLAS-040-049.py v1.0.0 · register regenerated from the realizer data, never hand-edited · No-AAA compliant
