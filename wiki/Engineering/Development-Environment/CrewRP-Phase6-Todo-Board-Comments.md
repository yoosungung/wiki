---
id: crewrp-phase6-todo-board-comments
title: "CrewRP Phase 6: 할 일·게시판 댓글 CRUD 수동 E2E"
status: canonical
owner: km
updated: "2026-11-14"
last_updated: "2026-11-14"
review_after: "2027-01-15"
sources:
  - inbox/crewrp/2026-11-13-phase6-comment-crud-e2e.md
  - inbox/crewrp/2026-11-13-phase6-comment-manual-e2e.md
  - inbox/pm/2026-11-13-crewrp-phase6-manual-e2e-closed.md
  - inbox/pm/2026-11-13-pm-checkpoint-crewrp-phase6-closeout.md
  - ticket:7ce664ec-722f-4020-8398-688e7a2a4b4c
  - ticket:161a162c-80f3-4e66-b27f-19df53852a25
  - inbox/pm/2026-11-11-roadmap-sync.md
  - inbox/pm/2026-11-09-roadmap-sync.md
  - inbox/pm/2026-11-08-roadmap-sync.md
  - inbox/pm/2026-11-07-roadmap-sync.md
  - inbox/pm/2026-11-03-roadmap-sync.md
  - inbox/pm/2026-11-02-roadmap-sync.md
  - inbox/pm/2026-10-31-roadmap-sync.md
  - inbox/pm/2026-10-30-roadmap-sync.md
  - inbox/pm/2026-10-29-roadmap-sync.md
  - inbox/pm/2026-10-27-roadmap-sync.md
  - inbox/pm/2026-10-26-roadmap-sync.md
  - inbox/pm/2026-10-25-roadmap-sync.md
  - inbox/pm/2026-10-24-roadmap-sync.md
  - inbox/pm/2026-10-23-roadmap-sync.md
  - inbox/pm/2026-10-21-roadmap-sync.md
  - inbox/pm/2026-10-14-roadmap-sync.md
  - inbox/pm/2026-10-15-roadmap-sync.md
  - inbox/pm/2026-10-16-roadmap-sync.md
  - inbox/pm/2026-10-17-roadmap-sync.md
  - inbox/pm/2026-10-18-roadmap-sync.md
  - inbox/pm/2026-10-19-roadmap-sync.md
  - inbox/pm/2026-10-20-roadmap-sync.md
  - ticket:51724bbd-8861-497d-b125-9b1e67ea2fd5
  - ticket:4c55a7df-66c0-4f40-a65e-468bbf438b8d
  - wiki/Engineering/Development-Environment/CrewRP-Phase5-Home-Comm-Manual-E2E.md
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - inbox/pm/2026-11-10-roadmap-sync.md
tags: ["Engineering", "DevEnv", "CrewRP", "Phase6", "E2E", "Comments"]
type: "wiki"
---

# CrewRP Phase 6: 할 일·게시판 댓글 CRUD 수동 E2E

ROADMAP current `## Phase 6 — 할 일·게시판 댓글` (2026-10-14 enqueue). Phase 5 런북: [[wiki/Engineering/Development-Environment/CrewRP-Phase5-Home-Comm-Manual-E2E.md]].

## 티켓 축

| 역할 | id | marker | 보드 (2026-11-09) |
|------|-----|--------|-------------------|
| Parent milestone | `51724bbd` | `roadmap:crewrp:milestone:phase-6-todo-board-comments` | **done** |
| Child | `4c55a7df` | `roadmap:crewrp:todo-board-comment-crud-manual-e2e` | **done** |

Done gate: child `test:` → parent Intent/`done`. `tenant_cd` N/A.

## Doc lag

- 보드 자식·milestone은 Done이나 ROADMAP `- [ ]`가 열려 있으면 sync current로 남음 → Phase 7+ enqueue 차단·pass-gate deferred (dedup `created=0`).
- **2026-10-16···11-03 sync:** 동일 doc lag → `created=0` (재enqueue 없음).
- **2026-11-07 sync:** 동일 doc lag → dedup `created=0` (재enqueue 없음).
- **2026-11-08 sync:** 동일 doc lag → dedup `created=0` (재enqueue 없음).
- **2026-11-09 sync:** 동일 doc lag → dedup `created=0` (재enqueue 없음).
- 진행을 넘기려면 ROADMAP 체크를 닫는다 — [[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]].

## 범위 (intake)

- 할 일·게시판 **댓글 CRUD** 수동 E2E (sim/device 증거는 child 티켓에 축적).

## 함정

- 시크릿·PAT 본문은 wiki에 기록하지 않는다.
- Phase 5 Discussions OAuth-scope 게이트와 별축 — Phase 6 AC는 댓글 CRUD 증거로 판정.

## Sync note 2026-11-13

- ROADMAP still Phase 6 (1× `- [ ]` 수동 E2E). Dedup markers on Done mile `7ce664ec` + child `161a162c` → roadmap-sync `created=0`. Pass-gate deferred until checkbox closed.

## Closeout 2026-11-13 (checkbox closed)

- Live CrudE2E: `ThreadTalkClient` / `DiscussionsClient` — issue + discussion comment CRUD (`yoosungung/crewrp-e2e-sandbox`; `ai-edu` NOT_FOUND for host token).
- iOS `CrudE2ETests.taskIssueCommentRoundTrip` + `discussionCommentRoundTrip` (+ Android twins). Host scopes: `repo` (+ oauth `read:org`); `project` not required for comment paths.
- ROADMAP Phase 6 last `- [ ]` → `[x]` (PR #10 merged `7a8ffbb`) — clears doc lag / pass-gate deferral; Phase 7 Study enqueue 가능.
- Popup/dialog title still binds to task/post title (empty → `새 할 일` / `새 글`); UI sim not re-run (host CrudE2E + code review).
- Board: mile `7ce664ec` + child `161a162c` Intent/`done`; FLOW empty after closeout.
