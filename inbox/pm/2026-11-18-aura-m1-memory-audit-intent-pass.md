---
id: inbox-pm-aura-m1-memory-audit-intent-pass
agent: pm
ticket_id: 2a04d47b-6e53-4df2-a8bb-c3d63924828d
updated: 2026-11-18
status: inbox
sources:
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - ticket:85741c7b-9713-44b3-91c5-2a2fc6a5bc24
  - https://github.com/yoosungung/aura/pull/15
---

# aura M1 memory_audit Intent pass → short_term TTL policy

- memory_audit monthly RANGE + FORCE RLS; smoke PASS
- PR #15 MERGED `77f3c745`; child `85741c7b` done
- Next: short_term TTL policy doc `06ca1e75`
