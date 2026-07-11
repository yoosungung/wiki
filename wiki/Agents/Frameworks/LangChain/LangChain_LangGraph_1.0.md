---
title: "LangChain_LangGraph_1.0"
related_raw: ["[[wiki/Agents/Frameworks/LangChain/LangChain_LangGraph_1.0.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'langchain_framework']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

---
**출처**: [원본 링크](https://blog.langchain.com/langchain-langgraph-1dot0/)
---

# LangChain and LangGraph 1.0

LangChain과 LangGraph 에이전트 프레임워크가 v1.0 이정표에 도달했습니다. LangChain 1.0은 핵심 에이전트 루프에 중점을 두고 미들웨어 개념을 통해 유연성을 제공하며 최신 콘텐츠 유형으로 모델 통합을 업그레이드했습니다. LangGraph 1.0은 프로덕션 수준의 장기 실행 에이전트를 지원하도록 설계된 하위 수준 프레임워크 및 런타임입니다.

**LangChain 1.0의 주요 변경 사항:**
*   새로운 `create_agent` 추상화 도입: 모든 모델 공급자와 함께 에이전트를 구축하는 가장 빠른 방법입니다.
*   LangGraph 런타임을 기반으로 구축되어 안정적인 에이전트를 지원합니다.
*   미들웨어를 통해 에이전트 루프의 동작을 세밀하게 제어하고 사용자 정의할 수 있습니다. (예: Human-in-the-loop, 요약, PII 수정)
*   표준 콘텐츠 블록을 통해 공급업체에 구애받지 않는 인터페이스를 제공합니다.
*   패키지 범위를 필수 추상화로 줄이고 레거시 기능은 `langchain-classic`으로 이동했습니다.
*   Python 3.9 지원이 중단되었으며, v1.0은 Python 3.10 이상을 필요로 합니다.

**LangGraph 1.0의 주요 기능:**
*   영구적인 상태: 에이전트의 실행 상태가 자동으로 유지됩니다.
*   내장된 지속성: 사용자 지정 데이터베이스 로직 없이 에이전트 워크플로우를 저장하고 재개할 수 있습니다.
*   Human-in-the-loop 패턴: 사람의 검토, 수정 또는 승인을 위해 에이전트 실행을 일시 중지할 수 있습니다.

LangChain은 표준 에이전트 패턴으로 빠르게 에이전트를 구축하고 배포하는 데 사용되며, LangGraph는 사용자 정의가 필요한 복잡한 워크플로우에 세밀한 제어를 제공합니다. LangChain 에이전트는 LangGraph를 기반으로 구축되므로 필요에 따라 두 프레임워크를 함께 사용할 수 있습니다.

새로운 통합 문서 사이트인 docs.langchain.com에서 Python 및 JavaScript에 걸쳐 모든 LangChain 및 LangGraph 문서를 확인할 수 있습니다.
