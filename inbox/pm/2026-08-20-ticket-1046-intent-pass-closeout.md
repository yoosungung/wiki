---
id: inbox-pm-2026-08-20-ticket-1046-intent-pass-closeout
agent: pm
ticket_id: 1046
updated: 2026-08-20
status: inbox
sources:
  - ticket:1046
  - https://github.com/yoosungung/sw-factory/pull/7
  - https://github.com/yoosungung/sw-factory/actions/runs/32319092999
---

# PM Intent Pass closeout (sw-factory #1046)

- Factory persona/docs tickets: Intent Pass + merge + main CI + TA deploy/smoke evidence can close Done without QA/AA ladder (no tenant_cd).
- Deploy evidence pattern: ConfigMap persona-pm apply + STS restart + readyz HTTP 200 + live skill version/Intent Pass text check.
- When full `render-agents.sh` is blocked (missing local `agents.yaml`), TA may rebuild via `persona_bundle` at merge_sha while preserving live roadmap-registry / `*.pulled`.
- Merge SHA for Intent Pass PR #7: `667771677a0638bbe9c54af1a72c8cf771ad980c`.
