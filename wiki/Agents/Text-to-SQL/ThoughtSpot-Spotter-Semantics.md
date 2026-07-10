---
title: "ThoughtSpot Spotter Semantics: 에이전틱 시맨틱 레이어"
tags: ["T2SQL", "Semantic-Layer", "ThoughtSpot", "Agentic-AI"]
type: "wiki"
status: "published"
last_updated: "2026-04-28"
---

# ThoughtSpot Spotter Semantics

ThoughtSpot이 발표한 **Spotter Semantics**는 AI 에이전트가 비즈니스 맥락을 자율적으로 이해하고 결정론적인 SQL을 생성할 수 있도록 설계된 업계 최초의 **'에이전틱 시맨틱 레이어(Agentic Semantic Layer)'**입니다.

## 🌟 핵심 특징

### 1. 결정론적 SQL 생성 (Deterministic T2SQL)
- **검색 토큰(Search Tokens) 아키텍처**: 확률적인 LLM 생성 방식 대신, 특허받은 검색 토큰과 **TML(ThoughtSpot Modeling Language)**을 사용하여 환각(Hallucination) 없는 정확한 SQL을 생성합니다.
- **결과 신뢰성**: 모든 답변이 정의된 비즈니스 규칙을 따르므로 기업 환경에서 요구하는 데이터 신뢰성을 보장합니다.

### 2. Spotter 3 및 산업별 에이전트
- **Spotter 3**: 단순한 답변 제공을 넘어 분석 계획 수립부터 복잡한 추론까지 수행하는 자율 분석 파트너입니다.
- **Spotter for Industries**: 리테일, 금융, 생명과학 등 산업군별 특수 용어와 워크플로우를 이해하는 특화 에이전트를 제공하여 'Context Gap'을 해소합니다.

### 3. 지능형 기능
- **SpotterViz**: 자연어 프롬프트 하나로 전체 라이브보드(시각화 대시보드)를 자동 구성합니다.
- **SpotterModel**: 데이터 분석에 최적화된 시맨틱 모델(테이블 간 관계, 지표 정의 등)을 AI가 자동으로 설계합니다.
- **Aggregate Awareness**: 쿼리의 복잡도에 따라 상세 테이블 또는 사전 집계 테이블로 자동 라우팅하여 성능을 최적화하고 비용을 절감합니다.

## 🔗 에코시스템 통합
- **Snowflake 네이티브 통합**: Snowflake의 **Semantic Views**를 OSI 표준으로 직접 통합했습니다. Snowflake의 Interactive Analytics 엔진과 결합하여 서브 세컨드(Sub-second) 단위의 지표 계산 및 답변 생성이 가능합니다.
- **MCP(Model Context Protocol) 지원**: ThoughtSpot을 MCP 서버로 활용하여 Claude, GPT 등 외부 AI 에이전트가 Snowflake나 Databricks의 데이터에 안전하게 접근할 수 있도록 지원합니다.
- **Databricks 통합**: Unity Catalog Business Semantics 및 Metric Views와 네이티브하게 통합되어 단일 진실 공급원(SSOT) 역할을 수행합니다.
- **dbt 통합**: dbt MetricFlow에서 정의한 메트릭을 즉시 활용 가능합니다.

## 💡 AX1센터 R&D 인사이트
- T2SQL의 성공 핵심은 모델 자체의 성능보다 **'시맨틱 레이어'를 통한 비즈니스 맥락 주입**에 있습니다.
- 현재 개발 중인 **MetaAdmin** 및 **T2SQL MCP 서버** 설계 시, ThoughtSpot의 '검색 토큰' 기반 결정론적 접근법과 '제어 지점(Control Point)'으로서의 시맨틱 레이어 전략을 벤치마킹할 필요가 있습니다.

## 🔗 관련 문서
- [[wiki/Agents/Text-to-SQL/Agentic-Semantic-Layer]]
- [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026]]
- [[wiki/Agents/Text-to-SQL/000_T2SQL-MOC]]
