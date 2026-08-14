---
id: inbox-qa-ticket779-scoreboard-delta
agent: qa
ticket_id: 779
updated: 2026-08-14
status: inbox
sources:
  - ticket:779
  - ticket:767
  - ticket:775
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - spider2-eval/DESIGN.md
---

# Scoreboard delta Full EX (#779)

- After #768/#769/#770 merge + #775 PG 4Gi, Full EX pass_rate **0.2519** (34/135), delta **+4** vs #767 0.2222. Not weekly canary.
- Wins: local018/017/015, local259, local228, local008 now PASS. PG conn-closed **12→0**.
- Residual: IPL local021 still mismatch; modern_data local065 PASS→mismatch.
- CLI `scoreboard-*.json` still omits `instance_id`; rebuild from Opik `experiment.get_items()`.
- Live metadata PVC SHA ≠ product git SHA; scoreboard measures tip live chat SSE.
