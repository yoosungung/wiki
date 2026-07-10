---
title: "BAdam"
related_raw: ["[[wiki/Models/SFT/BAdam.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_parameters']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

**BAdam (Block-wise Adam)**은 Adam 옵티마이저의 변형으로, 모델의 파라미터를 블록 단위로 업데이트하는 기법입니다. 이는 파라미터를 더 효율적으로 학습하고, 모델의 성능을 향상시키기 위해 설계되었습니다. BAdam은 특히 대규모 모델에서 유용하며, 파라미터 업데이트의 세밀한 제어를 가능하게 합니다.

### BAdam의 구성 요소

1. **mode (Whether to use layer-wise or ratio-wise BAdam optimizer)**
    
    - **설명**: BAdam 옵티마이저의 동작 방식을 설정합니다.
        - **layer-wise**: 레이어 단위로 파라미터를 업데이트합니다.
        - **ratio-wise**: 비율 단위로 파라미터를 업데이트합니다.
    - **사용 예**:
    ```python
    mode = 'layer-wise'  # 레이어 단위로 업데이트
	```

2. **switch mode (The strategy of picking block to update for layer-wise BAdam - ascending, descending, random, fixed)**
    
    - **설명**: 레이어 단위 업데이트 시 블록을 선택하는 전략을 설정합니다.
        - **ascending**: 아래에서 위로(하위 레이어부터 상위 레이어까지) 순차적으로 업데이트.
        - **descending**: 위에서 아래로(상위 레이어부터 하위 레이어까지) 순차적으로 업데이트.
        - **random**: 무작위로 블록을 선택하여 업데이트.
        - **fixed**: 고정된 순서로 블록을 선택하여 업데이트.
    - **사용 예**:
    ```python
    switch_mode = 'ascending'  # 아래에서 위로 순차적으로 업데이트
	```

3. **switch interval (Number of steps to update the block for layer-wise BAdam)**
    
    - **설명**: 레이어 단위 업데이트 시 블록을 업데이트하는 간격(스텝 수)을 설정합니다.
    - **사용 예**:
    ```python
    switch_interval = 10  # 10 스텝마다 블록을 업데이트
	```

4. **update ratio (The ratio of the update for ratio-wise BAdam)**
    
    - **설명**: 비율 단위 업데이트 시 업데이트 비율을 설정합니다. 비율 단위 업데이트는 전체 파라미터 중 일부만을 업데이트합니다.
    - **사용 예**:
	```python
	update_ratio = 0.1  # 전체 파라미터 중 10%를 업데이트
	```

### 예제 코드

아래는 PyTorch를 사용하여 BAdam 옵티마이저를 구현하는 간단한 예제입니다. 실제 구현은 더 복잡할 수 있으며, 여기서는 개념을 설명하기 위한 간단한 코드입니다.
```python
import torch
import torch.nn as nn
import torch.optim as optim
import random

class BAdam(optim.Adam):
    def __init__(self, params, mode='layer-wise', switch_mode='ascending', switch_interval=10, update_ratio=0.1, **kwargs):
        super(BAdam, self).__init__(params, **kwargs)
        self.mode = mode
        self.switch_mode = switch_mode
        self.switch_interval = switch_interval
        self.update_ratio = update_ratio
        self.step_count = 0

        if mode == 'layer-wise':
            self.layers = list(params)
            if switch_mode == 'fixed':
                self.layer_index = 0
            else:
                self.layer_index = None
        elif mode == 'ratio-wise':
            self.num_params = len(list(params))
    
    def step(self, closure=None):
        self.step_count += 1

        if self.mode == 'layer-wise':
            if self.step_count % self.switch_interval == 0:
                if self.switch_mode == 'ascending':
                    self.layer_index = (self.layer_index + 1) % len(self.layers)
                elif self.switch_mode == 'descending':
                    self.layer_index = (self.layer_index - 1) % len(self.layers)
                elif self.switch_mode == 'random':
                    self.layer_index = random.randint(0, len(self.layers) - 1)
                # If switch_mode is 'fixed', self.layer_index does not change

            if self.layer_index is not None:
                for i, group in enumerate(self.param_groups):
                    if i == self.layer_index:
                        for p in group['params']:
                            if p.grad is None:
                                continue
                            self._step_param(p)

        elif self.mode == 'ratio-wise':
            update_count = int(self.update_ratio * self.num_params)
            update_indices = random.sample(range(self.num_params), update_count)
            for i, group in enumerate(self.param_groups):
                for j, p in enumerate(group['params']):
                    if j in update_indices:
                        if p.grad is None:
                            continue
                        self._step_param(p)

    def _step_param(self, p):
        # Adam parameter update logic
        if p.grad is None:
            return
        grad = p.grad.data
        if grad.is_sparse:
            raise RuntimeError('Adam does not support sparse gradients, please consider SparseAdam instead')

        state = self.state[p]

        # State initialization
        if len(state) == 0:
            state['step'] = 0
            state['exp_avg'] = torch.zeros_like(p.data)
            state['exp_avg_sq'] = torch.zeros_like(p.data)

        exp_avg, exp_avg_sq = state['exp_avg'], state['exp_avg_sq']
        beta1, beta2 = self.defaults['betas']

        state['step'] += 1

        # Decay the first and second moment running average coefficient
        exp_avg.mul_(beta1).add_(1 - beta1, grad)
        exp_avg_sq.mul_(beta2).addcmul_(1 - beta2, grad, grad)

        denom = exp_avg_sq.sqrt().add_(self.defaults['eps'])

        step_size = self.defaults['lr'] * torch.sqrt(1 - beta2 ** state['step']) / (1 - beta1 ** state['step'])

        p.data.addcdiv_(-step_size, exp_avg, denom)

class ExampleModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(ExampleModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 파라미터 설정
input_dim = 128
hidden_dim = 64
output_dim = 10
mode = 'layer-wise'  # 또는 'ratio-wise'
switch_mode = 'ascending'  # 또는 'descending', 'random', 'fixed'
switch_interval = 10
update_ratio = 0.1

# 모델 생성
model = ExampleModel(input_dim, hidden_dim, output_dim)

# BAdam 옵티마이저 설정
optimizer = BAdam(model.parameters(), mode=mode, switch_mode=switch_mode, switch_interval=switch_interval, update_ratio=update_ratio, lr=0.001)

# 데이터 생성
input_data = torch.randn(32, input_dim)
target_data = torch.randn(32, output_dim)

# 모델 훈련 (예제)
criterion = nn.MSELoss()
for step in range(100):  # 100 스텝 동안 훈련
    model.train()
    optimizer.zero_grad()
    output = model(input_data)
    loss = criterion(output, target_data)
    loss.backward()
    optimizer.step()

    if step % 10 == 0:
        print(f"Step {step}, Training loss: {loss.item()}")
```

### 코드 설명

1. **BAdam 클래스**:
    
    - `mode`, `switch_mode`, `switch_interval`, `update_ratio` 파라미터를 사용하여 BAdam 옵티마이저를 정의합니다.
    - `layer-wise` 모드에서는 특정 간격마다 레이어를 순차적으로 또는 무작위로 선택하여 업데이트합니다.
    - `ratio-wise` 모드에서는 전체 파라미터 중 일부 비율을 무작위로 선택하여 업데이트합니다.
    - `_step_param` 메서드에서는 Adam 옵티마이저의 기본 파라미터 업데이트 논리를 적용합니다.
2. **ExampleModel 클래스**:
    
    - 두 개의 완전 연결 레이어로 구성된 간단한 모델을 정의합니다.
3. **모델 및 Optimizer 설정**:
    
    - 설정된 파라미터를 사용하여 모델을 생성하고, BAdam 옵티마이저를 설정합니다.
4. **모델 훈련**:
    
    - 예제 입력 데이터와 타겟 데이터를 사용하여 모델을 훈련합니다. 훈련 손실을 계산하고, 옵티마이저를 통해 모델의 파라미터를 업데이트합니다.