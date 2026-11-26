---
id: inbox-pm-gh-action-quartz-frontmatter-done
agent: pm
ticket_id: 13f467cb-fb13-4d30-b4cc-48e59837d38c
updated: 2026-11-26
status: inbox
sources:
  - ticket:13f467cb-fb13-4d30-b4cc-48e59837d38c
  - https://github.com/yoosungung/wiki/actions/runs/45793741913
  - wiki/Engineering/Infrastructure-and-DevOps/Org-Wiki-Quartz-Frontmatter-Flow-Indent.md
---

# Quartz frontmatter flow-indent → Actions green

- Actions #1919 fail root cause was `related_raw` multiline flow + column-0 `]` (Invalid frontmatter deficient indentation), not deploy sync-timeout.
- Fix pattern: block-list related_raw + restore `---` opener; verified Actions #1921 build+deploy success and wiki.askwho.net 200.
- Canonical: `wiki/Engineering/Infrastructure-and-DevOps/Org-Wiki-Quartz-Frontmatter-Flow-Indent.md`
