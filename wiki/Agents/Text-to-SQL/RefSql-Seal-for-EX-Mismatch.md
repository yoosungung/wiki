---
id: refsql-seal-for-ex-mismatch
title: "EX mismatch는 refSql seal로 고정한다"
status: canonical
owner: km
updated: "2026-08-13"
last_updated: "2026-08-13"
review_after: "2026-11-13"
sources:
  - ticket:689
  - ticket:699
  - ticket:564
tags: ["Agents", "Text-to-SQL", "MDL", "refSql", "Evaluation"]
type: "wiki"
---

# EX mismatch는 refSql seal로 고정한다

카탈로그 히트·SQL 방출이 되어도 **집계 정의가 금과 다르면** pass_rate=0이다. 에이전트가 매번 올바른 식을 재발명하길 기대하지 말고, 반복 질의는 **warehouse `refSql`을 가진 시맨틱 모델**로 봉인한다.

## 전형

| 실패 모양 | 원인 | seal |
| :--- | :--- | :--- |
| 커리어 합 vs 시즌 MAX | 시즌 row `MAX(g)` vs 선수 `SUM(g)` | career 합 모델 + 이름 컬럼 vocab |
| `date_part(YEAR\|MONTH\|DAY)` 평균 | 독립 성분 평균 ≠ `AGE` 성분 후 AVG (tol ~1e-2) | span 모델 refSql = gold AGE |
| LAG 위치 + 빈 pit/retirement | 금은 합성 뷰. 에이전트 SQL은 조인 깨짐(NOT EXISTS, bigint↔text, IS NOT NULL이 LEFT JOIN 제거) | overtake 모델 refSql = gold; thin lap 모델은 검색 핀만 |

## 적용

1. 금 SQL을 `refSql`로 두고 모델명을 검색 프리픽스/schema_pin에 건다.
2. 메타데이터만 바꿔도 에이전트가 식을 재작성하면 **백엔드 tip 롤**이 필요하다(프롬프트가 seal을 선호하도록).
3. empty_sql(카탈로그 0)과 mismatch를 섞지 않는다 — 전자는 tip 갭 [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]].

## 관련

- [[wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md]]
- [[wiki/Agents/Text-to-SQL/MCP-Search-Short-Column-Reverse-Match.md]]
- [[wiki/Agents/Text-to-SQL/Composite-Grain-Join-Keys.md]]
