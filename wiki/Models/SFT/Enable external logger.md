---
title: "Enable external logger"
related_raw: ["[[wiki/Models/SFT/Enable external logger.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_options']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

실험을 기록하고 시각화하기 위해 TensorBoard나 Weights & Biases (wandb)와 같은 외부 로깅 도구를 사용하는 것을 의미합니다. 이러한 도구들은 모델 훈련 과정에서 손실, 정확도, 학습률 등의 메트릭을 기록하고 시각화할 수 있게 도와줍니다.

### TensorBoard와 Weights & Biases

#### TensorBoard

TensorBoard는 TensorFlow에서 제공하는 시각화 도구로, PyTorch를 포함한 다른 프레임워크에서도 널리 사용됩니다. 실험 메트릭을 기록하고 시각화할 수 있으며, 훈련 과정을 모니터링하는 데 유용합니다.

#### Weights & Biases (wandb)

Weights & Biases는 모델 훈련과 실험을 추적하고 시각화하는데 사용되는 도구입니다. 실시간으로 훈련 메트릭을 모니터링하고, 여러 실험을 비교할 수 있으며, 팀과 협업할 때 유용합니다.

### 예제 코드

#### TensorBoard

1. **PyTorch 및 TensorBoard 설정**:
```bash
pip install torch torchvision tensorboard
```

2. **TensorBoard 사용 예제**:
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter

# 모델 정의
class SimpleModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.fc(x)

# 설정
input_dim = 10
output_dim = 1
model = SimpleModel(input_dim, output_dim)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
writer = SummaryWriter(log_dir='./runs/experiment1')

# 데이터 생성
inputs = torch.randn(32, input_dim)
targets = torch.randn(32, output_dim)

# 훈련 루프
num_epochs = 100
for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()

    # 로그 기록
    writer.add_scalar('Loss/train', loss.item(), epoch)
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}")

writer.close()
```

3. **TensorBoard 실행**:
```bash
tensorboard --logdir=./runs
```

#### Weights & Biases (wandb)

1. **wandb 설치 및 설정**:
```bash
pip install wandb wandb login  # 로그인 필요
```
2. **wandb 사용 예제**:
```python
import torch
import torch.nn as nn
import torch.optim as optim
import wandb

# Weights & Biases 초기화
wandb.init(project="my_project")

# 모델 정의
class SimpleModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.fc(x)

# 설정
input_dim = 10
output_dim = 1
model = SimpleModel(input_dim, output_dim)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 데이터 생성
inputs = torch.randn(32, input_dim)
targets = torch.randn(32, output_dim)

# 훈련 루프
num_epochs = 100
for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()

    # 로그 기록
    wandb.log({"Loss": loss.item()})
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}")

wandb.finish()
```