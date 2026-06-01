# 01-03-01_Q+ATLANTIDE — Architecture Index

## 1. Purpose

`Q+ATLANTIDE` is the controlled architecture and taxonomy ecosystem for Q-plus-A technologies, systems, evidence, governance, lifecycle knowledge, and programme applicability.

`Q+ATLANTIDE1000` is the controlled `000–999` identification schema used inside the Q+ATLANTIDE ecosystem.

```text
Q+ATLANTIDE      = architecture-taxonomy ecosystem
Q+ATLANTIDE1000  = controlled 000–999 identification schema
```

Q+ATLANTIDE shall remain **programme-agnostic**. Programme-specific implementations, such as AMPEL360 eWTW, shall reference Q+ATLANTIDE nodes through impact studies, PBS/FBS/IBS/EBS records, S1000D/CSDB mappings, DMCs, and evidence records.

---

## 2. Controlled Folder Structure

```text
01-03_TECHNOLOGIES/
└── 01-03-01_Q+ATLANTIDE/
    ├── README.md
    ├── 000-099_ATLAS/
    ├── 100-199_STA/
    ├── 200-299_DTTA/
    ├── 300-399_DTCEC/
    ├── 400-499_EPTA/
    ├── 500-599_AMTA/
    ├── 600-699_OGATA/
    ├── 700-799_ATACV/
    ├── 800-899_CYB/
    └── 900-999_QCSAA/
```

Do not create a separate folder named:

```text
01-03-01_Q+ATLANTIDE1000/
```

`Q+ATLANTIDE1000` is the schema name, not the preferred root folder name for the technology architecture ecosystem.

---

## 3. Q+ATLANTIDE Controlled Expansion

| Segment | Expansion      | Meaning                                                                           |
| ------- | -------------- | --------------------------------------------------------------------------------- |
| `Q+`    | Quantum Plus   | Quantum, advanced, transversal, and extensible layer.                             |
| `A`     | Aerospace      | Core aerospace domain.                                                            |
| `T`     | Top            | Highest level of classification.                                                  |
| `L`     | Level          | Top-level architecture / master range.                                            |
| `A`     | Architectures  | Controlled architecture bands.                                                    |
| `N`     | Novel          | New, disruptive, or emerging technologies.                                        |
| `T`     | Technologies   | Systems, subsystems, materials, energy, digital, cyber, and quantum technologies. |
| `I`     | Identification | Technical identification, traceability, and coding.                               |
| `D`     | Data           | Structured data, metadata, evidence, CSDB / PLM.                                  |
| `E`     | Ecosystem      | Complete classification and governance ecosystem.                                 |

Controlled statement:

> **Q+ATLANTIDE** means **Quantum + Aerospace Top Level Architectures and Novel Technologies Identification and Data Ecosystem**.

---

## 4. Canonical Hierarchy

```text
Q+ATLANTIDE
└── Q+ATLANTIDE1000 Schema
    └── Architecture Band / Master Range
        └── Code Range
            └── Section
                └── Subject / Node Folder
                    └── Markdown File Set
                        └── Numbered Item / Topic
```

Programme implementation may then map applicable architecture nodes to:

```text
Programme
└── Impact Study
    └── PBS / FBS / IBS / EBS
        └── S1000D-CSDB
            └── DMC / ICN / BREX / Applicability / Evidence
```

---

## 5. Hierarchy Table

| Level                            | Definition                                                        |                                Format | Example                                   |
| -------------------------------- | ----------------------------------------------------------------- | ------------------------------------: | ----------------------------------------- |
| Q+ATLANTIDE                      | Full architecture-taxonomy ecosystem.                             |                             ecosystem | `Q+ATLANTIDE`                             |
| Q+ATLANTIDE1000                  | Controlled `000–999` schema.                                      |                             `000–999` | `Q+ATLANTIDE1000`                         |
| Architecture Band / Master Range | One 100-code architecture band.                                   |                             `000–099` | `000-099_ATLAS`                           |
| Code Range                       | Internal 10-code block inside a master range.                     |                             `000–009` | `000-009_General-Information-and-Service` |
| Section                          | Two-digit section index inside the architecture band.             |                               `00–09` | `00`                                      |
| Subject / Node Folder            | Controlled architecture node inside a code range.                 |                   `000`, `010`, `021` | `021_Air-Conditioning-and-Pressurization` |
| Markdown File Set                | Controlled files inside a node folder.                            | `<node>-<item>-<Controlled-Title>.md` | `021-000-Air-Conditioning-General.md`     |
| Item / Topic                     | Numbered content item inside a node.                              |                   `000`, `001`, `002` | `000` = General                           |
| Programme DMC Mapping            | Programme-specific S1000D/CSDB implementation of a taxonomy node. |       `DMC-<PROGRAMME>-<node>-<item>` | `DMC-AMPEL360E-EWTW-021-060`              |

