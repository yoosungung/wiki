---
id: inbox-candidate-issue-radar-naver-missing
agent: candidate
ticket_id: 0
updated: 2026-08-04
status: inbox
sources:
  - skill:political-wiki-administration
  - run:issue-radar-2026-08-04T230105Z
---

# candidate.win issue-radar → today blocker (NAVER env)

- 08:00 KST issue-radar job: run `issue_radar.py` without Leantime flags, then `publish_today.py`; commit/push only `wiki/data/today.yaml` when changed.
- 2026-08-04 run: Google News seeds collected (~30), but `NAVER_CLIENT_ID`/`NAVER_CLIENT_SECRET` unset → Naver expand empty → all candidate scores < 4 → cache candidates=[].
- Did not overwrite `wiki/data/today.yaml` with empty items (would wipe public /today/ queue last generated 2026-07-16). No Leantime ticket created. No commit.
- Next: inject Naver Search API credentials into the candidate.win agent pod/env, re-run radar+publish_today, commit only today.yaml; push still needs write-capable GitHub token (see prior push-403 note).
