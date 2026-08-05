---
id: inbox-qa-2026-08-05-spider2-full-ex-runner-env
agent: qa
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - spider2-eval/DESIGN.md
---

# Spider2 full local* EX — runner env gap

- Ticket #172 needs `spider2-opik run --task gold-sql` on all 135 `local*` (not UI E2E).
- In-cluster Opik OK: `OPIK_URL_OVERRIDE=http://opik-frontend.opik.svc.cluster.local:5173/api`, dataset `spider2-lite-local-exec` count=135.
- PG TCP OK to `postgresql.postgres.svc.cluster.local:5432`, but QA runner SA cannot read `nl2sql-secrets` / postgres secrets and has no `MCP_POSTGRES_URL` / repo `.env`.
- Next: inject `MCP_POSTGRES_URL` (hermes → spider2db) into qa agent env or mount secret; then `spider2-opik check` → full gold-sql run → report attach.
