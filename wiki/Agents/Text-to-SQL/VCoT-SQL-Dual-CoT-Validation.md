---
id: vcot-sql-dual-cot-validation
title: "VCoT-SQL: 이중 CoT 단계별 검증 학습 기반 Text-to-SQL"
status: canonical
owner: km
updated: "2026-11-17"
last_updated: "2026-11-17"
sources:
  - https://arxiv.org/abs/2611.00815
tags: ["Agents", "Text-to-SQL", "NL2SQL", "Chain-of-Thought", "Verification", "sLM"]
type: "wiki"
---

# VCoT-SQL: 이중 CoT 단계별 검증 학습 기반 Text-to-SQL

**VCoT-SQL**([arXiv:2611.00815](https://arxiv.org/abs/2611.00815))은 Text-to-SQL용 합성 CoT(Chain-of-Thought) 학습 데이터에서 **최종 SQL 정답만 검증**할 때 중간 추론 오류(flawed reasoning steps)가 학습 데이터를 오염시키는 문제를 해결하기 위해, **절(clause) 단위 단계별 검증**과 **이중(생성기+검증기) CoT 학습**을 결합한 프레임워크다.

## 핵심 구성 요소

1. **계층적 스키마 필터링(Hierarchical Schema Filtering)**: 상호 보완적인 검색 전략들을 결합·정제해 DB에서 질의와 관련된 핵심 스키마 요소만 정밀 추출한다.
2. **SQL 생성기 (Clause-Level CoT)**: 절 단위 CoT 템플릿을 사용하며, 각 중간 추론 단계가 **실행(execution) 및 스키마 정렬(schema alignment) 체크**로 검증된 궤적만으로 학습한다.
3. **전용 SQL 검증기 (Diagnostic CoT)**: 구문(syntactic), 의미(semantic), 타입(type) 수준 오류를 탐지하는 진단형 CoT 템플릿으로 별도 검증 모델을 학습한다.

## 핵심 시사점 (교사 크기 vs 검증 엄밀성)

- **7B 모델 기반 CoT 합성**만으로도 `72B` 규모 모델이나 비공개 상용(closed-source) 교사 모델로 합성한 기법들을 능가한다.
- 즉, Text-to-SQL 데이터 합성에서는 **교사 모델 크기 확대보다 중간 단계 검증의 엄밀성**이 더 큰 성능 레버리지로 작동한다.
- **벤치마크**: BIRD dev **66.82%** 실행 정확도(EX)(기본 7B 모델 대비 +7%p), Spider test **86.8%**.

## 🔗 관련 문서

- [[wiki/Agents/Text-to-SQL/Text-to-SQL-Reasoning-2026.md]]
- [[wiki/Agents/Text-to-SQL/sLM-Text-to-SQL-MATS-Schema-Linking-2026.md]]
- [[wiki/Agents/Text-to-SQL/Arctic-Text2SQL-R1-Reinforcement-Learning.md]]
- [[wiki/Agents/Text-to-SQL/AV-SQL-Agentic-Views-Spider-2-0.md]]
