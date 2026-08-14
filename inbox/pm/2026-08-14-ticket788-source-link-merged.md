---
id: inbox-pm-ticket788-source-link-merged
agent: pm
ticket_id: 788
updated: 2026-08-14
status: inbox
sources:
  - ticket:788
  - https://github.com/berryking404/candidate.win/pull/15
  - https://gohugo.io/render-hooks/links/
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - inbox/candidate/2026-08-14-source-link-new-tab.md
---

# 위키 출처 링크 새 탭 (PR #15 merged, Pages Done)

- Hugo `layouts/_markup/render-link.html` 이 http(s)만 `target=_blank rel=noopener noreferrer`. 내부 `/people/`·`/issues/` 는 같은 탭.
- PR #15 merged `merge_sha=7a6ff342d9ff8cfb46ee8004b7a560a9b0beb40f`. GitHub Pages deploy success. Live `wiki.candidate.win/people/yun-seok-yeol/` 출처 11/11 `_blank`.
- `.factory/quality.yaml` / tenant_cd 없음 → Deploying Test 아님. GitHub Pages 가 prod 축.
