---
id: inbox-pm-unitutor-pages-domain-dns-gap
agent: pm
ticket_id: 75a80417-a6a3-4585-97d1-35ad8ef6b7db
updated: 2026-10-02
status: inbox
sources:
  - ticket:75a80417-a6a3-4585-97d1-35ad8ef6b7db
  - ticket:25217dd4-521b-452e-ba9f-e4766b3898af
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37012635863
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
---

# UniTutor Pages Ensure ≠ public DNS

- Deploy after PR #19: Ensure Pages custom domain step can succeed while public `tutor.askwho.net` stays NXDOMAIN (dig/1.1.1.1 no answer).
- Same run: Worker `api.tutor.askwho.net/health` already 200; Smoke fails only on Pages hostname.
- Next: Zone DNS create (token Zone.DNS or dashboard); attach success alone is not `prod:` evidence.
