---
title: "RL-학습의-한계"
related_raw: ["[[wiki/Models/RL/RL-학습의-한계.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---


Deepseek 등장 이후 RL의 효율성을 높이는 연구가 많았지만, 성능이 특정 지점에서 포화되는 경향이 나타납니다. 이는 RL 학습 자체의 근본적인 한계 때문일 수 있습니다.

## RL 학습의 세 가지 한계

1.  **지나치게 희소한 보상(Sparse Reward)**: 수많은 시도 중 정답 경로 하나에만 보상이 주어지므로, 중간 탐색 과정에 인센티브를 주기 어려워 스케일업이 힘듭니다.
2.  **지나치게 지역적인 가치 함수(Value Function)**: 가치 함수의 지역성은 보상 해킹, 다양성 고갈 등의 문제로 이어지며, 모델이 본질적인 단서 대신 표면적인 패턴에만 매몰되게 합니다.
3.  **RLVR 보상의 불확실성**: RLVR(Reinforcement Learning from Verified Results) 연구에서 오답이나 랜덤 선택에 보상을 주어도 성능이 오르는 등, 기존 RL 이론과 모순되는 현상이 나타납니다. 이는 LLM 환경에서 RL의 역할에 대한 추가적인 탐구가 필요함을 시사합니다.

## 관련 자료 (논문)

- 2025-10 Scaling RL Compute for LLMs Becomes Predictable - Meta
- 2025-11 Ilya Sutskever – We're moving from the age of scaling to the age of research
- 2025-02 From system 1 to system 2: A survey of reasoning large language models
- 2025-08 Deep Think with Confidence - Meta
- 2025-09 Outcome-Based Exploration for LLM Reasoning - Meta
- 2025-11 Scaling Generative Verifiers For Natural Language Mathematical Proof Verification And Selection - Nivida
- 2025-11 Bot Meets Shortcut: How Can LLMs Aid in Handling Unknown Invariance OOD Scenarios?
- 2025-11 From Solving to Verifying: A Unified Objective for Robust Reasoning in LLMs - Meta
- 2025-06 Spurious Reward: Rethinking Training Signals in RLVR
- 2025-09 DeepSearch – Overcoming RLVR Bottlenecks via Monte Carlo Tree Search
- 2025-04 Phi-4-Mini-Reasoning: Exploring the Limits of Small Reasoning Language Models in Math - Microsoft
- 2025-10 Exploration v.s. Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward

## 관련 노트

- [[wiki/Models/RL/RLHF]]
- [[wiki/Models/RL/TRL-OpenEnv Integration for Training LLMs]]
- [[wiki/Models/RL/Agent-R1 Training Powerful LLM Agents with End-to-End Reinforcement Learning]]
