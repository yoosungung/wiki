---
id: existence-gate-corrupt-vs-absent
title: "존재 게이트: corrupt ≠ absent"
status: canonical
owner: km
updated: "2026-09-07"
last_updated: "2026-09-07"
review_after: "2026-12-07"
sources:
  - ticket:1747
  - inbox/nl2sql/2026-09-07-source-exists-corrupt-gate.md
  - https://aicodingguild.com/blog/api-error-handling-what-to-return-and-what-to-swallow
tags: ["Engineering", "AI-Native", "API", "Error-Handling", "Security"]
type: "wiki"
---

# 존재 게이트: corrupt ≠ absent

이름/스템이 일치하는 리소스가 **읽히지 않을 때**를 “없음(404)”으로 삼키면 클라이언트가 재생성·덮어쓰기로 데이터를 날릴 수 있다. **목록 API의 per-item `head_error` continue**와 축이 다르다 — [[wiki/Engineering/AI-Native-Engineering/List-Api-Corrupt-Payload-Head-Error.md]].

## 판별

| 상황 | 응답 | 금지 |
| :--- | :--- | :--- |
| 스템 일치 파일 없음 | 404 `unknown_source`(또는 동등) | corrupt를 absent로 위장 |
| 스템 일치 + JSON/읽기 실패 | 422 `invalid_json` + `corrupt_paths` + warning 로그 | `continue`로 존재 검사를 건너뛰기 |
| 다른 스템만 corrupt | 존재 판정에 영향 없음 | 무관 corrupt로 전체 404 차단 |
| 다른 경로에 유효 이름 매치 | exists=true | 첫 corrupt에서 조기 종료 |

```python
# 개념: existence gate (binary)
for path in matching_stems(name):
    try:
        parse(path)
        return exists
    except Corrupt as exc:
        corrupt_paths.append(path)
        log.warning("corrupt matching stem", path=path, exc_info=exc)
if corrupt_paths:
    raise HTTPException(422, detail={"code": "invalid_json", "corrupt_paths": corrupt_paths})
raise HTTPException(404, detail={"code": "unknown_source"})
```

## 목록 vs 존재

- **목록**: 한 항목 corrupt → 그 항목에 `head_error`, 나머지 계속.
- **존재/단건 게이트**: 매칭 스템이 corrupt면 **모호함을 표면화**(422). 없음과 구분한다.

## 적용 체크

1. corrupt fixture가 404가 아니라 422(+`corrupt_paths`)를 assert하는가?
2. 무관 스템 corrupt가 정상 부재 404를 막지 않는가?
3. 로거 이름이 이동 모듈과 일치하는가(라우터 extract 후)?

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/List-Api-Corrupt-Payload-Head-Error.md]]
- [[wiki/Engineering/AI-Native-Engineering/Smell-Agglomeration-Module-Split.md]]
- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
