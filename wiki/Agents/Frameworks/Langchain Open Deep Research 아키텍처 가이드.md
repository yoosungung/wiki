---
title: "Langchain Open Deep Research 아키텍처 가이드"
related_raw: ["[[wiki/Agents/Frameworks/Langchain Open Deep Research 아키텍처 가이드.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'langchain_framework']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Langchain Open Deep Research 아키텍처 가이드

이 문서는 Langchain Open Deep Research의 내부 작동 방식에 대한 단계별 아키텍처 가이드를 요약한 것입니다.

## 주요 내용

Open Deep Research는 크게 세 부분으로 구성됩니다: 범위 지정(scoping), 연구(research), 최종 보고서(final report).

- **범위 지정 (Scoping):** 연구 단계의 입력을 구축하는 것을 목표로 합니다.
- **연구 (Research):** 감독자(supervisor)와 연구 하위 에이전트(research sub-agents)의 두 단계로 구성됩니다. 감독자는 브리프를 기반으로 Reflection을 사용하여 필요에 따라 여러 연구 하위 에이전트를 생성합니다.
- **보고서 (Report):** 수집된 모든 정보를 바탕으로 최종 보고서를 생성합니다.

## 핵심 디자인 패턴

- **Reflection 패턴:** 에이전트가 자체 출력을 평가하고 해당 피드백을 사용하여 응답을 반복적으로 개선할 수 있도록 합니다.
- **수동 도구 오케스트레이션 (Manual Tool Orchestration):** 복잡한 작업, 메모리 관리, 사용자 정의 라우팅 로직, 병렬 실행에 필요합니다.

## 단계별 가이드

1.  **사용자 질문:** LLM이 사용자에게 명확화가 필요한지 결정합니다.
2.  **사용자 명확화 질문에 응답:** LLM은 다시 명확화를 요청하거나 브리프 작성기로 진행할지 여부를 나타내는 구조화된 출력을 반환합니다.
3.  **브리프 생성 및 감독자에게 전달:** LLM을 호출하여 연구 브리프를 생성하고 상태에 저장합니다.
4.  **감독자 브리프 검토:** 감독자는 `think_tool`을 호출하여 수행할 작업을 이해합니다.
5.  **감독자 연구 시작:** 감독자는 LLM을 호출하여 `conduct_research` 도구와 함께 주제를 반환합니다.
6.  **연구 하위 에이전트 시작:** `conduct_research` 도구의 LLM 응답을 기반으로 동적으로 호출되는 하위 그래프입니다.
7.  **연구 에이전트 검색 시작:** 연구 노드는 `web_search` 도구 호출을 받습니다.
8.  **연구 에이전트 다중 검색 수행:** Tavily 검색을 사용하여 여러 검색을 병렬로 수행합니다.
9.  **연구 결과 검토:** 연구 노드는 `think_tool`을 호출하여 검색 결과를 검토합니다.
10. **연구 완료:** `research_complete` 도구를 호출하고 `compress_research` 노드로 이동하여 결과를 압축하고 감독자에게 반환합니다.
11. **연구 계획 재평가:** 감독자는 `think_tool`을 호출하여 다음 단계를 결정합니다.
12. **전체 연구 완료:** `research_complete` 도구가 호출되어 하위 그래프 실행을 완료합니다.
13. **최종 보고서 생성:** 마지막 단계는 LLM을 호출하여 최종 보고서를 생성하고 사용자에게 반환하는 것입니다.

## 관련 링크

- **Original Post:** [https://www.bolshchikov.com/p/open-deep-research-internals-a-step](https://www.bolshchikov.com/p/open-deep-research-internals-a-step)
- **GitHub:** [https://github.com/langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research)
- **Langchain Blog:** [https://blog.langchain.com/open-deep-research/](https://blog.langchain.com/open-deep-research/)

#Langchain #OpenDeepResearch #AI #Agent #Architecture
