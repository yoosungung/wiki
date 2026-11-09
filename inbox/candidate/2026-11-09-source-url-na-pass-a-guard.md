---
id: inbox-candidate-2026-11-09-source-url-na-pass-a-guard
agent: candidate
ticket_id: 38f15177-82cb-43c9-a7e0-549e9fda9a60
updated: 2026-11-09
status: inbox
sources:
  - ticket:38f15177-82cb-43c9-a7e0-549e9fda9a60
  - wiki/Engineering/AI-Native-Engineering/Hugo-External-Link-New-Tab.md
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
---

# Pass A: `source_url=N/A` 가 fallback을 가림

- Tier1 quote에 `source_url: "N/A"`가 오면 truthy라 `_source_url_from_stance`가 크롤 fallback http(s)를 스킵하고 `[출처](N/A)`를 기록했다.
- `quality_gate` Rule1은 empty URL만 강등 → `N/A`는 Rule3 캐시미스로 통과해 지지/반대 stance가 공개됐다.
- 수정: `is_valid_source_url`(http/https만) + Pass A format이 invalid quote를 skip하고 fallback 사용 + gate가 무효 URL 강등. 기존 `[출처](N/A)`는 미확인으로 정리. render-hook 앵커 금지는 secondary.
