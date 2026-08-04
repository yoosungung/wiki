---
id: inbox-pm-ticket122-merge-conflict-hold
agent: pm
ticket_id: 122
updated: 2026-08-04
status: inbox
sources:
  - ticket:122
  - ticket:121
  - https://github.com/yoosungung/nl2sql/pull/29
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #122 PR merge HOLD after #121 soft-dep

- Soft-dep order: merge #121/PR#28 first, then update #122/PR#29 onto main.
- Mechanical conflicts after #28: `ROADMAP.md` + `spider2-eval/DESIGN.md` only — keep both #121 weekly gold-sql line and #122 agent wiring done line; leave #123 open.
- Conflict resolve commit on PR#29: `45a8bf3` (merge main into feature/122-agent-chat-sse).
- Local gate: `cd spider2-eval && uv run pytest -q` → 13 passed.
- Merge still blocked on required CI (mcp-duckdb ~30m baseline on this repo); do not merge while UNSTABLE.
