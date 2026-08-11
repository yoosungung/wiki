---
id: inbox-nl2sql-ticket391-context-gate-fix
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-11-ticket391-test-42fe7f0-ac3-fail.md
  - wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md
  - wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md
---

# #391 tip test-42fe7f0 — hard context gate

- SoT: input alone `59320>40960` and `40009+1024` despite PR #57 budgets/`max_tokens=1024`.
- Fix: `ContextEditingMiddleware`/`ClearToolUsesEdit` on orchestrator+analyst — trigger 32k tokens, keep last 1 tool result, clear older ToolMessage bodies pre-model.
- Verify: pytest context_gate + related 59 passed.
