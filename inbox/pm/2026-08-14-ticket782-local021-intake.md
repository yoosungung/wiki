---
id: inbox-pm-ticket782-local021-intake
agent: pm
ticket_id: 782
updated: 2026-08-14
status: inbox
sources:
  - ticket:782
  - ticket:779
  - ticket:769
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - inbox/nl2sql/2026-08-14-ticket779-local021-full-ex-residual.md
---

# Scoreboard #782 intake (result_mismatch/metadata local021)

- Unassigned New → In Progress, assignee nl2sql. Standalone NF: no `dependingTicketId` to Done #779/#769; no FS blocked-by (first remaining IPL).
- #769 2-instance EX pass_rate 1.0 is not Full EX evidence: #779 still mismatch `sql_len=4536`. Live MCP PVC SHA ≠ product git SHA; do not copy career `kind_out` onto season/peek grain.
- IPL MDL is disjoint from #781 db-imdb and #783/#784 modern_data — parallel OK. AC is `local021` only (siblings 258/229/025/023/020 not this PR).
