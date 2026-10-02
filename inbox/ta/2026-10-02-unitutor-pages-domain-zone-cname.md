---
id: inbox-ta-unitutor-pages-domain-zone-cname
agent: ta
ticket_id: 75a80417-a6a3-4585-97d1-35ad8ef6b7db
updated: 2026-10-02
status: inbox
sources:
  - ticket:75a80417-a6a3-4585-97d1-35ad8ef6b7db
  - ticket:25217dd4-521b-452e-ba9f-e4766b3898af
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37012635863
  - https://github.com/yoosungung/UniTutorAI/pull/20
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
---

# UniTutor Pages attach ≠ zone DNS CNAME

- Deploy Ensure Pages custom domain can return HTTP 200 with `status=initializing` / `verification=pending` while public `tutor.askwho.net` stays NXDOMAIN and `--resolve` hits edge 530.
- Same-account attach does not always create zone DNS; Worker `api.tutor.askwho.net` custom_domain can resolve while Pages hostname does not.
- Fix pattern: after attach, Zone DNS API idempotent proxied CNAME `tutor.askwho.net` → `unitutor.pages.dev` (`deploy/pages_domain_dns.py`). Token needs Zone DNS Edit; else Dashboard.
