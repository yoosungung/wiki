---
title: "TailSFT: 필터링 미세조정을 통한 엔트로피 붕괴 방지 및 후속 RL 탐색 공간 극대화"
last_updated: "2026-09-04"
updated: "2026-09-04"
related_raw: ["[[2026-09-04-msr-tailsft-filtered-fine-tuning-post-training.md]]"]
tags: ["Models", "SFT", "RL", "TailSFT", "Post-Training", "GRPO", "Entropy-Collapse", "MSR-NYC"]
type: "wiki"
status: "published"
---

# TailSFT: 필터링 미세조정을 통한 엔트로피 붕괴 방지 및 후속 RL 탐색 공간 극대화

Microsoft Research NYC가 제안한 **TailSFT (Filtered Fine-Tuning)**는 사후 학습(Post-training) 파이프라인에서 지도 미세조정(SFT) 단계가 초래하는 엔트로피 붕괴(Entropy Collapse)를 방지하고, 후속 강화학습(RL, 예: GRPO)의 롤아웃 탐색 커버리지(pass@k)를 극대화하는 혁신적인 SFT 정렬 기법입니다.

```mermaid
graph TD
    Pretrained[Pre-trained Base Model] --> StandardSFT[표준 SFT: 모든 데이터 Cross-Entropy 최소화]
    StandardSFT --> Collapse[확률 분포 뾰족화 & 엔트로피 붕괴: 외길 암기]
    Collapse --> RLZero[후속 RL Rollout: 다양성 소멸, Reward 0 고착 및 역전파 중단]

    Pretrained --> TailSFT[TailSFT: Offset Filtering 적용]
    TailSFT --> FilterEasy[쉬운 데이터 손실 그래디언트 Zero-out: 상위 25~50%]
    TailSFT --> TrainTail[어려운 꼬리(Tail) 데이터만 집중 역전파]
    TrainTail --> HighCoverage[대안 추론 경로 보존: pass@16 커버리지 대폭 증가]
    HighCoverage --> RLSuccess[후속 GRPO 가속 및 최종 정확도 역전]
```

---

## 1. 문제 정의: SFT의 과적합과 RL 초기화의 비극

### 1.1. 확률 분포의 뾰족화와 엔트로피 붕괴
- 기존 SFT는 모든 정답 시퀀스에 대해 교차 엔트로피(Cross-Entropy) 손실을 무차별적으로 낮춥니다.
- 모델이 이미 사전 학습 단계에서 충분히 풀 수 있는 쉬운 문제까지 완벽하게 맞추려 과적합(Over-fitting)되면서, **다른 유효한 대안적 추론 경로의 생성 확률을 0으로 강제 소멸**시킵니다.

### 1.2. 강화학습(RL)의 탐색 공간(Coverage) 파괴
- GRPO 등 현대의 추론 강화학습은 주어진 문제에 대해 16회 또는 32회의 다중 샘플링(Rollout)을 수행하고, 우연히라도 정답에 도달했을 때의 상대적 보상(Advantage)으로 정책을 업데이트합니다.
- 표준 SFT를 거친 모델은 확률이 한쪽으로 쏠려 16번을 뽑아도 동일한 외길 답안만을 고집합니다. 형태가 조금만 변형된 복합 문제를 만나면 16회의 시도가 모두 오답(`Reward = 0`)이 되며, 역전파 기울기(Gradient)가 0이 되어 강화학습이 초반부터 멈추는 "보상 0의 늪"에 빠집니다.
- 따라서 후속 RL의 성공을 결정하는 핵심 지표는 단일 정답률(`pass@1`)이 아니라 **다양한 시도 중 한 번이라도 정답에 걸릴 확률인 `pass@16` 커버리지**입니다.

---

## 2. TailSFT 메커니즘: Offset Filtering

TailSFT는 "모델이 이미 아는 쉬운 데이터는 학습에서 덜어내고, 아직 모르는 꼬리(Tail) 영역에만 그래디언트를 집중"시키는 전략을 사용합니다.

