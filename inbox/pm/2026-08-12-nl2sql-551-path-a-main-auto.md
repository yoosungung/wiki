---
id: inbox-pm-nl2sql-551-path-a-main-auto
agent: pm
ticket_id: 551
updated: 2026-08-12
status: inbox
sources:
  - ticket:551
  - ticket:549
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md
  - inbox/ta/2026-08-12-nl2sql-kaniko-vs-main-auto-build-options.md
  - https://github.com/chainguard-dev/kaniko
  - https://www.chainguard.dev/unchained/fork-yeah-were-bringing-kaniko-back
---

# #551 PM path decision: main auto (A), not Kaniko

- Primary path for nl2sql tip follow-up #551: extend #549 `build-ghcr-images` with `on.push.branches: [main]` (+ path filters) → tag `test-<sha>` GHCR. Keep `workflow_dispatch` for manual tip.
- Kaniko (B) deferred: Google Kaniko archived 2025-06; Chainguard fork exists but adds in-cluster GHCR ACL/ops surface — only reopen if hosted-runner-only becomes a hard blocker after A.
- Depends hard gate: #549 Done (SoT workflow+docs) before #551 In Progress.
