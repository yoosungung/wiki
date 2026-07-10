---
title: "LangChain-Deep-Agents"
related_raw: ["[[wiki/Agents/Frameworks/LangChain/LangChain-Deep-Agents.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'deep_agents']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# LangChain Deep Agents: Agent 2.0 시대의 서막

### 1. 개요 및 핵심 컨셉
LangChain이 발표한 **Deep Agents**는 기존 에이전트들의 한계를 극복하기 위해 설계된 차세대 프레임워크입니다. 핵심은 '에이전틱 프리미티브(Agentic Primitives)'를 통한 복잡한 과업의 구조적 분해와 실행입니다. 기존 에이전트들이 단일 컨텍스트 내에서 모든 일을 처리하려다 '컨텍스트 부패(Context Rot)'를 겪는 문제를 해결하기 위해, 독립된 실행 환경을 가진 서브 에이전트 구조를 도입했습니다.

### 2. 주요 기술 세부 사항
- **Subagents (하위 에이전트):** 메인 에이전트로부터 특정 임무를 부여받아 격리된 컨텍스트에서 실행됩니다. 작업 완료 후 결과만 부모 에이전트에게 반환하여 메인 컨텍스트를 깨끗하게 유지합니다.
- **Skills (기술 지침):** 에이전트의 능력을 `SKILL.md` 형식으로 정의합니다. 이는 '점진적 공개(Progressive Disclosure)' 전략을 사용하여, 에이전트가 해당 기술을 사용할 때만 상세한 지침을 컨텍스트에 로드하게 함으로써 효율성을 극대화합니다.
- **Agent Harness:** 에이전트의 실행 경로(Trace)를 모니터링하고 가이드하는 제어 계층입니다. 이를 통해 에이전트의 '탈주'를 방지하고 결정론적인 실행을 돕습니다.

### 3. 관련 기술 URL 및 리소스
- [LangChain Deep Agents Blog](https://blog.langchain.dev/deep-agents/)
- [Agentic Primitives Documentation](https://python.langchain.com/docs/concepts/agentic_primitives/)
- [Modal Sandbox for Code Execution](https://modal.com/)

### 4. 설명 이미지 추출 (Conceptual)
- ![Deep Agents Architecture](https://blog.langchain.dev/content/images/2026/03/deep-agents-arch.png) (에이전트-서브에이전트 계층 구조도)
- ![Context Management Visualization](https://blog.langchain.dev/content/images/2026/03/context-isolation.png) (컨텍스트 격리 및 결과 통합 프로세스)

### 5. 관련 노트 링크
- [[wiki/Agents/Implementation/Deep-Agents-2.0]]
- [[wiki/Agents/Implementation/Deep-Agents-Architecture-2026]]
- [[wiki/Agents/Frameworks/LangChain/LangGraph-Summary-2026]]
- [[wiki/Agents/Frameworks/Agent-Frameworks/Agent0-Framework]]
