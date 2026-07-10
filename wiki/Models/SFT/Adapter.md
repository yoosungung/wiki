---
title: "Adapter"
related_raw: ["[[wiki/Models/SFT/Adapter.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

**Adapter**는 사전 학습된 모델을 특정 작업에 맞게 효율적으로 미세 조정하기 위한 방법론 중 하나입니다. Adapter는 주로 다음과 같은 이유로 사용됩니다:

1. **효율성**: 모든 모델 파라미터를 미세 조정하는 대신, Adapter는 소수의 추가 파라미터만 학습합니다. 이는 계산 비용을 크게 줄입니다.
2. **모듈성**: 특정 작업을 위해 학습된 Adapter를 다른 모델이나 작업에 쉽게 재사용할 수 있습니다.
3. **자원 절약**: 전체 모델의 모든 파라미터를 업데이트하지 않기 때문에, 메모리와 계산 자원이 절약됩니다.

### Adapter의 작동 방식

Adapter는 주로 Transformer 기반 모델에서 사용되며, 기존 모델의 파라미터는 고정(동결)하고, 새로운 작은 네트워크(어댑터 모듈)를 추가합니다. 이 작은 네트워크는 특정 작업에 맞게 학습됩니다. Adapter의 일반적인 구성은 다음과 같습니다:

1. **기존 모델 동결**: 기존 모델의 모든 파라미터는 고정되어 학습되지 않습니다.
2. **작은 네트워크 추가**: 모델의 각 계층(또는 일부 계층)에 작은 네트워크(어댑터 모듈)를 추가합니다.
3. **어댑터 학습**: 추가된 어댑터 모듈의 파라미터만 학습합니다.

### Adapter Path의 의미

**Adapter path**는 사용자가 미리 학습한 어댑터 모듈의 경로를 지정하는 설정입니다. 이 경로는 어댑터 모듈이 저장된 위치를 가리킵니다. 어댑터 모듈을 로드하여 특정 작업에 맞게 모델을 미세 조정하는 데 사용됩니다.

### Adapter의 예

Adapter를 사용한 미세 조정의 예는 다음과 같습니다:

1. **사전 학습된 모델**: 큰 언어 모델(예: BERT, GPT)을 사전 학습합니다.
2. **어댑터 추가**: 사전 학습된 모델의 각 계층에 작은 어댑터 모듈을 추가합니다.
3. **특정 작업에 맞게 학습**: 추가된 어댑터 모듈만 학습하여 특정 작업(예: 감정 분석, 번역)에 최적화합니다.

아래는 Python 코드로 어댑터를 추가하고 사용하는 예제입니다:
```python
from transformers import BertModel, BertConfig, AdapterConfig

# 사전 학습된 BERT 모델 로드
config = BertConfig.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased", config=config)

# 어댑터 구성
adapter_config = AdapterConfig.load("pfeiffer", reduction_factor=16)
model.add_adapter("classification_adapter", config=adapter_config)

# 어댑터 활성화
model.train_adapter("classification_adapter")

# 어댑터를 사용하여 모델 학습
# 여기서 model은 이제 어댑터 모듈만 학습합니다.

```

이 코드에서:

- **BertModel**: 사전 학습된 BERT 모델을 로드합니다.
- **AdapterConfig**: 어댑터 구성을 설정합니다 (여기서는 "pfeiffer" 구성 사용).
- **add_adapter**: 모델에 어댑터를 추가합니다.
- **train_adapter**: 추가된 어댑터를 학습 모드로 설정합니다.