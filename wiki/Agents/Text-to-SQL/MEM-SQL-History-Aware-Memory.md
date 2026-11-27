---
id: mem-sql-history-aware-memory
title: "MEM-SQL: 검증된 SQL 이력 메모리 + HARE 벤치"
status: canonical
owner: km
updated: "2026-11-28"
last_updated: "2026-11-28"
review_after: "2027-02-28"
sources:
  - https://arxiv.org/abs/2611.18338
tags: ["Agents", "Text-to-SQL", "NL2SQL", "Memory", "HARE", "Schema-Linking"]
type: "wiki"
---

# MEM-SQL: 검증된 SQL 이력 메모리 + HARE 벤치

**MEM-SQL**([arXiv:2611.18338](https://arxiv.org/abs/2611.18338), 2026-11)은 동일 DB에서 **이미 검증된 SQL 이력**을 재사용·조합해 새 질문을 푸는 Text-to-SQL 메모리 프레임이다. 질문은 독립 평가가 아니라 이력 적응으로 보고, 벤치 **HARE**(History-AwaRe Text-to-SQL BEnchmark, 1,600 요청 · 823 검증 쿼리 풀)로 정확도·비용을 함께 측정한다.

## 핵심 메커니즘

1. **3층 메모리**: whole-query 템플릿 · 재사용 SELECT 블록 · 도메인 개념↔스키마 매핑. 각 항목은 검색 가능 description + SQL/매핑.
2. **Coverage-gated routing**: 요구사항별로 후보를 검색하고, 해당 층의 **모든** 요구가 threshold 이상일 때만 그 층을 증거로 채택(강한 한 건이 미커버 요구를 가리지 않음).
3. **On-demand Schema Linking (OSL)**: 층이 하나도 자격 없거나 generator가 증거 부족으로 판단할 때만 스키마 링킹 — 매 턴 full schema 주입 회피.
4. **HARE 카테고리**: rephrase · parametric · component-parametric · structural · shared joins · shared concepts(+ composite). 실행 가능만으로 통과시키지 않고 이력 보존 관계까지 검증.

## 시사점

- 6 LLM 평균 EX: Direct(이력 없음) **37.1%** → MEM-SQL **50.0%**; 입력 토큰 **−76.6%**, 지연 **−68.8%**(평균).
- 다수 검증 쿼리를 새 구조·공유 join으로 합치는 요청은 병목(정확도 56.7%→29.7%). 템플릿이 정확도에, 블록이 조합에 기여.
- OSL을 다른 메모리 설계에 이식하면 비용은 일관 감소, 정확도 이득은 메모리 설계에 의존.
- AskWise/DisGuAD와 축이 다름: MEM-SQL은 **검증 이력 재사용·스키마 지연**, AskWise는 실행·수리 증명, DisGuAD는 생성기 앞단 명확화 선택. 공장 NL2SQL/SQL-MCP에는 “검증된 쿼리 템플릿·블록을 coverage gate로만 주입 + 스키마는 on-demand” 패턴을 재사용.
- 코드/아티팩트: 논문 페이지 참고 ([arXiv:2611.18338](https://arxiv.org/abs/2611.18338)).

## 🔗 관련 문서

- [[wiki/Agents/Text-to-SQL/000_Text-to-SQL-MOC.md]]
- [[wiki/Agents/Text-to-SQL/AskWise-Execution-Guided-Clarification.md]]
- [[wiki/Agents/Text-to-SQL/DisGuAD-Disagreement-Guided-Ambiguity.md]]
- [[wiki/Agents/Text-to-SQL/Metadata-RAG.md]]
