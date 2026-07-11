---
title: Meta-REFRAG
related_raw:
  - "[[wiki/RAG/Meta-REFRAG]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - semantic_chunking_and_contextual_rag
type: wiki
status: draft
last_updated: "2026-04-19"
updated: "2026-04-19"
---


# Meta의 REFRAG: RAG 시스템의 새로운 접근



Meta AI는 RAG(Retrieval Augmented Generation) 시스템의 효율성을 개선하기 위한 새로운 접근 방식인 REFRAG를 발표했습니다. REFRAG는 LLM에 전달되는 컨텍스트를 압축하고 필터링하여 속도를 높이고 비용을 절감합니다.



## 기술 다이어그램



*[이미지 삽입: REFRAG의 기술 다이어그램. 이 다이어그램은 질문과 컨텍스트가 청크로 나뉘고, 인코더를 통해 청크 임베딩으로 처리되며, RL 정책에 따라 선택적으로 확장되어 디코더에 공급되는 과정을 시각적으로 보여줍니다. 원본 논문 Figure 1 참조.]*



(이미지 출처: [REFRAG: Rethinking RAG based Decoding, arXiv:2509.01092](https://arxiv.org/abs/2509.01092))



## REFRAG의 주요 특징



- **속도 향상**: 첫 토큰 생성 시간이 30.85배 단축됩니다.

- **비용 절감**: 처리 토큰 수를 2-4배 줄여 비용을 절감합니다.

- **컨텍스트 확장**: 16배 더 큰 컨텍스트 창을 처리할 수 있습니다.

- **정확도 유지**: 정확도 손실 없이 성능을 향상시킵니다.



## 작동 방식



REFRAG는 각 청크를 단일 임베딩으로 압축하고, 강화 학습(RL) 기반의 정책을 사용하여 각 청크의 관련성을 평가합니다. 관련성이 높은 청크만 원래 형태로 확장되고 나머지는 압축된 상태로 LLM에 전달됩니다. 이를 통해 정보 밀도를 최적화하여 표현 효율성을 높입니다.



## 관련 자료



- **뉴스레터 및 MCP 가이드북**: [https://dailydoseofds.github.io/mcp-book/](https://dailydoseofds.github.io/mcp-book/)

- **REFRAG 논문**: [https://arxiv.org/abs/2509.01092](https://arxiv.org/abs/2509.01092)



## 관련 노트



- [[Areas/RAG기술현황(1)]]

- [[Areas/RAG기술현황(2)]]

- [[wiki/RAG/GraphRAG]]

- [[wiki/Models/Reasoning-and-Cognition/Why LLM models are not good at RAG]]




