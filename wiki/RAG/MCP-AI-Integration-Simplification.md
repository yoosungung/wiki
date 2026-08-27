---
title: "Model Context Protocol(MCP)을 통한 AI 도구 통합 간소화"
related_raw: ["[[raw/Simplifying AI Integrations with Model Context Protocol | Brij Kishore Pandey님이 토픽에 대해 올림.md]]"]
tags: ['#inbox', '#MCP', '#AI-Agent', '#System-Architecture']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# Model Context Protocol(MCP)을 통한 AI 도구 통합 간소화

## 1. 개요 및 배경 문제
* **N×M 아키텍처 문제**: AI 애플리케이션에 다양한 LLM 모델을 도입하고, 이에 대응하는 데이터베이스, GitHub, Slack, 사내 API 등 외부 시스템을 연동할 때, 개별 모델과 도구마다 맞춤형 커넥터(Glue Code)를 작성해야 하는 복잡성(N개의 모델 × M개의 도구)이 발생합니다.
* **해결책**: Anthropic이 제안한 **Model Context Protocol(MCP)**은 AI 애플리케이션(Host)과 외부 도구/데이터(Server) 사이의 개방형 표준 인터페이스를 정의하여 통합 복잡도를 O(1) 수준으로 슬림화합니다.

## 2. MCP의 3대 핵심 구성 요소 (Primitives)
MCP 사양은 크게 3가지 데이터 제공 방식을 규정합니다:
1. **Tools (도구)**: LLM이 특정 행동을 취하기 위해 직접 호출할 수 있는 실행 가능한 액션 (예: 데이터베이스 쓰기, API 호출).
2. **Resources (자원)**: LLM이 컨텍스트로 읽을 수 있는 파일, 데이터베이스 조회 결과 등의 정적/동적 데이터.
3. **Prompts (프롬프트)**: 사용자 흐름을 돕기 위해 미리 정의된 템플릿화된 워크플로우.

## 3. 프로덕션 아키텍처 도입 시 고려사항
MCP가 단순한 통합 어댑터를 표준화해주지만, 운영 관점에서는 다음과 같은 실질적인 과제들을 관리해야 합니다:
* **토큰 오버헤드**: 도구 스케마가 너무 커지면 프롬프트에 주입되는 토큰 사용량이 증가하여 비용과 효율성에 영향을 줍니다.
* **인증 및 인가 (Authentication/Authorization)**: 다수의 분산된 MCP 서버들에 대한 OAuth 인증 정보 관리 및 자원/액션 수준의 세밀한 권한 제어가 필요합니다.
* **스키마 드리프트 (Schema Drift)**: 호스트 애플리케이션과 원격 MCP 서버 간의 스키마 버전 불일치를 해소하기 위한 버전 제어.
* **관찰 가능성 (Observability)**: 모델 호출, MCP 도구 연동, 원격 API 게이트웨이 호출 등의 전체 트레이스를 로깅하고 모니터링해야 합니다.

## 4. 연동 프로토콜 설계
* **통신 프로토콜**: 로컬 환경에서는 `stdio` 방식을 사용하며, 원격 혹은 분산 환경에서는 `Streamable HTTP` 기반의 JSON-RPC 2.0 메시지를 교환합니다.
