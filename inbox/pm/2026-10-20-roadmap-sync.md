---
id: inbox-pm-2026-10-20-roadmap-sync
agent: pm
ticket_id: schedule:pm-roadmap-sync
updated: 2026-10-20
status: inbox
sources:
  - schedule:pm-roadmap-sync
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/Development-Environment/CrewRP-Phase6-Todo-Board-Comments.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
---

# pm-roadmap-sync 2026-10-20

- **crewrp** current=`## Phase 6 — 할 일·게시판 댓글`; open=`수동 E2E: 할 일·게시판 글에서 댓글 1회 작성·수정·삭제`.
- Dedup hit: `<!-- roadmap:crewrp:todo-board-comment-crud-manual-e2e -->` (`4c55a7df`, done) + parent `51724bbd` done → **created=0** (doc lag; ROADMAP `- [ ]` still open).
- Pass-gate / Phase 7 enqueue **deferred** until Phase 6 checkbox closed in ROADMAP.
- **uni-tutor** current=`## 나중` open LTI B2B; `GET /api/projects/1fc753f5…/tickets` → **403** → skip (same as prior ops skips).
