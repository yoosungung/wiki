---
title: "Event-Deep-Research"
related_raw: ["[[wiki/Agents/Implementation/Event-Deep-Research.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'implementations', 'llm_agent_builders_research']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Event Deep Research

**Event Deep Research**는 역사적 인물의 삶을 연구하고, 주요 사건들을 구조화된 JSON 타임라인으로 추출하는 AI 에이전트입니다.

![Event Deep Research](https://github.com/bernatsampera/event-deep-research/raw/master/media/event-deep-research.webp)

## 주요 기능

*   **감독 에이전트 (Supervisor Agent)**: 연구, 사고, 완료 등 여러 도구를 사용하여 전체 워크플로우를 조정합니다.
*   **병합 워크플로우 (Merge Workflow)**: 여러 소스에서 얻은 이벤트를 통합하고 중복을 제거합니다.
*   **다양한 모델 지원**: OpenAI, Anthropic, Google 또는 로컬 모델(Ollama)을 지원합니다.

## 아키텍처

![Architecture](https://github.com/bernatsampera/event-deep-research/raw/master/media/kronologs-graph.webp)

## 사용법

LangGraph Studio (http://localhost:2024)를 통해 `supervisor` 그래프를 선택하고 연구 쿼리(예: `{"person_to_research": "Albert Einstein"}`)를 입력하여 에이전트의 작동을 실시간으로 확인할 수 있습니다.

## 리소스

*   **GitHub Repository**: [https://github.com/bernatsampera/event-deep-research](https://github.com/bernatsampera/event-deep-research)

## 출처

*   [GitHub README](https://github.com/bernatsampera/event-deep-research/blob/master/README.md)
