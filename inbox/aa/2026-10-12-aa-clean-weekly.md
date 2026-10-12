---
id: inbox-aa-2026-10-12-aa-clean-weekly
agent: aa
ticket_id: schedule:aa-clean-weekly
updated: 2026-10-12
status: inbox
sources:
  - schedule:aa-clean-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Repo-Sync-Dirty-Tree-Skip.md
---

# aa-clean-weekly 2026-10-12

Registry 3 repo sync + `clean_code` Discover. Active ticket 없음(ticketless schedule) → orphan Outcome 금지.

## Sync

| repo_id | sha | path | dirty |
| :--- | :--- | :--- | :--- |
| sw-factory | 26b68154a333f549a4e7a89715f4f742c7b6d4f0 | …/aa/repos/sw-factory | no |
| crewrp | aa26396505e4e45cdcf1121e87ba1ae50d64d605 | …/aa/repos/crewrp | no |
| uni-tutor | 0d205c195ada785dffbf0788aab16bc70ea16c67 | …/aa/repos/uni-tutor | no |

## Per client

| client_repo | project_id | mechanical | heuristic | High/Med tickets |
| :--- | :--- | :--- | :--- | :--- |
| sw-factory | 8a927848-4411-42a8-8508-f7b8efb3ec60 | skip — no `.factory/quality.yaml` / no `clean_code:` | skipped with Discover | none |
| crewrp | 525d05c5-ef00-4ff6-917d-3632edc6493e | skip — same | skipped | none |
| uni-tutor | 1fc753f5-8cd8-4e01-af7a-39a798895904 | skip — same | skipped | none |

nl2sql: registry 밖 → out of scope.

## Notes

- Not a prod gate; no `aa: security pass|fail`.
- `nf-progress:` N/A — mechanical command never started.
- open `[clean-code]` tickets: none on client projects (dedup N/A).
