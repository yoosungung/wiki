---
title: "Why LLM models are not good at RAG"
related_raw: ["[[wiki/Models/Reasoning-and-Cognition/Why LLM models are not good at RAG.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'llm_applications_and_insights']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

## 요약

최근(2024-2025년) LLM 연구 동향은 SFT(Supervised Fine-Tuning) 기반의 파인튜닝 논문이 크게 줄고, 대부분의 고성능 공개 모델들이 대규모 중간 학습(mid training)과 RL(Reinforcement Learning)을 활용한 전역 최적화를 수행하고 있습니다. 이는 LLM 성능이 상향 평준화되면서 특정 태스크에 대한 SFT가 오히려 전체 성능을 저해하는 경우가 많기 때문입니다. 다만, 상담 챗봇과 같이 워크플로우가 고정된 환경에서는 일관성 유지를 위해 SFT가 여전히 사용되기도 합니다.

성능이 상향 평준화되었음에도 불구하고, LLM은 RAG(Retrieval Augmented Generation)를 효과적으로 활용하지 못하며, 검색을 결합해도 기대만큼의 성능이 나오지 않는 경우가 많습니다. 이는 근본적으로 세 가지 구조적 한계에서 비롯됩니다.

1.  **컨텍스트 길이 한계:**
    *   RAG는 외부 데이터를 컨텍스트에 삽입하는 방식인데, 이는 모델 파라미터에 지식이 내재된 경우보다 정보 효율성이 떨어집니다.
    *   사전 학습 단계에서는 텍스트의 양보다 텍스트의 품질과 정보 밀도가 중요하며, 모델은 긴 텍스트를 가중치에 압축하는 능력을 학습합니다. 하지만 RAG로 투입되는 원본 텍스트는 이러한 내부 압축 과정이 없습니다.
    *   결과적으로 비슷한 정보량을 채우기 위해 더 많은 텍스트를 넣어야 하며, 컨텍스트 길이가 길어질수록 멀리 떨어진 정보의 가중치가 희석되어 성능 저하로 이어집니다.

2.  **외부 컨텍스트 활용 능력 부족:**
    *   **쿼리 의도 전달의 구조적 한계:** 대부분의 RAG는 임베딩 기반 유사도 검색을 사용하지만, 임베딩은 토픽 수준의 유사성은 파악해도 토큰 단위의 지시사항이나 맥락적 의도를 제대로 반영하지 못합니다. 이로 인해 모델이 실제로 필요한 정보가 누락되거나 불필요한 정보가 유입되는 경우가 잦습니다.
    *   **모델 파라미터 지식 외의 지식이 주어졌을 때 내부 지식과의 호환성 문제:** In-Context Learning(ICL)은 온라인 학습과 유사한 효과를 가지지만, RAG로 제공되는 텍스트는 시의성이 중요하거나 공개되지 않은 데이터인 경우가 많아 모델이 접해보지 않은 지식일 가능성이 큽니다. 이는 호환성을 떨어뜨리고 제어하기 어렵게 만듭니다. 반대로 시의성이 중요하지 않거나 공개된 데이터는 이미 프론티어 모델에 학습되었을 가능성이 높아 RAG 시스템 구축 동인이 약해집니다.

3.  **장기 기억 문제:**
    *   대부분의 LLM은 장기 기억을 유지하지 못하여 대화가 길어질수록 사용자의 의도를 잊거나 이상한 방향으로 흘러가기 쉽고, 한번 잘못된 길로 빠지면 회복이 어렵습니다.
    *   최신 프론티어 모델들도 문제가 발생하면 "새로운 턴에서 다시 시작하라"고 권장합니다.
    *   이를 보완하기 위해 검색 LLM에서는 구조화된 출력 기반의 파인튜닝을 하거나, 턴마다 필요한 메모리를 별도로 관리하는 시스템을 추가하기도 합니다. 본질적으로 변경 가능한(mutable) 상태는 관리가 어렵고, 워크플로우를 복잡하게 만들며 새로운 변화에 유연하게 대처하기 힘들게 합니다.

## 참고된 논문/자료 (텍스트 내 직접적인 URL은 아님)

*   `[1] A Practical Approach for Building Production-Grade Conversational Agents with Workflow Graphs`
*   `[2] BeyondWeb: Lessons from Scaling Synthetic Data`
*   `[3] On the Theoretical Limitations of Embedding-Based Retrieval - Google DeepMind`
*   `[4] Learning without training: The implicit dynamics of in-context learning - Google Research`
*   `[5] SFR-RAG: Towards Contextually Faithful LLMs`
*   `[6] Sketch-of-thought: Efficient llm reasoning with adaptive cognitive-inspired sketching`
*   `[7] Atom of thoughts for markov llm test-time scaling`
*   `[8] Zerosearch: Incentivize the search capability of llms without searching`
*   `[9] From matching to generation: A survey on generative information retrieval`
*   `[10] Parametric retrieval augmented generation`

## 노트 링크

*   [[wiki/RAG/GraphRAG]]
*   Knowledge-Graph/GraphRAG-2
*   [[wiki/RAG/Light RAG]]
*   [[wiki/RAG/RAG-Anything - All-in-One RAG System]]
*   Areas/RAG기술현황(1)
*   Areas/RAG기술현황(2)