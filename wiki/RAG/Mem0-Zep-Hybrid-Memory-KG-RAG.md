---
title: Mem0-Zep-Hybrid-Memory-KG-RAG
related_raw:
  - "[[wiki/RAG/Mem0-Zep-Hybrid-Memory-KG-RAG]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
type: wiki
status: draft
last_updated: "2026-04-19"
---

# Mem0 & Zep: Hybrid Memory with Knowledge Graphs

**출처**: [원본 링크](https://www.mem0.ai/blog)
**날짜:** 2026-04-05
**태그:** #Memory-Framework #Knowledge-Graph #LLM-Agent #Mem0 #Zep #Graphiti

## 요약 (Summary)
2026년 AI 에이전트의 메모리 관리 시스템은 단순 벡터 저장소를 넘어, **지식 그래프(Knowledge Graph)**와 **시계열 분석**을 결합한 하이브리드 아키텍처로 진화하고 있습니다. **Mem0**와 **Zep**은 사용자의 과거 맥락과 관계를 지능적으로 보존하여 에이전트의 일관성과 추론 능력을 극대화하는 대표적인 프레임워크입니다.

## 주요 기술적 특징 (Technical Highlights)
1.  **Mem0 (Hybrid Memory)**:
    *   벡터 검색과 그래프 아키텍처를 결합하여 사용자 정보의 ADD, UPDATE, DELETE 작업을 지능적으로 수행.
    *   기존 방식 대비 토큰 사용량을 90% 이상 절감하면서도 고도의 정확도 유지.
2.  **Zep (Graphiti)**:
    *   'Graphiti' 라이브러리를 통해 **시계열 지식 그래프(Temporal Knowledge Graph)** 구축.
    *   사용자의 과거 대화 맥락을 시간 흐름에 따라 파악하여 장기 기억의 선후 관계를 명확히 이해.
3.  **Knowledge Extraction**:
    *   비구조화된 대화 데이터에서 엔티티와 관계를 자동으로 추출하여 동적으로 그래프 업데이트.
4.  **에이전트 개인화**:
    *   사용자의 취향, 과거 결정 내역 등을 그래프 상의 노드로 관리하여 진정한 의미의 '개인화된 AI' 구현.

## 기존 노트와 링크 (Related Notes)
*   Resources/03_Knowledge_Memory/Knowledge-Graph/Memory-Cognition/Memory-Cognition
*   Resources/03_Knowledge_Memory/Knowledge-Graph/GraphRAG-Implementation/GraphRAG-Implementation
*   Resources/02_Agents_Systems/LLM-Agent/Self-Evolving-Agents/Self-Evolving-Agents
