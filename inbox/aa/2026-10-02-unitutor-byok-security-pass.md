---
id: inbox-aa-unitutor-byok-security-pass
agent: aa
ticket_id: 5845c0fd-e3e9-4427-b41d-dca12f9de7b5
updated: 2026-10-02
status: inbox
sources:
  - ticket:5845c0fd-e3e9-4427-b41d-dca12f9de7b5
  - https://github.com/yoosungung/UniTutorAI/pull/16
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# UniTutor BYOK security pass (browser custody)

- Product lock: browser-only + request one-shot header `X-UniTutor-Byok-Key`; no server DB/KV persist.
- UniTutorAI has no `.factory/quality.yaml` `security.command` → mechanical SAST skipped; AA did tip↔merge secret/transport scope review + unit evidence.
- Pass criteria checked: localStorage custody, header not body, no echo in SSE/errors, CORS allowHeaders, BYOK preferred over env key.
- Residual: XSS can still steal localStorage keys (inherent to browser custody).