---

## 6. Controlled Architecture Band Register

| Master Range | Code    | Controlled Name                                         | Scope                                                                                                          |
| -----------: | ------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
|    `000–099` | `ATLAS` | Aircraft Top Level Architecture Schema/System           | New commercial aircraft architectures, BWB, WTW, hybrid-electric, hydrogen, S1000D/CSDB/PLM integration.       |
|    `100–199` | `STA`   | Space Technology Architecture                           | Space systems, spacecraft, orbital infrastructure, launch systems, in-orbit operations.                        |
|    `200–299` | `DTTA`  | Defence Technology Type Architecture                    | Defence, dual-use boundaries, C4ISR, resilience, electronic warfare, autonomous systems.                       |
|    `300–399` | `DTCEC` | Digital Twin, Cloud, Edge and AI Architecture           | Digital twins, AI, cloud, edge, XR, blockchain, analytics, digital thread.                                     |
|    `400–499` | `EPTA`  | Energy and Propulsion Technology Architecture           | Energy systems, storage, conversion, electric propulsion, hydrogen, advanced propulsion, thermal systems.      |
|    `500–599` | `AMTA`  | Advanced Materials, Bio and Nanotechnology Architecture | Advanced materials, bio/nano systems, metamaterials, additive manufacturing, circular materials.               |
|    `600–699` | `OGATA` | On-Ground Automation Technology Architecture            | Ground automation, robotics, factories, logistics, autonomous ground systems, human-robot interaction.         |
|    `700–799` | `ATACV` | Air Traffic and Aerial City Vehicles                    | Air traffic, aerial city vehicles, UAM, vertiports, UTM, urban integration, noise, aerial mobility governance. |
|    `800–899` | `CYB`   | Cybersecurity Architecture                              | Cybersecurity, post-quantum cryptography, resilience, secure architectures, ICS/OT, cyber operations.          |
|    `900–999` | `QCSAA` | Quantum Computing and Sentient Agency Architecture      | Quantum computing, quantum sensing, quantum communications, QML, agency governance.                            |

---

## 7. Acronym Register

| Acronym | Controlled Expansion                                    |
| ------- | ------------------------------------------------------- |
| `ATLAS` | Aircraft Top Level Architecture Schema/System           |
| `STA`   | Space Technology Architecture                           |
| `DTTA`  | Defence Technology Type Architecture                    |
| `DTCEC` | Digital Twin, Cloud, Edge and AI Architecture           |
| `EPTA`  | Energy and Propulsion Technology Architecture           |
| `AMTA`  | Advanced Materials, Bio and Nanotechnology Architecture |
| `OGATA` | On-Ground Automation Technology Architecture            |
| `ATACV` | Air Traffic and Aerial City Vehicles                    |
| `CYB`   | Cybersecurity Architecture                              |
| `QCSAA` | Quantum Computing and Sentient Agency Architecture      |

---

## 8. Deprecated Terms and Supersessions

| Deprecated / Superseded          | Correct Controlled Term                               | Status           |
| -------------------------------- | ----------------------------------------------------- | ---------------- |
| `Sub-range`                      | `Code Range`                                          | Deprecated       |
| `ACV`                            | `ATACV`                                               | Superseded       |
| `Aerial City / UAM Architecture` | `Air Traffic and Aerial City Vehicles`                | Superseded label |
| `Q+ATLANTIDE1000 folder root`    | `Q+ATLANTIDE folder root with Q+ATLANTIDE1000 schema` | Corrected        |

Controlled rule:

