---
id: inbox-aa-1511-aa-security-pass-sglang-16k
agent: aa
ticket_id: 1511
updated: 2026-08-31
status: inbox
sources:
  - ticket:1511
  - https://github.com/yoosungung/nl2sql/pull/143
---

# #1511 aa security pass (sglang 16k context gate)

- Deploy candidate: merge_sha `43a4ef65` · tip `ghcr.io/yoosungung/nl2sql-backend:test-43a4ef65` · PR #143.
- Diff surface: `NL2SQL_SGLANG_MAX_MODEL_LEN` env + scaled `context_clear_trigger_tokens`; test overlay CM `16384`; no auth/router/admin/Secret schema change.
- Tenant `.factory/quality.yaml` has no `security.command` — gate was manual skim of tip vs merge (stub-forbidden; did not invent SAST).
- LLM endpoint credentials remain K8s Secret (`OPENAI_API_BASE` / `OPENAI_API_KEY=EMPTY`); CM only model + max_model_len.
