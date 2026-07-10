---
title: "WrenAI: 시맨틱 레이어 기반 오픈소스 Generative BI 에이전트"
related_raw: ["[[WrenAI Ask Data Questions in Any Language, Get Accurate SQL and Insights | AI Engineering님이 토픽에 대해 올림 | LinkedIn.md]]"]
tags: ["Agents", "Text-to-SQL", "BI", "Semantic_Layer", "Open_Source", "WrenAI"]
type: "wiki"
status: "published"
last_updated: "2026-05-15"
---

# WrenAI: 비즈니스 사용자를 위한 지능형 SQL 에이전트

## 1. 개요
WrenAI는 자연어로 데이터베이스에 질문하고 정확한 SQL 쿼리와 시각화된 통찰을 얻을 수 있게 돕는 **오픈소스 Generative BI 에이전트**입니다. 기존 LLM 기반 Text-to-SQL 도구들의 고질적인 문제인 쿼리 부정확성과 일관성 부족을 '시맨틱 레이어' 도입을 통해 해결했습니다.

- **GitHub Repository**: [https://github.com/Canner/WrenAI](https://github.com/Canner/WrenAI)
- **최신 업데이트 (2026-05-07)**: 기존 `wren-engine` 레포지토리가 메인 레포지토리의 `core/` 디렉토리로 통합되었습니다. Rust 기반의 고성능 시맨틱 엔진을 탑재하고 있습니다.

## 2. 핵심 작동 원리: 시맨틱 레이어 (MDL)
WrenAI의 차별점은 데이터베이스와 AI 사이에 위치한 **시맨틱 레이어**입니다.
- **MDL (Modeling Definition Language)**: 스키마, 조인(Join) 관계, 핵심 메트릭(KPI)을 사전에 정의하여 AI가 비즈니스 맥락을 정확히 이해하도록 합니다.
- **거버넌스 및 정확도**: 정의된 규칙 내에서 쿼리를 생성하므로 환각(Hallucination)을 최소화하고 항상 동일한 비즈니스 로직에 기반한 결과를 보장합니다.

## 3. 주요 기능 및 장점
- **다국어 지원**: 언어에 구애받지 않고 자연어로 데이터 질문 가능.
- **자동 시각화**: 쿼리 결과에 최적화된 차트 및 리포트 자동 생성.
- **광범위한 연결성**: BigQuery, Snowflake, PostgreSQL, MySQL, Redshift, DuckDB, Oracle, SQL Server 등 주요 DB 지원.
- **유연한 모델 선택**: OpenAI, Anthropic, Google Gemini, DeepSeek, Groq, Ollama 등 다양한 LLM과 연동 가능.
- **임베디드 지원**: API를 통해 커스텀 에이전트나 SaaS 기능 내에 통합 가능.

## 4. 시사점
WrenAI는 데이터 분석가(Analyst)의 병목 현상을 해소하고, 비즈니스 사용자가 직접 실시간 데이터에 접근하여 의사결정을 내릴 수 있는 'Self-service BI'의 수준을 한 단계 높였습니다. 특히 복잡한 RAG 인프라 없이도 강력한 성능을 발휘한다는 점이 특징입니다.

## 관련 문서
- [[wiki/Agents/Text-to-SQL/Agentic-Semantic-Layer.md|에이전트 시맨틱 레이어 분석]]
- [[wiki/Agents/Text-to-SQL/ThoughtSpot-Spotter-Semantics.md|ThoughtSpot Spotter 및 시맨틱 레이어 비교]]
- [[wiki/Agents/Text-to-SQL/000_Text-to-SQL-MOC.md|Text-to-SQL MOC]]
