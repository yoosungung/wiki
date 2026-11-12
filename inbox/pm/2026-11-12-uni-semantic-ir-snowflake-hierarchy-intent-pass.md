---
id: inbox-pm-uni-semantic-ir-snowflake-hierarchy-intent-pass
agent: pm
ticket_id: 68f4207a-e514-48cb-9243-f5d77c83e652
updated: 2026-11-12
status: inbox
sources:
  - ticket:68f4207a-e514-48cb-9243-f5d77c83e652
  - https://github.com/yoosungung/uni-semantic/pull/11
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
---

# uni-semantic Phase2 IR snowflake·Hierarchy intent:pass

- PR #11 merged `b7d8c2f` — `$defs.snowflake_path` (`minItems`1/`uniqueItems`); omit=direct join, empty array invalid.
- Hierarchy additive optional `description`; levels ≥2 unique; 3-level valid + dup-levels invalid fixtures.
- Docs synced: ARCHITECTURE §3 · `ir/DESIGN.md` · ROADMAP Phase 2 all `[x]`.
- Evidence: `cd ir && npm test` 6/6 on main@`b7d8c2f`. Ticket `68f4207a` → done.
- Parent Phase 2 `9c068a99` ready for closeout (all children done).
