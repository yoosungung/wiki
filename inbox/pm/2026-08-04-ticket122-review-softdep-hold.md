---
id: inbox-pm-ticket122-review-softdep-hold
agent: pm
ticket_id: 122
updated: 2026-08-04
status: inbox
sources:
  - ticket:122
  - ticket:121
  - https://github.com/yoosungung/nl2sql/pull/29
  - https://github.com/yoosungung/nl2sql/pull/28
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #122 Review: content OK, soft-dep #121 + post-merge doc conflict

- PR #29 wires `--task agent` path A (`POST /api/chat` SSE → last non-empty `sql`); local `uv run pytest -q` → 13 passed; AC content-approved.
- Soft-dep: merge #121 / PR #28 first. After #28, #29 conflicts only in `ROADMAP.md` + `spider2-eval/DESIGN.md` (keep both #121 weekly gate lines and #122 agent wired lines).
- Merge also waits on PR #29 `mcp-duckdb` CI (same long duckdb smoke as #28). tenant_cd N/A — Done after merge without Deploy lanes.
- Canonical wiki §4.1 still says CLI exit 2; after merge, @km should flip to path-A wired (or promote this inbox).
