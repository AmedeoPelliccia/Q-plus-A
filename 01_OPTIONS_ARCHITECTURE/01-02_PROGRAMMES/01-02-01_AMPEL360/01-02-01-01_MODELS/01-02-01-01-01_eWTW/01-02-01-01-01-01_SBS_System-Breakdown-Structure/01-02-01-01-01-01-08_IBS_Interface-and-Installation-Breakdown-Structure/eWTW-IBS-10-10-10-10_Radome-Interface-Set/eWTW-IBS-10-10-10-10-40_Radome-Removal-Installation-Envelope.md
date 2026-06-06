---
document_id: AMPEL360-eWTW-IBS-10-10-10-10-40
title: "eWTW · IBS-10-10-10-10-40 — Radome Removal/Installation Envelope"
ibs_id: eWTW-IBS-10-10-10-10-40
parent: eWTW-IBS-10-10-10-10
item_type: interface_record
interface_class: installation_envelope
serves_pbs: eWTW-PBS-10-10-10-10-10
status: draft
effectivity:
  product: eWTW
  configuration: baseline
  msn_range: MSN-001..050
  status: active
---

# eWTW · IBS-10-10-10-10-40 — Radome Removal/Installation Envelope

- **Serves PBS element:** `eWTW-PBS-10-10-10-10-10` (Radome)
- **Interface class:** Access / removal clearance — installation boundary
- **Effectivity:** eWTW · baseline · MSN-001..050 · active

## Interface definition

Controls the **physical boundary** for removing and installing the radome for radar maintenance: the swept access envelope, removal clearance and required access zone. This record defines the installation *boundary*; the installation *task* (torque sequence, step-by-step procedure) is controlled by the PUB/DM layer, not here.

| Attribute | Value |
|---|---|
| Removal motion | Hinge-swing / detach (see attachment record `…-10`) |
| Access envelope | TBD swept volume for radome + technician access |
| Removal clearance | TBD clearance to nose cap, diverters and adjacent fairings |
| No-step / no-tool zones | TBD around RF window and diverter lands |
| Controlled task (reference) | PUB DM `…-520A` (remove), `…-720A` (install) |

## Constraints

- The envelope shall allow **repeated** removal/installation without degrading RF, sealing, or bonding performance.
- Removal clearance shall not violate the tolerance/datum stack of `…-50` on re-installation.

## References

- Install/remove data modules (task) — PUB `DMC-AMPEL360E-EWTW-053-520A` (remove) and `…-720A` (install) under the Forward Fuselage Section PUB layer.
- Interface set index — [`README.md`](README.md)
