---
title: GraphRAG - Part 4 - Microsoft Implementation
related_raw:
  - "[[wiki/RAG/GraphRAG - Part 4 - Microsoft Implementation]]"
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


https://github.com/microsoft/graphrag

**5. Graph Communities → Community Summaries**
이 단계에서는 **그래프 커뮤니티(community summaries)를 생성**합니다.

**동작 과정**
1. **커뮤니티 감지 (Community Detection)**
	• 그래프에서 서로 강하게 연결된 노드 그룹을 **Leiden 알고리즘**을 사용해 커뮤니티로 분할합니다.
	• 이 단계에서 **계층적(hierarchical) 구조**가 형성되며, 각 계층에서 세부적인 서브커뮤니티들이 만들어질 수 있습니다.
2. **커뮤니티 요약 생성**
	• 각 커뮤니티에 속한 요소들(노드, 엣지, 관련된 속성)을 기반으로 **LLM을 이용한 요약(summarization)을 수행**합니다.
	• Leaf-Level 커뮤니티에서는 모든 요소를 포함하여 요약을 수행하며, 상위 계층에서는 보다 압축적인 요약이 생성됩니다.
	• 요약 과정에서는 **가장 중요한 노드와 관계를 우선순위로 정리**하여 사용합니다.

**핵심 개념**
	• 커뮤니티 요약은 전체 데이터 세트의 구조와 의미를 **전반적으로 이해할 수 있도록** 도와줍니다.
	• 계층적 구조를 통해 **대규모 데이터 세트에서도 요약을 단계적으로 수행**할 수 있습니다.
	• 사용자가 특정 질문을 하기 전에 **데이터의 주요 주제나 구조를 탐색할 수 있도록 지원**합니다.

---
**6. Community Summaries → Community Answers → Global Answer**
이 단계에서는 **사용자의 질의(Query)에 대한 최종적인 답변**을 생성합니다.

**동작 과정**
1. **사용자 질의 입력**
	• 사용자가 데이터 세트에 대한 질문을 입력합니다.
2. **각 커뮤니티 요약에서 부분적 응답 생성 (Community Answers)**
	• 생성된 커뮤니티 요약을 기반으로 각 커뮤니티에서 질의와 관련된 부분을 추출하여 **부분적 응답(Partial Answers)을 생성**합니다.
	• **병렬처리**를 통해 여러 커뮤니티에서 동시에 응답을 생성할 수 있습니다.
	• 응답의 **유용성 점수(0~100점)를 LLM이 자체적으로 평가**하여 관련성이 낮은 응답을 필터링합니다.
3. **최종 응답(Global Answer) 생성**
	• 가장 관련성이 높은 커뮤니티 응답을 우선순위에 따라 정렬한 후, 이를 **하나의 글로벌 응답으로 통합(summarization)** 합니다.
	• 이때, 여러 커뮤니티에서 나온 답변을 취합하여 **보다 종합적이고 포괄적인 답변**을 생성합니다.

---
구현
https://github.com/microsoft/graphrag

1. **커뮤니티 감지 및 요약 생성 (5번 단계)**
• graphrag/indexing/community_detection.py: 이 파일은 Leiden 알고리즘을 사용하여 그래프에서 커뮤니티를 감지하는 기능을 포함하고 있습니다.
• graphrag/indexing/summarization.py: 이 파일은 감지된 각 커뮤니티에 대해 LLM을 활용하여 요약을 생성하는 기능을 다룹니다.

2. **커뮤니티 요약을 활용한 질의응답 및 최종 응답 생성 (6번 단계)**
• graphrag/query_engine/query_processor.py: 이 파일은 사용자 질의에 대해 관련된 커뮤니티 요약을 검색하고, 부분적인 응답을 생성한 후, 이를 종합하여 최종 응답을 생성하는 로직을 포함하고 있습니다.

---

## 이전

- [[wiki/RAG/GraphRAG]]
- [[wiki/RAG/GraphRAG - Part 2 - Implementation]]
- [[wiki/RAG/GraphRAG - Part 3 - Querying and Conclusion]]
