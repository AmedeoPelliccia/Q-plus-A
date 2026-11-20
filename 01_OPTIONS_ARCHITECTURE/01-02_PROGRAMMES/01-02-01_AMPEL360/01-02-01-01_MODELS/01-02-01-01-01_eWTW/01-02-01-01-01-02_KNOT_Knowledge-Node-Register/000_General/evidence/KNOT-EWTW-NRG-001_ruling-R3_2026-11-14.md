# Decision record — the energy carrier and the electrical sources deferred to the role of storage

| | |
|---|---|
| KNOTs | `KNOT-EWTW-NRG-001` Energy carrier, ruling R3 · `KNOT-EWTW-SRC-001` Electrical sources, ruling R1 |
| Date | 2026-11-14 |
| Authority | AM.PEL — architecture authority |
| Given | In the working session of 2026-11-14, in Italian. The authority approved this order: complete R1, close the two KNOTs on what is fixed and leave the remaining question in the role of storage, then open the KNOTs that the results exposed. Recorded here in English by Claude |
| Ratified | By the merge of the pull request that carries this record |

The rulings rest on the [research record](KNOT-EWTW-SRC-001_sources-and-storage_2026-11-14.md) of the sources and of storage, on the [candidate missions](MSN-EWTW-NRG-001/README.md), and on rulings R1 and R2 of the energy carrier, R1 as [completed](KNOT-EWTW-NRG-001_ruling-R1-completion_2026-11-14.md) in the same change.

---

## What was asked, and what the convention allows

The authority asked whether the KNOTs could be considered resolved. They cannot be `RULED`: a decision anchor is ruled by scoring its options against approved criteria ([CM-004][CM-004], rule 5), the criteria of the energy carrier are proposed, and the electrical sources have none. The verification script refuses the state.

What the two KNOTs have fixed can be recorded, and the choice that remains can be put in one place. That is what these rulings do. The two KNOTs become `DEFERRED`, which rule 6 defines in the same change: **that amendment is proposed, and the merge ratifies it with the rulings.**

## The two rulings

| KNOT | Ruling | What is fixed | What is deferred |
|---|---|---|---|
| `KNOT-EWTW-NRG-001` | R3 | Conventional fuel for a thermal machine carries the mission energy in every option that stands | Option B against option C: with or without a propulsion battery |
| `KNOT-EWTW-SRC-001` | R1 | A turbogenerator is a main source in every option that stands | Option B against option C: alone, or with batteries |

## One choice, in one place

The three KNOTs held the same choice. It stays in `KNOT-EWTW-STO-001`, whose options map onto the other two.

| `KNOT-EWTW-STO-001` | `KNOT-EWTW-NRG-001` | `KNOT-EWTW-SRC-001` |
|---|---|---|
| A — propulsive energy | C — both | C — combined |
| B — buffering for start, transients and peaks | C — both | C — combined |
| C — essential and emergency supply only | B — fuel, no propulsion battery | B — turbogenerators alone |

The act that rules the role of storage rules the other two.

## What the rulings do

- **They authorise what the remaining options share.** The fuel storage installation, S-ATLAS `028`, and the turbogenerator installation, S-ATLAS `068`, are in every option. Their definition does not wait for the battery. Where the fuel is carried is the question of `KNOT-EWTW-FUL-001`; number, rating and position of the turbogenerators stay gated.
- **They score nothing.** No option is retained or rejected. The criteria of the energy carrier stay proposed and are carried to the decision of the role of storage.
- **They leave the work running.** The KNUs of the two KNOTs continue: the mission budget, the loads, the size of the sources and the distribution do not depend on the deferred choice alone.

## What they do not do

- **They do not choose between fuel alone and fuel with a battery.** The mission screening sizes a battery that flies a share of the trip. It does not size one that only shaves the peaks, so the two roles cannot be compared yet.
- **They do not approve any criterion.** Approving criteria, with weights and thresholds, stays an act of the authority, and `KNOT-EWTW-STO-001` has none proposed.
- **They do not move the ownership of any element.** The propulsion battery installation stays filed under the energy carrier (rule 18).

## Checked before recording

- `tools/knot_check.py` 0.1.5 accepts the register with the two KNOTs `DEFERRED`, and fails it when a deferred KNOT names no other KNOT or has no complete ruling. Its tests include an attempt to retain an option of a deferred KNOT, which is refused.
- The architecture relations still regenerate options B and C of the electrical sources, and the prerequisites they derive agree with the register.
- The gates of the two KNOTs on the PBS stay in the view of pending allocations.

[CM-004]: ../../AMPEL360-KNOT-CM-004_Knowledge-Nodes-and-Units.md
