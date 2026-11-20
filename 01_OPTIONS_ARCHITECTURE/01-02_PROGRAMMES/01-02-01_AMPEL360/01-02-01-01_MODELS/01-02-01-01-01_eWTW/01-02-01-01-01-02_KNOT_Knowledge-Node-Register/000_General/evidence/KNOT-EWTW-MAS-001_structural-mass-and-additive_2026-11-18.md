# Research record — structural mass, topology optimisation and additive manufacturing

| | |
|---|---|
| KNOT | `KNOT-EWTW-MAS-001` Empty mass of the configuration |
| Serves | `KNU-EWTW-MAS-001-01`. It gives the methods of `-02` and the first inputs of `-03` |
| Produced by | Claude, 2026-11-18, at the request of the authority, by reading the sources named. The same hand researched and reviewed: no second reader has checked this record |
| Brief | The question of the authority of 2026-11-18: what a structure largely optimised in topology would gain, at the present and coming sizes and capacities of additive manufacturing |
| Read | Fourteen statements read at the source on 2026-11-17 and 2026-11-18, four findings of absence |

This record is a reading of public sources, written in our own words. It recommends no option. Its estimate for the eWTW is in the section of consequences, and it is arithmetic of the reviewer on two assumptions that the record names.

---

## Read at the source

### What an empty mass is made of, and how it is estimated

| # | Statement | Source | Kind |
|---|---|---|---|
| 1 | A sample breakdown of an aircraft of 73,500 kg at take-off gives the wing 10.64 % of that mass, the fuselage 10.86 %, the tail 1.76 % and the undercarriage 3.96 %: a basic structure of 27.23 %. Nacelles are 2.21 % and pylons 1.17 %. The power plant in all is 9.26 %, the fixed equipment 16.66 %, of which furnishings 8.16 %, and the operating empty mass 56.20 %. The aircraft is not named; the tool is calibrated on data of the industry that are not public | Lissys, page on the mass estimation of the Piano design tool | Calculated, calibrated |
| 2 | A first estimate takes, for transport aircraft, 49 kg for each square metre of exposed wing, 24 kg for each square metre of wetted fuselage, 27 kg for each square metre of tail, 4.3 % of the take-off mass for the landing gear and 17 % for systems and equipment | Scholz, *Aircraft Design* lecture notes, chapter 10, table 10.2, after Raymer, Hamburg University of Applied Sciences | Handbook method |
| 3 | A second method gives the mass of the fuselage from its wetted area to the power 1.2, with the dive speed, the tail arm and the sum of its width and height, and adds 8 % for a pressurised cabin. It gives the mass of the wing rising with the span, the load factor and the ratio of span to root thickness, and falling with the wing loading | The same chapter, after Torenbeek. The equations were only partly legible in the text read | Handbook method |
| 4 | A study of NASA takes composite structure as 23.5 % lighter than metal for the wing and the tail, and 14.5 % lighter for the fuselage | Nickol, *Hybrid Wing Body Configuration Scaling Study*, NASA Langley, 2012, read on 2026-11-17 | Assumption of a study |

### Topology optimisation of structure

| # | Statement | Source | Kind |
|---|---|---|---|
| 5 | The internal structure of a full-scale wing, optimised in topology at a resolution of a billion elements, is 2 to 5 % lighter than the wing designs in use, which the authors put at 40 to 200 t of fuel for each aeroplane and year. It is a computation on a supercomputer. Nothing was built | Aage, Andreassen, Lazarov and Sigmund, *Giga-voxel computational morphogenesis for structural design*, Nature 550, 2017, read on 2026-11-17 | Calculated |
| 6 | Airbus designed thirteen leading-edge ribs of the A380 by topology optimisation, in five weeks, and machined a prototype from aluminium alloy. The authors write that topology optimisation *still completely lack[s] the ability to deal with buckling criteria*, so each rib went through a sizing and shape optimisation with buckling constraints afterwards; that the truss-like results are *highly specialised* to their loads; and that the thirteen ribs came *close to the weight target*. The text read gives no mass and no saving | Krog, Tucker and Rollema, *Application of Topology, Sizing and Shape Optimization Methods to Optimal Design of Aircraft Components*, Airbus UK, as published by Altair Engineering in 2011 | Built, machined; saving not stated |
| 7 | On flat test components of 400 mm, a design by topology optimisation is 5 to 20 % lighter at equal stiffness than one drawn from engineering experience | Deng and Sun, *Optimization Design on Plate-Rib Structure for Certain Kinds of Aircraft*, ICAS 2008 | Calculated |
| 8 | A printed partition of the cabin of the A320, designed by a generative method, weighs 45 % less than the current one, 30 kg. A printed titanium bracket of the A350 is 30 % lighter than the milled part | Airbus, news of 3 March 2016, read on 2026-11-17 | Manufacturer |

### Additive manufacturing: size, rate and certification

