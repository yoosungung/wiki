---
title: "LLM 추론의 함정 - 생각을 멈춰야 정확해진다"
related_raw: ["[[wiki/Models/Reasoning-and-Cognition/LLM 추론의 함정 - 생각을 멈춰야 정확해진다.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'llm_applications_and_insights']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# LLM 추론의 함정 - 생각을 멈춰야 정확해진다

대규모 언어 모델(LLM)에서 '추론(Reasoning)'이 항상 성능을 향상시킨다는 기존의 믿음이 도전받고 있습니다. 특히 오탐률(FPR) 1% 미만이 요구되는 안전성 필터링이나 환각 탐지 같은 작업에서는 추론이 오히려 성능을 저하시키고 단순 분류보다 나쁜 결과를 초래하는 역설적인 현상이 나타났습니다.

## 주요 내용

- 연구 결과, 전체 정확도는 추론을 포함한 'Think On' 모드가 더 높았지만, 가장 중요한 1% FPR 기준에서는 추론이 없는 'Think Off' 모드가 일관되게 더 높은 재현율(Recall)을 보였습니다.
- 이러한 현상의 원인은 추론이 모델의 확신(confidence)을 극단적으로 밀어 넣기 때문입니다. 추론 과정이 길어질수록 모델은 옳고 그름을 떠나 과도한 확신을 가지게 되며, 실제로는 안전한 입력까지도 높은 위험 확신을 부여하게 됩니다.
- 추론 기반의 'self-verbalized confidence'는 문제가 심각하여 일부 데이터셋에서 1% FPR 기준 재현율이 0%에 가깝게 떨어지는 등 정밀도 중심 환경에서는 사실상 사용 불가능한 방식임이 드러났습니다.

## 해결책

- 'Think Off'와 'Think On'의 확신을 단순 평균하는 간단한 앙상블 방식이 가장 효과적이었습니다. 이 방법은 'Think On'의 전체 정확도 장점과 'Think Off'의 극저 FPR 환경 재현율 장점을 동시에 확보할 수 있었습니다.

결론적으로, 추론은 강력하지만 잘못된 확신을 지나치게 강화하여 높은 정밀도가 요구되는 환경에서는 오히려 해를 끼칠 수 있습니다.

## 관련 링크

- **LinkedIn Post:** [https://www.linkedin.com/posts/suk-hyun-kim-31ba9b369_tyerxk-sjkuis-confidence-activity-7394859743699218432-QM1S](https://www.linkedin.com/posts/suk-hyun-kim-31ba9b369_tyerxk-sjkuis-confidence-activity-7394859743699218432-QM1S)

#LLM #Reasoning #Confidence #AI
