---
id: static-site-frontmatter-title-sync
title: "정적 사이트: 데이터 title → front matter title 동기화"
status: canonical
owner: km
updated: "2026-08-14"
last_updated: "2026-08-14"
review_after: "2026-11-14"
sources:
  - ticket:171
tags: ["Engineering", "AI-Native", "Hugo", "Frontmatter", "CMS"]
type: "wiki"
---

# 정적 사이트: 데이터 title → front matter title 동기화

Hugo(또는 동등) 이슈/문서 페이지가 **wiki front matter `title`**만 렌더하고, YAML 데이터(`title_ko` 등)는 무시하면, 데이터만 채운 페이지 크롬에 **"—"**가 뜬다.

## 규칙

| 경로 | 기대 |
| :--- | :--- |
| 신규 셸 생성 | `create_wiki_page` / radar shell이 front matter `title`을 즉시 기록 |
| 메타 동기화 CLI | `apply-meta`가 status/conclusion뿐 아니라 **`title_ko`(fallback `title`) → front matter `title`** |
| 역사적 셸 | apply-meta 재실행 또는 일회 백필 |

`status`만 동기화하고 제목을 빠뜨리면 수동/부분 생성 페이지에서 재발한다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md]]
- [[wiki/Engineering/AI-Native-Engineering/Hugo-External-Link-New-Tab.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
