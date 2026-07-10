---
title: "Langchain_다중_에이전트_아키텍처_선택"
related_raw: ["[[wiki/Agents/Multi-Agent-and-Orchestration/Langchain_다중_에이전트_아키텍처_선택.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'multi_agent_orchestration_and_patterns']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Langchain: 확장 가능한 에이전트 애플리케이션을 위한 다중 에이전트 아키텍처 선택

이 블로그 게시물은 확장 가능한 에이전트 애플리케이션을 위한 다중 에이전트 아키텍처의 필요성을 탐구합니다. 주요 패턴으로는 서브에이전트, 스킬, 핸드오프, 라우터 네 가지가 있으며, 각각 작업 조정, 상태 관리 및 순차적 잠금 해제에 다른 접근 방식을 제공합니다. 각 아키텍처는 지연 시간, 비용 및 사용자 경험에 영향을 미치며, 특정 시나리오에 따라 성능이 다릅니다. 단일 에이전트와 도구로 시작하여 필요할 때만 다중 에이전트 패턴으로 전환하는 것이 좋습니다.

---

**관련 URL:**
*   Subagents documentation: [https://www.blog.langchain.com/subagents-documentation](https://www.blog.langchain.com/subagents-documentation) (추정)
*   Tutorial: Build a personal assistant with subagents: [https://www.blog.langchain.com/tutorial-build-a-personal-assistant-with-subagents](https://www.blog.langchain.com/tutorial-build-a-personal-assistant-with-subagents) (추정)
*   Skills documentation: [https://www.blog.langchain.com/skills-documentation](https://www.blog.langchain.com/skills-documentation) (추정)
*   Tutorial: Build a SQL assistant with on-demand skills: [https://www.blog.langchain.com/tutorial-build-a-sql-assistant-with-on-demand-skills](https://www.blog.langchain.com/tutorial-build-a-sql-assistant-with-on-demand-skills) (추정)
*   Handoffs documentation: [https://www.blog.langchain.com/handoffs-documentation](https://www.blog.langchain.com/handoffs-documentation) (추정)
*   Tutorial: Build customer support with handoffs: [https://www.blog.langchain.com/tutorial-build-customer-support-with-handoffs](https://www.blog.langchain.com/tutorial-build-customer-support-with-handoffs) (추정)
*   Router documentation: [https://www.blog.langchain.com/router-documentation](https://www.blog.langchain.com/router-documentation) (추정)
*   Tutorial: Build a multi-source knowledge base with routing: [https://www.blog.langchain.com/tutorial-build-a-multi-source-knowledge-base-with-routing](https://www.blog.langchain.com/tutorial-build-a-multi-source-knowledge-base-with-routing) (추정)
*   multi-agent performance docs: [https://www.blog.langchain.com/multi-agent-performance-docs](https://www.blog.langchain.com/multi-agent-performance-docs) (추정)

---