---
title: RAG-Best-Practices
related_raw:
  - "[[wiki/RAG/RAG-Best-Practices]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - semantic_chunking_and_contextual_rag
type: wiki
status: draft
last_updated: "2026-04-19"
---

# RAG(Retrieval Augmented Generation) 시스템 개선을 위한 모범 사례

**출처**: [원본 링크](https://www.linkedin.com/posts/kalyanksnlp_rag-best-practices-ugcPost-7399335167716331520-crgI)

RAG 시스템을 향상시키기 위한 모범 사례에 대한 논문을 기반으로 한 Kalyan KS의 LinkedIn 게시물 요약입니다.

## 주요 연구 결과

1.  **대조적 In-Context Learning RAG의 우수성:** 제안된 대조적 In-Context Learning RAG가 다른 모든 RAG 변형보다 뛰어난 성능을 보입니다.
2.  **Focus Mode RAG의 효과:** 높은 정밀도와 간결한 검색 문서를 사용하여 기본 모델들을 크게 능가합니다.
3.  **지식 기반 크기보다 품질과 관련성:** RAG 지식 기반의 크기 자체보다 문서의 품질과 관련성이 더 중요합니다.
4.  **효과 미미한 요인들:** 쿼리 확장, 다국어 표현, 문서 크기 변화, 검색 보폭과 같은 요인들은 의미 있는 개선으로 이어지지 않았습니다.
5.  **프롬프트 구성의 중요성:** RAG 아키텍처 내에서도 프롬프트 구성은 여전히 매우 중요합니다.

## 추가 의견

Niharika Tanaya의 댓글에 따르면, 많은 팀이 쿼리 확장 및 검색 보폭 조정과 같은 잘못된 레버를 최적화하고 있습니다. 진정한 투자 수익(ROI)은 문서 관련성, 프롬프트 구성, 검색 정밀도에 있으며, 무차별적인 규모 확장이 아닙니다.

---
## 관련 노트
- [[Areas/RAG기술현황(1)]]
- [[Areas/RAG기술현황(2)]]
- [[wiki/RAG/GraphRAG]]
- [[wiki/Engineering/Prompt-Engineering/프롬프트_컨텍스트_엔지니어링]]
