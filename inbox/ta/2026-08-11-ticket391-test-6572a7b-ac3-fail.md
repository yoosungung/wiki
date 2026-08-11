---
id: inbox-ta-ticket391-test-6572a7b-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/54
  - https://github.com/yoosungung/nl2sql/actions/runs/31453924169
---

# #391 AC3 fail on tip test-6572a7b

- Tip roll OK: `ghcr.io/yoosungung/nl2sql-backend:test-6572a7b` · merge_sha `6572a7bc742b7f47162008583fa859e4b4a0ad3c` (PR #54).
- AC3 experiment `ticket391-agent-smoke-test-6572a7b-20260811-030107` id `019feec4-4a6c-7340-aa8f-a25256c406a6` → pass_rate **0.0**, duration ~8m11s.
- empty-SQL count: **0** (SoT 1792 empty-stop superseded) — both local008/local022 emitted non-empty SQL via EnsureAnalystTaskMiddleware.
- Failures: local008 relation `baseball_player_batting_stats` missing; local022 incomplete SQL (`missing FROM-clause entry for table "b"`).
- Live logs also saw SGLang BadRequest context overflow (~40998 > 40960) / infinity JSON during analyst — keep MDL 40k.
