---
id: inbox-pm-ticket775-unassigned-triage
agent: pm
ticket_id: 775
updated: 2026-08-14
status: inbox
sources:
  - ticket:775
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Engineering/AI-Native-Engineering/Sessionless-MCP-Status-Label-Cache-Poison.md
  - wiki/Engineering/AI-Native-Engineering/Bridge-Agent-UserId-From-Config.md
  - bridge:/tmp/bridge.json
---

# #775 unassigned triage (Postgres memory 4Gi)

- Owner: ta (k8s Helm apply). Dual-loop In Progress is status **4** on nl2sql project (3 = New). Checkpoint once left New after claiming IP.
- AC this ticket: live `postgresql-0` limits.memory `4Gi` (fallback 2Gi only if schedule/apply blocked) + Ready + spider2db connect smoke. Shared PG FQDN: `postgresql.postgres.svc.cluster.local:5432`.
- Out of scope here: cluster-wide `statement_timeout`, nl2sql code, Prod. Eric #3777 hermesdb unused/delete — **assess only**; do not DROP on this ticket; memory bump first.
