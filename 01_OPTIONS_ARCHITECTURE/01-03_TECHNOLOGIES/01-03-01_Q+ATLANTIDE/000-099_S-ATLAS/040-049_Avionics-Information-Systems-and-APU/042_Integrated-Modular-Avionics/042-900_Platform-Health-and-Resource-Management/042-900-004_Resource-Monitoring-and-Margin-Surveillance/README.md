# 042-900-004 — Resource Monitoring and Margin Surveillance

**Node:** 042-900_Platform-Health-and-Resource-Management · **Subject:** 004

- Observed resource use (processing time, memory, network bandwidth, IO refresh) is compared at runtime against the budgets allocated in 042-400.
- Margin erosion below declared thresholds raises maintenance events before it raises operational ones — surveillance exists to buy time, not to assign blame.
- Persistent budget violation by a hosted function triggers the declared containment consequence for that function, never a silent rebudget: budget changes are configuration events (042-400-005).

