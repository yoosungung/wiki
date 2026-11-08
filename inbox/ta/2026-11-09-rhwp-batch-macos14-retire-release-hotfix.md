---
id: inbox-ta-rhwp-batch-macos14-retire-release-hotfix
agent: ta
ticket_id: 0f34dece-193b-4a93-bca5-6c8d408fb620
updated: 2026-11-09
status: inbox
sources:
  - ticket:0f34dece-193b-4a93-bca5-6c8d408fb620
  - https://github.blog/changelog/2026-10-01-github-actions-macos-14-runner-image-retirement/
  - https://github.com/actions/runner-images/issues/13518
  - https://github.com/yoosungung/rhwp_batch/pull/7
  - https://github.com/yoosungung/rhwp_batch/actions/runs/42529172553
---

# rhwp_batch Release: macos-14 retirement hotfix

- GitHub Actions retired `macos-14` on **2026-11-02**; jobs fail immediately with `macos-14-arm64-us-default is not supported`.
- Fix: pin mac matrix to `macos-15`; add `workflow_dispatch` + `tag` input so existing annotated tags (e.g. `v0.9.0`) can re-release without force-retag.
- Evidence: PR #7 merged `9e10cc9`; dispatch run 42529172553 → success (linux+mac+publish+docker); GH Release `v0.9.0` assets present.
