---
title: GraphRAG - Part 2 - Implementation
related_raw:
  - "[[wiki/RAG/GraphRAG - Part 2 - Implementation]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - graphrag_implementation
type: wiki
status: draft
last_updated: "2026-04-19"
---


우리가 따를 GraphRAG 시스템을 구축하는 접근 방식은 [Microsoft GraphRAG 구현에서](https://github.com/microsoft/graphrag) 채택되었습니다. 우리 자신의 GraphRAG 구현에 도달하기 위해 본질적으로 살펴볼 수 있는 [첨부 문서가](https://arxiv.org/html/2404.16130v1) 있습니다([이 기사의 첨부된 저장소](https://github.com/Black-Tusk-Data/minikg/tree/meta-earnings-example) 참조). 유용한 지식 그래프는 다음 단계를 통해 생성됩니다.

1. 1. 제공된 문서를 LLM의 컨텍스트 창에 맞출 수 있는 청크로 분할합니다.
2. 2. 각 청크에 대해, 그 안에 설명된 엔티티와 관계를 _해당 청크에 대한_ 지식 그래프로 추출합니다.
3. 3. 각 청크의 지식 그래프를 하나의 최상위 지식 그래프로 병합합니다.
4. 4. 최상위 지식 그래프를 [_커뮤니티로_](https://en.wikipedia.org/wiki/Community_structure) 분할합니다. 각 커뮤니티는 당면한 지식 기반 내에서 고유한 개념을 나타냅니다.

이 GraphRAG 접근 방식의 전제는 각 지식 그래프를 구축할 때 '추가 시끌'(즉, 아마도 중복된 가장자리/노드를 만들 수 있음)이 될 수 있다는 것입니다. 왜냐하면 궁극적으로 우리는 하위 그래프의 중복성을 추상화하는 '커뮤니티'와 인터페이스할 것이기 때문입니다.

## 지식 그래프 구성 연습

### 청킹

이론적으로, 당신은 아마도 당신의 LLM의 컨텍스트 창의 크기에 따라 문서 코퍼스를 청크하는 것을 벗어날 수 있을 것입니다. 그러나 실제로, 나는 많은 모델의 출력 한계에 맞추기에는 큰 청크 내에 너무 많은 정보가 있을 수 있다는 것을 발견했고, 출력의 품질이 떨어질 수 있다는 것은 말할 것도 없다. 그런 이유로, 청크 크기는 아마도 당신이 당면한 특정 코퍼스에 따라 조정해야 할 것입니다. ['문서 분할' 빌드 단계와](https://github.com/Black-Tusk-Data/minikg/blob/meta-earnings-example/minikg/build_steps/step_split_doc.py) [문서 '분할기' 구현을](https://github.com/Black-Tusk-Data/minikg/blob/meta-earnings-example/minikg/splitter.py) 참조하십시오.

### 실체

Microsoft 구현에서는 엔티티와 관계가 동시에 추출됩니다. LLM에 대한 작업을 단순화하기 위해, 내 접근 방식은 이것을 2개의 요청으로 나누는 것이었다 - 하나는 엔티티를 추출하는 것이고 후속 요청은 식별된 엔티티 간의 관계를 추출하는 것이었다. 이 단계에서 내가 가치 있다고 생각하는 또 다른 것은 우리가 관심 있는 특정 종류의 엔티티를 명시하는 것이다. 출력 모양의 JSON 스키마에서 "enum" 속성으로 이를 적용할 수도 있습니다. 메타 수익 통화 성적 증명서 예에서, 내가 시행한 엔티티 유형은 다음과 같다:

`    ["ORGANIZATION",   "EVENT",   "PRODUCT",   "PERSON",   "OPPORTUNITY",   "CHALLENGE"]  `

[엔티티/관계 추출 단계와](https://github.com/Black-Tusk-Data/minikg/blob/meta-earnings-example/minikg/build_steps/step_extract_chunk_kg.py) [엔티티 추출 구현을](https://github.com/Black-Tusk-Data/minikg/blob/meta-earnings-example/minikg/extractor/entity_extractor.py) [](https://github.com/Black-Tusk-Data/minikg/blob/meta-earnings-example/minikg/build_steps/step_extract_chunk_kg.py)참조하십시오[.](https://github.com/Black-Tusk-Data/minikg/blob/meta-earnings-example/minikg/build_steps/step_extract_chunk_kg.py)

### 관계

이 단계에서, 방금 엔티티를 추출한 동일한 청크에 대해, 우리는 LLM에게 식별된 엔티티 간의 모든 의미 있는 관계를 추출하도록 요청할 것입니다. [관계 추출 구현을](https://github.com/Black-Tusk-Data/minikg/blob/meta-earnings-example/minikg/extractor/entity_relationship_extractor.py) 참조하십시오. GraphRAG 구현은 이를 철저히 수행하기 위해 많은 노력을 기울입니다. 실제로 '모든 관계가 추출되었는지' 여부를 확인하기 위해 또 다른 LLM 요청을 수행하고 만족할 때까지 '관계 추출' 요청을 반복적으로 수행합니다. 내가 취한 접근 방식과 Microsoft 논문의 접근 방식의 한 가지 주요 차이점은 내가 엔티티 _간의 여러 관계를_ 허용한 반면 Microsoft 논문은 그렇지 않다는 것이다. 이것은 노드 사이에 그러한 여러 모서리를 허용하는 [_멀티그래프라고_](https://en.wikipedia.org/wiki/Multigraph) 불리는 상당히 다른 종류의 그래프를 초래한다. 이것은 우리가 커뮤니티 탐지 알고리즘에 대해 논의할 때 관련이 있을 것이다.

### 그래프 병합

이제 우리는 많은 작은 지식 그래프를 가지고 있으며, 그것들을 하나의 '마스터' 그래프로 결합하고 싶습니다. GraphRAG의 접근 방식은 실제로 매우 간단합니다. 그래프 G의 노드 A가 그래프 H의 노드 A와 동일한 엔티티를 나타내면, 우리는 G의 A의 모든 가장자리와 H의 A의 모든 가장자리를 가진 병합된 그래프에서 노드 A'를 만듭니다.

![](https://blacktuskdata.com/images/kg-intro/merging-graphs.svg)

새로운 노드는 단순히 모든 가장자리와 함께 추가됩니다. 노드 간의 다중 관계를 모델링하려는 시도는 없습니다. 두 엔티티는 단일 에지에 의해서만 연결됩니다([에지 병합 구현](https://github.com/microsoft/graphrag/blob/6d21ef268377e319a165ca2250bd6841737df1ad/graphrag/index/operations/merge_graphs/merge_graphs.py#L128) 및 [기본 에지 병합 작업](https://github.com/microsoft/graphrag/blob/6d21ef268377e319a165ca2250bd6841737df1ad/graphrag/index/operations/merge_graphs/merge_graphs.py#L24) 참조). 기본적으로, 병합 과정에서 두 개체 사이에 발생한 마지막 관계는 최종 그래프에서 그들 사이의 유일한 관계가 될 것이다.
내 구현에서, 노드 사이에 여러 개의 가장자리를 허용하고 있기 때문에, 나는 그들의 설명의 코사인 유사성을 사용하여 병합된 노드의 가장자리 사이에서 중복을 제거하려고 시도한다. 노드 사이에 단일 가장자리를 유지하는 또 다른 접근 방식은 두 엔티티 사이의 다른 가장자리를 병합할 때 두 엔티티 간의 관계를 지속적으로 요약(LLM을 사용하여)하는 것입니다.

### 공동체

커뮤니티 감지 단계를 위해 우리는 앞서 언급한 강력한 그래프 이론 수학의 일부를 활용할 것입니다. GraphRAG 구현은 커뮤니티를 감지하기 위해 ['라이덴 커뮤니티 탐지'](https://en.wikipedia.org/wiki/Leiden_algorithm)라는 알고리즘을 사용합니다([링크](https://github.com/microsoft/graphrag/blob/6d21ef268377e319a165ca2250bd6841737df1ad/graphrag/index/operations/cluster_graph.py#L134)). 안타깝게도 라이덴 알고리즘은 내가 구현에서 만든 것과 같은 다중 그래프가 아닌 엄격한 그래프에서만 실행할 수 있습니다. 따라서 나는 멀티 그래프에서 작동할 수 있는 ['루뱅 커뮤니티 탐지'](https://en.wikipedia.org/wiki/Louvain_method)라는 다른 알고리즘을 사용해야 했다. 라이덴 알고리즘은 루베인의 일부 결함을 개선하기 위해 개발되었지만, 개념 증명을 위해 이러한 결함을 받아들이기로 결정했습니다.

---

## 이전

- [[wiki/RAG/GraphRAG]]

## 다음

- [[wiki/RAG/GraphRAG - Part 3 - Querying and Conclusion]]
- [[wiki/RAG/GraphRAG - Part 4 - Microsoft Implementation]]
