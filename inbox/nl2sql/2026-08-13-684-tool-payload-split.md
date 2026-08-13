---
id: inbox-nl2sql-684-tool-payload-split
agent: nl2sql
ticket_id: 684
updated: 2026-08-13
status: inbox
sources:
  - ticket:684
  - ticket:682
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
---

# tool_payload god-module split (#684)

- Split `agent/tool_payload.py` into `execute_sse_stash.py` / `llm_slim.py` / `json_sanitize.py`; `tool_payload` remains thin re-export for stable imports.
- Smell agglomeration (SSE stash + LLM budgets + JSON sanitize) raised change intensity — prefer concern modules over one growing file.
- Behavior unchanged: existing `from …tool_payload import …` paths keep working; boundary covered by `tests/test_tool_payload_module_split.py`.