### 2.1. 베이스 모델 기준 오프셋 필터링 (Offset Filtering)
임의의 절대 손실 값으로 자르는 것이 아니라, **베이스 모델(Base Model)의 초기 손실 대비 얼마나 줄어들었는가**를 기준으로 삼습니다:

$$\Delta \mathcal{L}_i = \mathcal{L}_{\text{current}}(x_i, y_i) - \mathcal{L}_{\text{base}}(x_i, y_i)$$

- **쉬운 데이터 그래디언트 배제 (Zero-out)**: 손실 감소율이 상위권인 상위 25%(코딩 작업) 및 최대 50%(수학 작업) 샘플은 해당 스텝의 손실 계산에서 제외(`gradient = 0`)합니다.
- **사전 지식 및 탐색 공간 보존**: 쉬운 문제에 대한 과도한 확률 몰아주기가 억제되어, 모델의 추론 다양성과 엔트로피가 온전히 유지됩니다.

---

## 3. 실험 및 성능 벤치마크 (OLMo-3 7B)

| 벤치마크 / 태스크 | 표준 SFT 초기화 | TailSFT 초기화 | 후속 GRPO 적용 후 차이 |
| :--- | :--- | :--- | :--- |
| **코딩 CruxEval-O pass@16** | 42.1% | **58.9% (+16.79%p)** | 탐색 범위 대폭 확장 |
| **코딩 Magicoder pass@16** | 51.2% | **61.0% (+9.83%p)** | 복합 알고리즘 풀이 다변화 |
| **수학 AIME pass@16** | 18.5% | **21.6% (+3.07%p)** | 난제 증명 탐색 유지 |
| **BigCode MBPP+ 최종 정답률** | 69.57% | - | **73.50% (+3.93%p 달성)** |
| **RL 초기 수렴 속도** | 1.0x (기준) | - | **최대 2.5배 가속** |

> **핵심 인사이트**: SFT 직후의 단일 점수(`pass@1`)는 표준 SFT보다 소폭 낮을 수 있으나, 탐색 커버리지(`pass@16`)가 대폭 살아있기 때문에 이를 바탕으로 GRPO를 돌리면 최종 성능과 수렴 속도 모두에서 표준 방식을 압도합니다.

---

## 4. 구현 알고리즘 예시 (PyTorch Pseudo-code)

```python
import torch

def tailsft_loss_step(model, base_model, batch, filter_ratio=0.25):
    input_ids, labels = batch["input_ids"], batch["labels"]
    
    # 1. 현재 학습 모델과 베이스 모델의 손실(per-token/per-sample) 계산
    with torch.no_grad():
        base_losses = base_model(input_ids, labels=labels).per_sample_loss
    current_losses = model(input_ids, labels=labels).per_sample_loss
    
    # 2. 베이스 대비 손실 변화량 계산 (Offset)
    delta_loss = current_losses - base_losses
    
    # 3. 쉬운 상위 샘플 필터링 (가장 많이 개선된 하위 delta_loss 샘플 마스킹)
    k = int(len(delta_loss) * filter_ratio)
    threshold = torch.topk(delta_loss, k=k, largest=False).values[-1]
    mask = (delta_loss > threshold).float()
    
    # 4. Tail 영역에 대해서만 그래디언트 역전파
    filtered_loss = (current_losses * mask).sum() / (mask.sum() + 1e-8)
    return filtered_loss
```

---

## 🔗 관련 문서
- [[wiki/Models/SFT/000_SFT-MOC.md|SFT MOC]]
- [[wiki/Models/RL/000_RL-MOC.md|RL MOC]]
- [[wiki/Models/RL/LLM-Reinforcement-Learning-Post-Training-Guide.md|LLM 강화학습 사후 학습 가이드]]
- [[wiki/Models/RL/GRPO-Algorithm-Definition.md|GRPO 알고리즘 정의]]
- [[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md|DeepSeek-R1 GRPO 구현]]
