---
title: "Agent-R1 Training Powerful LLM Agents with End-to-End Reinforcement Learning"
related_raw: ["[[wiki/Models/RL/Agent-R1 Training Powerful LLM Agents with End-to-End Reinforcement Learning.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'llm_agent_training_rl']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---


이 논문은 복잡한 문제를 해결하기 위해 도구 사용을 통해 환경과 상호작용하는 LLM(대규모 언어 모델) 에이전트를 훈련하는 데 있어 강화 학습(RL)의 효과적인 적용이 초기 단계에 있으며, 유연하고 확장 가능한 훈련 프레임워크가 부족하다는 문제점을 다룹니다. 이를 해결하기 위해 저자들은 Agent-R1이라는 모듈식, 유연하며 사용자 친화적인 RL 기반 LLM 에이전트 훈련 프레임워크를 제안합니다.

## 주요 기술적 내용

1.  **LLM 에이전트를 위한 마르코프 결정 과정(MDP) 확장:**
    *   **상태 공간 (State Space, $\mathcal{S}$):** 정적 LLM은 주로 현재 텍스트 컨텍스트(초기 프롬프트 및 생성된 토큰 시퀀스)를 포함하지만, LLM 에이전트의 상태는 다중 턴 상호작용 및 환경 피드백의 전체 이력을 포함하여 훨씬 더 포괄적입니다.
    *   **행동 공간 (Action Space, $\mathcal{A}$):** 정적 LLM의 행동은 다음 토큰을 선택하는 것이지만, LLM 에이전트의 경우 특정 토큰 시퀀스가 외부 도구 또는 API를 호출하는 명령으로 해석될 수 있어 능동적인 환경 개입이 가능합니다.
    *   **상태 전이 확률 (State Transition Probability, $\mathcal{P}$):** 정적 LLM의 상태 전이는 결정론적이지만, LLM 에이전트의 상태 전이는 도구 사용으로 인한 환경 상호작용을 통합하여 확률론적일 수 있습니다.
    *   **보상 함수 (Reward Function, $\mathcal{R}$):** 정적 LLM은 일반적으로 최종 출력의 전체 품질을 평가하는 희소한 최종 보상을 받지만, LLM 에이전트는 작업 완료를 위한 최종 결과 보상 외에 효과적인 도구 호출과 같은 중간 단계에 대한 프로세스 보상($r_p$)을 받을 수 있어 더 풍부하고 밀도 높은 보상 구조를 가집니다.

2.  **Agent-R1 프레임워크:**
    *   **Tool 및 ToolEnv 모듈:**
        *   **Tool:** 특정 원자적 행동(예: 외부 API 호출, 코드 실행, 데이터베이스 접근)을 캡슐화하고 해당 행동의 원시 결과를 반환하는 역할을 합니다. `BaseTool` 추상 기본 클래스를 통해 표준화되며, `execute` 메서드와 JSON Schema 기반의 매개변수 정의를 포함합니다.
        *   **ToolEnv:** RL 환경 내에서 오케스트레이터 및 인터프리터 역할을 합니다. Tool의 원시 출력을 처리하여 에이전트의 인지 상태와 전체 작업 진행에 미치는 영향을 결정합니다. 상태 전이 관리, 보상 신호 계산, 새로운 상태 정보 패키징을 담당합니다. `BaseToolEnv` 추상 기본 클래스를 통해 `step` 메서드를 구현합니다.
    *   **다중 턴 궤적에서 에이전트 정책 최적화:**
        *   **정제되고 정렬된 이점 계산 (Refined and Aligned Advantage Calculation):** 최종 결과 보상뿐만 아니라 `ToolEnv`에서 수집된 프로세스 보상을 명시적으로 통합합니다. `Action Mask`를 사용하여 에이전트가 생성한 토큰에만 이점을 할당하여 정확한 크레딧 할당을 보장합니다.
        *   **마스킹된 정책 최적화 (Masked Policy Optimization - Actor Loss):** `Action Mask`를 사용하여 에이전트가 생성한 토큰에 대해서만 손실을 계산하여 정책 업데이트의 정확성을 높입니다.
        *   **가치 함수 업데이트 (Value Function Update - Critic Loss):** 비평가 모델은 궤적에서 얻은 관찰된 보상(프로세스 및 결과 보상 포함)을 사용하여 예상 누적 보상(가치)을 더 정확하게 추정하도록 훈련됩니다.

3.  **실험 연구:**
    *   **설정:** 다중 홉 질의응답(MultihopQA) 벤치마크(HotpotQA, 2WikiMultihopQA, Musique)에서 Qwen2.5-3B-Instruct 모델과 `wikisearch` 도구를 사용하여 실험을 수행했습니다.
    *   **결과:** PPO, GRPO 등 다양한 RL 알고리즘을 Agent-R1 프레임워크 내에서 평가한 결과, 모든 RL 훈련 에이전트가 Naive RAG 및 Base Tool Call과 같은 기준선을 크게 능가했습니다. 특히 GRPO가 가장 좋은 성능을 보였습니다.
    *   **어블레이션 연구:** 손실 마스크(loss mask)와 이점 마스크(advantage mask)가 정책 최적화에 중요하며, 이들을 비활성화할 경우 성능이 저하됨을 확인했습니다.

## 관련 링크

*   [[wiki/Models/RL/Self-Evolving Agents - 자가 학습형 AI 에이전트 재훈련 매뉴얼]]
*   [[wiki/Agents/Implementation/Model-Native-Agentic-AI]]
*   [[wiki/Models/RL/RLHF]]
*   [[wiki/Models/Reasoning-and-Cognition/Andrej_Karpathy_on_AGI]]
*   [[wiki/Models/Reasoning-and-Cognition/LLM_Parallel_Thinking_Parallel-R1]]
*   [[Archive/AI Agent 구성 (내부 교육용)]]

## References

*   **Agent-R1 GitHub 저장소:** https://github.com/0russwest0/Agent-R1
*   **논문 PDF:** [https://arxiv.org/pdf/2511.14460v1](https://arxiv.org/pdf/2511.14460v1)
