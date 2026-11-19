---
id: inbox-aura-memory-consolidate-promotion
agent: aura
ticket_id: b060ba50-142f-4cb2-9b5e-01d02c092de3
updated: 2026-11-19
status: inbox
sources:
  - ticket:b060ba50-142f-4cb2-9b5e-01d02c092de3
  - repo:aura/deploy/docs/memory-consolidate-promotion.md
---

# Aura M4 memory consolidate type promotion

- Only `aura.tasks.memory.consolidate` may change `memory_type`; store/embed/recall do not promote.
- Allowed edges: `short_term→episodic`, `episodic→long_term`, `episodic→semantic`. No skip/reverse.
- `similarity_only` / missing reason rejected; `recurrence` needs `evidence_count ≥ 3`.
- LIST partition: `soft_close` + `insert_promoted` (`supersedes_id`); never in-place `UPDATE memory_type`.
- Gate: `bash deploy/scripts/check-memory-consolidate.sh`.
