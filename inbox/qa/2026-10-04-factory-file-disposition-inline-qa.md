---
id: inbox-qa-factory-file-disposition-inline-qa
agent: qa
ticket_id: cebdb6bc-1535-46a7-abc8-9fe14e2cea3b
updated: 2026-10-04
status: inbox
sources:
  - ticket:cebdb6bc-1535-46a7-abc8-9fe14e2cea3b
  - https://github.com/yoosungung/sw-factory/pull/35
  - wiki/Engineering/Infrastructure-and-DevOps/Factory-Workers-Single-Env-CD.md
---

# Factory attachment inline vs download (QA)

- `GET /api/files/:id` MIME allowlist → `Content-Disposition: inline` (png/jpeg/gif/webp, pdf, text/plain); else `attachment` (HTML/SVG excluded for XSS).
- FE Files tab keeps `target=_blank`; browser shows image/PDF tab when inline, downloads when attachment.
- Live smoke: open `/projects/{id}?issue={ticketId}` → Files → click links; assert popup title/dims for png + Playwright `download` event for octet-stream.
- Unauthenticated GET → 401/403 (membership gate unchanged).
