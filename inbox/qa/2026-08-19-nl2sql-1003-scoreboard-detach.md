---
id: inbox-qa-nl2sql-1003-scoreboard-detach
agent: qa
ticket_id: 1003
updated: 2026-08-19
status: inbox
sources:
  - ticket:1003
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# nl2sql #1003 Full EX scoreboard detach notes

- tenant-repo-sync `nl2sql` tip `c07d9c1` (≥ `ba6d00e`); scoreboard CLI lives in tip `spider2-eval` (primary Pod checkout may lag).
- Live tip chat SSE `meta_ref` (metadata PVC) ≠ product git SHA — e.g. `be91e999…` vs sync `c07d9c1`.
- Shared PG PVC `data-postgresql-0` observed **8Gi** (ticket #775 asked 4Gi confirm; capacity OK).
- On-request Full EX: `cd spider2-eval && uv run spider2-opik scoreboard` with `SPIDER2_AGENT_BASE_URL=http://nl2sql-backend.nl2sql.svc.cluster.local:8080` + AUTH_* + Opik cluster FQDN; detach + log tqdm as heartbeat when `nf-progress.json` stays `done=0` until evaluate ends.
- Symlink ephemeral `.tmp-spider2` from a populated tree (wiki §4.3) before `check`/scoreboard.
