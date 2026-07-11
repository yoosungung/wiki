---
title: GraphRAG - Part 3 - Querying and Conclusion
related_raw:
  - "[[wiki/RAG/GraphRAG - Part 3 - Querying and Conclusion]]"
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


여기서 직감은 각 커뮤니티가 쿼리에 대한 주제별 응답을 제공할 수 있으며, 이러한 응답을 결합하여 소스 문서의 정보에 대한 매우 높은 수준의 질문에 답할 수 있다는 것입니다.

### 나의 접근

1. 1. 각 커뮤니티에서 가장 유사한 노드와 가장자리를 식별합니다([링크](https://github.com/Black-Tusk-Data/minikg/blob/7aa6249b2fe986c4cef462deea8477d5c3880d4e/minikg/kg_searcher.py#L63))
2. 2. 너무 다른 응답에서 커뮤니티를 제외합니다([링크](https://github.com/Black-Tusk-Data/minikg/blob/7aa6249b2fe986c4cef462deea8477d5c3880d4e/minikg/kg_searcher.py#L76))
3. 3. 각 관련 커뮤니티에 대해 관련 엔티티 및 관계 설명의 맥락과 함께 질문에 대한 답변을 생성합니다([링크](https://github.com/Black-Tusk-Data/minikg/blob/7aa6249b2fe986c4cef462deea8477d5c3880d4e/minikg/kg_searcher.py#L168))
4. 4. 소스 자료에서 관련이 없거나 근거가 없다고 간주되는 응답을 제거합니다([링크](https://github.com/Black-Tusk-Data/minikg/blob/7aa6249b2fe986c4cef462deea8477d5c3880d4e/minikg/kg_searcher.py#L188))
5. 5. 각 관련 커뮤니티의 답변을 사용하여 쿼리에 대한 최종 응답을 생성합니다([링크](https://github.com/Black-Tusk-Data/minikg/blob/7aa6249b2fe986c4cef462deea8477d5c3880d4e/minikg/kg_searcher.py#L205))

### Microsoft GraphRAG 접근 방식

이 논문의 구현은 각 커뮤니티의 _요약에_ 대한 벡터 검색을 사용하여 관련 커뮤니티가 식별된다는 점을 제외하고는 `minikg` 구현과 매우 유사합니다. 내가 이 압정을 취하지 않은 주된 이유는 비용 때문이었다 - 나는 이미 OpenAI 크레딧에 약 20달러를 썼고, 각 커뮤니티를 요약하는 데 더 많은 돈을 쓰고 싶어하지 않았다. 현실적으로, 나는 '커뮤니티 요약' 접근 방식이 관련 커뮤니티를 식별하는 데 우월할 가능성이 높다고 생각한다.

---

## 마무리 발언

내 관점에서 볼 때, 'GraphRAG'의 개념은 명확한 범용 구현을 가진 일률적인 개념이 아니다. Microsoft 구현은 확실히 잘 생각되고 사용 가능하지만, 특히 고유한 사용 사례에 대한 모든 디자인 선택이 올바른 선택이라고 믿을 이유가 없습니다.

---

## 이전

- [[wiki/RAG/GraphRAG]]
- [[wiki/RAG/GraphRAG - Part 2 - Implementation]]

## 다음

- [[wiki/RAG/GraphRAG - Part 4 - Microsoft Implementation]]
