---
id: inbox-candidate-issue-wiki-title-sync
agent: candidate
ticket_id: 171
updated: 2026-08-05
status: inbox
sources:
  - ticket:171
  - repo:data/cli/main.py
---

# issue apply-meta title_ko → wiki title

- Hugo 이슈 페이지는 front matter `title`이 없으면 브라우저에 "—"로 표시된다.
- `issue apply-meta`가 `status`/`conclusion`만 동기화하고 `title_ko`→`title`을 빠뜨리면 수동/부분 생성 페이지에서 제목 누락이 재발한다.
- 신규 생성 경로(`create_wiki_page`, `create_issue_shell`)는 이미 title을 넣는다. 기존 페이지 보정은 apply-meta가 담당해야 한다.
