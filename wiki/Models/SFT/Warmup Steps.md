---
title: "Warmup Steps"
related_raw: ["[[wiki/Models/SFT/Warmup Steps.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_parameters']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

딥러닝 모델을 훈련할 때 초기 학습률을 점진적으로 증가시키는 단계입니다. 이는 모델 훈련 초기 단계에서 학습률을 서서히 올려주어, 안정적인 훈련을 돕고 갑작스러운 학습률로 인해 발생할 수 있는 문제를 방지합니다. Warmup 단계가 끝난 후에는 설정된 학습률 스케줄에 따라 학습률이 조정됩니다.

### Warmup Steps의 역할

1. **훈련 안정성 향상**:
    
    - 모델 훈련 초기에는 가중치가 무작위로 초기화되어 있어, 큰 학습률로 훈련을 시작하면 손실이 급격히 변동하거나 발산할 수 있습니다. Warmup Steps는 이를 방지하고 훈련을 안정적으로 시작할 수 있게 합니다.
2. **그라디언트 안정화**:
    
    - 초기 단계에서 작은 학습률을 사용함으로써, 그라디언트가 안정적으로 계산되도록 돕습니다. 이는 특히 복잡한 모델이나 대규모 데이터셋에서 유용합니다.
3. **효율적인 학습률 증가**:
    
    - Warmup 단계가 끝난 후에는 일반적인 학습률 스케줄링 기법(예: 스텝 감소, 지수 감소, 코사인 감소 등)을 사용하여 학습률을 조정합니다. 이는 모델이 더 효과적으로 학습할 수 있도록 도와줍니다.

### Warmup Steps 설정 방법

Warmup Steps는 일반적으로 총 훈련 스텝 또는 에포크의 일정 비율로 설정됩니다. 예를 들어, 총 10,000 스텝을 훈련하는 경우, 1,000 스텝을 Warmup Steps로 설정할 수 있습니다.

### 예제 코드 (PyTorch)

다음은 PyTorch를 사용하여 Warmup Steps를 설정하고 사용하는 예제입니다. 이 예제에서는 `transformers` 라이브러리를 사용하여 학습률 스케줄러를 설정합니다.
```python
import torch
from torch.optim import Adam
from transformers import get_linear_schedule_with_warmup

# 모델 정의
model = torch.nn.Linear(10, 1)
criterion = torch.nn.MSELoss()
optimizer = Adam(model.parameters(), lr=0.001)

# 데이터셋 생성 (예제용)
inputs = torch.randn(1000, 10)
targets = torch.randn(1000, 1)
dataset = torch.utils.data.TensorDataset(inputs, targets)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)

# 학습 설정
num_epochs = 10
total_steps = len(dataloader) * num_epochs
warmup_steps = int(0.1 * total_steps)  # 전체 스텝의 10%를 Warmup Steps로 설정

# 학습률 스케줄러 정의
scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=warmup_steps, num_training_steps=total_steps)

# 학습 루프
for epoch in range(num_epochs):
    for step, (batch_inputs, batch_targets) in enumerate(dataloader):
        optimizer.zero_grad()  # 그라디언트 초기화
        outputs = model(batch_inputs)  # 모델 예측
        loss = criterion(outputs, batch_targets)  # 손실 계산
        loss.backward()  # 역전파
        optimizer.step()  # 가중치 업데이트
        scheduler.step()  # 학습률 스케줄러 스텝

        # Logging
        if (step + 1) % 100 == 0:
            current_lr = scheduler.get_last_lr()[0]
            print(f"Epoch [{epoch+1}/{num_epochs}], Step [{step+1}/{len(dataloader)}], Loss: {loss.item()}, Learning Rate: {current_lr}")

    print(f"Epoch [{epoch+1}/{num_epochs}] finished, Loss: {loss.item()}")

```

이 예제에서 `get_linear_schedule_with_warmup` 함수를 사용하여 Warmup Steps를 설정하고, 학습률을 선형적으로 증가시킨 후, 전체 훈련 스텝 동안 선형적으로 감소시키는 스케줄러를 생성합니다.