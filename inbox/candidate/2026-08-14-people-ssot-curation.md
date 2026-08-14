---
id: inbox-candidate-2026-08-14-people-ssot-curation
agent: candidate
ticket_id: 797
updated: 2026-08-14
status: inbox
sources:
  - ticket:797
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
---

# People stub promote hold axes

- Promote only when identity is unambiguous **and** ≥1 allowlisted official/profile URL exists (assembly.go.kr, *.go.kr, yna.co.kr, newsis.com, wikidata, etc.). Wiki-only or non-allowlisted hosts are not enough.
- Hold without promotion: school/org-as-person, role mismatch vs incumbent, reporters/citizens, homonyms, missing safe-host URL.
- Homonym trap: a safe-host URL for the **wrong** person (same name, different office) is a content-safety fail — do not attach it to promote. Example pattern: regional-coop officer vs asset-manager CEO sharing a name.
- Local unpublished Pass stack must not be ff-merged into curation; detach at origin/main, preserve the stack on a dated branch, ship curation only onto origin/main.
