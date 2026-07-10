---
title: "Deep Think with Confidence"
related_raw: ["[[wiki/Models/SFT/Deep Think with Confidence.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

대규모 언어 모델(LLM)의 추론 성능과 효율성을 동시에 향상시키는 방법을 제안합니다.

이 기술의 핵심은 **모델 내부의 '신뢰도 신호'를 활용**하는 것입니다. LLM이 여러 추론 경로를 생성할 때, DeepConf는 신뢰도가 낮은(품질이 낮은) 추론을 실시간(온라인) 또는 생성 후(오프라인)에 동적으로 필터링합니다.

주요 장점은 다음과 같습니다:

- **추가 학습 불필요:** 별도의 모델 훈련이나 하이퍼파라미터 조정 없이 테스트 시점에 바로 적용할 수 있습니다.
    
- **높은 효율성:** 기존 방식 대비 생성되는 토큰 수를 최대 84.7%까지 줄이면서도,
    
- **높은 정확도:** 추론 정확도는 유지하거나 오히려 향상시킵니다. (AIME 2025 벤치마크에서 최대 99.9% 정확도 달성)

https://arxiv.org/pdf/2508.15260