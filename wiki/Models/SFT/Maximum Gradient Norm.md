---
title: "Maximum Gradient Norm"
related_raw: ["[[wiki/Models/SFT/Maximum Gradient Norm.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_parameters']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

그라디언트의 크기를 제한하는 기법인 **Gradient Clipping**에서 사용되는 중요한 파라미터입니다. 이는 그라디언트 폭주 문제를 방지하고 학습을 안정화하기 위해 사용됩니다.

### Maximum Gradient Norm의 역할

1. **Gradient Clipping**:
    
    - **Gradient Clipping**은 그라디언트 벡터의 크기가 지정된 임계값을 초과하지 않도록 제한하는 방법입니다.
    - 이를 통해 학습 과정에서 발생할 수 있는 그라디언트 폭주 문제를 방지할 수 있습니다.
    - 그라디언트 폭주란, 그라디언트의 크기가 너무 커져서 가중치 업데이트가 지나치게 크게 이루어지는 문제를 말합니다. 이로 인해 손실 함수가 발산하거나 학습이 불안정해질 수 있습니다.
2. **Norm의 종류**:
    
    - **L2 Norm**: 일반적으로 사용되는 그라디언트의 노름은 L2 노름입니다. 이는 그라디언트 벡터의 각 요소의 제곱의 합의 제곱근입니다.
    - **L1 Norm**: L1 노름도 사용될 수 있으며, 이는 그라디언트 벡터의 각 요소의 절댓값의 합입니다.

### Maximum Gradient Norm의 설정 및 효과

1. **설정**:
    
    - **Max Norm**는 그라디언트 벡터의 크기를 제한하는 값입니다. 예를 들어, Max Norm을 1로 설정하면, 그라디언트 벡터의 크기가 1을 초과하지 않도록 조정됩니다.
    - 이는 그라디언트 벡터의 크기가 1을 초과할 경우, 벡터의 방향은 유지하되 크기를 1로 조정합니다.
2. **효과**:
    
    - **안정성**: 그라디언트 폭주를 방지하여 학습의 안정성을 높입니다.
    - **수렴 속도**: 너무 큰 그라디언트로 인해 발생하는 발산 문제를 방지함으로써, 모델이 더 빠르고 안정적으로 수렴할 수 있도록 합니다.

### 예제

아래는 PyTorch를 사용하여 Maximum Gradient Norm을 설정하는 예제입니다:

```python
import torch
import torch.nn as nn
import torch.optim as optim

# 모델 정의
model = nn.Linear(10, 1)

# 손실 함수 정의
criterion = nn.MSELoss()

# 옵티마이저 정의
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 학습 루프
for epoch in range(100):
    optimizer.zero_grad()       # 그라디언트 초기화
    outputs = model(inputs)     # 모델 예측
    loss = criterion(outputs, targets) # 손실 계산
    loss.backward()             # 역전파
    
    # Gradient Clipping
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    
    optimizer.step()            # 가중치 업데이트

```

이 예제에서 `torch.nn.utils.clip_grad_norm_` 함수는 주어진 `max_norm` 값(여기서는 1.0)을 사용하여 모델의 모든 파라미터에 대해 그라디언트 클리핑을 수행합니다.