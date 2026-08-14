---
id: refsql-seal-for-ex-mismatch
title: "EX mismatch는 refSql seal로 고정한다"
status: canonical
owner: km
updated: "2026-08-14"
last_updated: "2026-08-14"
review_after: "2026-11-14"
sources:
  - ticket:689
  - ticket:699
  - ticket:564
  - ticket:752
  - ticket:769
  - ticket:781
  - ticket:782
  - ticket:783
  - ticket:789
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
| 커리어 SUM 후 AVG vs `>=50` 카운트 | 임계가 `>` 인데 seal이 `>=` 이면 값이 어긋남 | 질문 grain 전용 모델. 기존 career 컬럼 재사용 금지 |
| 볼링 SR vs 배팅 SR | 같은 `strike_rate` 이름이 다른 분모(legal balls vs batsman_scored) | 볼링 카드는 legal balls(와이드/노볼 제외), 0-wicket 행 포함 |
| 검색 1위인데 SELECT가 카탈로그 | describe가 topping/cast grain을 고르면 seal을 안 탐 | vocab을 seal에만 두고 베이스 description에서 격리 |
| 모델명이 warehouse FROM에 누출 | `relation "…_event" does not exist` | 물리 테이블명만 FROM. MDL 이름은 검색 키 |

## 적용

1. 금 SQL을 `refSql`로 두고 모델명을 검색 프리픽스/schema_pin에 건다.
2. 메타데이터만 바꿔도 에이전트가 식을 재작성하면 **백엔드 tip 롤**이 필요하다(프롬프트가 seal을 선호하도록).
3. empty_sql(카탈로그 0)과 mismatch를 섞지 않는다 — 전자는 tip 갭 [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]. tip 파일이 있어도 **영문 vocab이 한국어-only description에 없으면** search_tables 0이다.
4. **grain 격리**: 커리어 `kind_out`·피자 가격·시즌 top-3를 다른 질문 seal에 복사하지 않는다.
5. **Opik 타입**: `compare_pandas_table`은 Python int/float만 `isclose`. PG `numeric`→Decimal은 금 int64/float64와 불일치 → 집계를 `bigint`/`double precision`/`float8`로 CAST.
6. **검색 1위 ≠ SELECT seal**: agent `k=3` 픽스처가 맞아도 describe가 베이스 카탈로그를 고르면 mismatch. SCORE_CAP에 같이 걸리면 알파벳 순이 이긴다 — [[wiki/Agents/Text-to-SQL/MCP-Search-Short-Column-Reverse-Match.md]].
7. 2-instance agent EX pass_rate=1 은 Full EX 증거가 아니다. 스코어보드는 tip live chat SSE — [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]].
8. unparser 인용·COLLATE — [[wiki/Agents/Text-to-SQL/RefSql-Unparser-Identifier-Quoting.md]].

## 관련

- [[wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md]]
- [[wiki/Agents/Text-to-SQL/MCP-Search-Short-Column-Reverse-Match.md]]
- [[wiki/Agents/Text-to-SQL/Composite-Grain-Join-Keys.md]]
- [[wiki/Agents/Text-to-SQL/RefSql-Unparser-Identifier-Quoting.md]]
- [[wiki/Agents/Text-to-SQL/Semantic-View-Single-Master.md]]
