---
id: inbox-ta-nl2sql-missing-deploy-yml
agent: ta
ticket_id: 918
updated: 2026-08-17
status: inbox
sources:
  - ticket:918
  - https://github.com/yoosungung/nl2sql
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# nl2sql tenant_cd: registry points to missing deploy.yml

- `tenant-cd-registry` enables nl2sql with `workflow: deploy.yml` + `image_input: image_tag`.
- On `main` (and merge_sha `85cba02`), `.github/workflows/` has only `ci.yml`, `build-ghcr-images.yml`, `publish-releases.yml` — no `deploy.yml`.
- `gh workflow run deploy.yml` fails: `workflow deploy.yml not found on the default branch`.
- TA must not invent a substitute workflow; leave Blocked + escalate human/platform until the repo adds `workflow_dispatch` deploy or registry is corrected.
