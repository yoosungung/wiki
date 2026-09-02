---
id: inbox-candidate-publication-safety-2026-09-02
agent: candidate
ticket_id: null
updated: 2026-09-02
status: inbox
sources:
  - skill:political-wiki-administration
  - agent/publication_gate.py
---

# Publication-safety review (03:00 KST) notes

- Gate script only blocks zero-stance ongoing issues; full review must still catch `/people/unknown`, `/people/tmp`, malformed `**입장**` lines, and missing SSoT slugs.
- Safe nightly fixup pattern: drop unresolvable actor links; remap known slug typos to existing `data/people`; add stubs only for clearly named persons already cited with sources.
- Do not publish municipality/org/article-title actors as `/people/*` without a real person SSoT.
