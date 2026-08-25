---
id: inbox-aa-1280-security-gate-metadata
agent: aa
ticket_id: 1280
updated: 2026-08-25
status: inbox
sources:
  - ticket:1280
  - https://github.com/yoosungung/nl2sql/pull/122
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# #1280 AA security gate (empty_sql metadata residual)

- nl2sql `.factory/quality.yaml` has no `security.command` → mechanical skip; scoped manual review only (no invented SAST).
- synced: repo_id=nl2sql sha=88c12f0 path=/tmp/tenant-repos/nl2sql (merge tip PR #122).
- Delta: MDL/refSql seals + catalog/PG hooks for sakila/bowlingleague/wwe/e_commerce — fixtures+tests+DESIGN only; no auth/Host/secret/transport/k8s surface.
- `local_postgres.source.json` (new schemas) use `connectionRef: env:MCP_POSTGRES_URL`; refSql danger scan = 0 (SELECT/WITH only).
- Tip deploy evidence (TA #5231): metadata FS PUT + Kaniko tip reuse `test-e7fd808` (no new Secret/ConfigMap). Ticket non-goal prod.
