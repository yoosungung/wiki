---
title: 핵심-클래스-Graphiti
related_raw:
  - "[[wiki/RAG/graphiti/핵심-클래스-Graphiti]]"
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

### 핵심 클래스: `Graphiti`
- 기본적으로 `Neo4jDriver`, `OpenAIClient`, `OpenAIEmbedder`, `OpenAIRerankerClient`를 초기화합니다(주입 가능).
- 텔레메트리 캡처, 동시 실행 제한, ensure_ascii 옵션(프롬프트/로그의 비ASCII 보존) 등을 지원.

graphiti_core/graphiti.py(130:221)
```python
class Graphiti:
    def __init__(
        self,
        uri: str | None = None,
        user: str | None = None,
        password: str | None = None,
        llm_client: LLMClient | None = None,
        embedder: EmbedderClient | None = None,
        cross_encoder: CrossEncoderClient | None = None,
        store_raw_episode_content: bool = True,
        graph_driver: GraphDriver | None = None,
        max_coroutines: int | None = None,
        ensure_ascii: bool = False,
    ):
        ...
        if graph_driver:
            self.driver = graph_driver
        else:
            if uri is None:
                raise ValueError('uri must be provided when graph_driver is None')
            self.driver = Neo4jDriver(uri, user, password)
        ...
        self.llm_client = llm_client or OpenAIClient()
        self.embedder = embedder or OpenAIEmbedder()
        self.cross_encoder = cross_encoder or OpenAIRerankerClient()

        self.clients = GraphitiClients(
            driver=self.driver,
            llm_client=self.llm_client,
            embedder=self.embedder,
            cross_encoder=self.cross_encoder,
            ensure_ascii=self.ensure_ascii,
        )
```



