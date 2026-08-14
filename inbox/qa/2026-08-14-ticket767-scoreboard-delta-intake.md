---
id: inbox-qa-ticket767-scoreboard-delta-intake
agent: qa
ticket_id: 767
updated: 2026-08-14
status: inbox
sources:
  - ticket:767
  - ticket:751
  - ticket:752
  - ticket:753
  - ticket:754
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md
  - spider2-eval/DESIGN.md
---

# Scoreboard delta Full EX request (#767)

- New on-request Full EX after improve bundle merge: PR #91 (#752) · #92 (#753) · #93 (#754). Tip `d1abfa3`.
- Baseline is **#751** experiment `scoreboard-agent-20260814T004125Z` pass_rate **0.2222** (30/135). Do not reopen #751 or `dependingTicketId` it (Done parent).
- Command: `cd spider2-eval && uv run spider2-opik scoreboard` (DESIGN §4.4). Not weekly `opik.command`. Detach + `nf-progress:`.
- NF measurement only — tenant_cd / Deploying Test / prod Done N/A.
- Live metadata PVC SHA ≠ product git SHA; scoreboard measures tip live chat SSE.
