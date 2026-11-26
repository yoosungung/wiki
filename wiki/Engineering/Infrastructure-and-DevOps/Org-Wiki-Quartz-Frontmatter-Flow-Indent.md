---
id: org-wiki-quartz-frontmatter-flow-indent
title: "org-wiki Quartz frontmatter flow-array indent"
status: canonical
owner: km
updated: "2026-11-26"
review_after: "2027-02-26"
sources:
  - ticket:13f467cb-fb13-4d30-b4cc-48e59837d38c
  - https://github.com/yoosungung/wiki/actions/runs/45722067188
tags: ["Engineering", "Infrastructure", "GitHub-Pages", "Quartz", "org-wiki", "frontmatter"]
type: "wiki"
---

# org-wiki Quartz frontmatter flow-array indent

`yoosungung/wiki` Deploy가 **Build Quartz Site**에서 `Invalid frontmatter: deficient indentation`로 죽으면 Pages sync flake([[wiki/Engineering/Infrastructure-and-DevOps/Org-Wiki-Pages-Deploy-Sync-Timeout.md]])가 아니라 **YAML frontmatter**를 먼저 본다.

## 판별

| 신호 | 해석 |
| :--- | :--- |
| build job red, `Failed to process markdown … Invalid frontmatter: deficient indentation` | 해당 md frontmatter YAML 파싱 실패 |
| 로그가 `key: [` 다음 줄들에 `"…"` 후 **column-0 `]`** | multiline flow sequence 닫는 괄호 들여쓰기 부족 (Quartz/gray-matter 계열) |
| deploy job skipped / 0s | build 선행 실패 — sync timeout 아님 |

## 수정

multiline flow를 **block list**로 바꾼다.

```yaml
# bad — `]` at column 0
related_raw: [
  "[[wiki/…]]",
  "[[raw/…]]"
]

# good
related_raw:
  - "[[wiki/…]]"
  - "[[raw/…]]"
```

한 줄 flow(`related_raw: ["a", "b"]`)는 보통 통과한다. **여러 줄 + 닫는 `]`가 맨 왼쪽**일 때만 터진다.

오프너도 `---\n`이어야 한다. `---title:`처럼 붙이면 gray-matter가 `engine "title: …" is not registered`로 실패한다.

## 증거 (2026-11-26)

- fail Actions #1919 / run `45722067188` (SHA `01ec590`): `Deep-Agents-Definition.md` 외 동일 패턴 9파일
- tip push로 block-list 변환 후 Deploy 재기동
