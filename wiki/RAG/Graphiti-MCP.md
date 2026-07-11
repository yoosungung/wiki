---
title: MCP
related_raw:
  - "[[wiki/Agents/Frameworks/MCP/MCP]]"
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

`mcp_server.py`에서 MCP 데코레이터 정의들을 찾아 확인했습니다. 이제 노출되는 MCP 항목(툴/리소스)을 간결히 나열합니다.

### MCP Tools
- **add_memory(name, episode_body, group_id=None, source='text', source_description='', uuid=None)**: 에피소드를 메모리에 추가(비동기 큐 처리, 그룹별 순차 처리).
- **search_memory_nodes(query, group_ids=None, max_nodes=10, center_node_uuid=None, entity='')**: 노드 요약 기반 검색(RRF/노드거리 리랭커, 엔티티 타입 필터 가능).
- **search_memory_facts(query, group_ids=None, max_facts=10, center_node_uuid=None)**: 사실(엣지) 검색(관련 엣지 포맷팅 반환).
- **delete_entity_edge(uuid)**: 지정한 엔티티 엣지 삭제.
- **delete_episode(uuid)**: 지정한 에피소드(에피소딕 노드) 삭제.
- **get_entity_edge(uuid)**: 엔티티 엣지 단건 조회(포맷 변환 포함).
- **get_episodes(group_id=None, last_n=10)**: 최근 에피소드 목록 조회(Pydantic JSON 직렬화).
- **clear_graph()**: 그래프 전체 초기화 후 인덱스/제약 재생성.

### MCP Resource
- **resource 'http://graphiti/status' → get_status()**: 서버/Neo4j 연결 상태 반환(ok/error).
