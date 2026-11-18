---
id: inbox-pm-aura-m2-orphan-gc-intent-m2-done
agent: pm
ticket_id: 1d669034-018b-45e0-986f-c50b24cfd735
updated: 2026-11-19
status: inbox
sources:
  - ticket:1d669034-018b-45e0-986f-c50b24cfd735
  - ticket:bb165a71-08a2-49af-828e-c5197688827e
  - https://github.com/yoosungung/aura/pull/31
---

# Aura M2 closeout — orphan content_ref GC Intent

- V2.2 고아 GC는 **설계 고정만** M2: grace 90일(`AURA_EVENTS`) · `refs/` only · live PG ref → SKIP · batch 100/day · task `aura.tasks.memory.object_gc` · 멱등 `object-gc:{tenant|all}:{yyyy-mm-dd}`; 본구현=M4.
- 정본 doc: `deploy/docs/object-store-orphan-gc.md` + gate `check-object-store-orphan-gc.sh`; PR#31 merge `530f1838`.
- M2 milestone `1d669034` children 7/7 done → milestone done; 다음 일상 sync는 pass-gate → M3.
