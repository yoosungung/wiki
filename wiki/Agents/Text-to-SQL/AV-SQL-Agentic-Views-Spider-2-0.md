---
title: "AV-SQL-Agentic-Views-Spider-2-0"
related_raw: ["[[wiki/Agents/Text-to-SQL/AV-SQL-Agentic-Views-Spider-2-0.md]]"]
tags: ['wiki', 'agents_and_systems', 'text-to-sql_(t2sql)_&_analytics', 'slm_for_text-to-sql_and_schema_linking']
type: "wiki"
status: "published"
last_updated: "2026-04-20"
updated: "2026-04-20"
---

# AV-SQL: Agentic Views를 통한 Text-to-SQL 혁신

## 요약 (Summary)
AV-SQL은 Spider 2.0 벤치마크에서 SOTA(State-of-the-Art) 성능을 달성한 최신 Text-to-SQL 프레임워크입니다. 이 연구의 핵심은 **"Agentic Views"** 기법으로, 에이전트가 복잡한 데이터베이스 스키마를 직접 다루는 대신, 질문에 최적화된 가상 뷰(View)를 생성하여 쿼리 작성을 단순화합니다. (arXiv:2604.07041)

## 핵심 기술 아키텍처 (Core Architecture)
AV-SQL은 3단계 에이전트 파이프라인을 통해 복잡한 쿼리를 분해하고 해결합니다:

1.  **Rewriter Agent (재작성 에이전트)**: 사용자의 자연어 질문을 분석하여 모호성을 제거하고, SQL 생성에 최적화된 형태로 명확하게 재구성합니다.
2.  **View Generator Agent (뷰 생성 에이전트)**: **핵심 단계**입니다. 전체 스키마를 청크 단위로 처리하며, 질문 해결에 필요한 테이블과 컬럼만 필터링한 **Agentic Views (CTE, Common Table Expressions)**를 생성합니다. 이를 통해 컨텍스트 윈도우 한계를 극복하고 스키마 링킹 오류를 최소화합니다.
3.  **Planner, Generator, & Revisor Agents**:
    *   **Planner**: 생성된 뷰들을 어떻게 조합할지 실행 계획을 세웁니다.
    *   **Generator**: 계획에 따라 최종 SQL을 합성합니다.
    *   **Revisor**: SQL을 실제 DB에서 실행하고, 오류 발생 시 피드백을 통해 쿼리를 수정(Self-Correction)합니다.

## 성능 (Performance Metrics)
AV-SQL은 특히 현실 세계의 대규모 스키마 환경에서 탁월한 성능을 입증했습니다:

- **Spider 2.0**: **70.38%** (Execution Accuracy) - 기존 SOTA 갱신
- **BIRD**: **72.16%**
- **Spider (Classic)**: **85.59%**
- **KaggleDBQA**: **63.78%**

## 기술적 시사점 및 AX1센터 적용 방안
- **기업용 DB 대응**: 수백 개의 테이블이 있는 엔터프라이즈 환경에서 'Agentic Views' 방식은 필수적입니다.
- **v2 로드맵 연계**: AX1센터의 T2SQL v2 로드맵(MetaAdmin 및 평가 파이프라인)에 이 아키텍처를 도입하여, 복잡한 비즈니스 로직이 포함된 쿼리 생성 능력을 강화할 수 있습니다. 특히 CTE 기반의 단계적 검증 방식은 'Evaluation Pipeline'의 신뢰도를 높이는 데 기여할 수 있습니다.

## 참고 자료 (References)
- [AV-SQL: Decomposing Complex Text-to-SQL Queries with Agentic Views (arXiv:2604.07041)](https://arxiv.org/abs/2604.07041)
- [GitHub Repository: pminhtam/AV-SQL](https://github.com/pminhtam/AV-SQL)
- Spider 2.0 Leaderboard

## 관련 노트 (Related Notes)
- [[wiki/Agents/Text-to-SQL/000_T2SQL-MOC.md]]
- [[wiki/Agents/Text-to-SQL/Spider-2.0-Benchmark-엔터프라이즈-SQL-워크플로우-평가.md]]
