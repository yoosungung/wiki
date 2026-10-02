---
id: factory-schedule-ops-skips
title: "Factory 스케줄 ops: empty skip · registry placeholder"
status: canonical
owner: km
updated: "2026-10-03"
review_after: "2027-01-03"
sources:
  - inbox/pm/2026-10-02-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-03-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-02-sw-factory-roadmap-sync-noop.md
  - inbox/pm/2026-10-03-sw-factory-roadmap-sync-no-checklist.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
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
- 스윕 2026-10-03: sw-factory/crewrp/UniTutorAI/wiki OPEN true-issue 0; sw-factory `open_issues_count=1`은 PR#24만. `nl2sql` issues 403 → count만.
- Actions/CD 실패 감시는 이 스케줄 범위 아님(→ ta).

## roadmap-sync no-op

- Registry `git_repo_url`이 `https://github.com/example/sw-factory.git` placeholder면 ephemeral clone 실패. 실remote `yoosungung/sw-factory`; 실 `project_id`=`8a927848-4411-42a8-8508-f7b8efb3ec60`.
- sync 계약: `##` + `- [ ]`/`- [x]`만. 표·plain bullet·상태 컬럼만 → **skip: no passed section**, pass-gate 티켓 미생성. 상세: [[wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md]]
- 2026-10-03 sw-factory ROADMAP: 모든 `##`에 checkbox 0 → incomplete/passed 없음 → skip.

## Outcome 티켓

Active `ticket_id` 없는 스케줄에서 감사용 orphan Outcome 생성 금지 — [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]].  
별도 Done/New 정책이 있는 스케줄(`km-wiki` 등)은 그 계약을 따른다.
