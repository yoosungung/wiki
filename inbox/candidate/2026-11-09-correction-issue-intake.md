---
id: inbox-candidate-correction-issue-intake
agent: candidate
ticket_id: 85b94ff9-1aa1-4616-8df6-3c87eef2c01a
updated: 2026-11-09
status: inbox
sources:
  - ticket:85b94ff9-1aa1-4616-8df6-3c87eef2c01a
  - https://github.com/berryking404/candidate.win/pull/21
---

# candidate.win 정정·삭제 → GitHub Issue 사전채움

- 모달 `submitReport()` stub(“점검 중”)은 Issue를 만들지 않음 → `wiki/static/js/report-issue-url.js`로 `issues/new?template=correction.yml|takedown.yml` 오픈.
- 쿼리 키 = Issue form 필드 `id` (`page-url`, `target-slug`, `target-kind`, correction:`incorrect`/`sources`, takedown:`reason`/`scope`/`legal-basis`).
- people/issues URL path에서 slug·kind 파생 (`/people/{slug}/` → person, `/issues/{slug}/` → issue).
