---
title: AGRAG-Advanced-Graph-RAG-MCMI
related_raw:
  - "[[wiki/RAG/AGRAG-Advanced-Graph-RAG-MCMI]]"
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

# AGRAG: 통계 기반 그래프 구축 및 MCMI 서브그래프 생성 (2026)

**AGRAG (Advanced Graph-based RAG)** 프레임워크는 기존 GraphRAG 시스템의 고비용 문제와 환각(Hallucination) 현상을 해결하기 위해 제안된 최신 기술입니다. LLM 대신 통계적 방법을 활용하여 지식 그래프를 구축하고, 최적의 추론 경로를 찾는 것이 핵심입니다.

### 1. 핵심 메커니즘
- **통계 기반 엔티티 추출:** 그래프 구축 시 LLM 호출 비용을 줄이고, LLM에서 발생할 수 있는 환각과 오류 전파를 방지하기 위해 통계적 기법을 사용합니다.
- **MCMI (Minimum Cost Maximum Influence) 서브그래프 생성:**
    - 검색 단계를 '최소 비용으로 최대 영향력을 가진 노드를 포함하는 서브그래프'를 찾는 문제로 정의합니다.
    - 높은 영향력을 가진 노드들을 포함하면서도 엣지 비용(추론 복잡도)을 최소화하여 포괄적이고 효율적인 답변 생성을 지원합니다.
    - 복잡한 순환(Cycle) 구조를 가진 그래프에서도 최적의 추론 경로를 식별할 수 있습니다.

### 2. 기술적 의의
- **추론 포괄성 향상:** 단순한 트리 구조를 넘어 복잡한 그래프 구조를 지원함으로써 멀티홉 추론 성능을 높였습니다.
- **비용 효율성:** 인덱싱 단계에서 LLM 의존도를 낮춰 대규모 데이터셋 처리에 유리합니다.
- **설명 가능성:** 모델이 특정 서브그래프를 선택한 이유를 명확히 제시할 수 있어 답변의 근거(Citation)가 강화됩니다.

### 3. 관련 링크 및 참고
- **원문:** [AGRAG: Advanced Graph-based Retrieval-Augmented Generation (arXiv:2511.05549)](https://arxiv.org/abs/2511.05549)
- **기존 노트:**
    - [[wiki/RAG/GraphRAG-vs-LightRAG-2026|GraphRAG vs LightRAG: 2026년 성능 비교]]
    - [[wiki/RAG/3-Layer-Graph-RAG-Deterministic-Search-System|3계층 Graph-RAG 시스템]]
    - [[wiki/Models/RL/WordLift-RLM-on-KG.md|지식 그래프 기반 RLM 아키텍처]]

**분류:** #GraphRAG #KnowledgeGraph #RAG #MCMI #AGRAG
