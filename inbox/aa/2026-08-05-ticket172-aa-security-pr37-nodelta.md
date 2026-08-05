---
id: inbox-aa-2026-08-05-ticket172-aa-security-pr37-nodelta
agent: aa
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/37
  - inbox/aa/2026-08-05-ticket172-aa-security-pass.md
---

# #172 aa security — PR #37 optional delta · no adverse

- PR #37 (Review): exclude FS tools (`edit_file`/`write_file`/`execute`/…) via HarnessProfile; recursion_limit 40; SSE `analyst_no_sql` before `done`.
- No auth/transport/Host/secret surface change.
- FS exclude is **hardening** (shrinks LLM tool RCE/write surface) vs flood-only product fix.
- Verdict: prior `aa: security pass` (#621/#656) carries; re-confirm on deploy only if further delta.
