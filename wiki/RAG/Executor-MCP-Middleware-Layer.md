---
title: "Executor: 에이전트 간 MCP 도구 통합 관리용 미들웨어 레이어"
related_raw: ["[[raw/Stop configuring the same integrations separately for every AI agent you use! Right now, every coding agent you use manages its own connections independently. Claude Code has its own MCP servers….md]]"]
tags: ['#inbox', '#MCP', '#Executor', '#Agent-Architecture', '#Tool-Governance']
type: "wiki"
status: "published"
last_updated: "2026-08-27"
updated: "2026-08-27"
---

# Executor: 에이전트 간 MCP 도구 통합 관리용 미들웨어 레이어

## 1. 개요 및 해결하려는 문제
* **개별 설정 파편화 (Siloed Configurations)**: 현재 서비스 중인 개별 AI 코딩 에이전트(Claude Code, Cursor, OpenCode, ChatGPT 등)는 각각 독자적으로 외부 연동(Connection) 및 MCP 서버 설정을 관리합니다.
* **설정 오버헤드**: 새로운 에이전트를 도입할 때마다 동일한 인증 자격 증명, 인증 흐름, 권한 정의 프로세스를 처음부터 반복 세팅해야 하는 비효율이 존재합니다.
* **해결책**: **Executor**는 개별 에이전트와 외부 도구/MCP 서비스 사이에 위치하는 통합 제어 미들웨어 레이어입니다. 한 번만 통합 설정을 구성하면 MCP 호환 규격의 모든 에이전트들이 공통 카탈로그로부터 도구를 가져와 사용하도록 통합 관리합니다.

## 2. 주요 기능 및 스펙
* **인티그레이션 타입 지원**: standard MCP 서버뿐만 아니라 OpenAPI 스펙, GraphQL API, Google Discovery 스펙을 통합 카탈로그 모델로 취합합니다.
* **도구 수준 거버넌스 정책 (Per-tool policies)**:
  - **Always allowed**: 모델의 임의 실행 승인.
  - **Gated behind approval**: 모델이 도구를 호출하기 전 사용자의 명시적 승인 단계 강제.
  - **Blocked**: 특정 보안 위협 도구 차단.
* **지연 및 비동기 승인 제어 (Paused Execution)**: 외부 인증 프로세스나 수동 승인이 처리되는 동안 실행 흐름을 일시 정지(Pause)시키고, 승인이 완료되면 안전하게 진행을 재개(Resume)하는 기능 제공.
* **도구 검색 인프라 (`executor tools search`)**: 에이전트가 카탈로그 전체를 대상으로 프롬프트 의도에 맞는 도구를 즉시 탐색하는 의도 기반 검색 인터페이스 지원.
* **배포 모델**: CLI 환경, 데스크톱 네이티브 앱, 호스팅형 Executor Cloud, Docker 컨테이너 및 Cloudflare Workers Edge 인프라 등 다각화된 환경 지원.
* **SDK 구성**: 임베디드 적용을 위해 TypeScript Promise API 및 Effect-native 비동기/부수효과 관리 API 패키지 기본 제공.