```yaml
deprecated_terms:
  sub_range:
    replace_with: "Code Range"
    status: deprecated
  acv:
    replace_with: "ATACV"
    status: superseded
  q_atlantide1000_root_folder:
    replace_with: "01-03-01_Q+ATLANTIDE"
    status: corrected
```

---

## 9. Master Architecture Table

|                            Master Range | Architecture Code | Architecture Name                                       | Primary Focus                                                                                            |
| --------------------------------------: | ----------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [`000–099`](01-03-01-01_000-099_ATLAS/) | `ATLAS`           | Aircraft Top Level Architecture Schema/System           | New commercial aircraft architectures, BWB, WTW, hybrid-electric, hydrogen, S1000D/CSDB/PLM integration. |
|   [`100–199`](01-03-01-02_100-199_STA/) | `STA`             | Space Technology Architecture                           | Space systems, LEO+, orbital infrastructure, interplanetary concepts.                                    |
|  [`200–299`](01-03-01-03_200-299_DTTA/) | `DTTA`            | Defence Technology Type Architecture                    | Defence, C4ISR, resilience, electronic warfare, autonomous systems.                                      |
| [`300–399`](01-03-01-04_300-399_DTCEC/) | `DTCEC`           | Digital Twin, Cloud, Edge and AI Architecture           | Digital twins, AI, cloud, edge, XR, blockchain, analytics.                                               |
|  [`400–499`](01-03-01-05_400-499_EPTA/) | `EPTA`            | Energy and Propulsion Technology Architecture           | Energy, storage, conversion, electric, hydrogen, and advanced propulsion.                                |
|  [`500–599`](01-03-01-06_500-599_AMTA/) | `AMTA`            | Advanced Materials, Bio and Nanotechnology Architecture | Advanced materials, bio/nano, metamaterials, additive manufacturing.                                     |
| [`600–699`](01-03-01-07_600-699_OGATA/) | `OGATA`           | On-Ground Automation Technology Architecture            | Ground automation, robotics, factories 4.0, logistics, human-robot interaction.                          |
| [`700–799`](01-03-01-08_700-799_ATACV/) | `ATACV`           | Air Traffic and Aerial City Vehicles                    | Air traffic, aerial city vehicles, UAM, vertiports, UTM, noise, urban integration.                       |
|   [`800–899`](01-03-01-09_800-899_CYB/) | `CYB`             | Cybersecurity Architecture                              | Cybersecurity, PQC, ICS/OT, SecOps, IAM, cyber-resilience.                                               |
| [`900–999`](01-03-01-10_900-999_QCSAA/) | `QCSAA`           | Quantum Computing and Sentient Agency Architecture      | Quantum computing, QML, quantum networks, sensing, agency governance.                                    |

---

## 10. English Code Range Baseline

### 10.1 ATLAS — Aircraft Top Level Architecture Schema/System

| Code Range | English Controlled Title                    |
| ---------: | ------------------------------------------- |
|  `000–009` | General Information and Service             |
|  `010–019` | Ground Handling and Servicing               |
|  `020–029` | Core Aircraft Systems                       |
|  `030–039` | Protection and Mechanical Systems           |
|  `040–049` | Avionics, Information Systems and APU       |
|  `050–059` | Primary Structures and Programme Interfaces |
|  `060–069` | Traditional Propulsion                      |
|  `070–079` | Eco-Tech and Hybrid-Electric Propulsion     |
|  `080–089` | Alternative and Quantum Propulsion          |
|  `090–099` | Type-Specific Programmes and Expansion      |

### 10.2 STA — Space Technology Architecture

| Code Range | English Controlled Title                                 |
| ---------: | -------------------------------------------------------- |
|  `100–109` | General Space Systems and Life Support                   |
|  `110–119` | Space Structures and Materials                           |
|  `120–129` | Traditional and Advanced Space Propulsion                |
|  `130–139` | Space Energy Systems                                     |
|  `140–149` | Space Avionics and Mission Control                       |
|  `150–159` | Space Communications                                     |
|  `160–169` | Space Sensors and Payloads                               |
|  `170–179` | In-Orbit Operations and Maintenance                      |
|  `180–189` | Space Infrastructure and Logistics                       |
|  `190–199` | Advanced Space Systems, Concepts and Future Applications |

