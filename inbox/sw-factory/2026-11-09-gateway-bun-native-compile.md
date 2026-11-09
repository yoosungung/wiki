---
id: inbox-sw-factory-gateway-bun-native-compile
agent: sw-factory
ticket_id: f2d0043d-a29b-4714-a9c6-4d6765bc502b
updated: 2026-11-09
status: inbox
sources:
  - ticket:f2d0043d-a29b-4714-a9c6-4d6765bc502b
  - https://bun.com/docs/compiler/executables
  - https://github.com/yoosungung/sw-factory/pull/41
---

# gateway bun native compile packaging

- `agent/gateway`는 `bun build --compile`로 단일 실행 파일 배포 가능 (`npm run agent:gateway:build` → `agent/gateway/dist/sw-factory-gateway`).
- 런타임 Node 불필요(바이너리에 Bun runtime 포함). `yaml`·`node:*` 번들 OK; 네이티브 애드온 없음.
- 타깃: 호스트 기본 + `GATEWAY_COMPILE_TARGET` (예: `bun-linux-x64` / `bun-linux-arm64`). Docker는 `TARGETPLATFORM`로 선택.
- 배포 범위: gateway 프로세스만 바이너리. cursor/persona seed/ensure-repos는 Node/`tsx` 유지.
- entrypoint·`scripts/macos/run-gateway.sh`는 native bin 우선, 없으면 tsx 폴백.
