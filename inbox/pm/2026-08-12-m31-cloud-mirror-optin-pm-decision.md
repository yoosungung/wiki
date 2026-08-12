---
id: inbox-pm-m31-cloud-mirror-optin-decision
agent: pm
ticket_id: 542
updated: 2026-08-12
status: inbox
sources:
  - ticket:542
  - ticket:541
  - wiki/Agents/Coding-and-Engineering/VSCode-Extension-Pure-Core-Host-Split.md
  - wiki/Engineering/AI-Native-Engineering/Epistemic-Debt-ChangeScore-Friction-Gate.md
  - https://code.visualstudio.com/api/references/contribution-points
---

# M3.1 클라우드 Mirror 옵트인 — PM 결정 (#542)

- AC는 옵트인 경로·기본 off·로컬 분리; 첫 PR은 `CloudMirrorAdapter` stub으로 충분(실 HTTP 비범위).
- Sanitizer·friction 가중치는 형제 #543/#544 — #542에 넣지 않음.
- Setting 키 승인: `codingland.mirror.cloudOptIn` boolean default false (VS Code contributes.configuration 관례).
