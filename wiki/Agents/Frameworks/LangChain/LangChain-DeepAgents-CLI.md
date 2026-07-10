---
title: "LangChain-DeepAgents-CLI"
related_raw: ["[[wiki/Agents/Frameworks/LangChain/LangChain-DeepAgents-CLI.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'langchain_framework']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# LangChain의 DeepAgents CLI: AI 에이전트의 영구 메모리 솔루션

**출처**: [원본 링크](https://www.linkedin.com/posts/paoloperrone_your-ai-agent-has-dementia-langchain-just-activity-7392761506779549696-XOHH)

LangChain이 출시한 DeepAgents CLI는 "AI 에이전트의 치매" 문제, 즉 세션 간에 컨텍스트를 잊어버리는 문제를 해결하기 위한 프로젝트입니다.

## 주요 기능

1.  **진정한 영구 메모리 (True persistent memory):**
    *   에이전트가 `~/.deepagents/memories/` 경로에 마크다운 형식의 노트를 직접 작성하여 과거 컨텍스트를 기억합니다.

2.  **안전한 파일 및 셸 작업:**
    *   파일 읽기/쓰기/편집 시 `diff` 미리보기를 제공하고, 셸 명령 실행 시 사용자 허가를 받습니다.

3.  **다중 에이전트 페르소나:**
    *   백엔드, 프론트엔드, 데브옵스 등 특정 전문 분야에 특화된 에이전트를 생성할 수 있습니다.

## 기술적 논의 (댓글 요약)

*   **긍정:** 영구 메모리가 컨텍스트적 의식, 서사 개발, 정체성 형성의 초기 단계가 될 수 있다는 의견이 있습니다.
*   **비판/우려:**
    *   기존 메모리 솔루션과의 차별성 부족.
    *   컨텍스트 창의 빠른 비대화 가능성.
    *   컨텍스트 드리프트, 메모리 블로트, "중간에서 길을 잃는" 문제 등 잠재적 기술 과제.

## 관련 링크

*   **GitHub 저장소:** https://github.com/langchain-ai/deepagents
*   **DeepAgents 문서:** https://docs.langchain.com/oss/python/deepagents/overview

---
## 관련 노트
- [[wiki/Agents/Frameworks/LangChain/LangChain_Deep_Agents_LangGraph_Course]]
- [[wiki/Agents/Frameworks/LangChain/LangChain_DeepAgents_v1_Rewrite]]
- [[wiki/Engineering/Prompt-Engineering/Context-Engineering-Sessions-and-Memory]]
- [[wiki/Agents/Memory-and-Cognition/Memory]]
