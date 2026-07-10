---
title: 아키텍처-포인트
related_raw:
  - "[[wiki/RAG/graphiti/아키텍처-포인트]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - graphiti
type: wiki
status: draft
last_updated: "2026-04-19"
---

### 아키텍처 포인트
- **플러그 가능한 백엔드**: `driver/neo4j_driver.py`, `falkordb_driver.py`, `kuzu_driver.py`, `neptune_driver.py`를 통해 동일 API로 다양한 DB 지원.
- **멀티 프로바이더 LLM/임베더/리랭커**: `llm_client/*`, `embedder/*`, `cross_encoder/*`로 OpenAI·Azure·Gemini·Anthropic·Groq·Voyage 등 교체 가능.
- **동시성 제어**: `helpers.semaphore_gather`와 `max_coroutines`로 병렬 처리 최적화.
- **검색 레시피**: `search/search_config_recipes.py`에 사전 구성된 하이브리드 전략 존재(RRF/MMR/크로스엔코더/노드거리).
- **텔레메트리**: 초기화 시 제공자 유형 감지 후 이벤트 전송(실패 무시하여 안전).



