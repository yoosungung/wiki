---
id: inbox-qa-ticket292-spider2-full-ex-detach
agent: qa
ticket_id: 292
updated: 2026-08-07
status: inbox
sources:
  - ticket:292
  - ticket:262
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md
  - spider2-eval/DESIGN.md
---

# Spider2 local* Full EX detach (#292)

- After #262 40k smoke Done, Full EX (~135 local* agent) is a separate ticket (#292); pass_rate remains soft/report-only.
- Live prerequisite: `sglang-gemma4-12b` `--context-length 40960` + fp8; preflight `spider2-opik check` OK before detach.
- Long-run: `nohup spider2-opik run --task agent --experiment-name ticket292-local-full-agent-ex-…` (no `--instance-ids` = full dataset) + `{SPIDER2_TMP_DIR}/nf-progress.json` / `nf-progress:` Leantime heartbeats (ARCHITECTURE §2.6 #10).
- Experiment started 2026-08-07: `ticket292-local-full-agent-ex-20260807-005059` · log `/tmp/ticket292-full-ex-20260807-005059.log` · pid tracked in ticket comments.
