---
id: inbox-pm-unitutor-cloudflare-deploy-prep
agent: pm
ticket_id: f7f980f3-ac59-42fc-a462-45ecfe6df2b8
updated: 2026-10-01
status: inbox
sources:
  - ticket:f7f980f3-ac59-42fc-a462-45ecfe6df2b8
  - wiki/Engineering/Infrastructure-and-DevOps/Cloudflare-D1-Migrations-Before-Worker-Deploy.md
---

# UniTutor Cloudflare 배포 준비 (intake)

- UniTutor DESIGN: FE=Cloudflare Pages(`dist/`), BE=Workers(`wrangler`), D1/R2/KV는 선택 바인딩.
- 갭(2026-10-01): `deploy/SETUP.md`·CI workflow 없음, `wrangler.jsonc` 최소 vars만, FE Pages/`VITE_*` API base 미비. AGENTS의 k8s 문구는 CF와 불일치 → CF 기준으로 정합.
- 첫 배포 최소: Pages 정적 + Workers 헬스/스텁. D1 쓰면 **migrations apply → wrangler deploy** 고정.
- 원격 배포 시크릿(`CLOUDFLARE_API_TOKEN` Workers+D1)은 인간 게이트; 없으면 blocker만.
