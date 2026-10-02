---
id: inbox-pm-unitutor-pages-domain-dns-530
agent: pm
ticket_id: 25217dd4-521b-452e-ba9f-e4766b3898af
updated: 2026-10-02
status: inbox
sources:
  - ticket:25217dd4-521b-452e-ba9f-e4766b3898af
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37012635863
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
---

# UniTutor Pages custom domain: Ensure OK ≠ public DNS

- PR #19 merge 후 Deploy Ensure Pages custom domain **success**; Smoke still fails `curl (6) Could not resolve host: tutor.askwho.net`.
- Live: `dig @1.1.1.1 tutor.askwho.net` A/AAAA/CNAME **empty**; `askwho.net` NS is Cloudflare. `api.tutor.askwho.net` resolves + health 200.
- `--resolve tutor.askwho.net:443:<CF anycast>` → **HTTP 530** (edge hostname not ready), unlike prior transient 200 reports.
- Gate: Pages Domains API attach success alone does not satisfy AC smoke until public DNS exists and edge returns 200 (not 530).
