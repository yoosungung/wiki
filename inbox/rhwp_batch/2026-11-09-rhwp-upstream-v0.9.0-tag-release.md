---
id: inbox-rhwp_batch-rhwp-upstream-v0.9.0-tag-release
agent: rhwp_batch
ticket_id: 0f34dece-193b-4a93-bca5-6c8d408fb620
updated: 2026-11-09
status: inbox
sources:
  - ticket:0f34dece-193b-4a93-bca5-6c8d408fb620
  - https://github.com/yoosungung/rhwp_batch/pull/6
  - https://api.github.com/repos/yoosungung/rhwp_batch/actions/runs/42525829659
---

# rhwp_batch v0.9.0 tag after PR #6 merge

- After PM intent:pass + squash merge of PR #6 onto main (`394534c`), push annotated tag `v0.9.0` (force 금지) to trigger `.github/workflows/release.yml`.
- Tag object points at merge commit; do not retag moved SHA.
- Prefer lean PR (#6: fonts/font-rules only) over fat vendor (#5 chrome/edge assets) for nest sync.
