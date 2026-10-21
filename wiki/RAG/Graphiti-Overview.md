---
title: 무엇을-하는-패키지인가
related_raw:
  - "[[wiki/RAG/graphiti/무엇을-하는-패키지인가]]"
  - "[[raw/2026-09-16-graphiti-v0.30.2-neo4j-falkordb.md]]"
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

### 무엇을 하는 패키지인가
- **지식 그래프(Neo4j/FalkorDB/Kuzu/Neptune 등) 위에 LLM·임베딩·리랭커를 결합해**
  - 에피소드 텍스트에서 노드/엣지 추출·중복제거·속성 보강
  - 벡터/풀텍스트/BFS 하이브리드 검색 및 다양한 리랭킹
  - 커뮤니티(클러스터) 생성/업데이트
  를 제공하는 상위 orchestration 레이어입니다.

### 최근 릴리스 앵커 (graphiti-core 0.31.2, 2026-10-20)
- **0.31.0** (2026-10-14): 기본 OpenAI 모델 `gpt-6-luna`(prompt cache off). `LLMRuntime`으로 프롬프트·모델 라우팅. 결합 추출 프롬프트 기본을 C2로. 노드/엣지 dedupe에 Jev·OpenAI Decisions 클라이언트. Zep 포크의 추출·중복제거·temporal 수정 업스트림. FalkorDB 6.x는 노드 fulltext 인덱스를 DDL 형으로.
- **0.31.1**: 버전 핀 정리.
- **0.31.2**: `certifi==2026.10.19`(eMudhra 대응). MCP 서버 **1.1.2**. 참조 MCP/REST는 **localhost 기본 listen**·reference-only. Neptune fulltext에 `group` 필터. `remove_episode`는 restated fact 유지·summary 재빌드. `add_episode_bulk`는 에피소드에 supported edges 기록.
- 0.30.2 축(Neo4j DB 라우팅·MCP `NEO4J_DATABASE`·FalkorDB per-hit 스캔 제거)은 유지.
- 상세: [[wiki/RAG/Graphiti-Driver-Abstraction.md]], [[wiki/RAG/Graphiti-MCP.md]], [[wiki/RAG/Graphiti-Architecture.md]].
- 출처: [v0.31.0](https://github.com/getzep/graphiti/releases/tag/v0.31.0), [v0.31.2](https://github.com/getzep/graphiti/releases/tag/v0.31.2).
- **로컬 대안 (2026-09-18)**: `graphiti-local` 0.4.1은 core `0.30.1`에 고정된 읽기 전용 MCP다. 업스트림 0.31.2와 핀이 다르다 — [[wiki/RAG/Graphiti-MCP.md]].



