---
title: "Cutoff Length"
related_raw: ["[[wiki/Models/SFT/Cutoff Length.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_parameters']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

입력 시퀀스의 최대 길이를 제한하는 파라미터입니다. 이는 특히 텍스트 데이터를 다루는 자연어 처리(NLP) 모델에서 중요한 역할을 합니다. Cutoff Length는 다음과 같은 역할을 합니다:

### Cutoff Length의 역할

1. **메모리 관리**:
    
    - 긴 시퀀스를 처리하는 데 필요한 메모리 사용량을 줄입니다.
    - 메모리 제한이 있는 환경에서 모델이 과부하되지 않도록 합니다.
2. **계산 효율성**:
    
    - 긴 시퀀스를 처리하는 데 필요한 계산량을 줄여 연산 속도를 향상시킵니다.
    - 불필요하게 긴 입력이 모델을 느리게 만드는 것을 방지합니다.
3. **모델의 성능 최적화**:
    
    - 너무 긴 입력 시퀀스는 모델의 성능에 부정적인 영향을 미칠 수 있습니다. 중요한 정보가 희석되거나 모델이 과적합(overfitting)될 수 있습니다.
    - 적절한 길이로 자르거나 패딩(padding)하여 모델이 적절한 범위 내에서 데이터를 처리하도록 합니다.

### Cutoff Length 설정 방법

Cutoff Length는 모델의 입력 시퀀스가 너무 길거나 짧지 않도록 조정하는 데 사용됩니다. 이를 설정하는 방법에는 여러 가지가 있습니다:

1. **고정 길이**:
    
    - 모든 입력 시퀀스를 동일한 길이로 자르거나 패딩합니다.
    - 예를 들어, Cutoff Length를 512로 설정하면 모든 입력 시퀀스는 최대 512 토큰으로 제한됩니다.
2. **동적 길이**:
    
    - 입력 데이터의 분포에 따라 동적으로 길이를 설정할 수 있습니다.
    - 이는 특히 트랜스포머 모델에서 사용되며, 각 배치에서 최대 시퀀스 길이를 다르게 설정할 수 있습니다.

### 예제 코드

다음은 PyTorch를 사용하여 Cutoff Length를 설정하는 예제입니다:
```python
import torch
from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# 예제 입력 텍스트
texts = ["This is an example sentence.", "This is another example of a sentence that is a bit longer."]

# Cutoff Length 설정
cutoff_length = 10

# 입력 시퀀스를 토큰화하고 자르기
inputs = tokenizer(texts, max_length=cutoff_length, truncation=True, padding='max_length', return_tensors='pt')

# 모델에 입력
outputs = model(**inputs)

print(outputs)

```

이 예제에서는 `max_length`와 `truncation`을 사용하여 입력 시퀀스를 자르고, `padding`을 통해 고정 길이로 패딩합니다. Cutoff Length는 여기서 `cutoff_length`로 설정됩니다.