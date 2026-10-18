---
id: inbox-pm-2026-10-19-roadmap-sync
agent: pm
ticket_id: null
updated: 2026-10-19
status: inbox
sources:
  - schedule:pm-roadmap-sync
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - ticket:51724bbd-8861-497d-b125-9b1e67ea2fd5
  - ticket:4c55a7df-66c0-4f40-a65e-468bbf438b8d
---

# pm-roadmap-sync 2026-10-19

- Registry: crewrp + uni-tutor (`.cursor/roadmap-registry.json`).
- **crewrp:** current=`## Phase 6 — 할 일·게시판 댓글` (1× `- [ ]` 수동 E2E 댓글 CRUD). Milestone `51724bbd` + child `4c55a7df` (`<!-- roadmap:crewrp:todo-board-comment-crud-manual-e2e -->`) already **done** → dedup skip `created=0`. Doc lag keeps Phase 7+ blocked; pass-gate deferred until ROADMAP checkbox closed. `tenant_cd` N/A.
- **uni-tutor:** registry entry present; pm session → **403 forbidden** (not in membership) → skip enqueue. Human: add pm to UniTutorAI project `1fc753f5-…`.
- Active ticket 없음 → orphan Outcome 미생성.
- factory MCP namespace 부재 → session-cookie REST로 get_ticket 후 동일 계약.
