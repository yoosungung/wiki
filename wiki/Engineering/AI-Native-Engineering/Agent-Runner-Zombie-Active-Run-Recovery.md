---
id: agent-runner-zombie-active-run-recovery
title: "Agent-runner: zombie active_run 복구 (R1–R5)"
status: canonical
owner: km
updated: "2026-08-06"
last_updated: "2026-08-06"
review_after: "2026-11-06"
sources:
  - ticket:197
  - ticket:199
  - ticket:200
  - https://cursor.com/docs/sdk/typescript
tags: ["Engineering", "AI-Native", "Agent-Runner", "SDK", "Recovery"]
type: "wiki"
---

# Agent-runner: zombie active_run 복구 (R1–R5)

SDK 워커 프로세스가 죽은 뒤에도 `POST /sessions/{id}/prompt`가 영구 **409 `skipped_active_run`** / `session.prompt.skipped reason=active_run`을 반환할 수 있다. soft budget·pre-lease recycle·멘션만으로는 SDK busy가 안 풀린다.

## 원인 분리

- 부모 `busyAgents`는 promise reject 시 클리어될 수 있으나, Cursor local agent에 **미종료 run**이 남으면 `Agent.resume`+`send`가 “already has active run”.
- HTTP 방언은 유지: **202 accepted / 409 skipped_active_run**. 복구는 parent/pool 내부 + `session.recover` 로그.
- **정상 mutex**: Pod Ready이고 `run.started`가 살아 있는데 `session.prompt.skipped reason=active_run`만 보이면 **zombie이 아님** — `session.recover`/재시작을 중복하지 말고 assignee가 현재 run을 마치게 둔다. zombie는 crash 후 skip만 누적·`run.background.failed` 패턴일 때.

## Recovery 요지 (DESIGN)

| ID | 요지 |
| :--- | :--- |
| R1–R2 | crash/`active_run` 실패 시 ticket↔agent 맵 forget |
| R3 | 연속 skip 임계(기본 **2**) → `run.cancel`/`Agent.cancelRun` 또는 핸들 없으면 **DELETE session + forget** |
| R4–R5 | 새 세션 생성·재시도; 관측 가능 로그 |

검증: `AGENT_RUNNER_MOCK=1 npm test` + `session-recover` 단위 테스트. 구 이미지의 live zombie Pod는 롤아웃 전까지 수동 recycle이 필요할 수 있다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Sessionless-MCP-Status-Label-Cache-Poison.md]]
- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
