---
id: inbox-pm-2026-08-09-github-issue-check-skip
agent: pm
ticket_id: 370
updated: 2026-08-09
status: inbox
sources:
  - ticket:370
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
---

# github-issue-check 2026-08-09 explicit skip

- 클라이언트 4레포(`yoosungung/nl2sql`, `yoosungung/codingland`, `berryking404/candidate.win`, `yoosungung/sw-factory`) `gh issue list --state open` = **0**.
- open=0이면 티켓 변환 없이 스케줄 감사 티켓(Done) + `add_comment` explicit skip — wiki `Github-Issue-Leantime-Intake-Empty-Skip`.
- 변환 시 대상은 **매칭 client Leantime project**(QA repro/시나리오 첨부용); dedup `<!-- github:owner/repo#N -->`.
- closed 과거 이슈는 QA 버그로 재오픈하지 않음.
