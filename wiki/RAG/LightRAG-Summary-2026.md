---
title: LightRAG-Summary-2026
related_raw:
  - "[[wiki/RAG/LightRAG-Summary-2026]]"
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

# LightRAG: 단순하고 빠른 검색 증강 생성

## 1. 요약 (Summary)

**LightRAG**는 홍콩대학교(HKU) 연구진이 개발한 오픈소스 프로젝트로, 지식 그래프(Knowledge Graph)를 활용하여 더 정확하고 효율적인 정보 검색 및 답변 생성을 목표로 합니다.

**핵심 특징 및 장점:**
*   **지식 그래프 통합**: 엔티티(Entity)와 관계(Relationship)를 추출하여 복잡한 다단계 추론이 필요한 질문에 대응.
*   **이중 레벨 검색 (Dual-Level Retrieval)**: 로컬(세부 정보) 및 글로벌(전체 맥락) 검색을 결합.
*   **효율성 및 속도**: 빠른 인덱싱 및 쿼리 성능, 대규모 데이터셋 최적화.
*   **증분 업데이트**: 새로운 문서가 추가될 때 전체 그래프를 다시 그릴 필요 없음.

## 2. 관련 URL
*   프로젝트: https://github.com/HKUDS/LightRAG
*   논문: https://arxiv.org/abs/2410.05779

## 3. 설명 이미지
![LightRAG Diagram](https://raw.githubusercontent.com/HKUDS/LightRAG/main/README.assets/b2aaf634151b4706892693ffb43d9093.png)
![LightRAG Indexing Flowchart](https://learnopencv.com/wp-content/uploads/2024/11/LightRAG-VectorDB-Json-KV-Store-Indexing-Flowchart-scaled.jpg)

## 4. 관련 노트 링크
[[wiki/RAG/GraphRAG]]
[[wiki/RAG/Light RAG]]
Knowledge-Graph
RAG
Vector-Database