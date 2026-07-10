---
title: "Snowflake Managed MCP Server & Snowflake Intelligence"
tags: ["Snowflake", "MCP", "Snowflake-Intelligence", "OSI", "Agent-Infrastructure"]
related_raw: ["[[raw/2026-04-24-snowflake-2026-updates-intelligence-mcp.md]]", "[[raw/2026-04-25-research-ingest-t2sql-osi-mcp.md]]"]
---

# Snowflake Managed MCP Server & Snowflake Intelligence

## 1. 개요
2026년 Snowflake는 **Snowflake Intelligence**와 **Managed MCP Server**를 통해 에이전트 중심의 기업 환경(Agentic Enterprise)을 위한 핵심 인프라를 구축하고 있습니다. 이는 에이전트가 기업 데이터에 안전하게 접근하고, 외부 도구와 협업하며, 비즈니스 맥락을 일관되게 유지하도록 돕습니다.

## 2. 주요 구성 요소

### Snowflake Intelligence
- 비즈니스 사용자를 위한 개인용 업무 에이전트.
- 자연어를 통해 데이터 분석, 시각화, 업무 자동화(Workflow)를 수행.
- **MCP 커넥터**를 기본 탑재하여 다단계 추론과 외부 도구 호출 지원.

### Managed MCP (Model Context Protocol) Server
- Snowflake 내부에서 호스팅되는 관리형 MCP 서버 인프라.
- **보안**: 별도의 외부 인프라 구축 없이 Snowflake의 거버넌스(RBAC) 체계 내에서 에이전트 도구를 실행.
- **연동**: Cortex Search, Cortex Analyst 등 내부 데이터 서비스뿐만 아니라 Gmail, Slack, Jira 등 외부 SaaS 도구와의 안전한 연결 제공.

## 3. 에이전트 문맥 공유 아키텍처 (2026)
2026년 Snowflake 에이전트 환경에서 문맥 공유는 다음과 같은 3계층 구조로 이루어집니다.

1.  **프로토콜 계층 (MCP)**: 에이전트와 도구 간의 통신 표준 (JSON-RPC 기반). "에이전트 통신을 위한 USB-C" 역할.
2.  **시맨틱 계층 (OSI)**: **Open Semantic Interchange** 표준을 통해 공유되는 데이터의 의미, 비즈니스 로직, 제약 조건을 정의.
3.  **거버넌스 계층**: Snowflake의 데이터 보안 및 정책에 따라 에이전트가 접근할 수 있는 문맥의 범위를 제어.

## 4. 핵심 가치: OSI와의 시너지
- **Time to Value 단축**: OSI 표준을 통해 시맨틱 모델을 표준화함으로써 에이전트가 비즈니스 로직을 이해하는 시간을 수개월에서 수분으로 단축.
- **Hallucination 감소**: 에이전트가 임의의 추론 대신 OSI에 정의된 비즈니스 규칙과 공식(Single Source of Truth)을 따르도록 강제.

## 관련 문서
- [[wiki/Engineering/Data-and-Security/OSI-Open-Semantic-Interchange.md]]
- [[wiki/Agents/Frameworks/MCP/MCP.md]]
- [[wiki/Agents/Text-to-SQL/ThoughtSpot-Spotter-Semantics.md]]
