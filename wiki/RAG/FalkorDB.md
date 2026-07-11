---
title: FalkorDB
related_raw:
  - "[[wiki/RAG/FalkorDB]]"
  - "[[Microsoft GraphRAG just got dethroned.\n\n(and the winner is 100% open-source)\n\nGraphRAG-SDK from FalkorDB is now topping the GraphRAG-Bench leaderboard with 69.73 overall accuracy across the Novel and… | Akshay Pachaar.md]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - knowledge_graph_foundations_and_databases
  - FalkorDB
  - GraphRAG
type: wiki
status: published
last_updated: "2026-05-01"
updated: "2026-05-01"
---

## 1. 개요
Microsoft, Google, AWS 등 모두 AI 에이전트를 위한 지식 그래프를 실시간 LLM 애플리케이션에 충분히 빠르게 만드는 문제를 해결하려고 합니다. FalkorDB는 전통적인 그래프 탐색 대신 희소 행렬과 선형 대수를 사용하여 이 문제를 해결하는 오픈 소스 그래프 데이터베이스입니다.

## 2. 벤치마크 성과 (2026)
2026년 최신 벤치마크 결과, FalkorDB의 **GraphRAG-SDK**가 Microsoft GraphRAG를 제치고 **GraphRAG-Bench 리더보드 1위**를 차지했습니다.
- **정확도**: 전체 69.73%의 정확도를 기록 (Novel 및 복잡한 쿼리 데이터셋 기준).
- **의의**: 100% 오픈 소스 솔루션이 엔터프라이즈급 상용 솔루션을 성능 면에서 압도함.

## 3. 핵심 아키텍처
기존 그래프 데이터베이스는 노드 간의 관계를 연결된 노드로 저장하고 한 번에 한 홉씩 탐색하여 대규모 지식 그래프에서 병목 현상을 일으킵니다. FalkorDB는 전체 그래프를 희소 행렬로 표현하여 필요한 연결만 저장하고, 탐색 대신 선형 대수를 사용하여 쿼리를 수학적 연산으로 만듭니다. 이는 탐색보다 훨씬 빠르고 효율적인 저장 공간을 제공합니다.

벡터 검색은 유사성만 포착하지만, FalkorDB는 엔티티 간의 미묘한 관계를 포착하여 AI 에이전트의 컨텍스트가 매우 정확하고 관련성 있도록 보장합니다.

## 4. 주요 특징
*   **초고속, 멀티테넌트**: LLM 애플리케이션 및 에이전트 메모리를 위해 최적화.
*   **희소 행렬 표현**: 메모리 및 계산 효율성 극대화.
*   **OpenCypher 지원**: Neo4j와 동일한 쿼리 언어 사용 가능.
*   **Redis 기반**: 검증된 인프라 위에서 쉬운 배포 및 확장.

## 5. 시작하기
Docker 명령 하나로 시작할 수 있으며, Python 클라이언트로 테스트했을 때 성능 차이가 즉시 나타납니다. 실시간으로 연결된 정보에 접근해야 하는 AI 에이전트를 구축한다면 탐색할 가치가 있는 100% 오픈 소스 프로젝트입니다.

**출처**: [Akshay Pachaar LinkedIn](https://www.linkedin.com/posts/akshay-pachaar_microsoft-graphrag-just-got-dethroned-ugcPost-7455594957853085696-8AU1?utm_source=share&utm_medium=member_ios&rcm=ACoAADm5eyABU_duDuXv1f9N-6JhXB_iNO6faes)

## Related Notes
- [[wiki/RAG/Knowledge Graph Extraction and Challenges.md]]
- [[wiki/Models/Reasoning-and-Cognition/LLM을 활용한 상향식 지식 그래프 구축.md]]
- [[wiki/RAG/GraphRAG.md]]
- [[wiki/RAG/sqlite-graph.md]]