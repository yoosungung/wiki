---
title: "2026-04-09-Unsloth-Llama-Factory"
related_raw: ["[[wiki/Models/SFT/2026-04-09-Unsloth-Llama-Factory.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'unsloth_ai_and_llama_factory_fine-tuning']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Unsloth AI 및 Llama Factory 파인튜닝 최신 업데이트 (2026-04-09)

## 요약
2026년 4월 초, Google Gemma 4 출시와 함께 Unsloth AI와 Llama Factory는 각각 압도적인 메모리 효율성과 범용성을 무기로 파인튜닝 생태계를 주도하고 있습니다. 특히 코딩 없이 로컬에서 학습이 가능한 Unsloth Studio의 출시가 주목받고 있습니다.

## 주요 내용

### 1. Unsloth AI 최신 업데이트 (2026.04)
- **Gemma 4 공식 지원:** Gemma 4 모델을 로컬(특히 Intel Mac 포함)에서 효율적으로 학습 및 실행할 수 있도록 지원합니다.
- **Unsloth Studio 출시:** GUI 기반 인터페이스로 코딩 없이 파인튜닝이 가능하며, **VRAM 사용량을 70% 절감**하여 일반 GPU에서도 Llama 4 등의 최신 모델 학습이 가능합니다.
- **도구 호출(Tool Calling) 가속:** 최적화 커널을 통해 도구 호출 정확도를 최대 80% 향상시켰으며, 웹 검색 시 실제 콘텐츠 추출 능력을 강화했습니다.

### 2. Llama Factory 동향
- **Day-0 지원:** Llama 4, Qwen 3 등 최신 모델이 출시되는 즉시 지원하는 정책을 유지하고 있습니다.
- **Unsloth 통합:** 내부적으로 `use_unsloth: true` 옵션을 통해 Unsloth의 속도 이점을 그대로 활용하면서 Llama Factory의 편리한 UI를 사용할 수 있습니다.
- **초거대 모델 학습:** KTransformers 연동을 통해 2개의 RTX 4090만으로 1조(1000B) 파라미터급 모델의 파인튜닝이 가능해졌습니다.

### 3. 도구 선택 가이드
- **Unsloth:** 제한된 GPU 자원에서 압도적인 속도와 효율이 필요할 때 (최대 30배 빠름).
- **Llama Factory:** 100개 이상의 다양한 모델을 실험하거나 체계적인 GUI 관리가 필요할 때.

## AX1센터 R&D 시사점
- 센터 내 GPU 자원을 효율적으로 활용하기 위해 **Unsloth Studio** 및 **Llama Factory + Unsloth 통합 모드**를 표준 파인튜닝 워크플로우로 채택할 것을 권장합니다.
- 특히 T2SQL 전용 sLM 개발 시 Unsloth의 도구 호출 최적화 기술을 적극 활용해야 합니다.

## 원문 URL 및 참고문헌
- [1] unsloth.ai (Gemma 4 공식 지원 블로그)
- [2] github.com/hiyouga/LLaMA-Factory (최신 모델 지원 릴리즈)

## 관련 노트
- [[wiki/Models/RL/Unsloth-Studio-GRPO]]
- [[wiki/Models/SFT/LLM_FineTuning_Libraries]]
