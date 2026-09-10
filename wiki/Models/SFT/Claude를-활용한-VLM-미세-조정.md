---
title: "Claude를-활용한-VLM-미세-조정"
related_raw: ["[[wiki/Models/SFT/Claude를-활용한-VLM-미세-조정.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Claude를 활용한 VLM 미세 조정

Merve Noyan의 게시물에 따르면, Anthropic의 Claude를 사용하여 개방형 비전 언어 모델(VLM)을 인간의 언어로 쉽게 미세 조정(Fine-Tuning)할 수 있습니다.

"HF Skills"라는 저장소를 통해 대규모 언어 모델(LLM)을 사용하여 다양한 작업을 자동화할 수 있으며, 특히 `model-trainer` 스킬은 SFT, DPO, GRPO와 같은 기법을 적용하고 Hugging Face Jobs를 사용하여 GPU에서 스크립트를 실행합니다.

게시물에서는 TRL 라이브러리의 기본 SFT 지원과, 사용자가 Claude에게 직접 변경을 요청할 수 있다는 점을 강조합니다.

이 접근 방식은 미세 조정 과정을 저수준 엔지니어링 작업에서 모델과의 '대화'로 전환시키는 중요한 변화를 의미합니다. 예를 들어, Qwen2-VL 모델에 대한 SFT 및 LoRA 구성을 자연어로 자동화하여 비전-언어 모델의 반복 및 개발 속도를 크게 향상시킬 수 있습니다.

## 관련 링크

*   원본 링크: [https://lnkd.in/d8s3HXwf](https://lnkd.in/d8s3HXwf)

## 관련 노트

*   [[wiki/Engineering/Infrastructure-and-DevOps/DGX Spark에서의 VLM 파인튜닝]]
*   [[wiki/Models/SFT/Fine-Tuning]]
*   [[wiki/Agents/Coding-and-Engineering/Claude_Code_on_the_web]]
*   [[wiki/Models/SFT/PEFT-Options]]
