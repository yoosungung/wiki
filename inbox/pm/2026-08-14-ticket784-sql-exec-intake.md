---
id: inbox-pm-ticket784-sql-exec-intake
agent: pm
ticket_id: 784
updated: 2026-08-14
status: inbox
sources:
  - ticket:784
  - ticket:783
  - ticket:779
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
---

# Scoreboard #784 intake (sql_exec_failed/metadata local073)

- Unassigned Blocked → assignee nl2sql, keep Blocked. Same modern_data `*.model.json` as #783 local065 → FS `<!-- blocked-by:783 -->` (not `dependingTicketId`; #779 Done parent).
- AC is `local073` only (n=14 not in scope). PG conn-closed this run n=0 — treat as MDL syntax (`near ".."`), not infra flake.
- Do not In Progress until #783 Done then clear marker. IPL (#782) and db-imdb (#781) are schema-disjoint → not blockers.
