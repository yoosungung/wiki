---
title: "LMSYS Miles: 온폴리시 증류 (On-Policy Distillation, OPD) 지원 가이드"
related_raw: ["[[2026-07-24-lmsys-opd-support-in-miles.md]]"]
tags: ["Models", "RL", "Post-Training", "Distillation", "LMSYS", "Miles", "SGLang"]
type: "wiki"
status: "published"
last_updated: "2026-07-24"
updated: "2026-07-24"
---

# LMSYS Miles: 온폴리시 증류 (On-Policy Distillation, OPD) 지원 가이드

## 1. 개요
[LMSYS Org의 공식 발표(2026-07-18)](https://www.lmsys.org/blog/2026-07-18-opd-support-in-miles)에 따르면, 대규모 강화 학습(RL) 및 사후 학습(Post-training) 프레임워크인 **Miles**에 **온폴리시 증류(On-Policy Distillation, OPD)**가 정식 탑재되었습니다. OPD는 고성능 교사 모델(Teacher)의 추론 흐름과 분포(KL-divergence)를 학습 모델(Student)에 동적으로 주입하여, 추론 정밀도는 유지하되 토큰 소모나 사고 경로를 효율화하는 기법입니다.

## 2. 핵심 학습 모드
Miles 프레임워크 내에서 OPD는 크게 두 가지 방식으로 동작합니다.

### 1) 순수 증류 (Pure Distillation)
- **메커니즘:** 학생 모델이 생성한 토큰 분포에 대해 교사 모델과의 역-KL(Reverse-KL) 오차를 최소화하도록 역전파를 수행합니다. 오직 교사 모델의 피드백 분포로만 학습이 진행됩니다.
- **용도:** 소형 모델이 대형 모델의 정밀한 언어적 뉘앙스나 논리 구조를 그대로 복사하기에 적합합니다.

### 2) RL 결합형 증류 (RL-Augmented Distillation)
- **메커니즘:** 환경으로부터 들어오는 작업 보상(Reward) 및 이점 추정치(Advantage from GRPO/PPO)와 교사 모델의 OPD 손실 함수를 가중치합하여 최종 Loss를 구합니다.
- **수식 컨셉:**
  $$Loss = L_{RL} + \lambda L_{OPD}$$
- **용도:** 정답 유무가 명확한 코딩/수학 문제 등에서 교사 모델의 분포를 가이드로 따르되, 최종 성능 검증은 테스트 케이스 통과 여부(Reward)로 가중치를 부여하는 하이브리드 학습에 유용합니다.

## 3. 기술적 최적화 명세
- **Sparse Teacher Scoring (희소 교사 채점):** 매 토큰마다 무거운 확률 분포 정보를 통신 교환하지 않고, 샘플링된 구간 혹은 특정 주요 토큰 노드에서만 교사 모델에 채점을 요청하여 네트워크 대역폭(payload) 오버헤드를 대폭 절감했습니다.
- **Top-k OPD 및 SGLang 결합:** 추론 서빙 엔진인 [SGLang](https://github.com/sgl-project/sglang)을 백엔드로 활용하여 교사 모델의 Top-k 확률 토큰들을 배치 단위로 동시 평가함으로써 학습 지연 시간(Latency)을 최소화했습니다.

## 4. 실전 검증 사례
LMSYS가 시연한 실증 실험 결과는 다음과 같습니다.
- **실험 환경:** 8× NVIDIA B200 GPU 단일 노드 활용.
- **실험 대상:** **Qwen3.5-35B-A3B** 모델의 자가 증류(Self-Distillation).
- **결과:** 교사 모델의 '긴 사고 경로(Long Reasoning)'에서 발현하는 성능을 유지하면서도, 학생 모델이 '짧은 사고(Shorter-Reasoning)'만으로 동일한 정답률을 기록하도록 거동을 전이하는 데 성공했습니다.

## 관련 문서
- [[wiki/Models/RL/000_RL-MOC.md|강화 학습 MOC]]
- [[wiki/Models/Optimization-and-Serving/000_Optimization-and-Serving-MOC.md|모델 최적화 및 서빙 MOC]]
- [[wiki/Models/Architectures/000_Architectures-MOC.md|모델 아키텍처 MOC]]
