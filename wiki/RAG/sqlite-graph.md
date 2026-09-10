---
title: sqlite-graph
related_raw:
  - "[[wiki/RAG/sqlite-graph]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - knowledge_graph_foundations_and_databases
type: wiki
status: draft
last_updated: "2026-04-19"
updated: "2026-04-19"
---


`sqlite-graph`는 SQLite에 그래프 데이터베이스 기능을 추가하는 확장 프로그램입니다.

## 기술적 요약

*   **Cypher 쿼리 지원:** SQLite 내에서 직접 Cypher 쿼리를 실행하여 그래프 패턴 매칭을 수행할 수 있습니다.
*   **그래프 알고리즘:** 연결성, 밀도, 중심성 등 다양한 그래프 알고리즘을 지원합니다.
*   **SQL 및 그래프 결합:** 표준 SQL과 그래프 작업을 함께 사용할 수 있습니다.
*   **제로 의존성:** 순수 C99로 작성되어 외부 의존성이 없습니다.
*   **현재 상태 (Alpha v0.1.0):**
    *   Cypher: `CREATE`, `MATCH`, `WHERE`, `RETURN` 지원
    *   성능: 노드 생성 30만+/초, 엣지 생성 39만+/초
*   **향후 계획 (v0.2.0):** 양방향 관계, 가변 길이 경로, 집계 함수 등 지원 예정

## 관련 링크

*   **GitHub Repository:** [https://github.com/agentflare-ai/sqlite-graph](https://github.com/agentflare-ai/sqlite-graph)

## 관련 노트

*   [[wiki/RAG/GraphRAG]]
*   Resources/Knowledge-Graph/LLM을 활용한 상향식 지식 그래프 구축
*   [[Projects/LinkedIn/janusGraph으로 여정]]
*   [[wiki/Engineering/Infrastructure-and-DevOps/Airflow DAG 테스트 환경 구축]]