### 10.3 DTTA — Defence Technology Type Architecture

| Code Range | English Controlled Title                    |
| ---------: | ------------------------------------------- |
|  `200–209` | Combat Systems and Armament                 |
|  `210–219` | C4ISR                                       |
|  `220–229` | Protection and Resilience                   |
|  `230–239` | Defence Robotics and Autonomous Systems     |
|  `240–249` | Defence Logistics and Maintenance           |
|  `250–259` | Cyber Defence and Electronic Warfare        |
|  `260–269` | Defence Materials and Sensors               |
|  `270–279` | Military Simulation and Training            |
|  `280–289` | Quantum Warfare and Disruptive Technologies |
|  `290–299` | Future Operational Concepts                 |

### 10.4 DTCEC — Digital Twin, Cloud, Edge and AI Architecture

| Code Range | English Controlled Title                      |
| ---------: | --------------------------------------------- |
|  `300–309` | Digital Twin Foundations                      |
|  `310–319` | Sensors and IoT for Digital Twins             |
|  `320–329` | AI and Machine Learning for Digital Twins     |
|  `330–339` | Cloud Computing and Distributed Architectures |
|  `340–349` | Advanced Simulation and Modelling             |
|  `350–359` | Extended Reality and Metaverse                |
|  `360–369` | Blockchain and Decentralized Technologies     |
|  `370–379` | Cybersecurity for Digital Twins               |
|  `380–389` | Analytics and Business Intelligence           |
|  `390–399` | Conscious and Evolutive Digital Twins         |

### 10.5 EPTA — Energy and Propulsion Technology Architecture

| Code Range | English Controlled Title                 |
| ---------: | ---------------------------------------- |
|  `400–409` | Conventional and Advanced Energy Sources |
|  `410–419` | Renewable Energy                         |
|  `420–429` | Energy Storage                           |
|  `430–439` | Energy Management and Distribution       |
|  `440–449` | Combustion Propulsion                    |
|  `450–459` | Electric and Hybrid Propulsion           |
|  `460–469` | Hydrogen Propulsion and Fuel Cells       |
|  `470–479` | New Propulsion Forms                     |
|  `480–489` | Energy and Quantum Optimization          |
|  `490–499` | Energy Recovery Systems                  |

### 10.6 AMTA — Advanced Materials, Bio and Nanotechnology Architecture

| Code Range | English Controlled Title                      |
| ---------: | --------------------------------------------- |
|  `500–509` | Advanced Composite Materials                  |
|  `510–519` | Metamaterials and Smart Materials             |
|  `520–529` | Nanomaterials and Functional Coatings         |
|  `530–539` | Biotechnology and Bioengineering              |
|  `540–549` | Biomaterials and Bionics                      |
|  `550–559` | Nanotechnology and Nanorobotics               |
|  `560–569` | Advanced Bio/Nano Sensors                     |
|  `570–579` | Additive Manufacturing for Advanced Materials |
|  `580–589` | Quantum Materials and Processes               |
|  `590–599` | Material Recycling and Sustainability         |

### 10.7 OGATA — On-Ground Automation Technology Architecture

| Code Range | English Controlled Title                   |
| ---------: | ------------------------------------------ |
|  `600–609` | Industrial and Collaborative Robotics      |
|  `610–619` | Autonomous Ground Vehicles                 |
|  `620–629` | Smart Infrastructure                       |
|  `630–639` | Factories 4.0 and Advanced Manufacturing   |
|  `640–649` | Automated Logistics and Warehousing        |
|  `650–659` | Precision Agriculture                      |
|  `660–669` | Automated Construction and Demolition      |
|  `670–679` | Autonomous Services in Closed Environments |
|  `680–689` | AI and Quantum Optimization                |
|  `690–699` | Human-Robot Interaction and Safety         |

### 10.8 ATACV — Air Traffic and Aerial City Vehicles

| Code Range | English Controlled Title                         |
| ---------: | ------------------------------------------------ |
|  `700–709` | Aerial City Vehicles and Urban Air Mobility      |
|  `710–719` | Vertiports and Heliport Platforms                |
|  `720–729` | Urban Air Traffic Management                     |
|  `730–739` | Urban Noise and Acoustics                        |
|  `740–749` | Environmental Sustainability in UAM              |
|  `750–759` | Legal, Regulatory and Certification Architecture |
|  `760–769` | Urban Interface and Social Acceptance            |
|  `770–779` | Operational Safety and Resilience                |
|  `780–789` | Quantum Optimization for Traffic and Logistics   |
|  `790–799` | Business Models and Aerial Mobility Ecosystems   |

