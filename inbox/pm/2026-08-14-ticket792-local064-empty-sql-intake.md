---
id: inbox-pm-ticket792-local064-empty-sql-intake
agent: pm
ticket_id: 792
updated: 2026-08-14
status: inbox
sources:
  - ticket:792
  - ticket:789
  - ticket:781
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# Scoreboard #792 intake (empty_sql/metadata local064)

- Unassigned New → In Progress, assignee nl2sql. Standalone NF: no `dependingTicketId` to Done #789; no FS blocked-by.
- Remaining empty_sql after #781 db-imdb 3→0: bank_sales_trading reps `local064`/`local074` — AC is those two, not n=11.
- Catalog tip gap (`*.model.json` missing) → search_tables 0 → empty_sql; fix is MDL seed/vocab + metadata git push then MCP PVC SHA, not prompt hardcode.
- bank_sales_trading MDL paths are disjoint from IPL (#793), modern_data (#794), city_legislation (#795), db-imdb (#796) → parallel OK.
