---
title: "Snowflake AI-Native 데이터 스택 분석"
related_raw: ["[[WrenAI Ask Data Questions in Any Language, Get Accurate SQL and Insights | AI Engineering님이 토픽에 대해 올림 | LinkedIn.md]]"]
tags: ["Engineering", "Infrastructure", "Snowflake", "AI-Native", "Cortex", "Text-to-SQL"]
type: "wiki"
status: "published"
last_updated: "2026-05-15"
updated: "2026-05-15"
---

# Snowflake AI-Native 데이터 플랫폼 스택

## 1. 개요
Snowflake는 단순한 데이터 웨어하우스를 넘어, 데이터 플랫폼 내부에서 AI 모델 실행, 에이전트 오케스트레이션, 비즈니스 인텔리전스를 통합 제공하는 **AI-Native 데이터 스택**으로 진화하고 있습니다.

## 2. Snowflake AI 스택의 4대 핵심 구성 요소

### 1) Cortex Code (The AI Engineer)
- **역할**: Snowflake 내부에서 실행되는 완전한 자율형 AI 에이전트.
- **기능**: 단순 코드 제안을 넘어 파이프라인 구축, SQL/Snowpark 작성, 태스크 관리, 창고(Warehouse) 운영 등을 직접 수행합니다.
- **비유**: "Snowflake 플랫폼 전체를 위한 GitHub Copilot".

### 2) Snowflake Copilot (The SQL Assistant)
- **역할**: 개발자의 생산성 향상을 위한 보조 도구.
- **기능**: 쿼리 제안, 로직 설명, 에러 수정, 조인(Join) 추천 등 SQL 작성 프로세스를 가속화합니다.

### 3) Cortex Analyst (The Business Brain)
- **역할**: 비즈니스 사용자를 위한 자연어 인터페이스.
- **기능**: 사용자의 질문을 SQL로 변환하고 즉시 실행하여 답을 제공합니다. 시맨틱 모델을 통해 비즈니스 맥락을 정확히 인지합니다.

### 4) AI SQL (AI Inside Queries)
- **역할**: SQL 쿼리 내부에서 직접 호출 가능한 AI 함수.
- **기능**: `SNOWFLAKE.CORTEX.SENTIMENT()`, `SUMMARIZE()` 등 SQL 함수 형태로 감성 분석, 텍스트 분류, 요약 등을 수행합니다.

## 3. 기술적 시사점: Unstructured to Structured
Snowflake AI 스택의 핵심 목표는 기업 데이터의 80%를 차지하는 **비정형 데이터(문서, 이메일, 전사 기록 등)**를 SQL 환경 내에서 즉시 사용 가능한 정형 데이터로 변환하는 것입니다. 별도의 외부 파이프라인 없이 데이터가 있는 곳에서 직접 AI가 가동된다는 점이 강력한 경쟁 우위입니다.

## 관련 문서
- [[wiki/Agents/Text-to-SQL/WrenAI-Generative-BI-Agent.md|WrenAI: 시맨틱 레이어 기반 BI 에이전트]]
- [[wiki/Engineering/Infrastructure-and-DevOps/000_Infrastructure-and-DevOps-MOC.md|인프라 및 DevOps MOC]]
- [[wiki/Models/Architectures/BigQuery의 AI 시대에 맞춰 재해석된 SQL.md|BigQuery의 SQL 재해석 분석]]
