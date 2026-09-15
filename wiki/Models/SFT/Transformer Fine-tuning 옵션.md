---
title: "Transformer Fine-tuning 옵션"
related_raw: ["[[wiki/Models/SFT/Transformer Fine-tuning 옵션.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Transformer Fine-tuning 옵션

Transformer 모델을 미세 조정(fine-tuning)할 때 사용할 수 있는 다양한 옵션과 기법들에 대한 노트입니다.

## 일반적인 Fine-tuning 전략

- [[wiki/Models/SFT/Fine-Tuning]]: 사전 훈련된 모델을 특정 작업에 맞게 추가 학습하는 일반적인 과정입니다.
- [[wiki/Models/SFT/Freeze]]: 모델의 일부 계층을 동결하고 나머지 계층만 학습하는 방법입니다.
- [[wiki/Models/SFT/LoRA]]: 파라미터 효율적 미세 조정 방법으로, 모델의 일부 매개변수만 학습하여 업데이트하는 방법입니다.
- [[wiki/Models/SFT/GaLora]]: Gaussian 분포 기반의 저차원 적응을 사용하는 기법입니다.
- [[wiki/Models/SFT/Adapter]]: 사전 학습된 모델에 작은 어댑터 모듈을 추가하여 학습하는 방법입니다.
- [[wiki/Models/RL/RLHF]]: 인간의 피드백을 이용해 강화 학습을 수행하는 기법입니다.
- [[wiki/Models/SFT/Train Stage]]: 훈련 단계를 정의하고, 각 단계에 맞는 설정을 하는 방법입니다.

## Optimizer 및 Learning Rate

- [[wiki/Models/SFT/Optimizer]]: 모델의 가중치를 업데이트하는 최적화 알고리즘입니다. (e.g., AdamW, Adafactor)
- [[wiki/Models/SFT/BAdam]]: 모델의 파라미터를 블록 단위로 업데이트하는 Adam 옵티마이저의 변형입니다.
- Learning Rate: 모델의 가중치를 업데이트할 때 사용하는 스텝 크기입니다.
- [[wiki/Models/SFT/LR Scheduler]]: 학습률을 동적으로 조정하는 방법입니다.
- [[wiki/Models/SFT/Warmup Steps]]: 훈련 초기 단계에서 학습률을 점진적으로 증가시키는 단계입니다.

## 메모리 및 속도 최적화

- [[wiki/Models/SFT/Batch Size]]: 한 번의 훈련 스텝에서 사용하는 데이터 샘플의 개수입니다.
- [[wiki/Models/SFT/Gradient Accumulation]]: 여러 미니 배치에 대한 그라디언트를 누적하여 가중치를 업데이트하는 방법입니다.
- [[wiki/Models/SFT/Booster]]: 모델 훈련 및 추론을 가속화하는 최적화 기술입니다. (e.g., FlashAttention2, Unsloth)
- [[wiki/Models/SFT/Compute Type]]: 훈련에 사용하는 숫자 표현 방식입니다. (e.g., FP16, BF16, FP32)
- [[wiki/Models/SFT/Enable S2 Attention]]: LongLoRA에서 제안된 Shift Short Attention 메커니즘을 사용하는 것입니다.
- [[wiki/Models/SFT/Pack sequences]]: 가변 길이의 시퀀스 데이터를 고정된 길이로 변환하는 과정입니다.
- [[wiki/Models/SFT/RoPE]]: 회전 위치 임베딩(Rotary Position Embedding)으로, 위치 정보를 효과적으로 인코딩하는 방법입니다.

## 정규화 및 안정성

- [[wiki/Models/SFT/Maximum Gradient Norm]]: 그라디언트의 크기를 제한하여 그라디언트 폭주를 방지하는 기법입니다.
- [[wiki/Models/SFT/NEFTune Alpha]]: 임베딩 벡터에 노이즈를 추가하여 일반화 성능을 향상시키는 기법입니다.
- [[wiki/Models/SFT/Upcast LayerNorm]]: 레이어 정규화 계층의 가중치를 float32로 변환하여 수치적 안정성을 확보하는 기법입니다.
- [[wiki/Models/SFT/Gradient]]: 모델의 손실 함수가 변화하는 방향과 크기를 나타냅니다.

## 데이터 처리

- [[wiki/Models/SFT/Cutoff Length]]: 입력 시퀀스의 최대 길이를 제한하는 파라미터입니다.
- [[wiki/Models/SFT/Resize token embeddings]]: 토크나이저의 어휘 크기와 임베딩 레이어의 크기를 조정하는 작업입니다.
- [[wiki/Models/SFT/Val size]]: 검증 데이터셋의 크기를 의미합니다.

## 로깅 및 저장

- [[wiki/Models/SFT/Logging Steps]]: 특정 간격마다 훈련 상태를 기록하는 과정입니다.
- [[wiki/Models/SFT/Save Steps]]: 특정 간격마다 모델의 상태를 저장하는 과정입니다.
- [[wiki/Models/SFT/Enable external logger]]: TensorBoard나 Weights & Biases와 같은 외부 로깅 도구를 사용하는 것입니다.
