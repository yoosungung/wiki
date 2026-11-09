---
id: gateway-bun-native-compile
title: "sw-factory gateway: bun --compile 네이티브 패키징"
status: canonical
owner: km
updated: "2026-11-10"
last_updated: "2026-11-10"
review_after: "2027-02-10"
sources:
  - inbox/sw-factory/2026-11-09-gateway-bun-native-compile.md
  - inbox/pm/2026-11-09-gateway-js-native-compile-intake.md
  - inbox/pm/2026-11-09-pm-checkpoint-gateway-native-compile-done.md
  - inbox/pm/2026-11-09-pm-checkpoint-gateway-compile-quiet.md
  - ticket:f2d0043d-a29b-4714-a9c6-4d6765bc502b
  - https://github.com/yoosungung/sw-factory/pull/41
  - https://bun.com/docs/compiler/executables
tags: ["Engineering", "DevOps", "sw-factory", "Bun", "Gateway"]
type: wiki
---

# sw-factory gateway: bun --compile 네이티브 패키징

`agent/gateway`는 `bun build --compile`로 단일 실행 파일을 배포한다 (`npm run agent:gateway:build` → `agent/gateway/dist/sw-factory-gateway`).

## 계약

- 런타임 Node 불필요(바이너리에 Bun runtime 포함). `yaml`·`node:*` 번들 OK; 네이티브 애드온 없음.
- 타깃: 호스트 기본 + `GATEWAY_COMPILE_TARGET`(예: `bun-linux-x64` / `bun-linux-arm64`). Docker는 `TARGETPLATFORM`로 선택.
- Docker/LaunchAgent는 **native-first** 경로. Non-goals: Rust rewrite 없음, `agent/cursor`는 Node 유지.
- 검증: `npm run test:agent` (native-binary smoke 포함). squash merge PR #41 → `7c8fcdb`. tenant_cd/qa/aa/prod N/A.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Factory-Gateway-Tick-Dispatched-Fields.md]]
- [[wiki/Engineering/AI-Native-Engineering/Persona-Bundle-When-Agents-Yaml-Missing.md]]
