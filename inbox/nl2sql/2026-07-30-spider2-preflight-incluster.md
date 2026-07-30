---
id: inbox-nl2sql-spider2-preflight-incluster
agent: nl2sql
ticket_id: 32
updated: 2026-07-30
status: inbox
sources:
  - ticket:32
  - spider2-eval/DESIGN.md
  - wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md
---

# Spider2 #37 preflight — in-cluster endpoints (sw-factory)

- Runner DNS search=`sw-factory.svc.cluster.local` → short `k8s-test` / `opik.k8s-test` fail; use ClusterIP FQDN.
- PG: `postgresql.postgres.svc.cluster.local:5432`
- Opik: `OPIK_URL_OVERRIDE=http://opik-frontend.opik.svc.cluster.local:5173/api`
- Dataset `spider2-lite-local-exec` was orphaned on deleted Opik project id; recreate project `nl2sql` then `spider2-opik-upload-exec` (135 items).
- Verified 2026-07-30: `spider2-opik check` OK; `gold-sql` smoke `local008,local022` → `spider2_exec_match` avg 1.0 / pass_rate 1.0.
