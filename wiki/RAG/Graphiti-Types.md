---
title: 타입-클라이언트-집합
related_raw:
  - "[[wiki/RAG/graphiti/타입-클라이언트-집합]]"
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

### 타입/클라이언트 집합
- `GraphitiClients`로 드라이버/LLM/임베더/크로스엔코더/ensure_ascii를 묶어 함수 간 전달.

graphiti_core/graphiti_types.py(25:33)
```python
class GraphitiClients(BaseModel):
    driver: GraphDriver
    llm_client: LLMClient
    embedder: EmbedderClient
    cross_encoder: CrossEncoderClient
    ensure_ascii: bool = False

    model_config = ConfigDict(arbitrary_types_allowed=True)
```



