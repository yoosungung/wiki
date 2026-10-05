---
id: inbox-qa-2026-10-05-qa-bulk-weekly
agent: qa
ticket_id: null
updated: 2026-10-05
status: inbox
sources:
  - schedule:qa-bulk-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
  - wiki/Engineering/AI-Native-Engineering/Soft-Gate-Exit-Code-vs-Pass-Rate.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# qa-bulk-weekly 2026-10-05

Registry sync + `bulk_api` / `opik` gates. Failures → New NF only; missing keys → skip (no NF). Long-run would use `nf-progress:`.

## synced

- `repo_id=sw-factory` **skip sync** — dirty working tree (`package.json`/`package-lock.json` add `@rollup/rollup-linux-arm64-gnu`); no stash; HEAD=`690c7265f701430e425745b2c0814ed8f2205da8` behind origin/main by 59; path=`deploy/local/.local-data/workspaces/qa/repos/sw-factory` project=`8a927848-4411-42a8-8508-f7b8efb3ec60`
- `repo_id=crewrp` sha=`84d8b4b5689500cf9d7f38b05d6ead9c49b62c9d` path=`deploy/local/.local-data/workspaces/qa/repos/crewrp` project=`525d05c5-ef00-4ff6-917d-3632edc6493e`
- `repo_id=uni-tutor` sha=`cc3b4c961181d23a5be472588cc40af709f7a49d` path=`deploy/local/.local-data/workspaces/qa/repos/uni-tutor` project=`1fc753f5-8cd8-4e01-af7a-39a798895904`

## bulk_api / opik results

| repo_id | bulk_api | opik | reason |
| :--- | :--- | :--- | :--- |
| sw-factory | skip | skip | no `.factory/quality.yaml` (and sync dirty) |
| crewrp | skip | skip | no `.factory/quality.yaml` |
| uni-tutor | skip | skip | no `.factory/quality.yaml` |

## factory smoke (bulk-api-probe)

- `GET https://factory.askwho.net/api/health` → **200** `{"ok":true,"service":"sw-factory-workers"}` — `qa: pass`
- Auth session `qa@example.com` ok (me 200)

## closeout

- New NF tickets: **0**
- Long-run / `nf-progress:`: N/A (no `opik.long_run` / command started)
- Active ticket outcome comment: N/A — ticketless schedule; orphan Outcome forbidden
- `nl2sql` has `opik:` in its quality.yaml but is **not** in this persona `clients-repos-registry.json` → out of scope
- tenant_cd Done gate: N/A for this NF run (no feature Done)
- `wiki: inbox/qa/2026-10-05-qa-bulk-weekly.md`
