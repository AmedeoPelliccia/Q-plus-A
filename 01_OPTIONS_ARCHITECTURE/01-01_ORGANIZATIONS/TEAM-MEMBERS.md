# Q+A Team Members Registry

> **Authoritative source:** [`TEAM-MEMBERS.csv`](TEAM-MEMBERS.csv) is the single source of truth for all Q+A organizational division memberships. This Markdown file is a human-readable representation of that registry. In the event of any discrepancy, the CSV record governs.

## Governance notice

- Membership in a Q+A division does **not** create an employment, commercial or legal relationship between the member and Q+A, its contributors or its associated programmes.
- Membership does **not** grant automatic authority to modify controlled architecture, part-number spaces, breakdown structures or technical publication nodes.
- Technical work still requires an approved work-package issue referencing a controlled product or architecture node.
- The registry is maintained by the repository owner and architecture authority, **Amedeo Pelliccia** (`@AmedeoPelliccia`).

For the membership request process, see [CONTRIBUTING.md](../../../CONTRIBUTING.md).

---

## Registry

| Member ID | GitHub user | Display name | Division | Role | Competencies | Status | Approval issue | Joined |
|---|---|---|---|---|---|---|---|---|
| QTEAM-0001 | [@AmedeoPelliccia](https://github.com/AmedeoPelliccia) | Amedeo Pelliccia | ALL-DIVISIONS | steward | aerospace systems engineering; product architecture; technical publications; configuration management; AI and quantum computing; programme governance; organizational architecture | ACTIVE | N/A — repository owner | 2024-01-01 |

---

## Adding a new member

1. Open a GitHub issue titled `[DIVISION MEMBERSHIP] <GitHub username> — <division code and name>`.
2. Await approval from the repository architecture authority.
3. Once approved, the next `member_id` is assigned and the row is added to `TEAM-MEMBERS.csv`.
4. This Markdown file is updated to reflect the new row.
5. The initial status is set to `APPROVED` or `ACTIVE`.

A contributor may **not** add themselves directly to the registry without an approved membership issue.

---

## Status values

| Status | Meaning |
|---|---|
| `APPROVED` | Membership approved; contributor not yet active |
| `ACTIVE` | Currently active member |
| `INACTIVE` | Member not currently contributing |
| `WITHDRAWN` | Member has withdrawn from the division |
| `SUSPENDED` | Membership temporarily suspended |
