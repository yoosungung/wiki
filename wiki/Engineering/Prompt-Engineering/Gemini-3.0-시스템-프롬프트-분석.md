---
title: "Gemini-3.0-시스템-프롬프트-분석"
related_raw: ["[[wiki/Engineering/Prompt-Engineering/Gemini-3.0-시스템-프롬프트-분석.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'prompt_engineering']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Gemini 3.0 시스템 프롬프트 분석

구글 딥마인드 개발자가 공유한 Gemini 3.0의 시스템 프롬프트를 통해, 복잡한 AI 에이전트의 행동을 제어하고 성능을 극대화하는 방법을 엿볼 수 있습니다. 이 시스템 프롬프트 하나로 벤치마크 성능이 5% 향상되었다는 점은 잘 만들어진 프롬프트의 중요성을 보여줍니다.

## 핵심 내용

1.  **충돌 시 '서열' 지정**: 프롬프트는 정책, 작업 순서, 전제 조건, 사용자 제약 등 충돌이 발생할 경우 따라야 할 명확한 우선순위를 정의합니다. 이는 에이전트가 혼란 없이 일관된 기준에 따라 작동하도록 만듭니다.

2.  **구체적인 프롬프트의 필요성**: Gemini와 같이 강력한 추론 능력을 가진 모델도, 복잡한 에이전트로서의 잠재력을 완전히 발휘하기 위해서는 단순한 추론을 넘어서는 구체적이고 상세한 지침이 필요합니다.

3.  **에이전트에게 요구되는 세 가지 행동**: 구글 개발자들은 에이전트에게 다음 세 가지 행동을 명시적으로 요구하라고 조언합니다.
    *   **끈기 (Persistence)**: 어려운 문제에 직면했을 때 포기하지 않고 계속 시도하도록 유도합니다.
    *   **위험 평가 (Risk Assessment)**: 행동을 취하기 전에 잠재적인 위험을 분석하고 평가하도록 합니다.
    *   **선제적 계획 (Proactive Planning)**: 단순히 주어진 작업을 수행하는 것을 넘어, 목표 달성을 위한 계획을 스스로 수립하도록 합니다.

이러한 프롬프팅 전략은 Distributional Convergence(모델이 특정 패턴의 답변만 생성하려는 경향)를 피하고, 보다 다양하고 창의적인 결과물을 얻는 데 도움이 될 수 있습니다.

## 관련 링크

*   원본 트윗: [https://x.com/_philschmid/status/1993032447291015282](https://x.com/_philschmid/status/1993032447291015282)
*   Google AI 프롬프트 전략 가이드: [https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ko#agentic-si-template](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ko#agentic-si-template)

## 관련 노트

*   [[wiki/Models/Small-Models/Google-Gemini-3]]
*   [[wiki/Engineering/Prompt-Engineering/Prompt-Decorators]]
*   [[wiki/Engineering/Prompt-Engineering/메타_프롬프트]]
*   [[Projects/LinkedIn/The Egg와 LLM 페르소나]]
*   [[wiki/Engineering/Prompt-Engineering/AI_질문법]]
