---
id: inbox-sql-mcp-marketing-yaml
agent: sql-mcp
ticket_id: 44336af7-b7a8-4e36-ad56-f5f24c538be2
updated: 2026-11-17
status: inbox
sources:
  - ticket:44336af7-b7a8-4e36-ad56-f5f24c538be2
  - https://github.com/yoosungung/sql-mcp/pull/4
  - wiki/Engineering/AI-Native-Engineering/Tenant-Marketing-Yaml-Persona-Overlay-Pattern.md
---

# sql-mcp `.factory/marketing.yaml` landed

- Path: product repo `.factory/marketing.yaml` (mm topic-radar What; missing→skip).
- Schema used flat contract (`sites`/`keywords`/`tone`/`product_mention`/`must_avoid`); ticket nested tone map / `comment_draft` / `locale` / `max_candidates_per_run` not in mm example — collapsed into string `tone` + soft mention.
- Keywords: NL2SQL, text-to-SQL, SQL generation, sql-mcp. Sites: linkedin + KR blogs (velog/tistory/naver/brunch) + medium/dev.to.
- Soft-mention only; no external auto-post.
