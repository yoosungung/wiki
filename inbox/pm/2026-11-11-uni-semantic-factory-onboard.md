---
id: inbox-pm-uni-semantic-factory-onboard
agent: pm
ticket_id: 4ae933b7-93a5-40d3-8564-9a33dcf31dab
updated: 2026-11-11
status: inbox
sources:
  - ticket:4ae933b7-93a5-40d3-8564-9a33dcf31dab
  - https://github.com/yoosungung/uni-semantic
---

# uni-semantic factory onboarding

- Factory project `120b0eb1-39cd-40cb-a70c-5a16aecbb61a` (client `5441b7df-…`) + sessions user `uni-semantic@example.com` → `8fd7fb70-…`.
- Client membership is **owner-only**; without it project member add returns `not_client_member`.
- Persona overlay optional: missing `deploy/personas/{name}` → `_default` only (same as aura/crewrp).
- **Ops host:** gateway+cursor LaunchAgents run on **macmini-server**; agents.yaml refresh/restart there (no remote SSH alias needed when agent already runs on that host).
- PM roadmap: `pm.roadmaps` + `roadmap-registry.json` / `github-issues-registry.json` for `uni-semantic`.
