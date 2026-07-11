---
title: "Lottery Ticket Hypothesis와 LLM"
related_raw: ["[[wiki/Models/Architectures/Lottery Ticket Hypothesis와 LLM.md]]"]
tags: ['wiki', 'ai_core', 'ai']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Lottery Ticket Hypothesis와 LLM

### 요약

MIT 연구진이 2018년 발표한 'Lottery Ticket Hypothesis'는 인공 신경망의 90%가 불필요할 수 있다는 가설을 제시했습니다. 이 가설은 큰 신경망을 학습시킨 후 가중치의 대부분을 제거하고 동일한 초기화 상태에서 다시 학습하면 원래 모델과 유사한 성능을 낼 수 있다고 주장했습니다. 그러나 이 아이디어는 전체 모델을 두 번 학습해야 하는 비효율성과 당시 하드웨어(GPU)가 희소성을 효율적으로 처리하지 못한다는 문제로 인해 실용성이 떨어진다는 평가를 받았습니다.

하지만 NVIDIA Ampere 아키텍처 이후 2:4 구조적 희소성을 전제로 설계된 Tensor Core가 도입되면서 상황이 변했습니다. 이 기술은 특정 희소 패턴(4개 중 2개만 non-zero)에서 연산을 절반으로 줄여 1.5~2배의 처리량 향상을 가능하게 했습니다. 이로써 희소성은 "정확하면서도 빠른" 상태가 되어 다시 주목받기 시작했습니다.

그럼에도 불구하고 "90% 희소 모델은 2배 빠르다"는 식의 과장된 주장이 확산되기도 했습니다. 실제 GPU는 90% 희소성이 아닌 50% 희소성(2:4 구조)을 가속하며, 90% 희소 모델은 오히려 성능 저하를 초래할 수 있습니다. 대규모 비용 절감 사례는 구조적 희소성 외에 양자화(INT8), 커널 퓨전, 배치 최적화 등 여러 최적화 기법이 복합적으로 적용된 결과입니다. 특히 LLM에서는 attention 계층이 희소성에 민감하여 주로 MLP 계층에 제한적으로 적용됩니다.

결론적으로 Lottery Ticket Hypothesis의 진정한 의미는 신경망이 본질적으로 과잉 파라미터화 되어 있으며, 대부분이 학습 안정화를 위한 '비계(scaffold)' 역할을 한다는 통찰입니다. 현대적 접근은 더 이상 dense 모델을 학습 후 잘라내는 방식이 아닌, 구조적 제약을 전제로 한 sparse-aware training과 양자화까지 포함한 공동 설계로 변화하고 있습니다. 미래는 단순히 큰 모델이 아니라, 무엇을 남기고 무엇을 버릴지 처음부터 알고 설계된 모델에 달려있습니다.

### 관련 링크

*   원본 게시물: `https://www.linkedin.com/posts/suk-hyun-k-31ba9b369_llm-tzartqrputyy-suaqtztfmqvz-activity-7413360421530841088-iyHr?utm_source=share&utm_medium=member_ios&rcm=ACoAADm5eyABU_duDuXv1f9N-6JhXB_iNO6faes`

### 관련 노트

*   `LLM`
*   `인공지능`
*   `AI`
*   `딥러닝`
*   `Lottery Ticket Hypothesis`
*   `Sparsity`
*   `Model Efficiency`
*   `AI Infrastructure`
*   `신경망`
*   `하드웨어 가속`
*   `GPU`
*   `NVIDIA Tensor Core`
*   `양자화`
*   `Transformer 모델`
