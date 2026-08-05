---
id: inbox-candidate-issue-wiki-title-ko-sync
agent: candidate
ticket_id: 171
updated: 2026-08-05
status: inbox
sources:
  - ticket:171
---

# Issue wiki title sync (title_ko → front matter title)

- Hugo issue pages render the page title from wiki front matter `title`, not from `data/issues/*.yaml` `title_ko`.
- Missing `title` shows as "—" in browser/page chrome even when YAML has `title_ko`.
- Recurrence prevention: `data/cli/main.py issue apply-meta` now syncs `title_ko` (fallback `title`) into wiki front matter `title`.
- New pages via `create_wiki_page` / `issue_radar.create_issue_shell` already set `title`; historical shells may still lack it until apply-meta.
