---
title: "EGGROLL-Backpropagation-없는-딥러닝"
related_raw: ["[[wiki/Models/SFT/EGGROLL-Backpropagation-없는-딥러닝.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---


NVIDIA와 옥스포드 대학이 발표한 "Evolution Strategies at the Hyperscale" (EGGROLL) 논문은 backpropagation 없이도 대규모 딥러닝 모델을 효과적으로 훈련할 수 있는 새로운 방법을 제시합니다.

## 주요 내용

EGGROLL은 진화 전략(Evolution Strategies, ES)을 기반으로 하며, 기존 ES의 높은 계산 비용과 스케일링 문제를 해결했습니다. full-rank perturbation 행렬 대신 두 개의 얇은 행렬을 곱한 low-rank perturbation을 사용하여 계산량과 메모리 사용량을 크게 줄였습니다.

### 핵심 성과

- **정수 연산 모델 훈련**: Gradient나 float 연산 없이, 정수(integer-only)로만 구성된 순환 신경망(recurrent language model)을 ES만으로 훈련하는 데 성공했습니다.
- **높은 확장성**: 각 워커(worker)가 독립적으로 perturbation을 재현하도록 설계하여 통신 비용을 0에 가깝게 만들었습니다. 이를 통해 기존 ES보다 200배 이상 큰 262,144개체 규모의 population까지 확장이 가능합니다.
- **성능**: 추론(reasoning) 태스크에서 GRPO 수준의 성능을 달성했습니다.

## 의의

EGGROLL은 '미분 가능성'과 'gradient'라는 딥러닝의 기본 전제를 흔들며, 다음과 같은 분야에 새로운 가능성을 엽니다.

- 미분이 어려운 시스템
- Discrete/hybrid 모델
- Massive simulation 기반 모델
- 정수 전용(integer-only) 뉴럴넷
- 강화학습

## 원문

- **논문**: [Evolution Strategies at the Hyperscale (EGGROLL)](https://arxiv.org/abs/2406.01786)

## 관련 노트

- [[wiki/Engineering/Infrastructure-and-DevOps/DGX Spark에서의 VLM 파인튜닝]]
