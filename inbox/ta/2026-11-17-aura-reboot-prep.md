---
id: inbox-ta-aura-reboot-prep
agent: ta
ticket_id: e9e09bfd-dac0-415e-8416-0247d7c75ef2
updated: 2026-11-17
status: inbox
sources:
  - ticket:e9e09bfd-dac0-415e-8416-0247d7c75ef2
  - https://github.com/yoosungung/aura
---

# aura reboot prep (orbstack)

- ta kubeconfig contexts = `orbstack` only; `aura` NS already NotFound (delete no-op).
- `yoosungung/aura` main force-rewrote to docs-only reboot tip `94ba62a` (Agent/MCP Serverless Runtime); local seed had no merge-base → hard reset to origin/main.
- tip has no `deploy/k8s/ghcr` / `deploy/SETUP.md`; re-apply N/A until M0 manifests. Old `aura-secrets` + ghcr overlay path retired at tip.
