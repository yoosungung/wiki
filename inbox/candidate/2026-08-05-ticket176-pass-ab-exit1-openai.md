---
id: inbox-candidate-ticket176-pass-ab-exit1-openai
agent: candidate
ticket_id: 176
updated: 2026-08-05
status: inbox
sources:
  - ticket:176
  - https://github.com/berryking404/candidate.win/pull/12
---

# Pass AB exit 1 after exit-99 fix

- PR #12 merge 후 relaunch: `exit_code=1` (not 99); completion status + PVC log OK.
- Cause: `build_agent` hardcodes `openai:gpt-5.4-mini` but `agent/.env` has only NAVER_* — missing `OPENAI_API_KEY`.
- Pass B batch submit also requires OpenAI; Tier1 SGLang default host `sglang-gemma4-31b` NXDOMAIN (cluster has `sglang-gemma4-12b`).
- Next: inject `OPENAI_API_KEY` into workspace `agent/.env`; optionally align `SGLANG_*` to 12b service.
