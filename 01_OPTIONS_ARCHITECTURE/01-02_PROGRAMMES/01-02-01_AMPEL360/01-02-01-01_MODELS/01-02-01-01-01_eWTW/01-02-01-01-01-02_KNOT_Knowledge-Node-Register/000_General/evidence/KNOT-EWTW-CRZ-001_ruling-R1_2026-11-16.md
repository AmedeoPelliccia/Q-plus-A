# Decision record — maturity required of the cruise point, and the moment of the minimum objective

| | |
|---|---|
| KNOT | `KNOT-EWTW-CRZ-001` Cruise point, ruling R1 |
| Date | 2026-11-16 |
| Authority | AM.PEL — architecture authority |
| Given | In the working session of 2026-11-16, in Italian. On the maturity: «i criteri di maturità sono approvati, a meno che tu non veda dei problemi». On the moment at which criterion `M5` applies: «va bene, manteniamo aperte ancora le opzioni in campo». Recorded here in English by Claude |
| Ratified | By the merge of the pull request that carries this record |

The ruling rests on the [proposal of the criteria and of the maturity](KNOT-EWTW-CRZ-001_criteria-proposal_2026-11-15.md), on the [screening of the cruise points](CRP-EWTW-CRZ-001/README.md) and on ruling R2 of the energy carrier ([decision record](KNOT-EWTW-NRG-001_ruling-R2_2026-11-14.md)).

---

## What the ruling does

**It approves the three maturity records.**

| Record | Element | Options | Level required | Level on record |
|---|---|---|---|---|
| `Q1` | Turbogenerator of megawatt class | A, B, C | 6 | none |
| `Q2` | Propeller driven by an electric motor of megawatt class, at the cruise Mach of the option | A, C | 6 | none |
| `Q3` | Ducted fan driven by an electric motor of megawatt class, at the cruise Mach of the option | B | 6 | none |

Level 6 of the Q+ATLANTIDE-TRL scale is a model or prototype of the system or subsystem demonstrated in a relevant environment. It is required at the release of the preliminary-design baseline, not of the concept baseline. It is the threshold of ruling R2, and no waiver is sought.

**It fixes when the minimum objective applies.** Criterion `M5`, a carbon dioxide metric not above the most stringent limit in law, is to be met at the release of the preliminary-design baseline. At the concept baseline the gap at nominal values is recorded as a target. Applied today it would reject every option: the screening puts the metric 23 % above the objective at the propeller points and 39 % above it at the jet point.

## How the words were read

The authority said *the maturity criteria*. The reviewer took that as the three maturity records. The ten criteria of the KNOT, `M1` to `M5` and `T1` to `T5`, are not named in it, and they stay `PROPOSED` until the authority names them. The approval is recorded on the narrower reading; the wider one costs one word, and nothing waits for it, because no option is scored before a drag polar exists (`KNOT-EWTW-AER-001`).

## What the reviewer checked

The approval was given unless the reviewer saw problems. None stands against the thresholds. Three points go with them.

- **The thresholds agree with ruling R2.** The turbogenerator is record `Q4` of `KNOT-EWTW-NRG-001` and record `Q1` here, at the same level and for the same decision. One element has one threshold.
- **No element has a level on record.** `level` is null in the three records: the reviewer set none on the evidence on record. The convention allows it. The release of a concept baseline asks for the readiness level and the assumptions of each immature element ([lifecycle model][LCM], §13.2), so the three levels are to be assessed before that release. Five of the six records of `KNOT-EWTW-NRG-001` are in the same state.
- **The relevant environment follows the cruise point.** Level 6 is a demonstration in a relevant environment. For the propulsors the records say which: the cruise Mach of the option. The same holds for the altitude. The pressure at the cruise point is the environment of the high-voltage distribution, record `Q5` of `KNOT-EWTW-NRG-001`, and its evidence is to be read against the point that is ruled.

## What it does not do

- **It approves no criterion.** Rule 5 of [CM-004][CM-004] keeps the KNOT closed to scoring while a criterion is `PROPOSED`.
- **It scores nothing.** Options A, B and C stay open.
- **It sets no level and grants no waiver.**

## Checked before recording

- `tools/knot_check.py` accepts the register with the three records `APPROVED` and the ruling `COMPLETE`.
- On a copy, an option rejected now is refused: *scored without criteria or maturity*. With the ten criteria approved as well, that failure is gone.

[CM-004]: ../../AMPEL360-KNOT-CM-004_Knowledge-Nodes-and-Units.md
[LCM]: ../../../../../../../../02_LIFECYCLE_MODEL/README.md
