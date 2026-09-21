---
id: inbox-codingland-ingest-skip-count
agent: codingland
ticket_id: 2206
updated: 2026-09-21
status: inbox
sources:
  - ticket:2206
  - https://scanaislop.com/blog/the-swallowed-exception-that-broke-production/
---

# Workspace ingest done vs skipped

- Full-scan `done` increments only when `ingestUri` returns a delta. A skip log that still increments `done` treats a detected read failure as success and hides missing graph nodes.
- Paths dropped by `isExcludedPath` before `ingestUri` are neither `done` nor `skipped`.
- Complete line shape: `ingest complete - {done} files, {skipped} skipped, {nodes} nodes`.
