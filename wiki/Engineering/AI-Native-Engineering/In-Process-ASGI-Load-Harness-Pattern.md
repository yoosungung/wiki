---
id: in-process-asgi-load-harness-pattern
title: "In-process ASGI 로드 하네스 (chat SSE·임계)"
status: canonical
owner: km
updated: "2026-08-04"
last_updated: "2026-08-04"
review_after: "2026-11-04"
sources:
  - ticket:114
  - ticket:116
  - ticket:99
tags: ["Engineering", "AI-Native", "Load", "ASGI", "Quality", "SSE"]
type: "wiki"
---

# In-process ASGI 로드 하네스 (chat SSE·임계)

주간 NF `load.command`를 **실 LLM/클러스터 없이** 재현하려면 in-process ASGI + FakeAgent가 기본이다. UI Playwright 축([[wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md]])·SQL EX 축([[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]])과 분리한다.

## 시나리오 골격

1. health warm-up (`GET /api/health` 등)
2. `POST /api/chat` SSE drain
3. `GET /api/conversations` (또는 동등 대화 목록)

## 기본 vs 실 LLM

| 모드 | 조건 | 용도 |
| :--- | :--- | :--- |
| **주간 기본** | in-process + FakeAgent, SGLang OFF | 결정적 p95·에러율 |
| **실 LLM opt-in** | `LOAD_REAL_LLM=1` + `LOAD_BASE_URL` + 앱 auth 헤더 | 클러스터/Ingress 검증 |

`ASGITransport`는 FastAPI **lifespan을 안 돈다** → `app.router.lifespan_context(app)`로 store/agent wire를 강제한다.

```python
# 개념: lifespan 없이 라우트만 올리면 store/agent 미초기화
async with app.router.lifespan_context(app):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        ...
```

## 임계 env (예시)

| env | 기본 역할 |
| :--- | :--- |
| `LOAD_P95_MS` | p95 상한 (예: 2000); `0`이면 즉시 실패로 게이트 자체 검증 |
| `LOAD_MAX_ERROR_RATE` | 허용 에러율 |
| `LOAD_WALL_SEC` | 벽시계 상한 |

위반 시 non-zero + `FAIL:` stderr. quality.yaml에만 키를 두고 커맨드가 health-only면 chat 회귀를 못 잡는다 — [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]].

## Auth 정합

앱이 `X-Forwarded-*` 신원 헤더를 쓰면 하네스도 동일 헤더를 맞춘다. 미인증 chat → 401이 정상 스모크다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
