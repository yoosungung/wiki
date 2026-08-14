---
id: inbox-pm-ticket767-scoreboard-delta-intake
agent: pm
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
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
  - spider2-eval/DESIGN.md
---

# Scoreboard delta Full EX intake (#767)

- On-request Full EX after improve merge PR #91 (#752) · #92 (#753) · #93 (#754). Tip `d1abfa3`. Baseline #751 `scoreboard-agent-20260814T004125Z` pass_rate **0.2222** (30/135).
- Standalone NF ticket — do not reopen #751 or set `dependingTicketId` to a Done scoreboard parent (Parent-Done / FS-vs-parent).
- Command: `cd spider2-eval && uv run spider2-opik scoreboard` (DESIGN §4.4). Detach + `nf-progress:` (wiki §7.3). Not weekly `opik.command`.
- Outcome: experiment id · pass_rate · delta vs 0.2222 · fail clusters · JSON attach · improve New ≤5 metadata-first.
- tenant_cd / Deploying Test / prod Done N/A — NF measurement only. Live metadata PVC SHA ≠ product git SHA.
