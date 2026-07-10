---
title: "Gradient"
related_raw: ["[[wiki/Models/SFT/Gradient.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_parameters']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

기계 학습, 특히 딥러닝에서 중요한 개념으로, 모델의 손실 함수(loss function)가 변화하는 방향과 크기를 나타냅니다. 그라디언트는 모델의 가중치를 최적화하는 데 사용되며, 학습 과정에서 가중치를 업데이트하는 데 중요한 역할을 합니다.

### Gradient의 개념

1. **정의**:
    
    - 그라디언트는 벡터로, 함수의 입력 변수들에 대한 편미분으로 구성됩니다.
    - 이는 함수의 기울기를 나타내며, 각 변수의 변화가 함수의 출력에 미치는 영향을 나타냅니다.
2. **수학적 표현**:
    
    - 예를 들어, 함수 f(x)의 그라디언트는 ∇f(x)로 표기하며, 이는 각 변수에 대한 편미분을 포함합니다:
        
        ∇f(x)=(∂f/∂x1,∂f/∂x2,…,∂f/∂xn)
        
3. **역전파(Backpropagation)**:
    
    - 딥러닝에서 그라디언트는 역전파 알고리즘을 통해 계산됩니다.
    - 역전파는 출력에서 입력 방향으로 그라디언트를 전파하여, 각 가중치에 대한 그라디언트를 계산합니다.
    - 이 과정은 연쇄 법칙(chain rule)을 사용하여 각 계층의 그라디언트를 효율적으로 계산합니다.

### Gradient의 역할

1. **손실 함수 최적화**:
    
    - 그라디언트는 손실 함수의 최소값을 찾는 데 사용됩니다.
    - 경사 하강법(Gradient Descent)과 같은 최적화 알고리즘은 그라디언트를 사용하여 가중치를 업데이트합니다.
2. **가중치 업데이트**:
    
    - 경사 하강법에서 가중치는 그라디언트를 따라 이동하여 손실을 최소화합니다.
    - 가중치 업데이트 공식:
        
        θnew=θold−η∇L(θold)
        
        여기서 θ는 가중치, η는 학습률(learning rate), ∇L은 손실 함수의 그라디언트입니다.

### Gradient Descent 알고리즘

경사 하강법은 그라디언트를 사용하여 손실 함수를 최적화하는 알고리즘입니다. 주요 변형으로는 다음과 같은 방법들이 있습니다:

1. **배치 경사 하강법 (Batch Gradient Descent)**:
    
    - 전체 훈련 데이터셋을 사용하여 한 번의 업데이트를 수행합니다.
    - 안정적이지만, 데이터셋이 큰 경우 계산 비용이 많이 듭니다.
2. **확률적 경사 하강법 (Stochastic Gradient Descent, SGD)**:
    
    - 한 개의 데이터 포인트에 대해 업데이트를 수행합니다.
    - 노이즈가 많지만, 빠르고 메모리 효율적입니다.
3. **미니배치 경사 하강법 (Mini-batch Gradient Descent)**:
    
    - 미니배치라 불리는 작은 데이터셋을 사용하여 업데이트를 수행합니다.
    - 배치와 SGD의 장점을 결합하여, 계산 효율성과 안정성을 향상시킵니다.

### Gradient의 문제와 해결책

1. **그라디언트 폭주 (Gradient Explosion)**:
    
    - 그라디언트의 크기가 너무 커져서 가중치 업데이트가 불안정해지는 현상입니다.
    - 해결책: Gradient Clipping(그라디언트 클리핑)을 사용하여 그라디언트의 크기를 제한합니다.
2. **그라디언트 소실 (Gradient Vanishing)**:
    
    - 그라디언트의 크기가 너무 작아져서 가중치 업데이트가 거의 이루어지지 않는 현상입니다.
    - 해결책: ReLU와 같은 활성화 함수 사용, 가중치 초기화 방법 개선, 배치 정규화(Batch Normalization) 사용.

### 예제 코드 (PyTorch)

아래는 간단한 경사 하강법을 사용하여 가중치를 업데이트하는 PyTorch 예제입니다:

```python
import torch

# 간단한 선형 모델 정의
model = torch.nn.Linear(10, 1)

# 손실 함수와 옵티마이저 정의
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 임의의 데이터 생성
inputs = torch.randn(100, 10)
targets = torch.randn(100, 1)

# 학습 루프
for epoch in range(100):
    optimizer.zero_grad()  # 그라디언트 초기화
    outputs = model(inputs)  # 모델 예측
    loss = criterion(outputs, targets)  # 손실 계산
    loss.backward()  # 그라디언트 계산
    optimizer.step()  # 가중치 업데이트

    print(f'Epoch {epoch+1}, Loss: {loss.item()}')

```

이 코드에서 `loss.backward()`는 그라디언트를 계산하고, `optimizer.step()`은 가중치를 업데이트합니다.