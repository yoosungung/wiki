---
id: inbox-candidate-2026-09-09-people-ssot-curation-18h
agent: candidate
ticket_id: 1828
updated: 2026-09-09
status: inbox
sources:
  - ticket:1828
  - repo:berryking404/candidate.win@a446be7
---

# People SSoT curation 18:00 KST — 2026-09-09

- Worktree: clean `main` @ `a446be7`; `git pull --ff-only origin main` OK.
- Orphan pre-pass: people yaml↔wiki orphan 0 (`_index` only wiki extra).
- Promoted: 0 (no stub with ≥1 allowlisted official/profile URL + unambiguous same-person/same-role).
- Remaining stubs: 33 (all reviewed; shortage vs preferred ~30 / min 20).
- SSoT: yaml 1095 / curated 1062 / stub 33 / parse_err 0.
- Validation: pytest people curation 3 passed; `publication_gate.py --base origin/main` PASS; no content diff → no commit/push.
- Held (reconfirmed): bak-jae-cheol (≠서울청장), hong-in-pyo (≠가스공사 사장/홍의락), go-hui-jin (role mismatch/volleyball coach), yu-hyeon-a (≠윤현아 거제시의원), gwak-sang-tan (no match), hwang-seong-taek (ambiguous; yna hits 트러스톤 대표), i-sang-hun (no named go.kr staff page), i-yeong-suk (kihasa.re.kr not allowlisted), bae-jae-go/no-dong-bu/jeong-bu/heo-chong-jang (non-person), reporters/citizen/vague stubs.
