---
title: "Memory-centric-Intelligence"
related_raw: ["[[wiki/Models/Reasoning-and-Cognition/Memory-centric-Intelligence.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'llm_applications_and_insights']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Memory-centric Intelligence

인공지능 분야에서 지난 10년간 트랜스포머(Transformer)가 지배적이었으나, 이제 그 한계가 드러나며 새로운 패러다임으로 전환되고 있습니다. 트랜스포머는 '컨텍스트 윈도우'라는 구조적 제약으로 인해 '기억 상실' 문제를 겪으며, 입력 길이가 길어질수록 연산 비용이 급증하고 장기 문맥에서 성능 저하를 보였습니다. 이는 모델이 진정한 의미의 '기억'을 갖지 못하고 대화가 새로 시작될 때마다 과거를 망각하는 백지상태에서 작동하기 때문입니다.

이러한 문제를 해결하기 위해 MIRAS와 Titans가 등장했습니다. 이들은 기억을 단순히 데이터를 저장하는 것이 아니라, 최적화 과정을 거치는 '살아있는 신경 모듈'로 재정의합니다. 특히 MIRAS는 '놀라움(Surprise)'을 신호로 삼아 예측과 실제의 오차가 클수록 정보를 강하게 기억하고, 덜 중요한 정보는 망각하는 방식으로 기억을 학습 과정으로 해석합니다. 이들의 기억 모듈은 추론(inference) 과정에서도 실시간으로 업데이트되어 '추론이 곧 학습(Inference is Learning)'인 시스템을 구현합니다.

Titans는 깊은 MLP(Multi-Layer Perceptron)로 구성된 'Neural Memory'를 도입하여 기존의 얕은 메모리 구조를 탈피했습니다. 이는 정보를 비선형적으로 요약하고 추상화하며, 모델이 과거 상태를 유지하거나 새로운 놀라움을 받아들여 기억을 수정할지 능동적으로 결정하게 합니다. 이러한 혁신 덕분에 Titans는 200만 토큰 이상의 초장기 문맥에서도 90% 이상의 정확도를 유지하며, 파라미터 수가 훨씬 많은 GPT-4를 능가하는 성능을 보여주었습니다.

결론적으로, MIRAS와 Titans의 등장은 트랜스포머의 개선을 넘어 인공지능 진화의 새로운 이정표를 제시합니다. Attention이 AI에게 '눈'을 뜨게 했다면, Neural Memory는 AI에게 경험을 축적하는 '기억'을 부여했습니다. 우리는 이제 '기억 중심 지능(Memory-centric Intelligence)' 시대로 진입하고 있으며, 미래의 AI는 Attention으로 현재를 직시하고 Neural Memory로 과거를 성찰하며 실시간 학습을 통해 스스로 진화하는 하이브리드 형태가 될 것입니다.

[출처](https://www.linkedin.com/posts/suk-hyun-kim-31ba9b369_qzcslr-memory-ai-activity-7403544752614174720-pzbn?utm_source=share&utm_medium=member_ios&rcm=ACoAADm5eyABU_duDuXv1f9N-6JhXB_iNO6faes)
