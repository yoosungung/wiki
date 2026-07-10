---
title: "PEFT-Options"
related_raw: ["[[wiki/Models/SFT/PEFT-Options.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_options']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# PEFT (Parameter-Efficient Fine-Tuning) 옵션

Avi Chawla는 2년 이상 LLM(대규모 언어 모델)을 미세 조정해왔으며, 상위 5가지 LLM 미세 조정 기술을 시각 자료와 함께 설명했습니다. 전통적인 미세 조정은 수십억 개의 매개변수와 수백 GB의 데이터를 다루는 LLM에는 비실용적이기 때문에, 매개변수 효율적인 미세 조정(PEFT)이 등장했습니다.

PEFT 기술은 LLM 가중치 행렬의 낮은 랭크 적응을 찾는 것을 포함합니다. 이는 원래 행렬에 저장된 정보를 여전히 나타낼 수 있는 더 작은 차원의 행렬입니다.

다음은 5가지 주요 미세 조정 기술입니다:

1.  **LoRA (Low-Rank Adaptation)**: 가중치 행렬과 함께 두 개의 낮은 랭크 학습 가능한 행렬 A와 B를 추가합니다. W를 미세 조정하는 대신, 이 낮은 랭크 행렬의 업데이트를 조정합니다. 가장 큰 LLM에서도 LoRA 행렬은 몇 MB의 메모리만 차지합니다.
2.  **LoRA-FA (Frozen-A)**: LoRA는 학습 가능한 매개변수를 크게 줄이지만, 낮은 랭크 가중치를 업데이트하는 데 상당한 활성화 메모리가 필요합니다. LoRA-FA는 행렬 A를 고정하고 행렬 B만 업데이트합니다.
3.  **VeRA**: LoRA에서 낮은 랭크 행렬 A와 B는 각 레이어마다 고유합니다. VeRA에서는 A와 B가 고정되고 무작위이며 모든 레이어에서 공유됩니다. 대신 레이어별 스케일링 벡터(b와 d)를 학습합니다.
4.  **Delta-LoRA**: 전통적인 방식은 아니지만 행렬 W도 조정합니다. 여기서는 두 연속 훈련 단계에서 행렬 A와 B의 곱 사이의 차이(또는 델타)가 W에 추가됩니다.
5.  **LoRA+**: LoRA에서는 행렬 A와 B가 동일한 학습률로 업데이트됩니다. LoRA+의 저자들은 행렬 B에 더 높은 학습률을 설정하면 더 나은 수렴을 가져온다는 것을 발견했습니다.

**관련 URL:**

*   MCP guidebook: `https://dailydoseofds.github.io/mcp-book/`

[출처](https://www.linkedin.com/posts/avi-chawla_i-have-been-fine-tuning-llms-for-over-2-years-activity-7400495583960018944-Tjzh?utm_source=share&utm_medium=member_ios&rcm=ACoAADm5eyABU_duDuXv1f9N-6JhXB_iNO6faes)
