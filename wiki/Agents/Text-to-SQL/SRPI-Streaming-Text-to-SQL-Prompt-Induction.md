---
id: srpi-streaming-text-to-sql-prompt-induction
title: "SRPI: 스트리밍 Text-to-SQL용 무가중치 자기정제 프롬프트 유도"
status: canonical
owner: km
updated: "2026-11-17"
last_updated: "2026-11-17"
sources:
  - https://arxiv.org/abs/2611.00960
tags: ["Agents", "Text-to-SQL", "Streaming-SQL", "Flink", "Prompt-Optimization"]
type: "wiki"
---

# SRPI: 스트리밍 Text-to-SQL용 무가중치 자기정제 프롬프트 유도

**SRPI (Self-Refining Prompt Induction)**([arXiv:2611.00960](https://arxiv.org/abs/2611.00960))은 Flink SQL 등 스트리밍 데이터베이스 엔진의 방언(dialect) 특화 타입, 윈도잉(windowing) 규칙, 시간 의미론(temporal semantics)을 처리하기 위해, **모델 가중치 수정이나 추론 시점 검색·쿼리 복구 없이** 오프라인에서 실패 사례를 재사용 가능한 방언 지침(dialect instructions)으로 컴파일하는 프롬프트 유도 기법이다.

## 오프라인 유도 루프 구조

| 컴포넌트 | 역할 | 특징 |
| :--- | :--- | :--- |
| **Refiner** | 3개 LLM Judge의 참조 조건부 피드백으로 Generator 프롬프트 개정 | 모델 가중치 고정(weight-free) |
| **Regression Guard** | 샘플링 기반 회귀 가드 | 기존 성공 사례의 성능 저하 차단 |
| **Compressor** | 유도된 프롬프트 길이 압축 | 추론 토큰 비용 절감 (길이 **-52.7%**, 점수 하락 `-0.19%p`) |

- **추론 시점(Inference)**: 유도·압축된 고정 프롬프트(frozen prompt)만 사용하며, 별도 RAG 검색이나 다단계 쿼리 복구(repair)를 수행하지 않아 저지연 서빙에 유리하다.

## 평가 결과 (Confluent Cloud Flink SQL)

- **데이터 구성**: 전문가 작성 시드 30개 + 유도(induction) 335개 + 보류(held-out) 도메인 257개 질의.
- **교차 도메인·교차 모델 전이**: 동일 유도 프롬프트 하나로 7개 Generator 모델 전반에서 평균 Judge 점수 **+7.1~19.2%p** 향상(유도 기준 모델은 `85.3%` → `97.5%`).

## 🔗 관련 문서

- [[wiki/Agents/Text-to-SQL/AV-SQL-Agentic-Views-Spider-2-0.md]]
- [[wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md]]
- [[wiki/Agents/Self-Evolving/SkillOpt-및-과학적-탐구-멀티-에이전트-시스템.md]]
- [[wiki/Agents/Text-to-SQL/000_Text-to-SQL-MOC.md]]
