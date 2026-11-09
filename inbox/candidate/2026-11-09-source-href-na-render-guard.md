---
id: inbox-candidate-source-href-na-render-guard
agent: candidate
ticket_id: 38f15177-82cb-43c9-a7e0-549e9fda9a60
updated: 2026-11-09
status: inbox
sources:
  - ticket:38f15177-82cb-43c9-a7e0-549e9fda9a60
  - https://wiki.candidate.win/people/i-si-ba/
---

# Hugo render-link: invalid source는 앵커 금지

- 증상: stance `[출처](N/A)` → prod HTML `<a href=N/A>출처</a>` (상대경로로 잘못 이동).
- 가드: `wiki/layouts/_markup/render-link.html` 에서 `http(s)://` 또는 `/` 로 시작하는 destination만 `<a>`; 그 외는 `.Text`만.
- 동일 가드: `issues-single.html` frontmatter source 표, `today/list.html` 대표 근거.
- 회귀 테스트: `agent/tests/test_source_link_new_tab.py`.
- 관련 canonical: [[wiki/Engineering/AI-Native-Engineering/Hugo-External-Link-New-Tab.md]] (새 탭 규칙; invalid destination 분기 보강 필요).
