---
id: inbox-pm-ticket793-local258-intake
agent: pm
ticket_id: 793
updated: 2026-08-14
status: inbox
sources:
  - ticket:793
  - ticket:789
  - ticket:782
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - inbox/qa/2026-08-14-ticket789-scoreboard-delta.md
---

# Scoreboard #793 intake (result_mismatch/metadata local258)

- Unassigned New → In Progress, assignee nl2sql. Standalone NF: no `dependingTicketId` to Done #789/#779/#782; no FS blocked-by (first remaining IPL after #782 local021 PASS).
- #789 Full EX pass_rate 0.3259; residual IPL mismatch local258/025/023/020. AC is `local258` only (siblings not this PR).
- IPL MDL is disjoint from #794 modern_data, #796 db-imdb, #795 city_legislation, #792 empty_sql — parallel OK; do not wire blocked-by across those files. Do not copy #782 over50-avg or #769 kind_out onto other IPL grain.
