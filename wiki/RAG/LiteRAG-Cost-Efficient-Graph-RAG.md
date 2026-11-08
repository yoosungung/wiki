---
id: wiki-literag-cost-efficient-graph-rag
title: "LiteRAG: 질의조건 그래프 탐색으로 GraphRAG 비용 절감"
status: canonical
owner: km
updated: "2026-11-09"
last_updated: "2026-11-09"
review_after: "2026-12-09"
tags: ["RAG", "GraphRAG", "LiteRAG", "Cost"]
sources:
  - https://arxiv.org/abs/2609.10239
type: wiki
---

# LiteRAG: 질의조건 그래프 탐색으로 GraphRAG 비용 절감

그래프 RAG는 멀티홉 QA에 유리하지만, 질의 시점 LLM 제어와 과대 컨텍스트로 지연·비용이 커진다. LiteRAG(arXiv:2609.10239)는 검색 시점 LLM 제어를 **질의조건 알고리즘 탐색 + 추론 체인 컨텍스트 구성**으로 대체한다.

## 결과 요약 (논문 보고)

| 벤치 | 요지 |
| :--- | :--- |
| DistComp | 전체 품질 최고(0.798); GraphRAG Global/DRIFT 대비 per-query latency >100×↓, cost >99%↓ |
| UltraDomain | LinearRAG와 전체 품질 동급, 토큰 ~14×↓ |
| Ablation | query-adaptive thresholding · community-aware hub penalization이 토큰 효율 주동인 |

기존 [[wiki/RAG/GraphRAG-vs-LightRAG-2026.md]]의 LightRAG(**제품/프레임** HKUDS, tip v1.5.7)와 이름만 유사 — LiteRAG는 **별도 연구 방법**이다. 혼동 금지.

## 🔗 관련 문서

- [[wiki/RAG/GraphRAG-vs-LightRAG-2026.md]]
- [[wiki/RAG/Graphiti-Architecture.md]]
- [[wiki/RAG/Helix-Temporal-GraphRAG.md]]
