---
id: inbox-pm-ticket109-mermaid-label-review
agent: pm
ticket_id: 109
updated: 2026-08-04
status: inbox
sources:
  - ticket:109
  - https://github.com/yoosungung/wiki/commit/b313dd70bb69bcf1c11a19f341a80178e9e82fee
  - https://github.com/yoosungung/wiki/actions/runs/30880317992
  - https://github.com/mermaid-js/mermaid/issues/6099
---

# #109 wiki Mermaid `N.` label / Unsupported markdown

- Quartz+Mermaid11: flowchart node text starting with `N.` is parsed as markdown ordered list → `Unsupported markdown: list` (nodes look empty aside from edges).
- Fix pattern: quote labels `Node["1. …"]` (not bare `Node[1. …]`). km applied on org-wiki main `b313dd7` (+ merge `26f07c4`) with `tests/test_mermaid_node_labels.py`.
- Deploy is GitHub Pages/Quartz Actions — not tenant_cd; no TA Deploying Test handoff. PR N/A under km main-direct-push policy.
- Cache: Pages/CDN `max-age=600`; Eric “still broken” reports shortly after deploy may be stale cache — hard refresh before reopening CSS/contrast scope.
