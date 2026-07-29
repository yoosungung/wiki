---
id: nl2sql-playwright-e2e-smoke
title: "nl2sql frontend Playwright UI 스모크"
status: canonical
owner: km
updated: "2026-07-29"
last_updated: "2026-07-29"
review_after: "2026-08-29"
sources:
  - ticket:31
  - https://playwright.dev/docs/best-practices
tags: ["Engineering", "AI-Native", "Playwright", "nl2sql", "E2E", "Quality"]
type: "wiki"
---

# nl2sql frontend Playwright UI 스모크

티켓 #31 — nl2sql 프론트엔드 UI 스모크. Spider2 exec_result 품질 게이트([[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]])와 **축이 다름**(UI vs SQL EX).

## 레지스트리·실행

- 레지스트리: `.factory/quality.yaml` → `e2e:` → `frontend/e2e/*.spec.ts`
- 실행:

```bash
cd frontend && npm run test:e2e
```

- Vite `webServer`로 기동; **backend/LLM 불필요**.

## Mock 패턴

metadata 목록은 `page.route`로 `GET /api/metadata/fs`를 mock한다 ([Playwright best practices](https://playwright.dev/docs/best-practices)).

## Pod / CDN IPv6 회피

Pod에서 Playwright 브라우저 CDN이 IPv6 `ENETUNREACH`일 때:

```bash
# apt chromium + 스킵 다운로드
PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
PLAYWRIGHT_CHROMIUM_PATH=/usr/bin/chromium
```

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
