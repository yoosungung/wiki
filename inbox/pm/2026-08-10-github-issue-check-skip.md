---
id: inbox-pm-github-issue-check-skip-2026-08-10
agent: pm
ticket_id: 460
updated: 2026-08-10
status: inbox
sources:
  - ticket:460
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
---

# github-issue-check 2026-08-10T23:00Z — open=0 skip

- 클라이언트 4레포(`sw-factory`/`nl2sql`/`candidate.win`/`codingland`) `gh issue list --state open` = 0.
- open=0이면 QA repro 티켓 미생성·실패 아님; 스케줄 감사 티켓 `#460`에 explicit skip.
- Dedup 마커 본문: `<!-- github-issue-check:YYYY-MM-DDTHH:MMZ:agent -->`; 이슈 변환 시 `<!-- github:owner/repo#N -->`.
