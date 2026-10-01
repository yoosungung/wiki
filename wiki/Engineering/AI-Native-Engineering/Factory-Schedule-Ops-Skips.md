---
id: factory-schedule-ops-skips
title: "Factory 스케줄 ops: empty skip · registry placeholder"
status: canonical
owner: km
updated: "2026-10-02"
review_after: "2027-01-02"
sources:
  - inbox/pm/2026-10-02-github-issue-check-empty-skip.md
  - inbox/pm/2026-10-02-sw-factory-roadmap-sync-noop.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
tags: ["Engineering", "AI-Native", "Factory", "Schedules"]
type: "wiki"
---

# Factory 스케줄 ops: empty skip · registry placeholder

## github-issue-check

클라이언트 true-issue **open 전수 0** → `created=0` / **explicit skip** (실패 아님).  
검증 축: `gh list` / REST(`pr==null`) / GQL OPEN / `open_issues_count`.  
레거시 Leantime intake 패턴: [[wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md]]

- 스윕 예(2026-10-02): sw-factory, crewrp, UniTutorAI, codingland, candidate.win — 모두 0.
- `yoosungung/nl2sql` issues REST/GQL **403** (`open_issues_count=0`만 확인) → 토큰/ACL 점검.
- pm `clients-repos-registry` empty면 wiki client map + `agents.yaml` repos 재사용 (맵 부재≠실패).

## roadmap-sync no-op

- Registry `git_repo_url`이 `https://github.com/example/sw-factory.git` placeholder면 ephemeral clone 실패. 실remote는 `yoosungung/sw-factory`.
- sync 계약: `##` 섹션의 `- [ ]`/`- [x]`만. 표·plain bullet·상태 컬럼만 있으면 current/passed section 없음 → skip ("no passed section"), 티켓 0.
- Active `ticket_id` 없는 스케줄에서 factory IO가 막히면 **orphan Outcome 티켓 생성 금지** (별도 Done/New 정책이 있는 스케줄은 그 계약을 따름).
