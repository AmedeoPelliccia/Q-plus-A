# Decision record — ruling R2 of the energy carrier

| | |
|---|---|
| KNOT | `KNOT-EWTW-NRG-001` Energy carrier |
| Ruling | R2, 2026-11-14 |
| Authority | AM.PEL — architecture authority |
| Given | In the working session of 2026-11-14, in Italian, as four decisions and the consequence accepted with them. Recorded here in English by Claude |
| Ratified | By the merge of the pull request that carries this record |
| Closes | `KNU-EWTW-NRG-001-02` Design mission and reserve policy |

The ruling rests on the [candidate missions](MSN-EWTW-NRG-001/README.md), on the [research record](KNOT-EWTW-NRG-001_energy-carrier_2026-11-14.md) of the energy carrier and on the [audit record](KNOT-EWTW-NRG-001_audit-of-mission-closure_2026-11-14.md) of the first version of the test. It scores no option, and it states no conformity of the eWTW with any rule.

---

## The four decisions

### 1. Missions

The set is approved with three roles. Mission M does not become the design mission.

| Mission | Stage | Role | What the role means |
|---|---:|---|---|
| S | 500 km | Sensitivity | The stage on which the terminal phases weigh as much as the cruise. It sizes nothing |
| M | About 1,100 km | Scoring | The average stage. Fuel, cost and emissions are compared on it. It is not the range requirement |
| L | 2,000 km, 100 seats, declared reserves | Requirement | It must close. It lies inside the envelope of the reference type, and the model already computes it |

The range the reference type is offered with, 2,400 nm, is not a gate. On that point the model asks for more fuel than the aircraft can load, so using it as a requirement would fail the reference for a defect of the model. It becomes a gate only when the model reproduces it within a written tolerance.

### 2. Reserve

Two numbers with two uses. They are not added.

- **For the eWTW, the final reserve is 30 minutes** at holding speed, at 1,500 ft. It is the floor of turbine-engined aeroplanes, taken as an assumption because no acceptable means of compliance gives a quantity for electric engines under CS-25. It reopens if EASA publishes one.
- **The alternate is a separate item.** It is not inside those 30 minutes.
- **The 45 minutes of the charts of the reference type** — 100 nm alternate and 45 min flight — stay the reserve of the reference. They are used only when the model is compared with that type. They are not the final reserve of electric engines.

### 3. Maturity

**Level 6** is required of each critical element at the release of the preliminary-design baseline, not of the concept baseline. The decision holds if level 6 means a prototype in a relevant environment. It does: see *What was checked*.

No critical element on the list is at level 6. Level 6 therefore freezes nothing now. It holds the passage to the preliminary-design baseline, unless an element has an approved maturation cycle with a fallback, or a waiver for that element. The level is not lowered to 5 to pass the motor, and it is not raised to 7.

### 4. Seats

**The aircraft keeps 100 seats.** Reducing the seats or the stage to make batteries alone close changes the aircraft. It is not a result of the comparison.

Option A stays in the record and is not a candidate. It reopens only on a pack that is demonstrated, not projected, and that closes mission L at 100 seats with the cycle life of service. A cell does not reopen it.

## The consequence accepted with them

On the requirement mission, at 100 seats, with the evidence on record:

- **Option B closes** at nominal values, and not at unfavourable values.
- **Option C is not eliminated.** That it breaks even at about 480 Wh/kg and saves 6 to 11 % of the fuel between 650 and 1,000 Wh/kg holds for a battery that flies a quarter of the short stage, and disappears if the empty mass grows with the take-off mass.
- **Option A is not a candidate** until its reopen condition is met.

The limit declared in the test still holds: the three options have the same empty mass, and the cruise of option B is set equal to that of the turbofan of the reference.

## What was checked before recording

| Point | Checked against | Result |
|---|---|---|
| The meaning of level 6 | `TRL-controlled-vocabulary.yaml` of the taxonomy, scheme Q+ATLANTIDE-TRL | TRL-6 is *System/subsystem model or prototype demonstration in relevant environment*. The condition of decision 3 is met |
| The reserve of the reference | Embraer 190 airport planning manual, section 3.2, revision 20, read on 2026-11-14 | The charts state a reserve of 100 nm alternate and 45 min flight, at Mach 0.78 with passengers at 100 kg |
| The figures of the consequence | `MSN-EWTW-NRG-001` 0.3.0 | They are those of the test. On mission L, option A needs about 1,560, 3,500 and 6,600 Wh/kg at favourable, nominal and unfavourable values |
| The level of the motor | `TRL-evidence-requirements.md` | The record showed level 5 on a statement of the manufacturer. Level 5 asks for test results in a relevant environment, so the record now shows no level |

## What the ruling does and does not do

- **It excludes option A from the scope. It does not reject it by scoring.** The criteria of the KNOT are still proposed, and no option is scored (CM-004, rule 5).
- **It approves the six maturity records** of the KNOT. The criteria stay proposed, so the gate of rule 5 stays closed.
- **It does not narrow the other KNOTs.** Option A of `KNOT-EWTW-SRC-001`, batteries alone, and option A of `KNOT-EWTW-PRP-001`, all-electric, rest on the option excluded here. Whether this ruling removes them is for the authority to say. The relations convention cannot yet record a node that is excluded alone and admitted in a combination (CM-005, rule 9).
- **It writes no tolerance** for the range of the reference type. Until one is written, that point is a check of the model.
- **It leaves ruling R1 as it is**: provisional, without rationale or evidence.

## Reopen conditions

| Condition | Reopens |
|---|---|
| A battery pack demonstrated, not projected, closes the requirement mission at 100 seats with the cycle life of service. A cell does not meet the condition | Option A |
| EASA publishes a quantity for the final reserve of a CS-25 aeroplane with electric engines | The reserve policy of the mission set |
