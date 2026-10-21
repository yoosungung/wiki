---
title: 에피소드-처리-파이프라인
related_raw:
  - "[[wiki/RAG/graphiti/에피소드-처리-파이프라인]]"
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

### 에피소드 처리 파이프라인
- 입력 텍스트(에피소드)에서
  1) 노드 추출 → 2) 엣지 추출 → 3) 포인터 해결/중복제거 → 4) 속성 보강(LLM) → 5) 임베딩 생성 → 6) 그래프 저장
- 필요 시 커뮤니티 업데이트 수행.

graphiti_core/graphiti.py(501:558)
```python
            extracted_nodes = await extract_nodes(
                self.clients, episode, previous_episodes, entity_types, excluded_entity_types
            )

            # Extract edges and resolve nodes
            (nodes, uuid_map, node_duplicates), extracted_edges = await semaphore_gather(
                resolve_extracted_nodes(...),
                extract_edges(...),
                max_coroutines=self.max_coroutines,
            )

            edges = resolve_edge_pointers(extracted_edges, uuid_map)

            (resolved_edges, invalidated_edges), hydrated_nodes = await semaphore_gather(
                resolve_extracted_edges(...),
                extract_attributes_from_nodes(...),
                max_coroutines=self.max_coroutines,
            )
            ...
            await add_nodes_and_edges_bulk(
                self.driver, [episode], episodic_edges, hydrated_nodes, entity_edges, self.embedder
            )
```

### v0.31.2 에피소드 삭제·벌크 (2026-10-20)

- `remove_episode`: restated fact를 남기고 summary를 다시 만든다(#2025). 삭제 = 그래프에서 에피소드만 지운다고 가정하지 말 것.
- `add_episode_bulk`: 에피소드에 supported edges를 기록(#2030). 벌크 적재 후 엣지 포인터가 비면 0.31.2 미만 핀을 의심.
- 릴리스 앵커: [[wiki/RAG/Graphiti-Overview.md]].



