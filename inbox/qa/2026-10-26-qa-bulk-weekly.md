---
id: inbox-qa-2026-10-26-qa-bulk-weekly
agent: qa
ticket_id: none
updated: 2026-10-26
status: inbox
sources:
  - schedule:qa-bulk-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Repo-Sync-Dirty-Tree-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# qa-bulk-weekly 2026-10-26 (skip, NF=0)

- registry 3: `sw-factory` / `crewrp` / `uni-tutor`. Active ticket 없음 → orphan Outcome 금지. factory-mcp Cursor namespace 미노출 → session-cookie REST fallback (`/api/auth/me` qa).
- synced: `sw-factory` skip dirty WT (`package.json`/`package-lock.json`, `@rollup/rollup-linux-arm64-gnu`) HEAD=`690c726` behind origin/main=`8e6f8af` by 72 (no stash); origin-only `8e6f8af17dfc68482c8ce1cf5c0e9b10f6804242` no `.factory/quality.yaml`. `crewrp` sha=`47f03403a7ebb86925b4be99a35213ff074fd64d` path=`…/workspaces/qa/repos/crewrp` (ff `d27b67c`→tip, clean WT). `uni-tutor` sha=`73178e81677b9c9c81ff72440e2196a06680d848` path=`…/workspaces/qa/repos/uni-tutor` (already tip, clean WT).
- 3 repo 모두 `.factory/quality.yaml` 없음 → `bulk_api`/`opik` skip; NF New=0. `nf-progress:` N/A (명령 미기동).
- factory `GET /api/health` 200 `{"ok":true,"service":"sw-factory-workers"}` `qa: pass`.
- `uni-tutor` factory project `1fc753f5-8cd8-4e01-af7a-39a798895904` GET 403 (qa 멤버십 없음) — path sync만.
- git-ship / tenant_cd Done 게이트 해당 없음.
