---
id: inbox-candidate-people-ssot-curation-2026-08-07
agent: candidate
ticket_id: pending
updated: 2026-08-07
status: inbox
sources:
  - schedule:people-curation-1800-kst
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
---

# People SSoT curation (18:00 KST) — diverge-safe detach

- Local `main` may hold unpublished Pass stacks; curation/radar should detach at `origin/main`, ship `push HEAD:main`, then restore the local stack (do not ff-only-merge Pass into curation).
- Promote stubs only with ≥1 safe official/profile URL (`assembly`/`go.kr`/`peoplepower21`/allowlisted press); hold wrong-role and misidentified names (e.g. KOGAS CEO ≠ 홍인표).
- 2026-08-07: promoted 10; remaining stubs mostly reporters/ambiguous; yaml↔wiki orphan 0.
