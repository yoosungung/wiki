---
id: inbox-pm-ticket768-empty-sql-intake
agent: pm
ticket_id: 768
updated: 2026-08-14
status: inbox
sources:
  - ticket:768
  - ticket:767
  - ticket:753
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# Scoreboard #768 intake (empty_sql/metadata local018)

- Remaining empty_sql after #753: california_traffic_collision reps `local018`/`local017`/`local015` — AC is those three, not n=15.
- Catalog tip gap (`*.model.json` missing) → search_tables 0 → empty_sql; fix is MDL seed/vocab + metadata git push then MCP PVC SHA, not prompt hardcode.
- california_traffic MDL paths are disjoint from IPL (#769/#770) → no FS blocked-by; do not `dependingTicketId` under Done #767.
