---
id: inbox-aura-memory-capture-mqt
agent: aura
ticket_id: 3a06af28-77ba-44af-853c-fd30e520fefa
updated: 2026-11-19
status: inbox
sources:
  - ticket:3a06af28-77ba-44af-853c-fd30e520fefa
  - https://github.com/yoosungung/aura/pull/25
---

# memory_capture MQT (PG 금지)

- `aura.tasks.memory.capture` → resp `aura.events.memory.candidates` / error `aura.events.memory.capture.error` (consumer `aura_memory_capture`, stream `AURA_TASKS`, minReplicaCount=0).
- Zero Direct Write: handler·Package에 `pg`/`set_config`/`AURA_DATABASE_HOST`/`query` 없음; selftest가 주입 `pgClient`를 무시.
- 정적 게이트: `bash deploy/scripts/check-memory-capture.sh`.
- M2 스켈레톤 extractor는 결정적 휴리스틱; 라이브 LLM Gateway는 Non-goal(M3).
