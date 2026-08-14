---
id: inbox-pm-ticket781-empty-sql-intake
agent: pm
ticket_id: 781
updated: 2026-08-14
status: inbox
sources:
  - ticket:781
  - ticket:779
  - ticket:768
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# Scoreboard #781 intake (empty_sql/metadata local100)

- Remaining empty_sql after #768 california_traffic PASS: db-imdb reps `local100`/`local098`/`local096` — AC is those three, not n=13.
- Catalog tip gap (`*.model.json` missing) → search_tables 0 → empty_sql; fix is MDL seed/vocab + metadata git push then MCP PVC SHA, not prompt hardcode.
- db-imdb MDL paths are disjoint from IPL (#782) and modern_data (#783/#784) → no FS blocked-by; do not `dependingTicketId` under Done #779.
