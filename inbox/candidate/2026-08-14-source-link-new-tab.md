---
id: inbox-candidate-2026-08-14-source-link-new-tab
agent: candidate
ticket_id: 788
updated: 2026-08-14
status: inbox
sources:
  - ticket:788
  - https://gohugo.io/render-hooks/links/
---

# 위키 외부 출처 링크는 새 탭

- 마크다운 `[출처](https://…)` 는 Hugo `layouts/_markup/render-link.html` 로 http(s)만 `target="_blank"` + `rel="noopener noreferrer"`.
- `/people/`, `/issues/` 내부 경로는 같은 탭. 콘텐츠 YAML/MD 변경 없음.
- 오늘의 화제 대표 근거 URL도 템플릿에서 새 탭. 이슈 입장 표 출처 링크는 기존과 동일.
