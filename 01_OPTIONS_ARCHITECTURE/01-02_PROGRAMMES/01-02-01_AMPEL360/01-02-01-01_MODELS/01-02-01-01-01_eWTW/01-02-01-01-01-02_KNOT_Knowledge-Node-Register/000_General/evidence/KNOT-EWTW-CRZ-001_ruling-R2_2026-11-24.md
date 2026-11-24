# Decision record — ruling R2 of the cruise point: the criteria approved, a working reference

| | |
|---|---|
| KNOT | `KNOT-EWTW-CRZ-001` Cruise point |
| Ruling | R2, of 2026-11-24 |
| Authority | AM.PEL — architecture authority |
| Drafted by | Claude, 2026-11-24, from the decisions of the authority of that day. It is the authority's by the merge of the pull request that carries it |
| Closes | `KNU-EWTW-CRZ-001-03` Decision criteria and maturity thresholds |

On 2026-11-24 the authority took three decisions. It approved the ten criteria of the cruise point, two with a modification. It took a working reference for the cruise point, the section and the wing. It confirmed the ambition of at least 26 %. This ruling scores and excludes no option.

---

## What the authority decided, and where

**The criteria.** The reviewer set the ten criteria on a page, one to a row, in Italian, with a decision to choose for each. The authority chose on that page on 2026-11-24: *Approvo* for eight rows and *Approvo con modifica* for two, with these words.

- `M2` — «Precisare che i 15.000 ft di quota-pressione cabina dopo un guasto o malfunzionamento ragionevolmente probabile si applicano se si richiede la certificazione per operazioni sopra 25.000 ft. FL310 rientra in questo caso.»
- `M5` — «Fissare il confronto alla curva ICAO new-type 2017, alla stessa MTOM. In LC-A si registra lo scarto. A `REV-B_RELEASED` anche il limite superiore giustificato del margine deve essere ≤ −26%.»

**The working reference and the objective.** On 2026-11-20 the reviewer had put four points to the authority, after a proposal of a second reader. The authority answered on 2026-11-24:

> «per i punti 2 e 3 sono d'accordo. per il punto 4, confermo l'ambizione di almeno -26% e dammi un metodo per decidere insieme l'intervallo.»

| Point | As the reviewer put it |
|---|---|
| 1 | To approve the ten criteria, with `M5` fixed to its curve |
| 2 | To take 360 kt at 31,000 ft and the section of five abreast as working assumptions, with the altitude to be closed when the turbines are sized |
| 3 | To record a wing of about 40 m of span in flight, and to leave the brace and folding tips open |
| 4 | To confirm the moment of ruling R1 at 26 %, and to define the interval before the rule is ratified |

## The criteria as approved

| Id | Class | Text | Decision |
|---|---|---|---|
| `M1` | Mandatory | The cabin pressure altitude is not above 8,000 ft at the maximum operating altitude, in normal operation | Approved |
| `M2` | Mandatory | If certification for operation above 25,000 ft is requested, the cabin pressure altitude stays at or below 15,000 ft after any reasonably probable failure or malfunction of the pressurisation system | Approved, modified |
| `M3` | Mandatory | The requirement mission closes at the cruise point, with the reserves of ruling R2 of `KNOT-EWTW-NRG-001` | Approved |
| `M4` | Mandatory | The cruise speed is not below 360 kt true airspeed | Approved |
| `M5` | Mandatory | The carbon dioxide metric of the aircraft is at least 26 % below the new-type level of ICAO Annex 16, Volume III, first edition of 2017, at the same maximum take-off mass, and the aircraft is to better that margin where it can. At the concept baseline the gap is recorded. At the release of the preliminary-design baseline the justified upper limit of the margin is at or below −26 % | Approved, modified |
| `T2` | Tradable, first, north star | Fuel loaded on the scoring mission. Lower is better | Approved |
| `T1` | Tradable, second | Power of the gas turbines for the cruise, referred to sea level, on the take-off mass of the requirement mission. Lower is better | Approved |
| `T3` | Tradable, third | Time at cruise speed on the scoring mission. Lower is better | Approved |
| `T4` | Tradable, fourth | Inception voltage of partial discharge left at the cruise altitude, as a share of its value at sea level. Higher is better | Approved |
| `T5` | Tradable, fifth | Ideal work to compress outside air to the cabin pressure. Lower is better | Approved |

- **How the tradable criteria decide.** One separates two options only when they differ by more than 5 % of the best value; otherwise the next one decides. There are no weights.
- **The two modified texts are drafted by the reviewer** from the words of the authority. The full texts are in the [record of the KNOT](../KNOT-EWTW-CRZ-001.yaml).
- **`M5` keeps two things the modification does not name.** The aircraft is to better the margin where it can: the decision of 2026-11-18. The margin of the EU taxonomy, 11 % below the level, stays as a floor of the programme: the decision of 2026-11-16.
- **`M2` follows the rule it comes from.** CS 25.841(a) ties the 15,000 ft to the certification requested, not to the cruise point. A second reader pointed it out.

## The working reference

| | Reference, as an assumption | Stays open |
|---|---|---|
| Cruise point | 360 kt at 31,000 ft, Mach 0.614 in the standard atmosphere | The altitude, until the gas turbines are sized (`KNOT-EWTW-GEN-001`). The three options of this KNOT |
| Section | Five abreast, two and three, 3.28 m of cabin width | The section (`KNOT-EWTW-FUS-001`). Its two purposes have proposed measures and no approved criterion |
| Wing | About 40 m of span in flight | The brace, folding tips, the aspect ratio and the area (`KNOT-EWTW-WNG-001`). With fixed tips a span of 40 m is code letter D |

It is a reference and not a choice. The [path to the concept baseline](../../../README.md#path-to-the-concept-baseline-of-the-aircraft) has it as step 5: what the screening does not separate takes a reference value as an assumption. The criteria and the maturity records of this KNOT are now approved, so rule 5 of CM-004 would let its options be scored; none is scored here.

## The objective

The ambition of at least 26 % is confirmed. Criterion `M5` as approved gives it two moments: the gap is recorded at the concept baseline, and at the release of the preliminary-design baseline the justified upper limit of the margin is at or below −26 %. That release is the moment of ruling R1, fixed when the criterion stood at 11 %.

How the upper limit is built is not decided. The authority asked for a method to decide it together. One is proposed in the [review record](KNOT-EWTW-CRZ-001_reference-and-interval_2026-11-24.md) of the same day. It is not ratified.

## What this ruling does not do

- It scores and excludes no option of the cruise point, of the section or of the wing.
- It approves no criterion of `KNOT-EWTW-FUS-001` or of `KNOT-EWTW-WNG-001`. The measures proposed for comfort and for the ground for hydrogen tanks are in the review record, as proposals.
- It sets no readiness level. Records `Q1` to `Q3` still have none.
- It does not ratify the method of the interval.

## Evidence

- The [review record](KNOT-EWTW-CRZ-001_reference-and-interval_2026-11-24.md) of 2026-11-24: the proposal reproduced, the checks of the reviewer, the first budget.
- The [criteria proposal](KNOT-EWTW-CRZ-001_criteria-proposal_2026-11-15.md), issue 3, and the [screening of the configurations](CFG-EWTW-AER-001/README.md), 0.2.0.
- The page of the criteria with the choices of the authority is a document outside the repository, kept by the authority. Its choices are transcribed above.
