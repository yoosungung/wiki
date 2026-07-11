---
title: "Gradient Accumulation"
related_raw: ["[[wiki/Models/SFT/Gradient Accumulation.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_parameters']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

딥러닝 모델을 훈련할 때 배치 크기를 늘리는 방법 중 하나로, 메모리 제한이 있는 환경에서 효과적으로 큰 배치 크기 효과를 얻기 위해 사용됩니다. Gradient Accumulation은 여러 미니 배치에 대한 그라디언트를 누적하여, 마치 큰 배치 크기를 사용하는 것처럼 가중치를 업데이트하는 방법입니다.

### Gradient Accumulation의 작동 원리

1. **미니 배치 처리**:
    
    - 모델은 여러 개의 작은 미니 배치를 순차적으로 처리합니다.
    - 각 미니 배치에 대해 손실(loss)을 계산하고, 역전파(backpropagation)를 통해 그라디언트를 계산합니다.
2. **그라디언트 누적**:
    
    - 계산된 그라디언트는 옵티마이저를 사용하여 즉시 가중치를 업데이트하는 대신, 누적됩니다.
    - `optimizer.step()`을 호출하기 전까지 누적된 그라디언트를 계속 더합니다.
3. **가중치 업데이트**:
    
    - 지정된 횟수의 미니 배치마다(gradient accumulation step) 옵티마이저를 사용하여 가중치를 업데이트합니다.
    - 그라디언트를 업데이트한 후에는 누적된 그라디언트를 초기화합니다.

### Gradient Accumulation의 장점

1. **메모리 효율성**:
    
    - 큰 배치 크기를 사용하는 것과 동일한 효과를 얻으면서, 메모리 사용량을 줄일 수 있습니다.
    - GPU 메모리 제한이 있는 환경에서 유용합니다.
2. **훈련 안정성**:
    
    - 큰 배치 크기는 더 안정적인 훈련을 가능하게 합니다. Gradient Accumulation은 이러한 큰 배치 크기의 장점을 살리면서 메모리 문제를 해결합니다.

### Gradient Accumulation 설정 방법

- **Gradient Accumulation Steps**: 한 번의 가중치 업데이트 전에 그라디언트를 누적할 미니 배치의 수를 지정합니다. 예를 들어, `gradient_accumulation_steps = 4`로 설정하면, 4개의 미니 배치에 대한 그라디언트를 누적한 후 가중치를 업데이트합니다.

### 예제 코드 (PyTorch)

아래는 PyTorch를 사용하여 Gradient Accumulation을 설정하는 예제입니다:

```python
import torch
from torch.utils.data import DataLoader, TensorDataset

# 예제 데이터셋 생성
inputs = torch.randn(1000, 10)  # 1000개의 샘플, 10개의 특성
targets = torch.randn(1000, 1)  # 1000개의 타겟 값

dataset = TensorDataset(inputs, targets)

# 미니 배치 크기 및 DataLoader 생성
mini_batch_size = 32
dataloader = DataLoader(dataset, batch_size=mini_batch_size, shuffle=True)

# 모델, 손실 함수, 옵티마이저 정의
model = torch.nn.Linear(10, 1)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Gradient Accumulation Steps 설정
gradient_accumulation_steps = 4

# 학습 루프
for epoch in range(100):
    optimizer.zero_grad()  # 그라디언트 초기화
    for i, (batch_inputs, batch_targets) in enumerate(dataloader):
        outputs = model(batch_inputs)  # 모델 예측
        loss = criterion(outputs, batch_targets)  # 손실 계산
        loss.backward()  # 그라디언트 계산

        # 그라디언트 누적
        if (i + 1) % gradient_accumulation_steps == 0:
            optimizer.step()  # 가중치 업데이트
            optimizer.zero_grad()  # 그라디언트 초기화

    print(f'Epoch {epoch+1}, Loss: {loss.item()}')

```

이 예제에서 `gradient_accumulation_steps`는 4로 설정되어 있으며, 매 4개의 미니 배치마다 그라디언트를 누적하여 가중치를 업데이트합니다.