---
id: inbox-ta-2026-09-01-nl2sql-1514-releases-token
agent: ta
ticket_id: 1514
updated: 2026-09-01
status: inbox
sources:
  - ticket:1514
  - https://github.com/yoosungung/nl2sql/actions/runs/33456955202
  - https://github.com/yoosungung/nl2sql-releases/releases/tag/v0.1.4
---

# nl2sql RELEASES_REPO_TOKEN git push auth

- `publish-releases` Sync README step: public `nl2sql-releases` clone OK; `git push` failed `Invalid username or token` when `RELEASES_REPO_TOKEN` stale (last set 2026-06-16).
- Fix: refresh `RELEASES_REPO_TOKEN` on `yoosungung/nl2sql` with a PAT that has Contents write on `nl2sql-releases`.
- #1514 cut: TA published `v0.1.4` linux-amd64 + README sync out-of-band after secret refresh; redispatch for green Actions.
