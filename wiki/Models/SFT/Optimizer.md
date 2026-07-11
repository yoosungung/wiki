---
title: "Optimizer"
related_raw: ["[[wiki/Models/SFT/Optimizer.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_parameters']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

딥러닝 모델을 훈련할 때 사용하는 옵티마이저는 모델의 가중치를 업데이트하여 손실 함수의 값을 최소화하는 역할을 합니다. 주어진 옵션인 `adamw_torch`, `adamw_8bit`, 그리고 `adafactor`는 각각의 특성과 장점을 가진 옵티마이저들입니다. 이들은 모델의 훈련 속도와 성능에 큰 영향을 미칩니다.

### 옵티마이저 옵션 설명

#### 1. AdamW (adamw_torch)

AdamW는 Adam 옵티마이저의 변형으로, 가중치 감쇠(weight decay)를 올바르게 적용하는 방법입니다. 이는 PyTorch에서 기본적으로 제공되는 AdamW 옵티마이저입니다.

- **특징**:
    
    - Adam 옵티마이저는 적응형 학습률을 사용하여 각 파라미터마다 학습률을 개별적으로 조정합니다.
    - AdamW는 Adam의 이점을 유지하면서, L2 정규화 대신 가중치 감쇠를 사용하여 더 나은 일반화 성능을 제공합니다.
- **사용 예**:
```python
optimizer = torch.optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)
```

- **장점**:
    
    - 빠른 수렴 속도와 높은 일반화 성능.
    - 가중치 감쇠를 통해 과적합을 방지.

#### 2. AdamW 8-bit (adamw_8bit)

AdamW 8-bit는 메모리 효율성을 높이기 위해 파라미터와 그라디언트를 8비트 정밀도로 저장하고 연산하는 AdamW의 변형입니다.

- **특징**:
    
    - 메모리 사용량을 크게 줄일 수 있습니다.
    - 특히 대규모 모델 훈련 시 GPU 메모리 제한을 극복하는 데 유용합니다.
- **사용 예**:
```python
from bitsandbytes.optim import AdamW8bit

optimizer = AdamW8bit(model.parameters(), lr=0.001, weight_decay=0.01)
```

- **장점**:
    
    - 메모리 효율성 증대.
    - 대규모 모델 훈련이 가능해짐.
- **단점**:
    
    - 8비트 정밀도로 인해 매우 미세한 정밀도가 필요한 작업에서는 성능이 저하될 수 있음.

#### 3. Adafactor

Adafactor는 Adagrad와 Adam의 변형으로, 메모리 효율성과 계산 효율성을 크게 향상시키는 옵티마이저입니다. 특히 매우 큰 모델에서 유용합니다.

- **특징**:
    
    - Adagrad의 장점을 유지하면서, 파라미터마다 개별 학습률을 조정합니다.
    - 메모리 사용량을 줄이기 위해 파라미터와 그라디언트를 축소하여 저장하고 연산합니다.
- **사용 예**:
```python
from transformers import Adafactor

optimizer = Adafactor(model.parameters(), lr=0.001, scale_parameter=True, relative_step=True)
```
- **장점**:
    - 메모리와 계산 효율성 증대.
    - 큰 모델에서의 우수한 성능.
- **단점**:
    - 사용법이 다소 복잡할 수 있으며, 하이퍼파라미터 튜닝이 필요할 수 있음.