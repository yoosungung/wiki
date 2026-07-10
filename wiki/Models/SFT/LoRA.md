---
title: "LoRA"
related_raw: ["[[wiki/Models/SFT/LoRA.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

**LoRA**는 파라미터 효율적 미세 조정 방법으로, 모델의 일부 매개변수만 학습하여 업데이트하는 방법입니다.

- **특징**:
    
    - **저랭크 매트릭스 추가**: 기존 모델의 파라미터 공간에 저랭크 매트릭스를 추가하여 학습합니다.
    - **경량화**: 모델 전체를 학습하지 않고, 저랭크 매트릭스만 학습하기 때문에 리소스가 적게 소모됩니다.
    - **빠른 학습**: 계산 비용이 적게 들고, 빠르게 학습할 수 있습니다.
- **장점**:
    
    - 적은 데이터와 계산 자원으로도 학습이 가능합니다.
    - 빠른 학습이 가능합니다.
    - 기존 모델의 성능을 유지하면서 특정 작업에 최적화할 수 있습니다.
- **단점**:
    
    - 성능이 풀 파인 튜닝에 비해 떨어질 수 있습니다.
    - 저랭크 근사로 인해 일부 복잡한 패턴을 학습하기 어려울 수 있습니다.
#### 1. Rank

- **설명**: Low-Rank Decomposition에서 사용하는 행렬의 랭크입니다. LoRA는 고차원 파라미터 행렬을 두 개의 저차원 행렬로 분해하여 학습합니다. 이때 저차원 행렬의 랭크를 지정하는 값이 `rank`입니다.
    
    - **높은 rank**: 모델의 표현력이 높아질 수 있지만, 학습 시간이 길어지고 메모리 사용량이 증가할 수 있습니다.
    - **낮은 rank**: 학습 효율성이 높아지고 메모리 사용량이 줄어들지만, 모델의 표현력은 제한될 수 있습니다.
- **사용 예**:
```python
rank = 4  # 저차원 행렬의 랭크를 4로 설정
```
   
#### 2. Alpha (Lora scaling coefficient)

- **설명**: LoRA의 스케일링 계수로, 저차원 행렬로부터 복원된 행렬에 적용됩니다. 이는 LoRA의 업데이트 크기를 조절하는 역할을 합니다.
    
    - **높은 alpha**: LoRA 업데이트가 더 큰 영향을 미쳐, 더 강력한 학습을 유도할 수 있습니다.
    - **낮은 alpha**: LoRA 업데이트의 영향을 줄여, 더 신중한 학습을 유도할 수 있습니다.
- **사용 예**:
```python
alpha = 16  # LoRA 스케일링 계수를 16으로 설정
```

#### 3. Dropout (Dropout ratio of LoRA weights)

- **설명**: LoRA의 가중치에 적용되는 드롭아웃 비율입니다. 드롭아웃은 모델의 과적합을 방지하기 위해 일부 가중치를 무작위로 제거하는 기법입니다.
    
    - **높은 dropout 비율**: 과적합 방지에 효과적이지만, 모델의 학습 속도와 성능이 저하될 수 있습니다.
    - **낮은 dropout 비율**: 학습 속도와 성능이 높아질 수 있지만, 과적합 위험이 증가할 수 있습니다.
- **사용 예**:
```python
dropout = 0.1  # LoRA 가중치의 드롭아웃 비율을 10%로 설정
```

#### 4. LR Ratio (Learning Rate ratio, B metrics in LoRA)

- **설명**: LoRA에서 저차원 행렬의 학습률(Learning Rate)과 기존 모델 파라미터의 학습률 간의 비율입니다. 일반적으로 저차원 행렬의 학습률은 기존 모델 파라미터의 학습률보다 낮게 설정됩니다.
    
    - **높은 LR Ratio**: 저차원 행렬이 더 빠르게 학습되도록 합니다.
    - **낮은 LR Ratio**: 저차원 행렬이 더 천천히 학습되도록 합니다.
- **사용 예**:
```python
lr_ratio = 0.1  # 저차원 행렬의 학습률을 기존 파라미터 학습률의 10%로 설정`
```

#### 5. Use rslora (Rank Stabilization Scaling for LoRA)

**rslora**는 Rank Stabilization Scaling을 사용하여 LoRA 레이어의 안정성을 향상시키는 기법입니다. 이는 랭크의 변동성을 줄이고, 모델 학습의 수렴 속도와 안정성을 높이기 위한 스케일링 기법입니다.

- **설명**: LoRA에서 사용되는 랭크(rank)가 학습 과정에서 변화할 수 있습니다. Rank Stabilization Scaling은 랭크의 변화에 따라 스케일링을 조정하여, 모델 학습을 더 안정적으로 만듭니다.
- **목적**: 랭크의 변동성으로 인한 학습 불안정을 줄이고, 학습의 수렴 속도를 높이는 것입니다.
- 사용 예:
```python
use_rslora = True  # Rank Stabilization Scaling 사용 설정
rank_stabilization_factor = 0.5  # 예시 스케일링 계수
```

#### 6. Use DoRA (Weight-Decomposed LoRA)

**DoRA**는 Weight-Decomposed LoRA로, LoRA의 가중치를 추가로 분해하여 더 효율적으로 학습할 수 있게 하는 기법입니다. 이는 모델의 가중치를 두 개의 저차원 행렬로 분해하는 대신, 가중치 자체를 분해하여 더 세밀한 학습을 가능하게 합니다.

- **설명**: 가중치 행렬을 두 개의 저차원 행렬로 분해하는 기존 LoRA 기법과 달리, DoRA는 가중치 자체를 분해하여 학습합니다. 이를 통해 가중치의 각 요소를 더 세밀하게 학습할 수 있습니다.
- **목적**: 모델의 학습 효율성을 높이고, 더 정밀한 조정을 가능하게 합니다.
- 사용 예:
```python
use_dora = True  # Weight-Decomposed LoRA 사용 설정
```

아래는 PyTorch를 사용하여 LoRA 구성 요소들을 설정하는 예제입니다:
```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class LoRALayer(nn.Module):
    def __init__(self, in_features, out_features, rank, alpha, dropout, lr_ratio, use_rslora, rank_stabilization_factor, use_dora):
        super(LoRALayer, self).__init__()
        self.rank = rank
        self.alpha = alpha
        self.dropout = nn.Dropout(p=dropout)
        self.use_rslora = use_rslora
        self.rank_stabilization_factor = rank_stabilization_factor
        self.use_dora = use_dora

        if use_dora:
            self.weight_a = nn.Parameter(torch.randn(in_features, rank))
            self.weight_b = nn.Parameter(torch.randn(rank, out_features))
        else:
            self.low_rank_a = nn.Parameter(torch.randn(in_features, rank))
            self.low_rank_b = nn.Parameter(torch.randn(rank, out_features))
        
        if use_rslora:
            self.scale = (alpha / rank) * rank_stabilization_factor
        else:
            self.scale = alpha / rank

        # 학습률 설정
        self.lr_ratio = lr_ratio

    def forward(self, x):
        if self.use_dora:
            low_rank_out = self.dropout(x @ self.weight_a @ self.weight_b) * self.scale
        else:
            low_rank_out = self.dropout(x @ self.low_rank_a @ self.low_rank_b) * self.scale
        return low_rank_out

class ExampleModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, rank, alpha, dropout, lr_ratio, use_rslora, rank_stabilization_factor, use_dora):
        super(ExampleModel, self).__init__()
        self.lora = LoRALayer(input_dim, hidden_dim, rank, alpha, dropout, lr_ratio, use_rslora, rank_stabilization_factor, use_dora)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.lora(x)
        x = F.relu(x)
        x = self.fc(x)
        return x

