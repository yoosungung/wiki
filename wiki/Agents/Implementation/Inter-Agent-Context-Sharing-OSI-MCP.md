---
title: OSI와 MCP를 활용한 에이전트 간 맥락 공유 (Inter-Agent Context Sharing)
tags:
  - Agents
  - OSI
  - MCP
  - Context Sharing
  - Interoperability
related_wiki:
  - "[[wiki/Engineering/Data-and-Security/OSI-Specification-v0.0.1]]"
  - "[[wiki/Agents/Implementation/Deep-Agents-Architecture-Patterns.md]]"
related_raw:
  - "[[raw/2026-07-14-Apache-Ossie-명세.md]]"
type: wiki
status: published
last_updated: "2026-07-14"
updated: "2026-07-14"
---

# OSI와 MCP를 활용한 에이전트 간 맥락 공유

## 1. 개요
데이터 분석 에이전트가 서로 다른 플랫폼(예: Snowflake, ThoughtSpot)에서 동작하더라도 동일한 비즈니스 로직과 데이터 정의를 유지할 수 있도록 하는 기술적 프레임워크입니다. **Open Semantic Interchange (OSI)**를 표준 언어로, **Model Context Protocol (MCP)**을 전송 프로토콜로 활용합니다.

## 2. 핵심 아키텍처
에이전트 간 맥락 공유는 다음과 같은 3계층 구조로 이루어집니다.

1.  **Semantic Layer (OSI)**: 데이터셋, 지표, 관계를 YAML로 정의하여 비즈니스 진실의 단일 원천(SSoT)을 제공합니다.
2.  **Protocol Layer (MCP)**: OSI 모델을 에이전트가 읽을 수 있는 '리소스(Resource)'나 '도구(Tool)'의 메타데이터로 변환하여 전달합니다.
3.  **Agent Layer**: 전달받은 OSI 컨텍스트를 시스템 프롬프트에 주입하여 도구 호출 및 쿼리 생성을 수행합니다.

## 3. 작동 원리 (Workflow)
1.  **OSI 정의**: 데이터 엔지니어가 `revenue` 지표와 `quarterly_report` 컨텍스트를 OSI 파일로 작성합니다.
2.  **MCP 서버 연동**: MCP 서버가 OSI 파일을 로드하고, 이를 `semantic/models` 리소스로 노출합니다.
3.  **에이전트 연결**:
    *   **Agent A (Snowflake 기반)**: MCP를 통해 OSI 모델을 읽고 Snowflake SQL을 생성합니다.
    *   **Agent B (ThoughtSpot 기반)**: 동일한 MCP 리소스를 참조하여 ThoughtSpot Search 쿼리를 생성합니다.
4.  **결과 정렬**: 두 에이전트가 동일한 지표 정의를 사용하게 합니다. 실제 결과 일치는 SQL 방언 변환, 데이터 스냅샷, 접근 정책을 별도로 검증해야 합니다.

## 4. 주요 이점
*   **일관성 (Consistency)**: 플랫폼에 관계없이 "매출"의 정의가 동일하게 유지됩니다.
*   **재사용성 (Reusability)**: 한 번 정의된 OSI 모델을 다양한 AI 서비스(챗봇, 대시보드 에이전트 등)에서 즉시 재사용할 수 있습니다.
*   **할루시네이션 방지**: 에이전트가 임의의 SQL 방언이나 계산 로직을 추론하지 않고 OSI에 명시된 공식을 따릅니다.

## 5. 명세 상태와 구현 조건
OSI 프로젝트는 **Apache Ossie**로 이전됐습니다. 최신 안정판은 0.1.1이며 0.2.0.dev0은 미출시 초안이므로, “v1.0 기반 무설정 상호운용”으로 간주할 수 없습니다. MCP 연동 시에는 안정 스키마 고정, 플랫폼별 변환기, 권한 정책, SQL 방언 회귀 테스트가 필요합니다.

## 🔗 관련 문서
- [[wiki/Engineering/Data-and-Security/OSI-Specification-v0.0.1]]
- [[wiki/Agents/Implementation/000_Agent-Implementations-MOC.md]]
- [[wiki/Engineering/Data-and-Security/Semantic-Layer-Spec.md]]
