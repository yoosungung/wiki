---
title: nanochat을 Transformers로 포팅하기
related_raw:
  - "[[wiki/Models/Architectures/nanochat을 Transformers로 포팅하기]]"
tags:
  - wiki
  - ai_core
  - models_and_libraries
  - llm_frameworks_and_libraries
type: wiki
status: draft
last_updated: "2026-04-19"
---


Andrej Karpathy의 nanochat 프로젝트를 Hugging Face의 `transformers` 라이브러리에 통합하는 과정을 통해 AI 모델링의 역사를 학습합니다. 이 과정은 nanochat이 다른 정식 모델들과 어떻게 관련되고 구성 요소를 공유하는지에 대한 통찰을 제공합니다.

![](https://huggingface.co/spaces/nanochat-students/transformers/blob/main/image1.png)

## nanochat 아키텍처의 주요 개선 사항

- **QK 정규화 (QK Normalization)**: Llama 4에서 대중화되었으며, 훈련 중 어텐션 점수를 안정화시킵니다.
- **가중치 분리 (Untied Weights)**: 임베딩과 LM 헤드 간의 가중치를 분리하여 모델에 유연성을 더합니다.
- **ReLU² 활성화 (ReLU² Activation)**: 표준 GELU 활성화를 대체하는 더 빠른 대안입니다.
- **멀티 쿼리 어텐션 (Multi-Query Attention, MQA)**: KV 캐시의 메모리 사용량을 줄입니다.

## 관련 자료

- [nanochat-students on Hugging Face](https://huggingface.co/nanochat-students)
- [nanochat GitHub](https://github.com/karpathy/nanochat)
- [Transformers Documentation](https://huggingface.co/docs/transformers/)
- [Llama 2 Paper](https://arxiv.org/abs/2307.09288)

## 관련 노트

- [[wiki/Models/Architectures/Transformer 모델의 구조와 작동 원리 - Part 2 - 아키텍처와 구현]]
- [[wiki/Models/Architectures/Transformer 모델의 구조와 작동 원리 - Part 3 - 심화 학습]]
- [[wiki/Models/Architectures/Transformer 모델의 구조와 작동 원리를 깊이 이해]]
- [[wiki/Models/Architectures/Weight-sparse transformers have interpretable circuits]]
