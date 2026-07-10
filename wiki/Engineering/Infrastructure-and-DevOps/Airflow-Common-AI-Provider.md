---
title: "Airflow Common AI Provider - 데이터 파이프라인과 AI 에이전트의 통합"
related_raw: ["[[raw/Untitled.md]]"]
tags: ["Airflow", "AI-Agent", "Orchestration", "Common-AI-Provider", "AIOps"]
type: "wiki"
status: "published"
last_updated: "2026-04-30"
---

# Airflow Common AI Provider

2026년 Apache Airflow는 LLM 및 AI 에이전트를 기존 데이터 파이프라인(DAG)에 직접 통합할 수 있는 공식 프로바이더 패키지인 **'Common AI Provider'**를 출시하였다. 이를 통해 데이터 오케스트레이션과 AI 에이전트 운영을 하나의 플랫폼에서 통합 관리할 수 있게 되었다.

## 주요 기능 및 구성 요소

### 1. TaskFlow 데코레이터
기존의 TaskFlow 문법 내에서 AI 작업을 자연스럽게 정의할 수 있는 6가지 데코레이터를 제공한다.
- `@task.agent`: 멀티스텝 루프를 수행하는 AI 에이전트 정의.
- `@task.llm`: LLM을 이용한 텍스트 생성 및 처리.
- `@task.llm_sql`: 자연어를 SQL로 변환하여 실행.
- `@task.llm_branch`: LLM의 판단에 따른 파이프라인 분기 처리.
- `@task.llm_json`: 구조화된 데이터(JSON) 출력 보장.

### 2. HookToolset
Airflow가 이미 보유한 350개 이상의 Hook(S3, Snowflake, Slack, Postgres 등)을 별도의 MCP(Model Context Protocol) 설정 없이 에이전트의 도구(Tool)로 즉시 전환하여 사용할 수 있다.

### 3. Human-in-the-Loop (HITL)
`require_approval=True` 설정을 통해 AI의 결과물을 보류 상태로 잠그고, 사람이 직접 승인, 수정 또는 재요청할 수 있는 워크플로우를 내장 지원한다.

### 4. 내결함성 및 효율성
- **Durable Execution**: `durable=True` 설정을 통해 에이전트 작업 실패 시 처음부터 다시 시작하지 않고 캐시된 스텝부터 수 밀리초 내에 재실행 가능하다.
- **자동 로깅 및 감사**: 토큰 사용량, 도구 호출 이력, 대화 히스토리가 Airflow 메타데이터 DB에 자동으로 기록된다.

## 기대 효과
- **운영 복잡성 감소**: 별도의 에이전트 전용 오케스트레이터 없이 기존 Airflow 인프라를 그대로 활용 가능하다.
- **데이터 소유권 확보**: 로컬 LLM 또는 기업 전용 API와 결합하여 데이터 보안을 강화할 수 있다.
- **가시성 확보**: 데이터 파이프라인의 일부로 AI 에이전트의 동작을 모니터링하고 감사할 수 있다.

## 참고 문서
- [[wiki/Engineering/Infrastructure-and-DevOps/airflow.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/000_AIOps-MOC.md]]

---
*Source: LinkedIn - Hyunsoo Lee (2026-04-29)*
