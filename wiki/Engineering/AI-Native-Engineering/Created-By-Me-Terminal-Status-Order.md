---
id: created-by-me-terminal-status-order
title: "Created-by-me: Done를 Archived 위에 (위젯 ORDER)"
status: canonical
owner: km
updated: "2026-08-06"
last_updated: "2026-08-06"
review_after: "2026-11-06"
sources:
  - ticket:266
tags: ["Engineering", "AI-Native", "Leantime", "UX", "Status"]
type: "wiki"
---

# Created-by-me: Done를 Archived 위에 (위젯 ORDER)

My Work **Created by me** 위젯이 `ORDER BY (t.status = 0) ASC`만 쓰면, Done(0)이 아닌 **모든 상태(Archived=-1 포함)**가 Done 위에 온다. 보드 `ticketlabels.sortKey`는 이 위젯을 구동하지 않는다.

## 수정 패턴

상태 그룹 순위(개념):

| 그룹 | rank | 예 |
| :--- | :--- | :--- |
| open / flow | 0 | New, In Progress, Review, … |
| Done | 1 | status=0 |
| Archived | 2 | status=-1 |

이차 정렬: `closedAt`/`modified` DESC. SQL/헬퍼명은 제품별(`STATUS_GROUP_ORDER_SQL`, `statusGroupRank`).

## 검증

- 보드 라벨 sortKey만 바꿔도 Created-by-me 순서는 안 바뀜 → **위젯 ORDER BY**를 고친다.
- 단위 테스트로 open < Done < Archived 순을 고정한다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Bridge-Agent-UserId-From-Config.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