| # | Statement | Source | Kind |
|---|---|---|---|
| 9 | Airbus has started to fit in series titanium parts made by wire deposition in the cargo door surround of the A350, up to seven metres long. The process deposits several kilograms an hour, against hundreds of grams for powder beds. The parts are machined after deposition and are *functionally and geometrically identical* to the forgings they replace: the gain claimed is in titanium and in lead time, not in mass. Wings and landing gear are named as longer-term goals | Airbus, story of 22 January 2026, read on 2026-11-17 | Manufacturer |
| 10 | The largest powder-bed machine announced has a build volume of 3,050 by 3,050 by 1,200 mm, with a height that can be extended to 5,000 mm, 100 lasers as standard, and a theoretical rate of up to 3,500 cm³ an hour. It was launched in April 2026; no delivery is reported | All3DP, 29 April 2026, on the Eplus3D EP-M3050, read on 2026-11-17 | Secondary |
| 11 | EASA classes additive parts from A, where a failure can directly affect continued safe flight and landing, to D. Its policy covers classes C and D, the parts of low and negligible criticality, and asks for early engagement for the others. It calls classes A and B *a particular challenge*, because the body of data is not yet developed, and writes that design values for complex parts are *yet to be standardised* | EASA, Certification Memorandum CM-S-008, issue 04 of 3 September 2025 | Regulator |
| 12 | Titanium alloy Ti-6Al-4V made by electron beam melting has a fatigue strength of 200 to 250 MPa at ten million cycles as built, and 550 to 600 MPa after hot isostatic pressing. The cracks start at voids left by incomplete melting, which the pressing closes | Hrabe, Gnäupel-Herold and Quinn, *Fatigue Properties of a Titanium Alloy (Ti-6Al-4V) Fabricated Via Electron Beam Melting*, NIST | Measured |

### Additive manufacturing in thermal and electrical parts

| # | Statement | Source | Kind |
|---|---|---|---|
| 13 | A printed two-phase heat exchanger, designed by simulation of tens of thousands of shapes, built and tested, improves on traditional designs by 30 to 50 % for the same power | University of Illinois Urbana-Champaign, Grainger College of Engineering, 11 March 2025, on a paper in the International Journal of Heat and Mass Transfer | Built and tested; secondary |
| 14 | A printed heat exchanger for the megawatt-class fuel cell system of the hydrogen aircraft of Airbus is in development; it was validated at laboratory scale, and its readiness is being assessed. No performance is given | 3D Printing Industry, 6 October 2025, on Conflux Technology and Airbus | Secondary |

### Findings of absence

| # | Statement |
|---|---|
| 15 | No published share of fittings, brackets and secondary structure in the structural mass of an aircraft of the class |
| 16 | No primary structure optimised in topology, built and in service, with a stated saving of mass. The one read as built gives none (statement 6) |
| 17 | No additive part of class A or B named as certified in the structure of an airliner, in what was read |
| 18 | No measured gain in power for each kilogram of an electric machine of megawatt class from additive manufacturing |

---

## What follows for the eWTW

Figures in this section are arithmetic of the reviewer.

- **What a lighter airframe is worth.** The [mission screening](MSN-EWTW-NRG-001/README.md) was run on copies with the empty mass lowered, at nominal values on the requirement mission. With 2 % less empty mass the fuel falls from 6,839 kg to 6,737 kg, by 1.5 %; with 5 % less to 6,584 kg, by 3.7 %; with 10 % less to 6,329 kg, by 7.5 %. Three quarters of a relative gain in empty mass arrive as fuel.
- **The structure is about half the empty mass.** By statement 1 the basic structure is 48 % of the operating empty mass, and 54 % with nacelles and pylons. On the 27,753 kg of the reference that is 13.5 to 15.1 t. The eWTW has another power plant, so the share is a first value only.
- **A structure largely optimised in topology gains a few per cent of it.** Primary structure that is already sized gains 2 to 5 % by computation (statement 5); small parts gain 30 to 45 % (statement 8), and no source gives their share of the structure (finding 15). Assuming that the 2 to 5 % holds for all primary structure, and that fittings and brackets are 3 to 8 % of the structure, the gain is 0.4 to 1.3 t: 1.4 to 4.7 % of the empty mass, and 1 to 3.5 % of the fuel. The two assumptions are the reviewer's.
- **The choice of material is the larger lever.** The factors of statement 4, applied to the shares of statement 1, take 8 % off the empty mass, about 6 % of the fuel. The reference type is a metal aircraft.
- **The sizes fit the small and middle parts, not the long ones.** Frames, door surrounds, ribs and fittings are within the seven metres of statement 9. Spars and skins of a wing of 34 m are not. A fine topology needs a powder bed, whose largest announced box is 3 m (statement 10), at a tenth of the rate; cutting it into segments adds joints, which cost the mass the topology saves.
- **The maturity is in two parts.** Brackets and near-net titanium blanks are in service. Primary structure optimised in topology exists as a computation (statement 5) and as machined ribs without a stated saving (statement 6), and the regulator's policy stops at parts of low criticality (statement 11). Fatigue is the reason: as built, the material has less than half the fatigue strength it has after pressing (statement 12). Under the threshold the programme keeps, level 6 at the preliminary-design baseline, this cannot be a nominal assumption. It can be a favourable case of the screening and an entry of the upgrade watch list.
- **Where additive manufacturing may pay more on this aircraft.** The one measured gain read outside structure is a heat exchanger, 30 to 50 % (statement 13), and a megawatt-class one is in development for a fuel cell system (statement 14). The eWTW rejects megawatts of heat from its electrical chain. Nothing measured is on record for the machines themselves (finding 18). This is a direction for research, not a figure.

These are consequences drawn by the reviewer. They are not quotations.

## Open

Research can still give:

- a mass breakdown by group of a named aircraft of 70 to 130 seats, and the share of fittings and brackets in it;
- the mass saved on the ribs of statement 6, in the full paper of its authors;
- named additive parts in the structure of airliners, with their class of criticality and the mass of the part they replace;
- measured results of additive heat exchangers, housings and windings at the power of megawatts.

The rest is work of the programme:

- the empty mass by option, with the methods of statements 2 and 3 checked on the reference type (`KNU-EWTW-MAS-001-02`);
- the factor on the empty mass that each structural technology is allowed, with its maturity record (`KNU-EWTW-MAS-001-03`).
