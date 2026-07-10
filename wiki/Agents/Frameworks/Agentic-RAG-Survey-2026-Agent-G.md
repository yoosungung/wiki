---
title: "Agentic-RAG-Survey-2026-Agent-G"
related_raw: ["[[wiki/Agents/Frameworks/Agentic-RAG-Survey-2026-Agent-G.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'agent_frameworks_and_trends']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Agentic RAG Survey 2026 & Agent-G

**출처**: [원본 링크](https://www.articsledge.com/blog/agentic-rag-survey-2026)
**날짜:** 2026-04-05
**태그:** #RAG #Agentic-RAG #LLM-Agent #Agent-G #AI-Trends

## 요약 (Summary)
2026년 RAG(Retrieval-Augmented Generation) 기술은 단순한 '검색 후 생성'의 단계를 넘어, AI 에이전트가 스스로 검색 전략을 수립하고 결과의 품질을 평가하며 반복적으로 정교화하는 **'Agentic RAG'**로 완전히 진화했습니다. 특히 **Agent-G** 프레임워크는 구조화된 지식 그래프와 비구조화된 텍스트 데이터를 지능적으로 결합하여 복잡한 다단계 추론(Multi-hop reasoning)에서 기존 방식 대비 압도적인 성능을 보여줍니다.

## 주요 기술적 특징 (Technical Highlights)
1.  **패러다임의 전환 (Naive to Agentic)**:
    *   Naive RAG → Advanced RAG → Modular RAG → **Agentic RAG**.
    *   에이전트가 검색 도구 선택, 검색 쿼리 수정, 결과 검증을 자율적으로 수행하는 '추론 파트너' 모델로 발전.
2.  **핵심 디자인 패턴**:
    *   **Reflection (자기 성찰)**: 생성된 답변의 품질을 스스로 평가하고 필요시 재검색 트리거.
    *   **Planning (계획)**: 복잡한 질문을 여러 하위 작업(Sub-tasks)으로 분해하여 해결.
    *   **Multi-agent Collaboration**: 검색, 분석, 요약 등 특화된 에이전트 간의 협업 체계.
3.  **Agent-G 프레임워크**:
    *   **Brain (LLM)**: 의사결정의 중심.
    *   **Critic Module**: 검색된 데이터의 관련성과 품질을 평가하여 교정 작업 수행.
    *   **Hybrid Extraction**: Graph DB의 구조화된 관계와 벡터 검색의 비구조화된 문맥을 통합.
4.  **성능 지표**:
    *   복잡한 추론 작업에서 기존 정적 RAG(34%) 대비 **89% 이상의 정확도** 달성.

## 기존 노트와 링크 (Related Notes)
*   [[wiki/RAG/GraphRAG-vs-LightRAG-2026]]
