---
id: crewrp-phase6-todo-board-comments
title: "CrewRP Phase 6: 할 일·게시판 댓글 CRUD 수동 E2E"
status: canonical
owner: km
updated: "2026-10-14"
review_after: "2027-01-14"
sources:
  - inbox/pm/2026-10-14-roadmap-sync.md
  - ticket:51724bbd-8861-497d-b125-9b1e67ea2fd5
  - ticket:4c55a7df-66c0-4f40-a65e-468bbf438b8d
  - wiki/Engineering/Development-Environment/CrewRP-Phase5-Home-Comm-Manual-E2E.md
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
tags: ["Engineering", "DevEnv", "CrewRP", "Phase6", "E2E", "Comments"]
type: "wiki"
---

# CrewRP Phase 6: 할 일·게시판 댓글 CRUD 수동 E2E

ROADMAP current `## Phase 6 — 할 일·게시판 댓글` (2026-10-14 enqueue). Phase 5 런북: [[wiki/Engineering/Development-Environment/CrewRP-Phase5-Home-Comm-Manual-E2E.md]].

## 티켓 축

| 역할 | id | marker |
|------|-----|--------|
| Parent milestone | `51724bbd` | `roadmap:crewrp:milestone:phase-6-todo-board-comments` |
| Child | `4c55a7df` | `roadmap:crewrp:todo-board-comment-crud-manual-e2e` |

Done gate: child `test:` → parent Intent/`done`. `tenant_cd` N/A. Phase 7+ blocked on current.

## 범위 (intake)

- 할 일·게시판 **댓글 CRUD** 수동 E2E (sim/device 증거는 child 티켓에 축적).
- Pass-gate는 incomplete `##`가 닫힐 때까지 deferred.

## 함정

- 시크릿·PAT 본문은 wiki에 기록하지 않는다.
- Phase 5 Discussions OAuth-scope 게이트와 별축 — Phase 6 AC는 댓글 CRUD 증거로 판정.
