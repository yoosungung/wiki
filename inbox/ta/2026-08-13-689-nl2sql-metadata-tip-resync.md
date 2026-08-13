---
id: inbox-ta-689-nl2sql-metadata-tip-resync
agent: ta
ticket_id: 689
updated: 2026-08-13
status: inbox
sources:
  - ticket:689
  - wiki/Engineering/Infrastructure-and-DevOps/Git-HTTP-Basic-Auth-Username-Env.md
  - inbox/nl2sql/2026-08-13-f1-overtake-catalog-tip-gap.md
---

# nl2sql-metadata tip PVC desync (not empty bare / not auth)

- `push_failed` `src refspec 'refs/heads/main' does not match any existing object` was tip-side: backend PVC had HEAD=`master` and **no** `refs/heads/main` while `METADATA_GIT_BRANCH=main`.
- git-http bare `nl2sql-metadata.git` already had `main`@`6ea134a` with full catalog (incl. `f1` ×52); `git`/`gitpassword` receive-pack 200.
- MCP tip PVC had `main` but sparse working tree (baseball+ipl only) at divergent SHA.
- Fix: scale backend+mcp 0 → re-clone both PVCs from `origin/main` → scale 1; push smoke (noop + throwaway branch) OK.
- k8s-test README recovery: "nl2sql metadata tip desync".
