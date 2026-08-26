---
title: "NVIDIA-ToolOrchestra"
related_raw: ["[[wiki/Agents/Multi-Agent-and-Orchestration/NVIDIA-ToolOrchestra.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'llm_systems_projects']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# NVIDIA ToolOrchestra

**출처**: [원본 링크](https://www.linkedin.com/posts/h4y3j1n_nvidia-activity-7402119478349905921-dGF5)

NVIDIA가 AI 에이전트 비용 문제를 해결하기 위한 프레임워크인 "ToolOrchestra"를 공개했습니다.

## 주요 내용

ToolOrchestra는 80억(8B) 파라미터의 작은 오케스트레이터 모델이 GPT-5, Claude와 같은 대규모 언어 모델(LLM) 및 전문 모델들을 적재적소에 호출하여 더 나은 결과를 도출하는 방식입니다. 이는 단일 거대 모델에 의존하는 대신, 여러 도구를 효율적으로 조율하는 발상의 전환을 보여줍니다.

### 주요 기술적 성과 및 특징

*   **HLE 벤치마크:** GPT-5(35.1%)를 능가하는 37.1%의 성능을 달성했습니다.
*   **비용 효율성:** τ2-Bench 및 FRAMES 벤치마크에서 GPT-5 대비 30%의 비용으로 더 높은 성능을 제공합니다.
*   **다목적 RL 훈련:** 정확도, 효율성, 사용자 선호도를 동시에 최적화합니다.
*   **도구 일반화:** 훈련 시 접하지 못한 새로운 도구에 대해서도 견고하게 작동하는 능력을 보여줍니다.
*   **오픈소스:** 모델 가중치, 코드, 데이터셋 전체가 공개되었습니다.

이 접근 방식은 비용 효율성이 중요한 프로덕션 환경에서 특히 유용할 것으로 예상됩니다.

## 관련 링크

*   **논문:** https://lnkd.in/geWm6W2w
*   **GitHub:** https://lnkd.in/gYxfK3b6

---
## 관련 노트
- [[wiki/Agents/Multi-Agent-and-Orchestration/멀티-에이전트-패턴]]
- [[wiki/Agents/Robotics-and-VLA/NVIDIA_Physical_AI]]
- [[wiki/Models/RL/RL-학습의-한계]]
