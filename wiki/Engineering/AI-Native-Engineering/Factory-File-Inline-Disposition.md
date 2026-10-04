---
id: factory-file-inline-disposition
title: "Factory: same-origin file Content-Disposition allowlist"
status: canonical
owner: km
updated: "2026-10-05"
review_after: "2027-01-05"
sources:
  - inbox/aa/2026-10-04-factory-file-inline-xss-gate.md
  - inbox/qa/2026-10-04-factory-file-disposition-inline-qa.md
  - inbox/ta/2026-10-04-factory-file-viewer-prod-pass.md
  - ticket:cebdb6bc-1535-46a7-abc8-9fe14e2cea3b
  - https://github.com/yoosungung/sw-factory/pull/35
  - https://web.dev/articles/securely-hosting-user-data
  - wiki/Engineering/Infrastructure-and-DevOps/Factory-Workers-Single-Env-CD.md
tags: ["Engineering", "AI-Native", "Factory", "Security", "Files"]
type: "wiki"
---

# Factory: same-origin file Content-Disposition allowlist

User attachments are served on the **app origin**. Browser `Content-Disposition: inline` must be **allowlist-only**.

## Rule

- Inline MIME (normalized `split(";")[0].trim().toLowerCase()`): `image/png|jpeg|gif|webp`, `application/pdf`, `text/plain`.
- Force `attachment` for `text/html`, `image/svg+xml`, `text/javascript`, and unknown MIME.
- Do **not** map `image/*` → inline — SVG executes script as a top-level document.
- Sanitize filename quotes/CRLF in disposition header.

## Ops evidence (2026-10-04)

- PR #35 / tip `02a5d4f` == merge; Deploy run 37168559498 (Workers single prod).
- Live: png → `inline`; octet-stream/html/svg → `attachment`; unauth GET → 401.
- Residual NF: `X-Content-Type-Options: nosniff` on `GET /api/files/:id`.

## Related

- [[wiki/Engineering/Infrastructure-and-DevOps/Factory-Workers-Single-Env-CD.md]]
- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
