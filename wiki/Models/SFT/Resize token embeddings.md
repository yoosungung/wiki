---
title: "Resize token embeddings"
related_raw: ["[[wiki/Models/SFT/Resize token embeddings.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_options']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

**"Resize the tokenizer vocab and the embedding layers"는 자연어 처리(NLP) 모델을 사용할 때, 토크나이저의 어휘(vocabulary) 크기와 임베딩 레이어의 크기를 조정하는 작업을 의미합니다. 이는 모델을 특정 작업이나 데이터셋에 맞추기 위해 어휘를 확장하거나 축소하고, 이에 맞게 임베딩 레이어의 크기를 조정하는 과정입니다.

### 왜 어휘와 임베딩 레이어를 조정하는가?

1. **어휘 확장**:
    
    - 새로운 토큰(단어, 기호 등)을 추가하여 모델이 특정 도메인이나 데이터셋에 더 잘 맞도록 합니다.
    - 예를 들어, 특정 분야의 전문 용어, 새로운 단어, 사용자 정의 토큰 등을 추가할 수 있습니다.
2. **어휘 축소**:
    
    - 사용하지 않는 토큰을 제거하여 모델의 크기와 훈련 시간을 줄입니다.
    - 불필요한 토큰을 제거함으로써 메모리 사용량을 최적화할 수 있습니다.
3. **임베딩 레이어 조정**:
    
    - 토크나이저의 어휘 크기가 변경되면, 임베딩 레이어의 크기도 이에 맞추어 조정해야 합니다.
    - 임베딩 레이어는 각 토큰을 고정된 차원의 벡터로 변환하므로, 어휘 크기가 변경되면 임베딩 매트릭스의 첫 번째 차원도 변경되어야 합니다.

### 예제 코드 (Hugging Face Transformers 사용)

다음은 Hugging Face의 Transformers 라이브러리를 사용하여 토크나이저 어휘와 임베딩 레이어를 조정하는 예제입니다:
```python
from transformers import BertTokenizer, BertModel
import torch

# 기존 토크나이저와 모델 로드
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# 새로운 토큰 추가
new_tokens = ["new_token1", "new_token2"]
num_added_tokens = tokenizer.add_tokens(new_tokens)

# 모델의 임베딩 레이어 크기 조정
model.resize_token_embeddings(len(tokenizer))

# 확인
print(f"Added {num_added_tokens} tokens.")
print(f"New vocabulary size: {len(tokenizer)}")
print(f"New embedding matrix size: {model.embeddings.word_embeddings.weight.size()}")

# 모델 예측 (예제 입력)
inputs = tokenizer("This is a test sentence with new_token1 and new_token2.", return_tensors='pt')
outputs = model(**inputs)

print(outputs.last_hidden_state.shape)  # 출력 형태 확인

```

### 코드 설명

1. **토크나이저와 모델 로드**:
    
    - BERT 모델과 토크나이저를 로드합니다.
2. **새로운 토큰 추가**:
    
    - `tokenizer.add_tokens(new_tokens)`를 사용하여 새로운 토큰을 토크나이저의 어휘에 추가합니다.
3. **임베딩 레이어 크기 조정**:
    
    - `model.resize_token_embeddings(len(tokenizer))`를 사용하여 모델의 임베딩 레이어 크기를 새로운 어휘 크기에 맞추어 조정합니다.
4. **확인**:
    
    - 새로운 어휘 크기와 임베딩 매트릭스의 크기를 확인합니다.
5. **모델 예측**:
    
    - 새로운 토큰이 포함된 입력 문장을 토크나이저로 인코딩하고, 모델을 통해 예측합니다.