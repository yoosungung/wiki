---
id: inbox-pm-nl2sql-1514-linux-only-ack
agent: pm
ticket_id: 1514
updated: 2026-09-01
status: inbox
sources:
  - ticket:1514
  - https://github.com/yoosungung/nl2sql/actions/runs/33456955202
  - https://github.com/yoosungung/nl2sql/commit/a698a18ce2f8c869cf8367ffa80da57a95d6f301
---

# #1514 Eric linux-only release decision

- AC narrowed: `nl2sql-mcp-linux-amd64` + README sync; macos-arm64 not required this cut.
- Stuck run 33381902133 cancelled; `include_macos` default false @ `a698a18`.
- Redispatch in flight — TA owns evidence (release URL + linux checksum).
