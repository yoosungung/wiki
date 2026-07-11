---
title: prompt
related_raw:
  - "[[wiki/RAG/graphiti/prompt]]"
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

### 프롬프트별 간략 기능 요약
- **extract_nodes**
  - extract_message: 대화 메시지에서 엔티티 노드 추출·분류
  - extract_json: JSON 소스에서 엔티티 추출·분류
  - extract_text: 일반 텍스트에서 엔티티 추출·분류
  - reflexion: 누락된 엔티티가 있는지 점검
  - classify_nodes: 추출된 엔티티의 타입 분류
  - extract_attributes: 엔티티 속성 값 추출/갱신
  - extract_summary: 엔티티 요약 생성/갱신

- **dedupe_nodes**
  - node: 신규 엔티티가 기존 엔티티의 중복인지 판정
  - nodes: 다수 엔티티에 대해 각각 중복 판정
  - node_list: 노드 목록 중 중복 묶음과 합성 요약 생성

- **extract_edges**
  - edge: 메시지에서 엔티티 간 사실(엣지) 추출(시간 정보 규칙 포함)
  - reflexion: 누락된 사실(엣지)이 있는지 점검
  - extract_attributes: 사실(엣지) 속성 값 추출/갱신

- **dedupe_edges**
  - edge: 새 사실이 기존 사실과 중복인지 판정
  - edge_list: 사실 목록 내 중복만 남기고 유니크 집합 도출
  - resolve_edge: 새 사실의 중복·모순·사실 타입 결정

- **invalidate_edges**
  - v1: 시간/내용 상 모순으로 만료(무효) 처리할 관계 판정
  - v2: 새 사실이 모순시키는 기존 사실들의 id 리스트 도출

- **extract_edge_dates**
  - v1: 사실(엣지) 자체에 직접 관련된 유효/무효 시점 추출

- **summarize_nodes**
  - summarize_pair: 두 요약을 하나의 간결한 요약으로 합성
  - summarize_context: 대화 컨텍스트로 특정 엔티티 요약과 속성 추출
  - summary_description: 주어진 요약의 1문장 설명 생성

- **eval**
  - qa_prompt: Alice 1인칭 응답 생성(요약/사실 기반)
  - eval_prompt: 정답 대비 응답의 정오 판정과 근거 작성
  - query_expansion: 질의를 검색 최적화 질문으로 변환
  - eval_add_episode_results: 그래프 추출 결과(베이스 vs 후보) 품질 비교 판정