---
title: "Freeze"
related_raw: ["[[wiki/Models/SFT/Freeze.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

**Freeze fine-tuning**은 모델의 일부 계층을 동결(업데이트하지 않음)하고 나머지 계층만 학습하는 방법입니다.

- **특징**:
    
    - **부분 계층 동결**: 일반적으로 상위 계층을 동결하고, 하위 계층만 학습합니다.
    - **리소스 절약**: 전체 모델을 학습하는 것보다 리소스와 시간이 적게 필요합니다.
    - **선택적 업데이트**: 중요한 계층만 업데이트하여 빠르게 수렴할 수 있습니다.
- **장점**:
    
    - 계산 비용과 시간이 절약됩니다.
    - 사전 학습된 모델의 일반적인 표현력을 유지하면서, 특정 작업에 맞게 조정할 수 있습니다.
- **단점**:
    
    - 학습할 수 있는 표현력의 한계가 있을 수 있습니다.
    - 동결된 계층이 특정 작업에 최적화되지 않을 수 있습니다.

### Freeze Tuning Configurations

Freeze tuning은 모델 훈련 과정에서 특정 레이어나 모듈의 파라미터를 고정(freeze)하고, 나머지 부분만 학습하도록 설정하는 기법입니다. 이는 모델의 일부만을 미세 조정(fine-tuning)함으로써 효율적인 학습을 가능하게 합니다. 주어진 설정들은 이러한 freeze tuning을 세밀하게 제어하는 데 사용됩니다.

#### 1. Trainable Layers

- **설명**: 학습 가능한(hidden) 레이어의 수를 지정합니다. 양수 값은 마지막 N개의 레이어를, 음수 값은 처음 N개의 레이어를 학습 가능하게 설정합니다.
    
    - **예**:
        - `3`: 마지막 3개의 레이어를 학습 가능하게 설정.
        - `-2`: 처음 2개의 레이어를 학습 가능하게 설정.
    
#### 2. Trainable Modules

- **설명**: 학습 가능한 모듈의 이름을 지정합니다. 여러 모듈을 쉼표로 구분하여 나열할 수 있습니다.
    
    - **예**:
        - `"layer1, layer2"`: `layer1`과 `layer2` 모듈을 학습 가능하게 설정.
        - `"encoder, decoder"`: `encoder`와 `decoder` 모듈을 학습 가능하게 설정.

#### 3. Extra Modules

- **설명**: hidden 레이어 외에 추가로 학습 가능한 모듈의 이름을 지정합니다. 여러 모듈을 쉼표로 구분하여 나열할 수 있습니다.
    
    - **예**:
        - `"embeddings"`: `embeddings` 모듈을 학습 가능하게 설정.
        - `"output_layer"`: `output_layer` 모듈을 학습 가능하게 설정.

### 예제 코드 (PyTorch)

아래는 PyTorch를 사용하여 이러한 설정들을 적용하는 예제입니다:
```python
import torch
import torch.nn as nn
import torch.optim as optim

class ExampleModel(nn.Module):
    def __init__(self):
        super(ExampleModel, self).__init__()
        self.embeddings = nn.Embedding(1000, 256)
        self.layer1 = nn.Linear(256, 128)
        self.layer2 = nn.Linear(128, 64)
        self.layer3 = nn.Linear(64, 32)
        self.output_layer = nn.Linear(32, 10)

    def forward(self, x):
        x = self.embeddings(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.output_layer(x)
        return x

# 모델 생성
model = ExampleModel()

# 설정
trainable_layers = 2  # 마지막 2개의 레이어를 학습 가능하게 설정
trainable_modules = "layer2, layer3"
extra_modules = "embeddings, output_layer"

# 모든 파라미터를 고정
for param in model.parameters():
    param.requires_grad = False

# 특정 레이어 학습 가능하게 설정
if trainable_layers > 0:
    for layer in list(model.children())[-trainable_layers:]:
        for param in layer.parameters():
            param.requires_grad = True
elif trainable_layers < 0:
    for layer in list(model.children())[:abs(trainable_layers)]:
        for param in layer.parameters():
            param.requires_grad = True

# 특정 모듈 학습 가능하게 설정
for module_name in trainable_modules.split(','):
    module = getattr(model, module_name.strip())
    for param in module.parameters():
        param.requires_grad = True

# 추가 모듈 학습 가능하게 설정
for module_name in extra_modules.split(','):
    module = getattr(model, module_name.strip())
    for param in module.parameters():
        param.requires_grad = True

# 확인: 학습 가능한 파라미터만 출력
for name, param in model.named_parameters():
    if param.requires_grad:
        print(f"Trainable parameter: {name}")

# 옵티마이저 설정 (학습 가능한 파라미터만 전달)
optimizer = optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=0.001)
```

### 코드 설명

1. **ExampleModel 클래스**:
    
    - 임베딩, 3개의 레이어, 출력 레이어로 구성된 간단한 모델을 정의합니다.
2. **모델 생성 및 설정**:
    
    - 모든 파라미터를 고정(freeze)하고, 설정에 따라 특정 레이어와 모듈을 학습 가능하게 설정합니다.
    - `trainable_layers`, `trainable_modules`, `extra_modules` 변수를 사용하여 학습 가능한 파라미터를 설정합니다.
3. **파라미터 학습 가능 여부 확인**:
    
    - 학습 가능한 파라미터만 출력하여 설정이 올바르게 적용되었는지 확인합니다.
4. **옵티마이저 설정**:
    
    - 학습 가능한 파라미터만 옵티마이저에 전달하여 모델을 훈련합니다.