---
id: aura-m4-memory-consolidate-promotion
title: "Aura M4: memory.consolidate type promotion"
status: canonical
owner: km
updated: "2026-11-19"
last_updated: "2026-11-19"
review_after: "2027-02-19"
sources:
  - inbox/aura/2026-11-19-memory-consolidate-promotion.md
  - ticket:b060ba50-142f-4cb2-9b5e-01d02c092de3
  - repo:aura/deploy/docs/memory-consolidate-promotion.md
tags: ["Engineering", "Aura", "Memory", "Consolidate", "MQT"]
type: wiki
---

# Aura M4: memory.consolidate type promotion

Ops summary only — L0 계약은 aura `ARCHITECTURE` §5 · `deploy/docs/memory-consolidate-promotion.md`.

## Rule

- **Only** `aura.tasks.memory.consolidate` may change `memory_type`. store / embed / recall do **not** promote.
- Allowed edges: `short_term→episodic`, `episodic→long_term`, `episodic→semantic`. No skip, no reverse.
- Reject `similarity_only` and missing reason. `recurrence` requires `evidence_count ≥ 3`.
- LIST partition: `soft_close` + `insert_promoted` (`supersedes_id`); never in-place `UPDATE memory_type`.

## Gate

`bash deploy/scripts/check-memory-consolidate.sh` (promote + handler selftest + MQT gate).

## Related

- [[wiki/Engineering/AI-Native-Engineering/Aura-M1-Memory-Pg-Pooler-Rls.md|Aura M1 memory partitions]]
- [[wiki/Engineering/AI-Native-Engineering/Aura-M2-Memory-Recall-Embed-Inject.md|Aura M2 recall/embed/inject]]
