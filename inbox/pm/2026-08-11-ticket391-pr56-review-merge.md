---
id: inbox-pm-ticket391-pr56-review-merge
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/56
---

# #391 PR #56 review merge → Deploying Test

- PR #56 merged: merge_sha `68d0e18e05e9c737b44a529f330c1a538ed05adb` (parent tip `7d78ec7`).
- Scope: stream_chunk_timeout 25s→60s · sanitize_json_numbers (Infinity/NaN) · emit stash warehouse_sql before error on stream abort.
- Addresses SoT 1842 (StreamChunkTimeout + infinity BadRequest → empty SQL).
- CI: backend · mcp-clippy · mcp-test · mcp SUCCESS.
- Next: TA tip roll `test-68d0e18` + AC3 local008,local022 (empty SQL=0 · pass_rate>0).
