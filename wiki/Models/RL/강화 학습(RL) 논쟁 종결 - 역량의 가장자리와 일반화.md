---
title: "강화 학습(RL) 논쟁 종결 - 역량의 가장자리와 일반화"
related_raw: ["[[wiki/Models/RL/강화 학습(RL) 논쟁 종결 - 역량의 가장자리와 일반화.md]]"]
tags: ['wiki', 'ai_core', 'ai_ml_development', 'grpo_dpo_reinforcement_learning']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# 강화 학습(RL) 논쟁 종결 - 역량의 가장자리와 일반화의 비밀

**요약:**
Ludovico Bessi의 게시물과 관련 댓글들은 강화 학습(RL)이 모델의 추론 능력을 확장하는지, 아니면 단순히 기존 기술을 다듬는 것인지에 대한 오랜 논쟁에 종지부를 찍습니다. 결론적으로, 두 주장 모두 옳았으며, 이는 측정 방식의 차이에서 비롯된 것이었습니다.

**주요 연구 결과:**

1.  **"역량의 가장자리(Edge of Competence)"에서만 RL이 작동:**
    *   RL은 모델이 너무 쉽거나 너무 어려운 작업을 훈련할 때는 능력 향상에 전혀 기여하지 못합니다.
    *   최적의 지점은 모델이 `pass@1`에서는 실패하지만 `pass@k`에서는 성공하는 작업, 즉 모델의 현재 역량 경계에 있는 작업입니다. 이는 RL이 모델의 잠재력을 최대한 발휘할 수 있는 "스위트 스팟"입니다.

2.  **일반화를 위한 "1% 규칙":**
    *   RL은 무에서 유를 창조할 수 없습니다. 그러나 새로운 도메인에 대한 사전 훈련 노출이 0%일 때는 완전히 실패하지만, 단 1%의 노출만 있어도 가장 어려운 작업으로 일반화하여 `pass@128`에서 60% 이상의 성능 향상을 보입니다. 이는 RL이 작은 "씨앗"만 있으면 기존 능력을 크게 확장할 수 있음을 시사합니다.

3.  **"중간 훈련(Mid-training)"의 숨겨진 힘:**
    *   Qwen 모델이 LLaMA보다 RL에 더 잘 반응하는 이유 중 하나는 "중간 훈련"에 있습니다. 중간 훈련은 RL이 활용할 수 있는 사전 지식(prior)을 모델에 심어줍니다.
    *   중간 훈련과 가벼운 RL을 결합하면 순수 RL보다 OOD(Out-of-Distribution) 작업에서 10.8% 더 나은 성능을 달성합니다. 이는 RL의 효과를 극대화하기 위해 모델의 훈련 단계와 방법을 신중하게 고려해야 함을 의미합니다.

4.  **"프로세스 보상(Process Rewards)"으로 보상 해킹 해결:**
    *   결과(outcome) 보상과 단계별 검증(step-by-step verification)을 혼합하는 "프로세스 보상" 방식은 `pass@1` 성능을 4-5% 향상시킵니다.
    *   이를 통해 모델은 지름길을 악용하는 대신, 충실한 추론(faithful reasoning)으로 전환하게 됩니다. 이는 RL 훈련에서 보상 설계의 중요성을 강조하며, 모델이 원하는 행동을 학습하도록 유도하는 데 필수적입니다.

**댓글을 통한 추가 통찰:**

*   **RL의 역할 재정의:** Brian Huang는 RL이 새로운 능력을 이끌어내지 못한다는 주장이 틀렸다고 언급하며, IMAMA S.는 RL이 마법 같은 추론 업그레이드가 아니라, 이미 작동하는 시스템의 미세 조정에 가깝다고 설명합니다. SFT(Supervised Fine-Tuning)가 펌웨어를 플래싱하는 것이라면, RL은 피드백을 통해 가중치를 실시간으로 조정하는 것과 같다는 비유를 들며 RL 훈련에 인내심이 필요하다고 강조합니다.
*   **잠재된 구조의 증폭:** Shuvam Chatterjee와 Eun-gu(Nick) Heo는 RL이 새로운 능력을 창조하기보다 기존 구조를 증폭시키는 역할을 한다고 설명합니다. Georgy Zoloev는 "역량의 가장자리"와 1% 노출, 중간 훈련의 중요성을 다시 한번 강조하며, 프로세스 보상 혼합이 OOD 평가에서 순수 결과 RL보다 나은지 질문합니다.
*   **무작위 보상의 효과:** Pushpak Pujari는 Qwen2.5 연구에서 순수한 무작위 노이즈 보상이 실제 정답 보상만큼 효과적일 수 있음을 지적합니다. 이는 RLVR이 새로운 추론을 가르치는 것이 아니라, 사전 훈련된 잠재된 코드 추론 능력을 활성화시켰을 뿐일 수 있다는 통찰을 제공합니다.

결론적으로, RL은 모델의 잠재력을 최대한 활용하고 특정 작업에 대한 성능을 미세 조정하는 강력한 도구이지만, 그 효과는 모델의 사전 훈련 상태, 훈련 작업의 난이도, 그리고 보상 설계 방식에 크게 좌우됩니다. RL은 무에서 유를 창조하는 마법이 아니라, 모델이 이미 가지고 있는 "역량의 가장자리"에서 가장 효과적으로 작동하며, 적절한 "씨앗"과 "중간 훈련"을 통해 일반화 능력을 크게 향상시킬 수 있습니다.

**추출된 URL:**
*   `https://open.substack.com/pub/machinelearningatscale/p/the-rl-training-recipe-when-post?r=jeeym&utm_campaign=post&utm_medium=web`
*   `https://lnkd.in/dxsfpsaY`
*   `https://lnkd.in/g96KD8uS`
*   `https://rehanganapathy.github.io`
*   `https://lnkd.in/gMMXmVMb?`
*   `https://arxiv.org`
*   `https://lnkd.in/euu5X7gu`

**관련 노트:**
*   [[wiki/Models/RL/NVIDIA GDPO: 다중 보상 RL의 GRPO 결함 해결]]
*   [[wiki/Models/RL/RLHF]]
*   [[wiki/Models/RL/Agent-R1 Training Powerful LLM Agents with End-to-End Reinforcement Learning]]
*   [[wiki/Models/Reasoning-and-Cognition/LLM 학습 패러다임]]
*   [[wiki/Models/SFT/Fine-Tuning]]