### 10.9 CYB — Cybersecurity Architecture

| Code Range | English Controlled Title                       |
| ---------: | ---------------------------------------------- |
|  `800–809` | Cybersecurity Governance and Risk Management   |
|  `810–819` | Network and Communication Security             |
|  `820–829` | Data and Storage Security                      |
|  `830–839` | Identity and Access Management                 |
|  `840–849` | Application and Software Security              |
|  `850–859` | Operational Cybersecurity                      |
|  `860–869` | Cloud and Edge Security                        |
|  `870–879` | ICS/OT Cybersecurity                           |
|  `880–889` | Post-Quantum Cryptography and Quantum Security |
|  `890–899` | Threat Intelligence and Cyber Resilience       |

### 10.10 QCSAA — Quantum Computing and Sentient Agency Architecture

| Code Range | English Controlled Title                               |
| ---------: | ------------------------------------------------------ |
|  `900–909` | Quantum Computing Foundations                          |
|  `910–919` | Quantum Machine Learning and Quantum AI                |
|  `920–929` | Quantum Networks and Communications                    |
|  `930–939` | Quantum Cybersecurity                                  |
|  `940–949` | Quantum Sensors and Metrology                          |
|  `950–959` | Quantum Simulation                                     |
|  `960–969` | Quantum Robotics and Matter Manipulation               |
|  `970–979` | Quantum Sentient Agency                                |
|  `980–989` | Governance and Ethics of AI and Quantum Sentience      |
|  `990–999` | QCSAA Future Applications and Inter-Architecture Links |

---

## 11. Programme Separation Rule

Q+ATLANTIDE is programme-agnostic.

Programme-specific folders shall not be created directly inside Q+ATLANTIDE architecture nodes unless they are explicitly labelled as examples or mappings.

Correct pattern:

```text
Q+ATLANTIDE/
└── 000-099_ATLAS/
    └── 070-079_Eco-Tech-and-Hybrid-Electric-Propulsion/
        └── 070_Hybrid-Electric-Architecture-Overview/
            └── 070-000-General.md

Programmes/
└── AMPEL360/
    └── eWTW/
        └── impact-study/
            └── Q+ATLANTIDE-mapping/
```

Controlled rule:

```yaml
programme_separation_rule:
  id: QATL-PROGRAMME-SEPARATION-001
  rule: >
    Q+ATLANTIDE defines programme-agnostic architecture nodes. Programme-specific
    implementations shall reference Q+ATLANTIDE nodes through impact studies,
    DMC mappings, PBS/FBS/IBS/EBS records, and evidence artefacts. Programme
    names, product effectivity, MSN ranges, and S1000D DMCs shall not be treated
    as native architecture definitions inside Q+ATLANTIDE.
```

---

## 12. Language Rule

The canonical architecture layer shall use English technical naming.

Legacy Spanish, Italian, or mixed-language names may remain only as historical aliases or transition references.

Controlled rule:

```yaml
language_rule:
  id: QATL-LANG-001
  canonical_language: "English"
  rule: >
    Q+ATLANTIDE architecture band names, code range names, node folder names,
    README files, and controlled taxonomy tables shall use English technical
    naming. Non-English names may be retained as deprecated aliases during
    migration but shall not be used for new controlled architecture folders.
```

---

## 13. Controlled Closure Statement

`01-03-01_Q+ATLANTIDE/README.md` defines the controlled technology architecture index for Q-plus-A.

It establishes:

* Q+ATLANTIDE as the architecture-taxonomy ecosystem;
* Q+ATLANTIDE1000 as the `000–999` schema;
* the canonical hierarchy;
* the controlled architecture band register;
* the English code range baseline;
* the supersession of `ACV` by `ATACV`;
* the separation between programme-agnostic architecture and programme-specific implementation.

This README shall be treated as the controlling architecture entry point for technology taxonomy governance.
