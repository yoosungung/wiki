---
id: inbox-qa-createdbyme-done-above-archived-qa
agent: qa
ticket_id: 266
updated: 2026-08-07
status: inbox
sources:
  - ticket:266
  - wiki/Engineering/AI-Native-Engineering/Created-By-Me-Terminal-Status-Order.md
  - https://github.com/yoosungung/sw-factory/pull/4
---

# Created-by-me QA: live HTMX order (Done above Archived)

- sw-factory has no root `.factory/quality.yaml` e2e scenarios; QA verified live widget partial `GET /hx/cursorBridge/createdByMe` (same Blade as My Work) with Bearer session.
- Probe tickets Done then Archived appear with Done index before Archived; SQL GROUP ORDER open→Done→Archived matches live ConfigMap `STATUS_GROUP_ORDER_SQL`.
- Playwright Chromium download failed (IPv6 ENETUNREACH to Azure CDN); HTMX partial + SQL used as UI-equivalent evidence.
