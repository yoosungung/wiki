---
id: mdl-only-domain-knowledge
title: "도메인 지식은 MDL만 (에이전트 프롬프트 하드코딩 금지)"
status: canonical
owner: km
updated: "2026-08-14"
last_updated: "2026-08-14"
review_after: "2026-11-14"
sources:
  - ticket:702
  - ticket:781
  - ticket:796
tags: ["Agents", "Text-to-SQL", "MDL", "Semantic-Layer", "Prompt"]
type: "wiki"
---

# 도메인 지식은 MDL만 (에이전트 프롬프트 하드코딩 금지)

특정 스키마·조인·지표 규칙을 **시스템 프롬프트에 박으면** 새 DB마다 프롬프트를 고치고, 카탈로그와 모순이 생긴다. 교정면은 **description / `refSql` / view / relationship**이다.

## 규칙

| 넣을 곳 | 넣지 말 곳 |
| :--- | :--- |
| 모델 `description`, 컬럼 vocab, `refSql` seal, 관계 | analyst/orchestrator 시스템 프롬프트의 스키마명·지표식 |
| 카탈로그 검색 회귀 (`search_*_catalog`) | `source` 파서의 도메인 접두 특수케이스 |

오케스트레이터 예시는 `[Spider2 schema: <name>]`처럼 **플레이스홀더**. `source`/`models_used`는 snake_case 일반화.

```text
# 회귀 개념
assert "ipl_" not in analyst_system_prompt.lower()
assert "f1_" not in analyst_system_prompt.lower()
# 도메인 픽스처는 MCP search 테스트에 유지
```

프롬프트 Boy Scout로 EX를 고치려다 보면 empty_sql만 줄고 **결과 mismatch**는 남는다. grain/join/`refSql`이 정본 — [[wiki/Agents/Text-to-SQL/Composite-Grain-Join-Keys.md]], [[wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md]].

## vocab 격리

질문 키워드(“final ingredients”, “Shahrukh number”, “month-end balance”)는 **해당 seal description에만** 둔다. 베이스 카탈로그에 남겨 두면 search는 맞아도 SELECT가 베이스 grain을 고른다. 한국어-only description은 영문 벤치 질의를 `search_tables` 0으로 떨어뜨린다 — 파일 유무와 별축.

## 관련

- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
- [[wiki/Agents/Text-to-SQL/Semantic-View-Single-Master.md]]
- [[wiki/Engineering/AI-Native-Engineering/On-Demand-Schema-Describe-Tools.md]]
