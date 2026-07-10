---
title: "VisPlay - Self-Evolving Reinforcement Learning Framework for VLMs"
related_raw: ["[[wiki/Agents/Frameworks/VisPlay - Self-Evolving Reinforcement Learning Framework for VLMs.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'llm_agent_training_rl']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# VisPlay: Vision-Language Model을 위한 자기 진화 강화 학습 프레임워크

"VisPlay"는 레이블이 없는 방대한 이미지 데이터를 활용하여 Vision-Language Model(VLM)이 자율적으로 추론 능력을 향상시킬 수 있도록 하는 새로운 자기 진화 강화 학습 프레임워크입니다.

## 핵심 아이디어

VisPlay는 단일 기본 VLM이 두 가지 역할, 즉 **이미지 조건부 질문자(Image-Conditioned Questioner)**와 **다중 모드 추론기(Multimodal Reasoner)**를 수행하도록 합니다. 이 두 역할은 **그룹 상대 정책 최적화(GRPO, Group-Relative Policy Optimization)**를 통해 함께 훈련되어 질문과 답변의 품질을 지속적으로 개선합니다. 이 과정에서 다양성과 난이도에 대한 보상을 활용하여 모델이 더욱 복잡하고 깊이 있는 추론 능력을 학습하도록 유도합니다.

## 주요 성과

이 접근 방식을 통해 Qwen2.5-VL 및 MiMo-VL과 같은 VLM은 8개의 주요 벤치마크(MM-Vet, MMMU 포함)에서 시각적 추론, 구성적 일반화 및 환각 감소 등 다방면에서 일관된 성능 향상을 보였습니다. 이는 진정으로 자가 개선이 가능한 다중 모드 AI를 향한 중요한 진전이며, 향후 연구를 위한 확장 가능한 경로를 제시합니다.

## 관련 링크

*   **논문 (Hugging Face):** [https://lnkd.in/eUpzXTVd](https://lnkd.in/eUpzXTVd)
*   **프로젝트 페이지:** [https://lnkd.in/eh5tUiAf](https://lnkd.in/eh5tUiAf)
*   **코드 (GitHub):** [https://lnkd.in/etZArtkP](https://lnkd.in/etZArtkP)
