---
id: semantic-view-single-master
title: "시맨틱 뷰는 마스터 테이블 하나"
status: canonical
owner: km
updated: "2026-08-13"
last_updated: "2026-08-13"
review_after: "2026-11-13"
sources:
  - ticket:698
  - ticket:697
tags: ["Agents", "Text-to-SQL", "MDL", "Semantic-Layer"]
type: "wiki"
---

# 시맨틱 뷰는 마스터 테이블 하나

복합 이벤트 뷰에 **조인되지 않은 두 번째 팩트**를 넣으면 번역기가 `multiple master inner tables`를 내고, execute가 실패한다. stash/SSE autofill이 있어도 **warehouse_sql이 없거나 탐색 SQL만** 나와 empty_sql로 채점된다.

## 패턴

- 뷰의 inner FROM은 **grain을 정의하는 마스터 1개** (예: ball-by-ball).
- 차원 테이블은 관계/조인으로만. 마스터와 grain이 다른 팩트(`player_match` 등)는 같은 뷰에 넣지 않는다.
- 역할 컬럼은 물리명과 의미를 맞춘다: `player_id`:=`bowler` vs `player_out`(아웃된 타자). 둘을 같은 `player_id`로 덮으면 GROUP BY가 왜곡된다.

```text
# 개념: 실패 SQL/로그
mdl_translation_error: multiple master inner tables (2)
# 조치: 미조인 팩트 드롭, master=grain 테이블, 회귀 search_*_catalog
```

stash가 execute 성공 SQL을 채워도, 번역 오류면 peek할 warehouse가 없다 — [[wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md]].

## 관련

- [[wiki/Agents/Text-to-SQL/Composite-Grain-Join-Keys.md]]
- [[wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
