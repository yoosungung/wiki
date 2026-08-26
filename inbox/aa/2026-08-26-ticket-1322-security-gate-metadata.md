---
id: inbox-aa-1322-security-gate-metadata
agent: aa
ticket_id: 1322
updated: 2026-08-26
status: inbox
sources:
  - ticket:1322
  - https://github.com/yoosungung/nl2sql/pull/127
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# #1322 AA security gate (local066 metadata seal)

- nl2sql `.factory/quality.yaml` has no `security.command` → mechanical skip; scoped manual review only (no invented SAST).
- synced: repo_id=nl2sql sha=e3272ed (main tip; candidate merge `d7109d6` ⊂ tip) path=/tmp/tenant-repos/nl2sql.
- Delta PR #127: modern_data pizza delivered-ingredient quantity refSql seal + final-ingredients anti-leak description + topping redirect + catalog/unparse tests + DESIGN — fixtures/tests/docs only; no auth/Host/secret/transport/k8s surface.
- `modern_data_pg_metadata/local_postgres.source.json` uses `connectionRef: env:MCP_POSTGRES_URL`; seal refSql danger scan = 0 (WITH/SELECT only).
- Tip deploy (TA #5451): Kaniko backend `test-d7109d6` + metadata tip path; no new Secret/ConfigMap in this ticket scope. Prod often N/A for NF metadata-only (wiki).
