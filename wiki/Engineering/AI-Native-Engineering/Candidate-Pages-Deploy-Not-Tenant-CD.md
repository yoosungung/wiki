---
id: candidate-pages-deploy-not-tenant-cd
title: "candidate.win feature deploy = GitHub Pages (tenant_cd N/A)"
status: canonical
owner: km
updated: "2026-11-11"
last_updated: "2026-11-11"
review_after: "2027-02-11"
sources:
  - inbox/ta/2026-11-10-candidate-pages-deploy-not-tenant-cd.md
  - ticket:63833bbf-76a6-493d-854c-404c3ffb5488
  - https://github.com/berryking404/candidate.win/actions/runs/42786019356
  - wiki/Engineering/AI-Native-Engineering/Candidate-Source-URL-NA-Guard.md
  - wiki/Engineering/Infrastructure-and-DevOps/Tenant-CD-Registry-Missing-Workflow.md
tags: ["Engineering", "AI-Native", "candidate.win", "GitHub-Pages", "tenant_cd"]
type: wiki
---

# candidate.win feature deploy = GitHub Pages (tenant_cd N/A)

`ta.tenant_cd[]` / `tenant-cd-registry.json`에 candidate.win이 없고 제품에 `.factory/cd.yaml`도 없다. k8s tenant_cd 경로를 **발명하지 않는다**.

## 계약

| 축 | 내용 |
| :--- | :--- |
| Deploy | `deploy.yml` = Pages `workflow_dispatch`. `environment` / `image_tag` input 없음 |
| Done 게이트 | `test:` + `prod:` (QA/AA ladder 없음) |
| prod 증거 | merge push → Pages Deploy success + live smoke (예: `wiki.candidate.win`) |

레지스트리 workflow 부재 시 tip-path 대체 금지 축은 [[wiki/Engineering/Infrastructure-and-DevOps/Tenant-CD-Registry-Missing-Workflow.md]] — 여기서는 **레지스트리 자체가 없음**이므로 Pages가 정본 CD.

## 예

merge `55d1f459` → Actions run 42786019356 success; live JS `접수 완료` early-return → `closeReportModal()` (정정 모달 UX).

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Candidate-Correction-Report-Worker.md]]
- [[wiki/Engineering/AI-Native-Engineering/Candidate-Sourceless-Stance-Takedown.md]]
