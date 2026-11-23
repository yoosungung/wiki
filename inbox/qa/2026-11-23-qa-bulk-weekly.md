---
id: inbox-qa-2026-11-23-qa-bulk-weekly
agent: qa
ticket_id: 90701013-54c4-49e9-93c9-39adea1ceb4a
updated: 2026-11-23
status: inbox
sources:
  - ticket:90701013-54c4-49e9-93c9-39adea1ceb4a
  - schedule:qa-bulk-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Repo-Sync-Dirty-Tree-Skip.md
---

# qa-bulk-weekly 2026-11-23

- Registry 8 repos: sync OK 7 (sw-factory/crewrp/sql-mcp/rhwp_batch/candidate.win/uni-semantic/scanbooks); aura sync blocker (ahead 125 / behind 174, unrelated histories — no force).
- Discover: 전 클라이언트 `.factory/quality.yaml` 없음 → `bulk_api`/`opik` skip · opik-eval N/A · Factory `GET /api/health` 200 `qa: pass` · NF New=0.
- Pattern reuse: Tenant-Quality-Yaml-Gate-Skip-Pattern (missing yaml ≠ fail).
