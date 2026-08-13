---
id: mcp-search-short-column-reverse-match
title: "검색 스코어링: 짧은 컬럼 역매칭을 끈다"
status: canonical
owner: km
updated: "2026-08-13"
last_updated: "2026-08-13"
review_after: "2026-11-13"
sources:
  - ticket:564
tags: ["Agents", "Text-to-SQL", "MCP", "Search", "Schema"]
type: "wiki"
---

# 검색 스코어링: 짧은 컬럼 역매칭을 끈다

`score_column`이 `token.contains(col)` **역매칭**을 허용하면 1글자 컬럼(`g`, `a`, `e`)이 스키마 토큰(`baseball`) 안에 타서 **엉뚱한 팩트 테이블**이 1위로 오른다. 질문은 batting인데 fielding이 상위가 되는 전형.

## 가드

| 규칙 | 요지 |
| :--- | :--- |
| 역매칭 최소 길이 | `col` 길이 &lt; 4이면 `token.contains(col)` 무시 |
| 스키마 필터 | 스키마가 이미 핀이면 쿼리에서 중복 스키마 토큰을 제거 |
| 스키마-only 쿼리 | `{schema} stats`처럼 키워드가 빈약하면 질문 키워드로 enrich |
| 다양성 | fact+dimension이 한 묶음에 오도록 token-coverage / `k` 3–4 |

커리어 합 vs 시즌 MAX처럼 **집계 grain 오류**는 검색 랭킹과 별축이다. 검색이 맞아도 analyst가 시즌 row `MAX(g)`를 내면 mismatch — [[wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md]].

## 관련

- [[wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
- [[wiki/Engineering/AI-Native-Engineering/On-Demand-Schema-Describe-Tools.md]]
