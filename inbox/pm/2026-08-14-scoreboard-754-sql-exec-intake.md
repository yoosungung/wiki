---
id: inbox-pm-scoreboard-754-sql-exec-intake
agent: pm
ticket_id: 754
updated: 2026-08-14
status: inbox
sources:
  - ticket:754
  - ticket:751
  - ticket:752
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
---

# Scoreboard #754 intake (sql_exec_failed/metadata)

- Cluster sql_exec_failed/metadata n=14; AC is IPL reps `local259` (`relation "br" does not exist`) and `local228` (generated rel col), not full n=14.
- Same IPL `*.model.json` as #752 IPL slice → FS `blocked-by:752` until #752 Done; do not PUT IPL MDL in parallel.
- Domain fix stays in tip MDL (`description` / `refSql` / view / relationship); do not hardcode unknown relation names in agent prompts.
- Do **not** `dependingTicketId` link under Done parent #751.
