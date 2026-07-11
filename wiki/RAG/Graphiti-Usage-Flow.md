---
title: 일반-사용-흐름
related_raw:
  - "[[wiki/RAG/graphiti/일반-사용-흐름]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - graphiti
type: wiki
status: draft
last_updated: "2026-04-19"
updated: "2026-04-19"
---

### 일반 사용 흐름(요약)
- 그래프 연결 생성: `Graphiti(uri, user, password)` 또는 커스텀 `graph_driver` 주입.
- 데이터 적재: `add_episode(...)` 혹은 `add_episode_bulk(...)`.
- 검색: 간단히 `search(query)` 또는 고급 `search_(query, config=...)`.
- 유지보수: `build_indices_and_constraints`, `build_communities`, `remove_episode` 등 호출.

원하시면 특정 드라이버나 클라이언트 구현, 프롬프트 기반 추출 로직(`prompts/*`)까지 더 깊게 파고들어 상세 동작을 추가로 설명드릴게요.



