---
id: inbox-pm-ticket779-scoreboard-delta-intake
agent: pm
ticket_id: 779
updated: 2026-08-14
status: inbox
sources:
  - ticket:779
  - ticket:767
  - ticket:768
  - ticket:769
  - ticket:770
  - ticket:775
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
  - spider2-eval/DESIGN.md
---

# Scoreboard delta Full EX intake (#779)

- On-request Full EX after improve merge PR #94 (#769) · #95 (#768) · #96 (#770). Tip `0d1e442`. Also #775 PG 4Gi live (conn-closed flake mitigation).
- Baseline #767 `scoreboard-agent-20260814T045642Z` pass_rate **0.2222** (30/135). Standalone NF ticket — do not reopen #767 or set `dependingTicketId` to a Done scoreboard parent.
- Command: `cd spider2-eval && uv run spider2-opik scoreboard` (DESIGN §4.4). Detach + `nf-progress:` (wiki §7.3). Not weekly `opik.command`.
- Outcome: experiment id · pass_rate · delta vs 0.2222 · fail clusters · JSON attach · improve New ≤5 metadata-first. Residual PG conn-closed ≠ MDL miss.
- tenant_cd / Deploying Test / prod Done N/A — NF measurement only. Live metadata PVC SHA ≠ product git SHA.
