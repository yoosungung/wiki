---
id: hugo-external-link-new-tab
title: "정적 사이트: 외부 http(s) 링크는 새 탭"
status: canonical
owner: km
updated: "2026-08-14"
last_updated: "2026-08-14"
review_after: "2026-11-14"
sources:
  - ticket:788
  - https://gohugo.io/render-hooks/links/
tags: ["Engineering", "AI-Native", "Hugo", "Render-Hooks", "UX"]
type: "wiki"
---

# 정적 사이트: 외부 http(s) 링크는 새 탭

마크다운 `[출처](https://…)` 를 콘텐츠 YAML/MD에서 고치지 않고, **렌더 훅**에서만 새 탭을 연다. 내부 경로는 같은 탭을 유지한다.

## 규칙

| 링크 | 동작 |
| :--- | :--- |
| `http://` / `https://` | `target="_blank"` + `rel="noopener noreferrer"` |
| 사이트 내부 경로 (`/people/`, `/issues/` 등) | 같은 탭 |

Hugo는 `layouts/_markup/render-link.html` 훅이 정본이다. ([render hooks](https://gohugo.io/render-hooks/links/))

## 함정

- 본문·데이터 파일에 `target=` 를 심으면 템플릿과 이중 관리가 된다. **훅만** 바꾼다.
- 대표 근거 URL(예: 이슈 랜딩의 외부 출처)도 훅을 탄다. 표 안의 내부 경로와 축을 섞지 않는다.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Static-Site-Frontmatter-Title-Sync.md]]
- [[wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md]]
