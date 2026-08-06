---
id: inbox-candidate-people-ssot-curation-2026-08-06
agent: candidate
ticket_id: null
updated: 2026-08-06
status: inbox
sources:
  - https://github.com/berryking404/candidate.win/commit/67490c69a09e5af6d666b1d16131b833a232067f
---

# People SSoT curation 18:00 KST — diverged main workaround

- When local `main` has unpublished Pass D commits ahead of `origin/main`, people curation can detach at `origin/main`, curate, push `HEAD:main`, then `git checkout main` to preserve the Pass D stack.
- Do not ff-only-pull over dirty leftover `agent/cron/` WIP that already landed via PR; restore/remove duplicates first.
- 2026-08-06 outcome: promoted 5 stubs → curated; remaining stub 18; push `67490c6`.
