---
id: inbox-pm-2026-11-09-gateway-js-native-compile-intake
agent: pm
ticket_id: f2d0043d-a29b-4714-a9c6-4d6765bc502b
updated: 2026-11-09
status: inbox
sources:
  - ticket:f2d0043d-a29b-4714-a9c6-4d6765bc502b
  - agent/gateway/DESIGN.md
  - ARCHITECTURE.md§1.11-14
  - deploy/docker/Dockerfile
---

# gateway JS compile → native binary (intake)

- 공장 `sw-factory` 티켓: gateway를 Rust 재작성 없이 JS/TS compile/package로 단일 실행 파일 배포.
- 계약(Worker event-log / gateway 배달 경계) 변경 없음 — 배포 형태·DESIGN Commands·Docker/entrypoint/LaunchAgent만.
- 결합 컨테이너에서 cursor·persona seed CLI는 당분간 Node/`tsx` 유지 가능; AC의 “Node 제거”는 **gateway 프로세스** 기준.
- 증거 게이트: gateway tests green + binary smoke; tenant_cd/qa/aa/prod N/A.
- open: bun vs deno (또는 동등) PoC, darwin-arm64+linux 타깃, Docker에서 gateway만 바이너리 교체 범위.
