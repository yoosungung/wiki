---
title: "LLM_Thinking_Time_Prompt_Engineering"
related_raw: ["[[wiki/Engineering/Prompt-Engineering/LLM_Thinking_Time_Prompt_Engineering.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'prompt_engineering']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

이 콘텐츠는 대규모 언어 모델(LLM)의 "사고 시간(Thinking Time)" 개념과 프롬프트 엔지니어링에서의 중요성에 대해 설명합니다. "더 깊이 생각하라"와 같은 프롬프트가 LLM의 내부 처리 시간을 크게 늘려 특히 복잡한 문제에 대해 더 정확하고 안정적인 출력을 유도하는 방법을 강조합니다. 이 게시물은 사고 시간이 프롬프트를 해석하고, 추론 사슬을 생성하며, 중간 계산을 수행하고, 후보 답변을 평가하는 과정을 포함한다고 설명합니다. 또한, 깊은 추론을 장려하기 위한 핵심 프롬프트 엔지니어링 기술로 연쇄적 사고(CoT) 프롬프팅(Zero-shot CoT 포함), 성찰 기반 CoT/자가 평가, 그리고 느린 사고 접근법을 소개합니다. 저자는 효과적인 프롬프트 엔지니어링이란 모델에게 "생각할" 충분한 기회를 제공하는 구조를 설계하여 속도와 사고의 깊이 사이의 균형을 맞추는 것이라고 강조합니다. CoT, 자가 성찰, 메타인지를 결합한 "느린 사고 프롬프트"의 예시도 제공됩니다.

---
### 관련 노트
- RAG기술현황(2)
- 추출 Prompt 예시
- LLM을 활용한 상향식 지식 그래프 구축
- [[wiki/Models/RL/RLHF]]