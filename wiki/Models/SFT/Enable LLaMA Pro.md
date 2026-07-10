---
title: "Enable LLaMA Pro"
related_raw: ["[[wiki/Models/SFT/Enable LLaMA Pro.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_options']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

LLaMA 모델의 확장된 블록에서 파라미터를 학습 가능(trainable)하도록 설정하는 것을 의미합니다. 이는 특정 모델 블록의 파라미터를 동결(freeze)하지 않고, 모델 훈련 과정에서 업데이트될 수 있도록 허용하는 것입니다.

### LLaMA 모델

LLaMA(Large Language Model) 모델은 대규모 언어 모델로, 트랜스포머 아키텍처를 기반으로 합니다. 이 모델은 텍스트 생성을 비롯한 다양한 자연어 처리(NLP) 작업에 사용됩니다. LLaMA Pro는 이러한 모델의 확장된 버전으로, 특정 블록이나 모듈에서 파라미터를 학습 가능하도록 설정할 수 있습니다.

### 블록 확장과 파라미터 학습

1. **확장된 블록(Expanded Blocks)**:
    
    - 모델의 특정 부분을 확장하거나 추가 기능을 도입한 블록을 의미합니다. 예를 들어, 더 많은 레이어를 추가하거나 기존 블록을 확장하여 더 많은 파라미터를 포함할 수 있습니다.
2. **파라미터 학습 가능 설정(Make Parameters Trainable)**:
    
    - 확장된 블록의 파라미터를 학습 가능하도록 설정함으로써, 모델 훈련 과정에서 이 파라미터들이 업데이트되도록 합니다.
    - 이는 모델의 특정 부분을 미세 조정(fine-tuning)하거나, 전체 모델을 처음부터 훈련할 때 중요합니다.

### 예제 코드 (PyTorch)

아래는 PyTorch를 사용하여 LLaMA 모델의 확장된 블록에서 파라미터를 학습 가능하도록 설정하는 예제입니다. 여기서는 모델의 특정 블록을 확장하고, 그 파라미터를 학습 가능하게 설정합니다.
```python
import torch
import torch.nn as nn

class ExpandedBlock(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(ExpandedBlock, self).__init__()
        self.linear1 = nn.Linear(input_dim, output_dim)
        self.activation = nn.ReLU()
        self.linear2 = nn.Linear(output_dim, output_dim)
    
    def forward(self, x):
        x = self.linear1(x)
        x = self.activation(x)
        x = self.linear2(x)
        return x

class LLaMAPro(nn.Module):
    def __init__(self, input_dim, output_dim, expanded_dim):
        super(LLaMAPro, self).__init__()
        self.initial_block = nn.Linear(input_dim, expanded_dim)
        self.expanded_block = ExpandedBlock(expanded_dim, output_dim)
        self.final_block = nn.Linear(output_dim, output_dim)
    
    def forward(self, x):
        x = self.initial_block(x)
        x = self.expanded_block(x)
        x = self.final_block(x)
        return x

# 모델 생성
input_dim = 128
output_dim = 64
expanded_dim = 256
model = LLaMAPro(input_dim, output_dim, expanded_dim)

# 확장된 블록의 파라미터를 학습 가능하도록 설정
for name, param in model.expanded_block.named_parameters():
    param.requires_grad = True
    print(f"Parameter {name} is set to be trainable.")

# Optimizer 정의
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 입력 데이터 생성
input_data = torch.randn(32, input_dim)

# 모델 훈련 (예제)
model.train()
output = model(input_data)
loss = torch.mean((output - torch.randn(32, output_dim)) ** 2)
loss.backward()
optimizer.step()
```

### 코드 설명

1. **ExpandedBlock 클래스**:
    
    - 확장된 블록을 정의합니다. 여기서는 두 개의 선형 레이어와 ReLU 활성화 함수를 포함합니다.
2. **LLaMAPro 클래스**:
    
    - LLaMA 모델을 정의하며, 초기 블록, 확장된 블록, 최종 블록으로 구성됩니다.
3. **모델 생성 및 파라미터 학습 가능 설정**:
    
    - 모델을 생성한 후, 확장된 블록의 파라미터를 학습 가능하도록 설정합니다.
    - `param.requires_grad = True`를 통해 파라미터가 훈련 과정에서 업데이트되도록 설정합니다.
4. **Optimizer 정의 및 모델 훈련**:
    
    - Adam 옵티마이저를 사용하여 모델의 파라미터를 업데이트합니다.
    - 예제 입력 데이터를 생성하고, 모델 훈련을 수행합니다.