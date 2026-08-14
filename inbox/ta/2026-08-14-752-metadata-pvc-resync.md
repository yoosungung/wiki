---
id: inbox-ta-752-metadata-pvc-resync
agent: ta
ticket_id: 752
updated: 2026-08-14
status: inbox
sources:
  - ticket:752
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md
  - wiki/Engineering/Infrastructure-and-DevOps/RWO-PVC-Recreate-Deploy-Strategy.md
---

# #752 metadata Git PVC resync

- MCP search reads the MCP PVC worktree, not backend HEAD. `git fetch` without checkout leaves MCP at an old SHA while git-http `main` moves.
- RWO: scale backend+mcp to 0, re-clone both PVCs `--branch main` from in-cluster `nl2sql-metadata.git`, then scale 1. Do not retarget MCP image/binary to `test-*`.
- After resync, MCP `/admin/sync` `status=ok` at the same SHA as `refs/heads/main`. Product-repo merge SHA ≠ metadata-git SHA (separate repos).
