---
id: inbox-ta-unitutor-pages-dns-list-403-soft-skip
agent: ta
ticket_id: 25217dd4-521b-452e-ba9f-e4766b3898af
updated: 2026-10-02
status: inbox
sources:
  - ticket:25217dd4-521b-452e-ba9f-e4766b3898af
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37014137924
  - https://github.com/yoosungung/UniTutorAI/pull/22
---

# UniTutor Pages DNS list 403 soft-skip

- CLOUDFLARE_API_TOKEN can Zone Read + Pages attach but **DNS records list returns 403** (no Zone DNS Read/Edit).
- Ensure hard-fail blocked Smoke even when Pages domain `unitutor.askwho.net` status=active and public DNS/HTTP 200.
- Fix: `dns-list-soft-skip` on 403 → continue to Smoke; Dashboard owns CNAME until token gains DNS Edit.
