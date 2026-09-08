# AMPEL360-SBS-ID-CM-002 — Cross-structure identification and referencing

**Issue 1** · Owner: Q-STRUCTURES · Authority: AM.PEL · Status: **PROPOSED — merge constitutes ratification.**
Sibling of `AMPEL360-PBS-PN-CM-001` (which governs the PBS internally). CM-002 governs how the other ten breakdown structures of the SBS identify their objects and reference the PBS.

## 1. The rule

> **A breakdown structure numbers its objects after the PBS when, and only when, each object is in one-to-one correspondence with a product node. When the correspondence is many-to-many, the structure keeps a sovereign identifier space and carries a typed reference instead.**

Cardinality decides — not preference, not symmetry. And in both cases the reference is machine-resolvable: *derived id* or *typed reference*, never an unchecked prose mention.

## 2. Why the rule has two halves

**Product-indexed structures are views.** A cost object, a provisioning item, an interface dossier, a measure of a part, a maintenance data module: each has exactly one subject in the product tree. Giving it an independent number would create a second identity for one thing — the very fault CM-001 §6 forbids inside the PBS, repeated one level up. The CSN is already the crossing trace (§3.3); a view inherits it.

**Intent-indexed structures are graphs.** A function is realized by many products and a product serves many functions; a work package delivers across products and a product consumes many work packages; a risk spans items; a requirement is allocated to several and satisfied by evidence from elsewhere. Numbering these after the PBS would silently impose one-object-per-part — a function tree wearing a product costume, a work plan with one package per fitting. The allocation matrix, which is the entire value of the FBS, would collapse into a renamed BOM.

**Corollary (the mirror of CM-001 §3.1).** As no PBS artifact may claim its codes *are* S-ATLAS addresses, no structure may claim its ids *are* PBS codes. A derived id embeds the CSN because it is derived from it; it does not assert that the object is the product.

## 3. Register

| Structure | Id space | Grammar | Reference to PBS | Cardinality |
|---|---|---|---|---|
| **IBS** | derived | `eWTW-IBS-<CSN>-<counterpart>` = the ICD id (A1.9) | is the id | 1:1 with a declared interface |
| **CBS** (recurring) | derived | `eWTW-CBS-<CSN>-<item>` | is the id | 1:1 with a make/buy item |
| **CBS** (non-recurring) | sovereign | `eWTW-CBS-<WBS id>` | `incurredBy:` | n:m with work |
| **LBS** | derived | `eWTW-LBS-<CSN>-<item>` | is the id | 1:1 with a provisioned item |
| **TPMS** (product measures) | derived | `TPM-<CSN>-<MEASURE>` | is the id | 1:1 with a product scope |
| **TPMS** (programme measures) | sovereign | `TPM-PROG-<MEASURE>` | `scope:` | 1:n |
| **TPuBS** | derived by standard | S1000D DMC; SNS aligns 1:1 by number with the PBS-local code (CM-001 §9) | SNS + `ssot-ref.yaml` | 1:1 per data module subject |
| **EBS** | none (derived index) | path-addressed: evidence stays with its node (C1.5) | `subject:` (PN or act id) | index over both |
| **FBS** | sovereign | `eWTW-FBS-<n>` | `realized_by:` | **n:m** |
| **WBS** | sovereign | `eWTW-WBS-<n>-<n>` | `delivers:` | **n:m** |
| **RBS** | sovereign | `R-<CSN>-<seq>` when the risk is confined to one station, else `R-<seq>` | `affects:` | 1:1 or n:m |
| **ReqBS** | sovereign | `REQ-<level>-<seq>` | `allocatedTo:` + `satisfies:` (function) | **n:m** |

**Station-scoped dossiers (IBS).** Not every IBS document describes a joint: removal/installation envelopes and tolerance-and-datum stacks belong to a station as a whole. These carry the station CSN with a reserved alphabetic suffix instead of a counterpart — `eWTW-IBS-<CSN>-INST` and `-TOL` — so the numeric field stays unambiguously "counterpart" and the two classes never collide.

RBS is the instructive middle case: a risk confined to one station may carry the CSN for legibility (`R-533001-02`), but the field that binds is `affects:` — the day the risk widens, the id stays and the reference list grows.

## 4. Obligations

**4.1** Every reference field resolves to an existing node; a dangling reference is a preflight fatal, exactly as `REFERENCE-DANGLING` and `PBS-COUNTERPART-DANGLING` are in the PBS engines.
**4.2** Derived ids are regenerated, never typed: if the CSN changes under a ratified act, the views regenerate; sovereign ids never change.
**4.3** Coverage is derivable in both directions — product → structures (what does this station owe) and structure → products (what does this function cover) — because one side of every link is always a resolvable PBS identity.
**4.4** Views hold no engineering content that contradicts their subject: a cost object may not restate a quantity, it reads it from `part.yaml`.

## 5. Immediate consequences on the current repository

The IBS placeholder chain (`eWTW-IBS-10-…`, the ordinal x10 chain) is superseded by §3: the five radome dossiers become `eWTW-IBS-531004-<counterpart>` against the ICDs already declared on that station. The FBS keeps `eWTW-FBS-10 … 120` and repoints `realized_by` from the absent placeholder chapter code to real chapter and station ids. The WBS keeps its discipline-and-phase numbering unchanged. EBS is created as a derived index, with no numbering of its own.

<!-- Generated 2026-09-06 - GitHub Copilot - SBS rework under CM-002 -->
