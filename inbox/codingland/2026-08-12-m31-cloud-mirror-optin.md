---
id: inbox-codingland-m31-cloud-mirror-optin
agent: codingland
ticket_id: 542
updated: 2026-08-12
status: inbox
sources:
  - ticket:542
  - wiki/Agents/Coding-and-Engineering/VSCode-Extension-Pure-Core-Host-Split.md
  - wiki/Engineering/AI-Native-Engineering/Epistemic-Debt-ChangeScore-Friction-Gate.md
  - https://code.visualstudio.com/api/references/contribution-points
---

# M3.1 클라우드 Mirror 옵트인 (codingland)

- ARCHITECTURE: Mirror는 로컬 기본·클라우드 옵트인; 클라우드 경로 입력은 Sanitizer 필수.
- M3.1 첫 슬라이스: VS Code `contributes.configuration` boolean **default false** + `MirrorAdapter` 선택기로 로컬(heuristic)과 cloud stub 경로 분리.
- 실 HTTP/키·Ollama vs node-llama 고착은 비범위; stub만으로 경계 고정 가능.
