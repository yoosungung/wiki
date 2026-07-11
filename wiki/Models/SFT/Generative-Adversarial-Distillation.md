---
title: "Generative-Adversarial-Distillation"
related_raw: ["[[wiki/Models/SFT/Generative-Adversarial-Distillation.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---


이 문서는 "Black-Box On-Policy Distillation of Large Language Models" 연구에서 제안된 GAD(Generative Adversarial Distillation)에 대한 요약입니다.

## 기술적 요약

GAD는 교사 모델이 생성한 텍스트만 사용 가능한 블랙박스 환경에서 LLM의 지식 증류(Knowledge Distillation)를 수행하는 방법입니다.

*   **문제점:** 교사 모델의 확률(logits) 정보 없이 텍스트만으로 학생 모델을 학습시켜야 합니다.
*   **GAD 프레임워크:**
    *   **생성자(Generator):** 학생 모델 역할을 하며, 프롬프트에 대한 응답을 생성합니다.
    *   **판별자(Discriminator):** 교사 모델의 응답과 학생 모델의 응답을 구별하도록 학습됩니다.
*   **학습 과정:**
    *   생성자와 판별자는 2인 미니맥스 게임(two-player minimax game)을 통해 서로 경쟁하며 학습합니다.
    *   생성자는 판별자를 속이는 방향으로, 판별자는 더 잘 구별하는 방향으로 학습됩니다.
    *   이 과정에서 판별자는 온-정책 보상 모델(on-policy reward model)의 역할을 수행하며, 생성자는 강화학습(RL)을 통해 학습됩니다.
*   **결과:**
    *   GAD로 학습된 Qwen2.5-14B-Instruct 모델은 교사 모델인 GPT-5 Chat과 유사한 성능을 보였습니다.
    *   기존의 지식 증류 방법(SeqKD)보다 우수한 성능을 보였으며, 특히 분포 외 일반화(out-of-distribution generalization)에서 강점을 보였습니다.

## 관련 링크

*   **ArXiv 논문:** [https://arxiv.org/abs/2511.10643](https://arxiv.org/abs/2511.10643)

## 관련 노트

*   [[wiki/Models/SFT/Fine-Tuning]]
*   [[wiki/Models/RL/RLHF]]
*   [[Areas/RAG기술현황(2)]]

