---
title: "DeepAgent: T2SQL을 위한 지능형 에이전트 프레임워크"
related_raw: ["[[raw/2026-04-18-Semantic-Layer-and-DeepAgent-T2SQL]]", "[[raw/2026-04-19-T2SQL-Semantic-Layer-Metadata-RAG-Trend]]", "[[raw/2026-04-19-T2SQL-Opik-Semantic-Layer-DeepAgent-Trends]]", "[[raw/2026-04-20-T2SQL-Trends-Summary]]"]
tags: ["wiki", "T2SQL", "DeepAgent", "Agentic-Workflow"]
type: "wiki"
status: "published"
last_updated: "2026-04-20"
---

# DeepAgent 기반 T2SQL 구현

DeepAgent는 LLM의 추론 능력과 도구 사용(Tool Use)을 극대화하여 복잡한 비즈니스 질의를 처리할 수 있게 돕는 에이전트 프레임워크입니다. 2026년 현재, 단일 프롬프트 방식을 넘어선 **멀티 에이전트 협업 구조**가 엔터프라이즈 표준으로 자리 잡았습니다.

## 🌟 주요 프레임워크 및 동향

### 1. LangChain Deep Agents (2026.04 출시)
- **개념**: 복잡한 계획(Planning), 도구 호출, 상태 관리를 자동화하는 차세대 에이전트 프레임워크입니다.
- **특징**: '에이전트 하네스' 기능을 통해 여러 전문 에이전트를 조립하고, 장기 기억(Long-term Memory)과 자가 교정 루프를 표준화된 인터페이스로 제공합니다.

### 2. 표준 멀티 에이전트 워크플로우
1. **Schema Agent**: 수천 개의 컬럼 중 질문과 관련된 15~20개 내외의 핵심 메타데이터만 동적으로 필터링 (Schema Pruning).
2. **Planner Agent**: 질문 의도를 분석하고 시맨틱 레이어의 메트릭/차원을 활용하여 CoT(Chain-of-Thought) 기반의 쿼리 실행 계획 수립. (추천: **Gemini 3.1 Pro**)
3. **SQL Agent**: 계획에 따라 시맨틱 API를 호출하거나 SQL 생성. (추천: **Qwen 2.5 Coder 7B/32B**)
4. **Validator/Fix Agent**: 생성된 SQL을 실행하고 오류 발생 시 피드백을 통해 스스로 수정 (Self-Correction).

### 3. 주요 성과
- **Spider 2.0 성능**: 에이전트 워크플로우 도입 시 정확도가 대폭 향상됩니다. 특히 **Databao Agent**는 dbt 프로젝트 환경에서의 워크플로우 최적화를 통해 Spider 2.0-DBT 벤치마크에서 **1위**를 기록했습니다 (2026.02).

## 🌟 핵심 기능 및 기술

### 1. 계층적 탐색 (Hierarchical Discovery)
- **방식**: 대규모 스키마에서 단순 RAG 검색 대신, 에이전트가 **[DB -> 스키마 -> 테이블 -> 샘플 데이터]** 순으로 단계적으로 메타데이터를 탐색합니다.
- **장점**: 토큰 비용을 최대 85% 절감하며, 질문과 무관한 테이블로 인한 혼선을 방지합니다.

### 2. 자율적 메모리 폴딩 (Autonomous Memory Folding)
- **설명**: 사용자와의 긴 대화 이력을 '에피소드 메모리'로 압축하여 관리하여 컨텍스트 유지력과 토큰 효율성을 동시에 확보합니다.

### 3. 평가 및 관측 (Evaluation & Observability)
- **Opik (Comet)**: 에이전트의 사고 과정(Trace)을 실시간으로 기록하고 병목 지점을 시각화하여 최적화 루프를 지원합니다.
- **G-Eval (LLM-as-a-Judge)**: 자연어 가이드라인에 기초하여 생성된 SQL의 비즈니스 정합성을 평가합니다.

## 🔗 관련 문서
- [[wiki/Agents/Text-to-SQL/Semantic-Layer]]
- [[wiki/Agents/Frameworks/MCP/MCP-Integration]]
- [[T2SQL_Planning]]
- [[wiki/Agents/Text-to-SQL/sLM-for-T2SQL]]
- [[wiki/Engineering/AI-Native-Engineering/Coder-Models-2026]]
- [[wiki/Agents/Text-to-SQL/Spider-2.0]]
