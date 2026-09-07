---
id: inbox-pm-codingland-1751-ci-restore
agent: pm
ticket_id: 1751
updated: 2026-09-07
status: inbox
sources:
  - ticket:1751
  - https://github.com/yoosungung/codingland/pull/16
  - https://github.com/yoosungung/codingland/pull/15
---

# codingland #1751 follow-up — restore extension ci script

- #15 conflict resolve dropped `extension/package.json` `ci` while quality.yaml/DESIGN still invoke it → AA clean_code broken.
- PR#16 restores `"ci": "npm test && npm run test:vscode"`; tenant_cd N/A; Done after merge.
