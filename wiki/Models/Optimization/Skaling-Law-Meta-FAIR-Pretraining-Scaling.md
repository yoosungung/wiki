---
title: "Skaling: 친칠라와 카플란 결합을 통한 사전학습 스케일링 법칙 및 L자형 샘플링"
last_updated: "2026-09-04"
updated: "2026-09-04"
related_raw: ["[[2026-09-04-meta-fair-skaling-chinchilla-kaplan-scaling-law.md]]"]
tags: ["Models", "Optimization", "Scaling-Laws", "Skaling", "Pre-training", "Chinchilla", "Meta-FAIR"]
type: "wiki"
status: "published"
---

# Skaling: 친칠라와 카플란 결합을 통한 사전학습 스케일링 법칙 및 L자형 샘플링

Meta FAIR 연구진이 제안한 **Skaling**은 2022년 DeepMind의 친칠라(Chinchilla) 법칙이 지니고 있던 수학적 맹점(파라미터 수 $N$과 학습 토큰 수 $D$ 간의 상호작용 부재)을 단 하나의 거듭제곱 지수 $k$로 교정하고, 사전학습 성능 예측에 소모되는 연산 비용(FLOPs)을 10분의 1로 절감한 차세대 스케일링 법칙(Scaling Law)입니다.

```mermaid
graph TD
    Chinchilla[기존 Chinchilla: 덧셈 식 Loss = A/N^a + B/D^b + E] --> Flaw[수학적 맹점: 교차 도함수 = 0, 상호작용 무시]
    Flaw --> SaddleError[오버트레이닝 영역 외삽 시 안장형 오차 발생]

    Skaling[Meta Skaling: 바깥 지수 k 도입 Loss = [A/N^a + B/D^b]^k + E] --> Synergy[음의 교차 상호작용 반영: N과 D의 시너지 포착]
    Synergy --> Accurate[외삽 오차 MAPE 1.5~3배 감소]
    Synergy --> LShape[L자형 샘플링: 고비용 Grid Sweep 대체, 연산량 90% 절감]
```

---

## 1. 친칠라 법칙의 수학적 한계: '덧셈의 착각'

2022년 친칠라 법칙은 "파라미터 1개당 약 20개의 토큰을 학습시키는 것이 최적"이라는 황금률을 제시했습니다. 그러나 친칠라 공식은 손실을 단순 분리형 덧셈으로 정의했습니다:

$$\mathcal{L}_{\text{Chinchilla}}(N, D) = \frac{A}{N^\alpha} + \frac{B}{D^\beta} + E$$

이 수식은 편미분 시 $\frac{\partial^2 \mathcal{L}}{\partial N \partial D} = 0$이 되어, **"모델 크기가 데이터 학습 효율에 아무런 영향을 주지 않는다"**는 비현실적 전제를 내포합니다.
실제 LLM 학습 곡면에서는 모델 크기($N$)와 데이터($D$)를 동시에 확장할 때 손실이 더 가파르게 감소하는 **음(-)의 교차 상호작용**이 강하게 존재합니다. 친칠라는 이를 무시했기 때문에 극단적인 소형 모델이나 대량의 데이터를 들이붓는 오버트레이닝(Overtraining) 영역으로 갈수록 심각한 안장형 오차(Saddle-shaped Error)를 유발했습니다.

---

## 2. Skaling 공식: 단 1개의 거듭제곱 지수로 완성된 결합

Meta FAIR는 기존 덧셈 식 전체를 묶고 바깥 지수 $k$를 부여한 간결한 형태를 제안했습니다:

$$\mathcal{L}_{\text{Skaling}}(N, D) = \left[ \frac{A}{N^\alpha} + \frac{B}{D^\beta} \right]^k + E \quad (k \approx 0.31 \sim 0.45)$$

### 핵심 수식적 특성
1. **자연스러운 상호작용 포착**: 지수 $k$를 통해 모델 파라미터와 데이터 간의 비선형 교차 상호작용을 파라미터 낭비 없이 정확히 모델링합니다.
2. **단조 감소성 보장**: 모델 크기와 토큰 수가 증가할 때 손실이 단조 감소함을 수학적으로 완벽히 보장합니다.
3. **외삽 오차(MAPE) 대폭 감소**: 초거대 모델로 외삽할 때 발생하는 예측 오차를 기존 대비 **1.5배~3배 이상 감소**시켰습니다.

---

## 3. 10배 저렴한 'L자형(L-shape)' 샘플링 기법

초거대 모델(100B, 1T)을 학습시키기 전, 연구진들은 수십 개의 소형 모델을 $N \times D$ 격자(Grid Sweep)로 돌려보며 스케일링 곡선을 피팅합니다. 그러나 전체 연산의 90% 이상은 격자의 우상단(큰 모델 + 많은 데이터)에서 소모됩니다.

Skaling은 $N$과 $D$의 상호작용 함수를 정확히 규명했으므로, 값비싼 우상단 격자를 전부 학습할 필요가 없습니다:
- **N-band**: 적은 토큰($D$)으로 모델 크기($N$)만 다양하게 늘리는 경량 실험.
- **D-band**: 아주 작은 100M대 모델로 데이터 토큰 수($D$)만 길게 늘려보는 경량 실험.

경계선 영역만 **'L자 모양'**으로 가볍게 프로파일링하는 것만으로 전체 격자를 전수 조사한 친칠라보다 훨씬 정밀하게 초대형 모델의 최종 손실을 예측할 수 있으며, **사전 프로파일링 FLOPs를 10배(90%) 절감**합니다.

---

## 4. 모델 파라미터별 최적 데이터 규모 및 오버트레이닝 경제학

Skaling 법칙에 따른 순수 학습 연산(Compute-Optimal) 기준 권장 토큰 규모:

| 모델 파라미터 ($N$) | Skaling 권장 최적 토큰 ($D$) | 파라미터당 토큰 수 |
| :--- | :--- | :--- |
| **1B** | 30B ~ 40B | ~30-40x |
| **9B** | 250B ~ 350B | ~30-38x |
| **30B** | 700B ~ 900B | ~25-30x |
| **100B** | 2T ~ 3T | ~20-30x |
| **1T (1000B)** | 20T ~ 30T | ~20-30x |

### 오버트레이닝(Overtraining)의 경제적 당위성
- 스케일링 법칙의 최적점은 **"사전학습 비용 최소화"**만을 고려한 결과입니다.
- 실제 상용 서비스 배포 환경에서는 수백억 회 이상의 질의가 발생하므로 **"서버 추론 비용(Inference FLOPs)"**이 전체 TCO를 지배합니다.
- 따라서 소형 모델(예: Liquid AI 2.6B에 34T 토큰 학습, Gemma 4 / Qwen)에 권장 최적점 대비 수십 배의 데이터를 학습시키는 오버트레이닝은 추론 지연 시간과 서빙 인프라 비용을 절감하기 위한 철저히 경제적인 전략입니다.

---

## 🔗 관련 문서
- [[wiki/Models/Optimization/000_Optimization-MOC.md|Optimization MOC]]
- [[wiki/Models/Architectures/000_Architectures-MOC.md|Architectures MOC]]
- [[wiki/Models/Architectures/LLM 아키텍처 비교.md|LLM 아키텍처 비교]]
- [[wiki/Models/SFT/TailSFT-Filtered-Fine-Tuning.md|TailSFT 필터링 미세조정]]
