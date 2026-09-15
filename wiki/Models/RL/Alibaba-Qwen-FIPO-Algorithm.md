---
title: "Alibaba-Qwen-FIPO-Algorithm"
related_raw: ["[[wiki/Models/RL/Alibaba-Qwen-FIPO-Algorithm.md]]"]
tags: ['wiki', 'ai_core', 'ai_ml_development', 'grpo_dpo_reinforcement_learning']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# FIPO: DeepSeek-R1 GRPO를 능가하는 새로운 강화학습 알고리즘

**날짜:** 2026-04-08
**출처**: [Alibaba Qwen Team / The Decoder](https://the-decoder.com/alibaba-qwen-team-presents-fipo-a-better-alternative-to-deepseeks-grpo/)

## 요약
알리바바 Qwen 팀이 발표한 **FIPO(Future-KL Influenced Policy Optimization)**는 DeepSeek-R1의 GRPO 방식의 한계를 극복하고 추론 능력을 극대화한 강화학습 알고리즘입니다.

## 핵심 내용
- **GRPO의 문제점:** 최종 결과에 기반한 균등 보상 배분으로 인해 추론 체인의 정교함이 부족함.
- **FIPO의 혁신:** 각 토큰이 이후 추론에 미치는 '미래 영향력'을 계산하여 토큰 단위로 보상을 차등 배분.
- **성능:** 
    - 추론 토큰 길이를 4,000개에서 10,000개 이상으로 확장.
    - 수학 벤치마크(AIME 2024)에서 DeepSeek-R1-Zero 능가 (정확도 58%).
- **공개 계획:** Qwen 팀은 해당 훈련 시스템 전체를 오픈소스로 공개할 예정.

## 관련 노트
- [[wiki/Models/RL/DeepSeek-R1-GRPO-Guide]]
- [[wiki/Models/RL/NVIDIA GDPO: 다중 보상 RL의 GRPO 결함 해결]]
- [[wiki/Models/RL/GRPO-Scaling-Laws-Efficiency]]
