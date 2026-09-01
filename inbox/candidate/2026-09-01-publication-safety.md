---
id: inbox-candidate-2026-09-01-publication-safety
agent: candidate
ticket_id: 1564
updated: 2026-09-01
status: inbox
sources:
  - ticket:1564
  - schedule:publication-safety-03:00-KST
  - repo:berryking404/candidate.win@9e5f30d
---

# Publication-safety review 03:00 KST — 2026-09-01

- Gate `publication_gate.py --base origin/main` exit 0 before/after hygiene; push allowed only after content review.
- Hygiene pattern (same as 2026-08-31): remap SSoT slug aliases, delink non-SSoT/org person links, drop weak misattribution stance lines; do not invent people stubs at publication time unless slug shells already exist.
- Pass stack can leave broken romanization (`lee-jaemyung`, `yonghyein`, `oh-geoho`) and `/people/unknown`; publication gate must normalize against `data/people` before ship.
- Hugo may be absent in runner; note skip rather than failing the gate when content checks pass.
