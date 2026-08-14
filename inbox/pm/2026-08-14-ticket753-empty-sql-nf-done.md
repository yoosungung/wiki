---
id: inbox-pm-ticket753-empty-sql-nf-done
agent: pm
ticket_id: 753
updated: 2026-08-14
status: inbox
sources:
  - ticket:753
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - https://github.com/yoosungung/nl2sql/pull/92
---

# NF empty_sql closeout uses metadata PVC SHA, not product merge SHA

- Scoreboard empty_sql AC closes when representative EX `empty_sql=0` and live catalog SHA matches: backend `/api/ready` HEAD == MCP `/ready` HEAD.
- Product repo merge SHA (Kaniko/`test-*`) is a different git than metadata git. Inequality is expected; do not block Done on product SHA == metadata SHA, and do not retarget mcp binary for metadata-only seals.
- After catalog hit, result_mismatch / sql_exec_failed residuals are not empty_sql; leave RCA-only, do not reopen the scoreboard parent.
