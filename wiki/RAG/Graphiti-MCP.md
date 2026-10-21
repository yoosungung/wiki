---
title: MCP
related_raw:
  - "[[wiki/Agents/Frameworks/MCP/MCP]]"
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
sources:
  - https://pypi.org/project/graphiti-local/
  - raw/2026-09-19-graphiti-local-readonly-mcp.md
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

### v0.30.2 배포 체크리스트 (MCP + Neo4j)

- **`NEO4J_DATABASE` 명시**: MCP 서버가 드라이버 DB 설정을 존중하도록 수정됨(#1812). 기본 `neo4j`가 아니면 환경변수/설정을 반드시 맞춤 — [[wiki/RAG/Graphiti-Driver-Abstraction.md]]의 `execute_query` 라우팅과 동일 계열.
- **멀티 테넌트 `group_id`**: 동시 요청 isolation은 요청 스코프 드라이버에 의존(0.30.2+). `clear` by `group_ids` 시 Saga 노드 누락 수정 포함.
- **업그레이드 순서**: graphiti-core ≥0.30.2 → MCP 이미지/프로세스 재기동 → `http://graphiti/status`로 연결·DB 확인.

### v0.31.x MCP (2026-10-14···20)

출처: [v0.31.0](https://github.com/getzep/graphiti/releases/tag/v0.31.0), [v0.31.2](https://github.com/getzep/graphiti/releases/tag/v0.31.2).

- **MCP SDK 2.x** (`mcp_server`). 도구는 요청 `group_id` 그래프만 본다(#1926).
- 참조 MCP/REST 서버는 **reference-only**. 기본 listen은 **localhost** — 공개 바인딩을 가정하지 말 것(#2032/#2035).
- 핀: graphiti-core **0.31.2** + MCP 서버 **1.1.2** + `certifi>=2026.10.19`(eMudhra).
- 업그레이드: core 0.31.2 → MCP 1.1.2 재기동 → `http://graphiti/status`. graphiti-local 0.4.1 핀(`0.30.1`)과 섞지 말 것.

### graphiti-local 0.4.1 — 읽기 전용 MCP + 사람 승인 큐 (2026-09-18)

업스트림 MCP(`add_memory` 등 쓰기 포함)와 별개로, [graphiti-local](https://pypi.org/project/graphiti-local/) 0.4.1은 **로컬 에이전트 메모리**용 래퍼다. core 핀은 `graphiti-core==0.30.1`(업스트림 0.30.2보다 한 패치 뒤). 0.30.2의 Neo4j/FalkorDB 수정을 쓰려면 이 핀을 그대로 믿지 말고 core를 먼저 맞춘다.

| 축 | 업스트림 MCP | graphiti-local |
| :--- | :--- | :--- |
| 쓰기 | 에피소드 추가·삭제 | **읽기 전용** 도구 6개. 제안은 별도 큐, 사람이 승인·적용 |
| 저장 | Neo4j/FalkorDB 등 | 기본은 임베디드 LadybugDB(`ladybug` ≥0.19.1). FalkorDB·Neo4j도 지원 |
| 추론 | 호스팅/자체 LLM | 로컬 Ollama. Docker·클라우드 키 없이 기동 가능 |
| 기본 검색 | 설정 따름 | 현재 사실. 이력은 `kg ask --history` |

```bash
# 추출을 그래프에 넣기 전 스냅샷 검토 후, 출력된 restore로만 승격
kg-ingest INPUT --review-output review.jsonl
```

에이전트가 MCP로 그래프를 직접 써야 하면 graphiti-local이 아니라 업스트림 `mcp_server`를 쓴다.

