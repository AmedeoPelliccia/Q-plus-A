# 042-200-600 — Network Configuration and Data Loading

**Node:** 042-200_Avionics-Data-Network · **Subject:** 006

- The network configuration (contract tables, forwarding tables, policing parameters, domain filters) is a single, versioned, consistency-checked data set: one network, one configuration state.
- Configuration generation is tool-supported and rule-checked; generation rules and checks are themselves controlled items.
- Loading, configuration reporting and version verification follow the onboard-maintenance interfaces (REF 045).
- Change control: any contract change re-runs the determinism analysis of 003 before release; partial loads are prohibited by doctrine.

