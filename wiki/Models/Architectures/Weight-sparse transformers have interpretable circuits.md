---
title: "Weight-sparse transformers have interpretable circuits"
related_raw: ["[[wiki/Models/Architectures/Weight-sparse transformers have interpretable circuits.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'llm_systems_projects']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Weight-sparse transformers have interpretable circuits

이 논문은 언어 모델에서 해석 가능한 회로를 얻기 위해 가중치 희소 트랜스포머를 소개합니다. 대부분의 가중치를 0으로 제한함으로써 각 뉴런은 적은 수의 연결만을 가지게 되어 회로를 더 이해하기 쉽게 만듭니다. 연구자들은 모델을 가지치기하여 작업별 회로를 분리하며, 이 회로들은 종종 자연스러운 개념에 해당하는 뉴런과 잔여 채널을 포함합니다. 가중치 희소성은 해석 가능성을 향상시키지만, 성능과의 상충 관계가 있습니다. 모델 크기를 확장하면 성능-해석 가능성 경계가 개선됩니다. 이 방법은 "브릿지"를 사용하여 기존의 밀집 모델을 설명하는 데에도 적용될 수 있습니다.

## 관련 URL
*   [https://github.com/openai/circuit_sparsity/](https://github.com/openai/circuit_sparsity/)

## 원본
*   [https://arxiv.org/html/2511.13653v1](https://arxiv.org/html/2511.13653v1)

## 관련 노트
*   Transformer 모델의 구조와 작동 원리
*   [[wiki/Models/Architectures/Transformer 모델의 구조와 작동 원리 - Part 2 - 아키텍처와 구현]]
*   [[wiki/Models/Architectures/Transformer 모델의 구조와 작동 원리 - Part 3 - 심화 학습]]
*   Transformer Fine-tuning 옵션
