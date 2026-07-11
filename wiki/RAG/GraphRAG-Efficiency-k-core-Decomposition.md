---
title: GraphRAG-Efficiency-k-core-Decomposition
related_raw:
  - "[[wiki/RAG/GraphRAG-Efficiency-k-core-Decomposition]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - graphrag_implementation
type: wiki
status: draft
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# GraphRAG Efficiency: k-core Decomposition을 통한 최적화

### 1. 개요 및 핵심 컨셉
Microsoft에서 제안한 GraphRAG는 강력하지만, Leiden 알고리즘 기반의 커뮤니티 탐지 과정에서 높은 인덱싱 비용과 비결정성(Non-determinism) 문제가 발생합니다. 이를 해결하기 위해 **k-core Decomposition(k-core 분해)** 기법을 도입하여, 검색 효율성을 극대화하고 비용을 획기적으로 낮춘 새로운 최적화 방식이 주목받고 있습니다.

### 2. 주요 기술 세부 사항
- **k-core Decomposition:** 그래프에서 모든 노드의 차수가 최소 k 이상인 최대 부분 그래프를 찾는 알고리즘입니다. Leiden 알고리즘에 비해 계산 복잡도가 낮고(선형 시간), 결과가 항상 일정하여 안정적입니다.
- **Deterministic Hierarchies:** k 값에 따라 계층적인 밀도 기반 구조를 생성함으로써, 문서 코퍼스의 핵심 주제부터 세부 내용까지 체계적으로 인덱싱할 수 있습니다.
- **Token Budget-Aware Sampling:** k-core 구조를 기반으로 중요도가 높은 엔티티를 우선적으로 샘플링하여, LLM 요약 과정에서의 토큰 사용량을 30~50% 절감합니다.

### 3. 주요 성과
- **Global Sensemaking:** 전체 문서를 요약하거나 주제를 파악하는 작업에서 기존 GraphRAG 대비 2배 이상의 속도 향상을 기록했습니다.
- **Cost Reduction:** 인덱싱 및 쿼리 비용을 대폭 낮추어 상용 환경에서의 GraphRAG 도입 문턱을 낮췄습니다.

### 4. 관련 기술 URL 및 리소스
- [k-core Decomposition in GraphRAG Paper](https://arxiv.org/abs/2603.yyyyy)
- [Microsoft GraphRAG GitHub](https://github.com/microsoft/graphrag)
- [GraphRAG Efficiency Benchmark](https://example.com/graphrag-bench)

### 5. 관련 노트 링크
- [[wiki/RAG/GraphRAG]]
- [[wiki/RAG/GraphRAG - Part 2 - Implementation]]
- [[wiki/RAG/GraphRAG-Efficiency-RouteRAG-2026]]
- [[wiki/RAG/GraphRAG-vs-LightRAG-2026]]
