---
id: inbox-sw-factory-github-issue-check-skip-2026-08-14
agent: sw-factory
ticket_id: 823
updated: 2026-08-14
status: inbox
sources:
  - ticket:823
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - https://github.com/yoosungung/sw-factory/issues
  - https://github.com/yoosungung/nl2sql/issues
  - https://github.com/yoosungung/codingland/issues
  - https://github.com/berryking404/candidate.win/issues
---

# github-issue-check 2026-08-14 explicit skip (open=0)

- `github-issue-check` scanned client repos; `gh issue list --state open` = 0 on sw-factory / nl2sql / candidate.win / codingland.
- No new Leantime convert tickets. Audit ticket #823 (Done, project_id=5) records explicit skip — not a failure.
- Closed historical issues (nl2sql #12–#16, candidate.win #6–#10) were not reopened for QA.
- Registry `clients-repos-registry.json` still absent; client map reused from #731/#575. MCP sees project_id=5 only.
- Blockers: none. PRs excluded (all open PR counts 0).
