---
id: openai-http-429-billing-vs-rate-limit-triage
title: "OpenAI HTTP 429: 빌링·쿼터 vs rate limit 트리아지"
status: canonical
owner: km
updated: "2026-09-06"
last_updated: "2026-09-06"
review_after: "2026-12-06"
sources:
  - https://developers.openai.com/api/docs/guides/error-codes
  - https://help.openai.com/en/articles/5955604
  - inbox/pm/2026-09-04-candydate-pass-ab-openai-quota.md
  - inbox/pm/2026-09-06-candydate-pass-ab-openai-credits.md
  - ticket:1655
  - ticket:1686
  - ticket:1717
tags: ["Engineering", "AI-Native", "OpenAI", "Billing", "RateLimit", "Triage"]
type: "wiki"
---

# OpenAI HTTP 429: 빌링·쿼터 vs rate limit 트리아지

동일 HTTP **429**라도 `error.code`에 따라 **재시도가 의미 있는지**가 갈린다. SDK가 `RateLimitError`로 감싸도 본문 code를 먼저 본다.

## 판별 표

| `error.code` (대표) | 원인 | 재시도 | 라우팅 |
| :--- | :--- | :--- | :--- |
| `rate_limit_exceeded` / RPM·TPM 한도 | 요청이 너무 빠름 | **예** — `Retry-After` 또는 지수 백오프 | 자동 재시도·부하 조절 |
| `slow_down` | ramp-rate (급증) | **예** — 완만히 올리기 | 자동 재시도 |
| `credit_balance_exhausted` | 선불 크레딧 고갈 | **아니오** | 인간 빌링 (`Waiting for Approval`) |
| `organization_spend_limit_exceeded` / `project_spend_limit_exceeded` | org/project spend cap | **아니오** | 인간 한도 상향 |
| `organization_usage_limit_exceeded` | OpenAI 부여 usage cap | **아니오** | 한도 상향 요청·support |

공식 가이드: 빌링·spend·쿼터 계열은 재시도로 복구되지 않는다. `error.type`이 `insufficient_quota`여도 **code로 세분**한다. ([Error codes](https://developers.openai.com/api/docs/guides/error-codes))

## 운영 규칙

1. 스케줄/Pass 수집이 429로 실패하면 **본문 `error.code`를 로그·티켓에 남긴다**(HTTP만으로 rate-limit 취급 금지).
2. `credit_balance_exhausted` / spend·usage limit → In Progress 재시도 루프 **금지**. `Waiting for Approval` + 인간(billing) assignee. 새 `@mention` 폭주 금지. 미배정 cron 실패를 **Blocked(FS 마커 없이)** 로 두지 않는다 — Approval lane이 정본.
3. `rate_limit_exceeded` / `slow_down` → 백오프·동시성 축소 후 재실행. 직전 cron이 연속 성공이었으면 코드 회귀보다 **일시 한도**를 먼저 의한다.
4. 해제 검증: 크레딧/한도 복구 후 다음 스케줄 성공 또는 수동 수집 1회.
5. SDK가 `RateLimitError`로 감싸도 `type=insufficient_quota`만 보지 말고 **`code=credit_balance_exhausted`** 를 로그·티켓에 남긴다(연속 동일 코드 streak면 재시도·코드 회귀 가설 금지).

```python
# 개념: SDK RateLimitError라도 body code로 분기
code = getattr(getattr(exc, "body", None), "get", lambda *_: None)("error", {}).get("code") \
    or (exc.body or {}).get("error", {}).get("code")  # SDK 버전에 맞게 파싱
if code in {
    "credit_balance_exhausted",
    "organization_spend_limit_exceeded",
    "project_spend_limit_exceeded",
    "organization_usage_limit_exceeded",
}:
    # → Waiting for Approval (human billing) — retry 금지
    ...
else:
    # → Retry-After / exponential backoff
    ...
```

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md]] — 임계 spend alert의 Approval lane
- [[wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md]] — 수집 실패 시 빈 산출물 덮어쓰기 금지
