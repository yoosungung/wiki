---
id: inbox-nl2sql-ticket391-stream-timeout-fix
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-11-ticket391-test-7d78ec7-ac3-fail.md
  - https://github.com/sgl-project/sglang/issues/4097
---

# #391 tip test-7d78ec7 — stream timeout + infinity JSON

- SoT: StreamChunkTimeoutError (25s idle) + SGLang BadRequest `number is infinity when parsed as double` → empty SSE sql / pass_rate 0.
- Fix: `DEFAULT_STREAM_CHUNK_TIMEOUT_S=60` (`NL2SQL_STREAM_CHUNK_TIMEOUT_S`) under Spider2 ~120s client; `sanitize_json_numbers` on execute LLM preview; `_to_sse` emits stashed `warehouse_sql` before `error` on stream abort.
- Verify: `backend/.venv/bin/python -m pytest tests/test_stream_timeout_guard.py …` (related suite 68 passed).
