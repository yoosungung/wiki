---
id: inbox-qa-qa-bulk-weekly-2026-10-12
agent: qa
ticket_id: schedule:qa-bulk-weekly
updated: 2026-10-12
status: inbox
sources:
  - schedule:qa-bulk-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Repo-Sync-Dirty-Tree-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
  - https://factory.askwho.net/api/health
---

# qa-bulk-weekly 2026-10-12

Registry: sw-factory / crewrp / uni-tutor (persona `clients-repos-registry.json`).

## Sync

| repo | result | HEAD |
| :--- | :--- | :--- |
| crewrp | ff-only sync OK | `aa26396` (main=origin/main) |
| uni-tutor | already tip | `73178e8` |
| sw-factory | **skip sync** — dirty `package.json`/`package-lock.json` (behind origin/main by 66); no stash/reset | `690c726` |

## Gates (`.factory/quality.yaml`)

| repo | bulk_api | opik |
| :--- | :--- | :--- |
| crewrp | skip — no `.factory/quality.yaml` on tip | skip |
| uni-tutor | skip — no `.factory/quality.yaml` on tip | skip |
| sw-factory | skip — no `.factory/quality.yaml` on origin/main tip (dirty sync skip; tip also has no file) | skip |

NF New tickets: **0** (skip ≠ fail).

## Factory smoke (`bulk-api-probe`)

- `GET https://factory.askwho.net/api/health` → **200** `{"ok":true,"service":"sw-factory-workers"}`
- `qa: pass`

## Notes

- factory MCP namespace absent in this Cursor session (`mcp.json` points at Docker `/app/.../stdio.ts`); used REST + `lt_session` cookie.
- Active `ticket_id` 없음 → orphan Outcome/`add_comment` 금지 ([[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]).
- Long-run / `nf-progress:` N/A — no long command started.
