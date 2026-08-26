---
id: inbox-pm-1317-scoreboard-intake
agent: pm
ticket_id: 1317
updated: 2026-08-26
status: inbox
sources:
  - ticket:1317
  - ticket:1266
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #1317 — post-improve delta scoreboard intake

- #1317은 #1266과 동일 headline이지만 **두 번째 on-request Full EX** — #1266 Done(0.4296) 이후 improve wave(#1267–#1272, #1280) merge 뒤 재측정.
- baseline은 #1003(0.3407)이 아니라 **#1266 pass_rate 0.4296** (exp `scoreboard-agent-20260825T035955Z`).
- tip gate: origin/main ≥ `88c12f0` (PR #122 #1280 merge); 채점 축은 tip live chat SSE(metadata PVC), checkout SHA와 불일치 가능(wiki §7.3).
- NF executor: **qa** (detach + `nf-progress:`); tenant_cd N/A.
