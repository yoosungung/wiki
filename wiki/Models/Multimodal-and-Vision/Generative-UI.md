---
title: "Generative-UI"
related_raw: ["[[wiki/Models/Multimodal-and-Vision/Generative-UI.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'llm_applications_and_insights']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# 생성형 UI (Generative UI)

"생성형 UI"는 AI 모델이 단순한 콘텐츠 생성을 넘어, 웹 페이지, 게임, 도구, 애플리케이션과 같은 몰입형 시각적 경험과 대화형 인터페이스를 포함한 전체 사용자 경험을 동적으로 생성하고 맞춤화하는 새로운 기술입니다.

## 주요 내용

이 기술은 사용자의 프롬프트(요구사항)에 따라 실시간으로 맞춤형 UI를 생성합니다. 예를 들어, "달의 위상에 따른 조수 변화를 보여줘"라고 요청하면, 단순히 텍스트로 설명하는 대신, 날짜를 조절하며 달의 모양과 조수 높이 변화를 직접 확인 할 수 있는 대화형 UI를 즉석에서 만들어줍니다.

이 기술은 현재 다음과 같은 Google 서비스에 적용되고 있습니다.

*   **Gemini 앱:** 동적 보기, 시각적 레이아웃 생성
*   **Google 검색 (AI 모드):** 검색 결과에 대화형 UI 제공

## 구현 방식

생성형 UI는 Google의 Gemini 3 Pro 모델을 기반으로 하며, 다음과 같은 과정을 통해 구현됩니다.

1.  **도구 접근 (Tool Access):** 모델이 UI 생성을 위해 필요한 도구에 접근합니다.
2.  **시스템 지침 (System Instructions):** 신중하게 작성된 시스템 지침에 따라 모델이 작동합니다.
3.  **후처리 (Post-processing):** 생성된 UI를 최종적으로 다듬어 사용자에게 제공합니다.

## 평가 및 전망

인간 평가자를 대상으로 한 테스트에서, 생성형 UI의 결과물은 표준 LLM의 텍스트 기반 결과물보다 훨씬 높은 선호도를 보였습니다.

이 연구는 아직 초기 단계이며, 생성 속도와 정확성을 개선하기 위한 작업이 계속 진행 중입니다. 생성형 UI 기술은 앞으로 사용자와 AI의 상호작용 방식을 근본적으로 변화시킬 잠재력을 가지고 있습니다.

## 관련 링크

*   [[wiki/Models/Small-Models/Google-Gemini-3]]
*   [[wiki/Agents/Implementation/Computer Use Agents]]
*   [[wiki/Agents/Robotics-and-VLA/ByteDance_UI-TARS-2_Autonomous_GUI_Agents]]
*   [[Projects/LinkedIn/Bioinfomatics와의 경험]]

## 원본 URL

*   [Generative UI: A rich, custom, visual, interactive user experience for any prompt](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/)
