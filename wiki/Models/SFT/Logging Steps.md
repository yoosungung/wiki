---
title: "Logging Steps"
related_raw: ["[[wiki/Models/SFT/Logging Steps.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_parameters']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

딥러닝 모델을 훈련하는 동안 특정 간격마다 훈련 상태와 관련된 정보를 기록하는 과정을 의미합니다. Logging Steps는 모델의 훈련 과정을 모니터링하고, 성능을 평가하며, 문제가 발생했을 때 디버깅하는 데 중요한 역할을 합니다.

### Logging Steps의 역할

1. **훈련 모니터링**:
    
    - 모델 훈련이 제대로 진행되고 있는지 실시간으로 모니터링할 수 있습니다.
    - 손실 함수 값, 정확도, 학습률 등의 주요 메트릭을 주기적으로 확인할 수 있습니다.
2. **성능 평가**:
    
    - 훈련 과정에서의 성능 변화를 기록하여, 모델이 제대로 학습하고 있는지 평가할 수 있습니다.
    - 로그를 통해 과적합(overfitting)이나 과소적합(underfitting) 문제를 조기에 발견할 수 있습니다.
3. **디버깅**:
    
    - 모델 훈련 중 문제가 발생했을 때, 로그를 통해 문제의 원인을 파악할 수 있습니다.
    - 예를 들어, 손실 값이 갑자기 급격히 변하는 경우 학습률이나 데이터 문제를 의심할 수 있습니다.

### Logging Steps 설정 방법

Logging Steps는 일반적으로 훈련 루프에서 특정 간격마다 로그를 기록하도록 설정됩니다. 예를 들어, `logging_steps=100`으로 설정하면 매 100 스텝마다 로그를 기록합니다.

### 예제 코드

다음은 PyTorch를 사용하여 Logging Steps를 설정하고 사용하는 예제입니다:
```python
import torch
import torch.nn as nn
import torch.optim as optim

# 모델 정의
model = nn.Linear(10, 1)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 데이터셋 생성 (예제용)
inputs = torch.randn(1000, 10)
targets = torch.randn(1000, 1)
dataset = torch.utils.data.TensorDataset(inputs, targets)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)

# 학습 루프 설정
num_epochs = 10
logging_steps = 100  # 로그를 기록할 스텝 간격

# 학습 루프
for epoch in range(num_epochs):
    for step, (batch_inputs, batch_targets) in enumerate(dataloader):
        optimizer.zero_grad()  # 그라디언트 초기화
        outputs = model(batch_inputs)  # 모델 예측
        loss = criterion(outputs, batch_targets)  # 손실 계산
        loss.backward()  # 역전파
        optimizer.step()  # 가중치 업데이트

        # Logging Steps
        if (step + 1) % logging_steps == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}], Step [{step+1}/{len(dataloader)}], Loss: {loss.item()}")

    # 에포크가 끝날 때마다 로그 기록
    print(f"Epoch [{epoch+1}/{num_epochs}] finished, Loss: {loss.item()}")

```

이 예제에서는 `logging_steps`를 100으로 설정하여, 매 100 스텝마다 현재 손실 값을 출력합니다.