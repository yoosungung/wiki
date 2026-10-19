---
id: inbox-qa-2026-10-19-qa-bulk-weekly
agent: qa
ticket_id: schedule:qa-bulk-weekly
updated: 2026-10-19
status: inbox
sources:
  - schedule:qa-bulk-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Repo-Sync-Dirty-Tree-Skip.md
---

# qa-bulk-weekly 2026-10-19

Registry 3 repo Discover — `.factory/quality.yaml` / `bulk_api`/`opik` 전무 → 게이트 미기동; NF New=0.
factory `GET /api/health` → 200 `{"ok":true,"service":"sw-factory-workers"}` → `qa: pass`.

| repo_id | sync | sha | bulk_api / opik |
| :--- | :--- | :--- | :--- |
| sw-factory | skip — dirty WT (`package.json`/`package-lock.json`; no stash) | tip `8e6f8af17dfc68482c8ce1cf5c0e9b10f6804242` (origin, no local sync) | skip — no `.factory/quality.yaml` |
| crewrp | synced | `d27b67c85718e81e95c8dc097a5b5403e004d35d` | skip — no `.factory/quality.yaml` |
| uni-tutor | synced | `73178e81677b9c9c81ff72440e2196a06680d848` | skip — no `.factory/quality.yaml` |

- Active 티켓 없음(스케줄) → orphan Outcome 코멘트 금지.
- `nf-progress:` N/A (명령 미기동).
- factory-mcp 네임스페이스 미노출; session cookie REST로 health/me만 확인. 티켓 write 없음.
