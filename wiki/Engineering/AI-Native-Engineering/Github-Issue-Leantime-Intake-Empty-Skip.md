---
id: github-issue-leantime-intake-empty-skip
title: "GH issue→Leantime intake: open 0이면 explicit skip"
status: canonical
owner: km
updated: "2026-09-01"
last_updated: "2026-09-01"
review_after: "2026-11-30"
sources:
  - schedule:github-issue-check
  - ticket:942
  - ticket:279
  - ticket:344
  - ticket:359
  - ticket:343
  - ticket:370
  - ticket:373
  - ticket:386
  - ticket:521
  - ticket:533
  - ticket:518
  - ticket:575
  - ticket:571
  - ticket:1535
  - ticket:1574
  - inbox/pm/2026-08-31-github-issue-check-empty-skip.md
  - inbox/pm/2026-09-01-github-issue-check-empty-skip.md
tags: ["Engineering", "AI-Native", "GitHub", "Leantime", "Intake"]
type: "wiki"
---

# GH issue→Leantime intake: open 0이면 explicit skip

클라이언트 레포(`gh issue list --state open`)가 **0건**이면 티켓을 만들지 않고 **explicit skip**을 스케줄/감사 티켓에 남긴다. 실패로 올리지 않는다.

## 절차

1. 레지스트리 클라이언트 전수 `gh issue list --state open`.
2. open=0 → skip 코멘트(점검 범위·lookback 포함). blocker 없음.
3. open>0 → **매칭 클라이언트 Leantime project**에 변환(QA가 repro/시나리오 첨부 가능).
4. Dedup 마커: 본문에 `<!-- github:owner/repo#N -->`.

## 클라이언트 맵 (2026-09-01)

| project_id | repo | 비고 |
|------------|------|------|
| 5 | `yoosungung/sw-factory` | gh list + REST true Issues |
| 6 | `yoosungung/nl2sql` | all-time 16건 모두 closed |
| 7 | `berryking404/candidate.win` | REST |
| 8 | `yoosungung/codingland` | gh list + GraphQL OPEN + REST `pull_request==null` |

lookback `2026-08-31T23:01Z` ~ `2026-09-01T23:01Z` 구간 open=0이면 created=0·explicit skip(실패 아님).

## 스킵 축

- 이미 closed된 과거 이슈를 QA 버그로 재오픈하지 않는다.
- MCP discovery 실패 시 JSON-RPC fallback으로 seal 가능 — [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]].
- 레지스트리 JSON이 없어도 **직전 클라이언트 맵을 재사용**해 open=0 skip을 남긴다. 맵 부재를 실패로 올리지 않는다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
