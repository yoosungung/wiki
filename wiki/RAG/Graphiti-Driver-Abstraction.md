---
title: 드라이버-추상화
related_raw:
  - "[[wiki/RAG/graphiti/드라이버-추상화]]"
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

### 드라이버 추상화
- 다양한 그래프 백엔드에 대한 공통 인터페이스(`execute_query`, `session`, `delete_all_indexes` 등) 제공합니다.

graphiti_core/driver/driver.py(58:90)
```python
class GraphDriver(ABC):
    provider: GraphProvider
    fulltext_syntax: str = (
        ''  # Neo4j (default) syntax does not require a prefix for fulltext queries
    )
    _database: str

    @abstractmethod
    def execute_query(self, cypher_query_: str, **kwargs: Any) -> Coroutine: ...
    @abstractmethod
    def session(self, database: str | None = None) -> GraphDriverSession: ...
    @abstractmethod
    def close(self): ...
    @abstractmethod
    def delete_all_indexes(self) -> Coroutine: ...

    def with_database(self, database: str) -> 'GraphDriver':
        cloned = copy.copy(self)
        cloned._database = database
        return cloned
```

### v0.30.x 운영 함정 (Neo4j · FalkorDB)

출처: [Graphiti v0.30.0](https://github.com/getzep/graphiti/releases/tag/v0.30.0), [v0.30.2](https://github.com/getzep/graphiti/releases/tag/v0.30.2).

1. **Neo4j `execute_query` DB 라우팅 (0.30.0+)**  
   - 이전: 세션 쓰기는 `driver._database`를 따르지만 `execute_query`(검색 포함)는 서버 **home DB**로 나갈 수 있었음.  
   - 이후: 설정된 DB(기본 `neo4j`)로 라우팅. 호출별 오버라이드 `execute_query(..., database_="name")`.  
   - **영향 범위**: Neo4j Enterprise 멀티-DB에서 home ≠ `neo4j`이거나 커스텀 DB를 쓰던 셀프호스트. Community/기본 `neo4j`만 쓰면 무동작 변경.  
   - **마이그레이션**: 구버전 `execute_query`로 home에 쌓인 데이터가 있으면 명시적 DB로 이전하거나 `database=`를 홈 이름에 맞춤.

2. **FalkorDB fulltext (0.30.2+)**  
   - `edge_fulltext_search`가 히트마다 `:Entity` 전체 스캔하던 경로를 제거. 대규모 엣지 풀텍스트 부하 전 ≥0.30.2 권장.

3. **멀티 `group_id` 동시성 (0.30.2+)**  
   - 요청 스코프 드라이버로 concurrent multi-`group_id` 격리. `group_ids` 클리어 시 Saga 노드 포함.

관련: [[wiki/RAG/Graphiti-MCP.md]], [[wiki/RAG/Graphiti-Overview.md]], [[wiki/RAG/GraphRAG-vs-LightRAG-2026.md]].



