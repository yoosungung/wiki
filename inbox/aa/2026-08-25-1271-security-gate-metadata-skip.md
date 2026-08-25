---
id: inbox-aa-1271-security-gate-metadata-skip
agent: aa
ticket_id: 1271
updated: 2026-08-25
status: inbox
sources:
  - ticket:1271
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# #1271 AA security gate (metadata-only)

- nl2sql `.factory/quality.yaml` has no `security.command` → mechanical skip; scoped manual review only (no invented SAST).
- Delta `a9a5c2b` ⊂ tip `e7fd808`: complex_oracle MDL grain + 4 refSql seals + catalog/unparse/PG tests — no auth/Host/secret/transport surface.
- `local_postgres.source.json` uses `connectionRef: env:MCP_POSTGRES_URL`; seal SQL has no DDL/DML destructive keywords.
- Tip path already Kaniko `test-e7fd808`; this ticket’s live fix was FS metadata PUT (TA), not new Secret/ConfigMap.
