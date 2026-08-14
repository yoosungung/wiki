---
id: inbox-qa-ticket751-scoreboard-delta
agent: qa
ticket_id: 751
updated: 2026-08-14
status: inbox
sources:
  - ticket:751
  - ticket:688
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - spider2-eval/DESIGN.md
---

# Scoreboard delta Full EX (#751)

- On-request `spider2-opik scoreboard` (DESIGN §4.4) is **not** weekly canary; detach + `nf-progress:`.
- #688 baseline pass_rate **0.0296** (4/135). After #689–#691 (+#697/#698/#699/#702) merge, #751 **0.2222** (30/135), +26.
- Weekly smoke `local008`/`local022` **regressed** to result_mismatch (SQL emitted, EX fail). `local356` empty_sql cluster now **passes**.
- CLI `scoreboard-*.json` may omit `instance_id`; rebuild from Opik `experiment.get_items()` (enriched JSON).
- Fail clusters this run: result_mismatch/metadata n=67 · empty_sql/metadata n=24 · sql_exec_failed/metadata n=14. Improve: #752/#753/#754.
- Live metadata PVC SHA ≠ product git SHA; scoreboard measures **tip live** chat SSE, not runner checkout.
