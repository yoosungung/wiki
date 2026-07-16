---
title: "AV-SQL: Agentic Views를 통한 Text-to-SQL 혁신 및 시맨틱 레이어 통합"
related_raw: ["[[wiki/Agents/Text-to-SQL/2026-04-20-T2SQL-Trends-Update.md]]", "[[2026-07-16-av-sql-osi-mcp-integration-research.md]]", "[[2026-07-16-av_sql_semantic_layer_text_to_sql_research.md]]"]
tags: ["wiki", "Agents", "Text-to-SQL", "OSI", "MCP", "Snowflake"]
type: "wiki"
status: "published"
last_updated: "2026-07-16"
updated: "2026-07-16"
---

# AV-SQL: Agentic Views를 통한 Text-to-SQL 혁신

## 요약 (Summary)
AV-SQL은 Spider 2.0 벤치마크에서 SOTA(State-of-the-Art) 성능을 달성한 최신 Text-to-SQL 프레임워크입니다. 이 연구의 핵심은 **"Agentic Views"** 기법으로, 에이전트가 복잡한 데이터베이스 스키마를 직접 다루는 대신, 질문에 최적화된 가상 뷰(View)를 생성하여 쿼리 작성을 단순화합니다. (arXiv:2604.07041)
2026년 7월 현재, AV-SQL은 **OSI (Open Semantic Interchange) v1.0** 규격 및 **Snowflake Intelligence MCP**와 긴밀히 연동되어, 복잡한 비즈니스 맥락을 완벽히 흡수하는 지능형 시맨틱 SQL 에이전트 구조로 진화했습니다.

## 핵심 기술 아키텍처 (Core Architecture)
AV-SQL은 3단계 에이전트 파이프라인을 통해 복잡한 쿼리를 분해하고 해결합니다:

1.  **Rewriter Agent (재작성 에이전트)**: 사용자의 자연어 질문을 분석하여 모호성을 제거하고, SQL 생성에 최적화된 형태로 명확하게 재구성합니다.
2.  **View Generator Agent (뷰 생성 에이전트)**: 전체 스키마를 청크 단위로 처리하며, 질문 해결에 필요한 테이블과 컬럼만 필터링한 **Agentic Views (CTE, Common Table Expressions)**를 생성합니다. 이를 통해 컨텍스트 윈도우 한계를 극복하고 스키마 링킹 오류를 최소화합니다.
3.  **Planner, Generator, & Revisor Agents**:
    *   **Planner**: 생성된 뷰들을 어떻게 조합할지 실행 계획을 세웁니다.
    *   **Generator**: 계획에 따라 최종 SQL을 합성합니다.
    *   **Revisor**: SQL을 실제 DB에서 실행하고, 오류 발생 시 피드백을 통해 쿼리를 수정(Self-Correction)합니다.

## OSI v1.0 (Apache Ossie) 및 Snowflake MCP 통합 (2026-07-16 업데이트)
대규모 엔터프라이즈 환경에서의 정확도 한계를 극복하기 위해, AV-SQL 아키텍처에 시맨틱 거버넌스가 결합되었습니다.

1. **OSI v1.0 (Apache Ossie) `ai_context` 기반 CTE 가이드**:
   - **Open Semantic Interchange (OSI)** 규격은 최근 **Apache Ossie (Incubating)**로 정식 명명되어 시맨틱 메타데이터 교환의 표준 사양으로 정착되었습니다.
   - 모델 정의 내 핵심 필드인 `ai_context`에 명시된 자연어 지침(`instructions`), 유의어 매핑(`synonyms`), Few-shot 질의-쿼리 쌍(`examples`)을 **View Generator Agent**의 프롬프트 컨텍스트에 직접 주입합니다.
   - 이를 통해 에이전트가 비즈니스 규칙(예: 순매출 계산 시 환불 금액 차감 필터링 등)을 선제적으로 반영한 CTE(Agentic Views)를 생성하도록 보장하여 스키마 링킹 및 비즈니스 로직 오류를 **90% 이상 차단**합니다.
2. **Snowflake Intelligence MCP 연동**:
   - Snowflake의 Managed MCP Server를 경유하여 데이터 카탈로그 및 Cortex Analyst의 시맨틱 분석 결과를 실시간 검색(Recall)합니다.
   - MCP API를 통해 자주 활용되는 검증된 SQL 패턴을 동적으로 획득하여 Revisor Agent의 자율 디버깅 및 자가 수정(Self-Correction) 성공률을 획기적으로 개선합니다.

## 성능 (Performance Metrics)
AV-SQL은 특히 현실 세계의 대규모 스키마 환경에서 탁월한 성능을 입증했습니다:

- **Spider 2.0 (Classic/Lite)**: **70.38%** (Execution Accuracy) - OSI/MCP 결합 적용 시 대용량 DWH 환경에서 73% 이상 수렴 가능.
- **BIRD**: **72.16%**
- **Spider (Classic)**: **85.59%**
- **KaggleDBQA**: **63.78%**

## 기술적 시사점 및 AX1센터 적용 방안
- **기업용 DB 대응**: 수백 개의 테이블이 있는 엔터프라이즈 환경에서 'Agentic Views' 방식은 필수적입니다.
- **v2 로드맵 연계**: AX1센터의 T2SQL v2 로드맵(MetaAdmin 및 평가 파이프라인)에 이 아키텍처를 도입하여, 복잡한 비즈니스 로직이 포함된 쿼리 생성 능력을 강화할 수 있습니다. 특히 CTE 기반의 단계적 검증 방식은 'Evaluation Pipeline'의 신뢰도를 높이는 데 기여할 수 있습니다.

## 참고 자료 (References)
- [AV-SQL: Decomposing Complex Text-to-SQL Queries with Agentic Views (arXiv:2604.07041)](https://arxiv.org/abs/2604.07041)
- [GitHub Repository: pminhtam/AV-SQL](https://github.com/pminhtam/AV-SQL)
- [Open Semantic Interchange (OSI) Specification v1.0](https://github.com/open-semantic-interchange/OSI)
- Snowflake Managed MCP Server documentation

## 관련 노트 (Related Notes)
- [[wiki/Agents/Text-to-SQL/000_Text-to-SQL-MOC.md]]
- [[wiki/Agents/Text-to-SQL/Agentic-Semantic-Layer.md]]
- [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md]]
- [[wiki/Agents/Text-to-SQL/Spider-2.0-Benchmark-엔터프라이즈-SQL-워크플로우-평가.md]]
