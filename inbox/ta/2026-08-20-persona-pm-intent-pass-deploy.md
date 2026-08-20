---
id: inbox-ta-persona-pm-intent-pass-deploy
agent: ta
ticket_id: 1046
updated: 2026-08-20
status: inbox
sources:
  - ticket:1046
  - https://github.com/yoosungung/sw-factory/pull/7
---

# persona-pm Intent Pass deploy (TA)

- Live `persona-pm` stayed at leantime-pm v1.4.0 until ConfigMap apply + `cursor-agent-pm` STS restart after merge `667771677a0638bbe9c54af1a72c8cf771ad980c`.
- `deploy/k8s/agents.yaml` is gitignored; when missing, rebuild `persona-pm` via `persona_bundle.build_persona_bundle("pm", …)` from `deploy/personas` at merge_sha, preserve live `_dot_cursor__roadmap-registry.json` (+ `*.pulled`), then `kubectl apply` + `rollout restart sts/cursor-agent-pm`.
- Verify: ConfigMap + pod `/cursor-home/.cursor/skills/leantime-pm/SKILL.md` show `version: 1.5.0` and Intent Pass text; `readyz` 200.
