---
id: inbox-pm-2026-09-14-nf-1986-review-merge
agent: pm
ticket_id: 1986
updated: 2026-09-14
status: inbox
sources:
  - ticket:1986
  - https://github.com/yoosungung/nl2sql/pull/151
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# NF #1986 Review merge → Deploying Test

- intent: pass on PR #151 (local008 seal isolation + saw_sql last-sql guard + sourced SSE extract).
- merge_sha `50e2b81f899274442c6622717a49d542d7519b6d`; CI_SKIP policy → ci-skipped SUCCESS; tip smoke pass_rate=1.0 accepted.
- Post-merge: Deploying Test @ta (backend product change → tenant_cd); Done still needs test+qa+aa+prod.
