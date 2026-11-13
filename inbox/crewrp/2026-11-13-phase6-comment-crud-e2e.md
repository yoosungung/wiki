---
id: inbox-crewrp-phase6-comment-crud-e2e
agent: crewrp
ticket_id: 7ce664ec-722f-4020-8398-688e7a2a4b4c
updated: 2026-11-13
status: inbox
sources:
  - ticket:7ce664ec-722f-4020-8398-688e7a2a4b4c
  - ticket:161a162c-80f3-4e66-b27f-19df53852a25
  - wiki/Engineering/Development-Environment/CrewRP-Phase6-Todo-Board-Comments.md
---

# CrewRP Phase 6 comment CRUD E2E (live clients)

- E2E repo: `yoosungung/crewrp-e2e-sandbox` (Discussions on; `ai-edu` NOT_FOUND for this token).
- Coverage: `CrudE2ETests.taskIssueCommentRoundTrip` + `discussionCommentRoundTrip` (iOS); Android twins. Same clients as app task/board detail.
- Host token scopes used: `repo` (+ oauth `read:org`); `project` not required for comment paths.
- ROADMAP Phase 6 remaining `- [ ]` closed in PR; prior Done tickets left doc lag until checkbox + evidence.
