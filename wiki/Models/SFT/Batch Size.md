---
title: "Batch Size"
related_raw: ["[[wiki/Models/SFT/Batch Size.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_parameters']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

한 번의 훈련 스텝에서 사용하는 데이터 샘플의 개수를 의미합니다. 이는 모델의 가중치를 업데이트할 때 사용하는 데이터의 양을 결정하며, 모델 훈련의 효율성과 성능에 중요한 영향을 미칩니다.

### Batch Size의 역할과 중요성

1. **모델 업데이트 빈도**:
    
    - **작은 배치 크기**: 한 번에 적은 양의 데이터를 사용하여 더 자주 가중치를 업데이트합니다. 이는 모델이 더 자주 업데이트되므로 훈련이 빠르게 진행될 수 있지만, 각 스텝에서의 변동성이 커져 학습 과정이 불안정할 수 있습니다.
    - **큰 배치 크기**: 한 번에 많은 데이터를 사용하여 가중치를 업데이트합니다. 이는 훈련이 안정적이며, 각 스텝의 변동성이 작지만, 업데이트 빈도가 낮아져 훈련이 느려질 수 있습니다.
2. **메모리 사용**:
    
    - **작은 배치 크기**: 메모리 사용량이 적어, GPU 메모리 제한이 있는 환경에서 유리합니다.
    - **큰 배치 크기**: 메모리 사용량이 많아, 더 많은 GPU 메모리가 필요하지만, 병렬 처리의 효율성을 극대화할 수 있습니다.
3. **일반화 성능**:
    
    - **작은 배치 크기**: 일반적으로 더 나은 일반화 성능을 보일 수 있습니다. 각 배치에서의 변동성이 크므로, 모델이 다양한 데이터 분포를 더 잘 학습할 수 있습니다.
    - **큰 배치 크기**: 더 나은 수렴성을 보일 수 있지만, 과적합(overfitting) 위험이 증가할 수 있습니다.

### 배치 크기 선택의 기준

1. **하드웨어 제약**:
    
    - 사용 가능한 GPU 메모리의 크기에 따라 배치 크기를 조절해야 합니다. 큰 배치 크기는 더 많은 메모리를 요구하므로, 메모리 제약이 있을 경우 작은 배치 크기를 선택할 수 있습니다.
2. **훈련 속도와 안정성**:
    
    - 빠른 수렴을 위해 적절한 배치 크기를 선택해야 합니다. 일반적으로 작은 배치 크기는 훈련의 변동성이 크고, 큰 배치 크기는 더 안정적입니다.
3. **모델의 성능**:
    
    - 모델의 일반화 성능을 고려하여 배치 크기를 선택합니다. 작은 배치 크기는 더 나은 일반화 성능을 제공할 수 있습니다.

### 배치 크기 설정 예제 (PyTorch)

아래는 PyTorch를 사용하여 배치 크기를 설정하는 예제입니다:

```python
import torch
from torch.utils.data import DataLoader, TensorDataset

# 예제 데이터셋 생성
inputs = torch.randn(1000, 10)  # 1000개의 샘플, 10개의 특성
targets = torch.randn(1000, 1)  # 1000개의 타겟 값

dataset = TensorDataset(inputs, targets)

# 배치 크기 설정
batch_size = 32

# DataLoader 생성
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# 모델, 손실 함수, 옵티마이저 정의
model = torch.nn.Linear(10, 1)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 학습 루프
for epoch in range(100):
    for batch_inputs, batch_targets in dataloader:
        optimizer.zero_grad()  # 그라디언트 초기화
        outputs = model(batch_inputs)  # 모델 예측
        loss = criterion(outputs, batch_targets)  # 손실 계산
        loss.backward()  # 역전파
        optimizer.step()  # 가중치 업데이트

    print(f'Epoch {epoch+1}, Loss: {loss.item()}')

```

이 예제에서는 `batch_size`를 32로 설정하여 DataLoader를 생성하고, 각 배치마다 모델을 훈련합니다.