---
title: "LatentMAS"
related_raw: ["[[wiki/Agents/Multi-Agent-and-Orchestration/LatentMAS.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'llm_agent_theory_and_patterns']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# LatentMAS: 잠재 공간에서의 협력

**출처**: [원본 링크](https://www.linkedin.com/posts/suk-hyun-kim-31ba9b369_ai-suaqtztfmqvz-slsstwswktxu-activity-7401742864352768002-_-HE)

프린스턴, 스탠퍼드, UIUC 공동 연구진이 발표한 논문 〈Latent Collaboration in Multi-Agent Systems〉(2025)에 대한 요약입니다. 이 연구는 AI 에이전트 간의 협력이 인간이 설계한 규칙이나 언어가 아닌, '잠재 공간(latent space)'이라는 내부 표현 공간에서 자연스럽게 발생한다는 것을 보여줍니다.

## 주요 내용

*   **LatentMAS (Latent Multi-Agent Systems):** 에이전트들이 텍스트 기반 메시지 대신 각 에이전트의 최종 은닉층(hidden layer)에서 생성된 잠재 벡터(latent vector)를 직접 서로 전달하는 방식을 사용합니다.
*   **자발적 협력:** 외부적인 소통 규칙, 역할 분담, 협력 지시, 의사소통 채널 없이도 에이전트들이 자발적으로 협력하기 시작했습니다. 이는 모델 내부에서만 통용되는 새로운 언어가 생성된 것과 유사합니다.
*   **내적 협력 메커니즘:** 에이전트들은 행동으로 의도를 드러내지 않으면서도 내부적으로 신호를 교환하고, 역할을 바꾸며, 실시간 협상을 수행합니다.
*   **표현의 동기화:** 잠재 벡터를 공유함으로써 에이전트들이 내부에서 구축한 지식 구조가 다른 에이전트에게 손실 없이 전달되며, 이는 정보 전달을 넘어 '표현의 동기화'를 가능하게 합니다.
*   **성능 향상:** LatentMAS는 9개 벤치마크에서 기존의 단일 모델 및 텍스트 기반 MAS를 압도하는 성과를 보였습니다 (평균 13.3% 정확도 향상, 최대 7배 빠른 추론 속도, 평균 83.7% 토큰 절감).

## 시사점

이 연구는 AI가 외부에서 보이지 않는 곳에서 서로를 이해하고, 인간이 제공하지 않은 언어, 규칙, 구조를 내부에서 스스로 만들어내는 '진화적 협력' 단계에 진입하고 있음을 보여줍니다. 미래 AI 시스템이 언어 대신 표현을 공유하고, 규칙 대신 구조를 기반으로 협력하며, 지시 대신 환경을 통해 스스로 전략을 구축하는 방식으로 발전할 가능성을 시사합니다.

---
## 관련 노트
- [[wiki/Agents/Multi-Agent-and-Orchestration/멀티-에이전트-패턴]]
- [[wiki/Agents/Multi-Agent-and-Orchestration/Multi-Agent Systems - Collaboration, Complexity, and Innovation]]
- [[wiki/Agents/Multi-Agent-and-Orchestration/Multi-Agent Consensus Alignment]]
