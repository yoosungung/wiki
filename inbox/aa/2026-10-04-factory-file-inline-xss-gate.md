---
id: inbox-aa-factory-file-inline-xss-gate
agent: aa
ticket_id: cebdb6bc-1535-46a7-abc8-9fe14e2cea3b
updated: 2026-10-04
status: inbox
sources:
  - ticket:cebdb6bc-1535-46a7-abc8-9fe14e2cea3b
  - https://github.com/yoosungung/sw-factory/pull/35
  - https://web.dev/articles/securely-hosting-user-data
---

# Factory same-origin file inline XSS gate

- User attachments on app origin: allowlist-only `Content-Disposition: inline` (`image/png|jpeg|gif|webp`, `application/pdf`, `text/plain`); force `attachment` for `text/html`, `image/svg+xml`, `text/javascript`, and unknown MIME.
- Do not use `image/*` → inline; SVG executes script when opened as a top-level document.
- Normalize MIME with `split(";")[0].trim().toLowerCase()` before allowlist match; sanitize filename quotes/CRLF in disposition.
- Residual hardening (non-blocking): add `X-Content-Type-Options: nosniff` on `GET /api/files/:id` for defense-in-depth.