# 파라미터 설정
input_dim = 128
hidden_dim = 64
output_dim = 10
rank = 4
alpha = 16
dropout = 0.1
lr_ratio = 0.1
use_rslora = True
rank_stabilization_factor = 0.5
use_dora = True

# 모델 생성
model = ExampleModel(input_dim, hidden_dim, output_dim, rank, alpha, dropout, lr_ratio, use_rslora, rank_stabilization_factor, use_dora)

# Optimizer 설정
optimizer = torch.optim.Adam([
    {'params': model.fc.parameters()},
    {'params': model.lora.low_rank_a, 'lr': optimizer.defaults['lr'] * lr_ratio} if not use_dora else {'params': model.lora.weight_a, 'lr': optimizer.defaults['lr'] * lr_ratio},
    {'params': model.lora.low_rank_b, 'lr': optimizer.defaults['lr'] * lr_ratio} if not use_dora else {'params': model.lora.weight_b, 'lr': optimizer.defaults['lr'] * lr_ratio},
], lr=0.001)

# 데이터 생성
input_data = torch.randn(32, input_dim)

# 모델 훈련 (예제)
model.train()
output = model(input_data)
loss = torch.mean((output - torch.randn(32, output_dim)) ** 2)
loss.backward()
optimizer.step()
```
### 코드 설명

1. 1. **LoRALayer 클래스**:
    
    - `use_rslora`와 `rank_stabilization_factor`를 사용하여 Rank Stabilization Scaling을 적용합니다.
    - `use_dora`를 사용하여 Weight-Decomposed LoRA를 적용합니다.
    - 이를 통해 랭크 안정화 및 가중치 분해를 포함한 다양한 LoRA 변형을 사용할 수 있습니다.
2. **ExampleModel 클래스**:
    
    - LoRALayer와 Linear 레이어로 구성된 모델을 정의합니다.
    - LoRALayer의 파라미터로 다양한 LoRA 설정을 전달합니다.
3. **모델 및 Optimizer 설정**:
    
    - 설정된 파라미터를 사용하여 모델을 생성하고, Optimizer를 설정합니다.
4. **모델 훈련**:
    
    - 예제 입력 데이터를 사용하여 모델을 훈련합니다.