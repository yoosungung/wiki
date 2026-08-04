---
id: inbox-candidate-publication-gate-push-403
agent: candidate
ticket_id: 0
updated: 2026-08-04
status: inbox
sources:
  - ticket:publication-safety-2026-08-04
  - skill:political-wiki-administration
---

# candidate.win publication gate + push 403

- 03:00 KST publication-safety: run `agent/.venv/bin/python agent/publication_gate.py --base origin/main` before any push; exit 2 / PUBLICATION HOLD = hold.
- 2026-08-04: gate PASS (exit 0) on ahead commit `1c6b5a5` (12 people stub→curated); no issue-page zero-stance blockers.
- Push still blocked: GitHub 403 — token identity `yoosungung` lacks write on `berryking404/candidate.win`. Local commit remains ahead of origin/main until write-capable credentials are used.
- Report Leantime project 7 as user 9 (candidate) with Done/Blocked + commit hash + push/hold outcome.
