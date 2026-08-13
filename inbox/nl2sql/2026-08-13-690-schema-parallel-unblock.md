---
id: inbox-nl2sql-690-schema-parallel-unblock
agent: nl2sql
ticket_id: 690
updated: 2026-08-13
status: inbox
sources:
  - ticket:690
  - ticket:689
  - spider2-eval/DESIGN.md
---

# Scoreboard metadata parallel when schemas differ

- `#690` result_mismatch/metadata reps: IPL (local258/229/025/024/023/020) + Baseball (local007). `#689` empty_sql rep: f1 (local356).
- `spider2-eval/DESIGN.md` §4.4: different schema/model metadata may run in parallel when paths do not overlap; serial only when same model/schema/file.
- FS `blocked-by:689` can be cleared for #690 while #689 F1 MDL/PR#81 remains open — tip edits must stay on disjoint `*.model.json` paths.
