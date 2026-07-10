---
title: "Agent-Lightning"
related_raw: ["[[wiki/Agents/Implementation/Agent-Lightning.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'implementations', 'general_llm_agent_projects']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

Agent Lightning은 AI 에이전트를 최적화하고 훈련하기 위한 프레임워크입니다.
## 요약
*   **제로 코드 변경 (거의):** 기존 에이전트 코드에 최소한의 변경으로 최적화가 가능합니다.
*   **다양한 에이전트 프레임워크 지원:** LangChain, OpenAI Agent SDK, AutoGen, CrewAI, Microsoft Agent Framework 등 어떤 에이전트 프레임워크와도 호환됩니다.
*   **선택적 최적화:** 다중 에이전트 시스템에서 특정 에이전트만 선택적으로 최적화할 수 있습니다.
*   **다양한 알고리즘 지원:** 강화 학습, 자동 프롬프트 최적화, 지도 미세 조정 등 다양한 알고리즘을 활용합니다.

## 관련 링크
*   [[wiki/Agents/Frameworks/Microsoft-Frameworks/Microsoft Agent Framework]]
*   [[wiki/Agents/Frameworks/LangChain/LangChain_LangGraph_1.0]]
*   [[wiki/Agents/Implementation/DS-STAR) A State-of-the-Art Versatile Data Science Agent]]

## 원문
*   **GitHub:** [https://github.com/microsoft/agent-lightning](https://github.com/microsoft/agent-lightning)
*   **문서:** [https://microsoft.github.io/agent-lightning/](https://microsoft.github.io/agent-lightning/)
*   **예제:** [https://github.com/microsoft/agent-lightning/tree/main/examples](https://github.com/microsoft/agent-lightning/tree/main/examples)

## 설치
```bash
pip install agentlightning
```

최신 빌드를 위해서는 다음 명령어를 사용합니다:
```bash
pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ agentlightning
```
