---
id: inbox-aura-agent-checkpoints
agent: aura
ticket_id: 24e94cd4-15ee-41dd-9313-5ef26ef706b3
parent_id: 6a457aa6-1c75-4e0f-ace3-f6cb01baa104
updated: 2026-11-19
status: inbox
sources:
  - ticket:24e94cd4-15ee-41dd-9313-5ef26ef706b3
  - https://github.com/yoosungung/aura
---

# `agent_checkpoints` 예외 테이블 DDL (Aura M3)

- 테이블명 확정: `agent_checkpoints` — Zero Direct Write **유일 예외**; 쓰기=`agent_invoke` only · Pooler + `set_config('app.tenant_id', $1, true)`.
- FORCE RLS · UNIQUE `(tenant_id, run_id, seq)` · `kind` turn/tool/final · `state` JSONB(시크릿 금지) · 대형/PII→`content_ref` (256KB+).
- Non-goals: live INSERT/resume · TTL GC · checkpoint MQT.
- 게이트: `deploy/scripts/check-agent-checkpoints.sh` PASS.