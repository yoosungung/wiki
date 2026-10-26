---
id: inbox-aa-2026-10-26-aa-clean-weekly
agent: aa
ticket_id: none
updated: 2026-10-26
status: inbox
sources:
  - schedule:aa-clean-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Repo-Sync-Dirty-Tree-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
---

# aa-clean-weekly 2026-10-26 (skip, High/Med=0)

- registry 3: `sw-factory` / `crewrp` / `uni-tutor`. Active ticket 없음 → orphan Outcome 금지. factory-mcp Cursor namespace 미노출 → session-cookie REST fallback (`/api/auth/me` aa).
- synced: `sw-factory` sha=`8e6f8af17dfc68482c8ce1cf5c0e9b10f6804242` path=`…/workspaces/aa/repos/sw-factory` (already tip, clean WT); `crewrp` sha=`47f03403a7ebb86925b4be99a35213ff074fd64d` path=`…/workspaces/aa/repos/crewrp` (ff `d27b67c`→tip, clean WT); `uni-tutor` sha=`73178e81677b9c9c81ff72440e2196a06680d848` path=`…/workspaces/aa/repos/uni-tutor` (already tip, clean WT).
- 3 repo 모두 `.factory/quality.yaml` 없음 → `clean_code:` skip; mechanical/heuristic 미실행; High/Med New=0. not a prod gate. `nf-progress:` N/A (명령 미기동).
- `uni-tutor` factory project `1fc753f5-8cd8-4e01-af7a-39a798895904` GET 403 (aa 멤버십 없음) — path sync만.
- `nl2sql`은 `repos/`에 `clean_code.command`(ruff+mypy+pytest) 있으나 `clients-repos-registry` 밖 → 본 스케줄 범위 외.
- git-ship / tenant_cd Done 게이트 해당 없음.
