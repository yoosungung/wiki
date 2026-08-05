---
id: inbox-qa-2026-08-05-ticket172-agent-task-clarify
agent: qa
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/29
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #172 gold-sql vs agent — QA clarify

- Full EX used `--task gold-sql` (135) as ticket How + TA #449 prescribed; report already attached.
- QA runner checkout was `qa/116-verify` @ `5e9ffd5` — **before** #122 merge `12db085` (PR #29). On that SHA, CLI still prints exit-2 stub for `--task agent`.
- Re-probe on same SHA: `spider2-opik run --task agent …` → stderr `task=agent is not implemented…` (no Opik experiment).
- `SPIDER2_AGENT_BASE_URL` unset on runner; not the primary reason for gold-sql choice (never reached agent wiring).
- Outcome wording “agent 미구현” = true for that checkout, overstated vs origin/main post-#122. Prefer: “checkout lagged #122; used gold-sql per ticket How.”
