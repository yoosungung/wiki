---
id: inbox-qa-ticket779-scoreboard-delta-intake
agent: qa
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
  - spider2-eval/DESIGN.md
---

# Scoreboard delta Full EX request (#779)

- New on-request Full EX after improve bundle merge: PR #94 (#769) · #95 (#768) · #96 (#770). Tip `0d1e442`. Also #775 PG 4Gi live (conn-closed flake mitigation).
- Baseline is **#767** experiment `scoreboard-agent-20260814T045642Z` pass_rate **0.2222** (30/135). Do not reopen #767 or `dependingTicketId` it (Done parent).
- Command: `cd spider2-eval && uv run spider2-opik scoreboard` (DESIGN §4.4). Not weekly `opik.command`. Detach + `nf-progress:`.
- NF measurement only — tenant_cd / Deploying Test / prod Done N/A.
- Live metadata PVC SHA ≠ product git SHA; scoreboard measures tip live chat SSE.
