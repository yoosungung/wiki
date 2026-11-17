---
id: inbox-pm-rhwp-batch-marketing-yaml-intent
agent: pm
ticket_id: 01ab108e-cfa8-4732-9633-3c5ba4568870
updated: 2026-11-17
status: inbox
sources:
  - ticket:01ab108e-cfa8-4732-9633-3c5ba4568870
  - https://github.com/yoosungung/rhwp_batch/commit/f121f32
  - wiki/Engineering/AI-Native-Engineering/Tenant-Marketing-Yaml-Persona-Overlay-Pattern.md
---

# rhwp_batch marketing.yaml Intent (public-only sites)

- SoR for mm-topic-radar is `$path/.factory/marketing.yaml` (not `.md`); missing→skip.
- For `rhwp_batch`, prefer **public hosts only** (velog/hada/okky/medium/github/SO/HN). Exclude LinkedIn / blog.naver.com (login·검색품질 + topic-radar no-login).
- Dual path (main direct-push vs feature PR): keep one yaml on `main`; close conflicting PR after aligning SoR.
- Other mm `repo_ids` without yaml remain skip; do not invent sites/keywords in-ticket unless scoped.
