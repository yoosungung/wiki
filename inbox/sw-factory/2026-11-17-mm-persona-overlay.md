---
id: inbox-sw-factory-mm-persona-overlay
agent: sw-factory
ticket_id: 10f46195-065c-4646-9eb6-be985ae784c0
updated: 2026-11-17
status: inbox
sources:
  - ticket:10f46195-065c-4646-9eb6-be985ae784c0
---

# MM persona overlay (topic-radar / comment-draft)

- `deploy/personas/mm/` — Marketing Mentions: soft-mention, **외부 게시 금지**.
- What/where: tenant `$path/.factory/marketing.yaml` (`sites`, `keywords`, `tone`, `product_mention`, `must_avoid`). Missing → skip.
- How: `topic-radar` (public web search + `<!-- mm-radar:… -->` dedupe) → `comment-draft` (2–5 sentence draft on factory ticket only).
- `sites-guide.md` P0/P1/P2는 추천 힌트(정본 아님). 키워드/사이트 하드코딩·자동 게시·스크래퍼 Non-goal.
