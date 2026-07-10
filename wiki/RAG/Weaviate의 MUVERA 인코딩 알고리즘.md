---
title: Weaviate의 MUVERA 인코딩 알고리즘
related_raw:
  - "[[wiki/RAG/Weaviate의 MUVERA 인코딩 알고리즘]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - knowledge_graph_foundations_and_databases
type: wiki
status: draft
last_updated: "2026-04-19"
---

# Weaviate의 MUVERA 인코딩 알고리즘

이 블로그 게시물은 Weaviate 1.31에 구현된 MUVERA 인코딩 알고리즘에 대해 설명합니다. MUVERA는 다중 벡터 임베딩(예: ColBERT/ColPali)을 단일 고정 크기 벡터로 변환하여 메모리 및 계산 비용을 크게 줄입니다. 테스트 결과, 메모리 사용량이 약 70% 감소하고 가져오기 시간이 20분 이상에서 3-6분으로 단축되었습니다. 주요 단점은 검색 품질의 약간 손실이 있을 수 있지만 HNSW ef 값을 높여 완화할 수 있습니다. MUVERA는 대규모 배포, 메모리 비용이 중요한 경우, 약간의 검색 품질 저하를 허용할 수 있는 사용 사례, 더 빠른 인덱싱 속도가 필요한 애플리케이션에 가장 적합합니다. 이 글은 MUVERA의 작동 방식(공간 분할, 차원 축소, 다중 반복, 최종 투영)과 그 영향(메모리 및 수집 속도 향상, 검색 및 쿼리 처리량 감소)을 자세히 설명합니다.

## Links
- https://weaviate.io/blog/muvera?utm_source=linkedin&utm_medium=lm_social&utm_campaign=muvera&utm_content=diagram_post_680383730

## Images
- https://weaviate.io/img/blog/muvera/single-to-multi-vector-comparison.png
- https://weaviate.io/img/blog/muvera/multi-vector-embeddings-memory-comparison.png
- https://weaviate.io/img/blog/muvera/single-vs-multi-vector-memory-usage.png
- https://weaviate.io/img/blog/muvera/muvera-high-level-overview.png
- https://weaviate.io/img/blog/muvera/muvera-steps-1-space-partitioning.png
- https://weaviate.io/img/blog/muvera/muvera-steps-2-fill-empty-clusters.png
- https://weaviate.io/img/blog/muvera/muvera-steps-3-dimensionality-reduction.png
- https://weaviate.io/img/blog/muvera/heap-allocation-without-using-muvera-sq-vs-muvera-sq.png
- https://weaviate.io/img/blog/muvera/import-time-without-using-muvera-sq-vs-muvera-sq.png
- https://weaviate.io/img/blog/muvera/qps-without-using-muvera-sq-vs-muvera-sq.png
- https://weaviate.io/img/blog/muvera/recall-without-using-muvera-sq-vs-muvera-sq.png
- https://weaviate.io/img/blog/muvera/muvera-compared.png
