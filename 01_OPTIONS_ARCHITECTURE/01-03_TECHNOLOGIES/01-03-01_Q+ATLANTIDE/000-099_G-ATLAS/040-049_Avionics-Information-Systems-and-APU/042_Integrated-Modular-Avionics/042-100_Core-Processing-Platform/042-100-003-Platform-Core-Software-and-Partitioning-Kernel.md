# 042-100-003 — Platform Core Software and Partitioning Kernel

**Node:** 042-100_Core-Processing-Platform 

- The partitioning executive (time and space partitioning per the ARINC 653 service model) ships as a platform component with a characterized API and a declared configuration mechanism.
- Multicore enablement is a platform property: interference channels, mitigation mechanisms and configurable controls are identified and characterized at platform level, consistent with multicore certification guidance; the usage-domain evidence for each hosted set is produced under 042-400.
- Platform services exposed to partitions (health reporting hooks, time services, IO access abstractions) are versioned platform interfaces; changes follow platform configuration control.
- Core-software problem reporting and open-problem management are platform evidence items feeding the incremental-acceptance argument.

