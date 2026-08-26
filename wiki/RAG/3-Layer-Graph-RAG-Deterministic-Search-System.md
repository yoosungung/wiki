---
title: 3-Layer-Graph-RAG-Deterministic-Search-System
related_raw:
  - "[[wiki/RAG/3-Layer-Graph-RAG-Deterministic-Search-System]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - graphrag_implementation
type: wiki
status: draft
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# 3계층 Graph-RAG 시스템: 결정론적 지식 검색 아키텍처

## 개요
단순한 벡터 검색(Semantic Search)만으로는 엔터프라이즈 환경에서 요구하는 데이터 간의 복잡한 관계와 정확한 사실 전달에 한계가 있습니다. 이를 해결하기 위해 지식 그래프(Knowledge Graph)와 벡터 DB를 결합한 **3계층 Graph-RAG 시스템**이 대안으로 부상하고 있습니다.

## 아키텍처 구성

### 1. 지식 그래프 계층 (Knowledge Graph Layer)
- **역할:** 원자적 사실(Atomic Facts)과 엄격한 엔티티 관계를 저장합니다.
- **특징:** 미리 정의된 온톨로지(Ontology)를 사용하여 그래프 오염을 방지하고, 구조화된 쿼리(Cypher 등)를 통해 정확한 관계를 추출합니다.

### 2. 벡터 DB 계층 (Vector DB Layer)
- **역할:** 모호한 문맥 정보나 롱테일(Long-tail) 데이터를 처리합니다.
- **특징:** 시맨틱 유사도 검색을 통해 지식 그래프에 명시적으로 정의되지 않은 관련 정보를 보완합니다.

### 3. 프롬프트 기반 융합 계층 (Fusion Layer)
- **역할:** 지식 그래프와 벡터 DB에서 추출된 결과를 LLM이 결정론적으로 통합합니다.
- **특징:** 두 데이터 소스 간에 정보 충돌이 발생할 경우, 사전 정의된 우선순위나 논리적 판단을 통해 최종 답변을 생성합니다.

## 구현 시 핵심 전략

- **Ontology-First:** LLM에게 자유로운 엔티티 추출을 맡기지 말고, 고정된 스키마를 사용하여 데이터 품질을 관리해야 합니다.
- **Entity Resolution (엔티티 식별):** 동일 인물이나 개념이 서로 다른 이름으로 표기될 경우, 이름 매칭 -> 시맨틱 유사도 -> LLM 최종 판단의 3단계 중복 제거 전략을 사용하여 비용과 오답률을 줄입니다.
- **Lazy Indexing:** 초기 구축 비용을 줄이기 위해 모든 청크를 요약하는 대신, 실제 쿼리가 발생할 때 필요한 부분만 커뮤니티 요약을 수행하는 방식을 채택합니다.

## 시사점
- 3계층 아키텍처는 기존 RAG 대비 약 3.4배 높은 정확도를 보여주며, 특히 복잡한 엔터프라이즈 질문에 대한 포괄적인 답변 생성이 가능합니다.
- 법률, 의료, 복잡한 인프라 관리 등 정확도가 생명인 도메인에서 필수적인 구조로 자리 잡고 있습니다.

## 참고 및 관련 노트
- **원문 URL:** https://machinelearningmastery.com/building-a-3-layer-graph-rag-system/
- **관련 노트:**
    - [[wiki/RAG/GraphRAG|GraphRAG 개요 및 원리]]
    - [[wiki/RAG/Contextual-Retrieval-Anthropic-2026|Anthropic의 Contextual Retrieval 분석]]
    - [[wiki/Models/Reasoning-and-Cognition/LLM을 활용한 상향식 지식 그래프 구축.md|지식 그래프 구축 방법론]]
