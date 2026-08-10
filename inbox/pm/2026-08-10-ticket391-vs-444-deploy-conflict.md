---
id: inbox-pm-ticket391-vs-444-deploy-conflict
agent: pm
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - ticket:444
  - https://github.com/yoosungung/nl2sql/pull/50
  - https://github.com/yoosungung/nl2sql/pull/51
---

# #391 vs #444 deploy/dev conflict check

- Git: `f9622ab` (#444 PR#51) = Merge(`902ccf2` #391 PR#50, b22d40f). #391 commits are ancestors — no lost #391 code.
- Live: image `prod-f9622ab` READY; annotations still `nl2sql.io/image-tag=test-902ccf2` / `merge-sha=902ccf2` (stale vs image).
- Approach: #444 changes describe path (no Enum in describe_table; on-demand tools) and raises `DESCRIBE_JSON_CHARS_MAX` back to 12k vs #391's 2500 — supersedes trim strategy, keeps SEARCH_K≤2 / SEARCH_JSON 1500 / SSE stash.
- Board conflict: #444 Done/prod while #391 still Deploying Test waiting AC3 on obsolete `test-902ccf2`.
- Next: retarget #391 AC3 to `f9622ab` tip (live or test-f9622ab); do not validate only on pre-#444 tag.
