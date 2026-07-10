---
title: "Val size"
related_raw: ["[[wiki/Models/SFT/Val size.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_parameters']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

모델 훈련에서 **Validation Set**의 크기를 의미합니다. Validation Set은 모델의 성능을 평가하고, 과적합(overfitting)을 방지하기 위해 훈련 과정 중 사용되는 데이터셋입니다. 모델 훈련 중 주기적으로 또는 에포크(epoch)가 끝날 때마다 Validation Set을 사용하여 모델의 일반화 성능을 평가합니다.

### Validation Set의 역할

1. **모델 성능 평가**:
    
    - Validation Set은 모델이 훈련되지 않은 데이터를 사용하여 성능을 평가합니다. 이를 통해 모델이 새로운 데이터에 대해 얼마나 잘 일반화되는지를 확인할 수 있습니다.
2. **과적합 방지**:
    
    - 훈련 데이터에 과적합된 모델은 새로운 데이터에서 성능이 떨어질 수 있습니다. Validation Set을 사용하여 훈련 중 과적합을 감지하고, 이를 방지하기 위한 조치를 취할 수 있습니다.
3. **하이퍼파라미터 튜닝**:
    
    - Validation Set은 모델의 하이퍼파라미터를 조정하는 데 사용됩니다. 예를 들어, 학습률(learning rate), 배치 크기(batch size), 드롭아웃(dropout) 비율 등과 같은 하이퍼파라미터를 최적화할 때 Validation Set의 성능을 기준으로 조정합니다.

### Val size 설정 방법

- **Val size**는 일반적으로 전체 데이터셋의 일정 비율로 설정됩니다.
- **비율**: 보통 훈련 데이터의 10%에서 20%를 Validation Set으로 사용합니다. 예를 들어, 데이터셋이 10,000개 샘플로 구성되어 있다면, 1,000개에서 2,000개 샘플을 Validation Set으로 설정할 수 있습니다.
- **고정 크기**: 특정 크기로 고정할 수도 있습니다. 예를 들어, 1,000개의 샘플을 Validation Set으로 설정할 수 있습니다.

### 예제 코드

아래는 PyTorch를 사용하여 데이터셋을 훈련 세트와 Validation Set으로 분할하는 예제입니다:


```python
import torch
from torch.utils.data import DataLoader, random_split, TensorDataset

# 예제 데이터셋 생성
inputs = torch.randn(1000, 10)  # 1000개의 샘플, 10개의 특성
targets = torch.randn(1000, 1)  # 1000개의 타겟 값

dataset = TensorDataset(inputs, targets)

# Val size 설정
val_size = 0.2  # 전체 데이터의 20%를 Validation Set으로 사용
train_size = int(len(dataset) * (1 - val_size))
val_size = len(dataset) - train_size

# 데이터셋 분할
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

# DataLoader 생성
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32)

# 모델, 손실 함수, 옵티마이저 정의
model = torch.nn.Linear(10, 1)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 학습 루프
for epoch in range(100):
    model.train()
    for batch_inputs, batch_targets in train_loader:
        optimizer.zero_grad()  # 그라디언트 초기화
        outputs = model(batch_inputs)  # 모델 예측
        loss = criterion(outputs, batch_targets)  # 손실 계산
        loss.backward()  # 역전파
        optimizer.step()  # 가중치 업데이트

    # Validation 단계
    model.eval()
    val_loss = 0.0
    with torch.no_grad():
        for batch_inputs, batch_targets in val_loader:
            outputs = model(batch_inputs)
            loss = criterion(outputs, batch_targets)
            val_loss += loss.item()

    val_loss /= len(val_loader)
    print(f'Epoch {epoch+1}, Validation Loss: {val_loss}')

```

이 예제에서는 전체 데이터셋의 20%를 Validation Set으로 설정하고, 이를 사용하여 매 에포크마다 모델의 성능을 평가합니다.