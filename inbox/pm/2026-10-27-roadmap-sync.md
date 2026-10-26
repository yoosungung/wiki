---
id: inbox-pm-2026-10-27-roadmap-sync
agent: pm
ticket_id: 4c55a7df-66c0-4f40-a65e-468bbf438b8d
updated: 2026-10-27
status: inbox
sources:
  - schedule:pm-roadmap-sync
  - ticket:51724bbd-8861-497d-b125-9b1e67ea2fd5
  - ticket:4c55a7df-66c0-4f40-a65e-468bbf438b8d
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/Development-Environment/CrewRP-Phase6-Todo-Board-Comments.md
---

# pm-roadmap-sync 2026-10-27

- crewrp current remains `## Phase 6 — 할 일·게시판 댓글` (1× `- [ ]` 수동 E2E 댓글 CRUD). Parent `51724bbd` + child `4c55a7df` already **done** (`<!-- roadmap:crewrp:todo-board-comment-crud-manual-e2e -->`) → dedup skip `created=0`. Phase 7+ blocked; pass-gate deferred until ROADMAP checkbox closed. `tenant_cd` N/A.
- uni-tutor current `## 나중` LMS/LTI `- [ ]` 1×; pm GET project `1fc753f5-…` still **403** → skip enqueue. Human: add pm membership to UniTutorAI.
- No Active `ticket_id` on this schedule → no orphan Outcome comment. factory-mcp Cursor namespace absent; session-cookie REST used (read parent+child before skip).
