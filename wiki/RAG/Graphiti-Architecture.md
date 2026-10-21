---
title: 아키텍처-포인트
related_raw:
  - "[[wiki/RAG/graphiti/아키텍처-포인트]]"
  - "[[raw/2026-09-19-graphiti-local-readonly-mcp.md]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - graphiti
type: wiki
status: draft
last_updated: "2026-10-22"
updated: "2026-10-22"
---

### 아키텍처 포인트
- **플러그 가능한 백엔드**: `driver/neo4j_driver.py`, `falkordb_driver.py`, `kuzu_driver.py`, `neptune_driver.py`를 통해 동일 API로 다양한 DB 지원.
- **멀티 프로바이더 LLM/임베더/리랭커**: `llm_client/*`, `embedder/*`, `cross_encoder/*`로 OpenAI·Azure·Gemini·Anthropic·Groq·Voyage 등 교체 가능.
- **동시성 제어**: `helpers.semaphore_gather`와 `max_coroutines`로 병렬 처리 최적화.
- **검색 레시피**: `search/search_config_recipes.py`에 사전 구성된 하이브리드 전략 존재(RRF/MMR/크로스엔코더/노드거리).
- **텔레메트리**: 초기화 시 제공자 유형 감지 후 이벤트 전송(실패 무시하여 안전).
- **로컬 읽기 전용 래퍼**: `graphiti-local` 0.4.1은 임베디드 LadybugDB + Ollama. 쓰기 MCP가 아니라 제안 큐·사람 승인. core 핀 `0.30.1` — [[wiki/RAG/Graphiti-MCP.md]].
- **0.31.0 라우팅·추출 (2026-10-14)**: `LLMRuntime`이 프롬프트·모델 경로를 나눈다. 결합 추출 기본 프롬프트는 **C2**. 노드/엣지 dedupe에 Jev·OpenAI Decisions 클라이언트. 호스팅 OpenAI 기본 모델은 `gpt-6-luna`(prompt caching off). 릴리스 앵커: [[wiki/RAG/Graphiti-Overview.md]].



