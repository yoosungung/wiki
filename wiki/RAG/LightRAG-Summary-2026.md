---
title: LightRAG-Summary-2026
related_raw:
  - "[[raw/2026-09-15-lightrag-v1.5.7-workspace-pgtable.md]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - graphrag_implementation
type: wiki
status: draft
last_updated: "2026-09-15"
updated: "2026-09-15"
---

# LightRAG: 단순하고 빠른 검색 증강 생성

## 1. 요약 (Summary)

**LightRAG**는 홍콩대학교(HKU) 연구진이 개발한 오픈소스 프로젝트로, 지식 그래프(Knowledge Graph)를 활용하여 더 정확하고 효율적인 정보 검색 및 답변 생성을 목표로 합니다.

**핵심 특징 및 장점:**
*   **지식 그래프 통합**: 엔티티(Entity)와 관계(Relationship)를 추출하여 복잡한 다단계 추론이 필요한 질문에 대응.
*   **이중 레벨 검색 (Dual-Level Retrieval)**: 로컬(세부 정보) 및 글로벌(전체 맥락) 검색을 결합.
*   **효율성 및 속도**: 빠른 인덱싱 및 쿼리 성능, 대규모 데이터셋 최적화.
*   **증분 업데이트**: 새로운 문서가 추가될 때 전체 그래프를 다시 그릴 필요 없음.

## 2. v1.5.7 배포 체크리스트 (2026-09-02)

1. **엔드유저 표면**: `/workspace`를 공개 질의 엔트리로 두고, 문서·그래프·API docs는 관리자 엔트리에만 노출.
2. **브랜딩**: `UI_TEMPLATES_DIR`에 welcome/login/empty-state Markdown + `manifest.json`을 두고 재빌드 없이 로고·동의문·저작권 문구를 교체.
3. **전역 프롬프트**: `USER_PROMPT_PREFIX`(또는 `_FILE`)로 역할·인용·다이어램 규칙을 고정 — 요청 본문이 덮어쓰지 못함.
4. **스토리지**: Postgres 단일 DB를 목표로 할 때 `PGTableGraphStorage`를 선호; AGE 그래프는 오프라인 마이그레이션 도구로 테이블 백엔드로 이전. AGE ≥ 1.8.0 + `PGGraphStorage` 조합은 기동 거부.
5. **인제스트**: graph-first + deferred vector indexing으로 대량 업로드 피크를 분리; custom chunking selector로 문서군별 전략을 고정.

상세 비교·선택 가이드: [[wiki/RAG/GraphRAG-vs-LightRAG-2026.md]] §6.

## 3. 관련 URL
*   프로젝트: https://github.com/HKUDS/LightRAG
*   릴리스 v1.5.7: https://github.com/HKUDS/LightRAG/releases/tag/v1.5.7
*   논문: https://arxiv.org/abs/2410.05779

## 4. 설명 이미지
![LightRAG Diagram](https://raw.githubusercontent.com/HKUDS/LightRAG/main/README.assets/b2aaf634151b4706892693ffb43d9093.png)
![LightRAG Indexing Flowchart](https://learnopencv.com/wp-content/uploads/2024/11/LightRAG-VectorDB-Json-KV-Store-Indexing-Flowchart-scaled.jpg)

## 5. 관련 노트 링크
- [[wiki/RAG/GraphRAG-vs-LightRAG-2026.md]]
- [[wiki/RAG/000_RAG-MOC.md]]
- [[wiki/RAG/Graphiti-Architecture.md]]