---
title: "NEFTune Alpha"
related_raw: ["[[wiki/Models/SFT/NEFTune Alpha.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

임베딩 벡터에 추가되는 노이즈의 크기를 조절하는 파라미터입니다. 이는 모델의 학습 과정에서 임베딩 벡터에 노이즈를 추가하여 모델의 일반화 성능을 향상시키고, 과적합을 방지하는 데 사용됩니다.

### NEFTune Alpha의 역할

1. **모델 일반화 성능 향상**:
    - 임베딩 벡터에 노이즈를 추가함으로써 모델이 훈련 데이터에 너무 의존하지 않도록 합니다. 이는 모델이 다양한 데이터 분포에 대해 더 잘 일반화할 수 있도록 돕습니다.
2. **과적합 방지**:
    - 훈련 과정에서 노이즈를 추가하면 모델이 훈련 데이터의 노이즈와 변동성을 학습하게 되어, 과적합(overfitting)을 방지할 수 있습니다.
3. **로버스트니스 강화**:
    - 노이즈 추가는 모델이 입력 데이터의 작은 변동성에 덜 민감하도록 만들어, 모델의 로버스트니스(robustness)를 강화합니다.

### NEFTune Alpha 설정 방법

NEFTune Alpha는 임베딩 벡터에 추가할 노이즈의 표준 편차(standard deviation)를 정의합니다. 일반적으로 작은 값을 사용하여 모델이 안정적으로 학습할 수 있도록 합니다. 노이즈의 크기가 너무 크면 모델의 학습이 불안정해질 수 있습니다.

### 예제 코드

아래는 PyTorch를 사용하여 NEFTune Alpha를 설정하고 임베딩 벡터에 노이즈를 추가하는 예제입니다:
```python
import torch
import torch.nn as nn

class NoisyEmbedding(nn.Module):
    def __init__(self, num_embeddings, embedding_dim, alpha):
        super(NoisyEmbedding, self).__init__()
        self.embedding = nn.Embedding(num_embeddings, embedding_dim)
        self.alpha = alpha

    def forward(self, input):
        embedding_vectors = self.embedding(input)
        if self.training:  # Only add noise during training
            noise = torch.normal(0, self.alpha, size=embedding_vectors.size()).to(embedding_vectors.device)
            embedding_vectors += noise
        return embedding_vectors

# 파라미터 설정
num_embeddings = 1000  # 임베딩의 개수
embedding_dim = 128  # 임베딩 벡터의 차원
alpha = 0.01  # 노이즈의 표준 편차 (NEFTune Alpha)

# 모델 생성
model = NoisyEmbedding(num_embeddings, embedding_dim, alpha)

# 예제 입력
input = torch.randint(0, num_embeddings, (32,))  # 배치 크기 32

# 모델 예측
output = model(input)
print(output)

```

이 예제에서는 `NoisyEmbedding`이라는 클래스를 정의하여, 임베딩 벡터에 노이즈를 추가합니다. `alpha` 파라미터는 노이즈의 표준 편차를 조절하는 데 사용됩니다. 훈련 모드에서만 노이즈를 추가하도록 설정하여, 검증 또는 테스트 단계에서는 노이즈를 추가하지 않습니다.