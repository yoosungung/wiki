---
id: inbox-pm-2026-08-27-ticket-1371-scoreboard-intake
agent: pm
ticket_id: 1371
updated: 2026-08-27
status: inbox
sources:
  - ticket:1371
  - ticket:1317
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #1371 scoreboard NF intake (3rd delta Full EX)

- **Wave:** Eric on-request · post-#1317 improve bundle · baseline `scoreboard-agent-20260826T012835Z` pass_rate **0.4889** (66/135).
- **Tip gate:** tenant sync `origin/main` ≥ `d0fce04` (#1324 PR #130 merge).
- **Owner:** qa — detach `spider2-opik scoreboard` + `nf-progress:` (DESIGN §4.4 · wiki §7.3).
- **Predecessor Done:** #1318 archived · #1319–#1327 improve (incl. #1320 PR #128 · #1324 PR #130).
- **Non-goals:** weekly `opik.command` · prod deploy · new improve on this ticket · #1317 Outcome rewrite.
- **Outcome:** experiment id · pass_rate · delta vs 0.4889 · fail clusters (max 5 improve spin) · report JSON with `instance_id`.
