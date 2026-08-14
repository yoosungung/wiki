---
id: inbox-qa-ticket789-scoreboard-delta-intake
agent: qa
ticket_id: 789
updated: 2026-08-14
status: inbox
sources:
  - ticket:789
  - ticket:779
  - ticket:781
  - ticket:782
  - ticket:783
  - ticket:784
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
  - spider2-eval/DESIGN.md
---

# Scoreboard delta Full EX request (#789)

- New on-request Full EX after improve bundle merge: PR #97 (#782) · #98 (#783) · #99 (#781). Tip `fb31071`.
- Baseline is **#779** experiment `scoreboard-agent-20260814T064137Z` pass_rate **0.2519** (34/135). Do not reopen #779 or `dependingTicketId` it (Done parent).
- Command: `cd spider2-eval && uv run spider2-opik scoreboard` (DESIGN §4.4). Not weekly `opik.command`. Detach + `nf-progress:`.
- #784 (local073) still In Progress — recommend measure this merged bundle first, then next serialize (DESIGN §4.4 sequencing).
- NF measurement only — tenant_cd / Deploying Test / prod Done N/A.
- Live metadata PVC SHA ≠ product git SHA; scoreboard measures tip live chat SSE.
