---
title: 드라이버-추상화
related_raw:
  - "[[wiki/RAG/graphiti/드라이버-추상화]]"
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



