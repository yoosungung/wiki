---
title: 무엇을-하는-패키지인가
related_raw:
  - "[[wiki/RAG/graphiti/무엇을-하는-패키지인가]]"
  - "[[raw/2026-09-16-graphiti-v0.30.2-neo4j-falkordb.md]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - graphiti
type: wiki
status: draft
last_updated: "2026-09-16"
updated: "2026-09-16"
---

### 무엇을 하는 패키지인가
- **지식 그래프(Neo4j/FalkorDB/Kuzu/Neptune 등) 위에 LLM·임베딩·리랭커를 결합해**
  - 에피소드 텍스트에서 노드/엣지 추출·중복제거·속성 보강
  - 벡터/풀텍스트/BFS 하이브리드 검색 및 다양한 리랭킹
  - 커뮤니티(클러스터) 생성/업데이트
  를 제공하는 상위 orchestration 레이어입니다.

### 최근 릴리스 앵커 (graphiti-core 0.30.2, 2026-09-08)
- Neo4j: `execute_query`가 설정된 DB로 라우팅(멀티-DB Enterprise 주의).
- MCP: `NEO4J_DATABASE` 존중.
- FalkorDB: edge fulltext의 per-hit `:Entity` 스캔 제거.
- 상세·체크리스트: [[wiki/RAG/Graphiti-Driver-Abstraction.md]], [[wiki/RAG/Graphiti-MCP.md]].



