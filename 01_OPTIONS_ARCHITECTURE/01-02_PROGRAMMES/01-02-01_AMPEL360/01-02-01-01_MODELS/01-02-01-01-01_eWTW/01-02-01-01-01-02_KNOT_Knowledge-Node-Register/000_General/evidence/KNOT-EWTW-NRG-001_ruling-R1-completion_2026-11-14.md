# Decision record — completion of ruling R1 of the energy carrier

| | |
|---|---|
| KNOT | `KNOT-EWTW-NRG-001` Energy carrier |
| Ruling | R1, 2026-11-07: liquid hydrogen allocated to the BWB-Q100; option D, cryogenic hydrogen, excluded |
| Authority | AM.PEL — architecture authority |
| Completed | 2026-11-14, with rationale and evidence, once (CM-004, rule 7) |
| Restated | 2026-11-16, by the authority, before the merge: the last sentence. The draft said that the eWTW keeps a tube-and-wing fuselage; the authority states that its architecture lies between a conventional tube-and-wing and a blended wing body |
| Drafted by | Claude, from statements already in the repository, when the authority approved the order of work in the session of 2026-11-14 |
| Ratified | By the merge of the pull request that carries this record. **Until the merge the authority can replace the rationale. After it the ruling is not rewritten** |
| Closes | `KNU-EWTW-NRG-001-07` Rationale and evidence of ruling R1, on ratification |

The statement of 2026-11-07 is unchanged: the eWTW is all-electric, or hybrid-electric with conventional fuel; liquid hydrogen is allocated to the BWB-Q100. Ruling R2 has since excluded the all-electric option.

---

## Rationale

> The exclusion is a decision of allocation within the family of models. It is not the result of a comparison of carriers on this airframe: no trade of liquid hydrogen on the eWTW is on record, and none is claimed. The family carries liquid hydrogen in one model, the BWB-Q100. For the same energy liquid hydrogen needs about four times the volume of kerosene, which moves its storage out of the wing, and the place of the tanks then drives the centre of gravity. The eWTW is the model with a wide tube and a wing, an architecture between a conventional tube-and-wing and a blended wing body, for 100 passengers. Its geometry is not yet on record, and the family defines it on the carriers that do not need that volume.

## Evidence

Each sentence rests on a statement that was in the repository before this record, except the one the authority restated on 2026-11-16.

| Sentence | Where it is on record |
|---|---|
| The family carries liquid hydrogen in one model, the BWB-Q100 | [Models of the programme](../../../../README.md): the BWB-Q100 is the model assigned liquid hydrogen. [Model README](../../../README.md), section 5: scope narrowed on 2026-11-07 |
| Liquid hydrogen needs about four times the volume of kerosene, which moves storage out of the wing | [Root README](../../../../../../../../README.md), architecture delta, row 2 |
| The place of the tanks drives the centre of gravity | Same table, row 1 |
| The eWTW is the model with a wide tube and a wing, between a conventional tube-and-wing and a blended wing body, for 100 passengers | Stated by the authority on 2026-11-16. The model README names the configuration Wide Tube and Wing and gives 100 passengers; it does not define the wide tube |
| Its geometry is not yet on record | A search of the model README and of the product tree: no cross-section, no cabin, no wing and no drag polar. The one envelope on record is that of the aft fuselage, a concept assumption (`KNOT-EWTW-DAT-001`) |
| No trade of liquid hydrogen on the eWTW is on record | A search of the register and of the model README: no analysis, no research record and no KNU sizes hydrogen for this airframe |

## What the completion says and what it does not

- **It is an allocation, and it says so.** The rationale does not claim that hydrogen fails on this airframe; a wide tube may well hold more than a narrow one, and no record measures it. It records that the family places it elsewhere, and the two physical facts that make the placement a change of airframe and not of equipment.
- **The evidence is one-sided.** The README of the BWB-Q100 is not written yet, so the model that receives hydrogen does not state it. That node is a protected area.
- **It changes nothing in the option set.** Option D has been excluded since 2026-11-07, and with it the fuel cells of `KNOT-EWTW-SRC-001`.
- **It makes the two exclusions an auditable basis.** Until now they stood on the statement alone, and no KNOT could be ruled on them (rule 4). The architecture relations take the state of the ruling and now read `COMPLETE`.
- **The reopen condition is recorded** in `reopen_if`: the programme allocates liquid hydrogen to the eWTW, or the BWB-Q100 leaves the family of models.
- **One coupling stays as it was.** `KNOT-MRTT-CMA-001` targets commonality with the eWTW family under a liquid-hydrogen baseline, a premise the eWTW does not offer. It is for the MRTT-Q300 model to revisit.
