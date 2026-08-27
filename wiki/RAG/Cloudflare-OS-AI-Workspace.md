---
title: "Cloudflare OS AI Workspace"
tags: ['#inbox', '#RAG', '#Cloudflare']
type: "wiki"
status: "published"
---

# Cloudflare OS AI Workspace

## 핵심 요약
Cloudflare OS는 회사의 문서, 앱, 시스템 컨텍스트를 기반으로 AI 에이전트를 구동하고 개발할 수 있는 Cloudflare Workers 기반의 에이전트 워크스페이스입니다.

## 설계 및 아키텍처 (Design)
- **Durable Objects를 통한 협업**: 실시간 멀티플레이어 협업을 손쉽게 구현할 수 있는 상태 저장(serverless stateful) 프리미티브인 Durable Objects를 기반으로 하여 에이전트가 기본적으로 이를 지원합니다.
- **블루프린트(Blueprints)**: 생성한 앱(Gadget) 전체를 타인에게 노출하는 대신, 사용자가 직접 자신만의 사본을 생성 및 구동할 수 있도록 코드를 복제하는 Blueprint 기능을 제공합니다. 이를 통해 각 사용자는 AI를 활용해 소프트웨어를 스스로 수정할 수 있습니다.
- **샌드박스 보안(Secure by Default)**: 
  - 서버 측 코드는 동적 워커(Dynamic Worker) 환경에서 실행되며 외부 인터넷 접근이 기본적으로 차단됩니다. 특정 외부 자원(Workers Bindings)만 명시적으로 접근 가능합니다.
  - 클라이언트 측 코드는 샌드박스 처리된 iframe 내에서 구동되며, 통신은 `postMessage()`를 통한 Cap'n Web RPC로 제한됩니다.
- **역량 기반 접근 제어 (Capability-based Access Control)**: 모든 서비스(MCP)에 포괄적인 접근 권한을 주는 대신, 사용자가 명시적으로 자원(예: GitHub 저장소 링크)을 에이전트에 "소개(Introduce)"하는 방식의 최소 권한 원칙을 도입했습니다.

## 커맨드 및 배포 방법 (CLI Commands)
```bash
# 로컬 개발용 빠른 실행 (포트: 8787)
pnpm run-local

# 커스텀 개발을 위한 프론트엔드/백엔드 서버 분리 구동
pnpm dev-server
pnpm dev-client
```
- 추후 Cloudflare의 오픈소스 런타임인 `workerd`를 사용하여 자체 서버 배포 방식도 지원될 예정입니다.
