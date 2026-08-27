---
title: "Coexecutor Secure Integration Layer"
tags: ['#inbox', '#RAG', '#Integration', '#MCP']
type: "wiki"
status: "published"
---

# Coexecutor Secure Integration Layer

## 핵심 요약
Executor는 AI 에이전트가 OpenAPI, MCP, GraphQL, 커스텀 JS 함수 등을 안전한 환경에서 호출할 수 있도록 연결해 주는 통합 레이어(Integration Layer)입니다.

## 주요 기능 및 구조
- **안전한 실행 환경**: 내장형 백그라운드 서비스(Daemon)를 통해 실행되며 에이전트가 직접 인증 정보를 다루지 않고 API를 호출할 수 있도록 설계되었습니다.
- **다양한 배포 환경 지원**: CLI 서버 환경, 데스크톱 앱(Mac, Windows, Linux), Docker 기반 자체 호스팅, Cloudflare Worker 배포, 그리고 Executor Cloud 등 다양한 형태로 구동 가능합니다.
- **MCP 지원**: `add-mcp` 패키지를 통해 Claude Code, Cursor 등의 MCP 호환 클라이언트에 손쉽게 연동할 수 있습니다.

## CLI 명령어 (CLI Commands)
```bash
# 설치 및 백그라운드 서비스 구동
npm install -g executor
executor install

# 웹 UI 실행
executor web

# MCP 엔드포인트 연결 추가 (HTTP 방식)
npx add-mcp http://127.0.0.1:4788/mcp --transport http --name executor

# OpenAPI 통합 추가 예시
executor call executor openapi addIntegration '{
  "spec": "https://petstore3.swagger.io/api/v3/openapi.json",
  "namespace": "petstore",
  "baseUrl": "https://petstore3.swagger.io/api/v3"
}'
```

## API 스펙 (TypeScript SDK)
```typescript
import { createExecutor } from "@executor-js/sdk/promise";
import { openApiPlugin } from "@executor-js/plugin-openapi/promise";

const executor = await createExecutor({ plugins: [openApiPlugin()] });
const tools = await executor.tools.list({ integration: "inventory" });
const schema = await executor.tools.schema(tools[0].address);
await executor.close();
```
