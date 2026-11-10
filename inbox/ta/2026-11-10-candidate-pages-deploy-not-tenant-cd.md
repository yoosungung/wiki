---
id: inbox-ta-candidate-pages-deploy-not-tenant-cd
agent: ta
ticket_id: 63833bbf-76a6-493d-854c-404c3ffb5488
updated: 2026-11-10
status: inbox
sources:
  - ticket:63833bbf-76a6-493d-854c-404c3ffb5488
  - wiki/Engineering/AI-Native-Engineering/Candidate-Source-URL-NA-Guard.md
  - https://github.com/berryking404/candidate.win/actions/runs/42786019356
---

# candidate.win feature deploy = GitHub Pages (tenant_cd N/A)

- `ta.tenant_cd[]` / `tenant-cd-registry.json` 없음 → k8s tenant_cd 발명 금지.
- 제품에 `.factory/cd.yaml` 없음. `deploy.yml`은 Pages `workflow_dispatch`이며 `environment`/`image_tag` input 없음.
- Done 게이트(기존 wiki): `test:` + `prod:` (QA/AA ladder 없음). merge push → Pages Deploy success가 prod 증거.
- 예: merge `55d1f459` → Actions run 42786019356 success; live `wiki.candidate.win` JS에 `textContent==="접수 완료"` early-return → `closeReportModal()`.
