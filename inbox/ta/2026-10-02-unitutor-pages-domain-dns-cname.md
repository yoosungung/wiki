---
id: inbox-ta-unitutor-pages-domain-dns-cname
agent: ta
ticket_id: 25217dd4-521b-452e-ba9f-e4766b3898af
updated: 2026-10-02
status: inbox
sources:
  - ticket:25217dd4-521b-452e-ba9f-e4766b3898af
  - https://github.com/yoosungung/UniTutorAI/pull/20
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
---

# UniTutor Pages: attach ≠ public DNS — ensure zone CNAME

- Pages Domains API attach can succeed while `dig tutor.askwho.net` is empty and edge returns 530 (1016).
- CI Ensure must also create proxied CNAME `tutor.askwho.net` → `unitutor.pages.dev` on zone `askwho.net` (`deploy/pages_domain_dns.py`).
- Token needs Zone DNS Edit; 403 → Dashboard Custom domains + DNS.
