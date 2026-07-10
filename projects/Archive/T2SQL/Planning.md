---
title: T2SQL v2 고도화 및 평가 체계 구축 로드맵
related_raw:
tags:
  - wiki
  - T2SQL
  - planning
  - roadmap
type: wiki
status: published
last_updated: 2026-04-19
---

# T2SQL 고도화 로드맵 (2026.Q2 - Q3)

본 문서는 엔터프라이즈 환경의 복잡한 데이터 구조를 효과적으로 처리하고, 높은 신뢰도의 SQL 생성을 위한 전략적 기술 로드맵을 정의합니다.

## 🚀 주요 목표
1. **데이터 자산화**: LLM이 데이터를 이해할 수 있도록 비즈니스 메타데이터와 세만틱 모델 구축.
2. **에이전틱 추론**: DeepAgent 기반의 다단계 추론 및 자가 교정(Self-Correction) 프로세스 도입.
3. **지속적 검증**: 엔터프라이즈급 성능 평가 체계 확립.

## 검색
    - **검색 키워드**: `G-Eval`, `Semantic layer`, `DeepAgent`, `Metadata RAG`, `DPO GRPO`
    - **탐색 채널**: `ArXiv`, `Medium`, `LinkedIn`, `GitHub`
    
## 📅 단계별 상세 계획

### 1단계: 데이터 자산화 및 세만틱 기반 구축 (Foundation)
*목표: LLM이 비즈니스 맥락을 정확히 파악할 수 있는 지식 기반 마련*
- **메타데이터 강화**: 주요 테이블/컬럼에 대한 비즈니스 설명(Description) 및 도메인 지식(Glossary) 자산화.
- **세만틱 모델링 (Measurement Governance)**: dbt 또는 Cube 연동 혹은 [[wiki/Agents/Text-to-SQL/Semantic-Layer-DeepAgent-Filesystem|DeepAgent Filesystem 방식]]을 통해 '매출', '이탈률' 등 복잡한 계산 로직을 사전에 정의하고 캡슐화. (LLM 정확도 최대 300% 향상 가능)
- **온톨로지 결합**: 데이터 간의 의미와 관계(Meaning)를 정의하는 온톨로지 구조를 시맨틱 레이어 하단에 결합하여 복잡한 추론 지원.
- **지능형 스키마 프루닝 (Metadata RAG)**: 질문의 의도에 따라 수천 개의 컬럼 중 필요한 정보만 동적으로 추출하여 컨텍스트 최적화. (참조: [[wiki/Agents/Text-to-SQL/Metadata-RAG|Metadata RAG 가이드]])

### 2단계: DeepAgent 기반 지능형 워크플로우 (Intelligence)
*목표: 복잡한 다단계 질의 해결 및 생성 결과의 신뢰성 확보*
- **Execute-Check-Refine 루프**: 생성된 쿼리를 실행하고 결과를 확인한 뒤 스스로 수정하는 **멀티 에이전트 검증** 구조를 표준 아키텍처로 채택.
- **Multi-Agent 추론 구조**: Planner(Gemini 3.1 Pro) - SQL(Qwen 2.5 Coder) - Validator(DeepSeek V4) 등 모델별 특성을 고려한 3단계 에이전트 워크플로우 구축.
- **sLM 평가 및 파인튜닝 (Coder-8B Focus)**: Qwen2.5-Coder-7B/8B 등 최신 Coder 계열 8B급 모델을 T2SQL 전용 벤치마크로 평가하고, 실무 도메인 데이터셋(Schema-Query Pair)을 활용한 파인튜닝을 통해 SQL 생성 성능 및 도메인 적응력을 극대화.
- **자율적 메모리 관리 (Memory Folding)**: 긴 대화 과정에서 핵심 의사결정 맥락을 '에피소드 메모리'로 압축하여 토큰 효율성 및 컨텍스트 유지력 강화.

### 3단계: 지능형 평가 및 고도화 (Optimization)
*목표: 객관적 지표 기반의 성능 측정 및 지속적 개선 루프 완성*
- **엔터프라이즈 성능 측정**: 대규모 스키마(700+ 테이블) 및 멀티 다이얼렉트 환경에서의 성능 측정(Execution Accuracy).
- **에이전틱 자기 교정 루프**: 실행 오류 피드백을 통해 쿼리를 자동 수정하는 루프를 평가 체계와 통합.
- **성능 모니터링 파이프라인**: 모델 업데이트 시 자동으로 평가를 수행하고 성능 변화를 추적하는 CI/CD 연동.

## 🔗 관련 문서
- [[wiki/Agents/Text-to-SQL/Spider-2.0]]
- [[wiki/Agents/Text-to-SQL/Semantic-Layer]]
- [[wiki/Agents/Text-to-SQL/Metadata-RAG]]
- [[wiki/Agents/Text-to-SQL/Semantic-Layer-DeepAgent-Filesystem]]
- [[wiki/Agents/Text-to-SQL/DeepAgent-T2SQL]]
- [[wiki/Engineering/AI-Native-Engineering/Coder-Models-2026]]
- [[wiki/Agents/Text-to-SQL/sLM-for-T2SQL]]
- [[연구_주제_관리]]
