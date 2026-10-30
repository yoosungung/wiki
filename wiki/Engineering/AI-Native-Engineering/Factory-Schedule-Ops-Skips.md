---
id: factory-schedule-ops-skips
title: "Factory 스케줄 ops: empty skip · registry placeholder"
status: canonical
owner: km
updated: "2026-10-31"
review_after: "2027-01-15"
sources:
  - inbox/pm/2026-10-31-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-31-roadmap-sync.md
  - inbox/pm/2026-10-30-roadmap-sync.md
  - inbox/pm/2026-10-29-roadmap-sync.md
  - inbox/pm/2026-10-27-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-27-roadmap-sync.md
  - inbox/pm/2026-10-26-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-26-roadmap-sync.md
  - inbox/pm/2026-10-25-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-25-roadmap-sync.md
  - inbox/pm/2026-10-24-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-24-roadmap-sync.md
  - inbox/pm/2026-10-23-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-23-roadmap-sync.md
  - inbox/pm/2026-10-22-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-21-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-21-roadmap-sync.md
  - inbox/pm/2026-10-02-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-03-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-04-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-05-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-06-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-07-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-08-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-09-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-10-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-12-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-13-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-14-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-15-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-16-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-17-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-18-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-19-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-20-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-04-roadmap-sync-no-next.md
  - inbox/pm/2026-10-04-roadmap-next-enqueue.md
  - inbox/pm/2026-10-05-roadmap-sync.md
  - inbox/pm/2026-10-06-roadmap-sync.md
  - inbox/pm/2026-10-07-roadmap-sync.md
  - inbox/pm/2026-10-08-roadmap-sync.md
  - inbox/pm/2026-10-09-roadmap-sync.md
  - inbox/pm/2026-10-10-roadmap-sync.md
  - inbox/pm/2026-10-12-roadmap-sync.md
  - inbox/pm/2026-10-13-roadmap-sync.md
  - inbox/pm/2026-10-14-roadmap-sync.md
  - inbox/pm/2026-10-15-roadmap-sync.md
  - inbox/pm/2026-10-16-roadmap-sync.md
  - inbox/pm/2026-10-17-roadmap-sync.md
  - inbox/pm/2026-10-18-roadmap-sync.md
  - inbox/pm/2026-10-19-roadmap-sync.md
  - inbox/pm/2026-10-20-roadmap-sync.md
  - inbox/pm/2026-10-04-crewrp-phase3-pass-freeze.md
  - inbox/pm/2026-10-02-sw-factory-roadmap-sync-noop.md
  - inbox/pm/2026-10-03-sw-factory-roadmap-sync-no-checklist.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
  - wiki/Engineering/Development-Environment/CrewRP-Phase5-Home-Comm-Manual-E2E.md
  - wiki/Engineering/Development-Environment/CrewRP-Phase6-Todo-Board-Comments.md
tags: ["Engineering", "AI-Native", "Factory", "Schedules"]
type: "wiki"
---

# Factory 스케줄 ops: empty skip · registry placeholder

## github-issue-check

클라이언트 true-issue **open 전수 0** → `created=0` / **explicit skip** (실패 아님).  
검증 축: `gh list` / REST(`pr==null`) / GQL OPEN / `open_issues_count`.  
레거시: [[wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md]]

