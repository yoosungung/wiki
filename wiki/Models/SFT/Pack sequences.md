---
title: "Pack sequences"
related_raw: ["[[wiki/Models/SFT/Pack sequences.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_options']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

"Pack sequences into samples of fixed length"**는 가변 길이의 시퀀스 데이터를 고정된 길이로 변환하는 과정을 의미합니다. 이는 딥러닝 모델, 특히 순환 신경망(RNN)이나 트랜스포머 모델을 훈련할 때 중요한 전처리 단계입니다. 고정된 길이의 샘플로 변환하면 배치 처리가 용이해지고, GPU의 병렬 연산 성능을 최대로 활용할 수 있습니다.

### 왜 고정된 길이로 변환하는가?

1. **효율적인 배치 처리**:
    
    - 고정된 길이의 샘플로 변환하면 모델이 효율적으로 배치 처리를 수행할 수 있습니다.
    - 이는 메모리 사용을 최적화하고, 계산 속도를 향상시킵니다.
2. **GPU 활용 극대화**:
    
    - 고정된 길이의 입력 데이터를 사용하면 GPU의 병렬 처리 능력을 최대한 활용할 수 있습니다.
    - 가변 길이의 시퀀스를 처리할 때 발생하는 패딩과 관련된 비효율성을 줄입니다.
3. **일관된 입력 형식**:
    
    - 모델 훈련 과정에서 일관된 입력 형식을 유지하여, 복잡성을 줄이고 디버깅을 용이하게 합니다.

### 고정된 길이로 변환하는 방법

1. **패딩(Padding)**:
    
    - 짧은 시퀀스에 패딩 토큰을 추가하여 고정된 길이로 맞춥니다.
    - 일반적으로 패딩 토큰은 특별한 토큰 ID(예: 0)로 지정됩니다.
2. **잘라내기(Truncation)**:
    
    - 긴 시퀀스는 고정된 길이에 맞추어 잘라냅니다.
    - 고정된 길이보다 긴 시퀀스의 경우, 앞이나 뒤에서 일정 부분을 잘라냅니다.

### 예제 코드 (PyTorch 및 Hugging Face Transformers)

아래는 PyTorch와 Hugging Face Transformers 라이브러리를 사용하여 시퀀스를 고정된 길이로 변환하는 예제입니다:
```python
from transformers import BertTokenizer
import torch

# 토크나이저 로드
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# 예제 입력 시퀀스
texts = [
    "This is a short sentence.",
    "This is a much longer sentence that will need to be truncated to fit the fixed length."
]

# 고정된 길이 설정
fixed_length = 10

# 시퀀스 토큰화 및 고정된 길이로 변환
tokenized_inputs = tokenizer(texts, padding='max_length', truncation=True, max_length=fixed_length, return_tensors='pt')

# 결과 확인
print(tokenized_inputs)

# PyTorch 데이터셋 및 데이터로더 생성
class TextDataset(torch.utils.data.Dataset):
    def __init__(self, tokenized_inputs):
        self.input_ids = tokenized_inputs['input_ids']
        self.attention_mask = tokenized_inputs['attention_mask']

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return {
            'input_ids': self.input_ids[idx],
            'attention_mask': self.attention_mask[idx]
        }

dataset = TextDataset(tokenized_inputs)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=True)

# 배치 데이터 확인
for batch in dataloader:
    print(batch)
```

### 코드 설명

1. **토크나이저 로드**:
    
    - BERT 모델의 토크나이저를 로드합니다.
2. **입력 시퀀스 토큰화 및 고정된 길이로 변환**:
    
    - `tokenizer`를 사용하여 시퀀스를 토큰화하고, 패딩 및 잘라내기를 통해 고정된 길이로 변환합니다.
    - `padding='max_length'`와 `truncation=True` 옵션을 사용하여 시퀀스를 고정된 길이로 맞춥니다.
    - `max_length`를 `fixed_length`로 설정하여 고정된 길이를 지정합니다.
3. **PyTorch 데이터셋 및 데이터로더 생성**:
    
    - 변환된 시퀀스를 `TextDataset` 클래스로 감싸서 데이터셋을 생성합니다.
    - `DataLoader`를 사용하여 배치 처리를 위한 데이터로더를 생성합니다.
4. **배치 데이터 확인**:
    
    - 데이터로더를 통해 배치 데이터를 확인하고 출력합니다.