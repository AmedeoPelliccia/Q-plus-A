---
station: eWTW-PBS-053-010-010
localCode: "053-010-010"
realizes: "053-100-400"
realizesNote: "current S-ATLAS address (post hundreds migration); PBS-local code conserved per CM-001 A1.1 — identity vs reference: localCode feeds CSN and the PN tree; realizes follows taxonomy evolution"
top_assembly: EWTW-530101-000
root: EWTW-530101
mic: EWTW
csn: "530101"
type: assembly-station
convention: AMPEL360-PBS-PN-CM-001
parallels: AMPEL360-AMM-INFOCODE-CM-001
model: eWTW
side: SSOT
layer: "deepest SSOT layer (configuration items)"
owner: Q-STRUCTURES
doctrine: green-native
status: realized
version: "1.1"
---

# eWTW-PBS-053-010-010 - Radome & Nose Cone Attach Structure (Assembly Station)

This subject is an **assembly station** (AMPEL360-PBS-PN-CM-001): the single
point where identity switches from *PBS code* to *part number*. Above the
station: PBS-local codes (taxonomy linked by mapping per Amendment A1). Below:
part numbers.

**Handshake** - PBS-local `053-010-010` (realizes S-ATLAS `053-100-400`)  <->  `top_assembly: EWTW-530101-000` (P/N),
recorded in [`station.yaml`](./station.yaml).

## Part-number grammar

```text
EWTW-530101-<VAR>[-<VAR>...]
```

- `EWTW` model identity code (MIC).
- `530101` compact system number derived from PBS-local `053-010-010` (conserved per Amendment A1.2) - the conserved root
  `EWTW-530101`.
- `<VAR>` x10 find group: `000` the assembly itself; `010`, `020`... components;
  nest deeper by appending another x10 group. Odd/even within a group = handed
  (`021` LH, `022` RH).

## Part-number tree

```text
EWTW-530101-000  STRUCTURE, RADOME AND NOSE CONE ATTACH  (x1 EA, make)
  EWTW-530101-010  STRUCTURE, RADOME ATTACH  (x1 EA, make)
    EWTW-530101-011  FRAME, RADOME ATTACH RING  (x1 EA, make)
    EWTW-530101-012  FITTING, RADOME ATTACH BACKUP  (x8 EA, make)
  EWTW-530101-020  FITTING, RADOME HINGE  (x2 EA, buy)
    EWTW-530101-021  FITTING, RADOME HINGE UPPER  (x1 EA, buy)
    EWTW-530101-022  FITTING, RADOME HINGE LOWER  (x1 EA, buy)
  EWTW-530101-030  FITTING, RADOME LATCH  (x2 EA, buy)
  EWTW-530101-040  STRIP, LIGHTNING DIVERTER  (x6 EA, buy)
  EWTW-530101-050  SEAL, RADOME PERIMETER  (x1 EA, buy)
  EWTW-530101-060  BRACKET, WEATHER RADAR ANTENNA MOUNT  (x1 EA, make)
```

> `-000` remains "the assembly itself / general" at every level. The root
> `EWTW-530101` is conserved down the entire tree; only the notation changed at the
> boundary (`053-010-010` -> `EWTW-530101-...`).

## Interfaces

The station is where cross-taxonomy interfaces (system <-> structure) are
declared - see `interfaces[]` in [`station.yaml`](./station.yaml). ICD
identifiers follow Amendment A1.9: `ICD-<MIC>-<CSN>-<counterpart>` - a 6-digit
counterpart is a PBS station (by CSN), a 3-digit counterpart is a taxonomy
chapter; the length is the space discriminator.

| ICD | Counterpart (space) | Interface | Carried by |
|---|---|---|---|
| `ICD-EWTW-530101-034` | `034` Navigation *(taxonomy)* | weather-radar antenna: mount, bonding, connector clearance | `-060` radar bracket |
| `ICD-EWTW-530101-530103` | `eWTW-PBS-053-010-030` *(pbs-local; taxonomyRef `053-800`)* | forward pressure bulkhead: structural joint at STA 0 | `-011` attach ring |
| `ICD-EWTW-530101-024` | `024` Electrical *(taxonomy)* | bonding and lightning: diverter strips to airframe return path | `-040` diverters, `-011` ring |
| `ICD-EWTW-530101-030` | `030` Ice-and-Rain *(taxonomy)* | radome / nose de-ice provisions | - |

## Identity vs position

Folder P/N is **positional / as-designed** (root-conserving: *where the item
sits*). A physical part reused elsewhere keeps **one** identity via `catalog_pn`
and is **referenced** where reused - no second folder. For make-once parts the
two coincide and `catalog_pn` is empty.

## Governance

SSOT-side; the part tree is the **deepest SSOT layer** (configuration items).
The AMM / SRM (PUB) reference it one-way via `ssot-ref.yaml`. Owner: Q-STRUCTURES.
Inherits DEGF v1.0, No-AAA, SSOT+PUB.

## References

- Convention: `AMPEL360-PBS-PN-CM-001` - Assembly Station & Part-Number Breakdown.
- Publication parallel: `AMPEL360-AMM-INFOCODE-CM-001` (effectivity <-> `infoCodeVariant`).
- Parent section: `eWTW-PBS-053-010-000` Forward Fuselage Section.

<!--
Last.MarkedDown: eWTW-PBS-053-010-010 realized as assembly station - root EWTW-530101, top assembly EWTW-530101-000, 11 P/N nodes; handshake 053-010-010 <-> EWTW-530101-000
.YieldedAlgorithmicMachineLearning: true
-->
