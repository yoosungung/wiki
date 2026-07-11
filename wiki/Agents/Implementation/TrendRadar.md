---
title: "TrendRadar"
related_raw: ["[[wiki/Agents/Implementation/TrendRadar.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'implementations', 'llm_agent_builders_research']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# TrendRadar: 스마트 트렌딩 뉴스 어시스턴트

TrendRadar는 가볍고 배포하기 쉬운 스마트 트렌딩 뉴스 어시스턴트 프로젝트입니다. 30초 만에 배포하여 최신 트렌딩 뉴스를 모니터링하고 개인화된 알림을 받을 수 있습니다.

## 주요 기능

*   **다중 플랫폼 트렌딩 뉴스 집계**: 11개 주요 플랫폼의 트렌딩 뉴스를 모니터링하고 사용자 정의 플랫폼 추가를 지원합니다.
*   **스마트 푸시 전략**: `daily`, `current`, `incremental` 등 다양한 푸시 전략을 제공합니다.
*   **정확한 콘텐츠 필터링**: 개인 키워드를 설정하여 관련 뉴스만 수신합니다.
*   **트렌딩 분석**: 뉴스 인기 변화를 실시간으로 추적합니다.
*   **개인화된 트렌딩 알고리즘**: 사용자 관심사에 따라 뉴스를 재정렬합니다.
*   **다중 채널 실시간 푸시**: WeWork, Feishu, DingTalk, Telegram, Email, ntfy를 지원합니다.
*   **다중 플랫폼 지원**: GitHub Pages, Docker를 지원합니다.
*   **AI 스마트 분석 (v3.0.0 신규)**: MCP(Model Context Protocol) 기반의 AI 대화형 분석 시스템을 제공합니다.

## Docker 배포

Docker를 통해 빠른 배포를 지원하며, `docker-compose` 사용을 권장합니다. 환경 변수를 통해 설정을 오버라이드할 수 있습니다.

## AI 분석 배포

MCP 기반의 AI 분석 기능은 Cherry Studio, Claude Desktop, Cursor 등 다양한 클라이언트를 지원합니다.

## 관련 링크

*   **GitHub Repository**: [https://github.com/sansan0/TrendRadar](https://github.com/sansan0/TrendRadar)
*   **MCP**: [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)

## 관련 노트

*   [[wiki/Agents/Frameworks/MCP/MCP]]
*   [[Projects/LinkedIn/현대 AI 멀티에이전트 시스템의 구조와 동작]]
*   [[wiki/Agents/Implementation/MaxKB]]
*   [[wiki/Agents/Implementation/Airweave]]

