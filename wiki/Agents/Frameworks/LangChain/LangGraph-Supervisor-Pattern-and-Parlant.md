---
title: "LangGraph-Supervisor-Pattern-and-Parlant"
related_raw: ["[[wiki/Agents/Frameworks/LangChain/LangGraph-Supervisor-Pattern-and-Parlant.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'langchain_framework']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# LangGraph Supervisor Pattern and Parlant

LangGraph의 일반적인 감독자(supervisor) 패턴은 대화형 에이전트에서 들어오는 쿼리를 전문 하위 에이전트로 라우팅하지만, 고객이 여러 주제(예: 반품 및 보증)를 동시에 문의할 경우 하나의 하위 에이전트만 선택되어 다른 질문을 처리하지 못하거나 잘못된 정보를 제공할 수 있는 단점이 있습니다.

이 문제에 대한 해결책으로, 에이전트 간 라우팅 대신 '가이드라인(Guidelines)'을 사용하는 접근 방식을 제안합니다. 가이드라인은 '조건'과 '액션'으로 구성된 모듈식 지침 조각입니다. 사용자 쿼리에 따라 관련 가이드라인이 에이전트의 컨텍스트에 동적으로 로드되어 여러 주제에 걸쳐 일관된 응답을 가능하게 합니다.

이 접근 방식은 최근 인기를 얻고 있는 오픈 소스 프레임워크인 Parlant(15k+ 별)에 구현되어 있습니다.

**Original URL:**
- https://www.linkedin.com/posts/akshay-pachaar_massive-breakthrough-here-someone-fixed-activity-7389655732977319937-Kzir?utm_source=share&utm_medium=member_ios&rcm=ACoAADm5eyABU_duDuXv1f9N-6JhXB_iNO6faes

**Extracted URLs:**
- https://github.com/emcie-co/parlant
- https://arxiv.org/abs/2509.19599
