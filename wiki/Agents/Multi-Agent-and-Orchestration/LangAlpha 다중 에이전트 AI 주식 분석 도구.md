---
title: "LangAlpha 다중 에이전트 AI 주식 분석 도구"
related_raw: ["[[wiki/Agents/Multi-Agent-and-Orchestration/LangAlpha 다중 에이전트 AI 주식 분석 도구.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'implementations', 'general_llm_agent_projects']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# LangAlpha: 다중 에이전트 AI 주식 분석 도구

LangAlpha는 주식 시장에 대한 포괄적인 통찰력을 제공하도록 설계된 다중 에이전트 AI 주식 분석 도구입니다. 이 도구는 LLM(Large Language Models)과 에이전트 워크플로우를 활용하여 데이터 수집, 처리 및 분석을 자동화합니다.

## 주요 기술

*   **언어**: Python
*   **프레임워크**: LangChain, LangGraph
*   **데이터 소스**: Polygon, Yahoo Finance, Tavily Search, Tickertick News API 등

## 핵심 기능

LangAlpha는 시장 정보 에이전트 워크플로우를 통해 작동합니다. 사용자 쿼리를 기반으로 감독 에이전트가 계획을 세우고, 여러 전문 에이전트가 협력하여 정보를 수집하고 분석합니다.

*   **연구원 에이전트 (Researcher Agent)**: 관련 정보 검색
*   **시장 에이전트 (Market Agent)**: 시장 데이터 분석
*   **브라우저 에이전트 (Browser Agent)**: 웹 브라우징
*   **코더 에이전트 (Coder Agent)**: 코드 실행
*   **분석가 에이전트 (Analyst Agent)**: 심층 분석
*   **보고서 에이전트 (Reporter Agent)**: 종합 보고서 생성

## 주요 특징

*   **자율 연구**: 사용자의 최소한의 개입으로 심층적인 시장 분석 수행
*   **심층 분석**: Damodaran 가치 평가 모델 및 거래 전략 포함
*   **구조화된 계획**: 감독 에이전트에 의한 체계적인 작업 분배
*   **유연한 오케스트레이션**: LangGraph 기반의 유연한 에이전트 워크플로우
*   **실행 가능한 통찰력**: 최종적으로 실행 가능한 투자 통찰력을 제공

## 설치 및 실행

Docker를 통해 간편하게 설치하고 웹 UI(http://localhost:8000)를 통해 접근할 수 있습니다.

```bash
git clone https://github.com/Chen-zexi/LangAlpha.git
cd LangAlpha
docker-compose up --build
```

## 관련 URL

*   **GitHub 저장소**: [https://github.com/Chen-zexi/LangAlpha](https://github.com/Chen-zexi/LangAlpha)
*   **Damodaran 가치 평가 모델**: [notebooks/ginzu_interface.ipynb](https://github.com/Chen-zexi/LangAlpha/blob/master/notebooks/ginzu_interface.ipynb)
*   **거래 전략**: [counter-trend-trading-strategy](https://github.com/Chen-zexi/LangAlpha/blob/master/counter-trend-trading-strategy)

---
*tags*: #StockMarket, #AI, #MultiAgent, #LLM, #LangChain, #LangGraph, #DataAnalysis*
