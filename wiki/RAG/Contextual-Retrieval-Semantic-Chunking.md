---
title: Contextual-Retrieval-Semantic-Chunking
related_raw:
  - "[[wiki/RAG/Contextual-Retrieval-Semantic-Chunking]]"
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

# Contextual Retrieval 및 Semantic Chunking (2026 RAG 최적화)

RAG(검색 증강 생성)의 성능을 극대화하기 위해 2026년 현재 가장 널리 사용되는 두 가지 핵심 기술인 **Contextual Retrieval**과 **Semantic Chunking**에 대해 설명합니다.

## 1. Contextual Retrieval (문맥적 검색)
Anthropic에서 제안한 기술로, 전통적인 RAG에서 문서 분할 시 발생하는 '문맥 소실' 문제를 해결합니다.

### 핵심 개념
*   **Chunk Contextualization:** 각 텍스트 청크(Chunk)를 벡터화하기 전, 해당 청크가 전체 문서 내에서 어떤 위치에 있고 어떤 의미를 갖는지 설명하는 짧은 문맥(약 50~100토큰)을 추가합니다.
*   **Hybrid Search:** 벡터 기반의 'Contextual Embeddings'와 키워드 기반의 'Contextual BM25'를 결합하여 검색 정확도를 높입니다.

### 성능 및 효율성
*   **실패율 감소:** 검색 실패율을 최대 **67%**까지 줄일 수 있습니다 (기존 5.7% → 1.9%).
*   **프롬프트 캐싱 (Prompt Caching):** Claude의 프롬프트 캐싱 기능을 활용하면 수만 개의 청크에 문맥을 생성하는 비용을 **90% 이상 절감**하고 속도를 **2배 이상** 높일 수 있습니다.

---

## 2. Semantic Chunking (세만틱 청킹)
단순히 글자 수나 단락 기준이 아닌, 내용의 '의미적 경계'를 기준으로 문서를 나누는 방식입니다.

### 기술적 특징
*   **의미적 유사도 측정:** 인접한 문장 간의 임베딩 유사도를 계산하여 유사도가 급격히 떨어지는 지점을 경계로 설정합니다.
*   **Late Chunking:** 전체 문서를 먼저 임베딩한 후, 토큰 수준에서 풀링(Pooling)을 수행하여 각 청크가 전체 문서의 맥락을 유지하도록 하는 최신 기법입니다.

### 기대 효과
*   문맥이 끊기지 않는 완성도 높은 정보를 모델에 전달하여 '환각(Hallucination)' 현상을 줄이고 답변의 질을 높입니다.

## 3. 관련 링크 및 참고 자료
*   [Anthropic: Contextual Retrieval 공식 블로그](https://www.anthropic.com/news/contextual-retrieval)
*   [GitHub: Contextual Embeddings Cookbook](https://github.com/anthropics/anthropic-cookbook)
*   기존 노트 연동: [[wiki/RAG/GraphRAG|GraphRAG 개요]], [[wiki/RAG/RAG-Best-Practices|RAG 베스트 프랙티스]]

## 4. 관련 이미지 (개념도)
![Contextual Retrieval Workflow](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww.datocms-assets.com%2F60316%2F1726514652-contextual-retrieval.png&w=1920&q=75)
*(출처: Anthropic 공식 블로그)*
