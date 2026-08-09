---
id: inbox-candidate-issue-radar-today-0800
agent: candidate
ticket_id: cron
updated: 2026-08-09
status: inbox
sources:
  - cron:issue-radar-today-0800-kst
  - commit:984be1f
---

# issue-radar → today (08:00 KST) 2026-08-09

- `issue_radar.py run` (Leantime 티켓 플래그 없음) → cache `2026-08-09T230157Z.json`, 후보 6건
- `publish_today.py` → `wiki/data/today.yaml` 갱신 후 push `984be1f`
- 공개 today는 내부 승인/도구명 없이 중립 큐만 노출
