---
title: "open-agent-builder"
related_raw: ["[[wiki/Agents/Implementation/open-agent-builder.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'implementations', 'llm_agent_builders_research']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Open Agent Builder

Firecrawl의 Open Agent Builder는 AI 에이전트를 위한 시각적 워크플로우 빌더입니다. 드래그 앤 드롭 방식으로 웹 스크래핑 파이프라인을 구축하고 실시간으로 실행할 수 있습니다. 주요 기능으로는 8가지 핵심 노드 유형(시작, 에이전트, MCP 도구, 변환, If/Else, While 루프, 사용자 승인, 종료)을 포함하는 시각적 워크플로우 빌더, Firecrawl을 통한 웹 스크래핑 및 검색 기능, 그리고 LangGraph 실행 엔진, Clerk 인증, Convex 데이터베이스와 같은 엔터프라이즈 기능이 있습니다.

기술 스택은 Next.js 16, TypeScript, LangGraph, Convex, Clerk, Tailwind CSS, React Flow 등을 포함하며, Anthropic Claude, OpenAI, Groq와 같은 LLM 제공업체를 지원합니다. 설치 및 설정에는 Node.js 18+, Firecrawl API 키, Convex 및 Clerk 계정이 필요합니다. Anthropic Claude는 MCP(Multi-tool Co-operation Protocol) 도구 지원에 현재 권장됩니다.

## 원문 URL

*   https://github.com/firecrawl/open-agent-builder/

## 추출된 URL

*   `http://localhost:3000`
*   `firecrawl.dev`
*   `clerk.com`

## 링크

*   [[wiki/Agents/Implementation/LangSmith-No-Code-Agent-Builder]]
*   [[wiki/Agents/Frameworks/LangChain/LangChain_Deep_Agents_LangGraph_Course]]
*   [[wiki/Agents/Frameworks/LangChain/LangChain_Middleware]]
*   [[wiki/Agents/Implementation/deepagents]]
*   [[wiki/Agents/Frameworks/LangChain/LangChain_DeepAgents_v1_Rewrite]]
*   [[wiki/Agents/Frameworks/LangChain/LangGraph-Supervisor-Pattern-and-Parlant]]
*   [[wiki/Agents/Coding-and-Engineering/fastcampus-ai-agent-vibecoding]]
*   [[wiki/Agents/Frameworks/LangChain/LangChain_LangGraph_1.0]]
*   [[wiki/Agents/Memory-and-Cognition/OpenMemory]]
*   [[wiki/Agents/Frameworks/LangChain/custom_langchain_chat_model]]
*   [[Projects/LinkedIn/현대 AI 멀티에이전트 시스템의 구조와 동작]]
*   Projects/LinkedIn/농업 AI Agent 구성
*   [[Archive/AI Agent 구성 (내부 교육용)]]