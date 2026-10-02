---
id: inbox-ta-unitutor-pages-domain-attach-idempotent
agent: ta
ticket_id: 25217dd4-521b-452e-ba9f-e4766b3898af
updated: 2026-10-02
status: inbox
sources:
  - ticket:25217dd4-521b-452e-ba9f-e4766b3898af
  - ticket:75a80417-a6a3-4585-97d1-35ad8ef6b7db
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37012154863
  - https://github.com/yoosungung/UniTutorAI/pull/19
---

# UniTutor Pages domain Ensure: JSON list + POST already-exists

- Compact `grep -F '"name":"host"'` misses pretty `"name": "host"` → false miss → re-POST.
- After Dashboard/prior attach, Cloudflare Pages Domains POST often returns **400**; treat already/exist/duplicate as success so Smoke can run.
- Helper: UniTutorAI `deploy/pages_domain_attached.py` (check + attach-ok).
- Domain may already serve Pages (`dig @1.1.1.1` + `--resolve` → 200) while stub resolvers still fail NXDOMAIN.
