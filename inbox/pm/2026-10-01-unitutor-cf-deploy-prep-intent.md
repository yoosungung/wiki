---
id: inbox-pm-unitutor-cf-deploy-prep-intent
agent: pm
ticket_id: f7f980f3-ac59-42fc-a462-45ecfe6df2b8
updated: 2026-10-01
status: inbox
sources:
  - ticket:f7f980f3-ac59-42fc-a462-45ecfe6df2b8
  - https://github.com/yoosungung/UniTutorAI/pull/8
  - wiki/Engineering/Infrastructure-and-DevOps/Cloudflare-D1-Migrations-Before-Worker-Deploy.md
---

# UniTutor Cloudflare deploy prep — Intent pass

- UniTutor CF 배포 준비(AC1–4): `deploy/SETUP.md`, Workers `deploy:dry-run`, Pages + `VITE_API_BASE_URL`, CI — PR #8 squash merge `fa13d742`.
- D1 미바인딩 → apply→deploy는 SETUP에 N/A로 문서화; 바인딩 시 wiki D1-before-deploy 순서 적용.
- macOS에서 `package-lock.json` 재생성 시 `@rollup/rollup-linux-x64-gnu` 패키지 엔트리가 빠져 Linux CI가 깨질 수 있음 → main lock 기준으로 재생성해 optional platform 엔트리 유지.
- 원격 첫 배포는 `CLOUDFLARE_API_TOKEN` / `CLOUDFLARE_ACCOUNT_ID` / Pages `unitutor` 준비 후 별도 티켓.
