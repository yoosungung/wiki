---
id: inbox-codingland-m0-extension-layout
agent: codingland
ticket_id: 242
updated: 2026-08-06
status: inbox
sources:
  - ticket:242
  - ARCHITECTURE.md
  - ROADMAP.md
---

# Codingland M0 extension layout

- `extension/core` is vscode-free (Jest-only); `extension/host` is the VS Code adapter (Foam-style pure-core split).
- M0 ships GraphDelta apply, AST fingerprint stub (sha256 of structural fields), and ARCHITECTURE §5 protocol envelope parse — not microworld/Replay/Gate.
- Host stubs: Sidebar WebviewView, Custom Editor canvas (`*.codingland.json`) with Time Bar + Hot Reboot placeholders, OutputChannel panel, `codingland.revealBeside` → `ViewColumn.Beside`.
- Dev commands live under `extension/`: `npm test` (core ~1s), `npm run compile`.
