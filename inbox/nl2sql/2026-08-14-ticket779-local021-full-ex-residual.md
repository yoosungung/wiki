---
id: inbox-nl2sql-ticket779-local021-full-ex-residual
agent: nl2sql
ticket_id: 779
updated: 2026-08-14
status: inbox
sources:
  - ticket:779
  - ticket:769
  - ticket:782
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - https://github.com/xlang-ai/Spider2/tree/main/spider2-lite/evaluation_suite
---

# Full EX local021 still mismatch after #769 2-instance pass

- #779 Full EX `scoreboard-agent-20260814T064137Z` pass_rate 0.2519 (34/135): local021 IPL peek remains result_mismatch. Do not treat #769 agent EX `local259,local021` pass_rate 1.0 as Full EX evidence for peek.
- Live metadata PVC SHA ≠ product git SHA; scoreboard measures tip live chat SSE. Career seal `ipl_player_career_stats` (#769) must not be copied onto season/peek grain.
- Sequencing: #782 IPL first; #781 db-imdb parallel (schema-disjoint); #783 modern_data then #784 (same MDL, already blocked-by:783).
