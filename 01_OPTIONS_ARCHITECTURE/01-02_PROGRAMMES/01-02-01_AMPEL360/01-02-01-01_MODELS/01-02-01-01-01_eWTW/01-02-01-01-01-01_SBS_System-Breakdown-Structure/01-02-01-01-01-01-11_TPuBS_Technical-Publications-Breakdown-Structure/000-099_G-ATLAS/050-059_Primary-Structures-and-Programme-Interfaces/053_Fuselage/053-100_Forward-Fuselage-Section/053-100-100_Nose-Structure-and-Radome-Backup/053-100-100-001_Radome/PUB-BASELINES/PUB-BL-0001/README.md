# PUB-BL-0001 — Radome Publication Baseline

> Publication baseline / issue record for the Radome part (`053-100-100-001`).
> Publications have their **own** release cycle, independent of engineering
> lifecycle and revision. This baseline records which engineering LC/REV states
> it is valid for — **referenced, not nested**.

| File | Purpose |
|---|---|
| `publication-baseline.yaml` | Baseline identity, issue, scope, change policy |
| `linked-engineering-baselines.yaml` | Engineering LC/REV states this baseline is valid for |
| `applicability.yaml` | Product/effectivity applicability + ACT/CCT/PCT references |
| `impact-analysis.yaml` | Whether an engineering change triggers a publication change |
| `dm-release-index.yaml` | Per-DM issue and engineering-revision linkage |

```yaml
Last.MarkedDown:
  publication_baseline_id: PUB-BL-0001
  publication_issue: "001-00"
  part: 053-100-100-001_Radome
  change_trigger: impact_analysis
  revision_link_mode: referenced_not_nested
  status: baseline
```
