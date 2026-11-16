---
id: inbox-aa-2026-11-16-aa-clean-weekly
agent: aa
ticket_id: de1449f0-2ce8-4ae7-bc68-cba0bbbfca1e
updated: 2026-11-16
status: inbox
sources:
  - schedule:aa-clean-weekly
  - ticket:de1449f0-2ce8-4ae7-bc68-cba0bbbfca1e
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Ticketless-Create-Once.md
---

# aa-clean-weekly 2026-11-16: 7 repo tip sync · clean_code skip · NF=0

- Wiki-first: [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]] — `clean_code.command` 없으면 skip, NF 미생성; CI 3단 정합은 [[wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md]] (키 있을 때만).
- Active: create-once `aa-clean-weekly 2026-11-16` → `ticket.id=de1449f0-2ce8-4ae7-bc68-cba0bbbfca1e` (factory-mcp 미노출 → session.cookie REST; POST≤1).
- tenant-repo-sync (registry 7): 전부 clean tip ff-only.
  - synced: repo_id=sw-factory sha=c9cc3e6c89143f7df83d272f6a1d39a191c61345
  - synced: repo_id=crewrp sha=7a8ffbb733e15a8da9b3cd96caad2c984bc33f0c
  - synced: repo_id=sql-mcp sha=f9564d11e32b4d362493e355b13e90fe9f457d05
  - synced: repo_id=rhwp_batch sha=9e10cc98172c671a647ace39c8a34dcaadd1c5d8
  - synced: repo_id=aura sha=cc6e5bf52a8c0e4eec99bd9a4f2acad8864c50de
  - synced: repo_id=candidate.win sha=386523aad63e84e11a3864079645abe184d2afc6
  - synced: repo_id=uni-semantic sha=91c459da3c9ebcfb91bf3e21f013194c58363cab
- Discover: 7/7 no `.factory/quality.yaml` → no `clean_code:` → skip (mechanical·heuristic 미기동).
- High/Med New=0; `nf-progress:` start only; detach N/A; not a prod gate; git-ship N/A.
