---
id: list-api-corrupt-payload-head-error
title: "목록 API corrupt 페이로드 → head_error (전체 실패 금지)"
status: canonical
owner: km
updated: "2026-08-19"
last_updated: "2026-08-19"
review_after: "2026-11-19"
sources:
  - ticket:918
  - https://aicodingguild.com/blog/api-error-handling-what-to-return-and-what-to-swallow
tags: ["Engineering", "AI-Native", "API", "Error-Handling", "Security"]
type: "wiki"
---

# 목록 API corrupt 페이로드 → head_error (전체 실패 금지)

디렉터리/메타데이터 **목록** API에서 항목 하나의 JSON·헤더가 깨져도 전체 응답을 500으로 죽이지 않는다. 해당 항목에 `head_error`(또는 동등 필드)를 넣고 나머지 항목은 계속 반환한다.

## 패턴

| 상황 | 응답 | 금지 |
| :--- | :--- | :--- |
| 항목 파싱 예외 | `head_error=str(exc)`(+ warning 로그), 목록 계속 | 한 파일 corrupt로 전체 list abort |
| 인증/principal | 기존 console/auth principal 유지 | corrupt 경로로 trust boundary 완화 |
| 경로 노출 | 일반 경로는 rel-path/JSON parse 메시지 | abs path를 일반 클라이언트에 흘림(Low residual이면 문서화만) |

```python
# 개념
try:
    head = parse_item(raw)
except Exception as exc:
    item["head_error"] = str(exc)
    log.warning("corrupt list item", exc_info=exc)
```

dotfile/숨김 필터·권한 게이트는 그대로 둔다. 리팩터로 helper를 빼도 **새 trust boundary**가 없으면 security mechanical skip + scoped manual로 충분 — [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]].

## 적용 체크

1. corrupt fixture unit이 `head_error`를 assert하는가?
2. 목록 성공 경로가 한 항목 실패로 무너지지 않는가?
3. 에러 문자열에 시크릿·불필요 abs path가 없는가?

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
