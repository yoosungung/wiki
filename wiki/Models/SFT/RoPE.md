---
title: "RoPE"
related_raw: ["[[wiki/Models/SFT/RoPE.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

RoPE (Rotary Position Embedding) Scaling은 Transformer 기반 모델에서 위치 정보를 효과적으로 인코딩하는 방법 중 하나입니다. Transformer 모델은 기본적으로 순서에 관계없는 데이터를 처리하기 때문에, 입력 토큰의 위치 정보를 인코딩하여 모델이 순서를 이해하도록 하는 것이 중요합니다. RoPE는 특히 대규모 언어 모델에서 이러한 위치 정보를 효율적으로 인코딩하는 방법입니다.

### RoPE (Rotary Position Embedding) 개념

RoPE는 토큰의 상대적 위치 정보를 각 토큰 임베딩에 주입하여 Transformer 모델이 순서 정보를 학습할 수 있도록 합니다. 이를 통해 모델은 순서에 민감한 작업에서 더 나은 성능을 발휘할 수 있습니다. RoPE는 다음과 같은 특징을 가집니다:

1. **회전 변환**: RoPE는 각 토큰의 임베딩 벡터에 회전 변환을 적용하여 위치 정보를 인코딩합니다. 이는 기존의 절대적 위치 임베딩 방식과 달리, 상대적 위치 정보를 효과적으로 인코딩할 수 있습니다.
2. **확장 가능성**: RoPE는 매우 큰 시퀀스 길이에 대해서도 위치 정보를 효과적으로 인코딩할 수 있어, 모델의 시퀀스 길이를 늘릴 때 유용합니다.
3. **연산 효율성**: RoPE는 상대적으로 간단한 연산을 사용하여 위치 정보를 인코딩하므로, 계산 비용이 적고 효율적입니다.

### RoPE Scaling의 역할

RoPE Scaling은 모델의 시퀀스 길이가 증가함에 따라 위치 임베딩의 스케일을 조정하는 방법입니다. 이는 매우 긴 시퀀스를 처리할 때 모델이 위치 정보를 효과적으로 인코딩할 수 있도록 도와줍니다.

### RoPE Scaling의 장점

1. **효과적인 위치 인코딩**: RoPE Scaling은 긴 시퀀스에서도 효과적인 위치 정보를 제공하여 모델이 순서 정보를 잘 학습할 수 있도록 합니다.
2. **모델 성능 향상**: 특히 긴 문장을 처리하는 NLP 작업에서 모델의 성능을 향상시킵니다.
3. **적응성**: RoPE Scaling은 다양한 시퀀스 길이에 대해 유연하게 적용될 수 있어, 다양한 길이의 입력을 처리할 수 있습니다.

### RoPE Scaling의 적용

RoPE Scaling을 적용하려면, 다음과 같은 절차를 따를 수 있습니다:

1. **회전 변환 매트릭스 생성**: 각 위치에 대해 회전 변환 매트릭스를 생성합니다.
2. **임베딩 벡터에 적용**: 각 토큰의 임베딩 벡터에 회전 변환을 적용하여 위치 정보를 인코딩합니다.
3. **스케일링 적용**: 시퀀스 길이에 따라 적절한 스케일링을 적용하여 위치 정보를 조정합니다.

### 예제 코드

다음은 RoPE를 적용한 위치 인코딩의 간단한 예제 코드입니다:
```python
import numpy as np

def rotary_embedding(dim, max_seq_len):
    # 회전 변환 매트릭스 생성
    theta = np.array([10000 ** (-2 * (i // 2) / dim) for i in range(dim)])
    seq_idx = np.arange(max_seq_len)
    idx_theta = np.outer(seq_idx, theta)

    cos_idx = np.cos(idx_theta)
    sin_idx = np.sin(idx_theta)

    def apply_rotary(x):
        # 임베딩 벡터에 회전 변환 적용
        x_cos = x * cos_idx[:x.shape[0], :]
        x_sin = x * sin_idx[:x.shape[0], :]
        return np.concatenate([x_cos, x_sin], axis=-1)
    
    return apply_rotary

# 예제 사용
max_seq_len = 512
dim = 128
apply_rotary = rotary_embedding(dim, max_seq_len)

# 임의의 임베딩 벡터에 회전 변환 적용
embedding = np.random.rand(max_seq_len, dim)
rotary_embedding = apply_rotary(embedding)

```

이 코드는 RoPE를 사용하여 임베딩 벡터에 위치 정보를 주입하는 과정을 보여줍니다.

### RoPE Scaling 옵션 구분

#### 1. None

**None** 옵션은 RoPE 스케일링을 적용하지 않는 것을 의미합니다.

- **특징**: 위치 정보의 스케일링이 없으며, 기본적인 RoPE 방식을 사용합니다.
- **적용**: 모든 위치에 대해 동일한 스케일링을 적용합니다.
- **사용 시기**: 상대적으로 짧은 시퀀스 길이에서 사용할 수 있으며, 스케일링이 필요하지 않은 경우 적합합니다.

#### 2. Linear

**Linear** 옵션은 위치 정보의 스케일링을 선형적으로 조정하는 방법입니다.

- **특징**: 시퀀스 길이에 따라 위치 임베딩의 크기를 선형적으로 증가시킵니다.
- **적용 방법**: 위치 임베딩 벡터가 시퀀스 길이에 비례하여 선형적으로 스케일링됩니다. 이를 통해 긴 시퀀스에서도 위치 정보를 보다 명확하게 인코딩할 수 있습니다.
- **사용 시기**: 긴 시퀀스를 처리할 때, 위치 정보가 선형적으로 증가하는 경우에 적합합니다.

#### 3. Dynamic

**Dynamic** 옵션은 위치 정보의 스케일링을 동적으로 조정하는 방법입니다.

- **특징**: 시퀀스의 길이와 모델의 학습 과정에 따라 위치 임베딩의 스케일링을 동적으로 조정합니다.
- **적용 방법**: 시퀀스의 특정 특성이나 길이에 따라 위치 임베딩의 크기가 비선형적으로 변화합니다. 이는 모델이 시퀀스 길이에 더 유연하게 적응할 수 있게 합니다.
- **사용 시기**: 다양한 길이의 시퀀스를 처리해야 하며, 시퀀스 길이에 따라 위치 정보의 중요도가 다를 때 적합합니다.