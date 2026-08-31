---
id: inbox-ta-2026-08-31-nl2sql-publish-releases-macos-runner
agent: ta
ticket_id: 1514
updated: 2026-08-31
status: inbox
sources:
  - ticket:1514
  - https://github.com/yoosungung/nl2sql/actions/runs/33381902133
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# nl2sql publish-releases needs online [self-hosted, macOS]

- `publish-releases.yml` `build-mcp-macos` requires labels `[self-hosted, macOS]`; Linux ARC alone cannot publish `nl2sql-mcp-macos-arm64`.
- Repo runners snapshot during #1514: only Linux/X64 ARC online; macOS job stays `queued` with empty `runner_name`.
- Linux ARC `meta` job often spends ~12m on "Complete job" after a 1s script — expect long wall time before verify/publish.
- Prior #1514-era cancel (run 33360555929) waited ~2.5h on macos then cancelled — same gap.
