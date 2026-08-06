---
id: inbox-aa-gh-issue-sync-skip-2026-08-06
agent: aa
ticket_id: 286
updated: 2026-08-06
status: inbox
sources:
  - ticket:286
  - clients-repos-registry
---

# GH issue → Leantime sync skip (2026-08-06, aa)

- 전 client open GitHub issue 0건 → 티켓 변환 없음(explicit skip). ticket #286 (nl2sql project, QA 재현용 배치).
- 점검: nl2sql, sw-factory, codingland, candidate.win (`gh issue list --state open`).
- lookback ≥2026-08-04 created issue도 0. blocker 없음.
- Cursor Leantime MCP discovery error → JSON-RPC 직접 호출로 create_ticket/add_comment.
