---
id: inbox-candidate-ticket176-pass-ab-success
agent: candidate
ticket_id: 176
updated: 2026-08-05
status: inbox
sources:
  - ticket:176
---

# Pass AB success after OPENAI inject

- Eric injected OPENAI_API_KEY; candidate added Tier1 `sglang-gemma4-12b` env (non-secret).
- Relaunch `run_id=20260805T033834Z-10479`: status=done exit_code=0 (03:38:34Z→03:52:04Z).
- Pass A: all 18 ongoing issues completed; Pass B batch `batch_6a72b363ca808190a1c4ad9c58e94c86`.
- exit 99 path fixed earlier (setsid+bash); exit 1 cleared by key inject.
