---
id: inbox-pm-2026-10-23-roadmap-sync
agent: pm
ticket_id: schedule:pm-roadmap-sync
updated: 2026-10-23
status: inbox
sources:
  - schedule:pm-roadmap-sync
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/Development-Environment/CrewRP-Phase6-Todo-Board-Comments.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - ticket:51724bbd-8861-497d-b125-9b1e67ea2fd5
  - ticket:4c55a7df-66c0-4f40-a65e-468bbf438b8d
---

# pm-roadmap-sync 2026-10-23

- **crewrp** current=`## Phase 6 — 할 일·게시판 댓글` (1× `- [ ]` 수동 E2E). milestone reuse `51724bbd` (done, `roadmap:crewrp:milestone:phase-6-todo-board-comments`) + child `4c55a7df` (done, `roadmap:crewrp:todo-board-comment-crud-manual-e2e`) → **dedup skip `created=0`**. Doc lag: 보드 Done vs ROADMAP checkbox open → Phase 7+ blocked; pass-gate deferred. tenant_cd N/A.
- **uni-tutor** registry 있음. current would be `## 나중` LMS/LTI `- [ ]`. `GET /api/projects/1fc753f5-…` → **403** (pm not member) → skip enqueue. Human: add pm to UniTutorAI.
- factory MCP namespace 미노출 → session-cookie REST. Active ticket 없음 → orphan Outcome 미생성. ROADMAP rewrite 없음.
