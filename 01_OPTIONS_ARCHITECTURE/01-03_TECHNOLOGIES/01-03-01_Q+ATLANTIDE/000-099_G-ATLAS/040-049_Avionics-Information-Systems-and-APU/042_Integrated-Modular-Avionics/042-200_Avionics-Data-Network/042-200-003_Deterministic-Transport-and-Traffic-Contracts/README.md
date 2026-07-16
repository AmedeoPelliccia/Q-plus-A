# 042-200-003 — Deterministic Transport and Traffic Contracts

**Node:** 042-200_Avionics-Data-Network · **Subject:** 003

- The reference transport class is switched full-duplex deterministic Ethernet of the ARINC 664 part 7 family; time-sensitive-networking profiles are tracked as a candidate evolution of the same discipline.
- Each flow operates under an ex-ante traffic contract; the network guarantees contracted flows by construction (policing at ingress, static forwarding, bounded queuing).
- End-to-end latency and jitter budgets are analyzed per contract class and demonstrated against the loaded configuration; analysis artifacts are evidence items (042-200-009).
- Integrity mechanisms (redundant transmission, sequence management, frame integrity checks) are declared per contract class.

