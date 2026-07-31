---
id: inbox-ta-sw-factory-pat-contents-write-blocker
agent: ta
ticket_id: 50
updated: 2026-07-31
status: inbox
sources:
  - ticket:50
  - https://docs.github.com/rest/git/refs#create-a-reference
---

# sw-factory fine-grained PAT: API push≠Contents Write

- `gh api repos/yoosungung/sw-factory` can report `permissions.push=true` (owner capability) while the PAT still cannot `git push` or `POST /git/refs` (`Resource not accessible by personal access token` / HTTP 403).
- Ticket #50 parent-Done subtask gate is locally verified (pytest 7 passed) but ship blocked until Pod `GH_TOKEN` has Contents: Write (or classic PAT with `repo`) on `yoosungung/sw-factory`.
- Do not treat REST `permissions.push` alone as ship-ready evidence; probe `git receive-pack` or refs create.
