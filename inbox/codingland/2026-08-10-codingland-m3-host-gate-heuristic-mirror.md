---
id: inbox-codingland-m3-host-gate-heuristic-mirror
agent: codingland
ticket_id: 458
updated: 2026-08-10
status: inbox
sources:
  - ticket:458
  - https://docs.ollama.com/integrations/vscode
  - https://github.com/yoosungung/codingland/pull/4
---

# codingland M3 host Gate + Heuristic Mirror

- Host Gate hook default = command `codingland.triggerGate` (SCM vs husky still undecided).
- MirrorAdapter interface + HeuristicMirrorAdapter default; Ollama/node-llama runtime still ROADMAP undecided — no hard pick.
- `runGateSmoke` covers none/light/full (+ sessionLoad downshift) without VS Code electron.
