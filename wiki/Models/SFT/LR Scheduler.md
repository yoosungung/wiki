---
title: "LR Scheduler"
related_raw: ["[[wiki/Models/SFT/LR Scheduler.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_parameters']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

딥러닝 모델을 훈련할 때 학습률(learning rate)을 동적으로 조정하는 방법을 의미합니다. 학습률은 모델의 가중치를 업데이트할 때 사용하는 스텝 크기를 결정하는 중요한 하이퍼파라미터입니다. 학습률이 너무 크면 훈련이 불안정해지고, 너무 작으면 훈련이 매우 느려질 수 있습니다. 따라서 학습률을 적절히 조정하는 것이 모델 훈련의 성능과 효율성을 높이는 데 중요합니다.

### LR Scheduler의 역할

1. **훈련 안정성 향상**:
    
    - 초기에는 큰 학습률로 빠르게 학습하다가, 나중에는 작은 학습률로 더 정밀하게 조정하여 안정적인 수렴을 유도합니다.
2. **과적합 방지**:
    
    - 학습률을 주기적으로 낮추어 모델이 더 세밀하게 최적화를 수행하도록 하여, 훈련 데이터에 과적합되는 것을 방지합니다.
3. **훈련 속도 개선**:
    
    - 적절한 학습률 스케줄링을 통해 모델이 더 빠르게 최적화되고, 훈련 시간을 단축시킬 수 있습니다.

### LR Scheduler의 유형

1. **Step LR Scheduler**:
    
    - 일정한 에포크마다 학습률을 감소시키는 방식입니다.
    - 예: 매 10 에포크마다 학습률을 0.1배로 감소.
    ```
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
	```
    
2. **Exponential LR Scheduler**:
    
    - 매 에포크마다 학습률을 지수적으로 감소시키는 방식입니다.
    - 예: 매 에포크마다 학습률을 0.95배로 감소.
	```
	scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.95)
	```
    
3. **ReduceLROnPlateau**:
    
    - 검증 손실(validation loss)이 더 이상 감소하지 않을 때 학습률을 감소시키는 방식입니다.
    - 예: 검증 손실이 5 에포크 동안 개선되지 않으면 학습률을 0.1배로 감소.
    ```
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.1, patience=5)
	```
    
4. **Cosine Annealing LR Scheduler**:
    
    - 학습률을 코사인 함수 형태로 감소시키는 방식입니다. 학습률이 점진적으로 감소하다가, 다시 약간 증가하는 형태를 반복합니다.
    - 예: 50 에포크 동안 코사인 함수 형태로 학습률 조정.
    ```
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50)
    ```
    
5. **Cyclic LR Scheduler**:
    
    - 학습률을 주기적으로 변경하여, 일정 범위 내에서 증가 및 감소를 반복하는 방식입니다.
    - 예: 학습률이 0.001에서 0.01 사이를 주기적으로 변동.
    ```
    scheduler = torch.optim.lr_scheduler.CyclicLR(optimizer, base_lr=0.001, max_lr=0.01)
    ```
    

### 예제 코드 (PyTorch)

다음은 PyTorch를 사용하여 학습률 스케줄러를 설정하고 사용하는 예제입니다:

```python
import torch
import torch.nn as nn
import torch.optim as optim

# 모델 정의
model = nn.Linear(10, 1)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 학습률 스케줄러 정의 (예: StepLR)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)

# 학습 루프
for epoch in range(100):
    model.train()
    # 입력과 타겟 데이터 설정
    inputs = torch.randn(32, 10)
    targets = torch.randn(32, 1)

    optimizer.zero_grad()  # 그라디언트 초기화
    outputs = model(inputs)  # 모델 예측
    loss = criterion(outputs, targets)  # 손실 계산
    loss.backward()  # 역전파
    optimizer.step()  # 가중치 업데이트

    # 학습률 스케줄러 스텝
    scheduler.step()

    print(f'Epoch {epoch+1}, Loss: {loss.item()}, Learning Rate: {scheduler.get_last_lr()}')

```


이 예제에서는 `StepLR` 스케줄러를 사용하여 매 10 에포크마다 학습률을 0.1배로 감소시킵니다.