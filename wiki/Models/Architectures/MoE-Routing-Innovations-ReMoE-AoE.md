---
title: "Mixture-of-Experts(MoE) 라우팅 혁신 기법: ReMoE와 AoE"
related_raw: ["[[2026-08-26-moe_routing_innovation_remoe_aoe.md]]"]
tags: [moe, architectures, routing, optimization]
last_updated: "2026-08-26"
updated: "2026-08-26"
---

# 🔀 Mixture-of-Experts(MoE) 라우팅 혁신 기법: ReMoE와 AoE

## 1. 기존 Top-K 라우팅의 치명적 한계
전형적인 MoE(예: Mixtral, DeepSeek)는 입력 토큰 벡터와 라우터 가중치의 내적 값을 구하고, 이 중 상위 $K$개 전문가(Expert)를 칼같이 잘라내는 **Top-K 하드 게이팅** 방식을 씁니다.
- **미분 불가능성 (False Gradient)**: 상위 $K$개의 경계값 부근에서 전문가의 선택이 뒤바뀔 때 결괏값이 급작스레 도약(불연속)하므로 역전파 시 라우터 파라미터로 흐르는 기울기(Gradient)가 끊어지거나 파괴되어 학습 효율이 저하됨.
- **고정 할당의 비효율**: 매우 쉬운 중립 토큰('the', '\n' 등)과 매우 연산이 난해한 수학 공식 토큰 모두에 무조건 고정된 $K$개의 전문가를 작동시켜 연산 자원의 낭비가 초래됨.

## 2. ReMoE (ReLU Routing Mixture-of-Experts) - ICLR 2025

### 1) 핵심 아키텍처
기존의 Softmax와 Top-K 하드 게이팅을 제거하고, 라우터 활성화 함수로 **ReLU**를 도입함.
$$G(x) = 	ext{ReLU}(W_g \cdot x)$$
이로 인해 내적 값이 0 이상인 모든 전문가는 가동되고, 0 미만인 전문가는 완벽히 셧다운되는 단순하고 매끄러운(미분 가능한) 구조로 학습 안정성 및 정밀 피드백을 확보함.

### 2) 희소성 규제 및 동적 할당
- **L1 Regularization**: 모델이 모든 전문가를 다 켜려는 게으른 행동을 차단하기 위해, 라우터 출력에 L1 패널티를 줘 가중치를 0으로 적극 끌어내림.
- **Dynamic Expert Allocation (동적 전문가 할당)**: 난이도가 아주 낮아 가벼운 처리가 어울리는 토큰에는 스스로 1개의 전문가만 점수를 0 이상으로 켜고, 극도의 추론이 요구되는 복합 토큰에는 4개 이상의 전문가를 알아서 점수 0 위로 켜는 **토큰 난이도별 자율 수량 조절** 메커니즘을 획득함.

## 3. AoE (Autonomy-of-Experts Models) - ICML 2025

### 1) 핵심 아키텍처: 중앙 라우터의 완벽한 제거
기존의 MoE가 외부의 라우터에 의존해 토큰을 추측성 배정하던 비효율을 해결하기 위해 **중앙 라우터를 완전히 없애고 전문가가 자율 판단**하도록 설계함.
- **실력 입증제(Self-Evaluation)**: 입력 토큰 벡터가 각 전문가의 가중치 패턴과 강한 상관이 있을 때, 전문가 FFN 내부의 활성화 크기(Activation Norm)가 수학적으로 대폭 폭발한다는 원리를 이용.
- 모든 전문가가 가볍게 입력 벡터와의 적합성을 자가 판정하고, L2 노름이 큰 상위 $K$개 전문가만 최종 연산 경로를 완수하며 나머지는 즉시 중도 연산 중단(Early-stop).

### 2) 연산 병목 해결: Low-rank 분해

```
[Input Token x] 
       │
       ├─────────────────┬─────────────────┐ (1/3 Dimension Compression)
  [Expert 1]        [Expert 2]        [Expert N]
  Low-rank F1       Low-rank F1       Low-rank F1
       │                 │                 │
  (L2 Norm = 0.2)   (L2 Norm = 0.9)   (L2 Norm = 0.1)
                         │
                         ▼ (Top-K Selection: Winner Expert 2)
                    [Expert 2]
                    Restore to Full Dim (FFN2)
                         │
                         ▼
                     [Output]
```

- 모든 전문가가 전체 입력을 다 검토하기에는 플롭스(FLOPs) 부담이 과도함.
- 이를 해결하고자 FFN의 1차 가중치 행렬을 저차원 행렬 2개(압축용, 복원용)로 분리.
- 모든 전문가는 입력 차원을 **1/3로 얇게 압축**하는 가벼운 선형 연산만을 우선 수행하여 고유의 L2 Norm 값을 산출하고, 탈락한 전문가는 FFN 2차 연산을 스킵.
- 이로 인해 기존 MoE 연산량 대비 단 97%의 처리량 부하만으로도, 잘못된 전문가 배정에 따른 성능 저하를 차단하고 전문가별 고유의 전문화(Specialization)를 크게 극대화함.
