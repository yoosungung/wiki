---
title: 검색-파이프라인
related_raw:
  - "[[wiki/RAG/graphiti/검색-파이프라인]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - graphiti
type: wiki
status: draft
last_updated: "2026-04-19"
---

### 검색 파이프라인
- 입력 쿼리를 필요 시 임베딩 후, 엣지/노드/에피소드/커뮤니티 각 레이어에 대해
  - 검색: BM25(풀텍스트), 코사인 유사도(벡터), BFS
  - 리랭킹: RRF, MMR, Cross-Encoder, Node Distance, Episode Mentions
  를 병렬 실행하여 통합 결과를 만듭니다.

graphiti_core/search/search.py(68:86)
```python
async def search(
    clients: GraphitiClients,
    query: str,
    group_ids: list[str] | None,
    config: SearchConfig,
    search_filter: SearchFilters,
    center_node_uuid: str | None = None,
    bfs_origin_node_uuids: list[str] | None = None,
    query_vector: list[float] | None = None,
) -> SearchResults:
    start = time()

    driver = clients.driver
    embedder = clients.embedder
    cross_encoder = clients.cross_encoder

    if query.strip() == '':
        return SearchResults()
```

graphiti_core/search/search.py(110:129)
```python
    # if group_ids is empty, set it to None
    group_ids = group_ids if group_ids and group_ids != [''] else None
    (
        (edges, edge_reranker_scores),
        (nodes, node_reranker_scores),
        (episodes, episode_reranker_scores),
        (communities, community_reranker_scores),
    ) = await semaphore_gather(
        edge_search(...),
        node_search(...),
        episode_search(...),
        community_search(...),
    )
```

- `Graphiti.search`는 간단 레시피(엣지 중심 하이브리드 + RRF 또는 Node Distance)로 엣지 리스트를 반환.
- `Graphiti.search_`는 고급 설정(`SearchConfig`)을 받아 `SearchResults`(노드/엣지/에피소드/커뮤니티+점수)를 반환.

graphiti_core/graphiti.py(910:967)
```python
    async def search(
        self,
        query: str,
        center_node_uuid: str | None = None,
        group_ids: list[str] | None = None,
        num_results=DEFAULT_SEARCH_LIMIT,
        search_filter: SearchFilters | None = None,
    ) -> list[EntityEdge]:
        ...
        edges = (
            await search(
                self.clients,
                query,
                group_ids,
                search_config,
                search_filter if search_filter is not None else SearchFilters(),
                center_node_uuid,
            )
        ).edges

        return edges
```



