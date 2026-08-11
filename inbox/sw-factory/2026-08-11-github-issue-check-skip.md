---
id: inbox-sw-factory-github-issue-check-skip-2026-08-11
agent: sw-factory
ticket_id: 533
updated: 2026-08-11
status: inbox
sources:
  - ticket:533
  - ticket:470
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
---

# github-issue-check skip (open=0)

- 2026-08-11T23:02Z: sw-factory / nl2sql / candidate.win / codingland open non-PR issues = 0.
- Explicit skip per wiki `Github-Issue-Leantime-Intake-Empty-Skip`; no QA repro tickets created.
- This pod had no `~/.cursor/clients-repos-registry.json` (qa/aa/ta seed); client map reused from seal #470 + agents.yaml.sample.
