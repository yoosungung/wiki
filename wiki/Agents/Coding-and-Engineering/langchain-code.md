---
title: "langchain-code"
related_raw: ["[[wiki/Agents/Coding-and-Engineering/langchain-code.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'implementations', 'legal_and_coding_agents']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# langcode: AI 코딩 어시스턴트

**출처**: [원본 링크](https://github.com/zamalali/langchain-code)

LangCode는 Gemini, Anthropic, OpenAI, Ollama 모델을 ReAct 및 Deep 모드와 통합하여 코드베이스 내에서 기능 구현, 버그 수정, 코드 분석 등을 수행하는 강력한 CLI 도구입니다.

## 주요 기능
*   **대화형 런처:** `langcode` 명령으로 시작하여 사용자 친화적인 인터페이스를 통해 세션을 구성하고 다양한 기능에 접근할 수 있습니다.
*   **AI 기반 코드 이해:** 코드 심층 분석을 통해 질문에 답변하고 통찰력을 제공합니다.
*   **자동화된 코딩 작업:** 최소한의 노력으로 기능 구현, 버그 수정, 코드 리팩토링을 수행합니다.
*   **안전하고 검토 가능한 변경 사항:** 모든 수정 사항에 대해 명확한 diff를 생성하여 사용자가 변경 사항을 제어할 수 있도록 합니다.
*   **다중 LLM 지원:** Google Gemini 및 Anthropic Claude와 원활하게 통합되며, 작업에 가장 적합한 모델로 지능적으로 라우팅합니다.
*   **사용자 정의 가능한 지침:** `.langcode/langcode.md` 파일을 사용하여 프로젝트별 규칙 및 지침으로 에이전트의 동작을 맞춤 설정할 수 있습니다.
*   **MCP 확장성:** Model Context Protocol ([[wiki/Agents/Frameworks/MCP/MCP|MCP]])을 통해 사용자 정의 도구를 통합할 수 있습니다.

## 추론 엔진 및 워크플로우
*   `auto`: DEEP AUTOPILOT 종단 간 실행.
*   `bug_fix`: 진단 → 패치 → 검증의 안내된 워크플로우.
*   `feature_impl`: 계획 → 작은 diff → 테스트 → 검토의 워크플로우.

## 내부 작동 방식
*   **하이브리드 지능형 LLM 라우터:** 규칙이 강화되고 피드백을 인식하는 라우터가 복잡성, 컨텍스트 크기, 지연 시간 및 비용을 기반으로 각 작업에 적합한 모델을 선택합니다.
*   **에이전트 아키텍처:**
    *   **ReAct Agent:** 채팅, 읽기 및 대상 편집을 위한 빠른 루프입니다.
    *   **Deep Agent:** 복잡한 작업을 위한 구조화된 다중 에이전트 시스템으로, `research-agent`, `code-agent`, `git-agent`와 같은 하위 에이전트로 구성됩니다.

---
## 관련 노트
- [[wiki/Agents/Frameworks/LangChain/LangChain_Deep_Agents_LangGraph_Course]]
- [[wiki/Agents/Frameworks/LangChain/LangChain_DeepAgents_v1_Rewrite]]
- [[wiki/Agents/Frameworks/LangChain/custom_langchain_chat_model]]
- [[wiki/Agents/Frameworks/MCP/MCP]]
