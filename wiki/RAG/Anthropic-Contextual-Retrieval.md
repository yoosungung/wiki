---
title: Anthropic-Contextual-Retrieval
related_raw:
  - "[[wiki/RAG/Anthropic-Contextual-Retrieval]]"
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

# Anthropic: 맥락적 검색 (Contextual Retrieval)

## 요약
전통적인 RAG 시스템의 고질적인 문제인 '문맥 소실(Context Loss)'을 해결하기 위한 기술입니다. 문서를 작은 조각(Chunk)으로 나눌 때, 각 조각이 전체 문서 내에서 어떤 의미를 갖는지 설명하는 짧은 문맥(Contextual Blurb)을 LLM으로 생성하여 각 청크 앞에 붙여 임베딩하는 방식입니다. 이 기법은 검색 실패율을 49% 줄이며, 리랭킹(Reranking) 기술과 결합할 경우 실패율을 최대 67%까지 낮추는 획기적인 성능 향상을 보여줍니다.

## 핵심 기술
- **Contextual Retrieval**: 각 청크에 대해 "이 청크는 [전체 문서 제목/주제]의 [섹션]에 해당하며, [주요 맥락]을 다루고 있음"과 같은 정보를 추가.
- **BM25 + Vector Hybrid Search**: 키워드 기반 검색과 시맨틱 검색을 결합하여 정밀도 극대화.
- **Reranking**: 검색된 상위 결과들을 다시 한번 정교하게 평가하여 순위 조정.
- **효과**: 대명사(it, they 등)나 생략된 주어 등으로 인해 발생하는 검색 누락 방지.

## 기존 지식과의 연결
- [[wiki/RAG/RAG-Best-Practices|RAG 시스템 개선 모범 사례]]: 논문에서 강조한 'ROI가 높은 문서 관련성 개선'의 실질적인 구현 방법론입니다. 쿼리 확장(Query Expansion)보다 강력한 검색 성능 향상을 제공합니다.
- RAG: 데이터 전처리(Indexing) 단계의 혁신을 통해 검색 품질을 근본적으로 개선.
- Deep Agents: 에이전트가 정확한 정보를 바탕으로 판단을 내릴 수 있도록 고품질의 지식 공급.
- Knowledge Graph: 텍스트 조각에 메타데이터를 부여한다는 점에서 비정형 데이터의 구조화(그래프화) 초기 단계와 유사.

## 원문 URL
https://www.anthropic.com/news/contextual-retrieval
