---
title: "WordLift-RLM-on-KG"
related_raw: ["[[wiki/Models/RL/WordLift-RLM-on-KG.md]]"]
tags: ['wiki', 'knowledge_and_memory', 'advanced_rag_&_knowledge_graph', 'knowledge_graph_foundations_and_databases']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# WordLift: 지식 그래프 기반 추론 언어 모델 (RLM on KG)

## 요약
언어 모델(LLM)의 뛰어난 언어 이해력과 지식 그래프(Knowledge Graph)의 구조적 정확성을 결합한 아키텍처입니다. LLM이 지식 그래프의 노드와 엣지를 따라 논리적으로 탐색(Navigation)하며 답변을 생성하도록 하여 환각(Hallucination) 현상을 방지합니다. 특히 복잡한 다단계 질문(Multi-hop reasoning)에 대해 지식 그래프 상의 실제 연결 관계를 근거로 제시함으로써 답변의 신뢰도를 29.8% 향상시켰습니다.

## 핵심 개념
- **Navigator로서의 LLM**: LLM을 단순 정보 검색자가 아닌 지식 그래프를 탐색하는 주체로 활용.
- **RDF/SPARQL 연동**: 구조화된 지식 베이스(RDF)를 LLM이 직접 쿼리하거나 탐색할 수 있는 인터페이스 제공.
- **다단계 추론(Multi-hop Reasoning)**: 흩어져 있는 정보 조각들을 그래프 상의 경로를 따라 연결하여 종합적인 답변 생성.
- **출처 인용**: 지식 그래프 상의 엔티티와 관계를 답변의 근거로 명확히 제시.

## 기존 지식과의 연결
- Knowledge Graph: 단순 데이터베이스를 넘어 LLM의 추론을 가이드하는 '외부 지능' 역할.
- RAG: 유사도 기반 검색의 한계를 관계 기반 정밀 검색으로 극복하는 [[wiki/RAG/GraphRAG]]의 핵심 원리.
- Deep Agents: 전문 지식(법률, 의료 등)을 다루는 에이전트가 논리적 오류 없이 행동하도록 돕는 지식 베이스.

## 원문 URL
https://wordlift.io/blog/rlm-on-kg
