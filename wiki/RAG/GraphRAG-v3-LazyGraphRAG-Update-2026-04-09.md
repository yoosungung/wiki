---
title: GraphRAG-v3-LazyGraphRAG-Update-2026-04-09
related_raw:
  - "[[wiki/RAG/GraphRAG-v3-LazyGraphRAG-Update-2026-04-09]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - graphrag_implementation
type: wiki
status: draft
last_updated: "2026-04-19"
---

# Microsoft GraphRAG v3 및 LightRAG 업데이트 (2026-04-09)

## 요약
지식 그래프 기반의 RAG 아키텍처는 비용 효율성과 모듈화라는 두 마리 토끼를 잡기 위해 진화하고 있습니다. Microsoft의 **GraphRAG v3.0**과 **LazyGraphRAG**가 그 중심에 있습니다.

## 주요 내용
- **LazyGraphRAG:** 사전 인덱싱 비용을 99.9% 절감하면서 쿼리 시점에 동적으로 그래프를 구축하여 실무 적용성을 높였습니다.
- **모듈형 아키텍처:** GraphRAG 시스템이 개별 패키지로 분리되어 사용자가 LLM, 저장소, 벡터 엔진을 자유롭게 선택할 수 있게 되었습니다.
- **LightRAG 엔터프라이즈:** OpenSearch와의 통합 및 벡터 차원 자동 관리 기능을 통해 대규모 데이터셋 처리를 최적화했습니다.

## 원문 URL
- [Microsoft GraphRAG GitHub](https://github.com/microsoft/graphrag)

## 관련 노트
- [[wiki/RAG/GraphRAG-Efficiency-k-core-Decomposition]]
- [[wiki/RAG/LightRAG-Summary-2026]]
- [[wiki/RAG/GraphRAG-Efficiency-RouteRAG-2026]]
