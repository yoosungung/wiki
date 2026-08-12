---
id: inbox-codingland-m31-sanitizer-cloud-optin
agent: codingland
ticket_id: 541
updated: 2026-08-12
status: inbox
sources:
  - ticket:541
  - ticket:542
  - ticket:543
  - https://code.visualstudio.com/api/references/contribution-points
---

# M3.1 Sanitizer tests + cloud Mirror opt-in

- Sanitizer (ARCHITECTURE §4.5): namePatterns=substring, astSensitiveParams=exact key; depth budget counts array steps; `depth >= maxDepth` → `[MAX_DEPTH]` before leaf stringify.
- Cloud Mirror opt-in: `codingland.mirror.cloudOptIn` default false; `resolveMirrorAdapter` selects local Heuristic vs `CloudMirrorAdapter`; JSON `livingSpecSeed` parsed then sanitized before draft (no real HTTP in M3.1).
- #544 friction/`sessionLoad` weight lock remains ROADMAP undecided — experiment snapshot only until product judgment.
