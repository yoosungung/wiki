---
title: "Gated-Attention"
related_raw: ["[[wiki/Models/Architectures/Gated-Attention.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'llm_architecture_and_technical']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# 대규모 언어 모델을 위한 게이티드 어텐션

**출처**: [원본 링크](https://arxiv.org/pdf/2505.06708)

게이팅 메커니즘을 강화한 소프트맥스 어텐션에 대한 연구 논문입니다. Scaled Dot-Product Attention (SDPA) 이후 헤드별 시그모이드 게이트를 적용하는 간단한 수정이 일관되게 성능을 향상시킨다는 것을 발견했습니다.

## 주요 내용

*   **성능 향상:** SDPA 출력에 쿼리 의존적인 희소 게이팅 점수를 적용하여 조절하는 것이 성능 향상의 핵심 요인 중 하나입니다.
*   **훈련 안정성 향상:** 게이팅은 훈련 안정성을 높이고, 더 큰 학습률을 허용하며, 스케일링 속성을 개선합니다.
*   **비선형성 도입:** 소프트맥스 어텐션의 낮은 랭크 매핑에 비선형성을 도입하여 표현력을 향상시킵니다.
*   **어텐션 싱크 완화:** 희소 게이팅 메커니즘이 '어텐션 싱크'를 완화하고 장문 컨텍스트 외삽 성능을 향상시킵니다.

## 실험 결과

*   15B MoE 모델과 1.7B 밀집 모델에서 30가지 이상의 변형을 테스트했습니다.
*   SDPA 출력(G1) 또는 값 맵(G2)에 게이트를 삽입하는 것이 가장 효과적이었습니다.
*   헤드별 게이팅, 곱셈 게이팅, 시그모이드 활성화 함수가 선호되었습니다.
*   게이팅을 통해 훈련 안정성이 향상되고 손실 스파이크가 크게 감소했습니다.

## 분석

*   게이팅은 `Wv`와 `Wo` 사이의 비선형성 부족 문제를 해결하여 어텐션의 낮은 랭크 매핑의 표현력을 향상시킵니다.
*   효과적인 게이팅 점수는 희소하며, 쿼리 의존적인 희소성은 관련 없는 컨텍스트 정보를 필터링하는 데 중요합니다.
*   SDPA 출력의 희소 게이팅은 어텐션 싱크를 줄이고, 모델 내의 대규모 활성화를 감소시켜 훈련 안정성을 향상시킵니다.
*   게이팅은 모델이 재훈련 없이 더 긴 시퀀스로 효과적으로 일반화할 수 있도록 컨텍스트 길이 확장을 용이하게 합니다.

---
## 관련 노트
- [[wiki/Models/Architectures/Transformer 모델의 구조와 작동 원리를 깊이 이해]]
- [[wiki/Models/Architectures/RoPE-and-NoPE-Multi-Scale-Architecture]]
- [[wiki/Models/Architectures/Transformers-v5]]
