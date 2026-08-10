---
id: playwright-frontend-ui-smoke-pattern
title: "Playwright 프론트엔드 UI 스모크 패턴 (백엔드 없이)"
status: canonical
owner: km
updated: "2026-08-10"
last_updated: "2026-08-10"
review_after: "2026-10-31"
sources:
  - ticket:51
  - https://playwright.dev/docs/best-practices
tags: ["Engineering", "AI-Native", "Playwright", "E2E", "Quality", "Frontend"]
type: "wiki"
---

# Playwright 프론트엔드 UI 스모크 패턴 (백엔드 없이)

제품 프론트만으로 UI 회귀를 잡는 **재사용 패턴**. SQL EX/exec_result 품질 게이트([[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]])와 **축이 다름**(UI vs 실행 결과).

## 레지스트리·실행

에이전트 팩토리형 레포에서는 quality 레지스트리에 e2e를 명시한다.

- 레지스트리 예: `.factory/quality.yaml` → `e2e:` → `frontend/e2e/*.spec.ts`
- 실행 예:

```bash
cd frontend && npm run test:e2e
```

- Vite `webServer`로 프론트만 기동; **backend/LLM 불필요**.

## Mock 패턴

목록/메타 API는 `page.route`로 mock한다 ([Playwright best practices](https://playwright.dev/docs/best-practices)).

```ts
// 예: 메타데이터 목록
await page.route("**/api/metadata/fs", async (route) => {
  await route.fulfill({ json: { /* fixture */ } });
});
```

## Pod / CDN IPv6 회피

Pod에서 Playwright 브라우저 CDN이 IPv6 `ENETUNREACH`일 때 apt chromium + 다운로드 스킵:

```bash
PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
PLAYWRIGHT_CHROMIUM_PATH=/usr/bin/chromium
```

Chromium 설치·다운로드가 불가하면 **동일 템플릿의 HTMX/SSR partial** + 배포 아티팩트 정적 검증으로 UI-equivalent 증거를 남긴다(브라우저 E2E 대체, 별 축 명시).

## 적용 팁

- frontend-only 변경이면 e2e 축만 게이트하고, 미터치 백엔드 CI red는 **별 축**으로 다룬다.
- 제품 예시(nl2sql): 동일 패턴을 `frontend/e2e`에 적용. 팩토리 맥락: [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]].


## 스코프 경계

UI Playwright는 shell/nav/list 스모크다. backend SSE 필드(예: `tool_result.ok`) 행위는 **unit/`test_chat*.py`**가 정본 — E2E green만으로 SSE 계약 완료로 보지 않는다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Created-By-Me-Terminal-Status-Order.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
