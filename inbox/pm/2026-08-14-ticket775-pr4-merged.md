---
id: inbox-pm-ticket775-pr4-merged
agent: pm
ticket_id: 775
updated: 2026-08-14
status: inbox
sources:
  - ticket:775
  - https://github.com/yoosungung/k8s-test/pull/4
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - inbox/ta/2026-08-14-ticket775-postgres-memory-4gi.md
---

# #775 Review merge (k8s-test PR #4)

- Merged `https://github.com/yoosungung/k8s-test/pull/4` `bdc4556c0ce7afa5a02a0985084eeaeba047465c`. Gate `./scripts/test-postgresql-resources.sh` PASS on merged main. No required GitHub checks.
- Live STS already 4Gi/2Gi (ta patch + `resources-evidence.txt`). Remaining: Helm `deploy.sh` must not regress to 512Mi — ta only (pm no kubectl). Not tenant_cd; Prod N/A.
- hermesdb DROP still out of this AC (Eric #3777 assess-only).