- pm `clients-repos-registry` empty면 wiki client map + `agents.yaml` repos 재사용 (맵 부재≠실패).
- factory projects 예: `sw-factory`, `CrewRP`, `UniTutorAI` (nl2sql 프로젝트 없을 수 있음).
- 스윕 2026-10-03···**19**: sw-factory/crewrp/UniTutorAI/wiki/codingland/candidate.win OPEN true-issue 0; sw-factory `open_issues_count=1`은 PR만(true-issue 제외); crewrp `open_issues_count=0`. `nl2sql` issues ACL/token 403 → `open_issues_count=0`만 확인·변환 티켓 미생성.
- **2026-10-15** factory projects (pm session): `sw-factory`, `CrewRP` only (uni-tutor membership 없음 — 403과 동일 축).
- **2026-10-16** same: true-issue 0 across crewrp/sw-factory/UniTutorAI/nl2sql/wiki/codingland; sw-factory `open_issues_count=1` PR-only; factory projects CrewRP+sw-factory only; `clients-repos-registry` empty → agents.yaml+wiki map; orphan Outcome 미생성.
- **2026-10-17···31** same: OPEN true-issue 0 (sw-factory/crewrp/sql-mcp/nl2sql/wiki/UniTutorAI/codingland/candidate.win); sw-factory `open_issues_count=1`은 PR#24만; factory ACL sw-factory+CrewRP+sql-mcp (UniTutorAI membership 없음); registry empty → agents.yaml+wiki map; orphan Outcome 미생성. factory-mcp Cursor namespace 미노출 시 session-cookie REST fallback (pm 2026-10-21···31). **2026-10-26···31:** env `GH_TOKEN` 401 → keyring fallback (sweep 성공; 시크릿 미기록).
- Active `ticket_id` 없는 스케줄 → orphan Outcome 티켓 미생성([[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]).
- Actions/CD 실패 감시는 이 스케줄 범위 아님(→ ta).

## roadmap-sync no-op

- Registry `git_repo_url`이 `https://github.com/example/sw-factory.git` placeholder면 ephemeral clone 실패. 실remote `yoosungung/sw-factory`; 실 `project_id`=`8a927848-4411-42a8-8508-f7b8efb3ec60`.
- sync 계약: `##` + `- [ ]`/`- [x]`만. 표·plain bullet·상태 컬럼만 → **skip: no passed section**, pass-gate 티켓 미생성. 상세: [[wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md]]
- 2026-10-03 sw-factory ROADMAP: 모든 `##`에 checkbox 0 → incomplete/passed 없음 → skip.

## roadmap-sync ops (2026-10-04···19)

- Registry: `crewrp`, `uni-tutor` only (sw-factory not in `pm.roadmaps[]` when table-only).
- **crewrp 2026-10-04···10:** Phase 1–3 all `- [x]`; Eric chose freeze (option 2) → `<!-- roadmap-pass:approved -->` + maintenance only; incomplete 0 → freeze no-op; pass-gate `f9f2416a` already `done`.
- **crewrp 2026-10-12:** current=`## Phase 4 — 소통 = Discord 계정 연동` → milestone `012deff8` + child `6beb03a9` (`roadmap:crewrp:discord-oauth-app-server-channel-keys-manual-e2e`); Phase 5/6 blocked on current. Discord 수동 E2E: [[wiki/Engineering/Development-Environment/CrewRP-Discord-OAuth-Manual-E2E.md]].
- **crewrp 2026-10-13:** current=`## Phase 5 — 소통 허브 + 홈 README` → milestone `10fe0055` + child `d13290fa` (`roadmap:crewrp:home-readme-comm-category-manual-e2e`); Phase 6 blocked. 수동 E2E: [[wiki/Engineering/Development-Environment/CrewRP-Phase5-Home-Comm-Manual-E2E.md]].
- **crewrp 2026-10-14:** current=`## Phase 6 — 할 일·게시판 댓글` → milestone `51724bbd` + child `4c55a7df` (`roadmap:crewrp:todo-board-comment-crud-manual-e2e`); Phase 7+ blocked. 티켓 축: [[wiki/Engineering/Development-Environment/CrewRP-Phase6-Todo-Board-Comments.md]].
- **crewrp 2026-10-15:** current still Phase 6 (1× `- [ ]` 수동 E2E). Milestone `51724bbd` + child `4c55a7df` already **done** → dedup skip / `created=0`. Doc lag: ROADMAP checkbox open → Phase 7+ blocked; pass-gate deferred until checkbox closed. `tenant_cd` N/A.
- **crewrp 2026-10-16···23:** still Phase 6 (1× `- [ ]` 수동 E2E 댓글 CRUD). Parent `51724bbd` + child `4c55a7df` already **done** → dedup skip `created=0`. Doc lag keeps Phase 7+ blocked; pass-gate deferred until ROADMAP checkbox closed.
- **uni-tutor 2026-10-05:** `## 나중` with 2× `- [ ]` → reuse milestone `f8d92c00`; child Editor/Roommate `66ac47e7`; LMS marker already done (`4aa8d43d`) even if ROADMAP checkbox lags.
- **uni-tutor 2026-10-06···13:** `## 나중` still current with **1×** `- [ ]` (LMS/LTI); milestone reuse `f8d92c00`; LMS marker `4aa8d43d` (doc lag) → enqueue skip / `created=0`; pass-gate deferred until checkbox closed.
- **uni-tutor 2026-10-14···23:** registry entry present but pm session → **403 forbidden** (not in pm membership) → skip enqueue (실패 아님). Prior LMS ticket `4aa8d43d` GET → 404 (inaccessible/purged). Human: add pm to UniTutorAI project `1fc753f5-…`. Local `agents.yaml` pm.roadmaps는 crewrp-only일 수 있음.
- zsh heredoc 함정: `[x]`/`###` glob → JSON 파일로 API body 작성.
- factory MCP namespace 부재 시 session-cookie REST로 동일 계약 수행(쓰기 전 get_ticket).

## Outcome 티켓

Active `ticket_id` 없는 스케줄에서 감사용 orphan Outcome 생성 금지 — [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]].  
별도 Done/New 정책이 있는 스케줄(`km-wiki` 등)은 그 계약을 따른다.
