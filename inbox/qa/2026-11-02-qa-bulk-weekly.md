---
id: inbox-qa-2026-11-02-qa-bulk-weekly
agent: qa
ticket_id: schedule:qa-bulk-weekly
updated: 2026-11-02
status: inbox
sources:
  - schedule:qa-bulk-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Repo-Sync-Dirty-Tree-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# qa-bulk-weekly 2026-11-02

Registry 4 repo (`sw-factory` / `crewrp` / `sql-mcp` / `rhwp_batch`; `uni-tutor` 이번 레지스트리 밖). factory-mcp Cursor namespace 미노출 → session-cookie REST fallback.

| repo_id | sync | sha | quality.yaml | bulk_api / opik |
| :--- | :--- | :--- | :--- | :--- |
| sw-factory | skip dirty (`package.json`/`package-lock.json`, no stash). HEAD `690c726` behind origin/main `8e6f8af` by 72 | HEAD `690c726` / origin `8e6f8af` | 없음 (origin/main도 부재) | skip |
| crewrp | synced | `47f03403a7ebb86925b4be99a35213ff074fd64d` | 없음 | skip |
| sql-mcp | synced | `37da5744352979d2e179513e367c0ec737817cb9` | 없음 | skip |
| rhwp_batch | synced | `642974c32716882fd96b4b5d3d74ab5fdb5fdec8` | 없음 | skip |

- `qa:` factory `GET /api/health` → 200 `{"ok":true,"service":"sw-factory-workers"}`
- NF New=0 (키 부재 = skip, 실패 아님). `nf-progress:` N/A (명령 미기동, long_run 없음).
- Ticketless schedule: no Active `ticket_id` → no orphan Outcome / no feature Done.
