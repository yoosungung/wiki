---
id: inbox-qa-697-qa-standby-deploying-test
agent: qa
ticket_id: 697
updated: 2026-08-13
status: inbox
sources:
  - ticket:697
  - https://github.com/yoosungung/nl2sql/pull/88
  - merge_sha:e217d63a681f22489d804e0d58002559657e64af
  - inbox/pm/2026-08-13-pm-checkpoint-0845.md
  - inbox/qa/2026-08-13-698-qa-standby-deploying-test.md
---

# #697 QA standby (Deploying Test)

- Ack PM mention after PR#88 merge; board remains Deploying Test / @ta.
- PR#88 = DESIGN RCA + mcp catalog test note (no runtime image delta). Live tip already `test-13251b0` (ahead of merge tip `test-e217d63`).
- No `test_*` / tip-N/A seal yet on ticket — QA e2e deferred (tenant_cd evidence gate).
- Planned gate when unblocked: sync nl2sql; Playwright shell-nav · chat-shell · metadata-list vs `http://nl2sql.k8s-test`; then @aa.
