---
title: "Prompt-Decorators"
related_raw: ["[[wiki/Engineering/Prompt-Engineering/Prompt-Decorators.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'prompt_engineering']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Prompt Decorators: AI 사고 구조 설계의 새로운 패러다임

"프롬프트 엔지니어링 2.0 시대"의 도래를 알리는 새로운 개념인 'Prompt Decorators'가 등장했습니다. 이는 AI의 사고 구조를 직접 '설계'하는 새로운 방법을 제시합니다.

기존 프롬프팅 방식은 동일한 질문에도 AI가 다른 답변을 내놓는 일관성 문제를 안고 있었습니다. 이러한 한계를 극복하기 위해, 영국 셰필드할람대학교의 Mostapha Kalami Heris 박사는 "Prompt Decorators: A Declarative and Composable Syntax for Reasoning, Formatting, and Control in LLMs (2025.10)"라는 논문을 통해 새로운 접근법을 제안했습니다.

## Prompt Decorators란?

Prompt Decorators는 ChatGPT, Claude, Gemini와 같은 대규모 언어 모델(LLM)이 '어떻게 사고하고, 어떤 형식과 톤으로 답할지'를 자연어 대신 선언형 문법(Declarative Syntax)으로 제어하는 개념입니다.

예를 들어, 다음과 같은 데코레이터를 사용하여 AI의 행동을 명시적으로 지시할 수 있습니다.

*   `+++Reasoning`
*   `+++Tone(style=formal)`
*   `+++OutputFormat(format=markdown)`

이는 단순한 간결성을 넘어, AI 응답의 '구조적 제어'와 '일관성'을 확보하는 것을 목표로 합니다.

## 주요 내용

논문에서는 총 20개의 주요 데코레이터를 두 가지 기능 계열로 분류합니다.

1.  **사고·생성 제어 (Cognitive & Generative):** AI의 추론 방식과 생성 과정을 제어합니다.
2.  **표현·시스템 제어 (Expressive & Systemic):** AI의 응답 스타일과 시스템 레벨의 동작을 제어합니다.

또한, AI의 사고 및 표현 과정을 6단계 파이프라인(Parsing, Scope Resolution, Planning, Reasoning, Formatting, Introspection)으로 구조화하여, 각 단계를 체계적으로 제어하려는 시도를 보여줍니다.

## 한계와 의의

Prompt Decorators는 아직 초기 연구 단계이며, 다음과 같은 한계를 가집니다.

*   모델 의존성
*   시뮬레이션된 추론
*   데코레이터 간 충돌 위험
*   높은 진입 장벽
*   보안 위험
*   완전한 재현성 부재

하지만 이러한 한계에도 불구하고, Prompt Decorators는 프롬프트 설계의 표준화를 제시하고 AI 거버넌스의 기초를 마련한다는 점에서 의미 있는 시도입니다. 이는 "프롬프트 엔지니어링의 체계화"를 통해 AI의 사고, 문체, 구조를 선언형 문법으로 설계할 수 있는 가능성을 열어주는 중요한 연구입니다.

## 관련 링크

*   [메타 프롬프트](./메타_프롬프트.md)
*   [프롬프트 컨텍스트 엔지니어링](./프롬프트_컨텍스트_엔지니어링.md)
*   [AI 질문법](./AI_질문법.md)
*   [LLM Thinking Time Prompt Engineering](./LLM_Thinking_Time_Prompt_Engineering.md)

## 추출된 URL

*   [연구 논문: Prompt Decorators](https://arxiv.org/abs/2510.19850)
