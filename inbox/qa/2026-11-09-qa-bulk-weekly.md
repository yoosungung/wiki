---
id: inbox-qa-2026-11-09-qa-bulk-weekly
agent: qa
ticket_id: null
updated: 2026-11-09
status: inbox
sources:
  - schedule:qa-bulk-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Repo-Sync-Dirty-Tree-Skip.md
---

# qa-bulk-weekly 2026-11-09 — all clients skip (no bulk_api/opik)

- Schedule `qa-bulk-weekly`: tenant-repo-sync 6/6 OK, then Discover `bulk_api`/`opik` for bulk-api-probe / opik-eval.
- Registry paths under qa workspace `repos/`: sw-factory, crewrp, sql-mcp, rhwp_batch, aura, candidate.win.
- Sync evidence (ff-only; dirty 없음 → stash 없음):
  - synced: repo_id=sw-factory sha=7c8fcdb87695d5b000c6157ce8d142f69286e461
  - synced: repo_id=crewrp sha=47f03403a7ebb86925b4be99a35213ff074fd64d
  - synced: repo_id=sql-mcp sha=cb98bc853d3ceb1e357dc7022ddd0d937fdb211e
  - synced: repo_id=rhwp_batch sha=9e10cc98172c671a647ace39c8a34dcaadd1c5d8
  - synced: repo_id=aura sha=0dcc2f4e949941b70b7728ea018aea5b3e8291f2
  - synced: repo_id=candidate.win sha=8bf26bf385ea3a7079d3ac7d0a5c31b8ddbfa273
- Per client: no `.factory/quality.yaml` → no `bulk_api`/`opik` → **skip** (NF 미생성). Tenant probe/eval not run.
- Factory smoke (bulk-api-probe soft): `GET https://factory.askwho.net/api/health` → 200 `{"ok":true,"service":"sw-factory-workers"}` → `qa: pass`.
- NF New tickets: 0. `nf-progress:` N/A (mechanical 명령 미기동).
- Ticketless schedule (no Active ticket_id) → orphan Outcome 금지; outcome = this inbox only.
- Feature Done / tenant_cd gate: N/A (`tenant-cd-registry.json` 부재). factory-mcp Cursor namespace 미노출 → session-cookie REST fallback.
