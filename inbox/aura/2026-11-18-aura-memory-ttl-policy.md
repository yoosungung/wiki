---
id: inbox-aura-memory-ttl-policy
agent: aura
ticket_id: 06ca1e75-d8b6-4977-aa63-30dc13abe3e8
updated: 2026-11-18
status: inbox
sources:
  - ticket:06ca1e75-d8b6-4977-aa63-30dc13abe3e8
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
---

# Aura M1 memory TTL 수치 고정

- short_term 핫 **14일** · episodic **24개월** · audit **12개월** (ARCHITECTURE §6.2.2 → `deploy/docs/memory-ttl-policy.md`)
- DROP 판정: 파티션 상한 `U <= now() - interval '…'`; Soft-delete-only 방치 금지
- DROP 주기: **일 1회**(UTC); 담당 태스크 이름 `aura.tasks.memory.ttl` (구현·스케줄 CR은 M4)
- 정적 게이트: `bash deploy/scripts/check-memory-ttl.sh`
