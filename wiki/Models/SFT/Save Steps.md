---
title: "Save Steps"
related_raw: ["[[wiki/Models/SFT/Save Steps.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_parameters']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

딥러닝 모델 훈련 과정에서 특정 간격마다 모델의 상태를 저장하는 과정입니다. 이는 모델 체크포인트(checkpoint)를 생성하여, 훈련 도중이나 후에 모델을 다시 불러와서 사용하거나, 훈련을 이어서 진행할 수 있도록 합니다. Save Steps는 모델 훈련의 안정성과 효율성을 높이는 데 중요한 역할을 합니다.

### Save Steps의 역할

1. **훈련 재개**:
    
    - 훈련 중간에 시스템이 중단되거나, 메모리 오류가 발생하는 등의 이유로 훈련이 중단되었을 때, 저장된 체크포인트에서 훈련을 다시 시작할 수 있습니다.
    - 훈련 중간에 모델을 여러 번 저장함으로써, 특정 지점에서부터 다시 훈련을 시작할 수 있게 됩니다.
2. **모델 버전 관리**:
    
    - 모델 훈련 과정에서 다양한 단계의 모델 상태를 저장하여, 나중에 특정 시점의 모델을 다시 불러와서 평가하거나 사용할 수 있습니다.
    - 실험 결과를 비교하거나, 최적의 모델을 선택하는 데 유용합니다.
3. **모델 복원**:
    
    - 최종 훈련이 완료된 후, 저장된 모델을 불러와서 추론(inference) 또는 추가 훈련(fine-tuning)에 사용할 수 있습니다.
    - 이를 통해 훈련된 모델을 배포하거나 실험에 활용할 수 있습니다.

### Save Steps 설정 방법

Save Steps는 일반적으로 훈련 루프에서 특정 간격마다 모델의 상태를 파일로 저장하도록 설정됩니다. 예를 들어, `save_steps=1000`으로 설정하면 매 1000 스텝마다 모델 체크포인트를 저장합니다.

### 예제 코드

다음은 PyTorch를 사용하여 Save Steps를 설정하고 사용하는 예제입니다:
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
save_steps = 1000  # 모델을 저장할 스텝 간격
step_counter = 0  # 스텝 카운터 초기화

# 학습 루프
for epoch in range(num_epochs):
    for step, (batch_inputs, batch_targets) in enumerate(dataloader):
        step_counter += 1
        optimizer.zero_grad()  # 그라디언트 초기화
        outputs = model(batch_inputs)  # 모델 예측
        loss = criterion(outputs, batch_targets)  # 손실 계산
        loss.backward()  # 역전파
        optimizer.step()  # 가중치 업데이트

        # Save Steps
        if step_counter % save_steps == 0:
            checkpoint_path = f"checkpoint_epoch{epoch+1}_step{step_counter}.pth"
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'loss': loss.item(),
            }, checkpoint_path)
            print(f"Checkpoint saved at {checkpoint_path}")

    # 에포크가 끝날 때마다 로그 기록
    print(f"Epoch [{epoch+1}/{num_epochs}] finished, Loss: {loss.item()}")

# 최종 모델 저장
final_checkpoint_path = "final_model.pth"
torch.save(model.state_dict(), final_checkpoint_path)
print(f"Final model saved at {final_checkpoint_path}")

```

이 예제에서는 `save_steps`를 1000으로 설정하여, 매 1000 스텝마다 모델 체크포인트를 저장합니다. 체크포인트에는 모델의 상태, 옵티마이저의 상태, 현재 에포크 및 손실 값 등이 포함됩니다.