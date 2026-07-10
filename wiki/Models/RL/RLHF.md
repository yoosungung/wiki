---
title: "RLHF"
related_raw: ["[[wiki/Models/RL/RLHF.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

**RLHF (Reinforcement Learning from Human Feedback)**는 인간의 피드백을 이용해 강화 학습을 수행하는 기법입니다. 이 방법은 특히 자연어 처리(NLP) 분야에서 언어 모델의 성능을 개선하는 데 사용됩니다. RLHF는 모델이 생성한 결과물에 대해 인간이 제공하는 피드백을 학습 과정에 통합함으로써, 모델의 출력을 더 자연스럽고 유용하게 만듭니다.

### RLHF의 구성 요소

1. **언어 모델(Language Model)**:
    
    - 기본적으로 사전 학습된 언어 모델입니다. 예를 들어, GPT-3와 같은 대규모 언어 모델이 사용될 수 있습니다.
2. **피드백 수집(Feedback Collection)**:
    
    - 모델이 생성한 출력에 대해 인간이 피드백을 제공합니다. 이 피드백은 모델의 출력이 얼마나 적절한지, 유용한지, 혹은 정확한지를 평가합니다.
3. **보상 모델(Reward Model)**:
    
    - 인간 피드백을 바탕으로 보상을 예측하는 모델입니다. 이 모델은 언어 모델이 생성한 텍스트의 품질을 평가하고, 이 평가 결과를 보상 신호로 변환합니다.
4. **강화 학습(Reinforcement Learning)**:
    
    - 보상 모델에서 예측한 보상 신호를 사용하여 언어 모델을 미세 조정합니다. 일반적으로 Proximal Policy Optimization (PPO)과 같은 강화 학습 알고리즘이 사용됩니다.

### RLHF의 단계

1. **데이터 준비**:
    
    - 사전 학습된 언어 모델을 사용하여 다양한 프롬프트(prompt)에 대한 응답을 생성합니다.
    - 생성된 응답에 대해 인간 평가자들이 피드백을 제공합니다. 예를 들어, 응답이 적절한지, 유용한지 등을 평가합니다.
2. **보상 모델 훈련**:
    
    - 인간 평가자의 피드백을 사용하여 보상 모델을 훈련합니다. 보상 모델은 언어 모델의 출력에 대한 품질 점수를 예측합니다.
3. **강화 학습**:
    
    - 보상 모델의 예측을 바탕으로 언어 모델을 강화 학습합니다. 보상 신호를 최대화하기 위해 언어 모델의 파라미터를 업데이트합니다.
4. **반복 과정**:
    
    - 이 과정을 반복하여 언어 모델의 성능을 지속적으로 개선합니다.

### RLHF 설정 및 매개변수

#### 1. Beta value

- **설명**: 손실 함수에서 사용되는 베타 매개변수입니다. 이는 보상과 손실 간의 균형을 맞추는 역할을 합니다.
- **사용 예**:
```python
beta_value = 0.1  # 손실 함수에서의 베타 값
```
#### 2. Ftx gamma (The weight of SFT loss in the final loss)

- **설명**: 최종 손실에서 Supervised Fine-Tuning (SFT) 손실의 가중치입니다. 이는 지도 학습과 강화 학습의 손실을 결합할 때 사용됩니다.
- **사용 예**:
```python
ftx_gamma = 0.5  # 최종 손실에서 SFT 손실의 가중치
```

#### 3. Loss type (sigmoid, hinge, ipo, kto_pair)

- **설명**: 강화 학습에서 사용할 손실 함수의 유형을 지정합니다. 각 유형은 보상 신호를 처리하는 방식이 다릅니다.
    
    - **sigmoid**: 시그모이드 함수로 손실을 계산합니다.
    - **hinge**: 힌지 손실을 사용합니다.
    - **ipo**: 일종의 최적화 손실을 사용합니다.
    - **kto_pair**: 쌍(pairwise) 손실을 사용합니다.
- **사용 예**:
```python
loss_type = "sigmoid"  # 시그모이드 손실 함수 사용
```

#### 4. Reward model (Adapter of the reward model in PPO training)

- **설명**: PPO(Proximal Policy Optimization) 훈련에서 사용할 보상 모델의 어댑터입니다. 보상 모델은 모델의 출력을 평가하여 보상을 제공합니다.
- **사용 예**:
```python
reward_model = "adapter_name"  # PPO 훈련에서 사용할 보상 모델의 어댑터 이름
```

#### 5. Score norm (Normalizing scores in PPO training)

- **설명**: PPO 훈련에서 점수를 정규화하는 방법입니다. 점수 정규화는 모델이 보상을 일관되게 받도록 하여 훈련의 안정성을 향상시킵니다.
- **사용 예**:
```python
score_norm = True  # 점수를 정규화하도록 설정
```

#### 6. Whiten rewards (Whiten the rewards in PPO training)

- **설명**: PPO 훈련에서 보상을 정규화(whiten)하는 방법입니다. 보상 정규화는 보상의 분포를 정규 분포로 변환하여, 학습이 더 잘 이루어지도록 합니다.
- **사용 예**:
```python
whiten_rewards = True  # 보상을 정규화하도록 설정
```

### 예제 코드

아래는 RLHF 설정을 적용하여 모델을 훈련하는 예제 코드입니다:
```python
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 사전 학습된 GPT-2 모델 및 토크나이저 로드
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# 보상 모델 정의 (간단한 예제)
class RewardModel(nn.Module):
    def __init__(self):
        super(RewardModel, self).__init__()
        self.linear = nn.Linear(model.config.n_embd, 1)

    def forward(self, input_ids):
        outputs = model.transformer(input_ids)
        hidden_states = outputs.last_hidden_state
        rewards = self.linear(hidden_states[:, -1, :])
        return rewards

reward_model = RewardModel()

# 강화 학습 설정 (PPO 사용 예)
class PPOTrainer:
    def __init__(self, model, reward_model, beta_value, ftx_gamma, loss_type, score_norm, whiten_rewards, lr=1e-5):
        self.model = model
        self.reward_model = reward_model
        self.beta_value = beta_value
        self.ftx_gamma = ftx_gamma
        self.loss_type = loss_type
        self.score_norm = score_norm
        self.whiten_rewards = whiten_rewards
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)
    
    def compute_loss(self, input_ids, rewards):
        outputs = self.model(input_ids, labels=input_ids)
        logits = outputs.logits
        loss = nn.CrossEntropyLoss()(logits.view(-1, logits.size(-1)), input_ids.view(-1))
        
        if self.loss_type == "sigmoid":
            reward_loss = torch.sigmoid(-rewards).mean()
        elif self.loss_type == "hinge":
            reward_loss = torch.relu(1.0 - rewards).mean()
        elif self.loss_type == "ipo":
            reward_loss = (1.0 - torch.exp(rewards)).mean()
        elif self.loss_type == "kto_pair":
            reward_loss = (rewards**2).mean()  # 간단한 예제
        
        total_loss = self.beta_value * loss + self.ftx_gamma * reward_loss
        return total_loss

    def train(self, input_ids, rewards):
        self.optimizer.zero_grad()
        loss = self.compute_loss(input_ids, rewards)
        loss.backward()
        self.optimizer.step()
        return loss.item()

# 예제 데이터
input_text = "What is the capital of France?"
input_ids = tokenizer(input_text, return_tensors='pt').input_ids

# 보상 계산 (임의의 예제 보상)
with torch.no_grad():
    rewards = reward_model(input_ids)

# 강화 학습 훈련
trainer = PPOTrainer(model, reward_model, beta_value=0.1, ftx_gamma=0.5, loss_type="sigmoid", score_norm=True, whiten_rewards=True)
loss = trainer.train(input_ids, rewards)
print(f"Training loss: {loss}")
```

### 코드 설명

1. **모델 로드**:
    
    - 사전 학습된 GPT-2 모델과 토크나이저를 로드합니다.
2. **보상 모델 정의**:
    
    - 간단한 선형 레이어를 사용하여 보상 모델을 정의합니다.
3. **PPO 트레이너 정의**:
    
    - 다양한 RLHF 설정을 적용하여 PPO 트레이너 클래스를 정의합니다.
    - `compute_loss` 메서드는 모델의 출력과 보상을 사용하여 손실을 계산합니다.
    - `train` 메서드는 주어진 입력 시퀀스와 보상에 대해 모델을 훈련합니다.
4. **예제 데이터 및 훈련**:
    
    - 예제 입력 텍스트를 토큰화하고, 보상을 계산한 후, 모델을 훈련합니다.