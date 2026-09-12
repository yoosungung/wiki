---
id: inbox-candidate-2026-09-12-people-ssot-curation-18h
agent: candidate
ticket_id: 1920
updated: 2026-09-12
status: inbox
sources:
  - ticket:1920
  - schedule:people-ssot-curation-18h
  - repo:berryking404/candidate.win@fb1e0f8
---

# People SSoT curation 18:00 KST (2026-09-12)

- Outcome: Done · 0 promotions · stubs 33 remaining (shortage vs preferred ~30)
- Worktree: clean on origin/main @ `fb1e0f8`; no commit/push (no content diff)
- Orphan pre-pass: people yaml↔wiki orphan 0; parse_err 0; curated 1062 / stub 33 / yaml 1095
- Hold pattern unchanged: role/identity mismatches (bak-jae-cheol, hong-in-pyo, go-hui-jin, i-jeong-min), non-person title stubs (heo-chong-jang/bae-jae-go/no-dong-bu/jeong-bu), reporters/citizens without allowlisted official/profile URL
- Validation: pytest `test_people_curation_sources.py` 3 passed; `publication_gate.py --base origin/main` PASS
