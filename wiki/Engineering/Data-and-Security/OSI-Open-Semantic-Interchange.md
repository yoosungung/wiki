---
title: "OSI (Open Semantic Interchange)"
tags: ["OSI", "Semantic Layer", "Agent", "MCP", "Snowflake", "Data"]
last_updated: "2026-05-08"
updated: "2026-05-08"
related_raw: ["[[raw/2026-04-22-osi-mcp-agent-sharing.md]]", "[[raw/2026-04-29-Spider2-OSI-Updates.md]]", "[[raw/2026-05-08-daily-research-data.md]]"]
---

# OSI (Open Semantic Interchange)

## 1. 개요
**OSI(Open Semantic Interchange)**는 데이터 플랫폼, BI 도구, AI 에이전트 간에 **시맨틱 모델(Semantic Model)** 정의를 표준화된 방식으로 교환하기 위한 벤더 중립적 오픈 소스 표준입니다. 

Snowflake, ThoughtSpot, dbt Labs 등이 주도하여 **2026년 1월 27일 v1.0 사양이 공식 발표**되었으며, 2026년 4월 현재 BlackRock, S&P Global, Sigma, Hex 등 업계 리더들이 공동 창립 파트너로 참여하며 생태계가 급격히 확장되었습니다.

## 2. 핵심 목표
*   **상호운용성**: 플랫폼에 구애받지 않고 지표(Metric) 정의를 공유. 에이전트가 도구와 팀 간에 일관된 문맥을 공유할 수 있도록 함.
*   **SSoT(Single Source of Truth)**: 전사 비즈니스 로직의 통일된 관리.
*   **AI 에이전트 최적화**: `ai_context` 메타데이터 필드를 통해 LLM이 데이터 구조와 비즈니스 규칙을 정확히 이해하도록 지원하여 가치 창출 시간(Time to Value)을 수개월에서 수분 단위로 단축.

## 3. 상세 기술 명세: `ai_context` 구현 패턴
OSI v1.0의 핵심은 YAML 기반의 `ai_context` 필드를 활용하여 LLM에게 '자연어 가이드'를 제공하는 것입니다.

### 구현 레벨 (Implementation Levels)
1.  **모델 레벨 (Model Level)**:
    - **역할**: 모델 전체의 분석 범위와 AI 페르소나 정의.
    - **예시**: "소매 유통 분석 전용. 별도 요청 없으면 취소 주문 제외. 순매출(Net Revenue) 기본 사용."
2.  **데이터셋 레벨 (Dataset Level)**:
    - **역할**: 특정 테이블/뷰의 데이터 성격 및 조인 주의사항 전달.
    - **예시**: "snowflake.analytics.orders 참조. 'COMPLETED' 상태만 매출로 간주."
3.  **지표/차원 레벨 (Measure & Dimension Level)**:
    - **역할**: 용어 혼선 방지 및 동의어 정의.
    - **예시**: "VIP = 연간 10회 이상 구매자", "실적 = [매출, 성과, Performance]"

👉 기술적인 세부 스키마는 **[[OSI-Specification-v1.0]]** 노트를 참조하십시오.

## 4. 에이전트 문맥 공유 (Agentic Enterprise)
OSI는 2026년 에이전트 아키텍처에서 **시맨틱 계층(Semantic Layer)**의 표준으로 자리 잡았습니다.

### ThoughtSpot-Snowflake 네이티브 통합 (2026)
*   **Metadata Sync**: Snowflake Semantic Views에 정의된 OSI 메타데이터가 ThoughtSpot Analyst Studio로 자동 동기화됩니다.
*   **Agentic Execution**: 사용자의 질문(Spotter)을 해석할 때 OSI의 `ai_context`를 참조하여 Snowflake Cortex Agent가 최적의 SQL을 생성합니다.

### MCP (Model Context Protocol) 연동
*   OSI 표준으로 정의된 시맨틱 컨텍스트를 **Managed MCP 서버**를 통해 여러 에이전트에게 실시간 배포합니다.
*   **Protocol vs Semantic**: MCP가 에이전트와 도구 사이의 통신 통로(Protocol) 역할을 한다면, **OSI는 그 통로를 통해 전달되는 정보의 '의미'와 '문맥'을 규격화**합니다.
*   이를 통해 에이전트 간 답변의 일관성을 유지하고 복잡한 다중 도메인 협업 시나리오를 지원합니다.

## 관련 문서
*   [[wiki/Agents/Text-to-SQL/Agentic-Semantic-Layer.md]]
*   [[wiki/Agents/Text-to-SQL/2026-04-22-T2SQL-Trends-Update.md]]
*   [[wiki/Agents/Frameworks/MCP/000_MCP-MOC.md]]
