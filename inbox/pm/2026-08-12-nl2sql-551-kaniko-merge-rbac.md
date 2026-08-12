---
id: inbox-pm-nl2sql-551-kaniko-merge-rbac
agent: pm
ticket_id: 551
updated: 2026-08-12
status: inbox
sources:
  - ticket:551
  - https://github.com/yoosungung/nl2sql/pull/63
---

# nl2sql #551 Kaniko tip path merged; live Job needs RBAC

- PR #63 squash-merged @ `52d0b76` — in-cluster Kaniko Jobs + `build-tip-images-kaniko.sh` are primary Test tip → GHCR; `build-ghcr-images` stays workflow_dispatch fallback.
- Live smoke blocked: SA `system:serviceaccount:sw-factory:cursor-agent-ta` Forbidden on `batch/jobs` create in `nl2sql`; dry-run only until admin grants Job create or operator runs Job + Secret `nl2sql-ghcr-build`.
- After RBAC: TA can tip-build without Actions hosted-runner minutes — unblocks #391 tip path that was stuck on empty-step runner flake.
